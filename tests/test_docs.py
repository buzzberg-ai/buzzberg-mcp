import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_tools_md_matches_manifest():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    text = (ROOT / "TOOLS.md").read_text()
    headings = set(re.findall(r"^## ([a-z_]+)$", text, re.MULTILINE))
    expected = {tool["name"] for tool in manifest["tools"]}
    assert headings == expected


def test_prompt_cookbook_references_real_tools():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    expected = {tool["name"] for tool in manifest["tools"]}
    text = (ROOT / "PROMPTS.md").read_text()

    referenced = set(re.findall(r"`([a-z][a-z_]+)`", text))
    referenced.update(re.findall(r"`([a-z][a-z_]+)\(", text))
    tool_prefixes = ("get_", "read_", "search_", "add_", "save_")
    tool_like = {name for name in referenced if name.startswith(tool_prefixes)}

    assert tool_like <= expected


def test_setup_docs_recommend_oauth_without_breaking_personal_keys():
    readme = (ROOT / "README.md").read_text()
    install = (ROOT / "INSTALL.md").read_text()
    security = (ROOT / "SECURITY.md").read_text()

    for text in (readme, install):
        assert "https://mcp.buzzberg.ai/mcp" in text
        assert "Add custom connector" in text
        assert "OAuth client ID" in text
        assert "Existing `bzb_...` keys" in text

    assert "codex mcp login buzzberg" in readme
    assert "claude mcp add --transport http buzzberg" in install
    assert "PKCE S256" in security
    assert "coming after Buzzberg adds OAuth" not in readme


def test_no_legacy_personal_repo_references():
    forbidden = re.compile(
        "|".join(["n1" + "fan", r"github\.com/n1" + "fan", r"ghcr\.io/n1" + "fan"])
    )
    offenders = []
    for path in ROOT.rglob("*"):
        if (
            path.is_dir()
            or ".git" in path.parts
            or "__pycache__" in path.parts
            or ".pytest_cache" in path.parts
        ):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if forbidden.search(text):
            offenders.append(str(path.relative_to(ROOT)))
    assert offenders == []
