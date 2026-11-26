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
| ⭐ **Stars** | 157.2k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [16.4k](https://github.com/anthropics/claude-code/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | — |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-02-22 |
| 📦 **Latest release** | [v2.1.332](https://github.com/anthropics/claude-code/releases/tag/v2.1.332) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 36.7 MB |
| 🌐 **Website** | https://code.claude.com/docs/en/overview |

## 📦 Recent releases

### [v2.1.332](https://github.com/anthropics/claude-code/releases/tag/v2.1.332)
<sub>2026-11-25 · yesterday</sub>

> **What's changed**
> - Added skills from MCP servers (beta). They show as `server:skill` in the `/` menu; other skills keep their names
> - Added a `PreSkillShellCommand` hook event that can refuse a skill or command's inline shell commands as it loads; on 2.1.331 and older, a settings file naming it opens a dialog at start
> - Added "Always deliver" to the prompt for held messages from other sessions
> - Added a footer line that stays while a flagged message has your session on a different model, until you pick one with `/model`
> - Added an OpenTelemetry `assistant_response` event for text Claude sends through SendUserMessage or Cowork's message tool, when response logging is on
> …

### [v2.1.331](https://github.com/anthropics/claude-code/releases/tag/v2.1.331)
<sub>2026-11-23 · 2d ago</sub>

> **What's changed**
> - Added Code Mode support in terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS
> - Added `oidc.groups_jsonpath` to the Claude apps gateway, to read groups from the matching entries of a list of objects with a small subset of JSONPath (RFC 9535)
> - Added an API connectivity section to `claude doctor` that reports whether the API can be reached, with the HTTP status or the error, or says why it wasn't tested
> - Added a notice when tap-mode voice dictation stops by itself, after 15 seconds without recognized speech or at its 2-minute limit
> - Added `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` to ask for uncompressed model responses behind a proxy that cuts compressed ones off; not advised yet for self-hosted runners or Remote Control
> …

### [v2.1.330](https://github.com/anthropics/claude-code/releases/tag/v2.1.330)
<sub>2026-11-20 · 5d ago</sub>

> **What's changed**
> - Added sign-in to organizations managed in Anthropic's Enterprise Admin Console: after `claude auth login`, Claude Code applies the organization's settings and uses its cloud provider or gateway
> - Added easel, a built-in mod that draws charts when asked and under MCP metrics results, on Pro, Max and, where available, Team and Enterprise on macOS and Linux; turn automatic charts off in `/config`
> - Added `CLAUDE_CODE_FULL_SIGN_IN_LINK=1` to print the full sign-in link, if the short one shows an error or a script reads values from it
> - Self-hosted runner: Added `--start-dir` / `SELF_HOSTED_RUNNER_START_DIR` to have Claude start its work in a folder of a repository, while settings and hooks load as without it
> - Added a notice in cloud and self-hosted runner sessions when a plugin marketplace can't be fetched because its repository isn't one of the session's
> …

### [v2.1.329](https://github.com/anthropics/claude-code/releases/tag/v2.1.329)
<sub>2026-11-19 · 6d ago</sub>

> **What's changed**
> - Added a trust dialog warning that says where a folder's hooks are declared
> - Added a warning in the conversation, in Claude Desktop and other non-interactive hosts, when hooks in managed settings fail to load
> - Added this session's scheduled tasks, `/loop` wakeups, the goal and this conversation's forks to `/tasks`; x stops one after asking
> - Added a "Server message" row to a server's page in `/mcp` that shows the JSON-RPC error message of a remote HTTP MCP server that refuses the connection
> - Added a "Marketplace auto-update" row to `/status` that names managed marketplaces that get no automatic updates, and why
> …

### [v2.1.328](https://github.com/anthropics/claude-code/releases/tag/v2.1.328)
<sub>2026-11-19 · 7d ago</sub>

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
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/a3b7a20a282a7b75ed68c2f8a0d0ecc822171c3e) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/21f7e022adaaced2466519d76493f9f60fc1dd7f) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/9587741f62205d168459b1be9441fdb901a1b482) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/52b72f60f0fe95fb74916bde3de346d21dd49ff6) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/4b3e1552c570b952533d9cada2542a916bb60e3c) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/86fe5a152665324425225fe828edc7a30ecfebf2) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/a5e837526c8c37419cc6d9546fa4fa75b38f6118) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/f2db19637d4e7bbfb5bb322a92e84a878491505e) | actions-user |
| 2026-11-26 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/0fbd76b61c44029ced3ba8d0c8feab10fb8994f0) | actions-user |
| 2026-11-25 | [chore: Update mods/](https://github.com/anthropics/claude-code/commit/9c18e4ee9f67325e6aa47837784664e4ca5c992d) | actions-user |

[See all commits ↗](https://github.com/anthropics/claude-code/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anthropics/claude-code.git
```
