# anthropics/claude-code

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/anthropics/claude-code)

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Anthropic's official agentic coding tool for the terminal |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 156.6k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [16.0k](https://github.com/anthropics/claude-code/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | — |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2025-02-22 |
| 📦 **Latest release** | [v2.1.330](https://github.com/anthropics/claude-code/releases/tag/v2.1.330) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 36.3 MB |
| 🌐 **Website** | https://code.claude.com/docs/en/overview |

## 📦 Recent releases

### [v2.1.330](https://github.com/anthropics/claude-code/releases/tag/v2.1.330)
<sub>2026-11-20 · yesterday</sub>

> **What's changed**
> - Added sign-in to organizations managed in Anthropic's Enterprise Admin Console: after `claude auth login`, Claude Code applies the organization's settings and uses its cloud provider or gateway
> - Added easel, a built-in mod that draws charts when asked and under MCP metrics results, on Pro, Max and, where available, Team and Enterprise on macOS and Linux; turn automatic charts off in `/config`
> - Added `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` to print the full sign-in link, if the short one shows an error or a script reads values from it
> - Self-hosted runner: Added `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR` to have Claude start its work in a folder of a repository, while settings and hooks load as without it
> - Added a notice in cloud and self-hosted runner sessions when a plugin marketplace can't be fetched because its repository isn't one of the session's
> …

### [v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)
<sub>2026-11-19 · 2d ago</sub>

> **What's changed**
> - Added a trust dialog warning that says where a folder's hooks are declared
> - Added a warning in the conversation, in Claude Desktop and other non-interactive hosts, when hooks in managed settings fail to load
> - Added this session's scheduled tasks, `/loop` wakeups, the goal and this conversation's forks to `/tasks`; x stops one after asking
> - Added a "Server message" row to a server's page in `/mcp` that shows the JSON-RPC error message of a remote HTTP MCP server that refuses the connection
> - Added a "Marketplace auto-update" row to `/status` that names managed marketplaces that get no automatic updates, and why
> …

### [v2.1.328](https://github.com/anthropics/claude-code/releases/tag/v2.1.328)
<sub>2026-11-19 · 3d ago</sub>

> **What's changed**
> - Added auto mode for Claude Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude apps gateway; interactive sessions with no permission mode start in it
> - Added `"onFailure": "block"` for `mcp_tool` hooks, as for command and HTTP hooks: a hook whose call fails blocks the action
> - Added a warning when a message from a session that skips permission prompts may be held and dropped by a cloud session
> - Added a notice in `/status` and `claude doctor` when an OpenTelemetry exporter has no endpoint and its data would likely be lost
> - Added `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`, which lets a host stop `claude -p --resume` and `--continue` from running a tool call that a hook deferred
> …

### [v2.1.327](https://github.com/anthropics/claude-code/releases/tag/v2.1.327)
<sub>2026-11-17 · 4d ago</sub>

> **What's changed**
> - Added a confirmation before `/install-github-app` changes a repository
> - Added `claude mcp add-json <name> -` to read the server's JSON from stdin, so tokens can stay off the command line; not available inside a Claude Code session
> - Added a line when a resumed session's earlier messages can't be loaded
> - Added a list in `/status` of broken agent, skill, command and output style files, keybinding errors, an unavailable sandbox, ignored permission settings and hook matchers that never match
> - Added a note in `/config` when other settings override a row
> …

### [v2.1.326](https://github.com/anthropics/claude-code/releases/tag/v2.1.326)
<sub>2026-11-16 · 5d ago</sub>

> **What's changed**
> - Added support for turning on Code Mode while agent teams are enabled; if you already turned it on, sessions with teams on now start in Code Mode
> - Added a startup warning when an `--allowedTools`, `--disallowedTools` or `--tools` value has an entry that doesn't look like a complete rule
> - Added a message explaining why MCP servers stop loading when an administrator adds `managed-mcp.json` during a session
> - Added a row to `/status` that says when your provider or an environment variable such as `DISABLE_TELEMETRY` turns features off
> - Added a note in `/plugin` and `claude plugin list` when a malformed `plugin.json` field such as `author` or `homepage` is ignored
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/1006c2e4f783f016963fb290d3eb4afaa2d448b1) | actions-user |
| 2026-11-22 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/8af3c14e96cb69179726700cc24c2ace4b13cdb4) | actions-user |
| 2026-11-22 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/4d28f76521def29be66a9a233957924bab6e065a) | actions-user |
| 2026-11-22 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/6591fdae228a1a53407720c36c0ba630a83730cf) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/b022ba6df88a5ddfbcedc39739a191c7e2ff5196) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/6935d6e1ec69321aace1be56c73c876bade33e6b) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/d24156684a9ecfedfde133e2b92b7189d2710d9c) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/ed5b3a829c99d5ea34bc0b373e02c586d85cedc6) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/e1cd3c1ba8e992c43e8317760096338596105a4d) | actions-user |
| 2026-11-21 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/928ac132a30dbe1ccf1f800cc93c4e8a65e4c449) | actions-user |

[See all commits ↗](https://github.com/anthropics/claude-code/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anthropics/claude-code.git
```
