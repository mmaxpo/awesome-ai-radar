# davila7/claude-code-templates

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/davila7/claude-code-templates)

> Open-source registry and CLI for Claude Code components: agents, commands, skills, hooks, MCPs, settings and mods

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Ready-made Claude Code templates: agents, commands, settings |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 34.1k |
| 🍴 **Forks** | 4.1k |
| 🐞 **Open issues + PRs** | [556](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 39% · TypeScript 21% · HTML 11% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 309.6 MB |
| 🌐 **Website** | https://www.aitmpl.com |

## 📦 Recent releases

### [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7)
<sub>2026-10-09 · 1mo ago</sub>

> **Security**
> - **Fix command injection in the analytics Console Bridge** (port 3334) —
>   GHSA-4jm9-m3fr-9jpx, reported by @manus-pi. Affected 1.11.0 through
>   1.29.6. Terminal input is spawned with argv and passed through the
>   environment instead of interpolated into `expect`/`osascript` source, the
>   macOS `do script` fallback is removed, and the WebSocket handshake now
> …

### [v1.29.6](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.6) — v1.29.6 — Claude Mods: --mod installs Anthropic-layout plugins, 24 mods
<sub>2026-09-17 · 2mo ago</sub>

> Function Hooks become **Claude Mods**. Anthropic renamed the feature, shipped it
> behind an early-access flag in Claude Code >= 2.1.259, and published the source of
> its three built-in mods plus the full TypeScript declarations
> ([anthropics/claude-code#91870](https://github.com/anthropics/claude-code/issues/91870),
> [`mods/`](https://github.com/anthropics/claude-code/tree/main/mods)). This release
> aligns the CLI, the catalog and the site with what actually ships.
> …

### [v1.29.5](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.5) — v1.29.5 — Function Hooks: install TypeScript hooks from the catalog
<sub>2026-09-09 · 2mo ago</sub>

> Function Hooks land in the CLI. This release ships the `--function-hook` flag,
> which installs any of the 10 function hooks from the catalog as a local Claude
> Code plugin.
> Function hooks are Claude Code's proposed fifth hook type
> ([anthropics/claude-code#91870](https://github.com/anthropics/claude-code/issues/91870)):
> instead of a shell command that can only allow, deny or inject text, you write a
> …

### [v1.28.3](https://github.com/davila7/claude-code-templates/releases/tag/v1.28.3) — v1.28.3 - Plugin Skills Support in Skills Manager
<sub>2025-11-15 · 1y ago</sub>

> **🎯 Skills Manager: Plugin Skills Support**
> The Skills Manager Dashboard now detects and displays skills installed from Claude Code plugins!
> **✨ New Features**
> - **3-Source Skill Detection**: Skills Manager now scans three locations:
>   - 📁 **Personal**: `~/.claude/skills/` - Manually installed skills
>   - 📂 **Project**: `.claude/skills/` - Project-specific skills
> …

### [v1.27.0](https://github.com/davila7/claude-code-templates/releases/tag/v1.27.0) — v1.27.0 - Docker Sandbox Provider
<sub>2025-11-02 · 1y ago</sub>

> **🐳 Docker Sandbox Provider - Version 1.27.0**
> Execute Claude Code in isolated local Docker containers with complete control over your development environment.
> **✨ New Features**
> **Docker Sandbox Provider**
> - **Fully Local Execution**: Run Claude Code in isolated Docker containers
> - **Claude Agent SDK Integration**: Correct async generator implementation for reliable code generation
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/44fd6fda16f51e5accdde254d5f530fb45de7390) | github-actions[bot] |
| 2026-11-22 | [Drop the cumulative installers chart from /trending (#1658)](https://github.com/davila7/claude-code-templates/commit/ff245092fb27e84772da944e6976ab5641d3f31e) | davila7 |
| 2026-11-22 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/ea3c74fec310f73af16b51554a9d5fbba669271c) | github-actions[bot] |
| 2026-11-22 | [Add dependency-cooldown setting: skip packages published in the last …](https://github.com/davila7/claude-code-templates/commit/81dd4392f696da0b85e636f933e069b7ee468515) | davila7 |
| 2026-11-22 | [Redesign the component Files tab: one card, outline menu, line number…](https://github.com/davila7/claude-code-templates/commit/3c907d7700f6e883965ab31744908a1bf5382d70) | davila7 |
| 2026-11-21 | [docs(readme): use Proxy-Seller's partner tracking link (#1655)](https://github.com/davila7/claude-code-templates/commit/5a8853e7f0cbf5173451e329ae073250e6c442ca) | davila7 |
| 2026-11-21 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/2fbe86762ebc872fadc5495f3ae4171e27a5e4d8) | github-actions[bot] |
| 2026-11-21 | [Rewrite vulnerability-scanner skill: AI and agent risks, 2025/2026 OW…](https://github.com/davila7/claude-code-templates/commit/e3c1c93c12d14d52afa61b22577bfec613646f09) | davila7 |
| 2026-11-21 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/f37bd13c4644677a8390160b8a8f4ae9c136ca14) | github-actions[bot] |
| 2026-11-21 | [Leaderboard: "Harness Components Leaderboard" heading, searchable pag…](https://github.com/davila7/claude-code-templates/commit/fb7a8a09287a01584b6cd072e879ffcedd15f59e) | davila7 |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
