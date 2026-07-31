# Connect Buzzberg MCP

Buzzberg MCP lets your AI agent use Buzzberg market intelligence: trade ideas,
sentiment, speakers, prices, ticker mentions, source snippets, and your own
saved ideas.

## Recommended: Standard OAuth

Use OAuth when your client supports remote MCP authentication. You sign in to
Buzzberg in the browser and do not need to create, copy, or store a personal API
key.

### Claude Web, Desktop, And Mobile

1. In Claude web or Desktop, open **Customize -> Connectors**.
2. Select **+ -> Add custom connector**.
3. Name it **Buzzberg** and enter:

   ```text
   https://mcp.buzzberg.ai/mcp
   ```

4. Leave the OAuth client ID, client secret, and other advanced fields empty.
5. Select **Add**, then **Connect**.
6. Sign in to Buzzberg and approve access.
7. Enable Buzzberg from the Connectors menu in a conversation.

The connector follows the same Claude account across web, Desktop, and mobile.
Adding custom connectors directly on mobile is still in beta; web or Desktop is
the simplest setup path. Team and Enterprise workspaces require an owner to add
the connector before members can connect it.

### Claude Code

Add the Streamable HTTP server:

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

The login command opens the standard MCP OAuth flow in your browser.

## Personal API Keys For Existing And Other Clients

Existing `bzb_...` keys, `/sse` connections, Claude Desktop helper installs,
and manually configured clients continue to work. Use this path only when your
client cannot complete standard MCP OAuth.

1. Open Buzzberg.
2. Go to **Profile -> MCP Access**.
3. Click **New Key**.
4. Copy the key that starts with `bzb_`.

Keep this key private. Treat it like a password.

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
manually.

### Claude Desktop

Claude Desktop's local config expects a stdio server. Use `mcp-remote` as the
local bridge to Buzzberg's Streamable HTTP endpoint:

```json
{
  "mcpServers": {
    "buzzberg": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@0.1.38",
        "https://mcp.buzzberg.ai/mcp",
        "--transport",
        "http-only",
        "--header",
        "X-API-Key:bzb_YOUR_KEY_HERE"
      ]
    }
  }
}
```

Claude Desktop config paths:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

After editing, fully quit and reopen the client.
Do not share screenshots of this config after adding your real key.
The pinned bridge uses only Streamable HTTP and will not fall back to legacy SSE.
Keep `X-API-Key:` exactly as shown, with no space after the colon. If Claude
reports a timeout or disconnect, create a new key and replace only the
`bzb_...` value; revoked keys cannot reconnect.

### Cursor / Cline

These clients can use the direct remote-server config:

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

## Read Before Installing

If you want to inspect the package before installing:

```bash
pip download --only-binary :all: --no-deps buzzberg-mcp -d /tmp/bz
python -m zipfile -l /tmp/bz/buzzberg_mcp-*.whl
python -m pip install /tmp/bz/buzzberg_mcp-*.whl
```

## Troubleshooting

- OAuth connector does not finish: remove the Buzzberg connector, add
  `https://mcp.buzzberg.ai/mcp` again with advanced fields empty, then complete
  the browser sign-in.
- Buzzberg is connected but unavailable in a Claude chat: enable it from the
  conversation's Connectors menu.
- Tools do not appear: fully quit and reopen the client.
- `401 Unauthorized` or `403 Invalid or revoked API key`: create a new key in
  **Profile -> MCP Access**, replace the old `bzb_...` value, then fully restart
  the client.
- `429 Too Many Requests`: read `Retry-After` / `retry_after_seconds`, wait that many seconds, then continue with fewer parallel or bulk calls.
- Health check: `curl https://mcp.buzzberg.ai/health` should return `{"status":"ok","service":"buzzberg-mcp"}`.
