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
| 🐞 **Open issues + PRs** | [291](https://github.com/HKUDS/LightRAG/issues) |
| 💻 **Languages** | Python 91% · TypeScript 7% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `knowledge-graph` `large-language-models` `retrieval-augmented-generation` `genai` `graphrag` `llm` `rag` `gpt` `docling` `mineru` `ragas` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 126.5 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8)
<sub>2026-11-23 · 2d ago</sub>

> **Important Notes**
> **Highlights**
> **1. Introduces a new storage type: Configuration storage**
> This store holds the key LightRAG configuration. It prepares the ground for gradually moving settings from the .env file into backend storage, and it also lays the foundation for the next step: account and permission management.
> In v1.5.8 configuration storage holds each workspace's **embedding baselines**: for every vector target (entities, relationships, chunks), the embedding space its vectors were written in. **Changing the embedding model on an existing workspace now refuses startup**.
> * **Backends:** `JsonKVStorage`, `PGKVStorage`, `MongoKVStorage` and `OpenSearchKVStorage`, selected with `LIGHTRAG_CONFIG_STORAGE`. Left unset, it follows `LIGHTRAG_KV_STORAGE`, so most deployments need no new setting. `RedisKVStorage` is not admitted, so Redis deployments default to `JsonKVStorage`, with a startup warning.
> …

### [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2)
<sub>2026-11-21 · 4d ago</sub>

> **What's Changed**
> * fix(jina): stop retrying permanent 4xx errors by @Shizoqua in https://github.com/HKUDS/LightRAG/pull/4028
> * fix(pipeline): round-trip sidecar URIs for Windows drive paths by @rtmalikian in https://github.com/HKUDS/LightRAG/pull/4273
> * fix(rerank): stop retrying permanent errors in generic_rerank_api by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/4420
> * fix(query): return the failure shape from aquery_data when no keywords are extracted by @Zhuoxi2000 in https://github.com/HKUDS/LightRAG/pull/4419
> * fix(postgres): give AGE a valid graph name for long or digit-leading workspaces by @zzjiho in https://github.com/HKUDS/LightRAG/pull/4408
> …

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 11d ago</sub>

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
| 2026-11-26 | [Merge pull request #4686 from kongxinjun/fix/merge-inbound-edges](https://github.com/HKUDS/LightRAG/commit/287fefc85e2d1e739940948ce2a9cb4a0d48f08a) | danielaskdd |
| 2026-11-26 | [Merge pull request #4693 from MohammadHijjawi97/fix/summary-context-p…](https://github.com/HKUDS/LightRAG/commit/886a99719af69f69443c3101f295629ee6c3ed72) | danielaskdd |
| 2026-11-25 | [fix(summary): decide the no-LLM join on the bare texts first](https://github.com/HKUDS/LightRAG/commit/e5a1170b04ca7aa014af259204a3982125b9b742) | danielaskdd |
| 2026-11-25 | [test(graph): keep the populated-row union cases in the merge suite](https://github.com/HKUDS/LightRAG/commit/8a651bfbb195224fb57f997f7fdc9b7e9cfa707a) | danielaskdd |
| 2026-11-25 | [fix(summary): log descriptions trimmed from a summary prompt](https://github.com/HKUDS/LightRAG/commit/7cc5ea8e3298c02c9b12262c5a675575d9277119) | danielaskdd |
| 2026-11-25 | [test(graph): trim the merge chunk-tracking suite](https://github.com/HKUDS/LightRAG/commit/86aa0f0115a4b3417941acf10fcf6b4b774e9471) | danielaskdd |
| 2026-11-25 | [Merge pull request #4658 from HKUDS/dependabot/uv/python-minor-patch-…](https://github.com/HKUDS/LightRAG/commit/2487bbb5a56174a087208c3da69585cf5f33e8a0) | danielaskdd |
| 2026-11-25 | [build(evaluation): require ragas>=0.4.4 instead of capping langchain-…](https://github.com/HKUDS/LightRAG/commit/61bac8086e82adbae2564930297336abcde501fd) | danielaskdd |
| 2026-11-25 | [test(graph): fold the edge-direction merge test into the tracking suite](https://github.com/HKUDS/LightRAG/commit/333e4a553c40648e12e5e0dd8c686ad5eb926c5a) | danielaskdd |
| 2026-11-25 | [fix(summary): size summary groups by the prompt's JSON lines](https://github.com/HKUDS/LightRAG/commit/c54eae0e36dc1babfbacf67577831182dea50f59) | MohammadHijjawi97 |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
