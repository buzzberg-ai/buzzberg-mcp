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

Use this when you want attention from Buzzberg's highest-ranked speakers only,
not the whole database. `get_most_mentioned_tickers` ranks all Buzzberg
mentions; for a top-speaker-only pulse, ask your agent to use
`get_recent_source_text(source_type="twitter", speaker_rank_limit=50)` and count
tickers from that bounded set.

```text
Use Buzzberg to rank the tickers most mentioned by top-50 speakers today.
Show mentions, sentiment, direction mix, source mix, and whether each story
looks fresh or already crowded.
```

```python
get_recent_source_text(source_type="twitter", speaker_rank_limit=50, days=1)
```

## What To Look For

- Mention spikes before price moves: possible discovery.
- Mention spikes after a vertical price move: possible crowding.
- Multiple source types: broader confirmation than one X cluster.
- High mentions but neutral sentiment: attention without a clear trade view.
