# Connect Buzzberg MCP

Buzzberg MCP lets your AI agent use Buzzberg market intelligence: trade ideas,
sentiment, speakers, prices, ticker mentions, source snippets, and your own
watchlist.

You need one thing first: a Buzzberg MCP key.

## Get Your Key

1. Open Buzzberg.
2. Go to **Profile -> MCP Access**.
3. Click **New Key**.
4. Copy the key that starts with `bzb_`.

Keep this key private. Treat it like a password.

## Claude Desktop

Use this if you are on the normal Claude desktop app.

1. Open Terminal.
2. Run:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client claude-desktop
```

3. Paste your `bzb_...` key when setup asks for it. The input is hidden.
4. Fully quit Claude Desktop (`Cmd+Q` on macOS), then reopen it.
5. Ask Claude:

```text
Use Buzzberg to get the current price for BTC.
```

## Claude Code

Use this if you work from the `claude` CLI.

Ask Claude Code:

```text
Add Buzzberg as an MCP server.
Use SSE URL https://mcp.buzzberg.ai/sse.
Use Authorization: Bearer from my BUZZBERG_MCP_API_KEY environment variable.
```

Or run this manually:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

Then ask:

```text
Use Buzzberg to deep dive NOK. Who is bullish, what is the bull case, what are the risks, and what should I watch next?
```

## Codex

Use this if you want Codex to call Buzzberg tools.

Ask Codex:

```text
Add Buzzberg MCP to my Codex config.
Use Streamable HTTP URL https://mcp.buzzberg.ai/mcp.
Use bearer_token_env_var = "BUZZBERG_MCP_API_KEY".
Do not paste the secret key into the config file.
```

Manual setup:

1. Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.buzzberg]
url = "https://mcp.buzzberg.ai/mcp"
bearer_token_env_var = "BUZZBERG_MCP_API_KEY"
```

2. Start Codex from a shell where the key exists:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
codex
```

3. Ask Codex:

```text
Use Buzzberg to find the most mentioned tickers in the last 24 hours.
```

## OpenClaw

OpenClaw supports saved MCP server definitions.

Ask OpenClaw:

```text
Add Buzzberg as a remote MCP server.
Use Streamable HTTP URL https://mcp.buzzberg.ai/mcp.
Send Authorization: Bearer bzb_YOUR_KEY_HERE.
```

Manual setup:

```bash
openclaw mcp set buzzberg '{"url":"https://mcp.buzzberg.ai/mcp","transport":"streamable-http","headers":{"Authorization":"Bearer bzb_YOUR_KEY_HERE"}}'
```

You can check that the definition was saved:

```bash
openclaw mcp show buzzberg
```

Note: `openclaw mcp set` saves config. Your OpenClaw runtime decides when to
open the actual MCP connection.

## Cursor

Recommended:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client cursor
```

Manual config:

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

## Cline

Recommended:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client cline
```

Manual path: open **Cline -> Settings -> Edit MCP Settings** and add the same
`mcpServers` JSON block used for Cursor.

## Continue.dev

Recommended:

```bash
pip install buzzberg-mcp
buzzberg-mcp setup --client continue
```

Manual config lives in:

```text
~/.continue/config.json
```

## Python Client

Use Streamable HTTP for new clients:

```bash
pip install mcp
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
```

```python
import asyncio
import os
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    headers = {"Authorization": f"Bearer {os.environ['BUZZBERG_MCP_API_KEY']}"}
    async with streamablehttp_client(
        "https://mcp.buzzberg.ai/mcp",
        headers=headers,
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([tool.name for tool in tools.tools])

            result = await session.call_tool(
                "get_sentiment",
                arguments={"ticker": "NVDA", "days": 7},
            )
            print(result.content[0].text)

asyncio.run(main())
```

If your client only supports legacy SSE, use:

```text
URL: https://mcp.buzzberg.ai/sse
Header: Authorization: Bearer bzb_YOUR_KEY_HERE
```

## Any Other MCP Client

Use one of these:

```text
Streamable HTTP URL: https://mcp.buzzberg.ai/mcp
Legacy SSE URL:       https://mcp.buzzberg.ai/sse
Header:               Authorization: Bearer bzb_YOUR_KEY_HERE
```

Prefer Streamable HTTP for new clients. Use SSE for clients that explicitly ask
for SSE or have no `/mcp` support yet.

## Example Prompts

```text
Use Buzzberg to deep dive NOK. Explain the bull narrative, who is pushing it,
what is missing from the bear case, and what I should watch next.
```

```text
Use Buzzberg to show the most buzzed tickers in the last 7 days. Separate fresh
discovery from crowded post-move chatter.
```

```text
Use Buzzberg to compare sentiment and mentions vs price for NVDA over the last
30 days. Tell me if sentiment is leading, confirming, or lagging price.
```

## Beta Rate Limits

Buzzberg MCP is rate-limited during private beta. The current default limits are
about **120 tool calls per minute per user** and **2,000 tool calls per day per
user**, with an additional shared server-wide safety cap.

If your client gets `429 Too Many Requests`, wait for the `Retry-After` header
or `retry_after_seconds` value before continuing. Agents should avoid tight
retry loops, large parallel batches, and unbounded scans. Prefer one broad scan
or leaderboard first, then targeted follow-ups with small `limit`, `days`,
`top_n`, or `max_per_day` values. Speaker trade-history tools require one
`speaker_name`; there is no endpoint for dumping every speaker's ideas.

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
- `429 Too Many Requests`: read `Retry-After` / `retry_after_seconds`, wait that many seconds, then continue with fewer parallel or bulk calls.
- `/mcp` returns `404`: the server deploy has not reached your region yet; use SSE or try again after deploy.
- Health check: `curl https://mcp.buzzberg.ai/health` should return `{"status":"ok","service":"buzzberg-mcp"}`.
