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

## Quickstart

Get your key first:

1. Open Buzzberg.
2. Go to **Profile -> MCP Access**.
3. Click **New Key** and copy the `bzb_...` key.

Then install and configure:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup
```

`pip install` does not need your key. `buzzberg-mcp setup` will ask for it with
hidden input, then write the client config for Claude Desktop, Cursor, Cline, or
Continue.dev.

Claude Code users can also use the direct command:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

## What You Can Do With It

Seven ready-made research workflows. Each one is a single prompt that Claude
chains through the right Buzzberg tools and turns the raw data into a usable
research read:

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
the MCP server directly with the official Python SDK. ~10 lines:

```python
import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    headers = {"Authorization": "Bearer bzb_YOUR_KEY_HERE"}
    async with sse_client(
        "https://mcp.buzzberg.ai/sse",
        headers=headers,
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([t.name for t in tools.tools])  # 20 tools

            result = await session.call_tool(
                "get_sentiment",
                arguments={"ticker": "NVDA", "days": 7},
            )
            print(result.content[0].text)

asyncio.run(main())
```

If your agent framework supports MCP SSE servers with custom auth headers
(LangChain, AutoGen, Anthropic Agent SDK and similar generally do), point it
at `https://mcp.buzzberg.ai/sse` with the Bearer header. Full walkthrough
including Windows PowerShell and corporate-laptop ("no install allowed") paths
is in [INSTALL.md](INSTALL.md).

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
| Claude Desktop | Supported |
| Claude Code | Supported via SSE beta transport |
| Cursor | Supported |
| Cline | Supported |
| Continue.dev | Supported |
| Custom Python (mcp SDK) | Supported — see [INSTALL.md option 4](INSTALL.md#option-4-python-client) |
| Claude Mobile | Works only where custom headers are available |
| Agent SDK | Manual config supported |

Private beta currently uses SSE at `https://mcp.buzzberg.ai/sse`. Streamable
HTTP `/mcp` ships before broader beta; `/sse` will remain for legacy clients for
a migration window.

## Tools

Buzzberg exposes 20 tools — read (`search_trade_ideas`, `get_top_speakers`,
`get_sentiment`, `get_ticker_timeseries`, `get_most_mentioned_tickers`,
`get_top_sentiment_tickers`, `get_portfolio`, `get_price`, ...) and write
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

- [INSTALL.md](INSTALL.md) — six install paths including custom Python
- [TOOLS.md](TOOLS.md) — full tool reference
- [SECURITY.md](SECURITY.md) — threat model, disclosure, attestations
- [sessions/](sessions) — seven ready-made research workflows
- [examples/](examples) — per-tool example prompts
- [CHANGELOG.md](CHANGELOG.md) — breaking changes during private beta
