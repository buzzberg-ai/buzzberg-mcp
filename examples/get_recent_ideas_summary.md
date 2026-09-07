# Recent-ideas summary

Ask: "Summarize Buzzberg ideas from the last 24 hours."

```json
{"window": "24h", "delivery": "auto"}
```

Call `get_recent_ideas_summary`, read `agent_guide` and follow every exact
`pagination.next_cursor` until `has_more=false`. Intermediate pages can have
`summary_context=null`; the final page supplies the global context and complete
`analysis_instruction`. Read that instruction in full before analysis and its
delivery checklist again before output.

The current report has six interactive Top-10 tabs: Alpha Calls, Top Mentions,
Mentions Spike, Consensus, First Calls and Shorts. Use its saved rankings and
metrics. For Alpha Calls, read all supplied actionable theses for the
20-candidate shortlist and follow the bounded host review specified by the
instruction. Detailed blocks follow the prescribed order, expanding up to
three previously unseen tickers per section. Do not repeat a detailed ticker.

The grouped-v5 metadata covers the full query, while `data_projection` declares
the narrower report evidence. This tool does not export every market-wide
thesis. Use `get_recent_idea_candidates` for that research workflow.

For daily updates on a selected portfolio of up to 50 tickers, use
`get_portfolio_summary`. It returns all full LONG/SHORT/AVOID theses for those
tickers, one table and every ticker's detail without the market-wide ranking
or detail-count limits.
