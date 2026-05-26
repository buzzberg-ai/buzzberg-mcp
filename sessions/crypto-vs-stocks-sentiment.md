# Crypto vs Equities Sentiment

Quick read on how the macro sentiment lines up across asset classes — useful
before a rotation trade or when crypto-equity correlation breaks down.

## The ask

> Compare sentiment for BTC, ETH against major AI plays (NVDA, AMD, GOOGL) over
> the last 7 days. Show me whether smart-money is positioned the same way
> across both, or whether the camps are diverging.

## Tools Claude will chain

For each ticker in the list:

1. `get_sentiment(ticker=..., days=7)` — average sentiment + bull/bear split
2. `get_top_speaker_signals(top_n=20, window="7d", signal="first_flip")` — to
   see recent positioning shifts in either group
3. Synthesis prompt: Claude builds a side-by-side and calls out asymmetries

## What you'll get (illustrative)

> | Ticker | Avg sentiment (7d) | Bullish % | Bearish % | Mentions |
> |--------|--------------------|-----------|-----------|----------|
> | BTC | +0.18 | 22% | 8% | 412 |
> | ETH | +0.12 | 19% | 7% | 198 |
> | NVDA | +0.24 | 27% | 6% | 281 |
> | AMD | -0.05 | 18% | 24% | 142 |
> | GOOGL | +0.31 | 34% | 4% | 156 |

Claude will surface asymmetries:

> **Cross-asset divergence today:**
> - GOOGL is the strongest AI-related sentiment (+0.31) with very low bearish
>   share (4%) — consensus bull.
> - AMD has flipped *negative* on average over 7 days. `frenchie_` and others
>   are flipping to AVOID. Worth checking specific theses.
> - Crypto sentiment (BTC, ETH) is mildly positive but lower than NVDA/GOOGL.
>   Risk-on tilt is favoring equity AI exposures over crypto right now.

## Drill down

- *"Show me BTC bears verbatim — who's actually short and why?"* →
  `get_ticker_mentions(ticker="BTC", direction="short", days=7)`
- *"What's the AI portfolio doing on BTC right now?"* → `get_portfolio()`
  (will show whether the AI is long or short BTC, current weight)
- *"Crypto-correlated equities: where do MSTR, COIN, MARA sentiment net out?"*
  → ask Claude to repeat the same chain for those tickers

## Tips

- Buzzberg rolls related symbols up under one parent for display. BTC includes
  MSTR, IBIT, GBTC, BITO, BITB, BITW. GLD includes GOLD, GDX, IAU, XAU. SPY
  includes VOO and RSP. USO includes WTI, BRENT, BRN, BNO. If you want the
  pure-coin or pure-ETF sentiment, ask Claude to filter `source_type` to
  twitter-only or to use the specific symbol you care about.
- Use `get_sentiment_divergence` afterwards on tickers where the cross-asset
  picture shows disagreement — high spread + low average sentiment is often a
  setup for a directional thesis trade.
