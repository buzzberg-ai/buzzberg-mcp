# get_ticker_deep_dive

Ask: “Use Buzzberg to deep dive MU in English.”

```json
{"ticker":"MU","mode":"report"}
```

One response includes saved evidence, `analysis_instruction` and a ready-formatted
`presentation` header. On MCP Apps hosts, the tool displays a built-in dashboard
with the price, every available 7d/30d/YTD return, 24h sentiment/mentions/authors
versus 30-day averages, and aligned price/sentiment/mentions charts. The host
continues below it with a simple business overview, linked bull/bear arguments,
useful business numbers, measurable checks and key voices in English. Do not
recreate or duplicate the native charts.

Other hosts start with `presentation.header_markdown` and render charts when
supported. Omit YTD when unavailable. Connect real sentiment observations across
gaps visually, preserving nulls in data/tooltips. The native view includes date
inspection by pointer or keyboard, responsive layout and light/dark themes.

Use `mode="data"` for the same evidence without presentation instructions.
The tool does not call a model or market provider. The native UI receives the
same authenticated result and makes no additional research call. Its static
`ui://buzzberg/ticker-deep-dive-v1.html` resource contains no ticker/account data
and loads no external scripts or services. There is no archive offset or pagination.
Refresh the connector's tool discovery after the update; clients may cache the
new `_meta.ui.resourceUri` declaration. Host support for MCP Apps is required
for the fixed dashboard; the portable text report remains available otherwise.

Current arguments cover seven days. Context starts at 30 publication days and
extends to 90 when fewer than 30 qualifying publications are available; if at
most 30 qualify across the ticker's entire stored history, older history is
eligible too. Publications count once even when several speakers or ideas come
from the same video or post. Only public, visible, supported sources with named
authors and saved LONG/SHORT/AVOID/WATCH theses or key points qualify.

At most **30 materials / 50 ideas**, six derived YouTube notes and **90,000**
response characters are returned; full-history eligibility still respects idea,
author and text limits. The saved-thesis/points/quote budget is 60,000 characters.
Schema 1.2.0 supplies `query.context_days` (30, 90, or null for all history) and
`context_scope`; report format 2.2.0 keeps older arguments dated and marked as
context. Old numbers retain their periods, old forecasts stay attributed to
their original dates, and past catalysts are not presented as upcoming.
24h metrics and 30d charts keep their original periods. These selection details
belong in documentation or answers about selection, not an ordinary report footer.
Latest saved company actuals/guidance within 180 days are dated separately from
author estimates. Leaders use 180-day LONG/SHORT counts, including ties; first
recorded LONG is bounded metadata from public stored history, not global discovery.
No raw transcripts or newsletter article bodies are returned.

**100 combined requests/account/rolling 30 days**, shared with
`read_ticker_content`. Repeats, empty results and later failures count. Quota
outages refuse reads. Public visibility, dates and the sparse-history lifetime
threshold are checked again before delivery.
Errors return `isError=true`, no evidence, and a retry delay for quota exhaustion.
