# get_recent_idea_candidates

Use this as the primary first pass for broad requests such as "What are the
best Buzzberg ideas from the last 24 hours?" It returns the complete visible
candidate set grouped by internal ticker ID. No thesis is shortened.

`window` defaults to `6h` and accepts only `1h`, `6h`, `12h`, `24h`, or `1d`.
Requests for `3d` or `7d` are rejected rather than returning an incomplete
broad review.

## One complete response first

Call once with the desired window and optional source_type, direction or as_of.
Do not pass delivery, limit, cursor or offset. For example:

```json
{"window": "24h"}
```

First-call `delivery=paged` and `offset=0` are accepted for compatibility but
ignored, with a warning. A small `limit` does not truncate the complete result
or force paging. The existing server inline token budget and emergency idea
count decide whether fallback pages are necessary. Limits are server estimates,
not a guarantee about a client's available context.

Only if `pagination.has_more` is true, send its exact `next_cursor` alone:

```json
{"cursor": "<exact pagination.next_cursor from the preceding response>"}
```

Read every page before selecting ideas. Pages contain whole ticker groups and
never shorten theses. Existing valid signed cursors retain their original scope
and position. Positive offsets remain invalid. The complete publication window
must fit within the last seven days of current server time, including every
continuation. Refresh tool discovery to see the updated parameter descriptions.

## Current grouped schema 5.0.0

`get_recent_idea_candidates` used to return one flat chronological array of
ideas. The grouped response was briefly exposed as a second tool named
`get_recent_ideas_by_ticker`. That split was removed: broad recent-idea research
is one user request, so the established `get_recent_idea_candidates` name now
returns the grouped v5 contract directly. This endpoint is not a summary and it
does not choose the best ideas on the server.

The v5 first pass groups the fixed snapshot as:

```text
ticker
  -> canonical speaker
       -> directional ideas
       -> watch/neutral context
```

Every candidate and every `thesis_full` remains available. Shared ticker,
current-price, speaker, ready daily promotion bias and reviewed affiliation values are emitted once at the level
where they apply. This reduces repeated field names and makes consensus,
disagreement and repeated promotion visible without asking the model to join
mentions scattered across chronological pages.

Ticker groups are not ordered by raw mention count alone. Independent speakers
with LONG/SHORT/CLOSE/AVOID calls come first, followed by directional idea
count, total idea count and recency. This prevents a large WATCH/news stream
from outranking several independent actionable calls, while keeping that
context in the response.

Pagination now advances by whole ticker group. A ticker is never split between
pages, and every continuation uses the exact signed `next_cursor` from the same
snapshot. Source URLs/IDs, role provenance and duplicate-member evidence are
available through `get_trade_idea_details` only after the model selects
finalists; moving those audit fields does not remove a candidate or shorten its
thesis.

The current public contract has no top-level flat `idea_rows` response. Clients
with a cached tool catalog may still display that old v2 shape; this is stale
`tools/list` metadata, not a different Buzzberg endpoint. Reconnect or start a
new chat after the schema change. Do not reuse a v2 cursor: old positions
referred to flat idea rows, while v5 positions refer to ticker groups. The
removed `get_recent_ideas_by_ticker` name is no longer callable.

```text
Use Buzzberg to find the top 10 strongest trade ideas from the last 24 hours.
Call get_recent_idea_candidates(window="24h"). Read ticker_group_columns,
speaker_columns, promotion_bias_columns, and idea_columns once, then map every
ticker_group_rows array positionally.

While pagination.has_more is true, call the tool again with the exact
pagination.next_cursor unchanged. Do not use offset and do not select finalists
until the fixed-snapshot pass ends with has_more=false.

Treat repeated posts by one canonical speaker as one speaker, not independent
confirmation. Compare the full thesis, direction, signal, saved entry/current
price context, ready promotion/affiliation evidence, and disagreements inside each ticker.
After selecting finalists, call get_trade_idea_details with their idea IDs.
```

The response declares compact schemas once:

- `ticker_group_columns` describes each ticker group;
- `speaker_columns` describes canonical speakers inside a group;
- `promotion_bias_columns` describes the ready daily bias indicators;
- `source_columns` and `direction_columns` describe source and direction values;
- `idea_columns` describes the full-thesis idea rows split into directional
  ideas and watch/neutral context.

The current `idea_columns` are:

```text
idea_id, published_at, direction, signal, entry_price,
price_change_since_entry_pct, source, post_kind, thesis_full
```

Generic `confidence` is intentionally absent. The stored values are
source-specific ingestion signals with different meanings across Twitter,
YouTube, newsletters, and Reddit, so one shared numeric column would imply a
cross-source scale that does not exist.

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

The full first pass intentionally omits generic confidence, source URLs, source
IDs, role provenance, short theses, and duplicate-member payloads. Audit fields
are available for selected finalists through `get_trade_idea_details`.
