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
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-12-12 |
| 📦 **Latest release** | [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 196.9 MB |
| 🌐 **Website** | https://ragflow.io |

## 📦 Recent releases

### [nightly](https://github.com/infiniflow/ragflow/releases/tag/nightly) _(pre-release)_
<sub>2025-12-01 · 12mo ago</sub>

> Release nightly created from 2c15dfcdaa7637b2503214667a9dd17dc66262f7 at 2026-11-26 13:13:48+00:00

### [v1.0.0](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0)
<sub>2026-11-06 · 20d ago</sub>

> After three release candidates, we are pleased to announce the official release of RAGFlow 1.0, now ready for production. Built on a complete rewrite in Go, this release significantly reduces deployment and runtime overhead and introduces an all-new Agentic Chat experience. We encourage all users to upgrade for improved stability, performance, and question answering.
> **Highlights**
> - Rewritten in Go for lighter deployment: Docker images are approximately 10× smaller, and startup is approximately 10× faster.
> - Approximately 100× greater concurrency, with substantial improvements in query latency, memory usage, and document parsing speed.
> - All-new Agentic Chat: Enables multi-step reasoning and answers to complex questions through iterative retrieval, tool calls, and evidence sufficiency assessment.
> **Chat and Agents**
> …

### [v1.0.0-rc3](https://github.com/infiniflow/ragflow/releases/tag/v1.0.0-rc3)
<sub>2026-10-30 · 27d ago</sub>

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
| 2026-11-26 | [refactor(opensearch): require OpenSearch >= 2.19 and drop legacy fall…](https://github.com/infiniflow/ragflow/commit/625a53ad4c4ecb66abe32b4c0745564eaddeec94) | Sanderhoff-alt |
| 2026-11-26 | [Clean doc (#22872)](https://github.com/infiniflow/ragflow/commit/614622bf8775f304dab2e6f4c5536bf5f3773030) | yingfeng |
| 2026-11-26 | [Feat: RAGFlow desktop (#22697)](https://github.com/infiniflow/ragflow/commit/2c15dfcdaa7637b2503214667a9dd17dc66262f7) | yingfeng |
| 2026-11-26 | [fix(parser): include DOCX header/footer content in parsed output (#22…](https://github.com/infiniflow/ragflow/commit/a9ec65d9418088af96e89ebb8271fcb3d6af3a8f) | jay77721 |
| 2026-11-26 | [Feat: Modify the layout of the version history page within the workfl…](https://github.com/infiniflow/ragflow/commit/41447a3bddfd7d53e6161080ecebf3dde160e672) | cike8899 |
| 2026-11-26 | [Hoist function-local regexp compilation to package-level vars (#22851)](https://github.com/infiniflow/ragflow/commit/4f78a072c55a58c0029b29dc0eef6257d2d5b033) | xugangqiang |
| 2026-11-26 | [fix(ingestion): address the builtin template fs.FS with slash-separat…](https://github.com/infiniflow/ragflow/commit/42673f68c96f34e5eb2ca456eb0fe3d92941b4f1) | DZH166 |
| 2026-11-26 | [fix(ee-sync): list chunks by chunk id prefix, page the dataset versio…](https://github.com/infiniflow/ragflow/commit/1c66920c2fbd22c31d5b99d0909b3a6199c3ad9c) | qinling0210 |
| 2026-11-26 | [Fiix: Modify the layout of the chat channel and MCP pages. (#22856)](https://github.com/infiniflow/ragflow/commit/7dcef5ae0e12dab86ab6968ac72d27719f39c494) | cike8899 |
| 2026-11-26 | [fix(web): keep API documentation controls responsive (#22850)](https://github.com/infiniflow/ragflow/commit/4028bbb6b38f7ad30d8adbfaef88d9c9d42c5ebb) | QAQadws |

[See all commits ↗](https://github.com/infiniflow/ragflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/infiniflow/ragflow.git
```
