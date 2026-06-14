# get_recent_source_text

Use this tool when you want Claude/Codex to build a market TLDR from bounded
Buzzberg source context.

Important boundary: Twitter/X can return recent top-speaker ticker-idea tweet
text for the last 24 hours. YouTube and Substack/newsletters return Buzzberg
TLDRs and extracted trade ideas, not raw YouTube text or full article bodies,
for up to 7 days.

## Research Posts / Alpha Extraction

Prompt:

> Use Buzzberg research posts from the last 24h. Find the strongest new alpha
> ideas, second-order beneficiaries, repeated evidence, weak assumptions, and
> tickers worth a deeper dive. Quote short examples.

Tool call:

```json
{
  "source_type": "twitter",
  "post_kind": "research",
  "speaker_rank_limit": 50,
  "days": 1,
  "limit": 100
}
```

## Stock Lists / Watchlist Candidates

Prompt:

> Use Buzzberg stock-list posts from the last 7 days. Which tickers appear
> across multiple lists, what theme links them, which are fresh vs crowded, and
> which 10 should I research next?

Tool call:

```json
{
  "source_type": "newsletter",
  "post_kind": "stock list",
  "days": 7,
  "limit": 30
}
```

You can also use `source_type="twitter"` with `days=1` for same-day top-speaker
stock-list posts.

## Portfolio Updates

Prompt:

> Use Buzzberg portfolio-update posts from the last 7 days. What did speakers
> add, trim, close, or size up? Separate actual portfolio moves from generic
> commentary.

Tool call:

```json
{
  "source_type": "newsletter",
  "post_kind": "portfolio",
  "days": 7,
  "limit": 20
}
```

## Substack / Newsletter TLDR

Prompt:

> Use Buzzberg to build a 7-day newsletter thesis map. Show the strongest
> ticker narratives, key evidence, weak claims, and what changed this week.
> Separate hard data from vibes.

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

> Use Buzzberg to find first-order and second-order effects from this week's
> YouTube market discussions. Which tickers benefit directly, which suppliers
> or competitors are second-order plays, and what risks are speakers worried
> about?

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
Use Buzzberg to build a 7-day newsletter thesis map.
Show the strongest ticker narratives, key evidence, weak claims,
and what changed this week. Separate hard data from vibes.
```

```text
Use Buzzberg to find first-order and second-order effects from this week's
YouTube market discussions.
Which tickers benefit directly, which suppliers or competitors are second-order
plays, and what risks are speakers worried about?
```

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples.
```

## Notes

- Twitter/X is capped to the last 24 hours during private beta.
- YouTube and newsletter/Substack support up to 7 days, but return TLDRs and
  extracted trade ideas, not raw YouTube text or full article bodies.
- `post_kind` can be `research`, `portfolio_update`,
  `stock_recommendation_list`, `news`, or `other`. Friendly aliases like
  `stock list` and `portfolio` are accepted.
- Subscriber-only Substack text is not returned.
- Twitter defaults to Buzzberg ticker-idea tweets, not every tweet. `WATCH` and
  `AVOID` are included because they are still useful market signals.
- `include_segments` is deprecated/no-op. Raw YouTube transcript segments are
  not returned through MCP.
