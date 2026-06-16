"""Constants shared by the Buzzberg MCP installer."""

VERSION = "0.1.0b4"
MCP_URL = "https://mcp.buzzberg.ai/sse"
MCP_HTTP_URL = "https://mcp.buzzberg.ai/mcp"
MCP_HEALTH_URL = "https://mcp.buzzberg.ai/health"
SERVER_NAME = "buzzberg"
AUTH_HEADER = "Authorization"
BETA_BANNER = (
    f"Buzzberg MCP v{VERSION} (BETA). "
    "Issues: https://github.com/buzzberg-ai/buzzberg-mcp/issues"
)

CLIENT_CHOICES = (
    "claude-desktop",
    "claude-code",
    "cursor",
    "cline",
    "continue",
)
