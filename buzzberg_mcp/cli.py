"""Command line interface for the Buzzberg MCP installer."""

from __future__ import annotations

import argparse
import getpass
import os
import sys
from collections.abc import Iterable
from urllib.error import URLError
from urllib.request import urlopen

from .constants import BETA_BANNER, CLIENT_CHOICES, MCP_HEALTH_URL, VERSION
from .installers import (
    InstallerError,
    checked_paths,
    detect_clients,
    install_client,
)

DRY_RUN_PLACEHOLDER_KEY = "bzb_dry_run_placeholder_not_a_real_key"


def _print_warning() -> None:
    print(
        "WARNING: Your config now contains a Bearer secret. Treat it like a password. "
        "Exclude config and *.buzzberg.bak.* from support bundles, log uploads, and screen-shares."
    )


def _key_from_args(args: argparse.Namespace) -> str:
    if args.dry_run and not args.key_stdin and not os.environ.get("BUZZBERG_MCP_API_KEY"):
        return DRY_RUN_PLACEHOLDER_KEY
    if args.key_stdin:
        key = sys.stdin.readline().strip()
        if not key:
            raise InstallerError("--key-stdin was set, but stdin was empty.")
        return key
    env_key = os.environ.get("BUZZBERG_MCP_API_KEY", "").strip()
    if env_key:
        print("Using BUZZBERG_MCP_API_KEY from environment.")
        return env_key
    key = getpass.getpass("BUZZBERG_MCP_API_KEY (input hidden): ").strip()
    if not key:
        raise InstallerError("No API key provided.")
    return key


def _confirm(prompt: str, *, yes: bool) -> bool:
    if yes:
        return True
    answer = input(f"{prompt} [y/N] ").strip().lower()
    return answer in {"y", "yes"}


def _selected_clients(args: argparse.Namespace) -> list[str]:
    if args.client and args.all:
        raise InstallerError("Use either --client or --all, not both.")
    if args.client:
        return [args.client]
    detected = detect_clients()
    if args.all:
        if not detected:
            paths = "\n".join(f"  - {path}" for path in checked_paths())
            raise InstallerError(f"No installed clients detected. Checked:\n{paths}")
        clients = [item.name for item in detected]
        print("Detected clients:")
        for item in detected:
            location = f" ({item.path})" if item.path else ""
            print(f"  - {item.name}: {item.reason}{location}")
        if not _confirm(f"Configure all {len(clients)} detected clients?", yes=args.yes):
            raise InstallerError("Aborted.")
        return clients
    if not detected:
        paths = "\n".join(f"  - {path}" for path in checked_paths())
        raise InstallerError(
            "No installed clients detected. Use --client claude-desktop to create a config.\n"
            f"Checked:\n{paths}"
        )
    print("Detected clients:")
    for item in detected:
        location = f" ({item.path})" if item.path else ""
        print(f"  - {item.name}: {item.reason}{location}")
    if not _confirm(f"Configure these {len(detected)} clients?", yes=args.yes):
        raise InstallerError("Aborted.")
    return [item.name for item in detected]


def _run_setup(args: argparse.Namespace) -> int:
    print(BETA_BANNER)
    clients = _selected_clients(args)
    api_key = _key_from_args(args)
    failures = 0
    for client in clients:
        try:
            result = install_client(client, api_key, dry_run=args.dry_run, force=args.force)
        except (InstallerError, OSError) as exc:
            failures += 1
            print(f"[{client}] ERROR: {exc}", file=sys.stderr)
            continue
        label = f"[{client}]"
        if result.dry_run:
            print(f"{label} dry-run")
            if result.path:
                print(result.diff.rstrip() or "No changes.")
            elif result.message:
                print(result.message)
            continue
        print(f"{label} configured.")
        if result.path:
            print(f"  config: {result.path}")
        if result.backup_path:
            print(f"  backup: {result.backup_path}")
        if result.message:
            _print_warning()
    return 1 if failures else 0


def _run_health() -> int:
    try:
        with urlopen(MCP_HEALTH_URL, timeout=10) as response:  # noqa: S310 - fixed HTTPS URL
            body = response.read().decode("utf-8", errors="replace")
            print(body)
            return 0 if response.status == 200 else 1
    except URLError as exc:
        print(f"Health check failed: {exc}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="buzzberg-mcp")
    sub = parser.add_subparsers(dest="command")

    setup = sub.add_parser("setup", help="Configure MCP clients")
    setup.add_argument("--client", choices=CLIENT_CHOICES)
    setup.add_argument("--all", action="store_true", help="Configure all detected clients")
    setup.add_argument("--yes", action="store_true", help="Accept interactive confirmations")
    setup.add_argument(
        "--dry-run",
        action="store_true",
        help="Show redacted changes without writing",
    )
    setup.add_argument("--force", action="store_true", help="Overwrite an existing Buzzberg entry")
    setup.add_argument("--key-stdin", action="store_true", help="Read the MCP key from stdin")

    sub.add_parser("version", help="Print package version")
    sub.add_parser("health", help="Check the Buzzberg MCP health endpoint")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.command == "setup":
        try:
            return _run_setup(args)
        except InstallerError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1
    if args.command == "version":
        print(VERSION)
        return 0
    if args.command == "health":
        return _run_health()
    parser.print_help()
    return 0
