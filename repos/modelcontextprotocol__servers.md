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
| ⭐ **Stars** | 92.0k |
| 🍴 **Forks** | 12.0k |
| 🐞 **Open issues + PRs** | [18](https://github.com/modelcontextprotocol/servers/issues) |
| 💻 **Languages** | TypeScript 47% · JavaScript 33% · Python 19% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-12 (yesterday) |
| 📅 **Created** | 2024-11-19 |
| 📦 **Latest release** | [v2.4.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 33.8 MB |
| 🌐 **Website** | https://modelcontextprotocol.io |

## 📦 Recent releases

### [v2.4.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)
<sub>2026-11-11 · 2d ago</sub>

> **Security fixes**
> v2.4.0 fixes six vulnerabilities in three servers. Upgrade `@modelcontextprotocol/server-filesystem` to 2.3.0,
> and `mcp-server-git` and `mcp-server-fetch` to 2026.11.11.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `@modelcontextprotocol/server-filesystem` | all versions before 2.3.0, and date versions 2025.1.14 through 2026.8.31 | 2.3.0 |
> …

### [v2.3.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0)
<sub>2026-11-04 · 8d ago</sub>

> **Packages**
> | Package | Version | Registry | In this release |
> | --- | --- | --- | --- |
> | `@modelcontextprotocol/server-everything` | `2.2.1` | npm | **published** |
> | `@modelcontextprotocol/server-filesystem` | `2.2.0` | npm | **published** |
> | `@modelcontextprotocol/server-memory` | `2.1.0` | npm | **published** |
> …

### [v2.2.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.2.0)
<sub>2026-10-28 · 15d ago</sub>

> **Security: Node.js runtime and CA certificate updates (October 2026)**
> On October 20, 2026, eMudhra disclosed that the private keys for eight of its intermediate CA certificates could be recovered from the public certificates. On October 21, Node.js shipped [security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) that update its bundled CA certificates for the compromise and fix several unrelated high-severity runtime CVEs. On October 23, Python's `certifi` 2026.10.23 removed the eMudhra roots `emSign Root CA - C1` and `emSign ECC Root CA - C3`.
> **How these servers stand**
> - **The TypeScript servers rely on the Node.js runtime for certificate checks.** They ship no CA certificates of their own. Only `server-everything` makes outbound HTTPS requests (`gzip-file-as-resource`), and the Node.js it runs on verifies them. `server-filesystem`, `server-memory` and `server-sequential-thinking` make no network connections.
> - **`mcp-server-fetch` verifies HTTPS against the `certifi` bundle**, through `httpx`. Installing from PyPI (`uvx mcp-server-fetch`, `pip install mcp-server-fetch`) resolves the current `certifi`, 2026.10.23 or later. The repository's `fetch` Dockerfile installs from its lockfile, which this release moves to `certifi` 2026.10.23 (#5341).
> - **`mcp-server-git` and `mcp-server-time` make no network connections.**
> …

### [v2.1.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.1.0)
<sub>2026-10-25 · 19d ago</sub>

> **Security fixes**
> v2.1.0 fixes eight vulnerabilities in three servers. Upgrade
> `@modelcontextprotocol/server-filesystem` and `@modelcontextprotocol/server-everything`
> to 2.0.1, and `mcp-server-fetch` to 2026.10.24.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> …

### [v2.0.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.0.0)
<sub>2026-10-19 · 25d ago</sub>

> **Servers refactored to modern era**
> This release refactors all the servers to support the modern era spec, while still answering legacy era clients as expected.
> **Packages**
> | Package | Version | Registry | In this release |
> | --- | --- | --- | --- |
> | `@modelcontextprotocol/server-everything` | `2.0.0` | npm | **published** |
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [Merge pull request #5518 from modelcontextprotocol/v2/chore/5509-rele…](https://github.com/modelcontextprotocol/servers/commit/e1dc4b18dbb948921da37f3d4224a628730b43b0) | cliffhall |
| 2026-11-11 | [Merge pull request #5470 from modelcontextprotocol/changeset-release/…](https://github.com/modelcontextprotocol/servers/commit/6cfff622fb8eb41e2504340d5a6105d34094143c) | cliffhall |
| 2026-11-11 | [chore: version packages](https://github.com/modelcontextprotocol/servers/commit/5c6686a8c35864aa0675f63ee956aae87ea69ea3) | github-actions[bot] |
| 2026-11-11 | [Merge pull request #5510 from modelcontextprotocol/v2/chore/5509-pyth…](https://github.com/modelcontextprotocol/servers/commit/4ac5add6c09426c3b14c831a1c14a7c3f27416d5) | cliffhall |
| 2026-11-11 | [Merge pull request #5516 from modelcontextprotocol/v2/fix/ghsa-p9cv-8…](https://github.com/modelcontextprotocol/servers/commit/0d53550e078021e0f82b07f4cab47d77d362df78) | cliffhall |
| 2026-11-11 | [Merge pull request #5515 from modelcontextprotocol/v2/fix/ghsa-3rxj-6…](https://github.com/modelcontextprotocol/servers/commit/faef80baca51f9c9277341422729ed162927e72f) | cliffhall |
| 2026-11-11 | [Merge pull request #5514 from modelcontextprotocol/v2/fix/ghsa-6hqx-g…](https://github.com/modelcontextprotocol/servers/commit/1629bb33208a9d98b77abce4b52b2808d3090bb0) | cliffhall |
| 2026-11-11 | [fix(filesystem): address review round 4 for GHSA-p9cv-8g75-4xcg](https://github.com/modelcontextprotocol/servers/commit/505476dbdca218fd6a7b8f0c0ab95fbc5351313e) | cliffhall |
| 2026-11-11 | [fix(filesystem): address review round 3 for GHSA-p9cv-8g75-4xcg](https://github.com/modelcontextprotocol/servers/commit/3d22dc17b5d1b434267c9d42f22e7d5b336875fe) | cliffhall |
| 2026-11-11 | [fix(filesystem): address review round 2 for GHSA-p9cv-8g75-4xcg](https://github.com/modelcontextprotocol/servers/commit/db4cdfddfd447fee6a86ddd5e93f23203160cc2b) | cliffhall |

[See all commits ↗](https://github.com/modelcontextprotocol/servers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/modelcontextprotocol/servers.git
```
