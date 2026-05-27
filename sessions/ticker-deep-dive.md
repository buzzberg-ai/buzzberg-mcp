# Narrative Ticker Deep Dive

Use this when you do not want another generic ticker summary. Buzzberg is most
useful when Claude reads the social/source graph: who is pushing the idea, what
changed recently, whether the narrative is early or already crowded, and what
risk the bull camp is not discussing.

## The ask

> Use Buzzberg to do a narrative deep dive on NOK / Nokia.
>
> I want the short verdict, the core bull narrative, who is pushing it, what is
> missing from the bear side, whether the setup is early or crowded, and what I
> should watch next. Use Buzzberg data only.

## Tools Claude will chain

1. `get_ticker_info(ticker="NOK")` — overview, top speakers, recent ideas
2. `get_ticker_mentions(ticker="NOK")` — 24h / 7d / 30d attention by source
3. `get_sentiment(ticker="NOK", days=30)` — directional bias and speaker mix
4. `compare_speakers(ticker="NOK", days=30)` — whether there is a real bear camp
5. `search_trade_ideas(ticker="NOK", days=30, limit=20)` — recent theses and quotes
6. `read_ticker_content(ticker="NOK", days=30, limit=20)` — source snippets
7. `get_ticker_timeseries(ticker="NOK", days=90)` — price/sentiment/mentions context

## What you'll get (illustrative)

Claude should write like an analyst, not like a dashboard:

> **Short verdict:** Buzzberg shows Nokia as a bullish but increasingly crowded
> AI-infrastructure rerate story. The edge is not "Nokia is cheap"; it is that a
> cluster of active speakers is reframing Nokia from legacy telecom vendor to
> AI-RAN / optical / edge compute infrastructure.
>
> **What bulls are buying:**
> - Insider buying after the move, not just at the lows.
> - AI-RAN / edge AI narrative tied to NVIDIA, telecom base stations, and
>   distributed compute.
> - Optical backbone / Infinera angle: AI traffic needs coherent optical
>   capacity, and bulls compare the setup to other optical winners.
> - Multiple rerate: "legacy telecom wrapper" becoming "AI network
>   infrastructure".
>
> **Who is pushing it:** The signal is concentrated in a small group of active
> X accounts. That is useful for momentum discovery, but it also means the
> narrative may be less independently confirmed than it looks.
>
> **What is missing:** Very little bear-side discussion. That does not mean
> there is no risk; it means Buzzberg's current source graph is not surfacing
> much debate. The key diligence questions are backlog, margins after Infinera,
> real AI-RAN economics, and whether the rerate is already priced.
>
> **Trading read:** Bullish momentum setup, not clean value. Better after a
> pullback/consolidation or after confirmation from orders / analysts / insider
> follow-through.

## Drill down

- *"Show me only the bear case for NOK, even if it is weak."* →
  `search_trade_ideas(ticker="NOK", direction="short", days=90)` plus
  `compare_speakers(ticker="NOK", days=90)`
- *"Which speaker is driving the Nokia narrative most?"* →
  `compare_speakers(ticker="NOK", days=30)` and `get_speaker_profile(...)`
- *"Is this move crowded?"* → `get_ticker_timeseries(ticker="NOK", days=90)`
  and look for mention spikes after price spikes
- *"Read the actual source snippets behind the AI-RAN thesis."* →
  `read_ticker_content(ticker="NOK", days=30, limit=30, verbose=True)`

## Tips

- Ask for *"what Buzzberg uniquely sees"* to force Claude away from generic
  company background.
- Ask for *"what is missing"*; a one-sided bull graph is often a risk signal.
- Use `read_ticker_content` for source snippets and `search_trade_ideas` when
  you need speaker / direction / confidence filters.
