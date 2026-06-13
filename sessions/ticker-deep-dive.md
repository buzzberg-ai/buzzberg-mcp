# Narrative Ticker Deep Dive

Use this when you do not want another generic ticker summary. Buzzberg is most
useful when Claude reads the social/source graph: who is pushing the idea, what
changed recently, whether the narrative is early or already crowded, and what
risk the bull camp is not discussing.

## The ask

> Use Buzzberg to deep dive SIVE.
>
> Who is talking about it, what is the core bull thesis, what are the strongest
> bear risks or missing arguments, and is this early discovery, building
> momentum, or crowded? Use Buzzberg data only.

## Tools Claude will chain

1. `get_ticker_info(ticker="SIVE")` — overview, top speakers, recent ideas
2. `get_ticker_mentions(ticker="SIVE")` — 24h / 7d / 30d attention by source
3. `get_sentiment(ticker="SIVE", days=30)` — directional bias and speaker mix
4. `compare_speakers(ticker="SIVE", days=30)` — whether there is a real bear camp
5. `search_trade_ideas(ticker="SIVE", days=30, limit=20)` — recent theses and quotes
6. `read_ticker_content(ticker="SIVE", days=30, limit=20)` — source snippets/TLDRs
7. `get_ticker_timeseries(ticker="SIVE", days=90)` — price/sentiment/mentions context

## What you'll get

Claude should write like an analyst, not like a dashboard:

> **Short verdict:** Buzzberg shows whether the SIVE story is still early,
> building, or crowded by combining who mentioned it, how often mentions spiked,
> what direction those ideas had, and whether there is any real bear camp.
>
> **What bulls are buying:** The agent should summarize the repeated thesis,
> catalysts, and evidence from Buzzberg trade ideas and source TLDRs. It should
> separate fresh information from repeated claims.
>
> **Who is pushing it:** The agent should name the speakers driving the story,
> whether the signal is concentrated, and whether top-ranked speakers are
> entering, repeating, or fading the idea.
>
> **What is missing:** A one-sided positive graph is not automatically safe.
> The agent should call out missing bear arguments, weak evidence, stale claims,
> and whether price already moved before attention spiked.
>
> **Trading read:** The output should be a research read: catalysts, risks,
> crowding, what to monitor next, and which source snippets deserve follow-up.

## Drill down

- *"Show me only the bear case for SIVE, even if it is weak."* →
  `search_trade_ideas(ticker="SIVE", direction="short", days=90)` plus
  `compare_speakers(ticker="SIVE", days=90)`
- *"Which speaker is driving the SIVE narrative most?"* →
  `compare_speakers(ticker="SIVE", days=30)` and `get_speaker_profile(...)`
- *"Is this move crowded?"* → `get_ticker_timeseries(ticker="SIVE", days=90)`
  and look for mention spikes after price spikes
- *"Which days caused the biggest attention spikes?"* →
  `get_ticker_timeseries(ticker="SIVE", days=90)` plus targeted
  `read_ticker_content(ticker="SIVE", days=30, limit=30, verbose=True)`

## Tips

- Ask for *"what Buzzberg uniquely sees"* to force Claude away from generic
  company background.
- Ask for *"what is missing"*; a one-sided bull graph is often a risk signal.
- Use `read_ticker_content` for source snippets and `search_trade_ideas` when
  you need speaker / direction / confidence filters.
