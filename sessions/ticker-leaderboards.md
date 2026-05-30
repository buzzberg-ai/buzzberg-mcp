# Ticker Leaderboards

Use this when you want a market pulse before choosing what to research. Buzzberg
can rank tickers by attention ("most buzzed") or by sentiment, then include
daily history so Claude can tell whether a story is new, building, crowded, or
fading.

## The ask

> Use Buzzberg to show the most buzzed tickers in the last 24 hours and the
> strongest bullish narratives over the last 7 days.
>
> I care about the story, not just the leaderboard. For each ticker, explain
> why people are talking about it, whether the attention is new or crowded, and
> what source snippets I should read next.

## Tools Claude will chain

1. `get_most_mentioned_tickers(days=1, limit=20, history=True)` — today's
   attention leaderboard plus daily rows
2. `get_most_mentioned_tickers(days=7, limit=20, min_mentions=5, history=True)`
   — weekly buzz with history
3. `get_top_sentiment_tickers(days=7, min_mentions=5, direction="bullish", history=True)`
   — strongest positive narratives
4. `get_top_sentiment_tickers(days=7, min_mentions=5, direction="bearish", history=True)`
   — strongest negative narratives
5. `read_ticker_content(ticker="...", days=7, limit=20)` — source snippets
   behind the interesting spikes

## What you'll get

Ask Claude to write a market-intelligence read:

> **Most buzzed today:** not just "ticker X had 42 mentions", but why it is
> showing up now: earnings, insider buying, AI narrative, product news, short
> thesis, or a repeat of an already-known story.
>
> **7-day leaders:** which tickers are recruiting attention across the week
> instead of appearing for one noisy day.
>
> **Sentiment leaders:** where the crowd is strongly bullish or bearish after
> filtering out one-off mentions with `min_mentions`.
>
> **Historical read:** daily rows let Claude spot whether attention came before
> price/sentiment, appeared during the move, or arrived late after the move was
> already obvious.

## Follow-up prompts

- *"For the top 5 buzzed tickers, tell me which are fresh discovery and which
  are crowded repeats."*
- *"Show the 7-day daily history for the top bullish tickers, then pick one
  that looks early."*
- *"Find the strongest bearish narrative with at least 5 mentions and show the
  source snippets behind it."*
- *"Which ticker had rising mentions but weakening sentiment?"*

## Tips

- Use `days=1` for "what is hot right now".
- Use `days=7` for "what is actually building".
- Use `history=True` when you want charts or a narrative timeline.
- Use `min_mentions=5` or higher for sentiment rankings; otherwise one very
  bullish post can dominate the leaderboard.
- `days=1` is the current 24h window. Arbitrary `since_hours=12` style
  leaderboards are planned, but not live yet.
- To find acceleration today, compare `days=1` against `days=7` and ask your
  agent to rank tickers by today's share of weekly mentions. A dedicated
  acceleration/crowding tool is on the roadmap.
