# Connect Buzzberg MCP

Buzzberg MCP lets Claude, Cursor, Cline, Continue.dev, and custom MCP clients
use Buzzberg market-intelligence tools.

Private beta currently uses **SSE**:

```text
https://mcp.buzzberg.ai/sse
```

Streamable HTTP `/mcp` is not live yet. If your client only accepts `/mcp`, use
Claude Desktop, Claude Code, Cursor, or Cline for now.

## What's An MCP?

MCP stands for Model Context Protocol. It lets an AI agent connect to external
apps and tools. With Buzzberg connected, your agent can ask Buzzberg for market
data instead of guessing from its training data.

## What Your Agent Can Do

After connecting Buzzberg, your agent can:

- Analyze a ticker: sentiment, mentions, speakers, trade ideas, and source
  snippets.
- Find the most buzzed tickers today or over the last 7 days.
- Compare sentiment vs price and mentions vs price.
- Build a morning briefing from Buzzberg portfolio, top-speaker signals, and
  divergence.
- Add or remove tickers from your Buzzberg watchlist.
- Save trade ideas to your Buzzberg account.

Example prompts:

```text
Use Buzzberg to deep dive NOK. Explain the bull narrative, who is pushing it,
what is missing from the bear case, and what I should watch next.
```

```text
Use Buzzberg to show the most buzzed tickers in the last 7 days. Separate fresh
discovery from crowded post-move chatter.
```

## What Buzzberg Can Access

Your MCP key can access:

- Public Buzzberg market-intelligence data.
- Your own Buzzberg watchlist and saved ideas.
- Tool-call arguments your AI client sends to Buzzberg.

Your MCP key cannot:

- Place trades.
- Access your broker, X/Twitter, email, or files.
- See your full Claude/ChatGPT/Cursor conversation.
- Read or modify another user's Buzzberg data.

Keep your `bzb_...` key private. Treat it like a password.

## Get Your MCP Key

1. Open Buzzberg.
2. Go to **Profile -> MCP Access**.
3. Click **New Key**.
4. Copy the key that starts with `bzb_`.

## Connect Your AI Agent

### Claude Desktop

Recommended path:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client claude-desktop
```

Then fully quit and reopen Claude Desktop.

### Claude Code

Run this in your terminal:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

Then ask:

```text
Use Buzzberg to get the current price for BTC.
```

### Cursor

Recommended path:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client cursor
```

Or add this MCP server in Cursor settings:

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

### Cline

Recommended path:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client cline
```

Or open **Cline -> Settings -> Edit MCP Settings** and add the same
`mcpServers` JSON block used for Cursor.

### Continue.dev

Recommended path:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client continue
```

Manual config lives in:

```text
~/.continue/config.json
```

### Python Client

Use this if you are writing your own MCP client. Do not `POST /mcp`; Buzzberg
private beta currently uses SSE.

```bash
pip install mcp
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
```

```python
import asyncio
import os
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    headers = {"Authorization": f"Bearer {os.environ['BUZZBERG_MCP_API_KEY']}"}
    async with sse_client("https://mcp.buzzberg.ai/sse", headers=headers) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([tool.name for tool in tools.tools])

asyncio.run(main())
```

### Other MCP Clients

Use these settings:

```text
Transport: SSE
URL: https://mcp.buzzberg.ai/sse
Header: Authorization: Bearer bzb_YOUR_KEY_HERE
```

### Codex And ChatGPT

Codex and ChatGPT MCP apps generally expect Streamable HTTP. Buzzberg's
Streamable HTTP `/mcp` endpoint is not live yet, so use Claude Desktop, Claude
Code, Cursor, or Cline during private beta.

## No-Install Manual Setup

If you do not want to install the helper package, edit your client config
manually and add:

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

Claude Desktop config paths:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

After editing, fully quit and reopen the client.

## Read Before Installing

If you want to inspect the package before installing:

```bash
pip download --only-binary :all: --no-deps buzzberg-mcp -d /tmp/bz
python -m zipfile -l /tmp/bz/buzzberg_mcp-*.whl
python -m pip install /tmp/bz/buzzberg_mcp-*.whl
```

## Troubleshooting

- Tools do not appear: fully quit and reopen the client.
- `401 Unauthorized`: revoke and recreate the key in **Profile -> MCP Access**.
- `429 Too Many Requests`: close duplicate clients, wait a minute, then reconnect.
- Python client gets `404` on `/mcp`: use SSE at `https://mcp.buzzberg.ai/sse`.
- Health check: `curl https://mcp.buzzberg.ai/health` should return
  `{"status":"ok","service":"buzzberg-mcp"}`.
