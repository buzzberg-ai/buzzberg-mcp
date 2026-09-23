# get_ticker_deep_dive

Ask: “Use Buzzberg to deep dive MU in English.”

```json
{"ticker":"MU","mode":"report"}
```

One response includes saved evidence and `analysis_instruction`. The host writes
an English report with a simple business overview, price and available returns,
24h sentiment/mentions/authors versus 30-day averages, aligned price/sentiment/
mentions charts, linked bull/bear arguments, useful business numbers, measurable
checks and key voices on Buzzberg. Omit YTD when unavailable. Connect real
sentiment observations across gaps visually, preserving nulls in data/tooltips.

Use `mode="data"` for the same evidence without presentation instructions.
The tool does not call a model or market provider. Charts are rendered by the
client from the returned observations. There is no archive offset or pagination.

Selected arguments cover seven days with context up to thirty days; at most
20 materials / 50 ideas, six derived YouTube notes and 90,000 response characters.
Latest saved company actuals/guidance within 180 days are dated separately from
author estimates. Leaders use 180-day LONG/SHORT counts, including ties; first
recorded LONG is bounded metadata from public stored history, not global discovery.
No raw transcripts or newsletter article bodies are returned.

**100 combined requests/account/rolling 30 days**, shared with
`read_ticker_content`. Repeats, empty results and later failures count. Quota
outages refuse reads. Public visibility is checked again before delivery.
Errors return `isError=true`, no evidence, and a retry delay for quota exhaustion.
