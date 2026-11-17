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
| ⭐ **Stars** | 33.9k |
| 🍴 **Forks** | 4.0k |
| 🐞 **Open issues + PRs** | [533](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 40% · TypeScript 21% · HTML 12% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 297.5 MB |
| 🌐 **Website** | https://aitmpl.com |

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
| 2026-11-17 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268) | github-actions[bot] |
| 2026-11-17 | [Rewrite api-security-audit agent: endpoint map, OWASP API Top 10 2023…](https://github.com/davila7/claude-code-templates/commit/291762626caaaa180186dcc387211b9e1f3d2bba) | davila7 |
| 2026-11-17 | [mcp: make tool descriptions purely descriptive (#1596)](https://github.com/davila7/claude-code-templates/commit/a70d5f836e2474f97ef3509a1fc3633fc5e0e351) | davila7 |
| 2026-11-17 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/d8e4f386ed05fb554f9f5b24aa50f94965c7fb69) | github-actions[bot] |
| 2026-11-17 | [fix(mcp): partial-match fallback in search; fix force-push-blocker an…](https://github.com/davila7/claude-code-templates/commit/78b6ff4e36ce40b496d144e6197a94d60d40ed2a) | davila7 |
| 2026-11-17 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/b006fe0ee67c03076dadeba6c4360a6751b039f9) | github-actions[bot] |
| 2026-11-17 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/7d2d9c426ad2938975d061048329a802e85ea00f) | github-actions[bot] |
| 2026-11-17 | [feat(mcp): remote aitmpl MCP server for the catalog (mcp.aitmpl.com) …](https://github.com/davila7/claude-code-templates/commit/2e6fa9c138817da54f2515c3fccc023bdaf628a4) | davila7 |
| 2026-11-17 | [Blog: Bright Data Search skill spotlight (#1593)](https://github.com/davila7/claude-code-templates/commit/062a90ce680a1358089afb76cfc363cdbe5da13b) | davila7 |
| 2026-11-16 | [chore: remove leftover Vercel deploy config and references (#1588)](https://github.com/davila7/claude-code-templates/commit/12b74cb6c9d0854dbbe9e3b501fea1f29cedecab) | davila7 |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
