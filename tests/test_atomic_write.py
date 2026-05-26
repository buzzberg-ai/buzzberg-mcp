import json
import platform

from buzzberg_mcp import installers


def test_atomic_write_replaces_with_valid_json(monkeypatch, tmp_path):
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setattr(platform, "system", lambda: "Linux")
    path = installers.claude_desktop_config_path()
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"mcpServers": {}, "keep": ["a"]}))

    installers.install_client("claude-desktop", "bzb_secret", force=True)

    data = json.loads(path.read_text())
    assert data["keep"] == ["a"]
    assert data["mcpServers"]["buzzberg"]["url"].startswith("https://")
    assert not list(path.parent.glob("*.tmp"))
