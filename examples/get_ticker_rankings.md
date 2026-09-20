# get_ticker_rankings

Choose one ranking: mention volume (default), highest average sentiment
(`bullish`), or lowest average sentiment (`bearish`).

## Prompt

```text
Use Buzzberg to show the most buzzed tickers in the last 24 hours.

For each ticker, show mentions, source mix, sentiment, and whether the story
looks like fresh discovery or crowded post-move chatter. Include daily history
if useful.
```

## Tool Call

```python
get_ticker_rankings(days=1, limit=20, min_mentions=1, history=True)
```

## 7-Day Version

```python
get_ticker_rankings(days=7, limit=20, min_mentions=5, history=True)
```

## Top-50 Speaker Version

`get_ticker_rankings` ranks the whole Buzzberg conversation. For a
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

## Bullish Tool Call

```python
get_ticker_rankings(days=7, limit=20, min_mentions=5, mode="bullish", history=True)
```

## Bearish Tool Call

```python
get_ticker_rankings(days=7, limit=20, min_mentions=5, mode="bearish", history=True)
```

## Defaults and boundaries

Omitted/null `min_mentions` uses 1 for `mentions` and 3 for `bullish`/`bearish`.
Explicit values clamp to 1-1000. `days` defaults to 1 and clamps to 1-365 rolling
publication days before now; `limit` defaults to 20 and clamps to 1-50. There is
no historical end date, offset or pagination. `history=True` adds daily CSV for
at most the first 10 selected tickers over the same period and source selection.

Mention mode sorts by count, then average sentiment, and retains source and
direction mixes. Sentiment modes sort by average sentiment, then count, and
retain separate direction counts. They rank the entire eligible set: bullish
can include negative values and bearish can include positive values. They are
not LONG/SHORT idea filters. Known inverse ETF exposure normalization is unchanged.
Counts are mentions, not unique authors.

An empty `source_type` combines Twitter, YouTube, Substack/newsletter and Reddit.
For example:

```python
get_ticker_rankings(mode="bearish", days=7, source_type="youtube", min_mentions=5)
```

Existing public-content and hidden-idea filters remain in effect. Future
publications and disabled news are excluded. Paid/unknown newsletter content
requires the existing explicit public-preview-only visibility approval.
Only aggregates are returned, without individual ideas or original source bodies.
General MCP request controls are unchanged; this consolidation adds no dedicated quota.

Refresh your client tool catalog after deployment. The former mention and
sentiment command names are removed, rather than kept as callable aliases.
All ranking calculations, output columns and optional daily history are preserved.
