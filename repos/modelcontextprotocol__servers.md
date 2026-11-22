# modelcontextprotocol/servers

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/modelcontextprotocol/servers)

> Model Context Protocol Reference Servers

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔌 MCP & SDKs |
| **Project** | — |
| **Why it's worth a look** | Reference MCP servers (filesystem, GitHub, etc.) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 92.2k |
| 🍴 **Forks** | 12.0k |
| 🐞 **Open issues + PRs** | [17](https://github.com/modelcontextprotocol/servers/issues) |
| 💻 **Languages** | TypeScript 46% · JavaScript 31% · Python 22% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-19 (2d ago) |
| 📅 **Created** | 2024-11-19 |
| 📦 **Latest release** | [v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 34.3 MB |
| 🌐 **Website** | https://modelcontextprotocol.io |

## 📦 Recent releases

### [v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0)
<sub>2026-11-18 · 4d ago</sub>

> **Security fixes**
> v2.5.0 fixes eight vulnerabilities in three servers. Upgrade `mcp-server-git` to 2026.11.18,
> `@modelcontextprotocol/server-filesystem` to 2.4.0 and `@modelcontextprotocol/server-everything` to 2.3.1.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `mcp-server-git` | through 2026.11.11 | 2026.11.18 |
> …

### [v2.4.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)
<sub>2026-11-11 · 11d ago</sub>

> **Security fixes**
> v2.4.0 fixes six vulnerabilities in three servers. Upgrade `@modelcontextprotocol/server-filesystem` to 2.3.0,
> and `mcp-server-git` and `mcp-server-fetch` to 2026.11.11.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `@modelcontextprotocol/server-filesystem` | all versions before 2.3.0, and date versions 2025.1.14 through 2026.8.31 | 2.3.0 |
> …

### [v2.3.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0)
<sub>2026-11-04 · 17d ago</sub>

> **Packages**
> | Package | Version | Registry | In this release |
> | --- | --- | --- | --- |
> | `@modelcontextprotocol/server-everything` | `2.2.1` | npm | **published** |
> | `@modelcontextprotocol/server-filesystem` | `2.2.0` | npm | **published** |
> | `@modelcontextprotocol/server-memory` | `2.1.0` | npm | **published** |
> …

### [v2.2.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.2.0)
<sub>2026-10-28 · 24d ago</sub>

> **Security: Node.js runtime and CA certificate updates (October 2026)**
> On October 20, 2026, eMudhra disclosed that the private keys for eight of its intermediate CA certificates could be recovered from the public certificates. On October 21, Node.js shipped [security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) that update its bundled CA certificates for the compromise and fix several unrelated high-severity runtime CVEs. On October 23, Python's `certifi` 2026.10.23 removed the eMudhra roots `emSign Root CA - C1` and `emSign ECC Root CA - C3`.
> **How these servers stand**
> - **The TypeScript servers rely on the Node.js runtime for certificate checks.** They ship no CA certificates of their own. Only `server-everything` makes outbound HTTPS requests (`gzip-file-as-resource`), and the Node.js it runs on verifies them. `server-filesystem`, `server-memory` and `server-sequential-thinking` make no network connections.
> - **`mcp-server-fetch` verifies HTTPS against the `certifi` bundle**, through `httpx`. Installing from PyPI (`uvx mcp-server-fetch`, `pip install mcp-server-fetch`) resolves the current `certifi`, 2026.10.23 or later. The repository's `fetch` Dockerfile installs from its lockfile, which this release moves to `certifi` 2026.10.23 (#5341).
> - **`mcp-server-git` and `mcp-server-time` make no network connections.**
> …

### [v2.1.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0)
<sub>2026-10-25 · 28d ago</sub>

> **Security fixes**
> v2.1.0 fixes eight vulnerabilities in three servers. Upgrade
> `@modelcontextprotocol/server-filesystem` and `@modelcontextprotocol/server-everything`
> to 2.0.1, and `mcp-server-fetch` to 2026.10.24.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Merge pull request #5592 from modelcontextprotocol/v2/chore/5572-rele…](https://github.com/modelcontextprotocol/servers/commit/c799c8552b0f27b7a33a7b9233773da144dddcf5) | cliffhall |
| 2026-11-18 | [Merge pull request #5597 from modelcontextprotocol/changeset-release/…](https://github.com/modelcontextprotocol/servers/commit/7f383a8e0f34f72b6eb519798633cea5c0769be6) | cliffhall |
| 2026-11-18 | [chore: version packages](https://github.com/modelcontextprotocol/servers/commit/a4a2e2434edf6476762e23c10099ae4931f62519) | github-actions[bot] |
| 2026-11-18 | [Merge pull request #5596 from modelcontextprotocol/v2/fix/5595-memory…](https://github.com/modelcontextprotocol/servers/commit/69f8a37e4698657eea49a1968ca18d55c31608e6) | cliffhall |
| 2026-11-18 | [fix(memory): release held locks when the Streamable HTTP server stops](https://github.com/modelcontextprotocol/servers/commit/af86b99080b0f4af52ca6a8f4f1e043921ec6140) | cliffhall |
| 2026-11-18 | [Merge pull request #5537 from modelcontextprotocol/changeset-release/…](https://github.com/modelcontextprotocol/servers/commit/8e44b8fac205856f95a9cf2297982453ff250181) | cliffhall |
| 2026-11-18 | [chore: version packages](https://github.com/modelcontextprotocol/servers/commit/a13c39e647d8c553501ffe4d3f5d9db9dcc534f7) | github-actions[bot] |
| 2026-11-18 | [Merge pull request #5591 from modelcontextprotocol/v2/chore/5572-pyth…](https://github.com/modelcontextprotocol/servers/commit/d40ba2625341ba22c70b1e83b5c6644a94e45638) | cliffhall |
| 2026-11-18 | [chore: stamp Python CalVer versions for 2026.11.18](https://github.com/modelcontextprotocol/servers/commit/97ed9ec74f370222d4ceec50380d06dff36ac4e5) | github-actions[bot] |
| 2026-11-18 | [Merge pull request #5590 from modelcontextprotocol/v2/fix/ghsa-r2q8-f…](https://github.com/modelcontextprotocol/servers/commit/b7edbca57b8107fbd4ab814d89fe08904618a65d) | cliffhall |

[See all commits ↗](https://github.com/modelcontextprotocol/servers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/modelcontextprotocol/servers.git
```
