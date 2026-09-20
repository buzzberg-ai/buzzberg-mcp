# get_most_mentioned_tickers

Use this when you want the Buzzberg attention leaderboard: "what is everyone
talking about right now?"

## Prompt

```text
Use Buzzberg to show the most buzzed tickers in the last 24 hours.

For each ticker, show mentions, source mix, sentiment, and whether the story
looks like fresh discovery or crowded post-move chatter. Include daily history
if useful.
```

## Tool Call

```python
get_most_mentioned_tickers(days=1, limit=20, min_mentions=1, history=True)
```

## 7-Day Version

```python
get_most_mentioned_tickers(days=7, limit=20, min_mentions=5, history=True)
```

## Top-50 Speaker Version

`get_most_mentioned_tickers` ranks the whole Buzzberg conversation. For a
Twitter-derived top-speaker idea pulse, first identify the author set, then
collect recent saved ideas and keep only those authors:

```python
get_top_speakers(limit=50)
get_recent_idea_candidates(window="24h", source_type="twitter")
```

Follow every exact continuation cursor. Count the returned ideas by ticker and
label the coverage; these are saved idea mentions, not all original tweets.

## What To Look For

- Mention spikes before price moves: possible discovery.
- Mention spikes after a vertical price move: possible crowding.
- Multiple source types: broader confirmation than one X cluster.
- High mentions but neutral sentiment: attention without a clear trade view.
