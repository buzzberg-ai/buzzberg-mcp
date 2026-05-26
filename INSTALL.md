# Install Buzzberg MCP

## Start Here

Buzzberg MCP lets Claude, Cursor, Cline, and other MCP clients use Buzzberg
tools. You only need three things:

1. A Buzzberg account with private beta access.
2. A personal MCP key.
3. One MCP client, such as Claude Desktop or Claude Code.

Get your key first:

1. Open Buzzberg in your browser.
2. Go to **Profile -> MCP Access**.
3. Click **New Key**.
4. Copy the key that starts with `bzb_`.

Keep this key private. Treat it like a password.

## Which Install Should I Use?

| If you use... | Use this path |
|---|---|
| Claude Desktop | Option 1: installer |
| Cursor, Cline, or Continue.dev | Option 1: installer |
| Claude Code terminal app | Option 2: Claude Code command |
| Corporate laptop where installs are blocked | Option 3: manual JSON |
| Custom Python MCP client | Option 4: Python SSE example |
| Claude Mobile or Agent SDK | Option 5: other clients |
| Security review before install | Option 6: read before installing |

Buzzberg private beta currently uses **SSE**:

```text
https://mcp.buzzberg.ai/sse
```

The newer Streamable HTTP `/mcp` endpoint is not live yet.

## Option 1: Easiest Installer

Install the package:

```bash
pip install buzzberg-mcp
```

Run setup:

```bash
buzzberg-mcp setup
```

The setup command asks for your key with hidden input:

```text
BUZZBERG_MCP_API_KEY (input hidden):
```

Paste the `bzb_...` key and press Enter. The key is written into your MCP
client config as an `Authorization: Bearer ...` header.

If you are not sure what to choose, run:

```bash
buzzberg-mcp setup
```

The installer will look for supported clients and ask before writing anything.

For one specific client:

```bash
buzzberg-mcp setup --client claude-desktop
```

Other supported client names:

```bash
buzzberg-mcp setup --client cursor
buzzberg-mcp setup --client cline
buzzberg-mcp setup --client continue
```

For all detected clients:

```bash
buzzberg-mcp setup --all
```

The installer reads your key through a hidden prompt by default. For password
managers, use stdin:

```bash
pass show buzzberg/mcp | buzzberg-mcp setup --key-stdin --client claude-desktop
```

Dry-runs do not need a real key and never print a plaintext key:

```bash
buzzberg-mcp setup --dry-run --client claude-desktop
```

## Option 2: Claude Code Command

If you use Claude Code, this is the simplest path. Replace
`bzb_YOUR_KEY_HERE` with your key from **Profile -> MCP Access**:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

On Windows PowerShell:

```powershell
$env:BUZZBERG_MCP_API_KEY = "bzb_YOUR_KEY_HERE"
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse --header "Authorization: Bearer $env:BUZZBERG_MCP_API_KEY"
```

Then ask Claude Code something like:

```text
Use Buzzberg to get the current price for BTC.
```

## Option 3: Manual JSON

Use this path if you do not want to install anything. You will edit your MCP
client config file manually.

Transport: `sse`
URL: `https://mcp.buzzberg.ai/sse`
Header: `Authorization: Bearer <your bzb_ key>`

### Claude Desktop

macOS config file:

```text
~/Library/Application Support/Claude/claude_desktop_config.json
```

Windows config file:

```text
%APPDATA%/Claude/claude_desktop_config.json
```

Add this block. If the file already has `mcpServers`, add only the `buzzberg`
entry inside it.

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

After saving the file, fully quit Claude Desktop and reopen it.

### Cursor

Open Cursor settings, find **MCP Servers**, and add:

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

Open VS Code -> Cline -> Settings -> Edit MCP Settings. Add the same
`mcpServers` block used for Cursor.

### Continue.dev

Edit `~/.continue/config.json`:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "name": "buzzberg",
        "transport": {
          "type": "sse",
          "url": "https://mcp.buzzberg.ai/sse",
          "headers": {
            "Authorization": "Bearer bzb_YOUR_KEY_HERE"
          }
        }
      }
    ]
  }
}
```

## Option 4: Python Client

Use this if you are writing your own Python MCP client. Do not `POST /mcp`;
Buzzberg private beta currently uses SSE at `/sse`.

```bash
pip install mcp
```

```python
import asyncio
import os

from mcp import ClientSession
from mcp.client.sse import sse_client

BUZZBERG_KEY = os.environ["BUZZBERG_MCP_API_KEY"]

async def main():
    headers = {"Authorization": f"Bearer {BUZZBERG_KEY}"}

    async with sse_client(
        "https://mcp.buzzberg.ai/sse",
        headers=headers,
    ) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print([tool.name for tool in tools.tools])

            result = await session.call_tool(
                "get_price",
                arguments={"symbols": ["BTC"]},
            )
            print(result)

asyncio.run(main())
```

Run it:

```bash
export BUZZBERG_MCP_API_KEY="bzb_YOUR_KEY_HERE"
python buzzberg_test.py
```

## Option 5: Other Clients

### Claude Mobile

Use URL `https://mcp.buzzberg.ai/sse` and header
`Authorization: Bearer <BUZZBERG_MCP_API_KEY>` where the mobile integration UI
supports custom headers. If headers are unavailable, use Desktop, Code, Cursor,
or Cline during private beta.

### Agent SDK

```python
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    mcp_servers={
        "buzzberg": {
            "type": "sse",
            "url": "https://mcp.buzzberg.ai/sse",
            "headers": {"Authorization": f"Bearer {KEY}"},
        }
    },
    allowed_tools=["mcp__buzzberg__*"],
)
```

### Any MCP Client

Use these settings:

```text
Transport: SSE
URL: https://mcp.buzzberg.ai/sse
Header: Authorization: Bearer bzb_YOUR_KEY_HERE
```

If the client only supports Streamable HTTP `/mcp`, it will not work yet.

## Option 6: Read Before Installing

This path lets you inspect the wheel before installing it. It is the path for
"read before running"; a normal `pip install` may run package build/install code
by design.

```bash
pip download --only-binary :all: --no-deps buzzberg-mcp -d /tmp/bz
python -m zipfile -l /tmp/bz/buzzberg_mcp-*.whl
python -m pip install /tmp/bz/buzzberg_mcp-*.whl
```

Attestation verification is optional. The exact `pypi-attestations verify`
command will be copied here after it passes the Test PyPI smoke test.

## Troubleshooting

- Tools do not appear: fully quit and reopen the client, then validate JSON.
- 401 Unauthorized: revoke and recreate the key in Profile -> MCP Access.
- Connection timeout: corporate networks sometimes block SSE.
- Health check: `curl https://mcp.buzzberg.ai/health` should return `{"status":"ok"}`.
