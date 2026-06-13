# get_ticker_timeseries

Ask: "Use Buzzberg to build a 90-day chart dataset for SIVE: daily close, mention count, and average sentiment."

Buzzberg returns a machine-readable CSV block:

```csv
date,close,mentions,avg_sentiment,long,short,neutral,avoid
2026-05-25,4.82,12,0.2417,7,1,4,0
2026-05-26,4.91,8,0.1250,3,1,4,0
2026-05-27,,0,,0,0,0,0
```

Use it when you want Claude to plot sentiment and attention over time, or to compare price moves against Buzzberg discussion volume.

Notes:

- `mentions` counts Buzzberg ticker mentions by publication date.
- `avg_sentiment` is blank when there were no mentions that day.
- `close` is read from Buzzberg's cached `price_bars`; it can be blank on weekends or if no cached bar exists.
- Default sources are Twitter, YouTube, newsletters, and Reddit. Wire-service news is disabled for analysis.
