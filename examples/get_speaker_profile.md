# get_speaker_profile

Ask: "Show aleabitoreddit's author profile."

```python
get_speaker_profile(speaker_name="aleabitoreddit")
```

The default `mode="report"` returns schema 2.1.0 structured data plus one short
`analysis_instruction` for the host AI to present the report. Report format is
1.1.5. The server does not call an LLM or generate an HTML artifact.

The instruction separates content from presentation. Use normal conversation
text size, clear contrast, a larger author title and prominent metric values.
Give Focus extra room and wrap whole words; keep other metric values unbroken.
Keep dates/sample metadata compact and put methodology notes below the tables
or in a disclosure. Keyboard-accessible button-like tabs sit immediately above
the table. The selected tab has solid contrasting fill/text; other tabs keep
visible button styling without hover. The gap before tabs is clearly larger
than the gap between tabs and the table.

The four ticker tabs share widths defined once for all four tables; active-tab
content cannot change them. Use compact gaps, narrow rank/direction columns and
room for tickers/prices. On narrow screens, preserve text size and whole values,
allow horizontal table scrolling, and wrap headings. Right-align standalone numeric columns with tabular
digits and price/currency on one line. Emphasize tickers and returns; date links
stay understated but recognizable. Optional green/red denotes positive/negative
returns, preserving signs and neutral zero/missing values. Main Focus separates
Share from three left-aligned grid cells. Each cell holds one unbroken inline
"TICKER · count" pair with normal word spacing inside and compact gaps between
pairs. Wrap whole pairs on narrow screens. Inline counts remain beside their
ticker. Before delivery, test every supplied tab (all five for a full report)
at normal and narrow widths, scroll overflow tables, and check wrapping,
clipping, overlaps and shared-column positions in the rendered output. Code/HTML
inspection is not visual verification; state when rendered checks are unavailable.
This is guidance, not a fixed renderer or proof that a host performed those checks.

The linked author name is the sole title. The header appears once above the
tabs with handle, role, full bio and source links, without a closing recap.
Metrics appear as Alpha rank, Score, evaluated Calls, adjusted Return, Win rate,
Focus. followers_count is total X followers; leaderboard_followers_count counts
Buzzberg-ranked authors following that account on X. Show both with snapshot dates.
Credibility is omitted. Five tabs follow, each with at most 15 rows in both modes:

| Tab | Contents |
| --- | --- |
| Main Focus | Top 15 themes, coverage share, top 3 tickers with mention counts |
| Most Mentions | Top 15 by LONG+SHORT+AVOID; compact L/S/A/N counts and first-call context |
| Winners | Top 15 positive average saved position returns |
| Losers | Top 15 negative average saved position returns |
| Recent | Latest 15 lifetime first LONG/SHORT/AVOID calls |

Most Mentions is ordered by LONG+SHORT+AVOID descending, then total mentions
descending, then stable ticker ID. Preserve server order and show the translated
caption "Ranked by LONG+SHORT+AVOID; ties by total mentions".

Most Mentions columns: #, Ticker, Direction, L/S/A/N, First call, First call price,
Return. The displayed Return heading is "First-call return". The four counts
share one compact cell. Direction/date/price
and Return all belong to the exact lifetime first LONG/SHORT/AVOID idea, even
if it predates the requested `days` window. Missing first-call data stays null;
a later idea's return or entry price is never substituted.

Winners, Losers and Recent share columns: #, Ticker, Direction, Mentions, First call,
First call price, Return. The displayed Return heading is "Average position
return" in Winners/Losers and "First-call return" in Recent. Add the visible
Recent table caption "Latest first directional calls by ticker". Translate
headings, labels, captions and Focus/theme values into the user's language;
tab names and direction codes remain English. English strings above are
translation references. Direction/date/price identify the ticker's
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
Main Focus uses Coverage Map's full classified priceable denominator, including
themes outside the top 15. `total_themes` records the complete theme count;
`query.section_row_limit` is 15. In L/S/A/N, N combines WATCH+NEUTRAL; raw data
keeps CLOSE separate.
Hidden, paid, future, news and earnings-call rows are excluded. Histories above
50,000 rows return `history_limit_exceeded` with no partial report.

Migration: schema 2.0.0 replaces the former Markdown response with
`structuredContent` and a matching JSON text mirror. Refresh cached tool
metadata and read sections under `data`. Speaker Lens is still a separate
research dossier. Internal Buzzy requests data mode for its evidence workflow.
Schema 2.1.0 adds the Most Mentions first-call fields and a uniform 15-row cap;
request parameters are unchanged.
