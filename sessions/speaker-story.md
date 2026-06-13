# Speaker Story / Author History

Use this when you want to understand how one author developed an idea over
time, without reading every raw tweet or article.

## Prompt

```text
Use Buzzberg to analyze Serenity's NOK trade idea history.

I want:
1. The first recorded NOK idea from Serenity.
2. The recent NOK ideas from the last 90 days.
3. A daily history table for Serenity × NOK over 180 days.
4. Whether Serenity's stance changed: first mention, flips, increasing/decreasing conviction.
5. What I should watch next.

Use Buzzberg data only. Do not fetch raw source text.
```

## What the agent should call

```text
get_speaker_trade_ideas(speaker_name="Serenity", ticker="NOK", sort="oldest", limit=1, days=365, max_per_day=10)
get_speaker_trade_ideas(speaker_name="Serenity", ticker="NOK", sort="recent", limit=30, days=90, max_per_day=10)
get_speaker_ticker_history(speaker_name="Serenity", ticker="NOK", days=180)
```

## What this is good for

- Finding the origin of a trade idea.
- Seeing whether an author is adding, fading, flipping, or just repeating.
- Separating a real evolving thesis from one viral post.
- Building charts of speaker sentiment / mentions vs price.

## Follow-up prompts

```text
Show me the first time Serenity mentioned NOK, then compare it with her most
recent NOK mention. What changed?
```

```text
For Serenity x NOK, use the daily history CSV to identify the three biggest
sentiment or mention inflection points. Then tell me which source snippets I
should read next.
```

```text
Use Buzzberg to analyze Leo's last 90 days of trade ideas without choosing a
ticker first. Which tickers and narratives does he keep returning to?
```

```text
Use Buzzberg to show Serenity's all-time trade ideas with thesis.
Limit it to 100 ideas and keep at most 5 ideas per day.
Which tickers did she mention most, where did she flip direction, and how have
her views changed?
```

```text
Use Buzzberg to compare Serenity's NOK stance with other speakers talking
about NOK. Who agrees, who disagrees, and where is the thesis concentrated?
```

## Guardrails

These tools are intentionally scoped. Speaker trade history requires one
speaker and returns at most 200 ideas, with `max_per_day` defaulting to 10 so a
single noisy day cannot dominate the output. The daily history tool also
requires one ticker. Both return extracted trade-idea summaries and daily
aggregates, not a bulk export of raw Buzzberg source text.
