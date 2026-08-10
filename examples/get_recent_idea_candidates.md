# get_recent_idea_candidates

Use this as the primary first pass for broad requests such as "What are the
best Buzzberg ideas from the last 24 hours?" It returns the complete visible
candidate set grouped by internal ticker ID. No thesis is shortened.

```text
Use Buzzberg to find the top 10 strongest trade ideas from the last 24 hours.
Call get_recent_idea_candidates(window="24h"). Read ticker_group_columns,
speaker_columns, history_columns, and idea_columns once, then map every
ticker_group_rows array positionally.

While pagination.has_more is true, call the tool again with the exact
pagination.next_cursor unchanged. Do not use offset and do not select finalists
until the fixed-snapshot pass ends with has_more=false.

Treat repeated posts by one canonical speaker as one speaker, not independent
confirmation. Compare the full thesis, direction, signal, saved entry/current
price context, 365-day speaker history, and disagreements inside each ticker.
Use stored confidence as one ingestion-stage thesis/evidence quality signal,
never the sole rank; it is not a predicted return.
After selecting finalists, call get_trade_idea_details with their idea IDs.
```

The response declares four compact schemas once:

- `ticker_group_columns` describes each ticker group;
- `speaker_columns` describes canonical speakers inside a group;
- `history_columns` describes each speaker's compact prior-365-day direction
  counts;
- `idea_columns` describes the full-thesis idea rows split into directional
  ideas and watch/neutral context.

Ticker groups are ordered by independent directional speakers first, then
directional idea count, total idea count, latest directional activity, and
latest activity. This brings well-corroborated actionable groups forward
without deleting watch context or making a semantic quality decision.

Current price is the freshest stored Buzzberg live price or stored daily close.
`current_price_kind` and `current_price_as_of` identify which one was used.
`price_change_since_entry_pct` is the raw instrument-price change from the
saved entry; it is not direction-adjusted performance.

Pagination never splits a ticker group. A page can therefore contain fewer
groups than the requested limit when the response token budget is reached.
Every continuation uses the opaque signed `next_cursor` and preserves the same
`as_of` snapshot.

The full first pass intentionally omits source URLs, source IDs, role
provenance, short theses, and duplicate-member payloads. Those audit fields are
available for selected finalists through `get_trade_idea_details`.
