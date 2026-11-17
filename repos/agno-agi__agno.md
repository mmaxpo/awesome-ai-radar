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
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2022-05-04 |
| 📦 **Latest release** | [v3.2.0](https://github.com/agno-agi/agno/releases/tag/v3.2.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 329.5 MB |
| 🌐 **Website** | https://docs.agno.com |

## 📦 Recent releases

### [v3.2.0](https://github.com/agno-agi/agno/releases/tag/v3.2.0)
<sub>2026-11-12 · 4d ago</sub>

> **Summary**
> Agno v3.2 makes Super Agent faster and more capable with direct tools, expands Company task governance and coordination, introduces database-backed AgentOS homepage metrics, upgrades A2A to the v1.0 protocol, updates the Slack interface to use the Bolt SDK and makes external agents first-class stored components.
> **Changelog**
> **Breaking changes**
> - **OS Manager defaults and validation:** `OSManager.tool_call_limit` now defaults to 24 (was 8), and `num_history_runs` defaults to 5 (was 7). AgentOS refuses startup when `OSManager(root=...)` is combined with custom tools named `read_file`, `list_files`, or `search_content`.
> - **A2A v1.0:** AgentOS and `A2AClient` now run on the official `a2a-sdk` 1.x, so upgrade the Agno server and client together. ([#10956](https://github.com/agno-agi/agno/pull/10956))
> …

### [v3.1.12](https://github.com/agno-agi/agno/releases/tag/v3.1.12)
<sub>2026-10-29 · 19d ago</sub>

> **Changelog**
> **New Features:**
> - **Native Approvals for Harness Agents**: Claude's and Codex's own permission requests now reach the AgentOS approval UI. When the agent has a database, including one AgentOS supplies, a native request persists a PAUSED run that shows up in the existing chat and Approvals views, and Resolve plus Continue Run delivers the decision back to the same native execution without replaying the prompt. The harness's own policy decides when to ask — Claude keeps its `permission_mode` and explicit permission callbacks, Codex supports `approval_policy="on-request" | "untrusted" | "never"` alongside its existing SDK `auto_review` and `deny_all` modes — so there is no separate Agno setting to turn on. Decisions are validated against the exact action requested, with sync and async continuation, cancellation, expiry and storage-failure handling, and sandboxed agents keep this across Docker and AgentCore: capability negotiation, a decision RPC, fenced persistence, reattachment after an API-worker loss, separate approval-wait and execution budgets, and no replay after process loss. Note that a `CodexAgent` with no approval settings now runs under the native `on-request` policy, so a request that previously went nowhere pauses the run instead; `hitl_timeout` (default 900s) bounds how long it waits. See `cookbook/frameworks/human_in_the_loop/`.
> - **Initially Disabled Company Routines**: `Routine(enabled=False)` lets a template ship an inactive Routine that a user turns on later from the UI, with `True` still the default. Disabled Routines are created atomically, stay linked to their Product and visible in listings, are skipped by the scheduler, and keep the user's saved choice across restarts. The flag is honored in Python and YAML bootstrap, the setup and creation APIs, the sync and async Company Manager, and the Company tools. Duplicate create requests still return `409` and cannot enable an existing Routine, and the existing pause/resume endpoints enable it without recreating it. See `cookbook/05_agent_os/30_company/11_disabled_routine.py`.
> - **Headline Numbers on Charts**: `ChartTools.create_chart()` takes an optional preformatted `value` — a total or latest value such as `"$22.3K"` or `"94%"` — emitted as `"value"` in the chart block and rendered by Agno OS beside the chart title. The docstring tells the model to leave it out when no single number summarizes the chart, so averages and rates are not summed.
> **Improvements:**
> …

### [v3.1.11](https://github.com/agno-agi/agno/releases/tag/v3.1.11)
<sub>2026-10-27 · 20d ago</sub>

> **Changelog**
> **New Features:**
> - **Harness Agents in Teams and Workflows**: `ClaudeAgent` and `CodexAgent` can now be members of an Agno `Team` and steps of a `Workflow`, including inside `Parallel`, `Loop`, `Condition` and `Router`. The team leader delegates to them with `delegate_task_to_member` like any other member, each harness runs with its own model, tools and workspace, keeps its own conversation across turns of the same session, and the team or workflow collects its runs as usual. A harness agent with `sandbox=` runs each turn in its own container as a member or step, and AgentOS lists harness members on the team page. See `cookbook/frameworks/harness_teams/` and `cookbook/frameworks/harness_workflows/`.
> - **Session Search**: Added `GET /sessions/filter-schema` and `POST /sessions/search` with nested AND/OR/NOT filters on session name, session/user/component IDs, session type and created/updated timestamps, matching the Traces API. Predicates are applied before counting and pagination in PostgreSQL and SQLite, with a batched fallback for other adapters. Sync and async client methods are included.
> - **Company Tasks**: `POST /company/tasks` accepts `status`, so Tasks can be created in Backlog, Ready or Cancelled. Tasks can move between any stages, Done and Cancelled Tasks can reopen, and title and brief can be edited at any stage. In progress still starts only with a run, and moving out of it while that run is executing or paused is refused.
> - **Company Routines**: Added `POST /company/routines/{id}/cancel`, `/archive`, `/restore` and admin-only `DELETE /company/routines/{id}`. `GET /company/routines` takes `sort_by` and `sort_order`. Pause and resume on an on-demand Routine return `409`, and scheduler runs no longer move `updated_at`.
> …

### [v3.1.10](https://github.com/agno-agi/agno/releases/tag/v3.1.10)
<sub>2026-10-23 · 25d ago</sub>

> **Changelog**
> **Bug Fixes:**
> - **CodexAgent**: Now signs in automatically with `OPENAI_API_KEY`, and keeps an existing ChatGPT or other login.
> - **OS Manager**: OS Manager now lists and runs external agents such as `ClaudeAgent` and `CodexAgent` registered in `AgentOS(agents=[...])`, by name or ID.
> - **Knowledge Upload**: `POST /knowledge/content` now returns a clear `400` message when an upload has no file, `text_content` or URL, or when `url` is not a single URL.
> - **Tracing**: Spans from `AgentOS(tracing=True)` and `setup_tracing()` now keep up to 1,024 attributes, so model spans keep their full input and message history on runs with many tool calls. `OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT` and `OTEL_ATTRIBUTE_COUNT_LIMIT` still take precedence.
> …

### [v3.1.9](https://github.com/agno-agi/agno/releases/tag/v3.1.9)
<sub>2026-10-22 · 25d ago</sub>

> **Changelog**
> **New Features:**
> - **MCP Tool Runner**: `POST /mcp/server/tools/{tool_name}/run` runs any tool listed on the AgentOS Server Card over HTTP and returns its result, so a tool can be tested without an MCP client. Turn it off with `MCPConfig(tool_run_endpoint=False)`. See [cookbook](https://github.com/agno-agi/agno/blob/main/cookbook/05_agent_os/14_mcp/inspect_tools.py).
> **Bug Fixes:**
> - **AgentOS MCP Server**: `/mcp` and `/mcp/server-card` now accept browser requests from origins the AgentOS CORS policy allows, so `os.agno.com` can reach the MCP server of a local AgentOS. `/info` now reports the configured MCP path instead of always `/mcp`.
> - **Postgres Metrics**: Metrics refresh on a migrated database no longer loads the legacy `sessions.runs` column into memory.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix: postgres drop a failed table from MetaData so a retry can create…](https://github.com/agno-agi/agno/commit/8b5ce9f85812519a2452ff47981964b202e23828) | HhH666-ux |
| 2026-11-17 | [[fix] Pin Daytona extra below 1.0 and hint a supported SDK (#11725)](https://github.com/agno-agi/agno/commit/9aa12c4111e9f134089e7ac8d7ea3c7b320ac779) | ningyixi |
| 2026-11-17 | [fix: report MCPTools.connect() outcome and cleanup on CancelledError …](https://github.com/agno-agi/agno/commit/148d30fdfbc740a4c95d10d51ede8143a6cda5fa) | surlymochan |
| 2026-11-17 | [fix: surface SQLTools fetch errors instead of returning [] (#11680)](https://github.com/agno-agi/agno/commit/8a252e15b58de6dc923f533bd356089c033d8040) | adityav1709 |
| 2026-11-17 | [fix: qdrant honour batch_size when inserting documents (#11722)](https://github.com/agno-agi/agno/commit/f7c1c0380a8a1512dbf5aec831744d771e402d21) | HhH666-ux |
| 2026-11-17 | [fix: preserve non-ASCII characters in skill tool outputs (#11540)](https://github.com/agno-agi/agno/commit/a0d7208e4ec3c10f493ffc46df78b24c58c49bf1) | xingjy10 |
| 2026-11-16 | [fix: support openai-codex 0.163.0 and newer for native Codex approval…](https://github.com/agno-agi/agno/commit/11d144107895933cc6dc668eb520f7b850595d06) | sannya-singal |
| 2026-11-16 | [fix: pin httpx2<2.16.1 so mistralai imports again (#11703)](https://github.com/agno-agi/agno/commit/3cb5054ae5f8b20b50abe9e3e7364ae1ccf8cee1) | sannya-singal |
| 2026-11-16 | [chore: correct two docstrings that promise a returned tuple (#11550)](https://github.com/agno-agi/agno/commit/53cd81e884847341a0815b4a94b8ec8a79f478bd) | lxcxjxhx |
| 2026-11-16 | [fix: count real lines in Workspace.read_file so max_file_lines accept…](https://github.com/agno-agi/agno/commit/b19cf8833073f7181a9a797104895e0f7816dac2) | DZH166 |

[See all commits ↗](https://github.com/agno-agi/agno/commits)

## ⬇️ Get it

```bash
git clone https://github.com/agno-agi/agno.git
```
