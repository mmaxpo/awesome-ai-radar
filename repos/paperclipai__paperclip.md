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
| ⭐ **Stars** | 114.0k |
| 🍴 **Forks** | 18.9k |
| 🐞 **Open issues + PRs** | [6.7k](https://github.com/paperclipai/paperclip/issues) |
| 💻 **Languages** | TypeScript 93% · JavaScript 3% · Rust 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-orchestration` `agentic-ai` `ai-agents` `autonomous-agents` `claude-code` `codex` `mcp` `multi-agent` `openclaw` `workflow-automation` `acpx` `ai-engineering` `ai-governance` `ai-tools` `claude` `claude-skills` `hermes` `agent-skills` `llm` `project-management` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-03-02 |
| 📦 **Latest release** | [v2026.1106.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0) — 2026-11-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 539.5 MB |
| 🌐 **Website** | https://paperclip.ing |

## 📦 Recent releases

### [v2026.1106.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0)
<sub>2026-11-06 · 8d ago</sub>

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
<sub>2026-10-24 · 22d ago</sub>

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

### [v2026.1001.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1001.0)
<sub>2026-10-02 · 1mo ago</sub>

> **Paperclip v2026.1001.0**
> > Released: 2026-10-01
> Paperclip v2026.1001.0 carries 77 commits, promoted from `2026.921.0-beta.1`. The headline is reliability: a deep hardening pass over the native runner and chat recovery — approval and Stop races, session continuity, sandbox reconnection and cleanup — alongside a friendlier face: agent personas throughout the app, an animated onboarding character, and a rebuilt Slack setup. Around those: agents can review GitHub pull requests as scheduled review bots, Railway joins the connector catalog with governed deployment tools, approvals and answers queue during active runs instead of bouncing, and execution harnesses now default to full auto.
> **Breaking Changes**
> - **The legacy Composio broker is retired.** The API-key catalog method, broker clients, session creation, account synchronization, child lifecycle and toolkit routes, and the Services tab are all removed. Existing legacy Composio connections stop working, and there is no automated migration — the experimental MCP aggregator connectors (below) are the successor path; see the Upgrade Guide for the manual steps. Vercel provenance is untouched. ([#13758](https://github.com/paperclipai/paperclip/pull/13758))
> - **Execution harnesses now default to full auto.** Native runs default Claude/ACPX to `approve-all`, OpenCode to `allow`, and Codex to approval-and-sandbox bypass, and the legacy adapters follow the same policy — provider tools and connected tools included. Explicitly configured restrictive modes are preserved, and Paperclip's own approval decisions still enforce controller authority; only the *defaults* change. Operators who relied on unconfigured agents inheriting restrictive provider gates should set an explicit mode. ([#13686](https://github.com/paperclipai/paperclip/pull/13686), [#13693](https://github.com/paperclipai/paperclip/pull/13693))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [perf(release): stage the verified host release daemon instead of comp…](https://github.com/paperclipai/paperclip/commit/e7f31705dad6dfdfd0f0f3f9e017ed2e0afc584b) | cryppadotta |
| 2026-11-15 | [docs(skills): add aggregate-bound, lost-runner, and bug-class lessons…](https://github.com/paperclipai/paperclip/commit/8cd2d6a73d2097253dd329f55b637e12b20361c6) | cryppadotta |
| 2026-11-15 | [fix(comments): keep saved authorization cards from blocking replies (…](https://github.com/paperclipai/paperclip/commit/c17ef9249ddf4e30e0031cfca7f625c3f0723695) | cryppadotta |
| 2026-11-15 | [fix(server): wake a delivery task unscoped when it cannot apply settl…](https://github.com/paperclipai/paperclip/commit/689d62661d6d1fbf6ae6a4e20e5124888fa12dc0) | cryppadotta |
| 2026-11-15 | [refactor: split the runner-e2e and restart-chaos READMEs into a runbo…](https://github.com/paperclipai/paperclip/commit/fb3b09aaef535755040166d8c57abe023ca8063e) | cryppadotta |
| 2026-11-15 | [perf(release): build canary daemons during source verification and ke…](https://github.com/paperclipai/paperclip/commit/066c8244b5efba84335f400f2f191cc5a6850560) | cryppadotta |
| 2026-11-15 | [perf(recovery): re-check only changed tasks between hourly full backs…](https://github.com/paperclipai/paperclip/commit/83541e89ad3b90740ffc61a32c396dddb5834526) | cryppadotta |
| 2026-11-15 | [perf(db): carry scope hints in cross-process work notifications (#21681)](https://github.com/paperclipai/paperclip/commit/07d5a6ee17653b6df40904d4cc63ec2b6e3e9ca2) | cryppadotta |
| 2026-11-15 | [fix(evals): repair four cohort-15 chat cases and prefix board links i…](https://github.com/paperclipai/paperclip/commit/819f61f1fd358874568b02f1b9462529e9ad1899) | cryppadotta |
| 2026-11-15 | [fix(recovery): continue a task on its own when its saved files are pe…](https://github.com/paperclipai/paperclip/commit/ca23330c69b1f2b25bdadfcbda68317db97deaef) | cryppadotta |

[See all commits ↗](https://github.com/paperclipai/paperclip/commits)

## ⬇️ Get it

```bash
git clone https://github.com/paperclipai/paperclip.git
```
