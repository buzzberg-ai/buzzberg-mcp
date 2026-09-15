# Followed-author updates

Ask: “Summarize my followed authors over the last 24 hours.”

Use `get_my_feeds(feed_type="voice", include_members=False)` to select the feed,
then call `get_feed_summary(feed_id=...)`. The server reads that feed's membership
for the authenticated account and returns evidence plus `analysis_instruction`.
Follow the returned continuation with the same feed ID and exact cursor if needed.
The final instruction defines the author table, shared themes and detailed theses.

This is a private feed read. For an earnings-only report use
`get_earnings_calls_summary`; for selected portfolio tickers use
`get_portfolio_summary`.
