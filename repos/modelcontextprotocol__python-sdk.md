# modelcontextprotocol/python-sdk

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/modelcontextprotocol/python-sdk)

> The official Python SDK for Model Context Protocol servers and clients

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔌 MCP & SDKs |
| **Project** | — |
| **Why it's worth a look** | Official Python SDK to build MCP servers/clients |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 24.9k |
| 🍴 **Forks** | 4.1k |
| 🐞 **Open issues + PRs** | [413](https://github.com/modelcontextprotocol/python-sdk/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `mcp` `mcp-server` `mcp-client` |
| 🕒 **Last activity** | 2026-11-05 (9d ago) |
| 📅 **Created** | 2024-09-24 |
| 📦 **Latest release** | [v2.3.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.3.0) — 2026-10-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 17.8 MB |
| 🌐 **Website** | https://py.sdk.modelcontextprotocol.io/ |

## 📦 Recent releases

### [v2.3.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.3.0)
<sub>2026-10-02 · 1mo ago</sub>

> `pip install -U mcp`. Docs: https://py.sdk.modelcontextprotocol.io/
> Mostly fixes, plus three new options. A few things behave differently, so skim these first:
> **Behaviour changes**
> **`httpx2>=2.10.0` is now required** (#3600)
> - It was `>=2.5.0`. The new `max_sse_event_size` option needs it.
> - Nothing to do unless you pin `httpx2` below 2.10.
> …

### [v2.2.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0)
<sub>2026-09-07 · 2mo ago</sub>

> `pip install -U mcp`. Docs: https://py.sdk.modelcontextprotocol.io/
> A few defaults changed in this release. If you run a server or client on 2.x, skim these first:
> **Behaviour changes**
> **HTTP client redirects are only followed within the endpoint's origin** (#3397)
> - `Client("https://...")`, `streamable_http_client` and `sse_client` follow a redirect only if it stays on the same scheme, host and port (or upgrades `http` to `https` on the same host).
> - A redirect anywhere else is not followed: the call fails with `MCPError` and the session stays usable (an SSE connect fails with `httpx2.HTTPStatusError`). If that other URL is the server you meant, use it as the endpoint URL.
> …

### [v1.30.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0)
<sub>2026-09-07 · 2mo ago</sub>

> Maintenance release of the 1.x line. 2.x is the current line; 1.x docs are at https://py.sdk.modelcontextprotocol.io/v1/.
> A few defaults changed in this release. If you run a server or client on 1.x, skim these first:
> **Behaviour changes**
> **HTTP client redirects are only followed within the endpoint's origin** (#3448)
> - `streamable_http_client` and `sse_client` follow a redirect only if it stays on the same scheme, host and port (or upgrades `http` to `https` on the same host).
> - A redirect anywhere else now fails the request with `httpx.HTTPStatusError`. If that other URL is the server you meant, use it as the endpoint URL.
> …

### [v2.0.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.1)
<sub>2026-08-26 · 2mo ago</sub>

> One off backport of the FastMCP import warning for `2.0.x`, this is due to a lot of people running into this error and making issues on other repos about it. Ideally either pin `mcp<2` or upgrade to 2.
> **What's Changed**
> * [v2.0.x] Point imports of mcp.server.fastmcp at the migration guide by @maxisbey in https://github.com/modelcontextprotocol/python-sdk/pull/3393
> **Full Changelog**: https://github.com/modelcontextprotocol/python-sdk/compare/v2.0.0...v2.0.1

### [v2.1.1](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.1.1)
<sub>2026-08-25 · 2mo ago</sub>

> **What's Changed**
> * Point imports of mcp.server.fastmcp at the migration guide by @maxisbey in https://github.com/modelcontextprotocol/python-sdk/pull/3388
> **Full Changelog**: https://github.com/modelcontextprotocol/python-sdk/compare/v2.1.0...v2.1.1

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-05 | [Generate single-line `model_config` in surface types (#3820)](https://github.com/modelcontextprotocol/python-sdk/commit/77001c96f9507be0f4d009b83210a384a5e08bda) | Kludex |
| 2026-11-05 | [Keep unknown keys on client and server capabilities (#3812)](https://github.com/modelcontextprotocol/python-sdk/commit/82adc272e85c12f620df21db34b6086ed7619548) | Kludex |
| 2026-11-03 | [Bump the github-actions group with 7 updates (#3797)](https://github.com/modelcontextprotocol/python-sdk/commit/af4c6f4db2cd207f44374cd324a12cfbee8d2da6) | dependabot[bot] |
| 2026-10-27 | [Carry `capabilities.extensions` on legacy `initialize` handshakes (#3…](https://github.com/modelcontextprotocol/python-sdk/commit/d7845c073a2b9ba5ab2817ecf93d3e45ef24cd14) | Kludex |
| 2026-10-24 | [Give bare `dict`, `set` and `frozenset` return annotations structured…](https://github.com/modelcontextprotocol/python-sdk/commit/a525a3d9bece967d91534b746a6c842931b7b4ec) | Kludex |
| 2026-10-24 | [Treat `typing.Dict[str, X]` return annotations like `dict[str, X]` (#…](https://github.com/modelcontextprotocol/python-sdk/commit/5a3a23af65def4d636864d55701ff9395cad92d0) | Kludex |
| 2026-10-24 | [Drop generated titles from tool input and output schemas (#3757)](https://github.com/modelcontextprotocol/python-sdk/commit/72ff38cb5cb7c0f6d5024d1b185e5bf0c05f0cb0) | Kludex |
| 2026-10-24 | [Resolve open code scanning alerts (#3755)](https://github.com/modelcontextprotocol/python-sdk/commit/86ca12b4e977fe4739b478430e2b86018126ed6e) | Kludex |
| 2026-10-24 | [Bump the python-security group across 1 directory with 4 updates (#3752)](https://github.com/modelcontextprotocol/python-sdk/commit/910efd9497057f0c636afaebf52a2b9f8bf0c3b8) | dependabot[bot] |
| 2026-10-17 | [Give each SSE response its own header list (#3726)](https://github.com/modelcontextprotocol/python-sdk/commit/2af9e3089ac66b35c1550c500aae86a82efb1e17) | Kludex |

[See all commits ↗](https://github.com/modelcontextprotocol/python-sdk/commits)

## ⬇️ Get it

```bash
git clone https://github.com/modelcontextprotocol/python-sdk.git
```
