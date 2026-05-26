# Ticker Deep Dive

Full picture on a single name before you size a position: who's talking about
it, where they net out, what the smart-money divergence looks like, and what
the current price says.

## The ask

> Deep dive on NVDA using Buzzberg: sentiment over the last 7 days, mention
> volume by source, top speakers on both sides, recent specific theses with
> verbatim quotes, and the current price.

## Tools Claude will chain

1. `get_ticker_info(ticker="NVDA")` — high-level overview (count, top speakers,
   price)
2. `get_sentiment(ticker="NVDA", days=7)` — direction breakdown + source mix +
   per-speaker averages
3. `compare_speakers(ticker="NVDA", days=30)` — bulls vs bears table with
   credibility scores
4. `read_ticker_content(ticker="NVDA", days=14)` — verbatim quotes and
   AI-summarized theses, deduplicated per content piece
5. `get_price(tickers=["NVDA"])` — current price

## What you'll get (illustrative)

Sentiment breakdown (last 7d):

> | Direction | Count | % |
> |-----------|-------|---|
> | 🟢 LONG | 76 | 27% |
> | 🔴 SHORT | 8 | 3% |
> | ⚪ NEUTRAL | 81 | 29% |
> | 🔴 AVOID | 9 | 3% |
>
> **Total mentions:** 281 (7d) — Twitter 211, YouTube 51, Reddit 16, Substack 3

Bulls and bears (last 30d, ranked by credibility):

> - **Ray Dalio** (cred 10.0, Bridgewater) — 🟢 +0.50
> - **Citrini** (cred 9.2) — 🟢 +0.17 (mixed across 3 mentions)
> - **Dan Ives** (cred 7.7, Wedbush) — 🟢 +0.50 across 4 mentions
> - **Josh Brown** (cred 8.5, Ritholtz) — 🟢 +0.50
> - **Michael Green** (cred 6.5, Simplify) — 🔴 -0.50
> - **Chris Whalen** (cred 6.0) — 🔴 -0.50

Sample thesis from `read_ticker_content`:

> *"NVDA remains the only fully integrated AI platform — software + hardware +
> ecosystem. The recent 2.4% weekly dip is an attractive entry point ahead of
> the data-center capex cycle."* — illustrative bull thesis

## Drill down

- *"Show me the bear quotes verbatim."* → `search_trade_ideas(ticker="NVDA", direction="short", days=30)`
- *"What did Citrini specifically say across those 3 mentions?"* →
  `search_trade_ideas(ticker="NVDA", speaker="Citrini", days=30)`
- *"How does NVDA sentiment compare to AMD?"* → ask Claude to call
  `get_sentiment` for both tickers and produce a side-by-side.

## Tips

- `compare_speakers` is credibility-weighted by default. If you want raw count,
  combine with `get_sentiment(ticker=...).by_speaker`.
- `read_ticker_content` deduplicates by content piece — one CNBC clip = one
  entry even if multiple speakers in the clip mentioned NVDA. Use
  `get_ticker_mentions(ticker=...)` for the raw unfiltered stream (no dedup,
  no filters), or `search_trade_ideas(ticker=..., speaker=...)` when you need
  to filter by speaker / direction / confidence / time window.
- For a small / illiquid name, try `days=90` — 7-day windows are often too
  narrow to be useful.
