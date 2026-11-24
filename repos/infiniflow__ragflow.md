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
| ⭐ **Stars** | 94.6k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/infiniflow/ragflow/issues) |
| 💻 **Languages** | Go 73% · TypeScript 21% · C++ 3% · Python 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `rag` `retrieval-augmented-generation` `agentic-ai` `agentic-retrieval` `agentic-search` `context-management` `knowledge-compilation` `agent-harness` `context-engineering` `harness-engineering` `search-harness` `agent-native-database` `context-engine` `retrieval-harness` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 194.1 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 11mo ago</sub>

> Release nightly created from 8c68034679bf3f5aa6ad5d14ce3899b8915db1ea at 2026-11-24 13:15:17+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 18d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 25d ago</sub>

> 1.0.0-rc3 is the third and final release candidate before the official v1.0.0 release. It fixes several issues found in rc2 and introduces new features and enhancements.
> **Key updates:**
> 1. Introduced the decision model for evidence sufficiency judgment within the agentic tool loop, and the Categorize component for agents.
> 2. Added support for multiple versions of ingestion pipeline DSL.
> 3. Chat history now stores and displays prompts, token usage, and execution time.
> 4. Compatible with existing v1.0.0-rc2 schema, allowing a direct upgrade.
> …

### [v0.27.3](https://github.com/infiniflow/ragflow/releases/tag/v0.27.3)
<sub>2026-10-23 · 1mo ago</sub>

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
| 2026-11-24 | [fix(web): only underline doc citations that can be opened (#22743)](https://github.com/infiniflow/ragflow/commit/8c68034679bf3f5aa6ad5d14ce3899b8915db1ea) | dcc123456 |
| 2026-11-24 | [Fix: remove agent filter on message list page (#22742)](https://github.com/infiniflow/ragflow/commit/5e638a2298976ae6302b4ccc5732821ca0b496f6) | Lynn-Inf |
| 2026-11-24 | [Fix deployment to use X_PORT to expose port (#22741)](https://github.com/infiniflow/ragflow/commit/ca97dba4531c9b138cd048a6acd48d93cad28a93) | wangq8 |
| 2026-11-24 | [fix(web): target ES2020 in production builds (#22738)](https://github.com/infiniflow/ragflow/commit/c1b807c70ecc2333463102ec121c6d0479d245bc) | jay77721 |
| 2026-11-24 | [Add deepdoc server config (#22737)](https://github.com/infiniflow/ragflow/commit/3b3c40db5fd64273b0cca3f13fc7588051c6111a) | JinHai-CN |
| 2026-11-24 | [feat(parser): import Docling JSON exports (#22728)](https://github.com/infiniflow/ragflow/commit/190e62319f238dc09c4df9fe624efd7fa5c373e9) | BilalAtique |
| 2026-11-24 | [refactor(ingestor): remove unused supportedDocTypes and RegisterSuppo…](https://github.com/infiniflow/ragflow/commit/0cef432bdf94f84f32259affb2b7af858f2243ee) | jay77721 |
| 2026-11-24 | [build: add optional cgo and native-deps extension hooks (#22734)](https://github.com/infiniflow/ragflow/commit/4b6ee0fc2e5762fa3036ee8cfe8634b0f1074e01) | jay77721 |
| 2026-11-24 | [fix(oceanbase): route legacy chunk filters and updates through extra …](https://github.com/infiniflow/ragflow/commit/ad1e2a71316093a37e5ec94aad8015e9e49c3254) | hnwyllmm |
| 2026-11-24 | [Deploy without EXPOSE_X_PORT (#22735)](https://github.com/infiniflow/ragflow/commit/0ee43e8d39756c4681382ac9ba58e720a2e0f2be) | wangq8 |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
