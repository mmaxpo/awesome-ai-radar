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
| ⭐ **Stars** | 40.9k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [279](https://github.com/HKUDS/LightRAG/issues) |
| 💻 **Languages** | Python 91% · TypeScript 7% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `knowledge-graph` `large-language-models` `retrieval-augmented-generation` `genai` `graphrag` `llm` `rag` `gpt` `docling` `mineru` `ragas` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 127.9 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8)
<sub>2026-11-23 · yesterday</sub>

> **Important Notes**
> **Highlights**
> **1. Introduces a new storage type: Configuration storage**
> This store holds the key LightRAG configuration. It prepares the ground for gradually moving settings from the .env file into backend storage, and it also lays the foundation for the next step: account and permission management.
> In v1.5.8 configuration storage holds each workspace's **embedding baselines**: for every vector target (entities, relationships, chunks), the embedding space its vectors were written in. **Changing the embedding model on an existing workspace now refuses startup**.
> * **Backends:** `JsonKVStorage`, `PGKVStorage`, `MongoKVStorage` and `OpenSearchKVStorage`, selected with `LIGHTRAG_CONFIG_STORAGE`. Left unset, it follows `LIGHTRAG_KV_STORAGE`, so most deployments need no new setting. `RedisKVStorage` is not admitted, so Redis deployments default to `JsonKVStorage`, with a startup warning.
> …

### [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2)
<sub>2026-11-21 · 3d ago</sub>

> **What's Changed**
> * fix(jina): stop retrying permanent 4xx errors by @Shizoqua in https://github.com/HKUDS/LightRAG/pull/4028
> * fix(pipeline): round-trip sidecar URIs for Windows drive paths by @rtmalikian in https://github.com/HKUDS/LightRAG/pull/4273
> * fix(rerank): stop retrying permanent errors in generic_rerank_api by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/4420
> * fix(query): return the failure shape from aquery_data when no keywords are extracted by @Zhuoxi2000 in https://github.com/HKUDS/LightRAG/pull/4419
> * fix(postgres): give AGE a valid graph name for long or digit-leading workspaces by @zzjiho in https://github.com/HKUDS/LightRAG/pull/4408
> …

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 10d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Merge pull request #4691 from danielaskdd/feat/setup-voyageai-embedding](https://github.com/HKUDS/LightRAG/commit/64fc6cb3c510ebfca61da4ddcdeb9d94dad55ccf) | danielaskdd |
| 2026-11-25 | [feat(voyageai): honor EMBEDDING_BINDING_HOST as the VoyageAI endpoint](https://github.com/HKUDS/LightRAG/commit/86e223d2ab07a905dc492d05aa0a507e27211089) | danielaskdd |
| 2026-11-25 | [feat(setup): offer VoyageAI as an embedding provider in the wizard](https://github.com/HKUDS/LightRAG/commit/37eb760a31c27495c030740ddb2603e9f1bdc21e) | danielaskdd |
| 2026-11-24 | [Merge pull request #4642 from shadowinlife/perf/query-fitter-token-memo](https://github.com/HKUDS/LightRAG/commit/cf82ba9f1e516c5c9ba95a6c5adfb60489e0ce59) | danielaskdd |
| 2026-11-24 | [Merge pull request #4643 from kabishou11/fix/cross-provider-role-host…](https://github.com/HKUDS/LightRAG/commit/512345ec4bd706ab228c7eab25ade600d3e9f031) | danielaskdd |
| 2026-11-24 | [Merge pull request #4646 from leninworld/fix/embedding-base64-neo4j-k…](https://github.com/HKUDS/LightRAG/commit/db8cb33a3164835d72d9423f50b72cc4d294940a) | danielaskdd |
| 2026-11-24 | [test(operate): import the budget helpers from their new module path](https://github.com/HKUDS/LightRAG/commit/43fd41689bd574c765607bd687bb6641036af39a) | danielaskdd |
| 2026-11-24 | [test: move the Neo4j keep_alive parsing test into its own module](https://github.com/HKUDS/LightRAG/commit/0158c9f1524552b0de3d20745f5cd17df689bac0) | danielaskdd |
| 2026-11-24 | [fix(api): warn when a cross-provider role falls back to its default host](https://github.com/HKUDS/LightRAG/commit/a2d865a2dd67c535b8bd5073ae2c6dfa0c3c1b66) | danielaskdd |
| 2026-11-24 | [test(operate): move the total-budget fitter suites to tests/operate](https://github.com/HKUDS/LightRAG/commit/0acdca6610ada2ffdada525ecdf43203def9db34) | danielaskdd |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
