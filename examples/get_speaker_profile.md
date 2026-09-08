# get_speaker_profile

Ask: "Show aleabitoreddit's author profile."

```python
get_speaker_profile(speaker_name="aleabitoreddit")
```

The default `mode="report"` returns schema 2.0.0 structured data plus one short
`analysis_instruction` for the host AI to present the report. Report format is
1.0.0. The server does not call an LLM or generate an HTML artifact.

The header includes the linked author, handle, role, full bio and source links.
Metrics appear as Alpha rank, Score, evaluated Calls, adjusted Return, Win rate,
Focus. Followers and leaderboard followers are distinct snapshot counts.
Credibility is omitted. Five tabs follow:

| Tab | Contents |
| --- | --- |
| Main Focus | Theme, coverage share, top 3 tickers with mention counts |
| Most Mentions | Top 10 by LONG+SHORT+AVOID; Long, Short, Avoid, Neutral counts |
| Winners | Top 10 positive average saved position returns |
| Losers | Top 10 negative average saved position returns |
| Recent | Latest 10 lifetime first LONG/SHORT/AVOID calls |

Winners, Losers and Recent share columns: #, Ticker, Direction, First call,
First call price, Mentions, Return. Direction/date/price identify the ticker's
first actionable call. Recent returns belong to that exact call; Winners and
Losers use mean saved LONG/SHORT position returns. Missing prices/returns stay
null and display as an em dash, never as zero or a repeat's price.

Raw data for your own report or analysis:

```python
get_speaker_profile(speaker_name="aleabitoreddit", mode="data")
get_speaker_profile(speaker_name="aleabitoreddit", mode="data", sections=["all"])
get_speaker_profile(
    speaker_name="aleabitoreddit", mode="data", sections=["most_mentions", "recent"], days=30
)
```

Data mode omits `analysis_instruction` and `report_format_version`. Its default
section is `overview`; select specific sections or `['all']` for more evidence.
Both modes use the same data fields and calculations for the same selection.

`days=0` (default) uses all available history; 1-3650 selects a rolling
publication window. First calls are identified across lifetime history before
filtering: a recent repeat or flip never becomes a first call. Alpha keeps its
lifetime sample, separate from the speaker-detail Win rate sample. Saved
performance and follower data carry independent timestamps, not a promise of
live prices or a fresh X follower measurement.

Mention counts deduplicate a public source post plus exact instrument ID.
Main Focus uses Coverage Map's classified priceable denominator. The displayed
Neutral column combines WATCH+NEUTRAL; raw data keeps CLOSE separate.
Hidden, paid, future, news and earnings-call rows are excluded. Histories above
50,000 rows return `history_limit_exceeded` with no partial report.

Migration: schema 2.0.0 replaces the former Markdown response with
`structuredContent` and a matching JSON text mirror. Refresh cached tool
metadata and read sections under `data`. Speaker Lens is still a separate
research dossier. Internal Buzzy requests data mode for its evidence workflow.
