# save_trade_idea

Ask: "Save trade idea 12345 to my Buzzberg account."

The `idea_id` comes from read tools such as `search_trade_ideas`,
`get_top_speaker_signals`, `get_speaker_trade_ideas`, or
`get_speaker_ticker_history`.

Safe preview:

```json
{
  "idea_id": 12345,
  "dry_run": true
}
```

Actual write:

```json
{
  "idea_id": 12345
}
```

This write tool saves only to the account that owns the MCP API key.
