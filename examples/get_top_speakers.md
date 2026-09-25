# get_top_speakers

Ask: "Show the Buzzberg author leaderboard for 30-day returns."

The default request is `get_top_speakers()`: 30-day return horizon, all call
publication dates, all categories and platforms, Alpha order, 25 rows. The
response gives a Markdown table plus structured rows with rank, author, Alpha,
average return, excess versus S&P 500, win rate, call count and snapshot date.
The maximum is 50 rows.

To change the return horizon without changing which publication dates qualify:

```text
get_top_speakers(return_horizon="90d", calls_published="all", limit=50)
```

To consider only calls published in the last 180 days:

```text
get_top_speakers(return_horizon="90d", calls_published="180d", limit=50)
```

`return_horizon` also supports `7d`, `180d`, `360d` and `avg` (the website's
weighted 30/90/180 score). `calls_published` supports `all`, `ytd`, `30d`,
`90d` and `180d`. Compatible MCP Apps hosts show interactive controls that
requery the tool; text-only clients repeat the call with the new parameters.
