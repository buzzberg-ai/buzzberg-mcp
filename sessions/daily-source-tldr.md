# Daily Source TLDRs

Use this when you want Claude, Codex, or another MCP client to read the last 24
hours of Buzzberg source material and write a market TLDR.

This is not a price screen. It is a source-reading workflow: Buzzberg returns
the underlying public text, transcript, or trade-idea tweet text, and your AI
agent turns it into a summary with themes, examples, disagreements, and tickers.

## Top-50 Speaker Tweets

Ask:

```text
Use Buzzberg to summarize the last 24h of top-50 speaker tweets.
What are the main themes, crowded trades, new tickers, and disagreements?
Quote examples.
```

What Buzzberg provides:

- Full text of top-speaker tweets from the last 24 hours where Buzzberg found a
  trade idea.
- Speaker handle and speaker rank when available.
- Tickers attached to the tweet.
- Buzzberg trade idea direction, such as long, short, watch, or avoid.
- Source URL.

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

## Public Substack / Newsletter Text

Ask:

```text
Use Buzzberg to read public Substack text from the last 24h.
Give me a market TLDR and list tickers with the strongest narratives.
Quote examples.
```

What Buzzberg provides:

- Public/free newsletter or Substack text from the last 24 hours.
- For paid posts, only the public preview visible before the paywall.
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

## YouTube Transcripts

Ask:

```text
Use Buzzberg to read YouTube transcripts from the last 24h.
What are speakers worried about that is not obvious from price action?
Quote examples.
```

What Buzzberg provides:

- Transcript text from YouTube videos ingested in the last 24 hours.
- Timestamped transcript segments when available.
- Speaker/source, video URL, title, and related tickers when available.

Good follow-ups:

```text
Pull out the non-obvious risks and group them by macro, AI capex, credit, and earnings.
```

```text
Which tickers were discussed with the most conviction?
```

```text
Give me a timestamped quote list I can click through later.
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

- This source-reading tool is capped to the last 24 hours.
- Paid Substack content is not returned beyond the public/free preview.
- Twitter defaults to trade-idea tweets, not every tweet from every speaker.
- Large responses are capped so clients do not freeze on huge transcripts.
