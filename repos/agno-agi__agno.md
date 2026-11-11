# agno-agi/agno

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/agno-agi/agno)

> The self-driving agent platform

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why I saved it** | Fast framework for agents with memory, tools and teams |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 43.1k |
| 🍴 **Forks** | 6.3k |
| 🐞 **Open issues + PRs** | [1.9k](https://github.com/agno-agi/agno/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `developer-tools` `python` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2022-05-04 |
| 📦 **Latest release** | [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12) — 2026-10-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 328.6 MB |
| 🌐 **Website** | https://docs.agno.com |

## 📦 Recent releases

### [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12)
<sub>2026-10-29 · 12d ago</sub>

> **Changelog**
> **New Features:**
> - **Native Approvals for Harness Agents**: Claude's and Codex's own permission requests now reach the AgentOS approval UI. When the agent has a database, including one AgentOS supplies, a native request persists a PAUSED run that shows up in the existing chat and Approvals views, and Resolve plus Continue Run delivers the decision back to the same native execution without replaying the prompt. The harness's own policy decides when to ask — Claude keeps its `permission_mode` and explicit permission callbacks, Codex supports `approval_policy="on-request" | "untrusted" | "never"` alongside its existing SDK `auto_review` and `deny_all` modes — so there is no separate Agno setting to turn on. Decisions are validated against the exact action requested, with sync and async continuation, cancellation, expiry and storage-failure handling, and sandboxed agents keep this across Docker and AgentCore: capability negotiation, a decision RPC, fenced persistence, reattachment after an API-worker loss, separate approval-wait and execution budgets, and no replay after process loss. Note that a `CodexAgent` with no approval settings now runs under the native `on-request` policy, so a request that previously went nowhere pauses the run instead; `hitl_timeout` (default 900s) bounds how long it waits. See `cookbook/frameworks/human_in_the_loop/`.
> - **Initially Disabled Company Routines**: `Routine(enabled=False)` lets a template ship an inactive Routine that a user turns on later from the UI, with `True` still the default. Disabled Routines are created atomically, stay linked to their Product and visible in listings, are skipped by the scheduler, and keep the user's saved choice across restarts. The flag is honored in Python and YAML bootstrap, the setup and creation APIs, the sync and async Company Manager, and the Company tools. Duplicate create requests still return `409` and cannot enable an existing Routine, and the existing pause/resume endpoints enable it without recreating it. See `cookbook/05_agent_os/30_company/11_disabled_routine.py`.
> - **Headline Numbers on Charts**: `ChartTools.create_chart()` takes an optional preformatted `value` — a total or latest value such as `"$22.3K"` or `"94%"` — emitted as `"value"` in the chart block and rendered by Agno OS beside the chart title. The docstring tells the model to leave it out when no single number summarizes the chart, so averages and rates are not summed.
> **Improvements:**
> …

### [v3.1.11](https://github.com/agno-agi/agno/releases/tag/v3.1.11)
<sub>2026-10-27 · 14d ago</sub>

> **Changelog**
> **New Features:**
> - **Harness Agents in Teams and Workflows**: `ClaudeAgent` and `CodexAgent` can now be members of an Agno `Team` and steps of a `Workflow`, including inside `Parallel`, `Loop`, `Condition` and `Router`. The team leader delegates to them with `delegate_task_to_member` like any other member, each harness runs with its own model, tools and workspace, keeps its own conversation across turns of the same session, and the team or workflow collects its runs as usual. A harness agent with `sandbox=` runs each turn in its own container as a member or step, and AgentOS lists harness members on the team page. See `cookbook/frameworks/harness_teams/` and `cookbook/frameworks/harness_workflows/`.
> - **Session Search**: Added `GET /sessions/filter-schema` and `POST /sessions/search` with nested AND/OR/NOT filters on session name, session/user/component IDs, session type and created/updated timestamps, matching the Traces API. Predicates are applied before counting and pagination in PostgreSQL and SQLite, with a batched fallback for other adapters. Sync and async client methods are included.
> - **Company Tasks**: `POST /company/tasks` accepts `status`, so Tasks can be created in Backlog, Ready or Cancelled. Tasks can move between any stages, Done and Cancelled Tasks can reopen, and title and brief can be edited at any stage. In progress still starts only with a run, and moving out of it while that run is executing or paused is refused.
> - **Company Routines**: Added `POST /company/routines/{id}/cancel`, `/archive`, `/restore` and admin-only `DELETE /company/routines/{id}`. `GET /company/routines` takes `sort_by` and `sort_order`. Pause and resume on an on-demand Routine return `409`, and scheduler runs no longer move `updated_at`.
> …

### [v3.1.10](https://github.com/agno-agi/agno/releases/tag/v3.1.10)
<sub>2026-10-23 · 18d ago</sub>

> **Changelog**
> **Bug Fixes:**
> - **CodexAgent**: Now signs in automatically with `OPENAI_API_KEY`, and keeps an existing ChatGPT or other login.
> - **OS Manager**: OS Manager now lists and runs external agents such as `ClaudeAgent` and `CodexAgent` registered in `AgentOS(agents=[...])`, by name or ID.
> - **Knowledge Upload**: `POST /knowledge/content` now returns a clear `400` message when an upload has no file, `text_content` or URL, or when `url` is not a single URL.
> - **Tracing**: Spans from `AgentOS(tracing=True)` and `setup_tracing()` now keep up to 1,024 attributes, so model spans keep their full input and message history on runs with many tool calls. `OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT` and `OTEL_ATTRIBUTE_COUNT_LIMIT` still take precedence.
> …

### [v3.1.9](https://github.com/agno-agi/agno/releases/tag/v3.1.9)
<sub>2026-10-22 · 19d ago</sub>

> **Changelog**
> **New Features:**
> - **MCP Tool Runner**: `POST /mcp/server/tools/{tool_name}/run` runs any tool listed on the AgentOS Server Card over HTTP and returns its result, so a tool can be tested without an MCP client. Turn it off with `MCPConfig(tool_run_endpoint=False)`. See [cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/05_agent_os/14_mcp/inspect_tools.py).
> **Bug Fixes:**
> - **AgentOS MCP Server**: `/mcp` and `/mcp/server-card` now accept browser requests from origins the AgentOS CORS policy allows, so `os.agno.com` can reach the MCP server of a local AgentOS. `/info` now reports the configured MCP path instead of always `/mcp`.
> - **Postgres Metrics**: Metrics refresh on a migrated database no longer loads the legacy `sessions.runs` column into memory.
> …

### [v3.1.8](https://github.com/agno-agi/agno/releases/tag/v3.1.8)
<sub>2026-10-21 · 20d ago</sub>

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
| 2026-11-11 | [fix: metrics refresh follow-ups for MongoDB, Valkey and DynamoDB legacy runs (#11574)](https://github.com/agno-agi/agno/commit/0b88f303e1ebd58a92677652fdeaddd7e7618362) | harshsinha03 |
| 2026-11-10 | [fix: log metrics refresh no-op messages at debug level (#11570)](https://github.com/agno-agi/agno/commit/23eaf7db5c13d031d3148bbae088acad224431aa) | ysolanky |
| 2026-11-10 | [feat: update company details from human chats (#11569)](https://github.com/agno-agi/agno/commit/f19bdfa3f6fe245e7739945bf5d5f1c96726622a) | ashpreetbedi |
| 2026-11-10 | [feat: metrics tables, background refresh and /os/metrics homepage routes on every database (#10874)](https://github.com/agno-agi/agno/commit/d3e18144c2268dc80ae9d7a205d9929cc4751966) | harshsinha03 |
| 2026-11-10 | [fix: use beta Gemini Developer API for supported model features (#11564)](https://github.com/agno-agi/agno/commit/1d0d852a881a4fba60f7416601220f0a1347ca52) | Himanshu040604 |
| 2026-11-10 | [feat: add short Company coordination instructions to Super Agent (#11563)](https://github.com/agno-agi/agno/commit/1c3ef6c401f0134e8ca911f69a933f9b581349e5) | ashpreetbedi |
| 2026-11-10 | [feat: add public manager IDs and company details (#11502)](https://github.com/agno-agi/agno/commit/abedb7b046561fb38b5a400420c84f905a364320) | ashpreetbedi |
| 2026-11-09 | [[cookbook] Add Membase memory integration example (#11552)](https://github.com/agno-agi/agno/commit/f9272ec2dfd76b664ddf727b3abf564d62cbbea5) | parasyte-x |
| 2026-11-09 | [[fix] copy the reasoning block before writing derived params into it (#10310)](https://github.com/agno-agi/agno/commit/37d8f061a086403fbce017f360717dab05b0b34c) | feiiiiii5 |
| 2026-11-09 | [[fix] Preserve HTML and nested bodies in Gmail list tools (#10359)](https://github.com/agno-agi/agno/commit/ad31f9db5745485bfdd61636d54859f7bff01797) | tdog54646 |

[See all commits ↗](https://github.com/agno-agi/agno/commits)

## 👥 Top contributors

[ashpreetbedi](https://github.com/ashpreetbedi) (2569) · [ysolanky](https://github.com/ysolanky) (645) · [dirkbrnd](https://github.com/dirkbrnd) (453) · [kausmeows](https://github.com/kausmeows) (359) · [Mustafa-Esoofally](https://github.com/Mustafa-Esoofally) (224)

## ⬇️ Get it

```bash
git clone https://github.com/agno-agi/agno.git
```
