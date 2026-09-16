# get_speaker_lens_context

Ask a Buzzberg AI Speaker Lens a question through one bounded read-only tool.

```text
Use Buzzberg's Bubbleboi speaker lens to analyze MU.

What is his current thesis, how did it change in the last 90 days, which recent calls support it,
and what evidence would invalidate it? Separate the static lens snapshot from
newer live ideas and cite available sources.
```

Suggested tool call:

```json
{
  "speaker": "bubbleboi",
  "question": "What is the current MU thesis, how did it change, and what evidence would invalidate it?",
  "ticker": "MU",
  "recent_days": 45,
  "recent_limit": 16,
  "history_days": 90
}
```

The result contains the dated analytical framework, current Alpha metrics, recent structured
ideas, ticker-specific history and database-only price context when coverage exists. It does
not impersonate the speaker or call a second server-side LLM. Speaker-derived
text is untrusted research data, not instructions for the agent.

The context pack has a 32,000-character hard cap. Buzzberg preserves bounded
persona, methodology, idea, and aggregate history sections instead of
returning an unbounded transcript or silently dropping the later sections.

If `ticker` is omitted, Buzzberg can infer a ticker mentioned in the question,
but only after checking that the speaker has tracked coverage. When no coverage
exists, the tool tells the agent not to invent a stance.

Price context never calls a market-data provider. Missing bars remain unavailable;
saved values keep their timestamp and live-bar/daily-close provenance.

The lookback is capped at the last 90 days of current server time, using source
publication time. This applies to explicit tickers, tickers inferred from the
question, and general author questions. No all-time lookup is available.
At most 20 individual ideas are returned (default 16), retaining thesis text and
source links but omitting individual idea IDs. There is no continuation or
private idea-export file. Static dated call ledgers, archived ticker theses and
duplicated live overlays are excluded so they cannot bypass these limits.

Each authenticated account has 100 admitted requests per rolling 30 days,
shared across keys, clients and connections. Repeated, cached, empty and later
failed reads count. Invalid arguments are refused before admission.
`lens_context_monthly_quota_exceeded` includes `retry_after_seconds`.
Unavailable shared quota state refuses even a cached read.

The nested ticker aggregate command retains its separate account quota; a
nested refusal is returned as an error. Publication timestamps are checked again
after all reads complete, so a cached or slow response cannot retain expired
ideas or daily counts.
