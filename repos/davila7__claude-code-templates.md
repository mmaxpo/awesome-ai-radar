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
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-07-04 |
| 📦 **Latest release** | [v1.29.7](https://github.com/davila7/claude-code-templates/releases/tag/v1.29.7) — 2026-10-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 308.5 MB |
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
| 2026-11-26 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/24d9d16c0053791c2a02ad755d8c54272e893b27) | github-actions[bot] |
| 2026-11-26 | [Add SAP Learning AI certifications to /certifications (#1723)](https://github.com/davila7/claude-code-templates/commit/976138d4fbf2acbcc7290e5a0b5003990062134f) | davila7 |
| 2026-11-26 | [Add RoamSEO MCP to marketing (#1722)](https://github.com/davila7/claude-code-templates/commit/f4e1a69a88eef2497bef7bfcfa929495c9d506e1) | backslash112 |
| 2026-11-26 | [Add figmamcp skill (creative-design) (#1721)](https://github.com/davila7/claude-code-templates/commit/4b9c0d2c178f88a624552753f56676b0cab8ebb5) | MrCoder |
| 2026-11-26 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/ff316699a2c4e91624de01a6afe06d3c830d2bde) | github-actions[bot] |
| 2026-11-26 | [Add ChatAcademia MCP (academic research) (#1718)](https://github.com/davila7/claude-code-templates/commit/770b9ea83672bf58c58bd616ec9a9ed638b6741d) | khanhduyvt0101 |
| 2026-11-26 | [Add the Engineering Corpus MCP server (devtools) (#1714)](https://github.com/davila7/claude-code-templates/commit/2f0fe68705a57adb171389c785b58fef56fe0f93) | ymcbzrgn |
| 2026-11-26 | [chore: Update components and trending data](https://github.com/davila7/claude-code-templates/commit/2a104d81976267e26f31db66901b83f1c97a41df) | github-actions[bot] |
| 2026-11-26 | [chore: Update component content](https://github.com/davila7/claude-code-templates/commit/c959b4012b17d18765e2c18cd3b0128d7978b9bb) | github-actions[bot] |
| 2026-11-26 | [feat(hooks): add security/skill-shell-guard (PreSkillShellCommand) (#…](https://github.com/davila7/claude-code-templates/commit/cd14b29fd8b29308987ee3963c3c582a87b403e3) | davila7 |

[See all commits ↗](https://github.com/davila7/claude-code-templates/commits)

## ⬇️ Get it

```bash
git clone https://github.com/davila7/claude-code-templates.git
```
