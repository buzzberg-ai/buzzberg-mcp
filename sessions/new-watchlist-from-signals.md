# Build A Research Shortlist From Top-Speaker Signals

Build a non-mutating shortlist of names that just hit the top-speaker radar in
a given window: first-time mentions and direction flips only.

## The ask

> Build me a fresh research shortlist from the top-30 speakers' first-time and
> direction-flip calls in the last 24 hours. Show direction, source, thesis,
> invalidation, and what I should verify next.

## Tools Claude will chain

1. `get_top_speaker_signals(top_n=30, window="24h", signal="first_flip")` —
   surfaces only first-mention and flip events, skips noise
2. `search_trade_ideas(ticker=..., days=30)` for targeted thesis context on
   shortlisted names

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

The result stays in the agent response. This workflow does not write to your
Buzzberg account.

## Drill down

- *"For ren_aramb's 5-name semis basket — pull the verbatim tweet text"* →
  `search_trade_ideas(speaker="ren_aramb", days=1)`
- *"Why did frenchie_ flip on AMD? What was the previous direction?"* →
  `search_trade_ideas(ticker="AMD", speaker="frenchie_", days=30)`
- *"Filter the shortlist to LONGs only — skip the SHORT flips"* → ask Claude
  to filter the result before deeper research

## Signal types

- `signal="first"` — only first-time mentions across our entire dataset for
  this speaker+ticker pair. High-purity, may miss reversal interest.
- `signal="first_flip"` (default) — first-time mentions *and* direction
  flips. Best general-purpose value.
- `signal="all"` — every idea from top speakers in window, no signal filter.
  Firehose mode.

## Tips

- A FLIP is a reason to inspect what changed, not proof that the new direction
  is correct. Read the thesis and source before treating it as actionable.
- For longer-horizon names, widen `window="7d"` or `"30d"`. The 24h window is
  designed for active intraday/short-horizon traders.
