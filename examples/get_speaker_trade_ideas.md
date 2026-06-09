# get_speaker_trade_ideas

Use this when you want the trade-idea history of one author, without asking
Buzzberg to return the author's raw tweets/articles/transcripts.

## First idea by an author

Ask your agent:

```text
Use Buzzberg to find Serenity's first recorded NOK trade idea.
Return the date, direction, confidence, thesis, source type, and idea id.
Use Buzzberg data only.
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "ticker": "NOK",
  "sort": "oldest",
  "limit": 1,
  "days": 365
}
```

## Recent author story

Ask your agent:

```text
Use Buzzberg to summarize Leo's trade ideas from the last 90 days.
Which tickers does he keep returning to, what changed, and where is he most
bullish or bearish?
```

Tool call:

```json
{
  "speaker_name": "Leo",
  "days": 90,
  "limit": 50,
  "sort": "recent"
}
```

## Safety / scope

This tool requires one `speaker_name`, caps `days` and `limit`, and returns
extracted trade-idea summaries. It does not return full source text.

