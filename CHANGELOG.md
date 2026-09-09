# Changelog

## Beta Period

SemVer is not guaranteed before `1.0.0`. Breaking changes will be documented
here and announced to active beta users.

## Author profile overflow rules and rendered checks - 2026-09-09

- Report format 1.1.5 clarifies translated headings/captions/Focus values,
  directional ranking in Most Mentions, and leaderboard followers as
  Buzzberg-ranked authors following the account on X.
- Shared column widths stay fixed across tabs; narrow tables scroll while
  preserving text size/whole values. Focus can grow and wrap by words.
  Selected tabs have solid contrast; other tabs retain button styling.
- Rendered checks cover all supplied tabs at normal/narrow widths, scrolling,
  clipping, overlaps and column positions. Code/HTML inspection is not visual
  verification. Schema 2.1.0 and data behavior are unchanged.

## Main Focus ticker/count pairing - 2026-09-09

- Report format 1.1.4 keeps each Main Focus ticker and count in one unbroken
  inline "TICKER · count" pair, with normal word spacing inside and compact
  gaps between pairs. Right alignment applies only to standalone numeric
  columns. Schema 2.1.0 and data are unchanged.

## Author profile visual hierarchy and metric labels - 2026-09-09

- Report format 1.1.3 specifies contrasting selected tabs, a shared grid across
  the four ticker tables, compact gaps, consistent price/currency cells and
  aligned Main Focus ticker/count pairs. Tickers and returns carry emphasis.
- Return headers distinguish first-call returns from mean position returns;
  Recent visibly identifies latest first directional calls. Translate labels
  consistently except fixed tab names/direction codes, keep metadata compact
  and place methodology notes below tables or in a disclosure.
- Schema 2.1.0, calculations and the 15-row cap are unchanged.

## Portfolio events and author bias - 2026-09-08

- `get_portfolio_summary` schema/report 2.0.0 adds stored author promotion and
  affiliation bias, portfolio-update posts including closes, derived earnings
  calls and new stored 13F disclosures. Request parameters remain unchanged;
  `source_type` filters author ideas/portfolio updates, while earnings and 13F
  remain included for the selected tickers.
- Report membership now uses `report_eligible`: actionable ideas or new events.
  Hosts must process all event evidence and referenced shared earnings bodies,
  disclose unavailable sources and uncertain filing times, and distinguish
  corporate guidance and changes in portfolio weights from author calls/trades.
- The fixed `Buzzberg Portfolio Update` title, compact `NEUTRAL` column, 100-ticker
  limit and 900,000-token default estimated complete-response budget remain.
  No transcript export, server-side thesis selection or automatic subscription.

## Author profile column order and readability - 2026-09-08

- Report format 1.1.2 places L/S/A/N after Direction in Most Mentions and
  Mentions after Direction in Winners, Losers and Recent, followed by first
  call date, first call price and Return.
- Text matches the surrounding conversation's normal body size, with a larger
  author title, a compact metric grid and metadata grouped into short wrapping
  lines. Schema 2.1.0 and raw data are unchanged.

## Author profile presentation guidance - 2026-09-08

- Report format 1.1.1 separates fixed content from compact financial styling.
  The host chooses widths and spacing to suit the data and screen, and checks
  the actual rendered result when possible without claiming unavailable visual
  verification. Schema 2.1.0, request parameters and table contents are unchanged.

## Compact author profile tables - 2026-09-08

- Report format 1.1.0 uses a single linked author title/header above the tabs
  with no closing recap. Every tab returns at most 15 rows in both modes;
  coverage shares still include classified themes outside the displayed top 15.
- Schema 2.1.0 adds exact lifetime first-call direction/date/price/return to
  Most Mentions and displays its counts in one compact L/S/A/N cell. Missing
  values stay null; neither recent repeats nor later returns replace the first
  call. Request parameters are unchanged.

## Author profile report - 2026-09-08

- `get_speaker_profile` defaults to `mode="report"`: author context and five
  tabs with one short presentation instruction. `mode="data"` returns raw data
  for custom analysis; `sections` selects projections and `days=0` means all
  available history. No new tool name is added.
- Recent includes only lifetime first LONG/SHORT/AVOID calls. First-call date
  and price preserve exact idea identity; unavailable values remain null.
  Coverage shares, directional counts, saved returns and follower metadata
  expose their scope and timestamps. Credibility is removed.
- Breaking beta contract: schema 2.0.0 structuredContent plus JSON text mirror
  replaces the old Markdown profile. Clients must refresh cached tool metadata
  and consume the new data keys. Report format starts at 1.0.0.

## Daily portfolio summary - 2026-09-07

Report format 1.1.0 now shows only tickers with at least one LONG/SHORT/AVOID idea
in the requested 24h scope in both the table and details. Zero-actionable and
unknown tickers remain payload coverage metadata. If none qualify, the report
returns a single portfolio-level message instead of empty tables and blocks.

Follow-up: ticker feeds and portfolio requests now accept 100 distinct symbols;
author feeds accept 100 authors/independent sources, with linked accounts counted
together with their selected author. New read tools `get_my_feeds` and
`get_my_feed` let agents retrieve only their authenticated account's saved feeds
and pass a ticker feed's complete composition into the 24h portfolio summary.
The catalog now has 34 tools. Accountless connections cannot read personal feeds.

- Added `get_portfolio_summary`: complete 24h LONG/SHORT/AVOID thesis evidence
  for up to 50 selected tickers, author roles, saved mention/price context and
  an embedded one-table report instruction. Oversized results explicitly
  require a smaller ticker list; no partial theses are returned.
- Added the missing public catalog entry and example for
  `get_recent_ideas_summary`, distinguishing its market-wide six-tab report
  from the complete selected-ticker portfolio update.

## MCP recent-candidate window scope - 2026-08-29

- `get_recent_idea_candidates` now accepts only `1h`, `6h`, `12h`, `24h`, and
  the equivalent `1d` window. Its default remains `6h`.
- Requests for `3d` or `7d` are rejected before the query runs instead of
  depending on the former 500-row longer-window review ceiling.
- The `best_recent_ideas` prompt exposes the same exact-window set. Longer
  research should use a tool whose scope and filters are designed for it.

## MCP recent-candidate confidence field - 2026-08-29

- `get_recent_idea_candidates` no longer exposes generic `confidence` in its
  grouped cross-source idea rows. Stored source-specific values and other tools
  are unchanged.
- `idea_columns` now contains nine fields: `idea_id`, `published_at`,
  `direction`, `signal`, `entry_price`, `price_change_since_entry_pct`,
  `source`, `post_kind`, and `thesis_full`.
- The shared number combined ingestion signals with different meanings across
  Twitter, YouTube, newsletters, and Reddit, so it could not support a valid
  cross-source comparison.
- Flat v2 `idea_rows` shown by a long-lived client are cached tool metadata, not
  a second server contract. Reconnect or start a new chat to refresh the catalog.

## MCP service contract - 2026-08-10

- `get_recent_idea_candidates` now returns schema v3 grouped by ticker and
  canonical speaker, with complete full theses, stored price context, compact
  365-day history and whole-ticker cursor pagination.
- The temporary `get_recent_ideas_by_ticker` sibling was removed. It represented
  the same user request and made clients choose between competing flat and
  grouped tools.
- The change reduces repeated transport fields and puts all evidence for one
  ticker together; it does not pre-rank ideas, shorten theses or replace the
  calling model with a server-generated summary.
- Clients holding a cached tool schema should reconnect or start a new chat and
  begin a new cursor pass. Flat v2 cursors cannot address grouped v3 pages.

## 0.1.0b7

- Pins Claude Desktop's local bridge to `mcp-remote@0.1.38` instead of executing
  a floating `@latest` package on every launch.
- Forces the bridge to use Streamable HTTP only, preventing fallback attempts
  against the legacy SSE endpoint after reconnects.

## 0.1.0b6

- Security fix: `--dry-run` now redacts Buzzberg keys already present in the
  existing config as well as the new key being proposed.

## 0.1.0b5

- Makes Claude Desktop authentication reliable across macOS and Windows by
  using the supported `X-API-Key:bzb_...` bridge header without spaces.
- Documents that a timeout/disconnect can mean the saved key was revoked and
  should be replaced.

## 0.1.0b4

- Switches Claude Desktop's `mcp-remote` bridge from legacy SSE `/sse` to
  Streamable HTTP `/mcp`, avoiding stale SSE session failures after reconnects
  or server deploys.

## 0.1.0b3

- Simplifies Claude Desktop setup by writing the Bearer key directly in the
  `mcp-remote` header argument instead of using an environment variable. The
  dry-run path still redacts the key.

## 0.1.0b2

- Fixes Claude Desktop setup. Claude Desktop local config expects stdio MCP
  servers, so the installer now writes an `npx mcp-remote` bridge entry instead
  of a direct `url` / `headers` remote-server block.
- Updates Claude Desktop manual setup docs to match the working config.

## 0.1.0b1

- Initial private beta installer package.
- Adds stdlib-only client config writers for Claude Desktop, Claude Code,
  Cursor, Cline, and Continue.dev.
- Adds public SECURITY.md, TOOLS.md, examples, and release workflow skeleton.
