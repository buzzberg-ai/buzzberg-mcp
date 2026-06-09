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

```text
Use Buzzberg to find the most bullish tickers among top-50 speakers today.
Require at least 2 mentions and include daily history.
```

```python
get_top_sentiment_tickers(
    days=1,
    limit=20,
    min_mentions=2,
    direction="bullish",
    speaker_rank_limit=50,
    history=True,
)
```

## What To Look For

- High average sentiment plus rising mentions: strengthening narrative.
- High sentiment but low mentions: fragile signal, use a higher `min_mentions`.
- Strong bearish sentiment with source snippets: useful risk radar.
- Daily history: whether sentiment is improving, fading, or just repeating.
