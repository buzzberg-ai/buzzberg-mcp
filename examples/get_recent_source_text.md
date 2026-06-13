# get_recent_source_text

Use this tool when you want Claude/Codex to build a market TLDR from bounded
Buzzberg source context.

Important boundary: Twitter/X can return recent top-speaker ticker-idea tweet
text for the last 24 hours. YouTube and Substack/newsletters return Buzzberg
TLDRs and extracted trade ideas, not raw transcripts or full article bodies,
for up to 7 days.

## Substack / Newsletter TLDR

Prompt:

> Use Buzzberg to read Substack/newsletter TLDRs and trade ideas from the last
> 7 days. Summarize the main market themes, tickers, bullish theses, bearish
> theses, and what changed. Quote short examples where Buzzberg has public
> preview text.

Tool call:

```json
{
  "source_type": "newsletter",
  "days": 7,
  "limit": 20
}
```

## YouTube TLDR

Prompt:

> Use Buzzberg to read YouTube TLDRs and trade ideas from the last 7 days. Give
> me the top market narratives, tickers discussed, speaker disagreements, and
> anything that sounds like a new risk.

Tool call:

```json
{
  "source_type": "youtube",
  "days": 7,
  "limit": 30
}
```

## Top-Speaker Twitter TLDR

Prompt:

> Use Buzzberg to read tweets from top-50 speakers in the last 24 hours. Only
> use tweets where Buzzberg found ticker ideas: LONG, SHORT, WATCH, AVOID, or
> NEUTRAL. Summarize the main topics, crowded trades, new tickers,
> disagreements, and repeated words like "bottleneck" or "power".

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
Use Buzzberg to read Substack/newsletter TLDRs and trade ideas from the last 7d.
Give me a market TLDR and list tickers with the strongest narratives.
```

```text
Use Buzzberg to read YouTube TLDRs and trade ideas from the last 7d.
What are speakers worried about that is not obvious from price action?
```

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples.
```

## Notes

- Twitter/X is capped to the last 24 hours during private beta.
- YouTube and newsletter/Substack support up to 7 days, but return TLDRs and
  extracted trade ideas, not raw transcripts or full article bodies.
- Subscriber-only Substack text is not returned.
- Twitter defaults to Buzzberg ticker-idea tweets, not every tweet. `WATCH` and
  `AVOID` are included because they are still useful market signals.
- `include_segments` is deprecated/no-op. Raw YouTube transcript segments are
  not returned through MCP.
