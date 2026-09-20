# search_youtube_research

Search Buzzberg-derived YouTube research notes from the last seven days.

```text
Use Buzzberg YouTube research notes from the last 7 days to find discussions
about power bottlenecks and data-center capex. Summarize the thesis, tickers,
catalysts, risks, and source links.
```

Buzzberg returns derived notes and extracted market intelligence, not raw
transcripts.

## Query search and focused ticker report

```python
search_youtube_research(query="AI power", days=7, limit=10)
search_youtube_research(query="AI power", ticker="NVDA", days=7)
search_youtube_research(ticker="MU", days=7, limit=10)
```

Query search returns matching derived notes. Ticker without query returns only
ticker-scoped evidence, grouped into bullish/bearish/context/position sections
and Source Notes with video links. Both missing is refused. Both modes retain
seven-day and twenty-note caps (defaults 7/10), with no raw transcripts or
archive pagination. The focused report can include up to six extracted ideas
per note and twelve bullets per direction group; twenty notes is not twenty ideas.
