# search_trade_ideas

Ask: "Find all bullish NVDA ideas from the last week."

Buzzberg returns exact counts and complete JSON rows with speaker, ticker,
direction, confidence, saved thesis and publication date. The same rows appear
in `structuredContent[buzzberg_receipt]`. If the complete result fits 900,000
estimated tokens and 5,000 grouped ideas, one call returns it all.

## Search several exact tickers

Ask:

> Find Buzzberg trade ideas for SOXS or SQQQ from the last 90 days. Explain the
> underlying market exposure of each idea and keep the two tickers separate.

Make one scoped call for each ticker (SOXS, then SQQQ):

```json
{
  "ticker": "SOXS",
  "days": 90
}
```

This uses two of the account's 100 distinct ticker slots per rolling 30 days.
Repeated searches and cursor continuations for the same companies use no extra
slots. The separate author allowance is 100 distinct registered authors; authors
merely appearing in ticker-search results do not spend those slots.

## Research-post ideas

Ask:

> Use Buzzberg to find NVDA trade ideas from research posts in the last 24h. Show
> ticker, speaker, thesis, direction, confidence, and which ideas deserve a
> deeper follow-up.

Tool call:

```json
{
  "ticker": "NVDA",
  "post_kind": "research",
  "days": 1
}
```

## Stock-list ideas

Ask:

> Use Buzzberg to find NVDA trade ideas from stock-list posts this week. Which
> tickers show up as repeated candidates, and which have enough thesis quality
> to add to my research queue?

Tool call:

```json
{
  "ticker": "NVDA",
  "post_kind": "stock list",
  "days": 7
}
```

## Continue a result

Only oversized results require continuation; page size follows the byte budget,
not an artificial 20/50-row limit. The legacy `limit` argument in old calls is
ignored. If the reply has `pagination.next_cursor`, call
`search_trade_ideas(cursor=...)` with that token alone. Continue until
`has_more=false`. The current 90-day retention
boundary still applies; a cursor cannot unlock older publications.
