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
| ⭐ **Stars** | 43.2k |
| 🍴 **Forks** | 6.3k |
| 🐞 **Open issues + PRs** | [1.9k](https://github.com/agno-agi/agno/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `developer-tools` `python` `agents` `ai` `ai-agents` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2022-05-04 |
| 📦 **Latest release** | [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 2026-10-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 329.3 MB |
| 🌐 **Website** | https://docs.agno.com |

## 📦 Recent releases

### [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12)
<sub>2026-10-29 · 13d ago</sub>

> **Changelog**
> **New Features:**
> - **Native Approvals for Harness Agents**: Claude's and Codex's own permission requests now reach the AgentOS approval UI. When the agent has a database, including one AgentOS supplies, a native request persists a PAUSED run that shows up in the existing chat and Approvals views, and Resolve plus Continue Run delivers the decision back to the same native execution without replaying the prompt. The harness's own policy decides when to ask — Claude keeps its `permission_mode` and explicit permission callbacks, Codex supports `approval_policy="on-request" | "untrusted" | "never"` alongside its existing SDK `auto_review` and `deny_all` modes — so there is no separate Agno setting to turn on. Decisions are validated against the exact action requested, with sync and async continuation, cancellation, expiry and storage-failure handling, and sandboxed agents keep this across Docker and AgentCore: capability negotiation, a decision RPC, fenced persistence, reattachment after an API-worker loss, separate approval-wait and execution budgets, and no replay after process loss. Note that a `CodexAgent` with no approval settings now runs under the native `on-request` policy, so a request that previously went nowhere pauses the run instead; `hitl_timeout` (default 900s) bounds how long it waits. See `cookbook/frameworks/human_in_the_loop/`.
> - **Initially Disabled Company Routines**: `Routine(enabled=False)` lets a template ship an inactive Routine that a user turns on later from the UI, with `True` still the default. Disabled Routines are created atomically, stay linked to their Product and visible in listings, are skipped by the scheduler, and keep the user's saved choice across restarts. The flag is honored in Python and YAML bootstrap, the setup and creation APIs, the sync and async Company Manager, and the Company tools. Duplicate create requests still return `409` and cannot enable an existing Routine, and the existing pause/resume endpoints enable it without recreating it. See `cookbook/05_agent_os/30_company/11_disabled_routine.py`.
> - **Headline Numbers on Charts**: `ChartTools.create_chart()` takes an optional preformatted `value` — a total or latest value such as `"$22.3K"` or `"94%"` — emitted as `"value"` in the chart block and rendered by Agno OS beside the chart title. The docstring tells the model to leave it out when no single number summarizes the chart, so averages and rates are not summed.
> **Improvements:**
> …

### [v3.1.11](https://github.com/agno-agi/agno/releases/tag/v3.1.11)
<sub>2026-10-27 · 15d ago</sub>

> **Changelog**
> **New Features:**
> - **Harness Agents in Teams and Workflows**: `ClaudeAgent` and `CodexAgent` can now be members of an Agno `Team` and steps of a `Workflow`, including inside `Parallel`, `Loop`, `Condition` and `Router`. The team leader delegates to them with `delegate_task_to_member` like any other member, each harness runs with its own model, tools and workspace, keeps its own conversation across turns of the same session, and the team or workflow collects its runs as usual. A harness agent with `sandbox=` runs each turn in its own container as a member or step, and AgentOS lists harness members on the team page. See `cookbook/frameworks/harness_teams/` and `cookbook/frameworks/harness_workflows/`.
> - **Session Search**: Added `GET /sessions/filter-schema` and `POST /sessions/search` with nested AND/OR/NOT filters on session name, session/user/component IDs, session type and created/updated timestamps, matching the Traces API. Predicates are applied before counting and pagination in PostgreSQL and SQLite, with a batched fallback for other adapters. Sync and async client methods are included.
> - **Company Tasks**: `POST /company/tasks` accepts `status`, so Tasks can be created in Backlog, Ready or Cancelled. Tasks can move between any stages, Done and Cancelled Tasks can reopen, and title and brief can be edited at any stage. In progress still starts only with a run, and moving out of it while that run is executing or paused is refused.
> - **Company Routines**: Added `POST /company/routines/{id}/cancel`, `/archive`, `/restore` and admin-only `DELETE /company/routines/{id}`. `GET /company/routines` takes `sort_by` and `sort_order`. Pause and resume on an on-demand Routine return `409`, and scheduler runs no longer move `updated_at`.
> …

### [v3.1.10](https://github.com/agno-agi/agno/releases/tag/v3.1.10)
<sub>2026-10-23 · 20d ago</sub>

> **Changelog**
> **Bug Fixes:**
> - **CodexAgent**: Now signs in automatically with `OPENAI_API_KEY`, and keeps an existing ChatGPT or other login.
> - **OS Manager**: OS Manager now lists and runs external agents such as `ClaudeAgent` and `CodexAgent` registered in `AgentOS(agents=[...])`, by name or ID.
> - **Knowledge Upload**: `POST /knowledge/content` now returns a clear `400` message when an upload has no file, `text_content` or URL, or when `url` is not a single URL.
> - **Tracing**: Spans from `AgentOS(tracing=True)` and `setup_tracing()` now keep up to 1,024 attributes, so model spans keep their full input and message history on runs with many tool calls. `OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT` and `OTEL_ATTRIBUTE_COUNT_LIMIT` still take precedence.
> …

### [v3.1.9](https://github.com/agno-agi/agno/releases/tag/v3.1.9)
<sub>2026-10-22 · 20d ago</sub>

> **Changelog**
> **New Features:**
> - **MCP Tool Runner**: `POST /mcp/server/tools/{tool_name}/run` runs any tool listed on the AgentOS Server Card over HTTP and returns its result, so a tool can be tested without an MCP client. Turn it off with `MCPConfig(tool_run_endpoint=False)`. See [cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/05_agent_os/14_mcp/inspect_tools.py).
> **Bug Fixes:**
> - **AgentOS MCP Server**: `/mcp` and `/mcp/server-card` now accept browser requests from origins the AgentOS CORS policy allows, so `os.agno.com` can reach the MCP server of a local AgentOS. `/info` now reports the configured MCP path instead of always `/mcp`.
> - **Postgres Metrics**: Metrics refresh on a migrated database no longer loads the legacy `sessions.runs` column into memory.
> …

### [v3.1.8](https://github.com/agno-agi/agno/releases/tag/v3.1.8)
<sub>2026-10-21 · 22d ago</sub>

> **Changelog**
> **New Features**
> - Postgres Sandbox Checkpoint Store: Added `PostgresCheckpointStore` for storing sandbox checkpoints directly in PostgreSQL, allowing multi-replica deployments to restore sessions without S3 or shared filesystems. Checkpoints are chunked, written transactionally, deduplicated by SHA-256 and verified on read. It is opt-in; existing checkpoint defaults are unchanged. (#11186)
> - Framework Managers as Routine Executors: Company Routines can now use the internal Product Manager or OS Manager as executors through declarations, the Routine API and human-chat configuration. Reserved manager IDs resolve only from the owning AgentOS and cannot be replaced by saved or user-defined components. Includes an optional weekly Product Manager review. (#11193)
> - Sandbox Checkpoint Retention: Sandboxes now retain the three newest checkpoints per session by default. Configure `retain_checkpoints=None` to preserve every checkpoint. Unpublished or superseded checkpoints are retired and deleted after the run outcome is safely stored. (#11187)
> **Improvements**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [fix: Company fixes before 3.2 (#11592)](https://github.com/agno-agi/agno/commit/70be8704e1776f9369106030f976112754cc06ac) | ashpreetbedi |
| 2026-11-12 | [feat: deliver Company Task results with evidence and continue Tasks f…](https://github.com/agno-agi/agno/commit/616daeb3f872aac47cc26cd6e955c571cec1481c) | kausmeows |
| 2026-11-11 | [fix: stop the durable queue sweeping or reclaiming runs still executi…](https://github.com/agno-agi/agno/commit/257cd57e9637964f44fc3d7e3ad142ca066b2e43) | ysolanky |
| 2026-11-11 | [feat: one file tree for Super Agent, Mini Agent and Company (#11588)](https://github.com/agno-agi/agno/commit/8f7512c6790902578068743ae2328d3134e3938b) | ashpreetbedi |
| 2026-11-11 | [fix: send remote run fields in a shape AgentOS parses (#11587)](https://github.com/agno-agi/agno/commit/df3a5a4ea123336a9634d2b6e0640b5234e29b0e) | ysolanky |
| 2026-11-11 | [fix: run post-hook guardrails and keep workflow metadata on a continu…](https://github.com/agno-agi/agno/commit/484bdcd15251d66127f7ff8992ca326ee3fd42ba) | ashpreetbedi |
| 2026-11-11 | [feat: auto_accept is one switch on a Routine, in code or from chat (#…](https://github.com/agno-agi/agno/commit/94cb6698d3c631b44c0858f4990fd3cc76ef60ac) | ashpreetbedi |
| 2026-11-11 | [feat: decide Company work from chat and run accepted Tasks on Mini Ag…](https://github.com/agno-agi/agno/commit/20ce8b95da9f4d76290362d822a32e4b48970efc) | ashpreetbedi |
| 2026-11-11 | [feat: add a GitHub interface for webhook events and GitHub App creden…](https://github.com/agno-agi/agno/commit/e88fb12b5b3632cb1f2276cd123f471a545fb402) | kausmeows |
| 2026-11-11 | [feat: Super Agent does the work itself with direct tools (#11572)](https://github.com/agno-agi/agno/commit/bc6fcc99e2487959e7ae4bc671be6230991df277) | ashpreetbedi |

[See all commits ↗](https://github.com/agno-agi/agno/commits)

## ⬇️ Get it

```bash
git clone https://github.com/agno-agi/agno.git
```
