# get_ticker_timeseries

Ask: "Plot SIVE’s daily mentions and sentiment against its share price over the
last 180 complete days. Highlight the biggest attention spike."

```json
{
  "ticker": "SIVE",
  "days": 180,
  "trim_empty_prefix": false,
  "include_today": false
}
```

The response supplies the metrics to show above the chart:

- **Total mentions**, plus the average per requested calendar day.
- **Average sentiment**, weighted by mentions, on the −1 to +1 scale.
- **Price change**, with currency, first and last saved closes and their dates.

These are calculated from the requested data, not fixed example figures. The
`sentiment_price_chart` MCP prompt requests this same complete-days window and
instructs the host to use its returned metrics without mixing in another period.

The response also supplies a CSV block. This small excerpt is illustrative:

```csv
date,price_close,mentions,avg_sentiment,long,short,close,watch,neutral,avoid,non_directional
2026-05-25,4.82,12,0.2417,7,1,0,2,2,0,4
2026-05-26,4.91,8,0.1250,3,1,0,3,1,0,4
2026-05-27,,0,,0,0,0,0,0,0,0
```

The host should show mention bars, a connected saved-close line on its own price
axis, and an aligned sentiment panel with a fixed −1 to +1 scale. Connect
consecutive available price observations across weekends and other missing
calendar dates; **do not break the line at each blank, and do not invent prices**.
A missing-day tooltip must show unavailable. Keep every daily row, include hover
or touch readouts, highlight the largest mention spike and show coverage.
If the host cannot render a chart, show the metrics and data instead.

Notes:

- `mentions` counts visible Buzzberg ticker idea rows by publication date,
  including LONG, SHORT, WATCH, NEUTRAL, AVOID and CLOSE.
- `watch` is separate from `neutral`; `non_directional` combines them.
- `avg_sentiment` is blank when there were no mentions that day.
- `price_close` comes only from stored daily bars, so weekends and other days
  can be blank. Two compatible prices with a positive starting close are needed
  to calculate a return.
- Prefix trimming changes the returned CSV range, not the summary denominator.
- Default sources are Twitter, YouTube, newsletters and Reddit.
- `include_today=True` preserves the historical behavior; use `False` when the
  user asks for complete days. Dates use UTC.
