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
| ⭐ **Stars** | 33.7k |
| 🍴 **Forks** | 4.0k |
| 🐞 **Open issues + PRs** | [520](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 40% · TypeScript 20% · HTML 11% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 302.0 MB |
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
<sub>2026-09-17 · 1mo ago</sub>

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
<sub>2025-11-15 · 12mo ago</sub>

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
| 2026-11-15 | [fix(component-page): stop showing a component's date (#1564)](https://github.com/davila7/claude-code-templates/commit/8c9a4a2c4a12a3010a0d26eddd3c40e7cef16af1) | davila7 |
| 2026-11-15 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/b49cdd91a196e36436517251d038bb1a63ac9dd4) | github-actions[bot] |
| 2026-11-15 | [dashboard: keep personal accounts out of Organization sameAs (#1563)](https://github.com/davila7/claude-code-templates/commit/217aea5fca9c6f665cb74a72487860ba0a1309d1) | davila7 |
| 2026-11-15 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/acc46db2dc32b83caf78365ca4c2062ce918e25f) | github-actions[bot] |
| 2026-11-15 | [Add code-mode setting (CLAUDE_CODE_EXPERIMENTAL_CODE_MODE) (#1562)](https://github.com/davila7/claude-code-templates/commit/c2208fd0fca11c53e665c2a8b4e72fb73732734e) | davila7 |
| 2026-11-14 | [dashboard: home title from counts.json, richer Organization sameAs (#…](https://github.com/davila7/claude-code-templates/commit/df0832f580ea4864a510eba4031e943d9fe1bab5) | davila7 |
| 2026-11-14 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/06e607224df7801b50327114852ad82d9967e0a5) | github-actions[bot] |
| 2026-11-13 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/9b6d5eb86b62f91ef6498227b127d091f2a3b712) | github-actions[bot] |
| 2026-11-13 | [settings: main-model and advisor settings for the latest Claude model…](https://github.com/davila7/claude-code-templates/commit/5072497d82c2a75514c6fb4b1ed2fc77fe77a852) | davila7 |
| 2026-11-13 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/44915c477f3d466401c09758f6ccad4a383a93ad) | github-actions[bot] |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
