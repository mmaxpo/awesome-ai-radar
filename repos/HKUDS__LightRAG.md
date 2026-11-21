# HKUDS/LightRAG

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/HKUDS/LightRAG)

> [EMNLP2025] LightRAG: Simple and Fast Retrieval-Augmented Generation

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Simple, fast graph-based RAG |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 40.8k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [236](https://github.com/HKUDS/LightRAG/issues) |
| 💻 **Languages** | Python 91% · TypeScript 7% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `knowledge-graph` `large-language-models` `retrieval-augmented-generation` `genai` `graphrag` `llm` `rag` `gpt` `docling` `mineru` `ragas` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 123.9 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 6d ago</sub>

> **Important Notes**
> > v1.5.8rc1 is a release candidate. Please test it on a copy of your data before upgrading production.
> **Highlights**
> **1. Configuration storage: LightRAG now remembers which embedding model built your vectors**
> In earlier releases, changing `EMBEDDING_MODEL` or `EMBEDDING_DIM` on an existing deployment failed silently. Depending on the backend, LightRAG either kept the old vectors and returned wrong neighbours, or opened a new, empty vector container (Milvus / Qdrant / PostgreSQL) and served a knowledge graph with no vectors at all.
> v1.5.8 adds a **configuration storage**. It is a small KV namespace (`config`) that holds each workspace's **embedding baselines**: for every vector target (entities, relationships, chunks), the embedding space its vectors were written in. Startup checks the baselines against the current embedding configuration. If the space has changed, the server **refuses to start** and names the target and the way out, instead of serving bad results.
> …

### [v1.5.7](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7)
<sub>2026-09-02 · 2mo ago</sub>

> **Important Notes**
> **New Feature: Add end-user-facing entry point to WebUI**
> v1.5.7 adds a second, end-user-facing entry — `/workspace` — together with the **branding** and **prompt controls** a deployment needs before it can be handed to real users.
> * A query-only entry for end users: `/workspace`
> * Customizable welcome, login and empty-state pages
> * A global `USER_PROMPT_PREFIX`
> …

### [v1.5.7rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7rc2)
<sub>2026-08-19 · 3mo ago</sub>

> **What's New**
> * Add an offline tool to migrate a graph from Apache AGE to PostgreSQL tables by @ysys143 in https://github.com/HKUDS/LightRAG/pull/3620
> * feat: support graph-first ingestion with deferred vector indexing by @letsgetai in https://github.com/HKUDS/LightRAG/pull/3473
> * feat: add explicit custom chunking selector by @er-s-an in https://github.com/HKUDS/LightRAG/pull/3665
> * feat(api): add ENABLE_API_DOCS switch for API documentation exposure by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/3672
> **What's Changed**
> …

### [v1.5.7rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.7rc1) _(pre-release)_
<sub>2026-08-17 · 3mo ago</sub>

> **What's New**
> * Add an offline tool to migrate a graph from Apache AGE to PostgreSQL tables by @ysys143 in https://github.com/HKUDS/LightRAG/pull/3620
> * feat: support graph-first ingestion with deferred vector indexing by @letsgetai in https://github.com/HKUDS/LightRAG/pull/3473
> **What's Changed**
> * fix(kg): return copies from NetworkXStorage get_node and get_edge by @santhreal in https://github.com/HKUDS/LightRAG/pull/3588
> * fix(operate): compute most common entity type and normalize keywords on rebuild by @santhreal in https://github.com/HKUDS/LightRAG/pull/3589
> …

### [v1.5.6](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.6)
<sub>2026-08-06 · 3mo ago</sub>

> **Important Notes**
> Introducing **PGTableGraphStorage**, a new graph storage backend built on native PostgreSQL tables. By eliminating the dependency on Apache AGE, it not only simplifies deployment but also delivers significantly higher graph storage performance with reduced storage footprint. It will replace the AGE-based `PGGraphStorage` as the preferred graph storage solution for PostgreSQL. This makes **PostgreSQL** the go-to **all-in-one backend database** for LightRAG, enabling a single database to cover all four storage types.
> **What's New**
> * feat(kg): add PGTableGraphStorage — PostgreSQL-native graph backend (no AGE dependency) by @ysys143 in https://github.com/HKUDS/LightRAG/pull/3103
> * docs(pipeline): rewrite the dedup and concurrency chapters from a user's view by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/3583
> **What's Changed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [Merge pull request #4533 from danielaskdd/test/trim-aiohttp-retry-cases](https://github.com/HKUDS/LightRAG/commit/510be78afa81bbaeea9d31f3f72d645f4637d70a) | danielaskdd |
| 2026-11-21 | [test(retry): keep one status row per branch of the 5xx threshold](https://github.com/HKUDS/LightRAG/commit/e33ce719b5c9d7165efebad46803b734dbf61f7a) | danielaskdd |
| 2026-11-21 | [test(retry): pin the aiohttp retry table once, one wiring case per br…](https://github.com/HKUDS/LightRAG/commit/cf5cbad5de3b60117c8d4c35a3601d39ffc0f047) | danielaskdd |
| 2026-11-21 | [Merge pull request #4532 from Ymmcc/fix/jina-embedding-index-order](https://github.com/HKUDS/LightRAG/commit/2112670c9fcd4a93aa8fc1d0c7be44c3dd16dafa) | danielaskdd |
| 2026-11-21 | [test(jina): trim redundant index-order cases; name bad indices in the…](https://github.com/HKUDS/LightRAG/commit/015646d26045835c382f61dcc7118a668e37ce23) | danielaskdd |
| 2026-11-21 | [Merge pull request #4524 from wToTw123/codex/1120-partial-token-usage](https://github.com/HKUDS/LightRAG/commit/9fcb413d098fd7cdd2b8f6a823433584d4426584) | danielaskdd |
| 2026-11-21 | [fix(llm): normalize nullable Gemini usage counts at the binding](https://github.com/HKUDS/LightRAG/commit/d35fd394ed7803fc24ca100e6df008cbc3d37f37) | danielaskdd |
| 2026-11-21 | [Merge pull request #4526 from chuenchen309/fix/md-display-math-with-p…](https://github.com/HKUDS/LightRAG/commit/2ddb0c4104168556a26cb0e8a662695b00c5c5ac) | danielaskdd |
| 2026-11-21 | [Merge pull request #4531 from SDLSY/fix/kg-chunk-pick-method-validati…](https://github.com/HKUDS/LightRAG/commit/8fa35260b158759737196b1e2545c9c0b2916489) | danielaskdd |
| 2026-11-21 | [Merge pull request #4529 from Zhuoxi2000/fix-query-keywords-metadata-…](https://github.com/HKUDS/LightRAG/commit/eca4d7689e374fddb9f9bd20b8e2079433c9d9e1) | danielaskdd |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
