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
| ⭐ **Stars** | 92.3k |
| 🍴 **Forks** | 12.0k |
| 🐞 **Open issues + PRs** | [27](https://github.com/modelcontextprotocol/servers/issues) |
| 💻 **Languages** | TypeScript 47% · JavaScript 30% · Python 23% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2024-11-19 |
| 📦 **Latest release** | [v2.6.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0) — 2026-11-27 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 33.9 MB |
| 🌐 **Website** | https://modelcontextprotocol.io |

## 📦 Recent releases

### [v2.6.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.6.0)
<sub>2026-11-27 · today</sub>

> **Security fixes**
> v2.6.0 fixes eight vulnerabilities in three servers, and completes two fixes that v2.5.0 left open. Upgrade `mcp-server-git` to 2026.11.27,
> `@modelcontextprotocol/server-memory` to 2.2.2 and `mcp-server-fetch` to 2026.11.27; on Windows, also `@modelcontextprotocol/server-filesystem` to 2.4.1.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `mcp-server-git` | through 2026.11.18 | 2026.11.27 |
> …

### [v2.5.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.5.0)
<sub>2026-11-18 · 9d ago</sub>

> **Security fixes**
> v2.5.0 fixes eight vulnerabilities in three servers. Upgrade `mcp-server-git` to 2026.11.18,
> `@modelcontextprotocol/server-filesystem` to 2.4.0 and `@modelcontextprotocol/server-everything` to 2.3.1.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `mcp-server-git` | through 2026.11.11 | 2026.11.18 |
> …

### [v2.4.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.4.0)
<sub>2026-11-11 · 16d ago</sub>

> **Security fixes**
> v2.4.0 fixes six vulnerabilities in three servers. Upgrade `@modelcontextprotocol/server-filesystem` to 2.3.0,
> and `mcp-server-git` and `mcp-server-fetch` to 2026.11.11.
> | Package | Affected | Fixed in |
> | --- | --- | --- |
> | `@modelcontextprotocol/server-filesystem` | all versions before 2.3.0, and date versions 2025.1.14 through 2026.8.31 | 2.3.0 |
> …

### [v2.3.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.3.0)
<sub>2026-11-04 · 22d ago</sub>

> **Packages**
> | Package | Version | Registry | In this release |
> | --- | --- | --- | --- |
> | `@modelcontextprotocol/server-everything` | `2.2.1` | npm | **published** |
> | `@modelcontextprotocol/server-filesystem` | `2.2.0` | npm | **published** |
> | `@modelcontextprotocol/server-memory` | `2.1.0` | npm | **published** |
> …

### [v2.2.0](https://github.com/modelcontextprotocol/servers/releases/tag/v2.2.0)
<sub>2026-10-28 · 29d ago</sub>

> **Security: Node.js runtime and CA certificate updates (October 2026)**
> On October 20, 2026, eMudhra disclosed that the private keys for eight of its intermediate CA certificates could be recovered from the public certificates. On October 21, Node.js shipped [security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) that update its bundled CA certificates for the compromise and fix several unrelated high-severity runtime CVEs. On October 23, Python's `certifi` 2026.10.23 removed the eMudhra roots `emSign Root CA - C1` and `emSign ECC Root CA - C3`.
> **How these servers stand**
> - **The TypeScript servers rely on the Node.js runtime for certificate checks.** They ship no CA certificates of their own. Only `server-everything` makes outbound HTTPS requests (`gzip-file-as-resource`), and the Node.js it runs on verifies them. `server-filesystem`, `server-memory` and `server-sequential-thinking` make no network connections.
> - **`mcp-server-fetch` verifies HTTPS against the `certifi` bundle**, through `httpx`. Installing from PyPI (`uvx mcp-server-fetch`, `pip install mcp-server-fetch`) resolves the current `certifi`, 2026.10.23 or later. The repository's `fetch` Dockerfile installs from its lockfile, which this release moves to `certifi` 2026.10.23 (#5341).
> - **`mcp-server-git` and `mcp-server-time` make no network connections.**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [Merge pull request #5685 from modelcontextprotocol/v2/chore/5681-rele…](https://github.com/modelcontextprotocol/servers/commit/b502fd9fc711de7285977396db3b8a732d1c9f64) | cliffhall |
| 2026-11-27 | [Merge pull request #5682 from modelcontextprotocol/v2/chore/5681-pyth…](https://github.com/modelcontextprotocol/servers/commit/c0075947ac6be8bb402d0fb202ba68b2455f0909) | cliffhall |
| 2026-11-27 | [Merge pull request #5684 from modelcontextprotocol/v2/chore/5683-memo…](https://github.com/modelcontextprotocol/servers/commit/5de8459a2c01410d661259fbf6d656cf5fc7afc1) | cliffhall |
| 2026-11-27 | [test(memory): count a real Windows refusal of the lock put-back as a …](https://github.com/modelcontextprotocol/servers/commit/53afb97437da20225756908b0de1f1d4de766724) | cliffhall |
| 2026-11-27 | [chore: stamp Python CalVer versions for 2026.11.27](https://github.com/modelcontextprotocol/servers/commit/f1515d83c834e8b1910ee773389b05f994436a7b) | github-actions[bot] |
| 2026-11-27 | [Merge pull request #5633 from modelcontextprotocol/changeset-release/…](https://github.com/modelcontextprotocol/servers/commit/ee4f57cfa37486aec1c6872b39de09776db942ff) | cliffhall |
| 2026-11-27 | [chore: version packages](https://github.com/modelcontextprotocol/servers/commit/f779c21cea825ec201820ac7acbbc107a6c1eabd) | github-actions[bot] |
| 2026-11-27 | [Merge pull request #5677 from modelcontextprotocol/v2/fix/ghsa-5pwg-5…](https://github.com/modelcontextprotocol/servers/commit/b85db8a8c79a9469c3936e65b7a4e4a07e41b999) | cliffhall |
| 2026-11-27 | [test(git): compare the planted alternates entry as bytes](https://github.com/modelcontextprotocol/servers/commit/eb9c526b84e3a8d5f3e9a436c2e4d26d3ac25eb0) | cliffhall |
| 2026-11-27 | [test(git): write the marker blob with LF line endings on every platform](https://github.com/modelcontextprotocol/servers/commit/3a9143021c55224b756a9dd96398cda2747089a2) | cliffhall |

[See all commits ↗](https://github.com/modelcontextprotocol/servers/commits)

## ⬇️ Get it

```bash
git clone https://github.com/modelcontextprotocol/servers.git
```
