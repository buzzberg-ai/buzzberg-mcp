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


def test_recent_candidate_manifest_uses_cursor_pagination():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    recent = next(
        tool for tool in manifest["tools"]
        if tool["name"] == "get_recent_idea_candidates"
    )
    parameters = {param["name"]: param for param in recent["parameters"]}
    assert tuple(parameters) == (
        "window", "cursor", "as_of", "source_type",
        "direction", "delivery", "limit", "offset",
    )
    assert parameters["cursor"]["default"] == ""
    assert parameters["as_of"]["default"] == ""
    assert parameters["delivery"]["default"] == "auto"
    assert parameters["limit"]["default"] == 500
    assert parameters["offset"]["type"] == "int | None"
    assert parameters["offset"]["default"] is None
    assert recent["returns"] == "RecentIdeaCandidatesColumnarPage"

    tools_md = (ROOT / "TOOLS.md").read_text()
    section = tools_md.split("## get_recent_idea_candidates", 1)[1].split("\n## ", 1)[0]
    assert "`cursor`" in section
    assert "deprecated compatibility only" in section


def test_every_manifest_tool_has_one_example_and_no_stale_examples():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    expected = {tool["name"] for tool in manifest["tools"]}
    examples = {path.stem for path in (ROOT / "examples").glob("*.md")}

    assert examples == expected


def test_prompt_cookbook_references_real_tools():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    expected = {tool["name"] for tool in manifest["tools"]}
    text = (ROOT / "PROMPTS.md").read_text()

    referenced = set(re.findall(r"`([a-z][a-z_]+)`", text))
    referenced.update(re.findall(r"`([a-z][a-z_]+)\(", text))
    tool_prefixes = ("get_", "read_", "search_", "add_", "save_")
    tool_like = {name for name in referenced if name.startswith(tool_prefixes)}

    assert tool_like <= expected


def test_exact_window_workflow_does_not_use_alpha_as_thesis_quality():
    readme = (ROOT / "README.md").read_text()
    prompts = (ROOT / "PROMPTS.md").read_text()
    example = (ROOT / "examples/get_recent_idea_candidates.md").read_text()
    normalized_prompts = " ".join(prompts.split())

    assert "Buzzberg exposes 31 tools" in readme
    assert "get_recent_ideas_by_ticker(window=\"12h\"" in prompts
    assert "pagination.next_cursor" in prompts
    assert "Do not reconstruct an offset" in prompts
    assert "Follow every next offset" not in prompts
    assert "Do not rank by Alpha score" in normalized_prompts
    assert "professional role" in prompts
    assert "repeated promotion" in prompts
    assert "issuer conflicts" in prompts
    assert "### N. TICKER — **LONG/SHORT**" in prompts
    assert "one concise saved Buzzberg entry price" in prompts
    assert "get_ticker_timeseries(ticker, days=60)" in prompts
    assert "fewer than 6 non-empty closes" in prompts
    assert "fewer than 22" in prompts
    assert "targeted ticker+speaker lookup" in prompts
    assert "last complete close strictly before the idea" in prompts
    assert "Extended before call" in prompts
    assert "Repeat after run-up" in prompts
    assert "Company-specific selloff" in prompts
    assert "does not expose volume" in prompts
    assert "maximum 2-3 professional but plain-language sentences" in prompts
    assert "Speakers / bias" in prompts
    assert "appearances in this exact window" in prompts
    assert "110 words or fewer" in prompts
    assert "Do not add an introduction, honorable mentions" in normalized_prompts
    assert "material speakers only" in example
    assert "independent corroboration" in readme
    assert "not a score or rejection" in readme
    assert "500" in example


def test_grouped_recent_idea_workflow_is_public_and_cursor_complete():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    grouped = next(
        tool for tool in manifest["tools"]
        if tool["name"] == "get_recent_ideas_by_ticker"
    )
    details = next(
        tool for tool in manifest["tools"]
        if tool["name"] == "get_trade_idea_details"
    )
    parameters = {param["name"]: param for param in grouped["parameters"]}

    assert tuple(parameters) == (
        "window", "cursor", "as_of", "source_type",
        "direction", "delivery", "limit",
    )
    assert grouped["returns"] == "GroupedRecentIdeasColumnarPage"
    assert details["returns"] == "TradeIdeaDetailsBatch"
    assert parameters["limit"]["default"] == 200

    tools_md = (ROOT / "TOOLS.md").read_text()
    prompts = (ROOT / "PROMPTS.md").read_text()
    grouped_example = (ROOT / "examples/get_recent_ideas_by_ticker.md").read_text()
    detail_example = (ROOT / "examples/get_trade_idea_details.md").read_text()

    assert "whole-ticker groups" in tools_md
    assert "ticker_group_columns" in prompts
    assert "exact pagination.next_cursor" in prompts
    assert "full thesis" in grouped_example
    assert "independent directional speakers" in grouped_example
    assert "source URLs" in detail_example


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
