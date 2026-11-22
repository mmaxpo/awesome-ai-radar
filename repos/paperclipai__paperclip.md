# paperclipai/paperclip

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/paperclipai/paperclip)

> The open-source app everyone uses to manage agents at work

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Framework for running an organization of agents |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 115.8k |
| 🍴 **Forks** | 19.2k |
| 🐞 **Open issues + PRs** | [7.0k](https://github.com/paperclipai/paperclip/issues) |
| 💻 **Languages** | TypeScript 93% · JavaScript 3% · Rust 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-orchestration` `agentic-ai` `ai-agents` `autonomous-agents` `claude-code` `codex` `mcp` `multi-agent` `openclaw` `workflow-automation` `acpx` `ai-engineering` `ai-governance` `ai-tools` `claude` `claude-skills` `hermes` `agent-skills` `llm` `project-management` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-03-02 |
| 📦 **Latest release** | [v2026.1117.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1117.0) — 2026-11-18 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 555.2 MB |
| 🌐 **Website** | https://paperclip.ing |

## 📦 Recent releases

### [v2026.1117.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1117.0)
<sub>2026-11-18 · 3d ago</sub>

> **Paperclip v2026.1117.0**
> > Released: 2026-11-17
> Paperclip v2026.1117.0 carries 1,586 commits, promoted from `2026.1110.0-beta.0`. The headline is a new default workspace: the Coordinator layout and Agent Chat are now standard, and task chat shows what a Runner agent actually did — its plan, inline diffs, tool calls, subagents, and a plan you can approve. Around that: agents that can set up connections within delegated authority, a full YAML editor for agent configuration, context-window and usage-limit readouts with a one-click Compact, proactive chat messages and automatic mid-turn steering for Codex and Pi, Codex image generation, and 1Password, Supabase, Vercel, and boxd in the catalog. Underneath, Runner runs continue through restarts, crashes, and container redeploys in far more cases, local Codex and OpenCode agents stay warm for much faster follow-ups, sandbox workspaces can survive a server replacement on S3-backed installs, the board keeps working through dropped connections, and run logs and skill packages move out of PostgreSQL into your configured storage.
> **Breaking Changes**
> - **The built-in Google Workspace connector is off by default.** While Paperclip's Google app verification is pending, the unified Google Workspace connection introduced in v2026.1106.0 is gated behind a new experimental setting: with it off, the connector is hidden from Apps and its setup, discovery, and tool execution are blocked — including connections saved on v2026.1106.0 — and the Composio and Arcade Google apps appear instead. To keep a Google Workspace connection working, turn on **Settings → Experimental → Google Workspace connector (Paperclip)** (`enableGoogleWorkspaceConnector`). ([#19247](https://github.com/paperclipai/paperclip/pull/19247))
> - **Every subtask gets its own execution workspace.** Child tasks no longer share the parent's checkout, branch, or unmerged changes, on every creation path (API, `create_task`, chat suggestions, plugins, and the New sub-task dialog); `inheritExecutionWorkspaceFromIssueId` now copies only the project and workspace strategy, and an ancestor's `executionWorkspaceId` passed on create is dropped. A child an older release bound to its parent's workspace moves to its own workspace on its next run. Work that relied on a child editing the parent's checkout must merge or push through Git; unrelated tasks can still share a workspace through an explicit `existing` selection. ([#19860](https://github.com/paperclipai/paperclip/pull/19860))
> …

### [v2026.1106.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0)
<sub>2026-11-06 · 15d ago</sub>

> **Paperclip v2026.1106.0**
> > Released: 2026-11-06
> Paperclip v2026.1106.0 carries 515 commits, promoted from `2026.1023.0-beta.0`. The headline is that the Paperclip Runner is now the default for new agents: new Claude, Codex, OpenCode, and Pi agents start on the native Runner on qualified macOS and Linux hosts, existing agents get a one-click "Upgrade runner" action, and GitHub Copilot joins as a native harness. Around that: project repositories that automatically become skill sources, model-backed prompt injection prevention, agent observability to Braintrust or any OTLP endpoint, a unified Google Workspace connection, bulk edits on the Agents roster, workspaces that compact and expire themselves with encrypted restore points, and Grok Bot and Muse as experimental Runner providers. Underneath, server restarts report ready sooner, the Docker image boots from a precompiled bundle, task pages load faster, and more background services stop polling the database.
> **Breaking Changes**
> - **The Pipelines experiment is removed.** Pipeline boards, stage settings, case automation, review queues, the `pipelines` CLI commands, the `pipelines:write` permission, the `enablePipelines` setting, and the `linkedCases` field on task detail are gone; Cases and Routines remain. Existing pipeline tables and records are preserved untouched and a stored `enablePipelines` value is ignored. ([#16834](https://github.com/paperclipai/paperclip/pull/16834))
> - **Run failures no longer reach Sentry by default.** A backend DSN alone no longer reports agent run failures. Set `PAPERCLIP_SENTRY_RUN_FAILURES=unexpected` to keep the previous filtered policy or `all` to report every failed or timed-out run; the default is `off`. ([#16300](https://github.com/paperclipai/paperclip/pull/16300))
> …

### [v2026.1012.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1012.0)
<sub>2026-10-12 · 1mo ago</sub>

> **Paperclip v2026.1012.0**
> > Released: 2026-10-12
> Paperclip v2026.1012.0 carries 130 commits, promoted from `2026.1006.0-beta.0`. The headline is that outside assistants can now join your team: Claude Code, Codex, OpenCode, and any MCP client can connect to Paperclip as a signed-in person, review work, and delegate tasks, all behind an experimental setting. Around that: Chat leads the navigation with each agent's tasks and artifacts beside the conversation, the Connections catalog pulls in accounts you already linked in Composio and Arcade, connections carry usage instructions that reach your agents automatically, Claude Sonnet 5.5 and GPT-6.1 Sol arrive with refreshed harnesses, and agents can safely update company skills. Underneath, Codex runs survive server restarts and model-capacity errors, workspace restore locks move to crash-safe SQLite file locks, and default agent instructions shrink to a fraction of their former size.
> **Breaking Changes**
> - **Workspace restore locks change protocol; stop every old process before upgrading.** Restore and agent-file collection locks are now OS-backed SQLite file locks under `<instance root>/locks/directory-merge/`, released by the kernel when a process crashes. Old and new versions must not write to the same instance root at once: drain and stop all old server and worker processes (including other hosts or containers) before upgrading or rolling back, then move any leftover legacy `<hash>.lock/` directories to a scratch location. Never delete or move the new `.lock.sqlite` files. See `doc/workspace-restore-locks.md`. ([#14869](https://github.com/paperclipai/paperclip/pull/14869))
> - **Stored tool grants are enforced as written.** A grant whose `scope.allow` list does not match a tool, connection, or application no longer falls through to a broader policy; grants with unknown selectors or malformed restrictions now deny access. Review custom grants after upgrading if an agent loses a tool it previously used. ([#14915](https://github.com/paperclipai/paperclip/pull/14915))
> …

### [v2026.1023.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1023.0)
<sub>2026-10-24 · 29d ago</sub>

> **Paperclip v2026.1023.0**
> > Released: 2026-10-23
> Paperclip v2026.1023.0 carries 200 commits, promoted from `2026.1012.1-beta.0`. The headline is private work: a task or project can now be marked private and shared with named people and agents; everyone else cannot open it, find it in task lists or search, read its run transcripts, or reach it through a plugin. Around that: agents can run through your own model gateway (OpenRouter, Amazon Bedrock, Google Gemini, or any OpenAI Responses, Anthropic Messages, or Chat Completions endpoint), Slack bots set themselves up through Slack's Manifest API, the GitHub review bot gets a two-screen setup and a real **Paperclip Review** status check, Costs becomes an exact ledger that also shows monthly subscription fees, and connected assistants can edit tasks, upload files, and configure agents over MCP. Underneath, OpenAI Dot and Pi 1.0 join the experimental Runner, native OpenCode streams as it types, each agent gets a persistent cryptographic identity, and idle instances stop polling the database every second.
> **Breaking Changes**
> - **Operators can now edit the company.** The Operator role preset grows from one grant (`tasks:assign`) to fourteen: agent creation and configuration, skills, environments, invitations, task assignment, pipelines, connections, tool management and use, and audit reads. Existing Operators pick up the missing grants through the normal startup seeding; custom grant scopes are kept. Join approval and member-permission management stay out of the preset, and inviting an Admin now requires join approval while inviting an Owner also requires member-permission management. Review your member roles if Operators were meant to be read-mostly. ([#15377](https://github.com/paperclipai/paperclip/pull/15377))
> - **GitHub review bots move behind their own experimental setting.** The **GitHub Code Review Bot** catalog entry, its setup, and its management screens appear only while **Settings → Experimental → GitHub review bots** (`enableGitHubReviewBots`, off by default) is on; existing bots keep running while it is off. The old setup-method and delegated-agent screens are gone, and per-person automatic-run flags are replaced by author include/exclude filters (legacy `people[].automaticReviews` values are read but ignored). ([#15416](https://github.com/paperclipai/paperclip/pull/15416))
> …

### [v2026.1005.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1005.0)
<sub>2026-10-06 · 1mo ago</sub>

> **Paperclip v2026.1005.0**
> > Released: 2026-10-05
> Paperclip v2026.1005.0 carries 179 commits, promoted from `2026.1002.0-beta.0`. The headline is agents that carry more with them: Grok Build runs on the native runner, agents keep their own files across tasks, company skills sync from GitHub repositories, and Browser Use Cloud gives agents a live browser that people can watch and take over from the task. Around those: most connectors now set up in one click with MCP aggregators on by default, Slack conversations round-trip between the board and the thread, Agent Chat gets its own navigation and hands finished work back to the conversation, and the task composer picks model and effort per message. Underneath, a long reliability pass hardens the native runner, sandbox transport, and the heartbeat scheduler, including a fix for a server crash loop caused by a permanently rejected queued run.
> **Breaking Changes**
> - **Operator UI snippet injection is removed.** The `PAPERCLIP_CLOUD_UI_SNIPPET` and `PAPERCLIP_CLOUD_UI_SNIPPET_B64` settings no longer inject HTML into static or development pages. Operators who relied on them should move the integration to a plugin UI contribution before upgrading. ([#13789](https://github.com/paperclipai/paperclip/pull/13789))
> - **Keyboard shortcuts are always on, and their settings are gone.** The instance-wide General toggle and the per-user Profile preference are both removed, along with the `GET`/`PATCH /api/auth/preferences` routes; `PATCH /api/instance/settings/general` no longer accepts `keyboardShortcuts`. Every signed-in user now has shortcuts enabled. ([#14141](https://github.com/paperclipai/paperclip/pull/14141), [#14643](https://github.com/paperclipai/paperclip/pull/14643))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [fix(identity): read a provisioned agent key without an exclusive agen…](https://github.com/paperclipai/paperclip/commit/7671e0cf0d718351f3b0c4d6a7d33df9867ffb8a) | devinfoley |
| 2026-11-22 | [fix(runner): support native OpenCode on macOS SSH hosts (#22534)](https://github.com/paperclipai/paperclip/commit/28ed2f1db0eec8750be6ecb20c74694cb584d8e0) | devinfoley |
| 2026-11-22 | [test(restart-chaos): drain a max-hours hosted run from the end of arr…](https://github.com/paperclipai/paperclip/commit/e5f0e1508bd4eb00142433452b1afa85ec4446f8) | cryppadotta |
| 2026-11-22 | [test(ui): wait for the settings notification before the company home …](https://github.com/paperclipai/paperclip/commit/324ec1f537a9ba1e84239faa81bcef326a5dd1b7) | cryppadotta |
| 2026-11-22 | [fix(recovery): report an unprepared saved skill on resume instead of …](https://github.com/paperclipai/paperclip/commit/7e30ba2c453b7de36c40c10b90ae67b0a47cf2bd) | paperclipbugbot |
| 2026-11-22 | [fix(heartbeat): deliver a saved answer on a reviewed task with open b…](https://github.com/paperclipai/paperclip/commit/4ec1447a671774b3c921ffd4ae4bbe383fbbff9b) | paperclipbugbot |
| 2026-11-22 | [test(server): advance the maintenance fake clock only after database …](https://github.com/paperclipai/paperclip/commit/7a4a5bba8a0b2c82336f41e158d3fe676d16eba2) | cryppadotta |
| 2026-11-22 | [fix(chat): continue a Slack question that a person answered in Paperc…](https://github.com/paperclipai/paperclip/commit/782bd8d8ebc522a955c8c1f27be68b23ad4e6a96) | paperclipbugbot |
| 2026-11-22 | [fix(server): validate agentId query parameter on company activity end…](https://github.com/paperclipai/paperclip/commit/ac02de7732e8aad2d44304792db8cec4a5a0ebc0) | sentry[bot] |
| 2026-11-22 | [test(runner): wait for the background task notification turn before t…](https://github.com/paperclipai/paperclip/commit/28c11084ad86fdd8c5e17201b459b0f7df919e7b) | cryppadotta |

[See all commits ↗](https://github.com/paperclipai/paperclip/commits)

## ⬇️ Get it

```bash
git clone https://github.com/paperclipai/paperclip.git
```
