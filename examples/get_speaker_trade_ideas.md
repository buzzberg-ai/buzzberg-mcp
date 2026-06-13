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
  "days": 365,
  "max_per_day": 10
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
  "sort": "recent",
  "max_per_day": 10
}
```

## All-time author history with day caps

Ask your agent:

```text
Use Buzzberg to show Serenity's all-time trade ideas with thesis.
Limit it to 100 ideas and keep at most 5 ideas per day.
Which tickers did she mention most, what was her first idea,
where did she flip direction, and how have her views changed?
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "days": 0,
  "limit": 100,
  "max_per_day": 5,
  "sort": "recent"
}
```

## First and flip ideas only

Ask your agent:

```text
Use Buzzberg to find Serenity's first/flip trade ideas from the last year.
Which names look like genuine new stories versus repeated crowded trades?
```

Tool call:

```json
{
  "speaker_name": "Serenity",
  "days": 365,
  "signal": "first_flip",
  "limit": 100,
  "max_per_day": 5
}
```

## Safety / scope

This tool requires one `speaker_name`, caps `days`, `limit`, and `max_per_day`,
and returns extracted trade-idea summaries. It does not return full source text
or allow a bulk export of every speaker's ideas.
