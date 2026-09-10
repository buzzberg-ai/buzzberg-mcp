# Buzzberg MCP Tools

> Private Beta: tool names and signatures may change before broader beta.

## search_trade_ideas

Search trade ideas from Buzzberg by ticker, keywords, source, speaker, post kind, confidence, or direction.

**Inputs:**
- `ticker` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `speaker` (optional, str, default `''`)
- `post_kind` (optional, str, default `''`)
- `min_confidence` (optional, float, default `0.0`)
- `direction` (optional, str, default `''`)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `20`)
- `query` (optional, str, default `''`): explicit uppercase ticker symbols are
  exact idea-ticker filters; otherwise terms use bounded OR text search
- `cursor` (optional, str, default `''`): opaque continuation from the preceding
  page; pass it alone, its signed snapshot and original scope are authoritative

**Example prompt:**
> "Find trade ideas from research posts in the last 24h. Show ticker, speaker, thesis, direction, confidence, and which ideas deserve a deeper follow-up."

**Returns:** Markdown response from `search_trade_ideas`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/search_trade_ideas.md](examples/search_trade_ideas.md)

## get_speaker_trade_ideas

Get one author's complete 1/7/15/30-day idea history with full saved theses; 20 new requests per account per rolling 24h.

**Inputs:**
- `speaker_name` (required, str)
- `ticker` (optional, str, default `''`)
- `direction` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `signal` (optional, str, default `'all'`)
- `sort` (optional, str, default `'recent'`)
- `days` (optional, Literal[1, 7, 15, 30], default `30`)
- `include_thesis` (optional, bool, default `True`)
- `cursor` (optional, str, default `''`)

**Example prompt:**
> "Show Serenity's complete Buzzberg ideas from the last 30 days with full saved theses, direction, confidence, source and date. Follow any continuation cursor with the same speaker_name until has_more=false."

**Returns:** JSON text plus structuredContent[buzzberg_receipt] speaker schema 3.0.0; complete author history in the requested window, full saved theses by default, and account-bound continuation only on token-budget overflow.

**Scope:** Read-only, one author, authenticated registered accounts.

Available windows are **1, 7, 15 and 30 days**, default **30**. Windows
60/90/180/365 are reserved for a future paid release and currently refused;
`days=0` is refused. There is no `limit` or `max_per_day` argument.

`include_thesis=True` returns the full saved argument (short fallback only
when full text is missing). False returns the same ideas without argument
text. Ideas with no saved argument remain in both modes.

**Quota:** 20 new requests per rolling 24 hours per account, shared across
OAuth, personal keys and built-in Buzzy. Application errors/refusals do not
spend this quota; a successful empty result does. A repeated new call counts
again. General transport frequency protections still apply.

**Large responses:** Inline when the complete result fits the 900,000 estimated
token budget (serialized UTF-8 bytes / 3); otherwise follow `pagination.next_cursor`
with the same `speaker_name` and no other options. Continuations and replays do
not spend new-request quota. The snapshot expires one hour after the first
request, and replay never extends it. These are response-size estimates, not
an exact tokenizer or a promise about a client's available context.

These restrictions apply only to this command. Other MCP commands retain their
existing contracts. Refresh tool discovery after the update.

**Full example:** [examples/get_speaker_trade_ideas.md](examples/get_speaker_trade_ideas.md)

## get_speaker_ticker_history

Daily history for one speaker's stance on one ticker.

**Inputs:**
- `speaker_name` (required, str)
- `ticker` (required, str)
- `days` (optional, int, default `180`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Build a daily chart-style read of Serenity's SIVE stance over 180 days. Use idea IDs, daily direction mix, sentiment, and confidence."

**Returns:** Markdown response from `get_speaker_ticker_history`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_speaker_ticker_history.md](examples/get_speaker_ticker_history.md)

## get_recent_idea_candidates

Return every recent candidate grouped for first-pass LLM research.

This is schema v3 of the established recent-candidate request, not a
separate summary or ranking endpoint. It replaced the former flat response and
the temporary `get_recent_ideas_by_ticker` sibling.

Pages contain whole-ticker groups; one ticker is never split across cursors.

**Inputs:**
- `window` (optional, str, default `'6h'`): exact `1h`, `6h`, `12h`, `24h`, or `1d`; `3d` and `7d` are rejected
- `cursor` (optional, str, default `''`)
- `as_of` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `direction` (optional, str, default `''`)
- `delivery` (optional, str, default `'auto'`)
- `limit` (optional, int, default `200`)
- `offset` (deprecated transition only, int | None, default `None`): only `0` can start a request; continue with the exact `cursor`

**Example prompt:**
> "Find the strongest Buzzberg trade ideas from the last 24 hours. Read `ticker_group_columns`, `speaker_columns`, `history_columns`, `idea_columns`, and every `ticker_group_rows` page. While `has_more=true`, call the tool again with the exact `next_cursor` unchanged. Compare complete theses and their evidence only after the final page; source-specific confidence is intentionally absent from this cross-source result. Then use `get_trade_idea_details` for the finalist idea IDs that need source or duplicate evidence."

**Returns:** typed `structuredContent` (`GroupedRecentIdeasColumnarPage`) with whole-ticker groups, canonical speakers, compact 365-day histories, full-thesis idea rows, stored-price context, counts, a fixed snapshot and cursor pagination; `content[].text` is an exact compact-JSON mirror of the same page.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_recent_idea_candidates.md](examples/get_recent_idea_candidates.md)

## get_recent_ideas_summary

Return a configurable recent-ideas report with selected sections and sectors.

**Inputs:**
- `window` (optional, str, default `'24h'`)
- `cursor` (optional, str, default `''`)
- `as_of` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `direction` (optional, str, default `''`)
- `delivery` (optional, str, default `'auto'`)
- `limit` (optional, int, default `200`)
- `offset` (optional, int | None, default `None`)
- `sections` (optional, list[str] | None, default `None`)
- `sectors` (optional, list[str] | None, default `None`)
- `table_limit` (optional, int, default `10`)
- `detail_limit` (optional, int, default `3`)

**Example prompt:**
> "Summarize Buzzberg ideas from the last 24 hours. Read agent_guide and follow every exact pagination.next_cursor until has_more=false. Use the final summary_context and its complete analysis_instruction for selected tables (all six by default): Alpha Calls, Top Mentions, Mentions Spike, Consensus, First Calls and Shorts. Follow its bounded Alpha thesis review and unique-ticker detail selection; use saved metrics and source links without recounting authors. Request sections=[alpha_calls], sectors=[Information Technology, Crypto], detail_limit=5 for Alpha only with five detailed tickers. table_limit controls rows; detail_limit=0 requests tables only."

**Returns:** typed `structuredContent` (`GroupedRecentIdeasSummaryPage`) with the grouped-v5 metadata and report-scoped full-thesis evidence declared by data_projection, plus globally calculated `summary_context` on inline delivery or the final page. Context 10.0.0/report format 6.0.0 contains effective report_options, selected sections and limits (default six Top-10 tabs/three details), sector-scoped data, a 20-ticker Alpha shortlist for bounded host thesis review, complete display-row evidence, unique-ticker detail selection, saved author metrics, side Call prices, market context, original source links and a full presentation instruction; `content[].text` is an exact compact-JSON mirror of the same page.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_recent_ideas_summary.md](examples/get_recent_ideas_summary.md)

`sections` selects one or more of `alpha_calls`, `top_mentions`, `mentions_spike`,
`consensus`, `first_calls`, and `shorts`. Omit it for all six. Selected sections
always follow that canonical order; one section renders as a single table.
`sectors` filters by reviewed sector names, case-insensitively, with `IT` as an
alias for `Information Technology`. Unknown names return the available menu.
`table_limit` accepts 1–10 rows per table; `detail_limit` accepts 0–table_limit
unique detailed tickers per section. Zero requests tables only.

`limit` controls fallback response-page packing, not table rows. Continue with
the exact cursor alone: the selected filters and limits are pinned to it.
Refresh connector discovery or start a new chat if these four options are absent.

## get_portfolio_summary

Get a complete 24h portfolio update for up to 100 selected tickers.

**Inputs:**
- `tickers` (required, list[str])
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Give me a daily portfolio update for NVDA, BTC and TSLA. Call get_portfolio_summary with those tickers; read all returned full LONG/SHORT/AVOID theses, author bias, portfolio updates, earnings calls and 13F disclosures; follow analysis_instruction: one table with L/S/A/N, mentions, 30-day daily average and attention growth, a direction legend below, then qualifying tickers with prices, authors and roles, side Call prices, attributed arguments and source links. Include only tickers with report_eligible=true in both the table and details, including event-only tickers."

**Returns:** typed `structuredContent` (`PortfolioSummaryResult`) for up to 100 selected tickers over the last 24h: all full LONG/SHORT/AVOID theses, canonical authors with roles and stored promotion/affiliation bias, portfolio-update events including closes, shared derived earnings-call evidence and new stored 13F disclosures, source links, saved unique-author mention metrics, stored prices and the complete portfolio report instruction (schema 2.0.0, report format 2.0.1), with the fixed English title `Buzzberg Portfolio Update` and one compact `L/S/A/N` column in every language (e.g. `17/0/0/11`), with a direction legend below the table: only tickers with `report_eligible=true` appear in both the table and details, including event-only tickers. Per-source coverage distinguishes unavailable data from no events; source_type filters author ideas/portfolio updates only. Complete reports conditionally offer a daily summary when no equivalent recurring report is already known; scheduling requires user confirmation. Inline delivery is complete or explicitly returns `requires_narrowing` without partial theses; `content[].text` is an exact compact-JSON mirror.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_portfolio_summary.md](examples/get_portfolio_summary.md)

## get_my_feeds

Read your saved feeds; filter by ID/name/type and choose full members or names/counts only.

**Inputs:**
- `feed_type` (optional, str, default `''`)
- `limit` (optional, int, default `50`)
- `after_id` (optional, int, default `0`)
- `feed_id` (optional, int | None, default `None`)
- `name` (optional, str, default `''`)
- `include_members` (optional, bool, default `True`)

**Example prompt:**
> "Read my portfolio using get_my_feeds(name='my portfolio', feed_type='ticker') and pass its complete portfolio_tickers to get_portfolio_summary. For a known feed use feed_id; for names/counts only use include_members=False. Clarify multiple matches."

**Returns:** typed `PersonalFeedsResult` (schema 2.0.0), always with a feeds list. Optional feed_id, literal case-insensitive name substring and feed_type filters combine with AND. Default include_members=True returns complete ticker/author/source membership and portfolio_tickers; False returns metadata/counts only, omits member arrays and sets members_included=false. Pass a chosen full portfolio_tickers list directly to get_portfolio_summary. Follow next_after_id while has_more, retaining all filters; page limits count feeds, never members. No account override, shared cache or writes.

**Scope:** Read-only. Private feeds of the authenticated Buzzberg account only.

**Full example:** [examples/get_my_feeds.md](examples/get_my_feeds.md)

## get_trade_idea_details

Return full audit details for selected recent-idea finalists.

**Inputs:**
- `idea_ids` (required, list[int])

**Example prompt:**
> "Retrieve audit details for these finalist Buzzberg idea IDs: [123, 456]. Show each source URL, source identifiers, speaker-role provenance, full thesis, and any grouped near-duplicate evidence."

**Returns:** typed `structuredContent` (`TradeIdeaDetailsBatch`) containing full source identifiers and URLs, speaker-role provenance, thesis text and grouped near-duplicate evidence for up to 50 requested idea IDs; `content[].text` is an exact compact-JSON mirror.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_trade_idea_details.md](examples/get_trade_idea_details.md)

## get_top_speakers

List Buzzberg's top speakers by lifetime Alpha-rank.

`Adj. return` is the Bayesian-shrunk current mark-to-market mean for the
deduplicated Alpha evaluation set. It is not benchmark- or beta-adjusted.
`Evaluated Ideas` is the size of that set, not the number of all historical
mentions or all ideas with a 30-day return.

**Inputs:**
- `limit` (optional, int, default `25`)

**Example prompt:**
> "Use `get_top_speakers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_speakers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_speakers.md](examples/get_top_speakers.md)

## get_top_speaker_signals

Fresh trade ideas from the top-N Buzzberg speakers within a time window.

**Inputs:**
- `top_n` (optional, int, default `50`)
- `window` (optional, str, default `'7d'`)
- `signal` (optional, str, default `'first_flip'`)
- `direction` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `limit` (optional, int, default `30`)

**Example prompt:**
> "Use `get_top_speaker_signals` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_speaker_signals`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_speaker_signals.md](examples/get_top_speaker_signals.md)

## get_sentiment

Get sentiment analysis for a ticker: average sentiment, breakdown by direction, by speaker tier.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_sentiment` for a Buzzberg analysis."

**Returns:** Markdown response from `get_sentiment`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_sentiment.md](examples/get_sentiment.md)

## get_ticker_timeseries

Get daily sentiment, mention counts, and cached close prices for charting.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `90`)
- `source_type` (optional, str, default `''`)
- `trim_empty_prefix` (optional, bool, default `True`)

**Example prompt:**
> "Use `get_ticker_timeseries` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_timeseries`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_timeseries.md](examples/get_ticker_timeseries.md)

## get_most_mentioned_tickers

Rank tickers by Buzzberg mention volume over a lookback window.

**Inputs:**
- `days` (optional, int, default `1`)
- `limit` (optional, int, default `20`)
- `source_type` (optional, str, default `''`)
- `min_mentions` (optional, int, default `1`)
- `history` (optional, bool, default `False`)

**Example prompt:**
> "Use `get_most_mentioned_tickers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_most_mentioned_tickers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_most_mentioned_tickers.md](examples/get_most_mentioned_tickers.md)

## get_top_sentiment_tickers

Rank tickers by strongest bullish or bearish Buzzberg sentiment.

**Inputs:**
- `days` (optional, int, default `1`)
- `limit` (optional, int, default `20`)
- `min_mentions` (optional, int, default `3`)
- `direction` (optional, str, default `'bullish'`)
- `source_type` (optional, str, default `''`)
- `history` (optional, bool, default `False`)

**Example prompt:**
> "Use `get_top_sentiment_tickers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_sentiment_tickers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_sentiment_tickers.md](examples/get_top_sentiment_tickers.md)

## get_sentiment_divergence

Find tickers where speakers disagree most (high divergence in sentiment).

**Inputs:**
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)
- `min_mentions` (optional, int, default `5`)

**Example prompt:**
> "Use `get_sentiment_divergence` for a Buzzberg analysis."

**Returns:** Markdown response from `get_sentiment_divergence`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_sentiment_divergence.md](examples/get_sentiment_divergence.md)

## get_ticker_info

Price context comes only from persisted database bars, with the saved timestamp.
Missing prices stay unavailable; this tool never refreshes market data.

Get detailed info for a ticker: mention count, top speakers, recent ideas, stored price.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_ticker_info` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_info`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_info.md](examples/get_ticker_info.md)

## get_speaker_profile

Get an author report by default; use mode='data' for raw data for your own report.

**Inputs:**
- `speaker_name` (required, str)
- `mode` (optional, str, default `'report'`)
- `sections` (optional, list[str] | None, default `None`)
- `days` (optional, int, default `0`)

**Example prompt:**
> "Show aleabitoreddit's author profile as a report with Main Focus, Most Mentions, Winners, Losers and Recent first calls. Use mode='data' only when I request raw structured data to build my own report."

**Returns:** typed structuredContent (SpeakerProfileResult, schema 2.1.0) with selected author sections and a compact JSON text mirror. Default report mode adds one presentation instruction (format 1.1.5); data mode omits it. Each tab has at most 15 rows. Most Mentions includes first-call direction, date, price and return alongside compact L/S/A/N counts. Includes stored performance clocks, follower metadata, Coverage Map themes, directional mention rankings and exact lifetime first-call dates/prices.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_speaker_profile.md](examples/get_speaker_profile.md)

`sections` accepts `overview`, `followers`, `main_focus`, `most_mentions`,
`winners`, `losers`, `recent`, or `['all']`. Omitted sections mean a full report
in report mode and overview-only in data mode. Empty/unknown selections fail.
`days=0` means all available history; 1-3650 filters publication dates. First
calls are resolved against lifetime history before this filter. Performance
and follower snapshots expose their own dates; returns are not live quotes.

Schema 2.1.0 replaces the old Markdown profile. Refresh cached tool metadata;
use `data` keys for your own presentation. Credibility is no longer returned.

## compare_speakers

Compare what different speakers say about a ticker. Shows who's bullish vs bearish.

The Alpha columns use the same live definition as `get_top_speakers`:
Bayesian-shrunk current direction-adjusted mark-to-market return on the
deduplicated evaluation set, not benchmark-adjusted excess return.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `compare_speakers` for a Buzzberg analysis."

**Returns:** Markdown response from `compare_speakers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/compare_speakers.md](examples/compare_speakers.md)

## get_recent_content

Get latest content (videos, articles, tweets) from Buzzberg.

**Inputs:**
- `source_type` (optional, str, default `''`)
- `limit` (optional, int, default `10`)

**Example prompt:**
> "Use `get_recent_content` for a Buzzberg analysis."

**Returns:** Markdown response from `get_recent_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_recent_content.md](examples/get_recent_content.md)

## get_tickers_overview

Prices and their timestamps come only from persisted database bars.
Missing prices stay unavailable; this tool never refreshes market data.

Batch overview for multiple tickers: stored price, mentions, sentiment, and direction counts.

**Inputs:**
- `tickers` (required, list[str])
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_tickers_overview` for a Buzzberg analysis."

**Returns:** Markdown response from `get_tickers_overview`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_tickers_overview.md](examples/get_tickers_overview.md)

## search_content

Search public content titles by keyword.

**Inputs:**
- `query` (required, str)
- `limit` (optional, int, default `10`)
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Search recent public Buzzberg content titles for robotaxi. Show source type, date, and why each item may be worth reading."

**Returns:** Markdown response from `search_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/search_content.md](examples/search_content.md)

## search_youtube_research

Search derived Buzzberg YouTube research notes from the last 7 days.

**Inputs:**
- `query` (required, str)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)
- `ticker` (optional, str, default `''`)

**Example prompt:**
> "Use `search_youtube_research` for a Buzzberg analysis."

**Returns:** Markdown response from `search_youtube_research`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/search_youtube_research.md](examples/search_youtube_research.md)

## get_ticker_youtube_research

Get derived YouTube research notes for one ticker from the last 7 days.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)

**Example prompt:**
> "Use `get_ticker_youtube_research` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_youtube_research`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_youtube_research.md](examples/get_ticker_youtube_research.md)

## get_youtube_market_tldr

Summarize the derived YouTube research-note index for the last 1-7 days.

**Inputs:**
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `50`)

**Example prompt:**
> "Use `get_youtube_market_tldr` for a Buzzberg analysis."

**Returns:** Markdown response from `get_youtube_market_tldr`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_youtube_market_tldr.md](examples/get_youtube_market_tldr.md)

## get_ticker_mentions

Count mentions of a ticker across 24h / 7d / 30d windows, broken down by source.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_ticker_mentions` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_mentions`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_mentions.md](examples/get_ticker_mentions.md)

## read_ticker_content

Read recent content summaries and trade-context text mentioning a ticker.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)
- `verbose` (optional, bool, default `False`)

**Example prompt:**
> "Read recent SIVE content. Use YouTube and Substack TLDRs where available, not raw YouTube text or full articles. Summarize thesis, risks, and sources."

**Returns:** Markdown response from `read_ticker_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/read_ticker_content.md](examples/read_ticker_content.md)

## get_recent_source_text

Read recent source TLDRs + trade ideas for user-side research workflows.

**Inputs:**
- `source_type` (required, str)
- `limit` (optional, int, default `0`)
- `ticker` (optional, str, default `''`)
- `post_kind` (optional, str, default `''`)
- `speaker_rank_limit` (optional, int, default `0`)
- `include_all_tweets` (optional, bool, default `False`)
- `max_chars_per_item` (optional, int, default `0`)
- `max_total_chars` (optional, int, default `220000`)
- `include_segments` (optional, bool, default `False`)
- `days` (optional, int, default `1`)

**Example prompt:**
> "Read top-50 speaker Twitter/X ticker-idea tweets from the last 24h, or YouTube/Substack TLDRs plus trade ideas from the last 7d. Use post_kind='research' for alpha extraction, or post_kind='stock list' for stock-list posts. Summarize themes, tickers, and disagreements."

**Returns:** Markdown response from `get_recent_source_text`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_recent_source_text.md](examples/get_recent_source_text.md)

## save_trade_idea

[BETA] Bookmark a trade idea by its ID.

**Inputs:**
- `idea_id` (required, int)
- `user_email` (optional, str, default `''`)
- `dry_run` (optional, bool, default `False`)

**Example prompt:**
> "Use `save_trade_idea` for a Buzzberg analysis."

**Returns:** Markdown response from `save_trade_idea`.

**Scope:** WRITE — modifies only data owned by the API key owner.

**Full example:** [examples/save_trade_idea.md](examples/save_trade_idea.md)

## get_speaker_lens

Get a source-derived speaker lens with methodology and thesis history.

The track-record section separates four populations: the live Alpha evaluation
set, per-horizon measured ideas, signal-timing calls, and dated
initiation/flip ledger rows. It also reports how many ledger rows have matured
to a 30-day return versus remain `⏳`.

**Inputs:**
- `speaker` (required, str)
- `sections` (optional, str, default `'persona,methodology,track_record'`)

**Example prompt:**
> "Use `get_speaker_lens` for a Buzzberg analysis."

**Returns:** Markdown response from `get_speaker_lens`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_speaker_lens.md](examples/get_speaker_lens.md)

## get_speaker_lens_context

Build one bounded question-specific Speaker Lens context pack. It combines the
dated lens snapshot, current Alpha metrics, live structured ideas, and optional
ticker thesis, history, source links, and price context. The user's agent writes
the answer; Buzzberg does not make a second server-side LLM call.

**Inputs:**
- `speaker` (required, str)
- `question` (required, str, 1-400 characters)
- `ticker` (optional, str, default `''`)
- `recent_days` (optional, int, default `45`, capped at `90`)
- `recent_limit` (optional, int, default `16`, capped at `20`)
- `history_days` (optional, int, default `365`, capped at `365`)

**Example prompt:**
> "Use Buzzberg's Bubbleboi speaker lens to explain his current MU thesis, how it changed, and which evidence matters now."

**Returns:** A bounded Markdown context pack for the user's AI agent to analyze.
The complete response is capped at 32,000 characters; oversized lens sections,
idea lists, and history tables are truncated independently without leaving open
Markdown code fences.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_speaker_lens_context.md](examples/get_speaker_lens_context.md)

## list_speaker_lenses

List speakers that have an AI lens, ordered by the current live Alpha-rank.

**Inputs:**
- `limit` (optional, int, default `50`)

**Example prompt:**
> "Use `list_speaker_lenses` for a Buzzberg analysis."

**Returns:** Markdown response from `list_speaker_lenses`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/list_speaker_lenses.md](examples/list_speaker_lenses.md)

## find_site_section

Find where a feature lives in the Buzzberg interface. Read-only, no data is changed.

**Inputs:**
- `query` (required, str)
- `locale` (optional, str, default `'en'`)
- `limit` (optional, int, default `5`)

**Example prompt:**
> "Use `find_site_section` for a Buzzberg analysis."

**Returns:** Markdown response from `find_site_section`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/find_site_section.md](examples/find_site_section.md)
