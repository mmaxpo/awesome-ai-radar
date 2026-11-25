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
| ⭐ **Stars** | 34.2k |
| 🍴 **Forks** | 4.1k |
| 🐞 **Open issues + PRs** | [578](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 39% · TypeScript 21% · HTML 12% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 306.5 MB |
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
| 2026-11-25 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/8b71cff92cc556445c81313f8976933700dd4d6b) | github-actions[bot] |
| 2026-11-25 | [Add Ratchet plugin: line budget that stops agents from growing your r…](https://github.com/davila7/claude-code-templates/commit/a430092eaf36de2452903596378fc903c097b56d) | krishansubudhi |
| 2026-11-25 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/c4de112c9a0043261861dc55d92168eeb80b3127) | github-actions[bot] |
| 2026-11-24 | [feat(mcp): ask for a type or category on broad searches (form elicita…](https://github.com/davila7/claude-code-templates/commit/6db5ee05400346eaf1ad85f6d9de03ffb040fdc1) | davila7 |
| 2026-11-24 | [docs(claude-md): how to add an MCP component that serves skills (#1706)](https://github.com/davila7/claude-code-templates/commit/5f9e764638a88efb00d5ef247b7f15bcf3d7f225) | davila7 |
| 2026-11-24 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/b588e987e9cf32b72990c56afcae275a4bcea7ea) | github-actions[bot] |
| 2026-11-24 | [feat(mcp): serve the Skills over MCP example from mcp.aitmpl.com (#1704)](https://github.com/davila7/claude-code-templates/commit/69c881e858bb3cb60cb3266ac9030af1a8be0b83) | davila7 |
| 2026-11-24 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/a6a23d0ac4a2e403715837b76e6c64f2a5e36d5b) | github-actions[bot] |
| 2026-11-24 | [feat: Skills over MCP in MCP components, with an example server (#1701)](https://github.com/davila7/claude-code-templates/commit/0ee9bafdd18ea100658b57fa9a3a3df000f8f4be) | davila7 |
| 2026-11-24 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/be9f77d7efb1f34968eb83e673ca3c97b732ffe0) | github-actions[bot] |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
