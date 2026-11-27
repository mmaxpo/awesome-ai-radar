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
| ⭐ **Stars** | 94.8k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/infiniflow/ragflow/issues) |
| 💻 **Languages** | Go 73% · TypeScript 20% · C++ 3% · Python 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `rag` `retrieval-augmented-generation` `agentic-ai` `agentic-retrieval` `agentic-search` `context-management` `knowledge-compilation` `agent-harness` `context-engineering` `harness-engineering` `search-harness` `agent-native-database` `context-engine` `retrieval-harness` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 197.2 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 12mo ago</sub>

> Release nightly created from 70ed4c95d7eb4af7d893da7d340a4a02550a3b50 at 2026-11-27 13:11:41+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 21d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 28d ago</sub>

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
| 2026-11-27 | [refactor login command (#22927)](https://github.com/infiniflow/ragflow/commit/70ed4c95d7eb4af7d893da7d340a4a02550a3b50) | JinHai-CN |
| 2026-11-27 | [remove local file parse command (#22925)](https://github.com/infiniflow/ragflow/commit/b1b1c5bd7fd7d773672fb7a9e863b6d79b68c42e) | JinHai-CN |
| 2026-11-27 | [fix(title-chunker): reject zero chunk token cap (#22915)](https://github.com/infiniflow/ragflow/commit/b757eaa767c2b6dcb1b45dccccbaeb0aa3bd95f3) | jay77721 |
| 2026-11-27 | [fix: enforce permissions for compilation resources (#22922)](https://github.com/infiniflow/ragflow/commit/0976cf30e495f819826234a24525796e7619411a) | buua436 |
| 2026-11-27 | [Feat: Adjust the layout of the document pages (#22916)](https://github.com/infiniflow/ragflow/commit/7f89bafec4e49fbcc8c3536a9a83ba821e4d13c7) | cike8899 |
| 2026-11-27 | [Fix: failover and cascade for rerank model (#22918)](https://github.com/infiniflow/ragflow/commit/b0398e80287d24b30dcc258d820f1bc3b8409fdb) | Lynn-Inf |
| 2026-11-27 | [fix(dao): preserve stored MySQL datetime precision during auto-migrat…](https://github.com/infiniflow/ragflow/commit/9426df95cf6b82ef5494b9c5e8cf036ab7efdebf) | QAQadws |
| 2026-11-27 | [sensitive word filtering - stub (#22901)](https://github.com/infiniflow/ragflow/commit/cb130032b3544b0fb00129fc95999674bd708ca9) | wangq8 |
| 2026-11-27 | [fix(ingestion): keep every operator in dataflow debug logs (#22904)](https://github.com/infiniflow/ragflow/commit/a56c359eb78484fb5dd3fb8cf5de0015dad15b3a) | jay77721 |
| 2026-11-27 | [Feat: The creation time and file size are displayed in the bottom-lef…](https://github.com/infiniflow/ragflow/commit/cb3c5efdf0f4cf0a976bc510170dae249526813e) | cike8899 |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
