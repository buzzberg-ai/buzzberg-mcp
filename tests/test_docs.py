import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_earnings_contract_routing_and_examples():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tool = next(t for t in manifest["tools"] if t["name"] == "get_earnings_calls_summary")
    assert tool["scope"] == "read"
    assert tool["returns"] == "EarningsSummaryResult"
    assert [p["name"] for p in tool["parameters"]] == [
        "window", "company", "company_scope", "as_of", "timezone", "cursor",
    ]
    example = (ROOT / "examples/get_earnings_calls_summary.md").read_text()
    for block in re.findall(r"```json\n(.*?)\n```", example, re.S):
        assert json.loads(block)["window"] in {"7d", "yesterday", "30d"}
    assert "Call / Companies mentioned / Context" in example
    assert "other issuers' calls" in example
    assert "analysis_instruction" in example


def test_tools_md_matches_manifest():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    text = (ROOT / "TOOLS.md").read_text()
    headings = set(re.findall(r"^## ([a-z0-9_]+)$", text, re.MULTILINE))
    expected = {tool["name"] for tool in manifest["tools"]}
    assert headings == expected
    for tool in manifest["tools"]:
        section = text.split("## " + tool["name"] + "\n", 1)[1].split("\n## ", 1)[0]
        inputs = section.split("**Inputs:**", 1)[1].split("**Example prompt:**", 1)[0]
        documented = re.findall(r"^- `([a-z_]+)` \(", inputs, re.M)
        assert documented == [param["name"] for param in tool["parameters"]], tool["name"]


def test_pair_history_is_bounded_and_aggregate_only():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text(encoding="utf-8"))
    tool = next(t for t in manifest["tools"] if t["name"] == "get_speaker_ticker_history")
    params = {p["name"]: p for p in tool["parameters"]}
    assert params["days"]["default"] == 90
    example = (ROOT / "examples/get_speaker_ticker_history.md").read_text(encoding="utf-8")
    assert '"days": 90' in example
    assert "100 admitted requests per rolling 30 days" in example
    assert "history_monthly_quota_exceeded" in example
    assert "latest_direction,idea_ids" not in example
    assert "version 2.0.0" in example


def test_unified_lens_preserves_ticker_focus_and_shared_account_quota():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text(encoding="utf-8"))
    tool = next(t for t in manifest["tools"] if t["name"] == "get_speaker_lens")
    params = {p["name"]: p for p in tool["parameters"]}
    assert params["history_days"]["default"] == 90
    assert {p["name"] for p in tool["parameters"] if p["required"]} == {"speaker"}
    assert params["sections"]["default"] == "auto"
    assert params["question"]["default"] == ""
    assert params["recent_days"]["default"] == 90
    assert params["recent_limit"]["default"] == 20
    assert "get_speaker_lens_context" not in {t["name"] for t in manifest["tools"]}
    example = (ROOT / "examples/get_speaker_lens.md").read_text(encoding="utf-8")
    assert '"history_days": 90' in example
    assert "100 admitted requests per rolling 30 days" in example
    assert "At most 20 individual ideas" in example
    assert "omitting individual idea IDs" in example
    assert "speaker_lens_monthly_quota_exceeded" in example
    assert "outstanding calls to both former lens commands" in example
    assert "Selection is strict" in example


def test_speaker_history_launch_contract_and_examples():
    manifest = json.loads((ROOT / 'tools_manifest.json').read_text())
    tool = next(item for item in manifest['tools'] if item['name'] == 'get_speaker_trade_ideas')
    params = {item['name']: item for item in tool['parameters']}
    assert tuple(params) == ('speaker_name', 'ticker', 'direction', 'source_type', 'signal',
                             'sort', 'days', 'include_thesis', 'cursor')
    assert params['days']['default'] == 30
    assert params['days']['type'] == 'Literal[1, 7, 15, 30]'
    assert params['include_thesis']['default'] is True
    assert tool['returns'] == 'CallToolResult'
    text = (ROOT / 'examples/get_speaker_trade_ideas.md').read_text(encoding='utf-8')
    for raw in re.findall(r'```json\n(.*?)\n```', text, re.S):
        arguments = json.loads(raw)
        assert 'limit' not in arguments and 'max_per_day' not in arguments
        if 'cursor' in arguments:
            assert set(arguments) == {'speaker_name', 'cursor'}
        else:
            assert arguments.get('days', 30) in (1, 7, 15, 30)
    assert '20 new requests per rolling 24 hours' in text


def test_speaker_profile_publishes_report_default_and_explicit_raw_data():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tool = next(t for t in manifest["tools"] if t["name"] == "get_speaker_profile")
    assert tool["scope"] == "read"
    assert tool["returns"] == "SpeakerProfileResult"
    params = {p["name"]: p for p in tool["parameters"]}
    assert tuple(params) == ("speaker_name", "mode", "sections", "days")
    assert params["mode"]["default"] == "report"
    assert params["sections"]["default"] is None
    assert params["days"]["default"] == 0
    text = (ROOT / "TOOLS.md").read_text()
    section = text.split("## get_speaker_profile\n", 1)[1].split("\n## ", 1)[0]
    assert "2.5.0" in section and "Credibility is no longer returned" in section
    assert "at most 15 rows" in section
    example = (ROOT / "examples/get_speaker_profile.md").read_text()
    assert 'mode="data", sections=["all"]' in example
    assert "Data mode omits `analysis_instruction`" in example
    assert "lifetime first LONG/SHORT/AVOID" in example
    assert "history_limit_exceeded" in example
    assert "Direction, L/S/A/N, First call, First call price," in example
    assert "themes outside the top 15" in example
    assert "Statistics is first and initially selected" in example
    assert "7/30/90/180/360-day" in example
    assert 'sections=["statistics"]' in example
    assert '"market_view", "view_history", "theme_theses"' in example
    assert "not extra tabs" in example


def test_personal_feed_tools_publish_private_read_scope_and_portfolio_chain():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tools = {t["name"]: t for t in manifest["tools"]}
    assert len(tools) == 31
    assert "get_recent_source_text" not in tools
    expected = {
        "get_my_feeds": ["feed_type", "limit", "after_id", "feed_id", "name", "include_members"],
    }
    text = (ROOT / "TOOLS.md").read_text()
    for name, params in expected.items():
        assert tools[name]["scope"] == "read"
        assert tools[name]["returns"] == "PersonalFeedsResult"
        assert [p["name"] for p in tools[name]["parameters"]] == params
        section = text.split("## " + name + "\n", 1)[1].split("\n## ", 1)[0]
        assert "Private feeds of the authenticated Buzzberg account only" in section
        example = (ROOT / "examples" / (name + ".md")).read_text()
        assert "portfolio_tickers" in example
        assert "get_portfolio_summary" in example
    assert "100 selected tickers" in tools["get_portfolio_summary"]["summary"]
    assert "100 distinct" in (ROOT / "examples/get_portfolio_summary.md").read_text()
    assert "get_my_feed" not in tools
    params = {p["name"]: p for p in tools["get_my_feeds"]["parameters"]}
    assert params["include_members"]["default"] is True
    assert params["feed_id"]["default"] is None
    listing = (ROOT / "examples/get_my_feeds.md").read_text()
    assert "all_members_returned=true" in listing
    assert "members_included=false" in listing
    assert "initialization instructions" in listing
    assert "combine with AND" in listing


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
    assert parameters["limit"]["default"] == 200
    assert parameters["offset"]["type"] == "int | None"
    assert parameters["offset"]["default"] is None
    assert recent["returns"] == "GroupedRecentIdeasColumnarPage"

    tools_md = (ROOT / "TOOLS.md").read_text()
    section = tools_md.split("## get_recent_idea_candidates", 1)[1].split("\n## ", 1)[0]
    assert "`cursor`" in section
    assert "deprecated transition only" in section
    assert "source-specific confidence is intentionally absent" in section
    assert "Use stored confidence" not in section


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
    normalized_example = " ".join(example.split())

    assert "Buzzberg exposes 31 tools" in readme
    assert "get_recent_idea_candidates(window=\"12h\"" in prompts
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
    assert "No thesis is shortened" in example
    assert "independent corroboration" in readme
    assert "not a score or rejection" in readme
    assert "Current price is the freshest stored Buzzberg" in example
    assert "stale `tools/list` metadata" in normalized_example
    assert "idea_id, published_at, direction, signal, entry_price" in example
    assert "Generic `confidence` is intentionally absent" in example
    assert "Stored confidence" not in example
    exact_window = prompts.split(
        "## Strongest Ideas From an Exact Recent Window", 1
    )[1].split("\n## ", 1)[0]
    assert "Stored confidence" not in exact_window


def test_grouped_recent_idea_workflow_is_public_and_cursor_complete():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    grouped = next(
        tool for tool in manifest["tools"]
        if tool["name"] == "get_recent_idea_candidates"
    )
    details = next(
        tool for tool in manifest["tools"]
        if tool["name"] == "get_trade_idea_details"
    )
    parameters = {param["name"]: param for param in grouped["parameters"]}

    assert tuple(parameters) == (
        "window", "cursor", "as_of", "source_type",
        "direction", "delivery", "limit", "offset",
    )
    assert grouped["returns"] == "GroupedRecentIdeasColumnarPage"
    assert details["returns"] == "TradeIdeaDetailsBatch"
    assert parameters["limit"]["default"] == 200

    tools_md = (ROOT / "TOOLS.md").read_text()
    prompts = (ROOT / "PROMPTS.md").read_text()
    grouped_example = (ROOT / "examples/get_recent_idea_candidates.md").read_text()
    detail_example = (ROOT / "examples/get_trade_idea_details.md").read_text()
    recent_tool_docs = tools_md.split(
        "## get_recent_idea_candidates", 1
    )[1].split("\n## ", 1)[0]
    exact_window_prompt = prompts.split(
        "## Strongest Ideas From an Exact Recent Window", 1
    )[1].split("\n## ", 1)[0]

    assert "whole-ticker groups" in tools_md
    assert "exact `1h`, `6h`, `12h`, `24h`, or `1d`" in recent_tool_docs
    assert "`3d` and `7d` are rejected" in recent_tool_docs
    assert "ticker_group_columns" in prompts
    assert "exact pagination.next_cursor" in prompts
    assert "Requests for\n  `3d` or `7d` are rejected" in exact_window_prompt
    assert "500-row review ceiling" not in exact_window_prompt
    assert "full thesis" in grouped_example
    assert "independent directional speakers" in grouped_example
    assert "accepts only `1h`, `6h`, `12h`, `24h`, or `1d`" in grouped_example
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


def test_portfolio_summary_is_a_separate_complete_daily_contract():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tool = next(t for t in manifest["tools"] if t["name"] == "get_portfolio_summary")
    assert tool["scope"] == "read"
    assert tool["returns"] == "PortfolioSummaryResult"
    assert [p["name"] for p in tool["parameters"]] == ["tickers", "source_type"]
    assert tool["parameters"][0]["required"] is True
    example = (ROOT / "examples/get_portfolio_summary.md").read_text()
    assert "requires_narrowing" in example
    assert "every full LONG/SHORT/AVOID thesis" in example
    assert "every qualifying ticker once" in example
    assert "`report_eligible=true` in BOTH the table and details" in example
    assert "coverage.all_sources_available" in example
    assert "shared earnings_calls list" in example
    assert "promotion/affiliation bias" in example
    assert "new stored SEC 13F disclosures remain included" in example
    assert "no table or details" in example
    assert "Report format is 2.0.1" in example
    assert "exact English title `Buzzberg Portfolio Update` in every language" in example
    assert "Ticker | L/S/A/N | Mentions · 24h" in example
    assert "`mention_author_counts.non_directional`, not neutral sentiment alone" in example
    assert "get_recent_ideas_summary" in example

def test_price_service_is_retired_and_context_is_database_only():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    assert "get_price" not in {tool["name"] for tool in manifest["tools"]}
    assert not (ROOT / "examples/get_price.md").exists()
    for name in ("README.md", "TOOLS.md",
                 "examples/get_tickers_overview.md", "examples/get_speaker_lens.md"):
        text = (ROOT / name).read_text()
        assert "persisted database" in text or "market-data provider" in text


def test_timeseries_chart_contract_has_complete_days_and_summary():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tool = next(t for t in manifest["tools"] if t["name"] == "get_ticker_timeseries")
    params = {p["name"]: p for p in tool["parameters"]}
    assert params["include_today"]["default"] is True
    assert params["trim_empty_prefix"]["default"] is True
    example = (ROOT / "examples/get_ticker_timeseries.md").read_text()
    arguments = json.loads(re.search(r"```json\n(.*?)\n```", example, re.S).group(1))
    assert arguments == {
        "ticker": "SIVE", "days": 180, "trim_empty_prefix": False, "include_today": False,
    }
    for label in ("Total mentions", "Average sentiment", "Price change"):
        assert label in example
    assert "do not invent prices" in example
    assert "missing-day tooltip" in example


def test_earnings_export_limits_are_documented():
    example = (ROOT / "examples/get_earnings_calls_summary.md").read_text(encoding="utf-8")
    for marker in ("last 90 days from now", "100 requests per rolling 30 days",
                   "at most 20 calls per page", "earnings_monthly_quota_exceeded",
                   "retry_after_seconds", "Schema 2.0.0", "incomplete"):
        assert marker in example
    for block in re.findall(r"```json\n(.*?)\n```", example, re.S):
        assert json.loads(block).get("window") != "all"
    text = (ROOT / "TOOLS.md").read_text(encoding="utf-8")
    section = text.split("## get_earnings_calls_summary\n", 1)[1].split("\n## ", 1)[0]
    assert "100 requests per account per rolling 30 days" in section
    assert "For all NVIDIA" not in section


def test_ticker_rankings_modes_replace_both_former_commands():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text(encoding="utf-8"))
    tools = {t["name"]: t for t in manifest["tools"]}
    assert "get_most_mentioned_tickers" not in tools
    assert "get_top_sentiment_tickers" not in tools
    params = {p["name"]: p for p in tools["get_ticker_rankings"]["parameters"]}
    assert list(params) == ["mode", "days", "limit", "source_type", "min_mentions", "history"]
    assert params["mode"]["default"] == "mentions"
    assert params["min_mentions"]["default"] is None
    assert params["days"]["default"] == 1
    assert params["limit"]["default"] == 20
    example = (ROOT / "examples/get_ticker_rankings.md").read_text(encoding="utf-8")
    for expected in ('mode="bullish"', 'mode="bearish"', "first 10", "1-365", "1-50",
                     "1 for `mentions` and 3", "not LONG/SHORT", "original source bodies"):
        assert expected in example


def test_remaining_reader_groups_keep_all_modes_and_bounds():
    tools = {t["name"]: t for t in json.loads((ROOT / "tools_manifest.json").read_text())["tools"]}
    retired = {
        "get_recent_content", "get_ticker_info",
        "get_ticker_mentions", "get_ticker_youtube_research",
    }
    assert not retired.intersection(tools)
    for name in retired:
        assert not (ROOT / "examples" / (name + ".md")).exists()
    for name in ("search_content", "search_youtube_research"):
        params = {p["name"]: p for p in tools[name]["parameters"]}
        assert not params["query"]["required"] and params["query"]["default"] == ""
    overview = {p["name"]: p for p in tools["get_tickers_overview"]["parameters"]}
    assert overview["view"]["default"] == "overview"
    assert overview["days"]["default"] is None
    text = (ROOT / "examples/get_tickers_overview.md").read_text()
    assert 'view="details"' in text and 'view="mentions"' in text
    assert "exactly one input" in text and "reject days" in text
    text = (ROOT / "examples/search_content.md").read_text()
    assert "no age" in text and "30" in text and "365" in text
    text = (ROOT / "examples/search_youtube_research.md").read_text()
    assert 'search_youtube_research(ticker="MU"' in text
    assert "seven-day and twenty-note caps" in text


def test_ticker_deep_dive_is_one_call_with_bounded_report_contract():
    manifest = json.loads((ROOT / "tools_manifest.json").read_text())
    tool = next(t for t in manifest["tools"] if t["name"] == "get_ticker_deep_dive")
    assert [p["name"] for p in tool["parameters"]] == ["ticker", "mode"]
    assert tool["parameters"][1]["default"] == "report"
    example = (ROOT / "examples/get_ticker_deep_dive.md").read_text()
    assert "read_ticker_content" in example and "100 combined" in example
    assert "90,000" in example and "YTD" in example
    session = (ROOT / "sessions/ticker-deep-dive.md").read_text()
    assert "get_ticker_deep_dive" in session
    assert "get_tickers_overview(" not in session
    assert "get_sentiment(" not in session


def test_thirteenf_tools_publish_dated_read_only_contracts():
    tools = {t['name']: t for t in json.loads((ROOT / 'tools_manifest.json').read_text())['tools']}
    expected = {
        'get_13f_funds': ['period', 'include_consensus'],
        'get_13f_holdings': ['fund', 'report_date', 'view', 'ticker', 'limit', 'offset', 'snapshot_version'],
        'get_13f_stock_ownership': ['ticker', 'quarters', 'limit', 'offset', 'snapshot_version'],
    }
    for name, parameters in expected.items():
        assert tools[name]['scope'] == 'read'
        assert [p['name'] for p in tools[name]['parameters']] == parameters
        example = (ROOT / 'examples' / (name + '.md')).read_text()
        assert 'disclosed' in example and 'not' in example
    assert '13F' in (ROOT / 'examples/get_ticker_deep_dive.md').read_text()
