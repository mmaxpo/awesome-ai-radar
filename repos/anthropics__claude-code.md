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
| ⭐ **Stars** | 157.0k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [16.2k](https://github.com/anthropics/claude-code/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | — |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-02-22 |
| 📦 **Latest release** | [v2.1.332](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 37.5 MB |
| 🌐 **Website** | https://code.claude.com/docs/en/overview |

## 📦 Recent releases

### [v2.1.332](https://github.com/anthropics/claude-code/releases/tag/v2.1.332)
<sub>2026-11-25 · today</sub>

> **What's changed**
> - Added skills from MCP servers (beta). They show as `server:skill` in the `/` menu; other skills keep their names
> - Added a `PreSkillShellCommand` hook event that can refuse a skill or command's inline shell commands as it loads; on 2.1.331 and older, a settings file naming it opens a dialog at start
> - Added "Always deliver" to the prompt for held messages from other sessions
> - Added a footer line that stays while a flagged message has your session on a different model, until you pick one with `/model`
> - Added an OpenTelemetry `assistant_response` event for text Claude sends through SendUserMessage or Cowork's message tool, when response logging is on
> …

### [v2.1.331](https://github.com/anthropics/claude-code/releases/tag/v2.1.331)
<sub>2026-11-23 · yesterday</sub>

> **What's changed**
> - Added Code Mode support in terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS
> - Added `oidc.groups_jsonpath` to the Claude apps gateway, to read groups from the matching entries of a list of objects with a small subset of JSONPath (RFC 9535)
> - Added an API connectivity section to `claude doctor` that reports whether the API can be reached, with the HTTP status or the error, or says why it wasn't tested
> - Added a notice when tap-mode voice dictation stops by itself, after 15 seconds without recognized speech or at its 2-minute limit
> - Added `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` to ask for uncompressed model responses behind a proxy that cuts compressed ones off; not advised yet for self-hosted runners or Remote Control
> …

### [v2.1.330](https://github.com/anthropics/claude-code/releases/tag/v2.1.330)
<sub>2026-11-20 · 4d ago</sub>

> **What's changed**
> - Added sign-in to organizations managed in Anthropic's Enterprise Admin Console: after `claude auth login`, Claude Code applies the organization's settings and uses its cloud provider or gateway
> - Added easel, a built-in mod that draws charts when asked and under MCP metrics results, on Pro, Max and, where available, Team and Enterprise on macOS and Linux; turn automatic charts off in `/config`
> - Added `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` to print the full sign-in link, if the short one shows an error or a script reads values from it
> - Self-hosted runner: Added `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR` to have Claude start its work in a folder of a repository, while settings and hooks load as without it
> - Added a notice in cloud and self-hosted runner sessions when a plugin marketplace can't be fetched because its repository isn't one of the session's
> …

### [v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)
<sub>2026-11-19 · 5d ago</sub>

> **What's changed**
> - Added a trust dialog warning that says where a folder's hooks are declared
> - Added a warning in the conversation, in Claude Desktop and other non-interactive hosts, when hooks in managed settings fail to load
> - Added this session's scheduled tasks, `/loop` wakeups, the goal and this conversation's forks to `/tasks`; x stops one after asking
> - Added a "Server message" row to a server's page in `/mcp` that shows the JSON-RPC error message of a remote HTTP MCP server that refuses the connection
> - Added a "Marketplace auto-update" row to `/status` that names managed marketplaces that get no automatic updates, and why
> …

### [v2.1.328](https://github.com/anthropics/claude-code/releases/tag/v2.1.328)
<sub>2026-11-19 · 6d ago</sub>

> **What's changed**
> - Added auto mode for Claude Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude apps gateway; interactive sessions with no permission mode start in it
> - Added `"onFailure": "block"` for `mcp_tool` hooks, as for command and HTTP hooks: a hook whose call fails blocks the action
> - Added a warning when a message from a session that skips permission prompts may be held and dropped by a cloud session
> - Added a notice in `/status` and `claude doctor` when an OpenTelemetry exporter has no endpoint and its data would likely be lost
> - Added `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`, which lets a host stop `claude -p --resume` and `--continue` from running a tool call that a hook deferred
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/4cc5e8b63a5cc6fcddd1bf7fed04ebd712d0c91a) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/7e8faf5f2fa5865a92b039d1e7a93022d8629f9a) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/ab54ad2f7ef0c20b7011ae6d88c9e17213ed3273) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/676706c4f370471a224097880ba80fd457e09bd9) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/d66368052c9303ce022c017a5b59d62ebd57d1e7) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/7ae5de41a7fee96788fcf98fc7b218f4177611d8) | actions-user |
| 2026-11-25 | [chore: Update CHANGELOG.md and feed.xml](https://github.com/anthropics/claude-code/commit/eb8e6d253d0dbee6e52fb0d5fdcb72c9396fe3e8) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/772d3a40ac44f5ec0c816eb913edeea5bde2d320) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/fa0dece70669a54b3104c618de9eebaaa78af19f) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/1f1cad0c697ea1e82c0eefbb5119694c418d14bc) | actions-user |

[See all commits ↗](https://github.com/anthropics/claude-code/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anthropics/claude-code.git
```
