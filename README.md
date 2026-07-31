# Buzzberg MCP

[![PyPI](https://img.shields.io/pypi/v/buzzberg-mcp)](https://pypi.org/project/buzzberg-mcp/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-private--beta-orange)

> Private Beta: the MCP contract can change before broader beta. See
> [CHANGELOG.md](CHANGELOG.md) for breaking changes.

Buzzberg MCP connects Claude, Cursor, Cline, Continue.dev, and other MCP clients
to Buzzberg market intelligence: trade ideas, sentiment, speakers, prices, and
saved-idea actions for your own Buzzberg account.

## Connect Your AI Agent

### Claude Web, Desktop, And Mobile

No Terminal, package install, or copied API key is required.

1. In Claude web or Desktop, open **Customize -> Connectors**.
2. Select **+ -> Add custom connector**.
3. Name it **Buzzberg** and paste:

   ```text
   https://mcp.buzzberg.ai/mcp
   ```

4. Leave the OAuth client ID, client secret, and other advanced fields empty.
5. Select **Add**, then **Connect**. Sign in to Buzzberg and approve access.
6. Enable Buzzberg from the Connectors menu in a conversation.

The remote connector follows the same Claude account across web, Desktop, and
mobile. Adding a custom connector directly on mobile is still in beta, so web
or Desktop is the simplest setup path. On Team and Enterprise plans, an owner
must add the connector before members can connect it.

### Claude Code

```bash
claude mcp add --transport http buzzberg https://mcp.buzzberg.ai/mcp
```

Open `/mcp` in Claude Code, select Buzzberg, and complete the browser sign-in.
Claude Code stores and refreshes the OAuth connection.

### Codex

```bash
codex mcp add buzzberg --url https://mcp.buzzberg.ai/mcp
codex mcp login buzzberg
```

The second command opens the standard MCP OAuth flow in your browser.

### Other Clients And Existing Setups

Clients that cannot complete standard MCP OAuth can still use a personal key.
Existing `bzb_...` keys, `/sse` connections, Claude Desktop helper installs,
and manually configured clients continue to work unchanged.

See [INSTALL.md](INSTALL.md) for Cursor, Cline, Continue.dev, OpenClaw,
custom Python clients, and the API-key compatibility path.

## What You Can Do With It

Buzzberg is useful when you want your AI agent to read the market conversation,
not just fetch a price. Ask one plain-English question; Claude, Codex, or
another MCP client chains the right Buzzberg tools and turns bounded market
context into a usable research read.

### Research beyond the headlines

Even a strong web research pass can miss smaller but important facts scattered
across specialist posts, videos, newsletters, and market discussions. Buzzberg
gives your AI source-linked research from many different speakers covering the
same ticker. By comparing their facts, theses, risks, and disagreements, the
agent can catch details a general search may overlook and build a more complete
investment picture.

Use web research for fundamentals, filings, company announcements, and recent
news. Add Buzzberg for source-linked research from multiple market voices:
additional facts, competing theses, risks, disagreements, and second-order
effects. Buzzberg does not guarantee exhaustive coverage and should not replace
primary filings or independent verification.

```text
Research SIVE using both web search and Buzzberg.

Use web search for company fundamentals, filings, and current news.
Use Buzzberg for source-linked mentions, speaker theses, trade ideas,
sentiment, disagreements, and narrative changes across available sources.

Combine both into one report. Highlight non-consensus arguments,
overlooked risks, second-order effects, repeated claims, and facts
that still need verification. Cite sources and note coverage gaps.
```

In supported clients, Buzzberg also exposes these workflows through MCP
`prompts/list` and context through `resources/list`, similar to Kaito-style MCP
servers. Ask your agent to **"list Buzzberg workflows"** or use the manual
prompts below.

Discoverable MCP prompts include:

- `daily_alpha_brief`
- `top_speaker_market_tldr`
- `ticker_deep_dive`
- `narrative_map`
- `research_posts_alpha`
- `stock_list_candidates`
- `portfolio_update_tracker`
- `speaker_story`
- `sentiment_price_chart`
- `contrarian_scan`
- `keyword_mining`

Discoverable MCP resources include:

- `buzzberg://workflows`
- `buzzberg://data-boundaries`
- `buzzberg://top-speakers`
- `buzzberg://market/leaderboards`

Start manually with these prompts:

```text
Use Buzzberg to deep dive SIVE.
Who is talking about it, what is the core bull thesis,
what are the strongest bear risks or missing arguments,
and is this early discovery, building momentum, or crowded?
```

```text
Use Buzzberg to give me today's top-speaker market brief.
What are the main themes, crowded trades, new tickers, and disagreements?
Quote examples.
```

```text
Use Buzzberg to build a 7-day newsletter thesis map.
Show the strongest ticker narratives, key evidence, weak claims,
and what changed this week. Separate hard data from vibes.
```

```text
Use Buzzberg to find first-order and second-order effects from this week's
YouTube market discussions.
Which tickers benefit directly, which suppliers or competitors are second-order
plays, and what risks are speakers worried about?
```

```text
Use Buzzberg to map the SIVE narrative.
Combine top-speaker trade ideas, YouTube TLDRs, newsletter TLDRs,
sentiment, and recent source snippets.
Separate catalysts, evidence, repeated claims, and open questions.
```

```text
Use Buzzberg research posts from the last 24h.
Find the strongest new alpha ideas, second-order beneficiaries,
repeated evidence, weak assumptions, and tickers worth a deeper dive.
Quote short examples.
```

```text
Use Buzzberg stock-list posts from the last 7 days.
Which tickers appear across multiple lists, what theme links them,
which are fresh vs crowded, and which 10 should I research next?
```

```text
Use Buzzberg portfolio-update posts from the last 7 days.
What did speakers add, trim, close, or size up?
Separate actual portfolio moves from generic commentary.
```

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples and point to the tickers each theme is about.
```

```text
Use Buzzberg to build a 90d mentions vs price read for SIVE.
Show daily mention spikes, sentiment on those days, and price reaction.
Which days look like narrative ignition or narrative exhaustion?
```

```text
Use Buzzberg to show Serenity's all-time trade ideas with thesis.
Limit it to 100 ideas and keep at most 5 ideas per day.
Which tickers did she mention most, what was her first idea,
where did she flip direction, and how have her views changed?
```

```text
Use Buzzberg to analyze all trade ideas from Serenity about SIVE.
Show the first mention, latest mention, direction changes, thesis evolution,
and whether confidence increased or faded.
```

```text
Use Buzzberg to rank the tickers most mentioned by top-50 speakers today.
Show mentions, sentiment, direction mix, source mix, and whether each story
looks fresh or already crowded.
```

What Buzzberg sends to the AI agent:

- **Substack/newsletters:** Buzzberg TLDRs, public previews where available,
  and extracted trade ideas for the last 7 days. Raw article bodies are not
  returned through MCP.
- **YouTube:** Buzzberg TLDRs and extracted trade ideas for the last 7 days.
  Raw YouTube source text and timestamped segment dumps are not returned through MCP.
- **Twitter/X:** top-speaker tweets from the last 24 hours where Buzzberg found
  ticker ideas, including the full tweet text, speaker, tickers, and direction:
  `LONG`, `SHORT`, `WATCH`, `AVOID`, or `NEUTRAL`. This is not every tweet.
  For multi-day research, use structured trade ideas rather than raw Twitter
  source text.
- **Post-kind filters:** source context can be narrowed to `research`,
  `portfolio_update`, `stock_recommendation_list`, `news`, or `other`, so an
  agent can ask specifically for research posts, stock lists, or portfolio moves.
- **Ticker research:** mentions, sentiment, trade ideas, speaker profiles,
  price snapshots, and daily sentiment/mention history for chart-style reads.
- **Narrative research:** ticker deep dives that combine trade ideas, source
  TLDRs, top-speaker tweets, sentiment, mentions, and price context.
- **Speaker research:** bounded trade-idea history for one author, plus
  speaker/ticker daily history for charts of changing views over time. Speaker
  history requires one speaker name, caps output at 200 ideas, and defaults to
  at most 10 returned ideas per calendar day.

## Beta Rate Limits And Agent Etiquette

Buzzberg MCP is rate-limited during private beta. The current default limits are
about **120 tool calls per minute per user** and **2,000 tool calls per day per
user**, with an additional shared server-wide safety cap. These limits may
change during beta as we tune capacity.

If your client receives `429 Too Many Requests`, read the `Retry-After` header
or `retry_after_seconds` field and wait that many seconds before continuing.
Do not retry in a tight loop.

For best results, ask your agent to work in a bounded, staged way:

- Start with one broad scan or leaderboard, then do targeted follow-ups.
- Use `limit`, `days`, `top_n`, and `max_per_day` instead of unbounded scans.
- For author history, provide a `speaker_name`; Buzzberg does not expose a
  "dump all speakers' ideas" endpoint.
- Use batch tools such as `get_tickers_overview` for multi-ticker screens.
- Keep concurrency small; avoid dozens of parallel calls.
- Use the write tool only when you explicitly want to save an idea.
- Use `dry_run=True` on write tools when you want your agent to verify the
  action without changing your account.
- Keep your `bzb_...` key in an environment variable or local config; do not
  paste it into shared prompts, code, or logs.

Contract notes:

- Trade-idea tools include `idea_id` values. Use those IDs with
  `save_trade_idea`.
- Price outputs include currency/namespace context where available. Do not
  assume every displayed number is USD; foreign listings such as SIVE can be
  native-currency prices.
- `get_ticker_mentions` uses ingestion time, meaning when Buzzberg added the
  mention. `get_ticker_timeseries` uses source publication date for chart rows,
  so totals may differ.
- Mention counts include visible `LONG`, `SHORT`, `WATCH`, `NEUTRAL`, `AVOID`,
  and `CLOSE` rows. Chart CSVs expose `watch` separately so early-interest
  signals do not disappear into neutral.
- `get_speaker_profile` separates alpha rank from credibility. Alpha rank is
  historical idea performance; credibility is a profile/source quality score.
- `Adj. return` is not benchmark- or beta-adjusted excess return. It is the
  Bayesian-shrunk mean of current, direction-adjusted mark-to-market returns
  from Buzzberg's deduplicated Alpha evaluation set: the first eligible
  entry-priced LONG/SHORT thesis per related ticker and evaluation side.
- `Evaluated` is the number of currently priceable positions in that Alpha
  set. It will not match a lens's 24h/7d/30d `n` (all tracked ideas with a
  valid return at that horizon), signal-timing `n` (calls with both 24h and
  30d returns), or ledger rows (first calls and later LONG/SHORT flips).
- A `⏳` ledger row is retained but does not yet have a 30-day return. Speaker
  lenses report the current 30-day ledger maturity so agents can distinguish
  a proven historical sample from calls that are still too new to evaluate.

Ready-made workflows:

- **[Daily source TLDRs](sessions/daily-source-tldr.md)** — summarize the last
  24 hours of top-50 speaker ticker-idea tweets, plus up to 7 days of
  Substack/newsletter and YouTube TLDRs; ask for themes, crowded trades,
  repeated words, disagreements, and quoted examples.
- **[Ticker leaderboards](sessions/ticker-leaderboards.md)** — most buzzed
  tickers, strongest bullish/bearish sentiment, and daily historical buzz for
  1d / 7d / 30d windows.
- **[Morning briefing](sessions/morning-briefing.md)** — a complete fresh-idea
  pass + sentiment divergence radar + important recent content in one read.
- **[Narrative ticker deep dive](sessions/ticker-deep-dive.md)** — what
  Buzzberg uniquely knows about a ticker: who is pushing it, what the bull
  narrative is, what is missing, and whether the setup is early or crowded.
- **[Speaker story / author history](sessions/speaker-story.md)** — first idea,
  recent ideas, stance changes, and speaker/ticker history for one author.
- **[Sentiment vs price chart](sessions/sentiment-price-chart.md)** — daily
  sentiment, mentions, and cached close prices so Claude can explain whether
  Buzzberg sentiment leads, confirms, or lags price.
- **[Mentions vs price chart](sessions/mentions-price-chart.md)** — attention
  spikes vs price moves, useful for spotting narrative ignition, exhaustion,
  and post-move crowding.
- **[Contrarian scan](sessions/contrarian-scan.md)** — tickers where
  smart-money disagrees the most, ranked by sentiment spread. High-volatility
  setups where the camps are obvious.
- **[Build a research shortlist from top-speaker signals](sessions/new-watchlist-from-signals.md)** —
  review first-time mentions and direction flips from the top-30 speakers
  without changing your Buzzberg account.

## Using It From Your Own Code

If you don't use Claude Desktop / Cursor / Cline / Continue, you can talk to
the MCP server directly with the official Python SDK over Streamable HTTP:

```python
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    headers = {"Authorization": "Bearer bzb_YOUR_KEY_HERE"}
    async with streamablehttp_client(
        "https://mcp.buzzberg.ai/mcp",
        headers=headers,
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([t.name for t in tools.tools])  # 29 tools

            result = await session.call_tool(
                "get_sentiment",
                arguments={"ticker": "NVDA", "days": 7},
            )
            print(result.content[0].text)

asyncio.run(main())
```

If your agent framework only supports legacy SSE, use
`https://mcp.buzzberg.ai/sse` with the same `Authorization: Bearer ...` header.
Full walkthrough including Windows PowerShell and corporate-laptop
("no install allowed") paths is in [INSTALL.md](INSTALL.md).

## What Your Key Can Do

| Action | Allowed? |
|---|---|
| Read public trade ideas, sentiment, and prices | Yes |
| Save trade ideas to your account | Yes |
| Server sees tool-call arguments Claude sends | Yes* |
| See another user's saved ideas | No |
| Change another user's saved ideas | No |
| Place trades on an exchange | No |
| See your full Claude conversation | No |
| Access your X, broker, or other accounts | No |
| Download files from your computer | No |

*Buzzberg receives only MCP requests and tool arguments selected by your client,
not your full Claude transcript. Avoid putting sensitive private text into tool
arguments.

## Supported Clients

| Client | Status |
|---|---|
| Claude web / Desktop | Recommended: remote connector with OAuth |
| Claude Mobile | Uses the remote connector from the same Claude account |
| Claude Code | Recommended: Streamable HTTP `/mcp` with OAuth |
| Codex | Streamable HTTP `/mcp` with OAuth or a personal key |
| OpenClaw | Supported via Streamable HTTP `/mcp` |
| Cursor | Supported |
| Cline | Supported |
| Continue.dev | Supported |
| Custom Python (mcp SDK) | Supported via Streamable HTTP `/mcp` |
| Agent SDK | Manual config supported |

Buzzberg exposes two MCP transports:

- Streamable HTTP: `https://mcp.buzzberg.ai/mcp` for OAuth-capable and newer agents.
- Legacy SSE: `https://mcp.buzzberg.ai/sse` remains available for existing and older clients.

## Tools, Prompts, And Resources

Buzzberg exposes 29 tools — read (`get_recent_idea_candidates`,
`search_trade_ideas`, `get_top_speakers`,
`get_sentiment`, `get_ticker_timeseries`, `get_most_mentioned_tickers`,
`get_top_sentiment_tickers`, `get_recent_source_text`, `get_tickers_overview`,
`get_speaker_trade_ideas`, `get_speaker_ticker_history`,
`get_speaker_lens`, `get_speaker_lens_context`, `get_price`, ...) and one account-scoped write tool
(`save_trade_idea`). See [TOOLS.md](TOOLS.md) for
signatures and per-tool examples in [examples/](examples).

Buzzberg also exposes MCP prompts and resources:

- `prompts/list` shows ready-made research workflows such as complete
  exact-window idea review, ticker deep dive, daily alpha brief, research-post
  extraction, stock-list candidates, speaker story, and sentiment/price reads.
- `resources/list` exposes lightweight context such as `buzzberg://workflows`,
  `buzzberg://data-boundaries`, `buzzberg://top-speakers`, and
  `buzzberg://market/leaderboards`.

Clients that do not support prompts/resources can still use all tools normally;
these are additive capabilities, not a replacement for existing tools.

## Trust And Verification

The recommended OAuth connector does not install code on your computer and does
not expose a personal API key to the client configuration.

The optional `buzzberg-mcp` package remains available for API-key compatibility
setups. pip uses HTTPS and package hashes from the index for download integrity,
but pip does not automatically verify Sigstore attestations.

Buzzberg releases use PyPI Trusted Publishing through GitHub OIDC. Attestations
are available for manual verification — see [SECURITY.md](SECURITY.md) for the
current verification status and threat model. (The exact
`pypi-attestations verify` command will be published once the Test PyPI smoke
confirms working syntax.)

## Links

- [INSTALL.md](INSTALL.md) — simple setup by AI client
- [TOOLS.md](TOOLS.md) — full tool reference
- [SECURITY.md](SECURITY.md) — threat model, disclosure, attestations
- [sessions/](sessions) — ready-made research workflows
- [examples/](examples) — per-tool example prompts
- [CHANGELOG.md](CHANGELOG.md) — breaking changes during private beta
