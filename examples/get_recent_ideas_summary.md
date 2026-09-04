# get_recent_ideas_summary

Use this for a ready-made recent-ideas report rather than a raw candidate pass.
It defaults to the complete prior 24 hours and returns the same lossless
grouped-v4 evidence as `get_recent_idea_candidates`, plus globally calculated
`summary_context` and a host-agent instruction.

```text
Use get_recent_ideas_summary(window="24h"). If pagination.has_more is true,
follow the exact pagination.next_cursor until has_more=false. Do not reconstruct
an offset or start another snapshot. Intermediate pages can have null
summary_context; use the context from the complete inline response or final page.

Resolve every candidate idea ID in summary_context against the grouped rows.
Use the returned HIGH, MEDIUM, LOW, or NONE promotion-bias level exactly as
supplied. If promotion_bias_snapshot is unavailable or a row is null, write
Bias N/A and do not infer it from current posts or role text. Report an issuer relationship
separately; it must never raise or lower directional bias.

Follow the returned summary instruction for the compact table and detailed
sections. Do not recount authors, recompute server rankings, treat repeated posts
as independent confirmation, or rank by source-specific confidence.
```

The summary context is calculated against the complete fixed snapshot before
page slicing. It includes overview counts, Alpha-call candidate pools,
unique-author Trend, LONG-versus-SHORT-or-AVOID Consensus, directional Attention
spikes, most-mentioned rankings, exact First Calls from lifetime Alpha Top-100
authors, compact ticker metrics, and the candidate IDs needed to recover full
theses from `ticker_group_rows`.

The grouped evidence and promotion-bias contract are documented in
[`get_recent_idea_candidates`](get_recent_idea_candidates.md). Source URLs and
duplicate-member evidence remain a bounded finalist lookup through
`get_trade_idea_details`.
