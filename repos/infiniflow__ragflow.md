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
| ⭐ **Stars** | 94.7k |
| 🍴 **Forks** | 11.4k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/infiniflow/ragflow/issues) |
| 💻 **Languages** | Go 73% · TypeScript 20% · C++ 3% · Python 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `rag` `retrieval-augmented-generation` `agentic-ai` `agentic-retrieval` `agentic-search` `context-management` `knowledge-compilation` `agent-harness` `context-engineering` `harness-engineering` `search-harness` `agent-native-database` `context-engine` `retrieval-harness` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 194.8 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 11mo ago</sub>

> Release nightly created from bb7b3c28888c21e1610678d3d7b8c2094265a644 at 2026-11-25 13:16:01+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 19d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 26d ago</sub>

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
| 2026-11-25 | [fix(chunker): skip a header-only table in the general media context (…](https://github.com/infiniflow/ragflow/commit/bb7b3c28888c21e1610678d3d7b8c2094265a644) | ccclucky |
| 2026-11-25 | [Cut redundant metadata and storage round trips in hot paths (#22791)](https://github.com/infiniflow/ragflow/commit/22ea6f46d095516a5debd07713d1624b50c5c56f) | xugangqiang |
| 2026-11-25 | [fix(dataset): support parsing error label overlays (#22801)](https://github.com/infiniflow/ragflow/commit/dcb941398a1eccb2e42c8a5c650c5e5517e40d6b) | 6ba3i |
| 2026-11-25 | [Revert "Fix ingestion pipeline no create from template" (#22800) Reve…](https://github.com/infiniflow/ragflow/commit/2e06609a7b53da96181bb97b5c6475081762e4e2) | wangq8 |
| 2026-11-25 | [Batch dataset authorization and metadata lookups to remove N+1 querie…](https://github.com/infiniflow/ragflow/commit/915373e685cc5668b5a53da8cb44cff07209f6d3) | xugangqiang |
| 2026-11-25 | [fix(web): use provider name for instance model queries (#22799)](https://github.com/infiniflow/ragflow/commit/2cafb363c219c6ed498bf3fcab06145f62bc144b) | dcc123456 |
| 2026-11-25 | [fix(parser): retry transient SoMark poll failures and pin the status …](https://github.com/infiniflow/ragflow/commit/9c84b712b1084afe10659e6e329b5b9816ab4418) | lemonzoey |
| 2026-11-25 | [fix(wiki): honor saved extraction guidance (#22384)](https://github.com/infiniflow/ragflow/commit/a572e095e0ddfad4ef2d19a5eccff0f92356e498) | linkangjun |
| 2026-11-25 | [Fix ingestion pipeline no create from template (#22797)](https://github.com/infiniflow/ragflow/commit/302fa276436c00516e1edc060c48b4991328344c) | wangq8 |
| 2026-11-25 | [feat(agent): expose execution lifecycle hooks (#22792)](https://github.com/infiniflow/ragflow/commit/796e5fda9cf651e3d6847813783a66d7ff63a83f) | 6ba3i |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
