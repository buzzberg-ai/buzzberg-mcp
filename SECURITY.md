# Security Policy

## Reporting

Email security issues to `security@buzzberg.ai`. We acknowledge reports within
72 hours. Please do not file public GitHub issues for vulnerabilities.

## Threat Model

Buzzberg MCP is a hosted remote MCP server. The public package in this repo is
an installer and documentation package; it is not the server implementation.

- Confused deputy: the server resolves each Bearer key to a server-side user
  context. Write tools use that context and do not accept user-id overrides.
- Token passthrough: Buzzberg MCP keys are not passed to downstream market-data
  providers.
- Session hijacking: there is no server-side session cookie for MCP. Each request
  authenticates with a Bearer key.
- SSRF: tool inputs are not arbitrary outbound HTTP URLs.
- Local installer compromise: installer code is public in this repo and releases
  are published with PyPI Trusted Publishing through GitHub OIDC.

See [security-controls.json](security-controls.json) for the sanitized public
mapping of scope claims to enforcement mechanisms.

## What Your Key Can And Cannot Do

| Action | Allowed? |
|---|---|
| Read public trade ideas, sentiment, and prices | Yes |
| Add/remove tickers in your watchlist | Yes |
| Save trade ideas to your account | Yes |
| Server sees tool-call arguments Claude sends | Yes |
| See another user's watchlist or saved ideas | No |
| Change another user's watchlist or saved ideas | No |
| Place trades on an exchange | No |
| See your full Claude conversation | No |
| Access your X, broker, or other accounts | No |
| Download files from your computer | No |

## Key Storage

MCP keys are generated as `bzb_` plus a high-entropy random value from
`secrets.token_urlsafe(32)`. Buzzberg stores a SHA-256 hash of the key, not the
raw key. SHA-256 is appropriate here because the secret is random and high
entropy; this is not a low-entropy password.

## Logging

Buzzberg stores `last_used_at` per key and standard HTTP access logs such as
path, status, IP, and response time. Buzzberg does not intentionally log request
bodies, tool arguments, or MCP response payloads. Per-tool audit logs are on the
roadmap but are not present in this beta.

## What The Server Can See

The server receives MCP requests and tool arguments sent by your client. Tool
arguments are visible to Buzzberg. The server does not receive your full Claude
conversation unless your client chooses to include text from that conversation
inside a tool argument.

## Key Lifecycle

Buzzberg MCP is in private beta. Request a demo key at
[hello@buzzberg.ai](mailto:hello@buzzberg.ai). If you already have beta access,
create keys in Buzzberg Profile -> MCP Access and revoke keys from the same
page. Revoked keys stop authenticating once their `revoked_at` timestamp is set.

If the server is compromised, Buzzberg will revoke all active MCP keys, require
re-issue, and email active MCP users within 72 hours.

## Attestation Verification

pip does not automatically verify Sigstore attestations. Buzzberg releases use
PyPI Trusted Publishing through GitHub OIDC, and attestations are available for
manual verification. The exact `pypi-attestations verify` command will be added
after the Test PyPI smoke test validates the working syntax.
