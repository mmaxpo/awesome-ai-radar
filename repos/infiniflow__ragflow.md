# infiniflow/ragflow

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/infiniflow/ragflow)

> RAGFlow is an agent-native database: a Retrieval-Augmented Generation (RAG) engine that grew into context infrastructure.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Agent-native RAG engine with deep document understanding |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 94.5k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/infiniflow/ragflow/issues) |
| 💻 **Languages** | Go 72% · TypeScript 21% · C++ 3% · Python 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `rag` `retrieval-augmented-generation` `agentic-ai` `agentic-retrieval` `agentic-search` `context-management` `knowledge-compilation` `agent-harness` `context-engineering` `harness-engineering` `search-harness` `agent-native-database` `context-engine` `retrieval-harness` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 192.0 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 11mo ago</sub>

> Release nightly created from 91c702e86be3dcb3cabc9f6d81e485d02241bef8 at 2026-11-21 13:10:30+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 15d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 22d ago</sub>

> 1.0.0-rc3 is the third and final release candidate before the official v1.0.0 release. It fixes several issues found in rc2 and introduces new features and enhancements.
> **Key updates:**
> 1. Introduced the decision model for evidence sufficiency judgment within the agentic tool loop, and the Categorize component for agents.
> 2. Added support for multiple versions of ingestion pipeline DSL.
> 3. Chat history now stores and displays prompts, token usage, and execution time.
> 4. Compatible with existing v1.0.0-rc2 schema, allowing a direct upgrade.
> …

### [v0.27.3](https://github.com/infiniflow/ragflow/releases/tag/v0.27.3)
<sub>2026-10-23 · 29d ago</sub>

> **What's Changed**
> * Port agentic RAG to GO by @qinling0210 in https://github.com/infiniflow/ragflow/pull/19500
> * Revert "fix(ingestion): allow re-parsing a document whose parse was canceled at progress 0" by @wangq8 in https://github.com/infiniflow/ragflow/pull/19503
> * fix(agent/tool): translate MCP tool inputSchema.properties in Info() by @mkaaad in https://github.com/infiniflow/ragflow/pull/19244
> * Fix: remove deprecated functions by @Lynn-Inf in https://github.com/infiniflow/ragflow/pull/19449
> * fix(sdk): preserve agent answer references by @AnnaSuSu in https://github.com/infiniflow/ragflow/pull/19365
> …

### [v1.0.0-rc2](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc2)
<sub>2026-10-16 · 1mo ago</sub>

> 1.0.0-rc2 is the second release candidate for v1.0.0. This release fixes several issues in rc1 and introduces new features and expanded support.
> **Highlights**
> 1. Introduced Agentic mode for chat, replacing the Low, Medium, High, and Ultra thinking levels.
> 2. Preserved compatibility with existing v1.0.0-rc1 data, allowing direct upgrades.
> 3. Added support for Team/Me sharing.
> 4. Added support for model providers DemonRoute and Opper, web search tools Firecrawl and Search1API, and the MinerU 4 model.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Converge hand-written helpers to shared stdlib and common symbols (#2…](https://github.com/infiniflow/ragflow/commit/91c702e86be3dcb3cabc9f6d81e485d02241bef8) | xugangqiang |
| 2026-11-20 | [Refactor: expose single mode for RAGFlow (#22608)](https://github.com/infiniflow/ragflow/commit/687a9dc87f1edfbf3b35ed8c72ebb192af65b6ef) | wangq8 |
| 2026-11-20 | [fix(agent): keep sentence terminators when narrowing search chunks (#…](https://github.com/infiniflow/ragflow/commit/2038ae5210c6bb6c5a7905eb16bea352f4a3e41f) | chuenchen309 |
| 2026-11-20 | [fix(infinity): render filter conditions in a stable key order (#22169)](https://github.com/infiniflow/ragflow/commit/ffa33766b702f04a633fe44817eaaee58f605f4d) | ccclucky |
| 2026-11-20 | [Fix compliance (#22601)](https://github.com/infiniflow/ragflow/commit/fa7697b1490fcc23939085e41905c8ff5140d6f8) | wangq8 |
| 2026-11-20 | [feat(model): implement soft delete using active status (#22595)](https://github.com/infiniflow/ragflow/commit/ac229305537a0fe71cad7b8de602456debffdaa7) | flyingwhit |
| 2026-11-20 | [Feat: Adjust the layout of the compilation template page (#22603)](https://github.com/infiniflow/ragflow/commit/f1f682534f6189b2db97eb551e1fb496b9aa891f) | cike8899 |
| 2026-11-20 | [Feat: update component styles to use rounded-2xl and rounded-full for…](https://github.com/infiniflow/ragflow/commit/c381212fa86eee5e0bdde25c8a6d433aa28bc437) | cike8899 |
| 2026-11-20 | [feat: add last login tenant column (#22596)](https://github.com/infiniflow/ragflow/commit/e91c8e0432d91c52d5192d52951f53dcc97187c7) | buua436 |
| 2026-11-20 | [Feat: Adjust the layout of the search page (#22597)](https://github.com/infiniflow/ragflow/commit/ea99ad0d1d1e99f128980784a51d7cc56228dd5d) | cike8899 |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
