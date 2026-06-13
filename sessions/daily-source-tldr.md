# Daily Source TLDRs

Use this when you want Claude, Codex, or another MCP client to build a market
TLDR from Buzzberg source context.

This is not a price screen. It is a bounded research workflow: Buzzberg returns
top-speaker ticker-idea tweet text for the last 24 hours, plus YouTube and
Substack/newsletter TLDRs with extracted trade ideas for up to 7 days. Your AI
agent turns that into a summary with themes, examples, disagreements, and
tickers.

## Top-50 Speaker Tweets

Ask:

```text
Use Buzzberg to summarize the last 24h of top-50 speaker tweets.
What are the main themes, crowded trades, new tickers, and disagreements?
Quote examples.
```

What Buzzberg provides:

- Full text of top-speaker tweets from the last 24 hours where Buzzberg found a
  ticker idea.
- Speaker handle and speaker rank when available.
- Tickers attached to the tweet.
- Buzzberg direction: `LONG`, `SHORT`, `WATCH`, `AVOID`, or `NEUTRAL`.
- Source URL.

Default mode is high-signal: it does **not** return every tweet by the top-50
speakers. It returns tweets that Buzzberg mapped to a ticker idea. In practice,
100-200 items is already enough for a strong daily TLDR; use more only when you
want keyword counts or broader theme mining.

Good follow-ups:

```text
Which tickers appeared for the first time today?
```

```text
Which trades look crowded because multiple top speakers repeated the same thesis?
```

```text
Which speakers disagree, and what exactly did each side say?
```

## Substack / Newsletter TLDRs

Ask:

```text
Use Buzzberg to build a 7-day newsletter thesis map.
Show the strongest ticker narratives, key evidence, weak claims,
and what changed this week. Separate hard data from vibes.
```

What Buzzberg provides:

- Buzzberg TLDRs and extracted trade ideas from newsletter/Substack content.
- Public previews where available.
- Subscriber-only/full article bodies are not returned.
- Title, author/source, URL, published time, and related tickers when available.

Good follow-ups:

```text
Separate hard evidence from narrative claims.
```

```text
Which tickers have the strongest bull thesis, and which ones only have vibes?
```

```text
What changed today compared with the last week of Buzzberg sentiment?
```

## YouTube TLDRs

Ask:

```text
Use Buzzberg to find first-order and second-order effects from this week's
YouTube market discussions.
Which tickers benefit directly, which suppliers or competitors are second-order
plays, and what risks are speakers worried about?
```

What Buzzberg provides:

- Buzzberg TLDRs and extracted trade ideas from YouTube videos.
- Speaker/source, video URL, title, and related tickers when available.

Raw transcripts and timestamped transcript dumps are not returned through MCP.
Ask for ticker/source follow-ups when you need more context around a specific
video.

Good follow-ups:

```text
Pull out the non-obvious risks and group them by macro, AI capex, credit, and earnings.
```

```text
Which tickers were discussed with the most conviction?
```

```text
Give me the video links I should click through later.
```

## Repeated Words / Theme Counts

Ask:

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples and point to the tickers each theme is about.
```

Buzzberg does not pre-compute this word count. It returns the source text, and
your AI agent counts words and phrases from that text.

Good follow-ups:

```text
Which repeated words look like real market themes rather than noise?
```

```text
Map each repeated theme to the tickers speakers are trading.
```

```text
Which theme is most underpriced based on low mentions but strong conviction?
```

## Limits During Private Beta

- Twitter/X source text is capped to the last 24 hours.
- YouTube and Substack/newsletter context supports up to 7 days, but returns
  TLDRs and extracted trade ideas, not raw transcripts or full articles.
- Twitter defaults to ticker-idea tweets, not every tweet from every speaker.
- Large responses are capped so clients do not freeze.
