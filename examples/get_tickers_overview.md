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

- stored price and its saved timestamp;
- 24h / 7d / 30d mention counts;
- average sentiment over the requested lookback;
- direction counts for `LONG`, `SHORT`, `WATCH`, `AVOID`, and `NEUTRAL`;
- missing ticker symbols, if any.

This is the preferred first step for broad market scans. Use targeted tools like
`get_tickers_overview` with view='details' or view='mentions', or `read_ticker_content` after the
overview narrows the basket.

Prices come only from persisted database bars. Missing values stay unavailable;
this request never refreshes prices through a market-data provider.

## Single-ticker views

```python
get_tickers_overview(tickers=["NVDA"], view="details")
get_tickers_overview(tickers=["NVDA"], view="mentions")
```

Details returns identity, lifetime counts/directions/top five authors, stored
price and at most five short idea previews published in the last 30 days (ten
rows scanned). Mentions returns counts by source over 24h/7d/30d by ingestion
time, not individual mentions or quotations. Both require exactly one input
ticker and reject days. Omit days for these fixed-window views. Overview alone
accepts up to 50 symbols and days (default 30, maximum 90). No pagination.
