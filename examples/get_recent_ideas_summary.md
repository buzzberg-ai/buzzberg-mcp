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

By default, the report has six interactive Top-10 tabs: Alpha Calls, Top Mentions,
Mentions Spike, Consensus, First Calls and Shorts. Use its saved rankings and
metrics. For Alpha Calls, read all supplied actionable theses for the
20-candidate shortlist and follow the bounded host review specified by the
instruction. Detailed blocks follow the prescribed order, expanding up to
three previously unseen tickers per section by default. Do not repeat a detailed ticker.

## Choose sections, sectors and report size

Ask: "Show only Alpha Calls for Information Technology and Crypto, with five
detailed tickers."

```json
{
  "window": "24h",
  "sections": ["alpha_calls"],
  "sectors": ["Information Technology", "Crypto"],
  "table_limit": 10,
  "detail_limit": 5
}
```

Ask: "Give me just the five most-mentioned tickers, without detailed writeups."

```json
{
  "window": "24h",
  "sections": ["top_mentions"],
  "table_limit": 5,
  "detail_limit": 0
}
```

`sections` accepts a nonempty list of `alpha_calls`, `top_mentions`,
`mentions_spike`, `consensus`, `first_calls`, and `shorts`. Omit it to include all
six. Sections are deduplicated and returned in canonical order. A single section
uses one table without tabs; multiple sections use only the selected tabs.

`sectors` accepts reviewed sector names, matched case-insensitively with OR
semantics. `IT` aliases `Information Technology`; unknown names return the
available menu. Omit it to include all sectors and unclassified tickers.

`table_limit` is 1–10 rows per selected table. `detail_limit` is 0–table_limit
unique detailed tickers per section; zero omits the detailed blocks. The existing
`limit` parameter controls fallback page packing, not the number of table rows.
Empty sections stay empty. With Alpha selected, read all supplied actionable
theses for its shortlist even when fewer table rows or no details are requested.

The returned `report_options` describe the effective filters and limits. They
are pinned to the signed cursor: continue with the exact cursor alone. Old
cursors without report options require a fresh request. Refresh connector
discovery or start a new chat if these options are missing from the client's
cached tool schema. The current context is 10.0.0 and report format is 6.0.0.

The grouped-v5 metadata covers the full query, while `data_projection` declares
the narrower report evidence. This tool does not export every market-wide
thesis. Use `get_recent_idea_candidates` for that research workflow.

For daily updates on a selected portfolio of up to 100 tickers, use
`get_portfolio_summary`. It returns all full LONG/SHORT/AVOID theses for those
tickers plus portfolio updates, earnings calls and newly stored 13F events.
Its table and details include every ticker with `report_eligible=true`, including
event-only tickers, without the market-wide ranking or detail-count limits.
