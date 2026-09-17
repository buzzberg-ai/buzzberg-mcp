# read_ticker_content

Ask: "Read up to 20 NVDA materials published in the last 30 days. Summarize
the theses, risks and sources."

```json
{"ticker": "NVDA", "days": 30, "limit": 20}
```

The command returns short public posts and derived YouTube/newsletter summaries,
with authors, publication dates and source links. It does not return raw YouTube
transcripts or full newsletter articles. Defaults remain 7 days and 10 materials.
The hard caps are 20 materials and the last 30 days from current server time,
based on publication rather than ingestion. There is no historical offset or
pagination. Future/undated materials are excluded; cached and slow reads are
checked again before return.

An authenticated account gets 100 requests per rolling 30 days, shared across
all tickers, sources, keys, clients and channels. Repeats, cache hits, unknown
tickers, empty results and later read failures count. Invalid arguments do not.
Missing account identity or shared quota state refuses the read.

When the allowance is exhausted, the result has `isError=true`,
`error_code=ticker_content_monthly_quota_exceeded`, an empty `result`,
and `retry_after_seconds`. Wait for that interval; changing keys or filters
does not create another allowance.
