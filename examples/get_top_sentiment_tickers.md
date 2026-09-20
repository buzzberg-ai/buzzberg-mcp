# get_top_sentiment_tickers

Use this when you want the strongest bullish or bearish ticker narratives in a
time window.

## Prompt

```text
Use Buzzberg to find the strongest bullish ticker narratives over the last 7
days. Require at least 5 mentions per ticker. Explain the story behind the top
names and what I should read next.
```

## Bullish Tool Call

```python
get_top_sentiment_tickers(days=7, limit=20, min_mentions=5, direction="bullish", history=True)
```

## Bearish Tool Call

```python
get_top_sentiment_tickers(days=7, limit=20, min_mentions=5, direction="bearish", history=True)
```

## Top-50 Speaker Version

For a top-speaker view, identify the authors and collect the complete recent
Twitter-derived idea set:

```python
get_top_speakers(limit=50)
get_recent_idea_candidates(window="24h", source_type="twitter")
```

Follow every exact continuation cursor, filter to those authors, then group the
saved ideas by ticker and direction. Use returned sentiment only where available.
This describes extracted ideas, not original tweets. The ticker sentiment tool
itself ranks the full Buzzberg conversation, not a top-speaker subset.

## What To Look For

- High average sentiment plus rising mentions: strengthening narrative.
- High sentiment but low mentions: fragile signal, use a higher `min_mentions`.
- Strong bearish sentiment with source snippets: useful risk radar.
- Daily history: whether sentiment is improving, fading, or just repeating.
