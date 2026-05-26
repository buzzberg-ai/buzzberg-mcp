"""Client config writers for Buzzberg MCP.

The module is stdlib-only by design. It modifies only the Buzzberg MCP entry,
preserves unknown JSON fields, redacts tokens in dry-runs, and writes atomically.
"""

from __future__ import annotations

import difflib
import hashlib
import json
import os
import platform
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .constants import AUTH_HEADER, MCP_URL, SERVER_NAME


class InstallerError(RuntimeError):
    """Raised when a client config cannot be safely updated."""


@dataclass(frozen=True)
class InstallResult:
    client: str
    path: Path | None
    changed: bool
    dry_run: bool
    backup_path: Path | None = None
    message: str = ""
    diff: str = ""


@dataclass(frozen=True)
class DetectedClient:
    name: str
    path: Path | None
    reason: str


def redact_key(api_key: str) -> str:
    digest = hashlib.sha256(api_key.encode("utf-8")).hexdigest()[:6]
    return f"bzb_***REDACTED*** (k1: {digest})"


def server_entry(api_key: str) -> dict[str, Any]:
    return {
        "url": MCP_URL,
        "headers": {AUTH_HEADER: f"Bearer {api_key}"},
    }


def redacted_server_entry(api_key: str) -> dict[str, Any]:
    return {
        "url": MCP_URL,
        "headers": {AUTH_HEADER: f"Bearer {redact_key(api_key)}"},
    }


def _home() -> Path:
    return Path.home()


def _appdata() -> Path:
    raw = os.environ.get("APPDATA")
    return Path(raw) if raw else _home() / "AppData" / "Roaming"


def _code_config_root() -> Path:
    system = platform.system()
    if system == "Darwin":
        return _home() / "Library" / "Application Support" / "Code"
    if system == "Windows":
        return _appdata() / "Code"
    return _home() / ".config" / "Code"


def claude_desktop_config_path() -> Path:
    system = platform.system()
    if system == "Darwin":
        return _home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    if system == "Windows":
        return _appdata() / "Claude" / "claude_desktop_config.json"
    return _home() / ".config" / "Claude" / "claude_desktop_config.json"


def cursor_config_path() -> Path:
    return _home() / ".cursor" / "mcp.json"


def cline_config_path() -> Path:
    return (
        _code_config_root()
        / "User"
        / "globalStorage"
        / "saoudrizwan.claude-dev"
        / "settings"
        / "cline_mcp_settings.json"
    )


def continue_config_path() -> Path:
    return _home() / ".continue" / "config.json"


def client_config_path(client: str) -> Path | None:
    if client == "claude-desktop":
        return claude_desktop_config_path()
    if client == "cursor":
        return cursor_config_path()
    if client == "cline":
        return cline_config_path()
    if client == "continue":
        return continue_config_path()
    if client == "claude-code":
        return None
    raise InstallerError(f"Unsupported client: {client}")


def detect_clients() -> list[DetectedClient]:
    detected: list[DetectedClient] = []
    for client in ("claude-desktop", "cursor", "cline", "continue"):
        path = client_config_path(client)
        if path and (path.exists() or path.parent.exists()):
            detected.append(DetectedClient(client, path, "config path exists"))
    if shutil.which("claude"):
        detected.append(DetectedClient("claude-code", None, "`claude` command found"))
    return detected


def checked_paths() -> list[Path]:
    return [
        path
        for client in ("claude-desktop", "cursor", "cline", "continue")
        if (path := client_config_path(client)) is not None
    ]


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise InstallerError(f"Malformed JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise InstallerError(f"Expected top-level JSON object in {path}")
    return data


def _json_text(data: dict[str, Any]) -> str:
    return json.dumps(data, indent=2, sort_keys=False) + "\n"


def _chmod_600(path: Path) -> None:
    if os.name == "posix":
        try:
            path.chmod(0o600)
        except OSError:
            # Best effort: the caller still reports a successful write.
            return


def _backup_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_path = path.with_name(f"{path.name}.buzzberg.bak.{timestamp}")
    backup_path.write_bytes(path.read_bytes())
    _chmod_600(backup_path)
    return backup_path


def _atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(_json_text(data))
            fh.flush()
            os.fsync(fh.fileno())
        _chmod_600(tmp_path)
        os.replace(tmp_path, path)
        _chmod_600(path)
    except Exception:
        try:
            tmp_path.unlink(missing_ok=True)
        finally:
            raise


def _unified_diff(before: dict[str, Any], after: dict[str, Any], path: Path) -> str:
    before_lines = _json_text(before).splitlines(keepends=True)
    after_lines = _json_text(after).splitlines(keepends=True)
    return "".join(
        difflib.unified_diff(
            before_lines,
            after_lines,
            fromfile=f"{path} (before)",
            tofile=f"{path} (after)",
        )
    )


def _install_mcp_servers_style(
    client: str,
    path: Path,
    api_key: str,
    *,
    dry_run: bool,
    force: bool,
) -> InstallResult:
    before = _load_json(path)
    after = json.loads(json.dumps(before))
    servers = after.setdefault("mcpServers", {})
    if not isinstance(servers, dict):
        raise InstallerError(f"`mcpServers` must be an object in {path}")
    if SERVER_NAME in servers and not force and not dry_run:
        raise InstallerError(f"{client} already has a Buzzberg entry. Re-run with --force.")
    servers[SERVER_NAME] = redacted_server_entry(api_key) if dry_run else server_entry(api_key)
    diff = _unified_diff(before, after, path)
    if dry_run:
        return InstallResult(client, path, before != after, True, diff=diff)
    backup = _backup_existing(path)
    _atomic_write_json(path, after)
    return InstallResult(
        client,
        path,
        before != after,
        False,
        backup_path=backup,
        message="Config now contains a Bearer secret. Treat it like a password.",
    )


def _install_continue(path: Path, api_key: str, *, dry_run: bool, force: bool) -> InstallResult:
    before = _load_json(path)
    after = json.loads(json.dumps(before))
    experimental = after.setdefault("experimental", {})
    if not isinstance(experimental, dict):
        raise InstallerError(f"`experimental` must be an object in {path}")
    servers = experimental.setdefault("modelContextProtocolServers", [])
    if not isinstance(servers, list):
        raise InstallerError(f"`experimental.modelContextProtocolServers` must be a list in {path}")
    entry = {
        "name": SERVER_NAME,
        "transport": {
            "type": "sse",
            "url": MCP_URL,
            "headers": {
                AUTH_HEADER: f"Bearer {redact_key(api_key) if dry_run else api_key}",
            },
        },
    }
    existing_idx = next(
        (
            idx
            for idx, item in enumerate(servers)
            if isinstance(item, dict) and item.get("name") == SERVER_NAME
        ),
        None,
    )
    if existing_idx is not None and not force and not dry_run:
        raise InstallerError("Continue.dev already has a Buzzberg entry. Re-run with --force.")
    if existing_idx is None:
        servers.append(entry)
    else:
        servers[existing_idx] = entry
    diff = _unified_diff(before, after, path)
    if dry_run:
        return InstallResult("continue", path, before != after, True, diff=diff)
    backup = _backup_existing(path)
    _atomic_write_json(path, after)
    return InstallResult(
        "continue",
        path,
        before != after,
        False,
        backup_path=backup,
        message="Config now contains a Bearer secret. Treat it like a password.",
    )


def install_client(
    client: str,
    api_key: str,
    *,
    dry_run: bool = False,
    force: bool = False,
) -> InstallResult:
    if client == "claude-code":
        command = [
            "claude",
            "mcp",
            "add",
            "--transport",
            "sse",
            SERVER_NAME,
            MCP_URL,
            "--header",
            f"{AUTH_HEADER}: Bearer {api_key}",
        ]
        redacted = command[:-1] + [f"{AUTH_HEADER}: Bearer {redact_key(api_key)}"]
        if dry_run:
            return InstallResult(client, None, True, True, message=" ".join(redacted))
        subprocess.run(command, check=True)
        return InstallResult(
            client,
            None,
            True,
            False,
            message="Claude Code configured. Config now contains a Bearer secret.",
        )

    path = client_config_path(client)
    if path is None:
        raise InstallerError(f"No config path for {client}")
    if client == "continue":
        return _install_continue(path, api_key, dry_run=dry_run, force=force)
    return _install_mcp_servers_style(client, path, api_key, dry_run=dry_run, force=force)
