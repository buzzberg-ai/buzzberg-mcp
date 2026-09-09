# get_speaker_trade_ideas

Read one author's complete recent trade ideas, with full saved theses.
This command returns extracted ideas, not raw tweets, articles or transcripts.

## Author recap for the last month

Ask: “Summarize Serenity's trade ideas over the last 30 days, explain changes
in her arguments, and link the sources.”

```json
{"speaker_name": "Serenity"}
```

The default is 30 days with `include_thesis=true`. Full saved arguments take
precedence over short summaries. If only a short argument exists it is returned;
if neither exists the idea remains, with `is_thesis_bearing=false`.

## One ticker, chronological order

```json
{"speaker_name": "Serenity", "ticker": "SIVE", "days": 30, "sort": "oldest"}
```

This finds the earliest idea **within the requested window**. It does not
establish the author's first-ever mention.

## Long ideas from the last week

```json
{"speaker_name": "Leo", "days": 7, "direction": "long"}
```

All matching long ideas are returned. There is no caller row limit or per-day
sampling. Available directions: long, short, avoid, close, watch and neutral.
Near-identical corrected Twitter posts are grouped; `repeat_count` discloses
the grouped idea rows, and the newest correction supplies the argument.

## The same ideas without argument text

```json
{"speaker_name": "Leo", "days": 7, "direction": "long", "include_thesis": false}
```

This omits argument text from the same set of ideas. It does not select ideas
that lack a thesis. Other fields, including direction and source links, remain.

## First/flip signals from the last day

```json
{"speaker_name": "Serenity", "days": 1, "signal": "first_flip", "source_type": "twitter"}
```

A stored signal badge is a claim in the data, not independent proof of a
first-ever mention.

## Response and continuation

The MCP result contains JSON text (`ideas`, `counts`, `pagination`) and a
`structuredContent.buzzberg_receipt` of speaker schema 3.0.0. Small results
arrive in one response. Only overflow beyond 900,000 estimated tokens is paged.

When `pagination.has_more=true`, copy the exact `pagination.next_cursor`:

```json
{"speaker_name": "Serenity", "cursor": "COPY_THE_EXACT_NEXT_CURSOR"}
```

Pass the same author name and the cursor only. Repeat until `has_more=false`
before claiming to have read the whole result. The saved snapshot expires one
hour after the initial request; replay never extends it. Its author, filters,
ordering and thesis option cannot be changed by a continuation.

## Launch access and quota

Registered, authenticated accounts can request **1, 7, 15 or 30 days**.
Default: **30**. `days=0`, 60, 90, 180 and 365 are currently refused. Paid longer
history comes later. The removed `limit` and `max_per_day` arguments must not
be sent; refresh the connector's tool schema after the update.

Each account has **20 new requests per rolling 24 hours**, shared across all
clients. Application errors/refusals do not spend quota. Successful empty
results do; repeating a fresh query counts again. Continuations and replay of
valid cursors are free of this command's quota. General frequency limits remain.
On quota exhaustion, honor `retry_after_seconds` instead of retrying in a loop.

The server charges after query, snapshot creation and response serialization
succeed. A disconnect after this point cannot prove whether the host received
the answer. These limits apply only to this command.
