# Morning Briefing

Get a single-shot read on what changed overnight: AI portfolio state, fresh
calls from top-ranked speakers, and current prices for tickers that matter.

## The ask

> Give me a Buzzberg morning briefing: latest AI portfolio, strongest fresh
> ideas from the top-10 speakers in the last 24 hours, sentiment divergences
> worth watching, and prices for the tickers that matter most.

## Tools Claude will chain

1. `get_portfolio` — current 9-position AI portfolio with weights and entry
   prices
2. `get_top_speaker_signals(top_n=10, window="24h", signal="first_flip")` —
   fresh first/flip calls from highest-Alpha speakers only
3. `get_sentiment_divergence(limit=5, days=7)` — tickers where smart-money
   disagrees most
4. `get_price(tickers=[...])` — live prices for everything that came up

## What you'll get (illustrative)

A structured briefing in Claude's reply. Sample fragments from a real run:

**Fresh top-speaker activity (last 24h):**

> - `ren_aramb` (#4) opened a 5-name semis basket: **POWI, VICR, AOSL, VSH, WOLF** all 🟢 LONG
> - `frenchie_` (#9) flipped **AMD → 🔴 AVOID** (had been long earlier in the month)
> - `ParadisLabs` (#5) opened **SFTBY 🟢 LONG** (SoftBank ADR)
> - `Daniel Koss` flipped **IREN → 🔴 SHORT**

**Divergence radar (7d):**

> - **SIVE** — 111 mentions, sentiment spread 1.80 (max disagreement)
> - **NVDA** — 281 mentions, spread 1.60
> - **MU** — 128 mentions, spread 1.55

**AI portfolio top positions (illustrative snapshot):**

> - **MU 18% 🟢 LONG** at $751.00 — memory cycle + AI demand
> - **HLIT 15% 🟢 LONG** at $15.20 — virtualized cable software near-monopoly
> - **CRM 8% 🔴 SHORT** at $180.07 — Jim Bianco short thesis
> - **BTC 7% 🔴 SHORT** at $77,069.50 — BlackRock distribution

## Drill down

To go deeper on any thread Claude surfaces:

- *"Why is `frenchie_` flipping AMD? Show me the original tweet text."* →
  `get_ticker_mentions(ticker="AMD", speaker="frenchie_", days=2)`
- *"Who else is short CRM besides Jim Bianco?"* → `compare_speakers(ticker="CRM", days=30)`
- *"Drill into the SIVE divergence — who's the bull side and who's the bear side?"* →
  `compare_speakers(ticker="SIVE", days=7)`

## Tips

- Use `window="6h"` instead of `"24h"` for a "since I last checked" feel during
  the trading day.
- `signal="first"` (without flip) shows only first-ever calls — useful for
  finding net-new names. `signal="all"` is firehose mode.
- The AI portfolio is regenerated daily at 21:05 UTC. If you run this before
  that, you'll see yesterday's positions.
