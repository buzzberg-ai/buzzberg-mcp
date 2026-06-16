import argparse

import pytest

from buzzberg_mcp import cli


def test_version_command(capsys):
    assert cli.main(["version"]) == 0
    assert "0.1.0b2" in capsys.readouterr().out


def test_setup_client_invokes_installer(monkeypatch, capsys):
    calls = []

    def fake_install(client, key, *, dry_run=False, force=False):
        calls.append((client, key, dry_run, force))
        return argparse.Namespace(
            client=client,
            path=None,
            changed=True,
            dry_run=dry_run,
            backup_path=None,
            message="ok",
            diff="",
        )

    monkeypatch.setattr(cli, "install_client", fake_install)
    monkeypatch.setattr(cli, "_key_from_args", lambda _args: "bzb_secret")

    assert cli.main(["setup", "--client", "cursor", "--dry-run"]) == 0
    assert calls == [("cursor", "bzb_secret", True, False)]
    assert "[cursor] dry-run" in capsys.readouterr().out


def test_setup_all_requires_confirmation(monkeypatch):
    monkeypatch.setattr(
        cli,
        "detect_clients",
        lambda: [
            argparse.Namespace(name="cursor", path=None, reason="test"),
            argparse.Namespace(name="cline", path=None, reason="test"),
        ],
    )
    monkeypatch.setattr(cli, "input", lambda _prompt: "n", raising=False)
    with pytest.raises(cli.InstallerError, match="Aborted"):
        cli._selected_clients(argparse.Namespace(client=None, all=True, yes=False))


def test_setup_all_yes(monkeypatch):
    monkeypatch.setattr(
        cli,
        "detect_clients",
        lambda: [
            argparse.Namespace(name="cursor", path=None, reason="test"),
            argparse.Namespace(name="cline", path=None, reason="test"),
        ],
    )
    selected = cli._selected_clients(argparse.Namespace(client=None, all=True, yes=True))
    assert selected == ["cursor", "cline"]
