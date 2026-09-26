# Tracked 13F funds and returns

> Show the investors you track and their returns this year.

Call `get_13f_funds(period="ytd")`. Show a compact table of fund/manager,
modeled copy return, SPY, excess return in percentage points, drawdown and latest
disclosed report date. Show the price date. These are not actual fund returns.

Periods: `1m`, `3m`, `6m`, `ytd`, `1y`, `3y`, `5y`, `all`. `all` uses per-fund
inception; do not compare unequal histories as equal periods. Missing full-period
returns remain unavailable. `include_consensus=true` adds a synthetic portfolio,
not another manager. No request-time SEC or price calls.
