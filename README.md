# Buzzberg MCP

[![PyPI](https://img.shields.io/pypi/v/buzzberg-mcp)](https://pypi.org/project/buzzberg-mcp/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-private--beta-orange)

> Private Beta: the MCP contract can change before broader beta. See
> [CHANGELOG.md](CHANGELOG.md) for breaking changes.

Buzzberg MCP connects Claude, Cursor, Cline, Continue.dev, and other MCP clients
to Buzzberg market intelligence: trade ideas, sentiment, speakers, prices, and
watchlist actions for your own Buzzberg account.

## Connect Your AI Agent

### 1. Get Your Buzzberg Key

1. Open Buzzberg.
2. Go to **Profile -> MCP Access**.
3. Click **New Key**.
4. Copy the key that starts with `bzb_`.

Keep this key private. Treat it like a password.

### 2. Connect Your Client

#### Claude Desktop

**Fast path:**

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client claude-desktop
```

Paste your `bzb_...` key when setup asks for it, then fully quit and reopen
Claude Desktop.

**No pip / manual path:**

1. Open your Claude Desktop config file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add:

```json
{
  "mcpServers": {
    "buzzberg": {
      "url": "https://mcp.buzzberg.ai/sse",
      "headers": {
        "Authorization": "Bearer bzb_YOUR_KEY_HERE"
      }
    }
  }
}
```

3. Fully quit and reopen Claude Desktop.

Claude's **Settings -> Connectors -> Add custom connector** flow is coming
after Buzzberg adds OAuth. Today that UI does not accept user-pasted static
Bearer keys, so the local config path above is the working Claude Desktop path.

#### Claude Code

Run this in Terminal:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

#### Codex

Codex uses Streamable HTTP. Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.buzzberg]
url = "https://mcp.buzzberg.ai/mcp"
bearer_token_env_var = "BUZZBERG_MCP_API_KEY"
```

Then start Codex from a shell where the key is available:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
codex
```

#### OpenClaw

OpenClaw can save remote MCP servers with Streamable HTTP:

```bash
openclaw mcp set buzzberg '{"url":"https://mcp.buzzberg.ai/mcp","transport":"streamable-http","headers":{"Authorization":"Bearer bzb_YOUR_KEY_HERE"}}'
```

#### Cursor, Cline, Continue.dev

The helper can write the config for these clients too:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client cursor      # or: cline / continue
```

More client-by-client setup options are in [INSTALL.md](INSTALL.md).

## What You Can Do With It

Buzzberg is useful when you want your AI agent to read the market conversation,
not just fetch a price. Ask one plain-English question; Claude, Codex, or
another MCP client chains the right Buzzberg tools and turns the raw source data
into a usable research read.

Start with these prompts:

```text
Use Buzzberg to summarize the last 24h of top-50 speaker tweets.
What are the main themes, crowded trades, new tickers, and disagreements?
Quote examples.
```

```text
Use Buzzberg to read public Substack text from the last 24h.
Give me a market TLDR and list tickers with the strongest narratives.
Quote examples.
```

```text
Use Buzzberg to read YouTube transcripts from the last 24h.
What are speakers worried about that is not obvious from price action?
Quote examples.
```

```text
Use Buzzberg Twitter data from top-50 speakers.
How many times did they mention "bottleneck", "power", "AI capex", and "memory"?
Quote examples and point to the tickers each theme is about.
```

What Buzzberg sends to the AI agent:

- **Substack/newsletters:** public/free article text from the last 24 hours.
  Paid posts return only the public preview visible before the paywall.
- **YouTube:** transcript text from the last 24 hours, with timestamped
  segments when available.
- **Twitter/X:** top-speaker tweets from the last 24 hours where Buzzberg found
  ticker ideas, including the full tweet text, speaker, tickers, and direction:
  `LONG`, `SHORT`, `WATCH`, `AVOID`, or `NEUTRAL`. This is not every tweet.
- **Ticker research:** mentions, sentiment, trade ideas, speaker profiles,
  price snapshots, and daily sentiment/mention history for chart-style reads.

Ready-made workflows:

- **[Daily source TLDRs](sessions/daily-source-tldr.md)** — summarize the last
  24 hours of top-50 speaker tweets, public Substack text, and YouTube
  transcripts; ask for themes, crowded trades, repeated words, disagreements,
  and quoted examples.
- **[Ticker leaderboards](sessions/ticker-leaderboards.md)** — most buzzed
  tickers, strongest bullish/bearish sentiment, and daily historical buzz for
  1d / 7d / 30d windows.
- **[Morning briefing](sessions/morning-briefing.md)** — AI portfolio state +
  fresh calls from top speakers + sentiment divergence radar in one read.
- **[Narrative ticker deep dive](sessions/ticker-deep-dive.md)** — what
  Buzzberg uniquely knows about a ticker: who is pushing it, what the bull
  narrative is, what is missing, and whether the setup is early or crowded.
- **[Sentiment vs price chart](sessions/sentiment-price-chart.md)** — daily
  sentiment, mentions, and cached close prices so Claude can explain whether
  Buzzberg sentiment leads, confirms, or lags price.
- **[Mentions vs price chart](sessions/mentions-price-chart.md)** — attention
  spikes vs price moves, useful for spotting narrative ignition, exhaustion,
  and post-move crowding.
- **[Contrarian scan](sessions/contrarian-scan.md)** — tickers where
  smart-money disagrees the most, ranked by sentiment spread. High-volatility
  setups where the camps are obvious.
- **[Build a watchlist from top-speaker signals](sessions/new-watchlist-from-signals.md)** —
  auto-curate first-time mentions and direction flips from the top-30 speakers
  in the last 24 hours.

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
            print([t.name for t in tools.tools])  # 21 tools

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
| Add/remove tickers in your watchlist | Yes |
| Save trade ideas to your account | Yes |
| Server sees tool-call arguments Claude sends | Yes* |
| See another user's watchlist or saved ideas | No |
| Change another user's watchlist or saved ideas | No |
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
| Claude Desktop | Supported via helper installer |
| Claude Code | Supported via SSE |
| Codex | Supported via Streamable HTTP `/mcp` |
| OpenClaw | Supported via Streamable HTTP `/mcp` |
| Cursor | Supported |
| Cline | Supported |
| Continue.dev | Supported |
| Custom Python (mcp SDK) | Supported via Streamable HTTP `/mcp` |
| Claude Mobile | Works only where custom headers are available |
| Agent SDK | Manual config supported |

Buzzberg exposes two MCP transports:

- Streamable HTTP: `https://mcp.buzzberg.ai/mcp` for Codex, OpenClaw, and newer agents.
- Legacy SSE: `https://mcp.buzzberg.ai/sse` for Claude Desktop, Claude Code, Cursor, Cline, and older clients.

## Tools

Buzzberg exposes 21 tools — read (`search_trade_ideas`, `get_top_speakers`,
`get_sentiment`, `get_ticker_timeseries`, `get_most_mentioned_tickers`,
`get_top_sentiment_tickers`, `get_recent_source_text`, `get_portfolio`, `get_price`, ...) and write
(`add_to_watchlist`, `save_trade_idea`, ...). See [TOOLS.md](TOOLS.md) for
signatures and per-tool examples in [examples/](examples).

## Trust And Verification

The normal path is `pip install buzzberg-mcp`. pip uses HTTPS and package hashes
from the index for download integrity, but pip does not automatically verify
Sigstore attestations.

Buzzberg releases use PyPI Trusted Publishing through GitHub OIDC. Attestations
are available for manual verification — see [SECURITY.md](SECURITY.md) for the
current verification status and threat model. (The exact
`pypi-attestations verify` command will be published once the Test PyPI smoke
confirms working syntax.)

## Links

- [INSTALL.md](INSTALL.md) — simple setup by AI client
- [TOOLS.md](TOOLS.md) — full tool reference
- [SECURITY.md](SECURITY.md) — threat model, disclosure, attestations
- [sessions/](sessions) — seven ready-made research workflows
- [examples/](examples) — per-tool example prompts
- [CHANGELOG.md](CHANGELOG.md) — breaking changes during private beta
