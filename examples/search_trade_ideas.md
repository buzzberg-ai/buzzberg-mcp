# search_trade_ideas

Ask: "Find bullish NVDA ideas from the last week, limited to 10 results."

Buzzberg returns a Markdown list or table of matching trade ideas with speaker,
ticker, direction, confidence, thesis, and date when available.

## Search several exact tickers

Ask:

> Find Buzzberg trade ideas for SOXS or SQQQ from the last 90 days. Explain the
> underlying market exposure of each idea and keep the two tickers separate.

Tool call:

```json
{
  "days": 90,
  "limit": 20,
  "query": "SOXS SQQQ inverse ETF"
}
```

Explicit uppercase ticker symbols in `query` are exact idea-ticker filters.
Generic words such as `inverse` and `ETF` provide context but do not broaden
the result to sibling tickers mentioned in the same source post. When a query
contains no explicit ticker symbols, Buzzberg performs bounded OR text search.

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
