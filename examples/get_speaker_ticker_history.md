# get_speaker_ticker_history

Use this when you want a chart-ready daily history for one speaker and one
ticker: idea counts, average sentiment, confidence, direction counts, latest
direction, and intraday direction changes. It returns aggregates only, without
individual idea IDs, theses or source links in any response format.

Ask your agent:

```text
Use Buzzberg to chart how Serenity's view on SIVE changed over the last 90 days.
Show daily idea count, average sentiment, long/short/watch counts,
and direction changes within each day.
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "ticker": "SIVE",
  "days": 90
}
```

The response includes CSV like:

```csv
date,ideas,avg_sentiment,avg_confidence,long,short,close,watch,neutral,avoid,latest_direction
2026-09-15,2,0.5000,0.7200,2,0,0,0,0,0,long
```

## Safety / scope

Both `speaker_name` and `ticker` are required and resolve one pair, including
known aliases. The lookback defaults to 90 days and is clamped to 1–90 days from
current server time, using publication time. Older and future publications are
excluded, including data that ages out while cached.

An authenticated account has 100 admitted requests per rolling 30 days,
shared across all clients, keys and connections. This allowance is separate from
search and detail requests. Repeated, cached and empty requests count; later read
failures also consume the admitted request. Missing arguments are refused before
admission. Changing credentials cannot reset the counter.

At the limit, the tool returns `history_monthly_quota_exceeded` with
`retry_after_seconds`. If shared quota state is unavailable, it refuses the
read, including cached data. The structured chronology and private aggregate
file use version 2.0.0. Archived version 1 files remain readable.
