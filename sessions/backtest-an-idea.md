# Backtest An Idea — Verbatim Drilldown

Take a name you're already curious about and reconstruct the conviction case
from the source pieces Buzzberg has ingested: tweets, video segments, Reddit
posts, and short snippets from newsletters where available. Each call comes
with the original speaker and a timestamp.

## The ask

> I'm thinking about going long URA (uranium ETF). Pull every Buzzberg call
> on URA from the last 30 days where confidence is at least 0.4, with the
> verbatim source text for each, ranked by speaker quality.

## Tools Claude will chain

1. `search_trade_ideas(ticker="URA", days=30, min_confidence=0.4)` — filtered
   list with direction, speaker, confidence, source, date, plus thesis text
   and verbatim quote per call
2. `get_speaker_profile(speaker_name=...)` for the loudest voices — track
   record + role
3. (Optional) `get_ticker_mentions(ticker="URA")` — raw unfiltered stream of
   every URA mention if you want to widen beyond the filtered call list

## What you'll get (illustrative)

Filtered call list (last 30d, confidence ≥ 0.4):

> | Ticker | Direction | Conf | Speaker | Source | Date |
> |--------|-----------|------|---------|--------|------|
> | URA | 🟢 LONG | 0.93 | Pentosh1 | Twitter | 2026-05-06 |
> | URA | 🟢 LONG | 0.90 | Pentosh1 | Twitter | 2026-05-07 |
> | URA | 🟢 LONG | 0.78 | Avi Felman | Twitter | 2026-04-28 |
> | URA | 🟢 LONG | 0.65 | Michael Pento | Julia LaRoche Show | 2026-05-12 |
> | URA | 🟢 LONG | 0.65 | Mando | Thread Guy | 2026-05-05 |
> | URA | watch | 0.65 | Erik Townsend | Macro Voices | 2026-05-14 |

Sample drill-down to actual source text:

> **Pentosh1 (Twitter, 2026-05-07, conf 0.90):**
> > *"\$URA is another great one that is looking primed for a breakout."*
>
> Thesis (AI-summarized from full thread):
> > Long URA on structural uranium deficit and global plans to triple nuclear
> > capacity, supported by AI data center power-demand tailwinds.
>
> **Michael Pento (Julia LaRoche Show, 2026-05-12, conf 0.65):**
> > Long URA as part of a stagflation hedge thesis — commodities and energy
> > over equities.

## Drill down

- *"Show me Pentosh1's track record"* → `get_speaker_profile(speaker_name="Pentosh1")`
- *"Has any high-credibility speaker called URA short in the last 90 days?"*
  → `search_trade_ideas(ticker="URA", direction="short", days=90)`
- *"What did Erik Townsend mean by 'watch'? Pull his full quote"* →
  `search_trade_ideas(ticker="URA", speaker="Erik Townsend", days=30)`
- *"Build me the bear case if there is one"* → ask Claude to invert and search
  for any short or AVOID calls

## Why this beats reading Twitter

- **Deduplicated** — each speaker × ticker × direction call shows once even
  if they repeated themselves 5 times.
- **Confidence-scored** — `confidence ≥ 0.4` filters out reactive/passing
  mentions and keeps thesis-level calls.
- **Source-anchored** — every call links back to the original tweet, video,
  newsletter, or Reddit post. No game of telephone.
- **Speaker-quality weighted** — `get_speaker_profile` tells you whether
  Pentosh1 is +4000% historical or noise.

## Tips

- For thinly-covered tickers, drop `min_confidence` to 0.0 and widen to
  `days=90`. You'll get more noise but won't miss the only call.
- Use `direction` to constrain — *"only the bulls"* / *"only the bears"* — for
  asymmetric reads.
- If you want chronological order, sort the result by date — Buzzberg's
  default sort is by relevance + recency.
