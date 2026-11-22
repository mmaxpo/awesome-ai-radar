# langgenius/dify

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/langgenius/dify)

> Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Build agentic workflows and RAG apps, self-hostable |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 161.7k |
| 🍴 **Forks** | 25.5k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/langgenius/dify/issues) |
| 💻 **Languages** | Python 57% · TypeScript 40% · JavaScript 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `gpt` `llm` `openai` `python` `agent` `nextjs` `workflow` `genai` `automation` `low-code` `mcp` `no-code` `agentic-ai` `agentic-framework` `agentic-workflow` `claude` `skills` `deepseek` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-04-12 |
| 📦 **Latest release** | [1.20.0](https://github.com/langgenius/dify/releases/tag/1.20.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 718.7 MB |
| 🌐 **Website** | https://dify.ai |

## 📦 Recent releases

### [1.20.0](https://github.com/langgenius/dify/releases/tag/1.20.0) — v1.20.0
<sub>2026-11-18 · 4d ago</sub>

> **Dify 1.20.0 keeps your traces flowing and your knowledge bases safer.** Export traces to any OpenTelemetry collector, keep Langfuse working after its legacy ingestion endpoint retirement, and scan uploaded knowledge files for malware before they are indexed. Chatflows can show Agent tool activity as it happens, and personal access tokens let scripts and agents call the Dify OpenAPI on your behalf. The bundled plugin daemon is upgraded to **0.6.15-local**.
> [New Features](#user-content-new-features) · [Configuration and Integration Changes](#user-content-configuration-and-integration-changes) · [Database Migrations](#user-content-database-migrations) · [Upgrade Guide](#user-content-upgrade-guide)
> **New Features**
> **New HITL: bring approvals into your team's messaging tools**
> **Integrate human review into your workflows via email and the messaging tools your team already uses.** New HITL introduces shared channels, centralized contacts, notification templates, and verified approval forms—allowing your team to configure recipients once and reuse them across Human Input nodes, and is now enabled by default (`NEXT_PUBLIC_ENABLE_HITL_IM=true`). (#44864, #45945)
> * **Reach approvers where they work.** Configure email and an IM platform—**Slack, Feishu/Lark, Microsoft Teams, DingTalk, or WeCom**—to deliver workflow review requests through your team's existing channels.
> …

### [1.19.0](https://github.com/langgenius/dify/releases/tag/1.19.0) — v1.19.0 - Trace Your Workflows, Layer by Layer
<sub>2026-11-04 · 18d ago</sub>

> **Dify 1.19.0 brings nested workflow tracing to your observability tools.** Follow a workflow into the Workflow Tools it calls, inspect the steps inside each invocation, and keep the LLM context alongside the execution tree.
> This release also makes Workflow Tools portable with App packages, adds Skill Hub automation, and makes Agent files easier to upload and preview. The bundled plugin daemon is upgraded to **0.6.14-local**.
> [Release highlights](#user-content-release-highlights) · [Upgrade guide](#user-content-upgrade-guide) · [Detailed changes](#user-content-detailed-changes)
> <a id="release-highlights"></a>
> **Release highlights**
> **Nested workflow tracing**
> …

### [1.18.0](https://github.com/langgenius/dify/releases/tag/1.18.0) — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility
<sub>2026-10-23 · 1mo ago</sub>

> Dify 1.18.0 brings **Agents that route workflows**, **portable app packages**, **deeper visibility into nested workflow runs**, and the opt-in **Agent Knowledge Base** experience. OpenAPI and the new difyctl expand how you build and manage apps from the command line.
> > [!IMPORTANT]
> > **Read the upgrade guide below before deploying.** Upgrade the API, workers, Agent Backend, and Agent runtime images together. Local Agent sandboxes require a non-empty authentication token, and Agent Backend uses a new run protocol. Source installations require Python 3.13. Install the new difyctl client and sign in again. Preserve your existing `PASSWORD_PEPPER` configuration.
> **Release highlights**
> **Agents that choose the next step**
> Let an Agent decide which workflow branch to take. Enable **Output Routes**, give each route a selection condition, and connect it to the next step—such as resolving a request directly or handing it to a specialist. The read-only `switch` output exposes the chosen route. (#42599)
> …

### [1.17.1](https://github.com/langgenius/dify/releases/tag/1.17.1) — v1.17.1 - Bug Fixes and Improvements
<sub>2026-09-10 · 2mo ago</sub>

> > [!WARNING]
> > **Self-hosted deployments using the bundled Weaviate must complete a manual, staged upgrade before starting 1.17.1.** The bundled Weaviate server moves from `1.27.0` to `1.39.2` — 12 minor versions — and skipping minors **is unsupported**. Pulling and restarting can silently and permanently break vector search. See Upgrade Guide below. Fresh deployments, external Weaviate, and other vector stores are unaffected.
> **New Features**
> **Dataset-Scoped Knowledge Base API Keys**
> - Knowledge base service-API keys were scoped to the whole workspace: one key could read and write every knowledge base in the tenant, so giving an integration access to a single knowledge base meant giving it access to all of them. Keys can now be bound to specific knowledge bases from the knowledge base's API access panel, with a workspace / this-knowledge-base scope selector at creation time. A bound key returns `403` for any other dataset — both documents and retrieval — and for endpoints that carry no dataset ID, such as list-all. Existing keys are unbound and keep their workspace-wide behavior, so nothing changes when you upgrade. (#37569)
> **Keyboard Movement for Workflow Nodes and Comments**
> …

### [1.17.0](https://github.com/langgenius/dify/releases/tag/1.17.0) — v1.17.0
<sub>2026-08-25 · 2mo ago</sub>

> **New Features**
> **Agent: E2B Sandbox, Home Snapshots, and Skill Management**
> - **E2B sandbox backend**: agent shell/code execution can now run on [E2B](https://e2b.dev) cloud sandboxes in addition to the local sandbox. Select the backend with `DIFY_AGENT_RUNTIME_BACKEND`; a new `docker-compose.e2b.yaml` ships the E2B stack, E2B traffic is authenticated, and the E2B template is synced on release (#39480, #39705, #39873, #39996, #40858, #40871, #40891, #40892).
> - **Build-time Home Snapshots**: when an agent build is applied (published), the agent's sandbox home directory — installed packages, prepared files, working state — is captured and subsequent runs of the published agent restore their home directory from that snapshot, so the agent starts from the exact filesystem state it had at build time. (#39702, #40876, #40996).
> - **Workspace-level Skill management**: Skills are reusable, versioned capabilities packaged with code and tool definitions that agents can discover and invoke. A new workspace-level skills manager with draft → publish → version lifecycle ships alongside a web UI (skill listing, builder panel, file editor).  (#39675, #39798, #39799, #41180).
> - **Context-aware history compaction**: long agent conversations no longer blow past the model's context window — Dify resolves each model's effective window and tiers compaction (clear old tool results first, then summarize older history) so runs stay within budget without losing recent context (#40872).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [fix(api): send custom tool JSON bodies as JSON when the content type …](https://github.com/langgenius/dify/commit/a06bc83cf02aafd6e18ff3f73af93e4d64c306cd) | Revinand |
| 2026-11-22 | [test(api): bring the tools transform service tests under strict pyref…](https://github.com/langgenius/dify/commit/597f623a1fc70650abe8a77b074b90cd3ddba7f2) | yetuge |
| 2026-11-22 | [fix(web): remove skip link animation (#46906)](https://github.com/langgenius/dify/commit/dfb269c1520e46899d722b9187ddad087a69d943) | lyzno1 |
| 2026-11-22 | [fix(web): preserve permission set deletion confirmation (#46903)](https://github.com/langgenius/dify/commit/68d0cffd004acbe70503912f41aa98580f27dd33) | lyzno1 |
| 2026-11-22 | [refactor(api): initialize trial provider records through short-lived …](https://github.com/langgenius/dify/commit/5cadff3b04282413df6484b247542438a45f8096) | paulhuiseismic |
| 2026-11-22 | [fix(web): allow canceling workflow DSL exports (#46901)](https://github.com/langgenius/dify/commit/a6ea1b0f9bd4e2a81376b56fed607cd63e886aeb) | lyzno1 |
| 2026-11-22 | [docs(dify-ui): clarify dialog dismissal during requests (#46895)](https://github.com/langgenius/dify/commit/f2b8315e5d294724caf7475c227382ce93c2d076) | lyzno1 |
| 2026-11-22 | [fix(api): resolve remaining pyrefly diagnostics (#46769) (#46770)](https://github.com/langgenius/dify/commit/c19e1446ba5e8404797dddf62ee00c9bbb2d1cbd) | P-r-e-m-i-u-m |
| 2026-11-22 | [fix(web): preserve the selected pipeline template during deletion (#4…](https://github.com/langgenius/dify/commit/6f99da3f8ce131d0d4cec1fad3dc3b649bf7a320) | lyzno1 |
| 2026-11-21 | [fix(web): keep external API deletion checks with the confirmation (#4…](https://github.com/langgenius/dify/commit/8b6fbfb010ff77b6d2d9e57c4fdd3d8225f3e6ca) | lyzno1 |

[See all commits ↗](https://github.com/langgenius/dify/commits)

## ⬇️ Get it

```bash
git clone https://github.com/langgenius/dify.git
```
