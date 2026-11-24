# upstash/context7

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/upstash/context7)

> Context7 Platform -- Up-to-date docs for AI agents

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Up-to-date library docs for coding agents (MCP) |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 65.4k |
| 🍴 **Forks** | 3.3k |
| 🐞 **Open issues + PRs** | [60](https://github.com/upstash/context7/issues) |
| 💻 **Languages** | TypeScript 98% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llm` `mcp` `mcp-server` `vibe-coding` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-03-26 |
| 📦 **Latest release** | [mcpb-v4.8.0](https://github.com/upstash/context7/releases/tag/mcpb-v4.8.0) — 2026-11-24 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 50.9 MB |
| 🌐 **Website** | https://context7.com |

## 📦 Recent releases

### [mcpb-v4.8.0](https://github.com/upstash/context7/releases/tag/mcpb-v4.8.0) — context7.mcpb 4.8.0
<sub>2026-11-24 · today</sub>

> MCP Bundle for [@upstash/context7-mcp@4.8.0](https://github.com/upstash/context7/releases/tag/%40upstash%2Fcontext7-mcp%404.8.0)

### [@upstash/context7-pi@0.2.0](https://github.com/upstash/context7/releases/tag/%40upstash/context7-pi%400.2.0)
<sub>2026-11-24 · today</sub>

> **Minor Changes**
> - 32dccfd: Agents pass the version a project uses as its own value, not as a suffix of the library ID. `query-docs` (MCP and pi) takes a `version` input and `ctx7 docs` a `--tag` option, sent to `/v2/context` as `version`; Context7 serves that version or the closest one it has. `resolve-library-id` no longer lists versions.

### [@upstash/context7-mcp@4.8.0](https://github.com/upstash/context7/releases/tag/%40upstash/context7-mcp%404.8.0)
<sub>2026-11-24 · today</sub>

> **Minor Changes**
> - 3e98f32: Serve the context7-mcp skill through the MCP skills extension (SEP-2640).
> - 32dccfd: Agents pass the version a project uses as its own value, not as a suffix of the library ID. `query-docs` (MCP and pi) takes a `version` input and `ctx7 docs` a `--tag` option, sent to `/v2/context` as `version`; Context7 serves that version or the closest one it has. `resolve-library-id` no longer lists versions.

### [ctx7@0.13.0](https://github.com/upstash/context7/releases/tag/ctx7%400.13.0)
<sub>2026-11-24 · today</sub>

> **Minor Changes**
> - 32dccfd: Agents pass the version a project uses as its own value, not as a suffix of the library ID. `query-docs` (MCP and pi) takes a `version` input and `ctx7 docs` a `--tag` option, sent to `/v2/context` as `version`; Context7 serves that version or the closest one it has. `resolve-library-id` no longer lists versions.
> - 11cb18d: Add `--vscode-insiders` to `ctx7 setup` and `ctx7 remove`. Global setup now writes to the VS Code Insiders user folder, and you can combine it with `--vscode` in one command. The setup picker and auto-detection do not list VS Code Insiders, so use the flag.
>   `ctx7 remove` no longer deletes a skill from a shared skills folder (such as `~/.agents/skills`) while another agent still uses it.
> **Patch Changes**
> - 88beb24: `ctx7 setup` also continues with OAuth when the browser login is refused an API key by the teamspace's policy, instead of ending with "Authorization denied".
> …

### [mcpb-v4.7.3](https://github.com/upstash/context7/releases/tag/mcpb-v4.7.3) — context7.mcpb 4.7.3
<sub>2026-11-17 · 7d ago</sub>

> MCP Bundle for [@upstash/context7-mcp@4.7.3](https://github.com/upstash/context7/releases/tag/%40upstash%2Fcontext7-mcp%404.7.3)

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [CTX7-4056: Document SCIM provisioning with Microsoft Entra ID (#3924)](https://github.com/upstash/context7/commit/be7f5c3075dde929a59f130a5b6e2d33926ab027) | fahreddinozcan |
| 2026-11-24 | [CTX7-4063: Show framed screenshots at the column width (#3930)](https://github.com/upstash/context7/commit/2c1e8641a99d344a2a016e9aaf4c5c1f4c5c6744) | fahreddinozcan |
| 2026-11-24 | [chore(release): version packages (#3886)](https://github.com/upstash/context7/commit/e67df84541654e9afab0c44556891d3cc3bbb971) | github-actions[bot] |
| 2026-11-24 | [CTX7-4060: Switch setup to OAuth when the device login is refused an …](https://github.com/upstash/context7/commit/88beb243f7042bb2a2129c9b81498720d909bde2) | fahreddinozcan |
| 2026-11-24 | [CTX7-4058: Add the 2.0.3 on-prem changelog (#3928)](https://github.com/upstash/context7/commit/9169e8b29fd744758e1fe2d3a2e826177b61b7a9) | fahreddinozcan |
| 2026-11-24 | [CTX7-3901: Document OAuth sign-in for on-prem MCP clients and write k…](https://github.com/upstash/context7/commit/2f472ff9f3dbed77403b34766effa24e0f62de90) | fahreddinozcan |
| 2026-11-24 | [CTX7-4006: Switch setup to OAuth when the teamspace refuses API keys …](https://github.com/upstash/context7/commit/82b851fcfeefd7f9a2c4fb0e1e3c598270dae522) | fahreddinozcan |
| 2026-11-24 | [CTX7-4050: Add a guide for putting Context7 behind your own MCP gatew…](https://github.com/upstash/context7/commit/eebfe62a41dda3e1a591d098d061a59334a48af0) | fahreddinozcan |
| 2026-11-23 | [CTX7-3978: Support VS Code Insiders in ctx7 setup (#3878)](https://github.com/upstash/context7/commit/11cb18d81c93bffe6c9c662ec7cb605f34ea6946) | fahreddinozcan |
| 2026-11-23 | [CTX7-4022: Tighten the Azure DevOps on-prem docs and add screenshots …](https://github.com/upstash/context7/commit/d648d80cf7484e7d0107892253a6a9b30d04d1e2) | fahreddinozcan |

[See all commits ↗](https://github.com/upstash/context7/commits)

## ⬇️ Get it

```bash
git clone https://github.com/upstash/context7.git
```
