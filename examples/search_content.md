# search_content

Use this for lightweight discovery across public content titles/names. This is
not full-text search across transcripts or private source material.

## Prompt

```text
Use Buzzberg to search recent public content titles for "robotaxi".
Show the matching items, source type, date, and why each might be worth reading.
```

## Tool Call

```python
search_content(query="robotaxi", days=30, limit=10)
```

## Source-Specific Search

```python
search_content(query="AI-RAN", days=90, source_type="twitter", limit=20)
```

## What Content Can Appear

- X/Twitter post titles or text snippets stored as content titles.
- YouTube video titles.
- Reddit post titles.
- Public newsletter/Substack preview titles.

Wire-service news is disabled for this tool. Paid/private newsletter bodies are
not searched or returned. Avoid sending sensitive private text as a search
query, because tool arguments are visible to the Buzzberg server.

## Latest materials without a search phrase

```python
search_content(limit=10)
search_content(source_type="youtube", days=7, limit=20)
```

Empty/whitespace query selects recent titles. Omitted/null days has no age
cutoff in this mode, preserving latest selection for sparse sources. Supplying
days narrows it to 1–365 rolling publication days. Title search defaults to 30
days when days is omitted/null. Both modes cap results at 30, default 10, and
return only bounded titles, source, date and links. No bodies, cursor or as_of.
