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
| ⭐ **Stars** | 33.8k |
| 🍴 **Forks** | 4.0k |
| 🐞 **Open issues + PRs** | [520](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 40% · TypeScript 20% · HTML 11% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 304.0 MB |
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
| 2026-11-16 | [chore: Update star history chart](https://github.com/davila7/claude-code-templates/commit/1530598131e773d2dc1bdefa7d28df64a7d6b656) | github-actions[bot] |
| 2026-11-16 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/7242320fee0ac821944bced293b280092d1750b4) | github-actions[bot] |
| 2026-11-15 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/43b1714a48c7169e861ebba129152ba85fb391f9) | github-actions[bot] |
| 2026-11-15 | [Add Google Stitch skills as three catalog plugins (design) (#1575)](https://github.com/davila7/claude-code-templates/commit/660222a0cfd0cc6350711e307eeaad1fd2127c28) | davila7 |
| 2026-11-15 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/c3addd2be27682e7d3f752aa9505426ed4551d8a) | github-actions[bot] |
| 2026-11-15 | [Ship the upstream LICENSE/NOTICE with external skills (#1577)](https://github.com/davila7/claude-code-templates/commit/11945a85c88970ffd85c58ff5487bf776596bd64) | davila7 |
| 2026-11-15 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/c13689d67d54b33e556b9cd78949767cc8c0c58b) | github-actions[bot] |
| 2026-11-15 | [Keep the catalog building when an external skill's repo is unreachabl…](https://github.com/davila7/claude-code-templates/commit/c935ccbc3e540a00ab1e532aba7270e93ceaf94e) | davila7 |
| 2026-11-15 | [Add Neon postgres-best-practices as an external skill (database) (#1570)](https://github.com/davila7/claude-code-templates/commit/132e9d387e0357f0e9633944bf4e419501b82539) | davila7 |
| 2026-11-15 | [Add cover-letter-lint skill (career) as an external skill (#1460)](https://github.com/davila7/claude-code-templates/commit/22dd06e16a3ced89e66fb1de7c3f20b2265829eb) | atokim4 |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
