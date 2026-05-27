# Buzzberg MCP Tools

> Private Beta: tool names and signatures may change before broader beta.

## search_trade_ideas

Search trade ideas from Buzzberg. Filter by ticker, source, speaker, confidence, direction.

**Inputs:**
- `ticker` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `speaker` (optional, str, default `''`)
- `min_confidence` (optional, float, default `0.0`)
- `direction` (optional, str, default `''`)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `20`)

**Example prompt:**
> "Use `search_trade_ideas` for a Buzzberg analysis."

**Returns:** Markdown response from `search_trade_ideas`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/search_trade_ideas.md](examples/search_trade_ideas.md)

## get_top_speakers

List Buzzberg's top speakers by lifetime Alpha-rank.

**Inputs:**
- `limit` (optional, int, default `25`)

**Example prompt:**
> "Use `get_top_speakers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_speakers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_speakers.md](examples/get_top_speakers.md)

## get_top_speaker_signals

Fresh trade ideas from the top-N Buzzberg speakers within a time window.

**Inputs:**
- `top_n` (optional, int, default `50`)
- `window` (optional, str, default `'7d'`)
- `signal` (optional, str, default `'first_flip'`)
- `direction` (optional, str, default `''`)
- `source_type` (optional, str, default `''`)
- `limit` (optional, int, default `30`)

**Example prompt:**
> "Use `get_top_speaker_signals` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_speaker_signals`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_speaker_signals.md](examples/get_top_speaker_signals.md)

## get_sentiment

Get sentiment analysis for a ticker: average sentiment, breakdown by direction, by speaker tier.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_sentiment` for a Buzzberg analysis."

**Returns:** Markdown response from `get_sentiment`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_sentiment.md](examples/get_sentiment.md)

## get_ticker_timeseries

Get daily sentiment, mention counts, and cached close prices for charting.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `90`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_ticker_timeseries` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_timeseries`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_timeseries.md](examples/get_ticker_timeseries.md)

## get_most_mentioned_tickers

Rank tickers by Buzzberg mention volume over a lookback window.

**Inputs:**
- `days` (optional, int, default `1`)
- `limit` (optional, int, default `20`)
- `source_type` (optional, str, default `''`)
- `min_mentions` (optional, int, default `1`)
- `history` (optional, bool, default `False`)

**Example prompt:**
> "Use `get_most_mentioned_tickers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_most_mentioned_tickers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_most_mentioned_tickers.md](examples/get_most_mentioned_tickers.md)

## get_top_sentiment_tickers

Rank tickers by strongest bullish or bearish Buzzberg sentiment.

**Inputs:**
- `days` (optional, int, default `1`)
- `limit` (optional, int, default `20`)
- `min_mentions` (optional, int, default `3`)
- `direction` (optional, str, default `'bullish'`)
- `source_type` (optional, str, default `''`)
- `history` (optional, bool, default `False`)

**Example prompt:**
> "Use `get_top_sentiment_tickers` for a Buzzberg analysis."

**Returns:** Markdown response from `get_top_sentiment_tickers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_top_sentiment_tickers.md](examples/get_top_sentiment_tickers.md)

## get_sentiment_divergence

Find tickers where speakers disagree most (high divergence in sentiment).

**Inputs:**
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)

**Example prompt:**
> "Use `get_sentiment_divergence` for a Buzzberg analysis."

**Returns:** Markdown response from `get_sentiment_divergence`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_sentiment_divergence.md](examples/get_sentiment_divergence.md)

## get_portfolio

Get the latest AI-generated portfolio snapshot with positions and P&L.

**Inputs:**
- `date` (optional, str, default `''`)

**Example prompt:**
> "Use `get_portfolio` for a Buzzberg analysis."

**Returns:** Markdown response from `get_portfolio`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_portfolio.md](examples/get_portfolio.md)

## get_ticker_info

Get detailed info for a ticker: mention count, top speakers, recent ideas, price.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_ticker_info` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_info`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_info.md](examples/get_ticker_info.md)

## get_speaker_profile

Get speaker profile: credibility, role, mention frequency, top tickers.

**Inputs:**
- `speaker_name` (required, str)

**Example prompt:**
> "Use `get_speaker_profile` for a Buzzberg analysis."

**Returns:** Markdown response from `get_speaker_profile`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_speaker_profile.md](examples/get_speaker_profile.md)

## compare_speakers

Compare what different speakers say about a ticker. Shows who's bullish vs bearish.

**Inputs:**
- `ticker` (required, str)
- `days` (optional, int, default `30`)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `compare_speakers` for a Buzzberg analysis."

**Returns:** Markdown response from `compare_speakers`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/compare_speakers.md](examples/compare_speakers.md)

## get_recent_content

Get latest content (videos, articles, tweets) from Buzzberg.

**Inputs:**
- `source_type` (optional, str, default `''`)
- `limit` (optional, int, default `10`)

**Example prompt:**
> "Use `get_recent_content` for a Buzzberg analysis."

**Returns:** Markdown response from `get_recent_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_recent_content.md](examples/get_recent_content.md)

## get_price

Get current prices for tickers via Massive (stocks) / Binance (crypto).

**Inputs:**
- `tickers` (required, list[str])

**Example prompt:**
> "Use `get_price` for a Buzzberg analysis."

**Returns:** Markdown response from `get_price`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_price.md](examples/get_price.md)

## search_content

Search content by keyword in title.

**Inputs:**
- `query` (required, str)
- `limit` (optional, int, default `10`)

**Example prompt:**
> "Use `search_content` for a Buzzberg analysis."

**Returns:** Markdown response from `search_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/search_content.md](examples/search_content.md)

## get_ticker_mentions

Count mentions of a ticker across 24h / 7d / 30d windows, broken down by source.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)

**Example prompt:**
> "Use `get_ticker_mentions` for a Buzzberg analysis."

**Returns:** Markdown response from `get_ticker_mentions`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/get_ticker_mentions.md](examples/get_ticker_mentions.md)

## read_ticker_content

Read the actual text bodies of content mentioning a ticker.

**Inputs:**
- `ticker` (required, str)
- `source_type` (optional, str, default `''`)
- `days` (optional, int, default `7`)
- `limit` (optional, int, default `10`)
- `verbose` (optional, bool, default `False`)

**Example prompt:**
> "Use `read_ticker_content` for a Buzzberg analysis."

**Returns:** Markdown response from `read_ticker_content`.

**Scope:** Read-only. Public Buzzberg market-intelligence data.

**Full example:** [examples/read_ticker_content.md](examples/read_ticker_content.md)

## add_to_watchlist

[BETA] Add a ticker to user's watchlist.

**Inputs:**
- `ticker` (required, str)
- `user_email` (optional, str, default `''`)

**Example prompt:**
> "Use `add_to_watchlist` for a Buzzberg analysis."

**Returns:** Markdown response from `add_to_watchlist`.

**Scope:** WRITE — modifies only data owned by the API key owner.

**Full example:** [examples/add_to_watchlist.md](examples/add_to_watchlist.md)

## remove_from_watchlist

[BETA] Remove a ticker from user's watchlist.

**Inputs:**
- `ticker` (required, str)
- `user_email` (optional, str, default `''`)

**Example prompt:**
> "Use `remove_from_watchlist` for a Buzzberg analysis."

**Returns:** Markdown response from `remove_from_watchlist`.

**Scope:** WRITE — modifies only data owned by the API key owner.

**Full example:** [examples/remove_from_watchlist.md](examples/remove_from_watchlist.md)

## save_trade_idea

[BETA] Bookmark a trade idea by its ID.

**Inputs:**
- `idea_id` (required, int)
- `user_email` (optional, str, default `''`)

**Example prompt:**
> "Use `save_trade_idea` for a Buzzberg analysis."

**Returns:** Markdown response from `save_trade_idea`.

**Scope:** WRITE — modifies only data owned by the API key owner.

**Full example:** [examples/save_trade_idea.md](examples/save_trade_idea.md)
