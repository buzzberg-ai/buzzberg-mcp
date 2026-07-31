# get_recent_idea_candidates

Use this for broad requests such as "What are the best ideas from the last six
hours?" The tool returns every visible supported-source idea candidate in an
exact recent window, not only top-ranked speakers or First/Flip signals.
Supported sources are Twitter, YouTube, Substack, and Reddit; disabled wire-news
is intentionally excluded.

```text
Use Buzzberg to find the strongest trade ideas from the last 6 hours.
Call get_recent_idea_candidates(window="6h", limit=200, offset=0), then follow
every next offset until the candidate pass is complete.

Do not rank by Alpha score, extractor confidence, follower count, or how
confidently the post is written. Compare thesis mechanism, catalyst timing,
entry/current price context, downside, the author's relevant professional role,
repeated promotion of the ticker, possible issuer conflicts, and independent
evidence. Cite each selected idea and state what remains unverified.
```

The response includes entry price, source, declared role, prior 365-day
speaker/ticker mention counts, and bias flags where the available data supports
them. Unknown roles and relationships remain unknown.

The scan is bounded to 500 candidate rows. Narrow `window` or `source_type`
when the server asks you to reduce the result set.
