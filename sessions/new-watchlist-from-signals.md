# Build A Watchlist From Top-Speaker Signals

Auto-curate a watchlist of names that just hit your radar from high-Alpha
speakers in a given window — first-time mentions and direction flips only,
filtering out re-iterated existing calls.

## The ask

> Build me a fresh watchlist from the top-30 speakers' first-time and
> direction-flip calls in the last 24 hours. Show direction and source,
> and add the names to my watchlist.

## Tools Claude will chain

1. `get_top_speaker_signals(top_n=30, window="24h", signal="first_flip")` —
   surfaces only first-mention and flip events, skips noise
2. For each ticker returned → `add_to_watchlist(ticker=...)` (write tool,
   scoped to your user account)

## What you'll get (illustrative)

Fresh signals table (last 24h):

> | Sig | Ticker | Dir | Speaker (rank) | When |
> |-----|--------|-----|----------------|------|
> | 1ST | POWI | 🟢 LONG | ren_aramb (#4) | 5h ago |
> | 1ST | VICR | 🟢 LONG | ren_aramb (#4) | 5h ago |
> | 1ST | AOSL | 🟢 LONG | ren_aramb (#4) | 5h ago |
> | 1ST | VSH | 🟢 LONG | ren_aramb (#4) | 5h ago |
> | 1ST | WOLF | 🟢 LONG | ren_aramb (#4) | 5h ago |
> | FLIP | AMD | 🔴 AVOID | frenchie_ (#9) | 1h ago |
> | 1ST | SFTBY | 🟢 LONG | ParadisLabs (#5) | 2h ago |
> | FLIP | IREN | 🔴 SHORT | Daniel Koss | 6h ago |
> | FLIP | SPY | 🔴 SHORT | Labubu Trader | 4h ago |

When you ask Claude to add them, you'll see:

> Added to your watchlist:
> - POWI, VICR, AOSL, VSH, WOLF (basket from ren_aramb, semis supply chain)
> - SFTBY (ParadisLabs)
> - AMD, IREN, SPY *(flagged with FLIP — direction change worth re-reading)*

## Drill down

- *"For ren_aramb's 5-name semis basket — pull the verbatim tweet text"* →
  `search_trade_ideas(speaker="ren_aramb", days=1)`
- *"Why did frenchie_ flip on AMD? What was the previous direction?"* →
  `search_trade_ideas(ticker="AMD", speaker="frenchie_", days=30)`
- *"Filter the watchlist add to LONGs only — skip the SHORT flips"* →
  ask Claude to filter the result list before calling `add_to_watchlist`

## Signal types

- `signal="first"` — only first-time mentions across our entire dataset for
  this speaker+ticker pair. High-purity, may miss reversal interest.
- `signal="first_flip"` (default) — first-time mentions *and* direction
  flips. Best general-purpose value.
- `signal="all"` — every idea from top speakers in window, no signal filter.
  Firehose mode.

## Tips

- A FLIP from one of the top-10 speakers is one of the strongest signals on
  the platform — when someone with +3000% historical track record reverses,
  it usually means a thesis-level update, not just noise.
- For longer-horizon names, widen `window="7d"` or `"30d"`. The 24h window is
  designed for active intraday/short-horizon traders.
