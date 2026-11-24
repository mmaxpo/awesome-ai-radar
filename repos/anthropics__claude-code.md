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
| ⭐ **Stars** | 156.9k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [16.1k](https://github.com/anthropics/claude-code/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | — |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-02-22 |
| 📦 **Latest release** | [v2.1.331](https://github.com/anthropics/claude-code/releases/tag/v2.1.331) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 37.0 MB |
| 🌐 **Website** | https://code.claude.com/docs/en/overview |

## 📦 Recent releases

### [v2.1.331](https://github.com/anthropics/claude-code/releases/tag/v2.1.331)
<sub>2026-11-23 · today</sub>

> **What's changed**
> - Added Code Mode support in terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS
> - Added `oidc.groups_jsonpath` to the Claude apps gateway, to read groups from the matching entries of a list of objects with a small subset of JSONPath (RFC 9535)
> - Added an API connectivity section to `claude doctor` that reports whether the API can be reached, with the HTTP status or the error, or says why it wasn't tested
> - Added a notice when tap-mode voice dictation stops by itself, after 15 seconds without recognized speech or at its 2-minute limit
> - Added `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` to ask for uncompressed model responses behind a proxy that cuts compressed ones off; not advised yet for self-hosted runners or Remote Control
> …

### [v2.1.330](https://github.com/anthropics/claude-code/releases/tag/v2.1.330)
<sub>2026-11-20 · 3d ago</sub>

> **What's changed**
> - Added sign-in to organizations managed in Anthropic's Enterprise Admin Console: after `claude auth login`, Claude Code applies the organization's settings and uses its cloud provider or gateway
> - Added easel, a built-in mod that draws charts when asked and under MCP metrics results, on Pro, Max and, where available, Team and Enterprise on macOS and Linux; turn automatic charts off in `/config`
> - Added `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` to print the full sign-in link, if the short one shows an error or a script reads values from it
> - Self-hosted runner: Added `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR` to have Claude start its work in a folder of a repository, while settings and hooks load as without it
> - Added a notice in cloud and self-hosted runner sessions when a plugin marketplace can't be fetched because its repository isn't one of the session's
> …

### [v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)
<sub>2026-11-19 · 4d ago</sub>

> **What's changed**
> - Added a trust dialog warning that says where a folder's hooks are declared
> - Added a warning in the conversation, in Claude Desktop and other non-interactive hosts, when hooks in managed settings fail to load
> - Added this session's scheduled tasks, `/loop` wakeups, the goal and this conversation's forks to `/tasks`; x stops one after asking
> - Added a "Server message" row to a server's page in `/mcp` that shows the JSON-RPC error message of a remote HTTP MCP server that refuses the connection
> - Added a "Marketplace auto-update" row to `/status` that names managed marketplaces that get no automatic updates, and why
> …

### [v2.1.328](https://github.com/anthropics/claude-code/releases/tag/v2.1.328)
<sub>2026-11-19 · 5d ago</sub>

> **What's changed**
> - Added auto mode for Claude Opus 4.6 and Sonnet 4.6 on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude apps gateway; interactive sessions with no permission mode start in it
> - Added `"onFailure": "block"` for `mcp_tool` hooks, as for command and HTTP hooks: a hook whose call fails blocks the action
> - Added a warning when a message from a session that skips permission prompts may be held and dropped by a cloud session
> - Added a notice in `/status` and `claude doctor` when an OpenTelemetry exporter has no endpoint and its data would likely be lost
> - Added `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`, which lets a host stop `claude -p --resume` and `--continue` from running a tool call that a hook deferred
> …

### [v2.1.327](https://github.com/anthropics/claude-code/releases/tag/v2.1.327)
<sub>2026-11-17 · 6d ago</sub>

> **What's changed**
> - Added a confirmation before `/install-github-app` changes a repository
> - Added `claude mcp add-json <name> -` to read the server's JSON from stdin, so tokens can stay off the command line; not available inside a Claude Code session
> - Added a line when a resumed session's earlier messages can't be loaded
> - Added a list in `/status` of broken agent, skill, command and output style files, keybinding errors, an unavailable sandbox, ignored permission settings and hook matchers that never match
> - Added a note in `/config` when other settings override a row
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/112541d8e85f32512d6169612ab4af30935d96b2) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/a66d0cfb4508af8e8a9e7d253636379c66e82640) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/2ff0c3cc93c7d062c27cffe228a8ab208b1770ab) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/7ee95ed94f73248f27ba609d0155d32411eab155) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/d9d9210b7f98b3bf29bac6faf0baf369f0aad672) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/35ff3df5ffc53bb35fd5f48e0da9788e2f858113) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/41be7734d0009c9af756bd3a7c1f52a0ccd0b3e9) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/a4cdd71b3df8927105db205f5b6ec7cdef8708b3) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/5d0d5aaa217b410a62062bc06c4dc78187ba6074) | actions-user |
| 2026-11-24 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/ea68ad63ec4abde18c4036b57a61cf3975c773bf) | actions-user |

[See all commits ↗](https://github.com/anthropics/claude-code/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anthropics/claude-code.git
```
