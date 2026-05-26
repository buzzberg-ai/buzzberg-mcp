# Contrarian Scan

Find tickers where smart-money speakers most disagree. High sentiment spread
flags both opportunities (someone is going to be wrong, big) and risks (your
edge is structurally lower in a consensus name).

## The ask

> Run a contrarian scan: find the 5 tickers with the highest sentiment spread
> in the last 7 days, show me the bulls and bears on each, and surface the
> highest-credibility speaker on each side.

## Tools Claude will chain

1. `get_sentiment_divergence(limit=5, days=7)` — ranks tickers by `max - min`
   sentiment among speakers
2. For each ticker → `compare_speakers(ticker=..., days=7)` to see who's where
3. For the most interesting one → `get_ticker_mentions(ticker=..., direction="short", days=7)`
   and the same with `direction="long"` for verbatim quotes

## What you'll get (illustrative)

Top divergent tickers (last 7d):

> | Ticker | Mentions | Spread | Min | Avg | Max |
> |--------|----------|--------|-----|-----|-----|
> | SIVE | 111 | **1.80** | -0.80 | +0.25 | +1.00 |
> | LITE | 79 | 1.60 | -0.70 | +0.31 | +0.90 |
> | NVDA | 281 | 1.60 | -0.70 | +0.24 | +0.90 |
> | MU | 128 | 1.55 | -0.65 | +0.35 | +0.90 |
> | FCEL | 62 | 1.50 | -0.50 | +0.40 | +1.00 |

For each ticker, Claude will fill in:

> **NVDA — bulls vs bears:**
> - Bull side: Ray Dalio (cred 10.0, +0.50), Dan Ives (cred 7.7, +0.50)
> - Bear side: Michael Green (cred 6.5, -0.50), Chris Whalen (cred 6.0, -0.50)
> - Spread reflects "data-center monopoly" vs "valuation+cycle peak" debate

## Why this is useful

- **High spread + high mention count** = institutional disagreement on a
  liquid name. Setup for a directional thesis trade.
- **High spread + low mention count** = something niche where one camp may be
  early or wrong. Read the quotes verbatim before reacting.
- **Low spread + high mention count** = consensus. Your edge from sentiment
  alone is small; you need a non-sentiment thesis (catalyst, valuation, etc.).

## Drill down

- *"Pull the verbatim short quotes on SIVE — what specifically are bears worried about?"*
- *"For NVDA, what's the credibility-weighted net sentiment?"*
- *"Show me names with spread > 1.5 AND > 50 mentions over the last 30 days"*

## Tips

- `days=7` is the default; widen to `days=30` for slower-moving names.
- Spread is in `[-1, 1]` ticker-level sentiment space, so spread 1.80 means
  someone's at -0.80 and someone else is at +1.00 — full opposite calls.
- A ticker with one outlier opinion can have huge spread without real
  controversy — always cross-check with `compare_speakers` to see how many
  speakers on each side.
