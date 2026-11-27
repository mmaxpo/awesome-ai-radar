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
| 🐞 **Open issues + PRs** | [286](https://github.com/HKUDS/LightRAG/issues) |
| 💻 **Languages** | Python 91% · TypeScript 7% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `knowledge-graph` `large-language-models` `retrieval-augmented-generation` `genai` `graphrag` `llm` `rag` `gpt` `docling` `mineru` `ragas` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 126.6 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8)
<sub>2026-11-23 · 3d ago</sub>

> **Important Notes**
> **Highlights**
> **1. Introduces a new storage type: Configuration storage**
> This store holds the key LightRAG configuration. It prepares the ground for gradually moving settings from the .env file into backend storage, and it also lays the foundation for the next step: account and permission management.
> In v1.5.8 configuration storage holds each workspace's **embedding baselines**: for every vector target (entities, relationships, chunks), the embedding space its vectors were written in. **Changing the embedding model on an existing workspace now refuses startup**.
> * **Backends:** `JsonKVStorage`, `PGKVStorage`, `MongoKVStorage` and `OpenSearchKVStorage`, selected with `LIGHTRAG_CONFIG_STORAGE`. Left unset, it follows `LIGHTRAG_KV_STORAGE`, so most deployments need no new setting. `RedisKVStorage` is not admitted, so Redis deployments default to `JsonKVStorage`, with a startup warning.
> …

### [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2)
<sub>2026-11-21 · 5d ago</sub>

> **What's Changed**
> * fix(jina): stop retrying permanent 4xx errors by @Shizoqua in https://github.com/HKUDS/LightRAG/pull/4028
> * fix(pipeline): round-trip sidecar URIs for Windows drive paths by @rtmalikian in https://github.com/HKUDS/LightRAG/pull/4273
> * fix(rerank): stop retrying permanent errors in generic_rerank_api by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/4420
> * fix(query): return the failure shape from aquery_data when no keywords are extracted by @Zhuoxi2000 in https://github.com/HKUDS/LightRAG/pull/4419
> * fix(postgres): give AGE a valid graph name for long or digit-leading workspaces by @zzjiho in https://github.com/HKUDS/LightRAG/pull/4408
> …

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 12d ago</sub>

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
| 2026-11-27 | [Merge pull request #4705 from chuenchen309/fix/bedrock-context-window](https://github.com/HKUDS/LightRAG/commit/47038cf1619b486b5409230aff1e98ba6a6ce5ca) | danielaskdd |
| 2026-11-27 | [Merge pull request #4717 from danielaskdd/test/trim-json-parsing-tests](https://github.com/HKUDS/LightRAG/commit/e3ef8b8b3534dbd75746f8a844ee0284053dab75) | danielaskdd |
| 2026-11-27 | [Merge pull request #4671 from passionworkeer/fix/table-markup-format-…](https://github.com/HKUDS/LightRAG/commit/07b882c47556d8c2da0a4c8fdd57b2e8d95bdfa1) | danielaskdd |
| 2026-11-27 | [Merge pull request #4715 from chuenchen309/fix/nvidia-sdk-retries](https://github.com/HKUDS/LightRAG/commit/8785674eff72977c8d1e793e587af00f9146c245) | danielaskdd |
| 2026-11-27 | [Merge branch 'main' into fix/table-markup-format-boundary](https://github.com/HKUDS/LightRAG/commit/816686caa2c938e229480ddbe617694565fd9055) | passionworkeer |
| 2026-11-27 | [test: pin that json mode none omits response_format entirely](https://github.com/HKUDS/LightRAG/commit/2e5ec172ade0d47eaa0ece1acaaf3878acabe840) | danielaskdd |
| 2026-11-27 | [test(table_markup): fold lookalike cases and trim redundant table cases](https://github.com/HKUDS/LightRAG/commit/b00f6b871801ddc1dd5ba21c141c8684b051d08e) | danielaskdd |
| 2026-11-27 | [test(bedrock): fold empty-response diagnostics and trim redundant tests](https://github.com/HKUDS/LightRAG/commit/40eb12a7c0a6496ec8dfa25d32e8d135176396ea) | danielaskdd |
| 2026-11-27 | [test: trim JSON fence, tolerant-load and keyword parsing tests](https://github.com/HKUDS/LightRAG/commit/7b7ed0e0469335c4af9c856ea4cbaf551b942615) | danielaskdd |
| 2026-11-27 | [Merge pull request #4692 from zhengqiuyang/fix/commonmark-code-fence-…](https://github.com/HKUDS/LightRAG/commit/5dc119f8bd3fadb999e46e4ba0583a59755e4011) | danielaskdd |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
