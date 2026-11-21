# agno-agi/agno

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/agno-agi/agno)

> The self-managing agent platform

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Fast framework for agents with memory, tools and teams |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 43.3k |
| 🍴 **Forks** | 6.3k |
| 🐞 **Open issues + PRs** | [1.9k](https://github.com/agno-agi/agno/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `developer-tools` `python` `agents` `ai` `ai-agents` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2022-05-04 |
| 📦 **Latest release** | [v3.2.1](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 330.0 MB |
| 🌐 **Website** | https://docs.agno.com |

## 📦 Recent releases

### [v3.2.1](https://github.com/agno-agi/agno/releases/tag/v3.2.1)
<sub>2026-11-17 · 3d ago</sub>

> **Changelog**
> **New Features:**
> - **Session Compactions**: `GET /sessions/{session_id}/compactions` lists a session's compactions on `SqliteDb` and `PostgresDb`, newest first, with how many messages each replaced and the token count before and after.
> - **Company Files**: A Task's files and the shared notes can now be read over the API with `GET /company/tasks/{task_id}/files` and `GET /company/notes`, each with a `/{path}` route to read one file. See [cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/05_agent_os/30_company/16_company_file_tree.py).
> **Improvements:**
> - **LinearTools, DiscordTools and ModelsLabTools**: Now take a `timeout` (default 30 seconds, 120 for ModelsLab) that applies to every request.
> …

### [v3.2.0](https://github.com/agno-agi/agno/releases/tag/v3.2.0)
<sub>2026-11-12 · 8d ago</sub>

> **Summary**
> Agno v3.2 makes Super Agent faster and more capable with direct tools, expands Company task governance and coordination, introduces database-backed AgentOS homepage metrics, upgrades A2A to the v1.0 protocol, updates the Slack interface to use the Bolt SDK and makes external agents first-class stored components.
> **Changelog**
> **Breaking changes**
> - **OS Manager defaults and validation:** `OSManager.tool_call_limit` now defaults to 24 (was 8), and `num_history_runs` defaults to 5 (was 7). AgentOS refuses startup when `OSManager(root=...)` is combined with custom tools named `read_file`, `list_files`, or `search_content`.
> - **A2A v1.0:** AgentOS and `A2AClient` now run on the official `a2a-sdk` 1.x, so upgrade the Agno server and client together. ([#10956](https://github.com/agno-agi/agno/pull/10956))
> …

### [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12)
<sub>2026-10-29 · 22d ago</sub>

> **Changelog**
> **New Features:**
> - **Native Approvals for Harness Agents**: Claude's and Codex's own permission requests now reach the AgentOS approval UI. When the agent has a database, including one AgentOS supplies, a native request persists a PAUSED run that shows up in the existing chat and Approvals views, and Resolve plus Continue Run delivers the decision back to the same native execution without replaying the prompt. The harness's own policy decides when to ask — Claude keeps its `permission_mode` and explicit permission callbacks, Codex supports `approval_policy="on-request" | "untrusted" | "never"` alongside its existing SDK `auto_review` and `deny_all` modes — so there is no separate Agno setting to turn on. Decisions are validated against the exact action requested, with sync and async continuation, cancellation, expiry and storage-failure handling, and sandboxed agents keep this across Docker and AgentCore: capability negotiation, a decision RPC, fenced persistence, reattachment after an API-worker loss, separate approval-wait and execution budgets, and no replay after process loss. Note that a `CodexAgent` with no approval settings now runs under the native `on-request` policy, so a request that previously went nowhere pauses the run instead; `hitl_timeout` (default 900s) bounds how long it waits. See `cookbook/frameworks/human_in_the_loop/`.
> - **Initially Disabled Company Routines**: `Routine(enabled=False)` lets a template ship an inactive Routine that a user turns on later from the UI, with `True` still the default. Disabled Routines are created atomically, stay linked to their Product and visible in listings, are skipped by the scheduler, and keep the user's saved choice across restarts. The flag is honored in Python and YAML bootstrap, the setup and creation APIs, the sync and async Company Manager, and the Company tools. Duplicate create requests still return `409` and cannot enable an existing Routine, and the existing pause/resume endpoints enable it without recreating it. See `cookbook/05_agent_os/30_company/11_disabled_routine.py`.
> - **Headline Numbers on Charts**: `ChartTools.create_chart()` takes an optional preformatted `value` — a total or latest value such as `"$22.3K"` or `"94%"` — emitted as `"value"` in the chart block and rendered by Agno OS beside the chart title. The docstring tells the model to leave it out when no single number summarizes the chart, so averages and rates are not summed.
> **Improvements:**
> …

### [v3.1.11](https://github.com/agno-agi/agno/releases/tag/v3.1.11)
<sub>2026-10-27 · 24d ago</sub>

> **Changelog**
> **New Features:**
> - **Harness Agents in Teams and Workflows**: `ClaudeAgent` and `CodexAgent` can now be members of an Agno `Team` and steps of a `Workflow`, including inside `Parallel`, `Loop`, `Condition` and `Router`. The team leader delegates to them with `delegate_task_to_member` like any other member, each harness runs with its own model, tools and workspace, keeps its own conversation across turns of the same session, and the team or workflow collects its runs as usual. A harness agent with `sandbox=` runs each turn in its own container as a member or step, and AgentOS lists harness members on the team page. See `cookbook/frameworks/harness_teams/` and `cookbook/frameworks/harness_workflows/`.
> - **Session Search**: Added `GET /sessions/filter-schema` and `POST /sessions/search` with nested AND/OR/NOT filters on session name, session/user/component IDs, session type and created/updated timestamps, matching the Traces API. Predicates are applied before counting and pagination in PostgreSQL and SQLite, with a batched fallback for other adapters. Sync and async client methods are included.
> - **Company Tasks**: `POST /company/tasks` accepts `status`, so Tasks can be created in Backlog, Ready or Cancelled. Tasks can move between any stages, Done and Cancelled Tasks can reopen, and title and brief can be edited at any stage. In progress still starts only with a run, and moving out of it while that run is executing or paused is refused.
> - **Company Routines**: Added `POST /company/routines/{id}/cancel`, `/archive`, `/restore` and admin-only `DELETE /company/routines/{id}`. `GET /company/routines` takes `sort_by` and `sort_order`. Pause and resume on an on-demand Routine return `409`, and scheduler runs no longer move `updated_at`.
> …

### [v3.1.10](https://github.com/agno-agi/agno/releases/tag/v3.1.10)
<sub>2026-10-23 · 29d ago</sub>

> **Changelog**
> **Bug Fixes:**
> - **CodexAgent**: Now signs in automatically with `OPENAI_API_KEY`, and keeps an existing ChatGPT or other login.
> - **OS Manager**: OS Manager now lists and runs external agents such as `ClaudeAgent` and `CodexAgent` registered in `AgentOS(agents=[...])`, by name or ID.
> - **Knowledge Upload**: `POST /knowledge/content` now returns a clear `400` message when an upload has no file, `text_content` or URL, or when `url` is not a single URL.
> - **Tracing**: Spans from `AgentOS(tracing=True)` and `setup_tracing()` now keep up to 1,024 attributes, so model spans keep their full input and message history on runs with many tool calls. `OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT` and `OTEL_ATTRIBUTE_COUNT_LIMIT` still take precedence.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [[cookbook] Add GetYouTubeTranscript hosted MCP example (#11785)](https://github.com/agno-agi/agno/commit/e59ca576219e589136e53b6cff8d6677899cf95f) | pushkarsingh32 |
| 2026-11-20 | [fix: workflow preserve falsy step content (0, False, []) in CEL conte…](https://github.com/agno-agi/agno/commit/cafe0b49457cc1859ab2401888fc3b2538443d7a) | TINGyu123644 |
| 2026-11-20 | [fix: workflow preserve falsy previous_step_content in StepInput.to_di…](https://github.com/agno-agi/agno/commit/d122d129c4abb00647139cfea40f0cdcf4eda861) | lkuko |
| 2026-11-19 | [[feat] Send an Agno User-Agent from the Sarvam provider (#11748)](https://github.com/agno-agi/agno/commit/b3b8b6832bf5a4a6c9ec5be5d3deae7290e44cbd) | vikashmaddi-sarvam |
| 2026-11-19 | [[fix] Surface Neo4jTools errors instead of returning [] (#11724)](https://github.com/agno-agi/agno/commit/365c9c7e74719c1d20b557178add8c65f27a4426) | LangerSword |
| 2026-11-18 | [[feat] Add Sarvam AI as a model provider (#11735)](https://github.com/agno-agi/agno/commit/821be55d1ec3bb472abe8bd94c3b2a0d6c78392f) | vikashmaddi-sarvam |
| 2026-11-18 | [fix: reject page 0 on session, memory, eval and knowledge list routes…](https://github.com/agno-agi/agno/commit/ea74915eb0b9ea8039704e6b39947804297caa96) | harshsinha03 |
| 2026-11-18 | [feat: inline JSON Schema output_schema in StudioTools (#11220)](https://github.com/agno-agi/agno/commit/59ca87f2d7fcda56d07b9fc4b5c4f60b17d5800d) | ysolanky |
| 2026-11-18 | [feat: add multi-image and validation to OpenAITools; deprecate DalleT…](https://github.com/agno-agi/agno/commit/69d83166c197672300109862a8ad6fbe6c366950) | sannya-singal |
| 2026-11-17 | [chore: Release v3.2.1 (#11691)](https://github.com/agno-agi/agno/commit/2e9a4521003da1cae559d8049a1c73306fc68004) | harshsinha03 |

[See all commits ↗](https://github.com/agno-agi/agno/commits)

## ⬇️ Get it

```bash
git clone https://github.com/agno-agi/agno.git
```
