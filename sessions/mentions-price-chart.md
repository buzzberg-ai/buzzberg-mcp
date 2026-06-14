# Mentions Vs Price Chart

Use this to separate "nobody is talking about it yet" from "everyone has already
found it." Mention volume is often the best Buzzberg proxy for narrative
attention.

## The ask

> Use Buzzberg to compare SIVE's mention volume against price over the last
> 90 days.
>
> Find attention spikes, explain what caused them, and classify the setup as
> ignored, discovered, crowded, or exhausted. I care less about exact numbers
> and more about what the attention pattern means.

## Tools Claude will chain

1. `get_ticker_timeseries(ticker="SIVE", days=90)` — daily mentions + close
2. `read_ticker_content(ticker="SIVE", days=30, limit=30)` — source snippets
   behind the latest spikes
3. `search_trade_ideas(ticker="SIVE", days=30, limit=30)` — directional calls
   behind the attention

## What you'll get

> **Attention read:** Buzzberg can show whether SIVE is being discovered,
> crowded, or ignored by comparing daily mentions, sentiment, and price closes.
> The point is not the exact row count; it is whether attention arrived before
> price, during the move, or after the move.
>
> **Healthy version:** mentions rise before or with price, and source snippets
> show new information or new catalysts.
>
> **Late version:** mentions spike after a vertical price move, but the content
> repeats the same already-known thesis. That is more crowding than discovery.
>
> **What to read next:** the source snippets on the biggest mention-spike days,
> especially where new speakers enter the conversation rather than the same
> accounts repeating the same thesis.

## Classification Cheat Sheet

- **Ignored:** low mentions, flat sentiment, price not moving much.
- **Discovered:** mentions rise before price or during early breakout.
- **Crowded:** mentions spike after a large move, with little new thesis detail.
- **Exhausted:** price stops responding to positive attention.

## Follow-up prompts

- *"Show me the three biggest SIVE mention-spike days and what caused each."*
- *"Did new speakers enter the SIVE story, or is it the same accounts repeating it?"*
- *"Compare mention spikes to direction: were they mostly LONG, WATCH, or neutral?"*
