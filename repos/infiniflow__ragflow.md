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
| 💻 **Languages** | Go 73% · TypeScript 20% · C++ 3% · Python 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `rag` `retrieval-augmented-generation` `agentic-ai` `agentic-retrieval` `agentic-search` `context-management` `knowledge-compilation` `agent-harness` `context-engineering` `harness-engineering` `search-harness` `agent-native-database` `context-engine` `retrieval-harness` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 193.9 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 11mo ago</sub>

> Release nightly created from da4a1556a33b345d0233c2fd4888424cebf9ccfd at 2026-11-23 13:15:13+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 17d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 24d ago</sub>

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
| 2026-11-23 | [fix(service): scope the engine-installed test per build, drop the ite…](https://github.com/infiniflow/ragflow/commit/da4a1556a33b345d0233c2fd4888424cebf9ccfd) | yuzhichang |
| 2026-11-23 | [feat(parser): add parser configuration hooks (#22688)](https://github.com/infiniflow/ragflow/commit/2a1273a3e337f08e9d67fb5ad3b3afabc20d9bb7) | jay77721 |
| 2026-11-23 | [feat(parser): add Nace Document Intelligence as a PDF parser (#22491)](https://github.com/infiniflow/ragflow/commit/391d21d99365eda4fc6ec543d8f4ccaa034e2436) | saruar-dev |
| 2026-11-23 | [fix(parser): keep one JSON value per JSON Lines record (#22660)](https://github.com/infiniflow/ragflow/commit/eb6c95bb66d9e6635cfda7c6cc96158d42c10eb1) | ZKunZhang |
| 2026-11-23 | [fix(parser): keep JSONL records past the scanner line limit (#22622)](https://github.com/infiniflow/ragflow/commit/5acae29a0e83773a26785dafcc64ccce296eeb82) | xinpingzh |
| 2026-11-23 | [fix(parser): preserve MonkeyOCRv2 layout provenance (#22509)](https://github.com/infiniflow/ragflow/commit/f9c6b72ad2cd56339e2565b25c62b8f37a00e2d1) | ZedingZhang |
| 2026-11-23 | [feat(ocr): make PaddleOCR parsing timeout configurable (#22502)](https://github.com/infiniflow/ragflow/commit/a64844c506233d51d72ee28099555804c6ef53da) | thirstyraven |
| 2026-11-23 | [fix(docker): preserve YAML quoting in service configuration (#22659)](https://github.com/infiniflow/ragflow/commit/2d1f7408498de9331b8b23bd3d05c3582efc3de2) | ZKunZhang |
| 2026-11-23 | [fix(agent): route Switch ELSE branch to every end_cpn_ids target (#22…](https://github.com/infiniflow/ragflow/commit/a00aa53cff5eda10f3204d52dfd657148dfac869) | Bensonluo |
| 2026-11-23 | [fix(mcp): reject share-link beta tokens on the MCP endpoints (#22439)](https://github.com/infiniflow/ragflow/commit/17ccdecc4195058249479135bbcc520bade7bdd8) | kongxinjun |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
