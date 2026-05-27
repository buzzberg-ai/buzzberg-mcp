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

## Narrative Ticker Deep Dive

```text
Use Buzzberg to do a narrative deep dive on NOK / Nokia.

I want:
1. The short verdict.
2. What Buzzberg uniquely sees from X, YouTube, newsletters, and Reddit.
3. The main bull narrative and the strongest catalysts.
4. Who is pushing the idea, and whether the signal is concentrated.
5. What is missing or under-discussed on the bear side.
6. Whether this looks early, crowded, or late.
7. What I should watch next.

Use Buzzberg data only. If Buzzberg has no NOK data, say that clearly.
```

Expected tools:

- `get_ticker_info`
- `get_ticker_mentions`
- `get_sentiment`
- `compare_speakers`
- `search_trade_ideas`
- `read_ticker_content`
- `get_ticker_timeseries`
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

## Most Buzzed Tickers

```text
Use Buzzberg to show the most buzzed tickers in the last 24 hours.

For each ticker, show mention count, source mix, sentiment, and why people are
talking about it. Then separate fresh discovery from crowded post-move chatter.
```

Expected tools:

- `get_most_mentioned_tickers`
- `read_ticker_content`
- `search_trade_ideas`

## 7-Day Sentiment Leaders

```text
Use Buzzberg to find the strongest bullish and bearish ticker narratives over
the last 7 days.

Use at least 5 mentions per ticker. Include historical daily rows if useful, but
do not just dump the table — explain what changed and what to watch next.
```

Expected tools:

- `get_top_sentiment_tickers`
- `get_most_mentioned_tickers`
- `read_ticker_content`

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

## Sentiment Vs Price Chart

```text
Use Buzzberg to create a 90-day sentiment vs price read for NOK.

Use daily sentiment, mention counts, and close prices. Do not just print the
table. Explain:
1. Did sentiment turn before price, after price, or with price?
2. Which days look like narrative inflection points?
3. Did the latest price move happen with broad participation or thin attention?
4. What follow-up content should I read?
```

Expected tools:

- `get_ticker_timeseries`
- `read_ticker_content`
- `search_trade_ideas`

## Mentions Vs Price Chart

```text
Use Buzzberg to compare NOK's mention volume against price over the last 90 days.

Find attention spikes, then explain what caused them. I care less about the
exact numbers and more about the narrative: was the stock ignored, discovered,
crowded, or exhausted?
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
