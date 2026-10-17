"""Constants shared by the Buzzberg MCP installer."""

VERSION = "1.0.0"
MCP_URL = "https://mcp.buzzberg.ai/sse"
MCP_HTTP_URL = "https://mcp.buzzberg.ai/mcp"
MCP_HEALTH_URL = "https://mcp.buzzberg.ai/health"
MCP_REMOTE_PACKAGE = "mcp-remote@0.1.38"
SERVER_NAME = "buzzberg"
AUTH_HEADER = "Authorization"
DESKTOP_API_KEY_HEADER = "X-API-Key"
BANNER = (
    f"Buzzberg MCP v{VERSION}. "
    "Issues: https://github.com/buzzberg-ai/buzzberg-mcp/issues"
)

CLIENT_CHOICES = (
    "claude-desktop",
    "claude-code",
    "cursor",
    "cline",
    "continue",
)
