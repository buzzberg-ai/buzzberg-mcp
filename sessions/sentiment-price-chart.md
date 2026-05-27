# Sentiment Vs Price Chart

Use this when you want Claude to explain the relationship between Buzzberg
sentiment and price instead of dumping a table. The edge is the interpretation:
did sentiment lead the move, confirm it, or show up after the trade was already
crowded?

## The ask

> Use Buzzberg to create a 90-day sentiment vs price read for NOK.
>
> Use daily sentiment, mention counts, and close prices. Do not just print the
> table. Explain whether sentiment led, lagged, or confirmed price; identify the
> narrative inflection days; and tell me which source snippets I should read.

## Tools Claude will chain

1. `get_ticker_timeseries(ticker="NOK", days=90)` — daily close, mentions,
   average sentiment, and direction counts
2. `read_ticker_content(ticker="NOK", days=30, limit=20)` — source snippets
   around recent inflection points
3. `search_trade_ideas(ticker="NOK", days=30, limit=20)` — thesis and quote
   details from recent calls

## What you'll get

Ask Claude to turn the CSV into an analyst read:

> **Read:** Sentiment is confirming the move rather than clearly leading it.
> The strongest positive sentiment appears after the stock has already rerated,
> which is consistent with a momentum narrative becoming visible to the crowd.
>
> **Inflection points:** Mention volume rose around the insider-buying and
> AI-RAN / NVIDIA narrative. That matters more than the exact sentiment decimal:
> the story changed from "legacy telecom" to "AI infrastructure optionality".
>
> **Risk flag:** If price keeps rising while sentiment stays high but mentions
> stop expanding, that can mean the narrative is no longer recruiting new
> buyers.

## Chart ideas

- Price line + average sentiment line.
- Price line + stacked direction bars (`long`, `short`, `neutral`, `avoid`).
- Annotate days where mentions jump and then ask `read_ticker_content` what
  caused the spike.

## Follow-up prompts

- *"Which days had the biggest sentiment jumps, and what content caused them?"*
- *"Show me dates where price rose but sentiment weakened."*
- *"Find the first day Buzzberg sentiment turned positive before the price move."*
