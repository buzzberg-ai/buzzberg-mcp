# get_recent_source_text

Use this tool when you want Claude/Codex to read the last 24 hours of source
material and write a TLDR from Buzzberg data.

## Substack TLDR

Prompt:

> Use Buzzberg to read Substack posts from the last 24 hours. Summarize the
> main market themes, tickers, bullish theses, bearish theses, and what changed
> today. Mention that paid posts include only the public/free preview.

Tool call:

```json
{
  "source_type": "newsletter",
  "limit": 20
}
```

## YouTube Transcript TLDR

Prompt:

> Use Buzzberg to read YouTube transcripts from the last 24 hours. Give me the
> top market narratives, tickers discussed, speaker disagreements, and anything
> that sounds like a new risk.

Tool call:

```json
{
  "source_type": "youtube",
  "limit": 10,
  "include_segments": true
}
```

## Top-Speaker Twitter TLDR

Prompt:

> Use Buzzberg to read tweets from top-50 speakers in the last 24 hours. Only
> use tweets where Buzzberg found trade ideas. Summarize the main topics,
> crowded trades, new tickers, disagreements, and repeated words like
> "bottleneck" or "power".

Tool call:

```json
{
  "source_type": "twitter",
  "speaker_rank_limit": 50,
  "limit": 200
}
```

## Repeated Words / Keyword Count

Prompt:

> Use Buzzberg Twitter data from top-50 speakers. How many times did they
> mention "bottleneck", "power", "AI capex", and "memory" in the last 24 hours?
> Quote examples and explain which tickers each theme points to.

Tool call:

```json
{
  "source_type": "twitter",
  "speaker_rank_limit": 50,
  "limit": 200
}
```

Claude/Codex can count words and phrases from the returned tweet text. Buzzberg
does not pre-compute the word count in this tool; the agent does it from the
source text it receives.

## Questions Users Can Ask

```text
Use Buzzberg to summarize the last 24h of top-50 speaker tweets.
What are the main themes, crowded trades, new tickers, and disagreements?
Quote examples.
```

```text
Use Buzzberg to read public Substack text from the last 24h.
Give me a market TLDR and list tickers with the strongest narratives.
```

```text
Use Buzzberg to read YouTube transcripts from the last 24h.
What are speakers worried about that is not obvious from price action?
```

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples.
```

## Notes

- This tool is capped to the last 24 hours during private beta.
- Paid Substack posts return only the public/free portion visible before the
  paywall.
- Twitter defaults to Buzzberg trade-idea tweets, not every tweet.
- YouTube can return timestamped transcript segments when available.
