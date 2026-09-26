# Which tracked investors disclosed a stock?

> Which tracked funds hold NVDA, and what changed over four quarters?

Call `get_13f_stock_ownership(ticker="NVDA", quarters=4)`. Use `quarters=1` for
latest disclosed positions only. Show fund/manager, quarter-end, filing date,
weight, weight change and SEC links. Separate exits/history from latest holders.

Searches full books for exact ticker symbols (class-share punctuation normalized).
This is not market-wide ownership, and 13F does not reveal live holdings or shorts.
No matches is scoped to checked managers; show partial/unavailable coverage when
present. Default 50/max 100 rows, 1–12 quarters per manager. Follow `next_offset`
with `snapshot_version` and identical filters when complete results are requested.
Stock deep dives already include the latest ownership block in one call.
