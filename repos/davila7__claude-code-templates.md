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
| ⭐ **Stars** | 34.0k |
| 🍴 **Forks** | 4.1k |
| 🐞 **Open issues + PRs** | [543](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 40% · TypeScript 21% · HTML 12% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 306.9 MB |
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
| 2026-11-20 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/e88848056dc85ded577b3b7368f351344e3536ce) | github-actions[bot] |
| 2026-11-20 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/053feb29f36e3e5ee9da29c964eb3723a7915bf8) | github-actions[bot] |
| 2026-11-20 | [Add GitRanks Contribute MCP to devtools (#1582)](https://github.com/davila7/claude-code-templates/commit/c125da1e4bef95766a312165a7b313f1a272dc4c) | maslianok |
| 2026-11-20 | [Add Sofya MCP to web-data (#1586)](https://github.com/davila7/claude-code-templates/commit/b3d9fac28866f3d63cb3fdab3ea739839bd7e7d2) | yusufgurdogan |
| 2026-11-20 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/1c6049978aa3a85c61df3018742c7fccf4533b1b) | github-actions[bot] |
| 2026-11-20 | [Add subagents-pane plugin: live pane of agents, skills and plans (#1616)](https://github.com/davila7/claude-code-templates/commit/6ffd27c64cdd6595e8149747129c7df8772f5d9b) | qaokss |
| 2026-11-20 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/6d52d5ae2a18a54cdc047d5bb20f752b057664ab) | github-actions[bot] |
| 2026-11-20 | [Add 6 review skills from off-grid-ai/skills as external skills (#1601)](https://github.com/davila7/claude-code-templates/commit/d7d12930a1d766836a16d3daef1246791c1e425e) | alichherawalla |
| 2026-11-20 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/ae5a6b27c52f54fea60ee651ea6b23eaa2be9b0f) | github-actions[bot] |
| 2026-11-20 | [Add lemlist MCP to marketing (#1628)](https://github.com/davila7/claude-code-templates/commit/aa96da95531a5c2736357676791d59e931e6535a) | micktaiwan |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
