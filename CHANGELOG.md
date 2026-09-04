# Changelog

## Beta Period

SemVer is not guaranteed before `1.0.0`. Breaking changes will be documented
here and announced to active beta users.

## MCP grouped schema v4 and ready summary - 2026-09-04

- `get_recent_idea_candidates` schema v4 replaces the per-request compact
  365-day speaker history with a daily precomputed directional promotion-bias
  result and transparent count, time-distribution, purity, freshness and failure
  evidence.
- The label uses a fixed preceding 180-day window ending 24 hours before the
  snapshot. Clients must use the returned `HIGH`, `MEDIUM`, `LOW`, or `NONE`
  value as supplied and keep issuer relationships separate.
- `promotion_bias_snapshot` reports whether the pinned daily generation is
  available, stale, or unavailable. Clients should show N/A rather than infer a
  replacement when no usable result exists.
- Added the existing `get_recent_ideas_summary` tool to the public manifest,
  tool reference and examples. It defaults to 24 hours, reuses the lossless
  grouped-v4 pages and adds global summary context on the complete/final page.
- Reconnect MCP clients and begin a new cursor pass after deployment so cached
  v3 metadata is not mixed with schema v4.

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
