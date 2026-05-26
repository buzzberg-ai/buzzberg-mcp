# Buzzberg MCP

![status](https://img.shields.io/badge/status-private--beta-orange)

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
| Claude Mobile | Works only where custom headers are available |
| Agent SDK | Manual config supported |

Private beta currently uses SSE at `https://mcp.buzzberg.ai/sse`. Streamable
HTTP `/mcp` ships before broader beta; `/sse` will remain for legacy clients for
a migration window.

## Tools

Buzzberg exposes 17 tools. See [TOOLS.md](TOOLS.md) for signatures and examples.

## Trust And Verification

The normal path is `pip install buzzberg-mcp`. pip uses HTTPS and package hashes
from the index for download integrity, but pip does not automatically verify
Sigstore attestations.

Buzzberg releases use PyPI Trusted Publishing through GitHub OIDC. Attestations
are available for manual verification; the exact command will be published after
the Test PyPI smoke test confirms the working `pypi-attestations` syntax.

Read more in [SECURITY.md](SECURITY.md).

## Links

- [INSTALL.md](INSTALL.md)
- [SECURITY.md](SECURITY.md)
- [TOOLS.md](TOOLS.md)
- [examples](examples)
- [sessions](sessions)
- [CHANGELOG.md](CHANGELOG.md)
