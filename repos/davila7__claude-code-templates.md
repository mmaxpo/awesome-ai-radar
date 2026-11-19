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
| 🐞 **Open issues + PRs** | [549](https://github.com/davila7/claude-code-templates/issues) |
| 💻 **Languages** | Python 40% · TypeScript 21% · HTML 12% · JavaScript 11% · TeX 7% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `anthropic` `anthropic-claude` `claude` `claude-code` `agent-skills` `ai-agents` `claude-code-plugins` `cli` `mcp` `registry` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 307.2 MB |
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
| 2026-11-19 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/619db084fd2e94742710f74680db4168ca2bd470) | github-actions[bot] |
| 2026-11-19 | [feat(dashboard): NVIDIA eye on the component page's scan card (#1622)](https://github.com/davila7/claude-code-templates/commit/ff2ca8a98b32ca9f56ee0e7d48e3dd4cd08937db) | davila7 |
| 2026-11-19 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/6f913a0cd61c244ef60480f085e2386cba4b5c46) | github-actions[bot] |
| 2026-11-19 | [fix(dashboard): keep the Files preview's expand bar under the preview…](https://github.com/davila7/claude-code-templates/commit/6c0bb15238cb5bfbf84ef27eb7e027720936e1e2) | davila7 |
| 2026-11-19 | [Scan excerpt fixes + Compatibility tab redesign (agent ring) (#1619)](https://github.com/davila7/claude-code-templates/commit/813a33607784f65cd3e14b15d226b729cdb493dc) | davila7 |
| 2026-11-19 | [feat(dashboard): scan report with a score ring, category bar and code…](https://github.com/davila7/claude-code-templates/commit/70d98086991273ea91a3af462502625344705a9a) | davila7 |
| 2026-11-18 | [feat(dashboard): NVIDIA eye on the scan reports, agent logos in Compa…](https://github.com/davila7/claude-code-templates/commit/7deaf763dc0c3e06fb500eeacf46f3bc121fb2df) | davila7 |
| 2026-11-18 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/21cc38c31641008077bef34338f612cee4f81c0a) | github-actions[bot] |
| 2026-11-18 | [Agent compatibility per skill (SkillEvaluator Harness Check) + fix $N…](https://github.com/davila7/claude-code-templates/commit/fdfbaf11c4c5fac39273824baa58c56b06155d28) | davila7 |
| 2026-11-18 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/d3a29567e1d4707db3377e5521a62f8ae5288aab) | github-actions[bot] |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
