# Morning Briefing

Get a single-shot read on what changed overnight: a complete recent idea
candidate pass, current disagreements, and prices for tickers that matter.

## The ask

> Give me a Buzzberg morning briefing: strongest fresh ideas from all visible
> speakers in the last 24 hours, sentiment divergences
> worth watching, and prices for the tickers that matter most. Review every
> candidate page before selecting.

## Tools Claude will chain

1. `get_recent_ideas_by_ticker(window="24h")` — every visible recent
   candidate grouped by ticker; Claude reads the four column declarations once,
   maps every `ticker_group_rows` page, and follows the exact `next_cursor`
   unchanged until `has_more=false` before selecting the strongest theses
2. `get_trade_idea_details(idea_ids=[...])` — source links, role provenance,
   and duplicate evidence for the selected finalists
3. `get_sentiment_divergence(limit=5, days=7)` — tickers where speakers
   disagree most
4. `get_recent_content(limit=5)` — important recent source items
5. `get_price(tickers=[...])` — live prices for everything that came up

## What you'll get (illustrative)

A structured briefing in Claude's reply. Sample fragments from a real run:

**Fresh activity (last 24h):**

> - `ren_aramb` (#4) opened a 5-name semis basket: **POWI, VICR, AOSL, VSH, WOLF** all 🟢 LONG
> - `frenchie_` (#9) flipped **AMD → 🔴 AVOID** (had been long earlier in the month)
> - `ParadisLabs` (#5) opened **SFTBY 🟢 LONG** (SoftBank ADR)
> - `Daniel Koss` flipped **IREN → 🔴 SHORT**

**Divergence radar (7d):**

> - **SIVE** — 111 mentions, sentiment spread 1.80 (max disagreement)
> - **NVDA** — 281 mentions, spread 1.60
> - **MU** — 128 mentions, spread 1.55

## Drill down

To go deeper on any thread Claude surfaces:

- *"Why is `frenchie_` flipping AMD? Show me the original tweet text."* →
  `search_trade_ideas(ticker="AMD", speaker="frenchie_", days=2)` (returns the
  call with thesis + verbatim quote)
- *"Who else is short CRM besides Jim Bianco?"* → `compare_speakers(ticker="CRM", days=30)`
- *"Drill into the SIVE divergence — who's the bull side and who's the bear side?"* →
  `compare_speakers(ticker="SIVE", days=7)`

## Tips

- Use `window="6h"` instead of `"24h"` for a "since I last checked" feel during
  the trading day.
- Treat stored confidence as one ingestion-stage thesis/evidence quality
  signal, not predicted return and never the sole rank. Do not treat Alpha
  score or follower count as thesis quality. Compare mechanism, entry context,
  author role, repeated promotion, conflicts, and independent evidence.
