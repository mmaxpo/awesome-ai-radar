# 21st-dev/magic-mcp

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/21st-dev/magic-mcp)

> It's like v0, but in your Cursor / Claude Code / Windsurf: search 10,000+ React/Tailwind components, generate new UI with AI, and publish your own — right from your editor. Magic MCP is now the 21st MCP; this package keeps old configs working. Setup: 21st.dev/mcp

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔌 MCP & SDKs |
| **Project** | — |
| **Why it's worth a look** | Generates React + Tailwind components from plain language |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 6.5k |
| 🍴 **Forks** | 534 |
| 🐞 **Open issues + PRs** | [9](https://github.com/21st-dev/magic-mcp/issues) |
| 💻 **Languages** | TypeScript 96% · Dockerfile 4% |
| 📜 **License** | ISC |
| 🏷 **Topics** | `21st` `claude` `cursor` `mcp` `model-context-protocol` `react` `tailwindcss` `ui-components` |
| 🕒 **Last activity** | 2026-09-09 (2mo ago) |
| 📅 **Created** | 2025-02-19 |
| 📦 **Latest release** | [v0.2.3](https://github.com/21st-dev/magic-mcp/releases/tag/v0.2.3) — 2026-09-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1.5 MB |
| 🌐 **Website** | https://21st.dev/mcp |

## 📦 Recent releases

### [v0.2.3](https://github.com/21st-dev/magic-mcp/releases/tag/v0.2.3) — 21st MCP compatibility proxy 0.2.3
<sub>2026-09-09 · 2mo ago</sub>

> The compatibility proxy continues to forward tool discovery and calls to the hosted 21st MCP server. Generation tools now depend on the authenticated account's AI access, including for existing proxy versions after refreshing tools or reconnecting.
> This release updates the bundled UI skill, installation guidance, plugin metadata (1.0.1), and the canonical dev.21st/mcp registry manifest (1.0.1). With AI off, agents use component search and retrieval, then adapt the code locally. Cached generation denials explain the required AI access and stop retry loops.
> Validation: TypeScript build, package contents review, and authenticated production smoke through the built stdio proxy passed. The only proxy runtime source change is its reported patch version.
> Published to npm as `@21st-dev/magic@0.2.3` (`latest`) through GitHub Actions Trusted Publishing with provenance. The npm archive exactly matches the attached tested package and SHA-256 checksum. [Verified publishing run](https://github.com/21st-dev/magic-mcp/actions/runs/34402249536). Existing npm installs also receive the server fix.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-09-09 | [ci: publish release archives with npm trusted publishing](https://github.com/21st-dev/magic-mcp/commit/6b5299e8a83ceffa73d4fc4e148905bb3eeeeb55) | serafimcloud |
| 2026-09-09 | [fix: align MCP proxy skills and metadata with hosted AI access](https://github.com/21st-dev/magic-mcp/commit/4fd82ae750b9759a50e0c59d9c3d4a8d313549ac) | serafimcloud |
| 2026-09-01 | [feat: self-hosted marketplace indexes + direct-add install instructions](https://github.com/21st-dev/magic-mcp/commit/6e5a43d3621442a450948864a74396d206b23c65) | bunasQ |
| 2026-08-31 | [feat: add Codex plugin manifest (.codex-plugin/plugin.json) for the C…](https://github.com/21st-dev/magic-mcp/commit/90efda5edd79c56a296fa892c8bea60867c06c7f) | bunasQ |
| 2026-08-31 | [feat: package the 21st MCP as an agent plugin (Cursor / Claude / Grok…](https://github.com/21st-dev/magic-mcp/commit/0410559c03e20dadcdc4b97c8e36510bf2a99df1) | bunasQ |
| 2026-07-31 | [0.2.2: stop asking a question that is already answered](https://github.com/21st-dev/magic-mcp/commit/dfba16c1b9baa63ed4efd0c69121ed08ba697b1a) | serafimcloud |
| 2026-07-24 | [0.2.1: keep the raw endpoint URL out of human-facing copy](https://github.com/21st-dev/magic-mcp/commit/b3ea2b7e0ff09e2d11dffd1e4fd0ef7f05077b8d) | serafimcloud |
| 2026-07-24 | [chore: drop unused git-operations util left from pre-proxy code](https://github.com/21st-dev/magic-mcp/commit/5e5e424ca20464fdeb1e2df26e5ccc8ab9a01cf7) | serafimcloud |
| 2026-07-24 | [v0.2.0: Magic MCP becomes a thin proxy to the unified 21st MCP](https://github.com/21st-dev/magic-mcp/commit/2b50dd9e4165d12641a9a42ec22d5d33252f7509) | serafimcloud |
| 2026-02-17 | [Merge pull request #41 from 21st-dev/fix/security-patches](https://github.com/21st-dev/magic-mcp/commit/b07bc9d1c0ce6fa7d70d831c103ffa7b71b4f8f8) | bunasQ |

[See all commits ↗](https://github.com/21st-dev/magic-mcp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/21st-dev/magic-mcp.git
```
