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
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 311.8 MB |
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
| 2026-11-24 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/03c316de3528b639d37c426314cf5b91b4e65e01) | github-actions[bot] |
| 2026-11-24 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/69203204b371fa3eccb77534f15c5df45a64a0a1) | github-actions[bot] |
| 2026-11-24 | [feat(skills): platform-oauth-linked-billing, set up Claude Platform O…](https://github.com/davila7/claude-code-templates/commit/df647f1b358e0b0aa5fc1b830d0814e1f8afbfbd) | davila7 |
| 2026-11-24 | [blog: add Automated Testing Workflow article (agent + command + hook)…](https://github.com/davila7/claude-code-templates/commit/279d494c9b4f1225f23679eafaedf83c333fa3b6) | davila7 |
| 2026-11-24 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/9de37d0750e82117b3ad20145cf6bc9c433a299f) | github-actions[bot] |
| 2026-11-24 | [Add release-manager agent (development-team) (#1675)](https://github.com/davila7/claude-code-templates/commit/0652b7c2d5825f214cac22cc269f5d5f9ee2a95f) | badhope |
| 2026-11-23 | [feat(dashboard): "Build my stack with Claude" page behind a flag (#1683)](https://github.com/davila7/claude-code-templates/commit/b3ef82024a085acfc214f6ad76a41ceb308c4d35) | davila7 |
| 2026-11-23 | [chore: Update star history chart](https://github.com/davila7/claude-code-templates/commit/c1bc5c1df4ff0bffb9a04d8f7790543681232423) | github-actions[bot] |
| 2026-11-23 | [fix(dashboard): align every icon in the collapsed sidebar (#1672)](https://github.com/davila7/claude-code-templates/commit/5e3c55d706f3b8c0e4eedee49a25cb8d2ef0e819) | davila7 |
| 2026-11-23 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/8929f198edc03efe3e135f1610b59dd4d29d8b0b) | github-actions[bot] |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
