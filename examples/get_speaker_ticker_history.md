# get_speaker_ticker_history

Use this when you want a chart-ready daily history for one speaker and one
ticker: idea counts, average sentiment, confidence, direction counts, latest
direction, and the `idea_id`s behind each daily bucket.

Ask your agent:

```text
Use Buzzberg to chart how Serenity's view on SIVE changed over the last 180 days.
Show daily idea count, average sentiment, long/short/watch counts, idea IDs,
and thesis changes. Then explain whether the story is early, crowded, or changing.
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "ticker": "SIVE",
  "days": 180
}
```

The response includes CSV like:

```csv
date,ideas,avg_sentiment,avg_confidence,long,short,close,watch,avoid,neutral,latest_direction,idea_ids
2026-05-27,2,0.5000,0.7200,2,0,0,0,0,0,long,12345;12346
```

## Safety / scope

This tool requires both `speaker_name` and `ticker`, so it is for targeted
speaker/ticker research rather than bulk database export.
