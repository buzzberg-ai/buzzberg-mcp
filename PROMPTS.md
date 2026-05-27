# Buzzberg MCP Prompt Cookbook

Use these prompts in Claude Desktop, Claude Code, Cursor, Cline, or any MCP
client after connecting Buzzberg.

Private beta uses SSE at `https://mcp.buzzberg.ai/sse`. If a client asks for a
Streamable HTTP `/mcp` URL, use the SSE option for now.

## Good Prompt Style

Ask Claude to use Buzzberg explicitly:

```text
Use Buzzberg tools for this. If Buzzberg has no data, say so. Cite speakers,
dates, tickers, and source types when available. Do not invent missing data.
This is research, not financial advice.
```

## First Smoke Test

```text
Use Buzzberg to get the current price for BTC.
```

Expected tools:

- `get_price`

## Ticker Deep Dive

```text
Use Buzzberg to analyze OUST.

I want:
1. Basic ticker info.
2. Who has mentioned OUST recently.
3. What the bullish thesis is.
4. What the bearish thesis or risks are.
5. Whether speakers disagree.
6. What I should watch next.

Use Buzzberg data only. If Buzzberg has no OUST data, say that clearly.
```

Expected tools:

- `get_ticker_info`
- `get_ticker_mentions`
- `get_sentiment`
- `compare_speakers`
- `search_trade_ideas`
- `get_price`

## Risk And Bear Case

```text
Use Buzzberg to build the bear case for NVDA from the last 30 days.

Find negative or cautious mentions, speaker disagreement, sentiment divergence,
and any repeated risk themes. Separate evidence from your interpretation.
```

Expected tools:

- `search_trade_ideas`
- `get_sentiment`
- `compare_speakers`
- `get_ticker_mentions`

## Who Said What

```text
Use Buzzberg to show who talked about TSLA recently.

Group by speaker. For each speaker, show their stance, confidence if available,
the source type, and the latest date. End with a one-paragraph consensus view.
```

Expected tools:

- `get_ticker_mentions`
- `compare_speakers`
- `search_trade_ideas`

## Contrarian Scan

```text
Use Buzzberg to find contrarian opportunities this week.

Look for tickers where speakers disagree, where sentiment is split, or where a
high-credibility speaker is against the crowd. Give me the top 5 and explain
why each one is interesting.
```

Expected tools:

- `get_sentiment_divergence`
- `compare_speakers`
- `get_price`

## Top Speaker Signals

```text
Use Buzzberg to find fresh long ideas from top-ranked speakers in the last 7
days. Prioritize ideas with clear thesis and confidence. Show ticker, speaker,
thesis, date, and source.
```

Expected tools:

- `get_top_speaker_signals`
- `search_trade_ideas`

## Speaker Due Diligence

```text
Use Buzzberg to profile Chamath Palihapitiya.

Show credibility, recent tickers, common themes, best recent signals if
available, and where his views differ from other speakers.
```

Expected tools:

- `get_speaker_profile`
- `search_trade_ideas`
- `compare_speakers`

## Morning Briefing

```text
Use Buzzberg to create a morning market briefing.

Include:
1. Latest portfolio snapshot.
2. Top fresh trade ideas.
3. Biggest sentiment divergences.
4. Most important recent content.
5. Three risks to watch today.
```

Expected tools:

- `get_portfolio`
- `search_trade_ideas`
- `get_sentiment_divergence`
- `get_recent_content`

## Watchlist Builder

This uses write tools and changes only your Buzzberg account.

```text
Use Buzzberg to find five tickers I should monitor from top speaker signals.
Explain why each belongs on a watchlist. Then ask me before adding them to my
Buzzberg watchlist.
```

Expected tools:

- `get_top_speaker_signals`
- `search_trade_ideas`
- `add_to_watchlist`

## Save An Idea

This uses write tools and changes only your Buzzberg account.

```text
Use Buzzberg to find the strongest long idea for AMD this week. Summarize the
thesis, risks, speaker, confidence, and source. Ask me before saving it to my
Buzzberg saved ideas.
```

Expected tools:

- `search_trade_ideas`
- `get_sentiment`
- `save_trade_idea`

## Crypto Vs Stocks Sentiment

```text
Use Buzzberg to compare sentiment around BTC, ETH, NVDA, and TSLA over the last
14 days. Show which assets have the strongest positive sentiment, the most
disagreement, and the clearest risk flags.
```

Expected tools:

- `get_sentiment`
- `compare_speakers`
- `get_price`

## Chart Sentiment And Mentions

```text
Use Buzzberg to create a 90-day chart dataset for NOK.

Return daily rows with close price, mention count, average sentiment, and
long/short/neutral/avoid counts. Then explain whether price moves seem to lead
or lag Buzzberg sentiment.
```

Expected tools:

- `get_ticker_timeseries`
- `read_ticker_content`
- `search_trade_ideas`

## Search The Content Archive

```text
Use Buzzberg to search recent content for "robotaxi". Show the most relevant
items, mentioned tickers, source type, speaker if available, and why each item
matters.
```

Expected tools:

- `search_content`
- `read_ticker_content`

## Output Format To Ask For

For investment research prompts, this format works well:

```text
Return:
- One-line verdict
- Evidence table
- Bull case
- Bear case / risks
- Speaker disagreement
- What changed recently
- What to watch next
- Data gaps
```

## If Something Looks Wrong

If Claude says there are no tools, fully quit and reopen the client.

If Claude reports `401 Unauthorized`, revoke and recreate your key in
**Profile -> MCP Access**.

If a Python client gets `404` on `/mcp`, switch it to SSE at
`https://mcp.buzzberg.ai/sse`.
