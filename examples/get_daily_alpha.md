# Daily Alpha

Ask for a Daily Alpha briefing. The host calls `get_daily_alpha` once and
follows `analysis_instruction` in your language. Available after server release;
reconnect if your client has cached the previous catalog.

```json
{}
```

Optional priorities:

```json
{
  "preferred_sources": ["SemiAnalysis", "All-In", "BG2", "Invest Like the Best", "FedGuy"],
  "preferred_speakers": ["Joseph Wang"],
  "preferred_subreddits": ["stocks", "investing"],
  "include_reddit": true,
  "reddit_order": "score"
}
```

The response is `DailyAlphaResult` schema 1.0.0, exposed as JSON text and
structuredContent. It contains the latest two published editions within seven
days, not an archive. No date, cursor or historical edition argument exists.
Each preference list accepts at most 20 names of 100 characters. Preferences
only reorder available material, are not saved and do not fetch missing episodes.

The host presents:

1. SPY, QQQ, US 10Y yield/change in basis points, gold (explicit GLD ETF proxy),
   and BTC with a sampled rolling 24h change when available. All prices are
   database-only. Omit missing instruments (including US 10Y), unavailable
   changes and quote-save timestamp boilerplate. Preserve currencies and session
   labels; premarket/after-hours changes are separate when available.
   BTC compares the current stored price with a same-currency observation near
   24h earlier. Its intraday history starts accumulating after server release.
2. Three or four latest published narratives with linked evidence. Broad
   related-ticker coverage is not a count of people endorsing the exact claim.
3. Two to four videos/posts with thesis, date, named speaker and current Authors
   rank/sample size when available. A video guest unrelated to the selected
   finding cannot raise that finding's reputation. Preview-only sources stay labeled.
4. Selected Reddit discussions sorted by saved score or comments and deduplicated
   by subject. Score is not an exact upvote count. This covers selected materials
   in these two editions, not a complete Reddit ranking or live poll.

No transcript fragments, original evidence quotes or private source bodies are
returned. Missing editions and partial source access stay explicit. Missing
market values stay in metadata and do not create empty rows in the report.
