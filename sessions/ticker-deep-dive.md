# Ticker Deep Dive

> Use Buzzberg to deep dive SIVE in English.

Call `get_ticker_deep_dive(ticker="SIVE")` once and follow its
`analysis_instruction`. Substitute MU, NBIS or another tracked ticker. Clients
with prompt support can use `ticker_deep_dive(symbol="SIVE")`.

The report explains the business simply, shows current 24h attention/sentiment
and saved price returns, draws three aligned charts, and synthesizes the main
bull/bear disagreement with linked authors and concrete business numbers.
It ends with measurable checks and key voices: Loudest Bull, Loudest Bear and
First recorded LONG on Buzzberg. The last label describes Buzzberg's stored
history, not first discovery in the world.

The server assembles saved data; your client writes the report. Missing YTD
is omitted and missing sentiment scores remain null even when the chart line
connects available observations. No baseline-calculation or price-staleness
boilerplate is printed in the normal report.

Follow-up research is optional and should be requested explicitly. This recipe
needs no automatic chain of other tools or web searches.

[Tool contract and limits](../examples/get_ticker_deep_dive.md)
