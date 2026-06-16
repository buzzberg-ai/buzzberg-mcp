import json
import platform

import pytest

from buzzberg_mcp import installers


def _set_home(monkeypatch, tmp_path, system="Linux"):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setattr(platform, "system", lambda: system)


def test_claude_desktop_install_creates_config(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    result = installers.install_client("claude-desktop", "bzb_secret", force=True)
    assert result.path is not None
    data = json.loads(result.path.read_text())
    buzzberg = data["mcpServers"]["buzzberg"]
    assert buzzberg["command"] == "npx"
    assert buzzberg["args"] == [
        "-y",
        "mcp-remote@latest",
        "https://mcp.buzzberg.ai/sse",
        "--transport",
        "sse-only",
        "--header",
        "Authorization:${AUTH_HEADER}",
    ]
    assert buzzberg["env"]["AUTH_HEADER"] == "Bearer bzb_secret"


def test_existing_unknown_fields_preserved(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    path = installers.cursor_config_path()
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {
                "custom": {"keep": True},
                "mcpServers": {"other": {"url": "https://example.com"}},
            }
        )
    )

    installers.install_client("cursor", "bzb_secret", force=True)

    data = json.loads(path.read_text())
    assert data["custom"] == {"keep": True}
    assert data["mcpServers"]["other"]["url"] == "https://example.com"
    assert data["mcpServers"]["buzzberg"]["headers"]["Authorization"] == "Bearer bzb_secret"


def test_dry_run_redacts_key_and_does_not_write(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    result = installers.install_client("claude-desktop", "bzb_secret", dry_run=True)
    assert result.path is not None
    assert not result.path.exists()
    assert "bzb_secret" not in result.diff
    assert "bzb_***REDACTED***" in result.diff


def test_backup_created_and_chmod_600(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    path = installers.cursor_config_path()
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"mcpServers": {}}))

    result = installers.install_client("cursor", "bzb_secret", force=True)

    assert result.backup_path is not None
    assert result.backup_path.exists()
    if installers.os.name == "posix":
        assert oct(result.backup_path.stat().st_mode & 0o777) == "0o600"
        assert oct(path.stat().st_mode & 0o777) == "0o600"


def test_existing_entry_requires_force(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    path = installers.cursor_config_path()
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"mcpServers": {"buzzberg": {"url": "old"}}}))
    with pytest.raises(installers.InstallerError, match="--force"):
        installers.install_client("cursor", "bzb_secret")


def test_malformed_json_aborts(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    path = installers.cursor_config_path()
    path.parent.mkdir(parents=True)
    path.write_text("{not json")
    with pytest.raises(installers.InstallerError, match="Malformed JSON"):
        installers.install_client("cursor", "bzb_secret", force=True)
    assert path.read_text() == "{not json"


def test_continue_writer_preserves_experimental_fields(monkeypatch, tmp_path):
    _set_home(monkeypatch, tmp_path)
    path = installers.continue_config_path()
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"experimental": {"other": 1}}))

    installers.install_client("continue", "bzb_secret", force=True)

    data = json.loads(path.read_text())
    assert data["experimental"]["other"] == 1
    servers = data["experimental"]["modelContextProtocolServers"]
    assert servers[0]["name"] == "buzzberg"
    assert servers[0]["transport"]["headers"]["Authorization"] == "Bearer bzb_secret"
