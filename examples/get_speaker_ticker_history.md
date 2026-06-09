# get_speaker_ticker_history

Use this when you want a chart-ready daily history for one speaker and one
ticker: mentions, average sentiment, direction counts, first/flip counts, and
cached daily close.

Ask your agent:

```text
Use Buzzberg to chart how Serenity's view on NOK changed over the last 180 days.
Show mentions, average sentiment, long/short/watch counts, first/flip markers,
and price. Then explain whether the story is early, crowded, or changing.
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "ticker": "NOK",
  "days": 180
}
```

The response includes CSV like:

```csv
date,close,mentions,avg_sentiment,long,short,watch,neutral,avoid,first,flip
2026-05-27,14.25,2,0.5000,2,0,0,0,0,1,0
```

## Safety / scope

This tool requires both `speaker_name` and `ticker`, so it is for targeted
speaker/ticker research rather than bulk database export.

