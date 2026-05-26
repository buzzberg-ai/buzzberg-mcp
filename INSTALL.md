# Install Buzzberg MCP

## Recommended Install

```bash
pip install buzzberg-mcp
buzzberg-mcp setup
```

For one client:

```bash
buzzberg-mcp setup --client cursor
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

## Paranoid Path

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

## Manual Install

Use this path if your security policy forbids installing packages. Add the
Buzzberg server to your client config manually.

Transport: `sse`
URL: `https://mcp.buzzberg.ai/sse`
Header: `Authorization: Bearer <key from Profile -> MCP Access>`

### Claude Desktop

macOS:
`~/Library/Application Support/Claude/claude_desktop_config.json`

Windows:
`%APPDATA%/Claude/claude_desktop_config.json`

Linux:
`~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "buzzberg": {
      "url": "https://mcp.buzzberg.ai/sse",
      "headers": {
        "Authorization": "Bearer <BUZZBERG_MCP_API_KEY>"
      }
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport sse buzzberg https://mcp.buzzberg.ai/sse \
  --header "Authorization: Bearer $BUZZBERG_MCP_API_KEY"
```

### Claude Mobile

Use URL `https://mcp.buzzberg.ai/sse` and header
`Authorization: Bearer <BUZZBERG_MCP_API_KEY>` where the mobile integration UI
supports custom headers. If headers are unavailable, use Desktop, Code, Cursor,
or Cline during private beta.

### Cursor

Settings -> MCP Servers -> Add new:

```json
{
  "mcpServers": {
    "buzzberg": {
      "url": "https://mcp.buzzberg.ai/sse",
      "headers": {
        "Authorization": "Bearer <BUZZBERG_MCP_API_KEY>"
      }
    }
  }
}
```

### Cline

VS Code -> Cline -> Settings -> Edit MCP Settings. Add the same `mcpServers`
block used for Cursor.

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
            "Authorization": "Bearer <BUZZBERG_MCP_API_KEY>"
          }
        }
      }
    ]
  }
}
```

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

## Troubleshooting

- Tools do not appear: fully quit and reopen the client, then validate JSON.
- 401 Unauthorized: revoke and recreate the key in Profile -> MCP Access.
- Connection timeout: corporate networks sometimes block SSE.
- Health check: `curl https://mcp.buzzberg.ai/health` should return `{"status":"ok"}`.
