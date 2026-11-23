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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 127.3 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2)
<sub>2026-11-21 · yesterday</sub>

> **What's Changed**
> * fix(jina): stop retrying permanent 4xx errors by @Shizoqua in https://github.com/HKUDS/LightRAG/pull/4028
> * fix(pipeline): round-trip sidecar URIs for Windows drive paths by @rtmalikian in https://github.com/HKUDS/LightRAG/pull/4273
> * fix(rerank): stop retrying permanent errors in generic_rerank_api by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/4420
> * fix(query): return the failure shape from aquery_data when no keywords are extracted by @Zhuoxi2000 in https://github.com/HKUDS/LightRAG/pull/4419
> * fix(postgres): give AGE a valid graph name for long or digit-leading workspaces by @zzjiho in https://github.com/HKUDS/LightRAG/pull/4408
> …

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 8d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Merge pull request #4610 from Sanskar1724/fix-table-split-rowspan](https://github.com/HKUDS/LightRAG/commit/1ac49a0c9725cd87dfa95abb11fd83a909d2eb91) | danielaskdd |
| 2026-11-23 | [Merge pull request #4620 from danielaskdd/docs/compress-stargazer-images](https://github.com/HKUDS/LightRAG/commit/07a90f5040f38f5c8e0bc62e2d96906fea0e07aa) | danielaskdd |
| 2026-11-23 | [docs: compress the stargazer affiliation images](https://github.com/HKUDS/LightRAG/commit/6ccc267e1125872b7fd0b4407f87796530c49607) | danielaskdd |
| 2026-11-23 | [Merge pull request #4619 from HKUDS/codex/readme-color-stargazer-caro…](https://github.com/HKUDS/LightRAG/commit/2a45e44fb7f2df19b916153f5bf6d77254dd4eee) | danielaskdd |
| 2026-11-23 | [docs: sync the stargazer carousel into the Japanese and Indonesian RE…](https://github.com/HKUDS/LightRAG/commit/a89d2677dc9d69dfc71793418abfd92197ccc5f4) | danielaskdd |
| 2026-11-23 | [test(chunker): restore the HTML header pipeline test](https://github.com/HKUDS/LightRAG/commit/fde988aecbf6c482376e542f14f08fa671832d75) | danielaskdd |
| 2026-11-23 | [test(chunker): trim the table-split tests and pin three unpinned bran…](https://github.com/HKUDS/LightRAG/commit/8dccd2c57083b28d40138c4766e7df30bfc5837a) | danielaskdd |
| 2026-11-23 | [docs: add the color stargazer affiliation carousel](https://github.com/HKUDS/LightRAG/commit/28a4ede97b5ff44311b2a53581cdded313cd8b62) | LarFii |
| 2026-11-23 | [fix(chunker): read rowspan tables with HTML's tokenizer rules](https://github.com/HKUDS/LightRAG/commit/229fdaa59322673fccf54c56ba7d79e58314332a) | danielaskdd |
| 2026-11-23 | [fix(chunker): require complete tags inside a rowspan table's cells](https://github.com/HKUDS/LightRAG/commit/c9175075686e517ee5e3ce0bdea41a3cd9717eaf) | danielaskdd |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
