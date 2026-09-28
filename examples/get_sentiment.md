# get_sentiment

Ask: "What is the 30 day sentiment for NVDA?"

Call `get_sentiment(ticker="NVDA")`. One response contains the whole report for
the last 30 days. Set `days` to choose 1–180 days from now; there is no historical
offset or continuation cursor. Optionally select `source_type`, such as
`youtube`, `twitter`, `newsletter` or `reddit`.

The Markdown report and `structuredContent.buzzberg_receipt` provide the same
average, mention count, direction/source tables and selected speaker samples.
The compatible receipt keeps its existing `rows`, `counts` and `effective_scope`;
`sentiment_details` adds these previously text-only fields:

| Field | Meaning |
| --- | --- |
| `version` | Extension version `1.0.0`; older receipts can omit the extension |
| `ticker_label` | Company name or the asset-type label from the heading |
| `weighting` | `per_mention`; authors with more mentions retain more weight |
| `bullish_pct`, `bearish_pct` | Rounded share of all mentions: LONG, and SHORT + AVOID |
| `non_directional_mentions` | WATCH + NEUTRAL mentions |
| `by_direction` | Direction, mention count and rounded percentage |
| `by_source` | Source type, display label and mention count |
| `top_speakers` | Speaker name, raw average, adjusted average and mention count |
| `speaker_selection` | At least two mentions, eight-mention prior, maximum ten speakers, ranked by absolute adjusted sentiment |
| `notes` | Existing direction-taxonomy, speaker-sample and inverse-ETF explanations |

The top-ten table is a selected sample, not the first page of all authors.
Whole-period counts include every eligible mention. Empty results carry empty
tables and no invented average. The tool reads saved sentiment values without
new AI analysis and returns no individual theses or original source text.

There is no dedicated monthly or distinct-ticker allowance for this tool.
Shared account work limits still apply across MCP calls.
