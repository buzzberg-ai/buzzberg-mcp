import argparse
import io

import pytest

from buzzberg_mcp import cli
from buzzberg_mcp.installers import redact_key


def _args(**kwargs):
    defaults = {
        "dry_run": False,
        "key_stdin": False,
    }
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


def test_no_key_value_flag_exists():
    parser = cli.build_parser()
    help_text = parser.format_help()
    assert "--key VALUE" not in help_text
    subparsers = next(
        action for action in parser._actions if isinstance(action, argparse._SubParsersAction)
    )
    setup_help = subparsers.choices["setup"].format_help()
    assert "--key-stdin" in setup_help
    assert "--key " not in setup_help


def test_dry_run_uses_placeholder_without_prompt(monkeypatch):
    monkeypatch.delenv("BUZZBERG_MCP_API_KEY", raising=False)
    monkeypatch.setattr(cli.getpass, "getpass", lambda _prompt: pytest.fail("should not prompt"))
    assert cli._key_from_args(_args(dry_run=True)) == cli.DRY_RUN_PLACEHOLDER_KEY


def test_env_key_source_does_not_print_key(monkeypatch, capsys):
    monkeypatch.setenv("BUZZBERG_MCP_API_KEY", "bzb_secret_value")
    assert cli._key_from_args(_args()) == "bzb_secret_value"
    out = capsys.readouterr().out
    assert "Using BUZZBERG_MCP_API_KEY from environment" in out
    assert "bzb_secret_value" not in out


def test_key_stdin(monkeypatch):
    monkeypatch.setattr(cli.sys, "stdin", io.StringIO("bzb_from_password_manager\n"))
    assert cli._key_from_args(_args(key_stdin=True)) == "bzb_from_password_manager"


def test_redact_key_is_stable_and_hides_value():
    redacted = redact_key("bzb_super_secret")
    assert "bzb_super_secret" not in redacted
    assert redacted.startswith("bzb_***REDACTED***")
    assert len(redacted.rsplit(" ", 1)[-1].strip(")")) == 6
