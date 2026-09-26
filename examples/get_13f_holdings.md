# Latest and historical 13F holdings

> Show Altimeter's portfolio, and how its NVDA weight changed.

Call `get_13f_holdings(fund="altimeter")` for latest disclosed positions. Show
quarter-end and filing date above the position table; latest is not a live book.
Rows show ticker/issuer, current and previous weights, change in percentage points
and status; exits are separate. Search uses full books, not only top ten holdings.

Then call `get_13f_holdings(fund="altimeter", view="history", ticker="NVDA")`.
A specific quarter uses `report_date="2026-03-31"`; retained dates are returned
in `available_reports`. Fund/manager names also work; ambiguous matches return
candidates. Default 20/max 100 rows. To show all, follow `next_offset` with the
returned `snapshot_version` and the same filters. Restart at zero after
`snapshot_changed`. Never infer shares bought/sold from weight changes or invent
manager cost basis. Empty filtered history applies only to retained reports.
