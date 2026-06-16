# Changelog

## Beta Period

SemVer is not guaranteed before `1.0.0`. Breaking changes will be documented
here and announced to active beta users.

## 0.1.0b2

- Fixes Claude Desktop setup. Claude Desktop local config expects stdio MCP
  servers, so the installer now writes an `npx mcp-remote` bridge entry instead
  of a direct `url` / `headers` remote-server block.
- Updates Claude Desktop manual setup docs to match the working config.

## 0.1.0b1

- Initial private beta installer package.
- Adds stdlib-only client config writers for Claude Desktop, Claude Code,
  Cursor, Cline, and Continue.dev.
- Adds public SECURITY.md, TOOLS.md, examples, and release workflow skeleton.
