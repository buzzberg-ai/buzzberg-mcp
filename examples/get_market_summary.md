# Market Summary

Ask for a market summary. The host calls `get_market_summary` once and
follows `analysis_instruction` in your language. Reconnect if your client has
cached the previous catalog.

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

The response is `MarketSummaryResult` schema 2.0.0, exposed as JSON text and
structuredContent. It combines the latest two published editions within seven
days with bounded fresh X evidence from the last 24 hours, not an archive. No date, cursor or historical edition argument exists.
Each preference list accepts at most 20 names of 100 characters. Preferences
prioritize available edition/X material, are not saved and do not fetch missing episodes.

The host uses a plain Market Summary title, without an edition/session suffix.
Edition dates, cutoffs and quote-save times remain metadata by default; no
preamble explains which editions were used. Source dates can qualify dated
events. Price labels follow `markets[].market_session`, never the research
edition: a premarket publication can support an afternoon market TLDR.

The host presents:

1. A short market TLDR, followed by SPY, QQQ, US 10Y yield/change in basis points, gold (explicit GLD ETF proxy),
   and BTC with a sampled rolling 24h change when available. All prices are
   database-only. Omit missing instruments (including US 10Y), unavailable
   changes and quote-save timestamp boilerplate. Preserve currencies and session
   labels. Show `since_open_change_pct` from `session_open` to `regular_price`
   as the default equity return. During postmarket, retain the regular close
   and its open-to-close move, then show the latest quote and
   `afterhours_change_pct` versus that close separately. Never pair an older
   session's return with today's price. If only `current_vs_previous_close_pct`
   is available, label its baseline explicitly; it is not since opening.
   Lead with measured SPY/QQQ changes. Current direction comes from `markets`,
   not old edition prose. Absolute prices cannot establish "near highs".
   BTC compares the current stored price with a same-currency observation near
   24h earlier. Its intraday history starts accumulating after server release.
2. Three or four themes, combining edition context and fresh updates according
   to `briefing.strategy`, with linked evidence. Broad
   related-ticker coverage is not a count of people endorsing the exact claim.
3. Two to three videos/posts with thesis, date, named speaker and current Authors
   rank/sample size when available. A video guest unrelated to the selected
   finding cannot raise that finding's reputation. Preview-only sources stay labeled.
4. Two worthwhile Reddit discussions on distinct topics when available.
   Each card links the topic, gives subreddit/date, an attributed thesis and why
   to read it. Favor substance and relevance, using engagement as a secondary
   signal within the supplied candidates. Keep counters out of default prose;
   explicit popularity requests can show the saved metrics and their scope.
   Distinguish a comment from a full thread; do not invent replies or consensus.
   This is a selection from the editions, not a complete Reddit ranking.

No transcript fragments, original evidence quotes or private source bodies are
returned. Missing editions remain explicit in metadata. Material source gaps
must not create false freshness. Missing market values stay in metadata and do
not create empty rows in the report.


## Automatic freshness

There is one compact hybrid workflow, with no mode or detail switch. The default
`{}` is normally presented in 450–650 words. Age is measured from the edition's
coverage cutoff. Up to 3 hours keeps edition themes first with a material-update
check; 3–12 hours blends new evidence; older or missing active-session coverage
uses fresh evidence first. Closed markets retain dated context. Late-processed
posts keep their original publication dates. Prices update independently.

The briefing retains the latest edition, previous summary, up to three
recommendations, two distinct Reddit cards and up to eight fresh posts. Logical
UTF-8 JSON is bounded to 45,000 bytes, including instructions. Whole optional
objects may be omitted with `briefing.budget_limited=true`. Transport
compatibility can duplicate this data.

Fresh selection reuses canonical author identities and current Authors ranks.
Substantive news/research and independent-author ticker attention precede rank;
explicit jokes/banter are excluded. Recent and untickered macro lanes preserve
room for new events. Metadata scans are bounded and `scan_complete` reports
overflow. `fresh_attention` is ticker attention in eligible new X material, not
an exact-narrative popularity score, endorsement count or the 24h Top Mentions
ranking. The host groups actual claims and keeps opposing arguments distinct.

Only selected derived theses/summaries leave the tool. Their truncation flags
limit claims to the visible evidence. Existing source-access rules apply;
hidden ticker claims cannot reappear through a general-summary fallback.
`fresh_status=unavailable` retains the usable edition and price sections without
pretending new developments were checked. These are selected materials, not a
complete feed or platform-wide ranking.
