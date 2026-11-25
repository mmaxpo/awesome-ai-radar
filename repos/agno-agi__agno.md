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
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2022-05-04 |
| 📦 **Latest release** | [v3.2.1](https://github.com/agno-agi/agno/releases/tag/v3.2.1) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 332.4 MB |
| 🌐 **Website** | https://docs.agno.com |

## 📦 Recent releases

### [v3.2.1](https://github.com/agno-agi/agno/releases/tag/v3.2.1)
<sub>2026-11-17 · 7d ago</sub>

> **Changelog**
> **New Features:**
> - **Session Compactions**: `GET /sessions/{session_id}/compactions` lists a session's compactions on `SqliteDb` and `PostgresDb`, newest first, with how many messages each replaced and the token count before and after.
> - **Company Files**: A Task's files and the shared notes can now be read over the API with `GET /company/tasks/{task_id}/files` and `GET /company/notes`, each with a `/{path}` route to read one file. See [cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/05_agent_os/30_company/16_company_file_tree.py).
> **Improvements:**
> - **LinearTools, DiscordTools and ModelsLabTools**: Now take a `timeout` (default 30 seconds, 120 for ModelsLab) that applies to every request.
> …

### [v3.2.0](https://github.com/agno-agi/agno/releases/tag/v3.2.0)
<sub>2026-11-12 · 12d ago</sub>

> **Summary**
> Agno v3.2 makes Super Agent faster and more capable with direct tools, expands Company task governance and coordination, introduces database-backed AgentOS homepage metrics, upgrades A2A to the v1.0 protocol, updates the Slack interface to use the Bolt SDK and makes external agents first-class stored components.
> **Changelog**
> **Breaking changes**
> - **OS Manager defaults and validation:** `OSManager.tool_call_limit` now defaults to 24 (was 8), and `num_history_runs` defaults to 5 (was 7). AgentOS refuses startup when `OSManager(root=...)` is combined with custom tools named `read_file`, `list_files`, or `search_content`.
> - **A2A v1.0:** AgentOS and `A2AClient` now run on the official `a2a-sdk` 1.x, so upgrade the Agno server and client together. ([#10956](https://github.com/agno-agi/agno/pull/10956))
> …

### [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12)
<sub>2026-10-29 · 27d ago</sub>

> **Changelog**
> **New Features:**
> - **Native Approvals for Harness Agents**: Claude's and Codex's own permission requests now reach the AgentOS approval UI. When the agent has a database, including one AgentOS supplies, a native request persists a PAUSED run that shows up in the existing chat and Approvals views, and Resolve plus Continue Run delivers the decision back to the same native execution without replaying the prompt. The harness's own policy decides when to ask — Claude keeps its `permission_mode` and explicit permission callbacks, Codex supports `approval_policy="on-request" | "untrusted" | "never"` alongside its existing SDK `auto_review` and `deny_all` modes — so there is no separate Agno setting to turn on. Decisions are validated against the exact action requested, with sync and async continuation, cancellation, expiry and storage-failure handling, and sandboxed agents keep this across Docker and AgentCore: capability negotiation, a decision RPC, fenced persistence, reattachment after an API-worker loss, separate approval-wait and execution budgets, and no replay after process loss. Note that a `CodexAgent` with no approval settings now runs under the native `on-request` policy, so a request that previously went nowhere pauses the run instead; `hitl_timeout` (default 900s) bounds how long it waits. See `cookbook/frameworks/human_in_the_loop/`.
> - **Initially Disabled Company Routines**: `Routine(enabled=False)` lets a template ship an inactive Routine that a user turns on later from the UI, with `True` still the default. Disabled Routines are created atomically, stay linked to their Product and visible in listings, are skipped by the scheduler, and keep the user's saved choice across restarts. The flag is honored in Python and YAML bootstrap, the setup and creation APIs, the sync and async Company Manager, and the Company tools. Duplicate create requests still return `409` and cannot enable an existing Routine, and the existing pause/resume endpoints enable it without recreating it. See `cookbook/05_agent_os/30_company/11_disabled_routine.py`.
> - **Headline Numbers on Charts**: `ChartTools.create_chart()` takes an optional preformatted `value` — a total or latest value such as `"$22.3K"` or `"94%"` — emitted as `"value"` in the chart block and rendered by Agno OS beside the chart title. The docstring tells the model to leave it out when no single number summarizes the chart, so averages and rates are not summed.
> **Improvements:**
> …

### [v3.1.11](https://github.com/agno-agi/agno/releases/tag/v3.1.11)
<sub>2026-10-27 · 28d ago</sub>

> **Changelog**
> **New Features:**
> - **Harness Agents in Teams and Workflows**: `ClaudeAgent` and `CodexAgent` can now be members of an Agno `Team` and steps of a `Workflow`, including inside `Parallel`, `Loop`, `Condition` and `Router`. The team leader delegates to them with `delegate_task_to_member` like any other member, each harness runs with its own model, tools and workspace, keeps its own conversation across turns of the same session, and the team or workflow collects its runs as usual. A harness agent with `sandbox=` runs each turn in its own container as a member or step, and AgentOS lists harness members on the team page. See `cookbook/frameworks/harness_teams/` and `cookbook/frameworks/harness_workflows/`.
> - **Session Search**: Added `GET /sessions/filter-schema` and `POST /sessions/search` with nested AND/OR/NOT filters on session name, session/user/component IDs, session type and created/updated timestamps, matching the Traces API. Predicates are applied before counting and pagination in PostgreSQL and SQLite, with a batched fallback for other adapters. Sync and async client methods are included.
> - **Company Tasks**: `POST /company/tasks` accepts `status`, so Tasks can be created in Backlog, Ready or Cancelled. Tasks can move between any stages, Done and Cancelled Tasks can reopen, and title and brief can be edited at any stage. In progress still starts only with a run, and moving out of it while that run is executing or paused is refused.
> - **Company Routines**: Added `POST /company/routines/{id}/cancel`, `/archive`, `/restore` and admin-only `DELETE /company/routines/{id}`. `GET /company/routines` takes `sort_by` and `sort_order`. Pause and resume on an on-demand Routine return `409`, and scheduler runs no longer move `updated_at`.
> …

### [v3.1.10](https://github.com/agno-agi/agno/releases/tag/v3.1.10)
<sub>2026-10-23 · 1mo ago</sub>

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
| 2026-11-25 | [feat: accept several comma-separated keys in JWT_VERIFICATION_KEY (#1…](https://github.com/agno-agi/agno/commit/ad3099f8564da68e0ce6625ce2335c3e3ff44817) | ashpreetbedi |
| 2026-11-24 | [[fix] Honor zero result limits in core knowledge searches (#10778)](https://github.com/agno-agi/agno/commit/bd24f44997b3cc86b3cfa9f6608bacc0353c601f) | FanouZeng-TT |
| 2026-11-24 | [[fix] Quote CSV query result fields and headers (#10681)](https://github.com/agno-agi/agno/commit/471f930b2eff3f96aedd45065eab00e9aeceb3f5) | Xuxchloris |
| 2026-11-24 | [fix: read the video id from youtu.be, shorts, embed and live links (#…](https://github.com/agno-agi/agno/commit/63a5a0f92dcb3ebacaf38fe2b8c6aeee52b0d071) | DZH166 |
| 2026-11-24 | [[fix] Gemini: pass image bytes to Part.from_bytes instead of a base64…](https://github.com/agno-agi/agno/commit/eb30cccc389fb16a56e8db3473adf51c05ee8ab4) | HardMax71 |
| 2026-11-24 | [[fix] Deduplicate llms.txt pages before applying the URL limit (#10671)](https://github.com/agno-agi/agno/commit/463e26d7c6c02a2238992b0a7caaba1949ec1696) | lakers-abing |
| 2026-11-24 | [chore: bump pyjwt to 2.15.1 in cookbook lockfiles (#10680)](https://github.com/agno-agi/agno/commit/ef5392390728d57637f8bd7d62122309ab4380bf) | katsugtgz |
| 2026-11-24 | [[fix] Count source pages toward web search result limit (#10678)](https://github.com/agno-agi/agno/commit/31dcf2ea387e448b7f3cab57e88e62a3fba56b6f) | lakers-abing |
| 2026-11-24 | [fix: reject a non-positive page size in CSVReader.async_read (#11829)](https://github.com/agno-agi/agno/commit/7915ddeead5f35a8fc5c1550a6c18e1311430e32) | DZH166 |
| 2026-11-24 | [fix: drop failed table from MetaData on MySQL and SQLite retry  (#11846)](https://github.com/agno-agi/agno/commit/2667dc4c0e02c9b65f2f1ff3c31dedbefa9aac48) | shotsan |

[See all commits ↗](https://github.com/agno-agi/agno/commits)

## ⬇️ Get it

```bash
git clone https://github.com/agno-agi/agno.git
```
