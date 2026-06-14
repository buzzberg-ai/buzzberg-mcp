# search_trade_ideas

Ask: "Find bullish NVDA ideas from the last week, limited to 10 results."

Buzzberg returns a Markdown list or table of matching trade ideas with speaker,
ticker, direction, confidence, thesis, and date when available.

## Research-post ideas

Ask:

> Use Buzzberg to find trade ideas from research posts in the last 24h. Show
> ticker, speaker, thesis, direction, confidence, and which ideas deserve a
> deeper follow-up.

Tool call:

```json
{
  "post_kind": "research",
  "days": 1,
  "limit": 25
}
```

## Stock-list ideas

Ask:

> Use Buzzberg to find trade ideas from stock-list posts this week. Which
> tickers show up as repeated candidates, and which have enough thesis quality
> to add to my research queue?

Tool call:

```json
{
  "post_kind": "stock list",
  "days": 7,
  "limit": 50
}
```
