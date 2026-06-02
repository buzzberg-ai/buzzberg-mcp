# get_tickers_overview

Use `get_tickers_overview` when you want to screen a basket of tickers without
calling one ticker tool over and over.

## Example prompt

```text
Use Buzzberg to screen these tickers:
NVDA, TSM, AMD, AVGO, DKNG, FLUT, COIN, HOOD, PLTR, SMCI.

First call get_tickers_overview for the basket. Then pick the top 3 names for
follow-up based on recent mentions, sentiment, and direction counts. For only
those top 3, read recent ticker content and explain the current thesis or debate.
```

## What to expect

The tool returns a compact Markdown table with:

- current price;
- 24h / 7d / 30d mention counts;
- average sentiment over the requested lookback;
- direction counts for `LONG`, `SHORT`, `WATCH`, `AVOID`, and `NEUTRAL`;
- missing ticker symbols, if any.

This is the preferred first step for broad market scans. Use targeted tools like
`get_ticker_mentions`, `get_ticker_info`, or `read_ticker_content` after the
overview narrows the basket.
