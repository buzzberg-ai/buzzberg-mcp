# get_trade_idea_details

Use this after `get_recent_idea_candidates` has produced a shortlist. It returns
audit details for up to 50 selected idea IDs without forcing those repeated
fields into every row of the broad first pass.

```text
Call get_trade_idea_details(
  idea_ids=[369804, 369755, 369701]
).

For each returned idea, show the source URL, source identifiers, declared
speaker role and its provenance, full thesis, and any grouped near-duplicate
members. Report requested IDs that were not found.
```

The typed result contains:

- the requested, returned, and missing idea IDs;
- ticker and effective direction;
- speaker role plus role provenance;
- source type, name, URL, Buzzberg content ID, and external platform ID;
- full and short thesis text where present;
- the complete member list for a near-duplicate group.

The source URLs and internal/external IDs are returned here because they are useful
for citations and audits, but needlessly repeat across the complete recent-idea
scan. `content[].text` is an exact compact-JSON mirror of the typed result.
