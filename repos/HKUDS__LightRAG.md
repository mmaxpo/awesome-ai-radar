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
| 🐞 **Open issues + PRs** | [245](https://github.com/HKUDS/LightRAG/issues) |
| 💻 **Languages** | Python 91% · TypeScript 7% · Shell 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `knowledge-graph` `large-language-models` `retrieval-augmented-generation` `genai` `graphrag` `llm` `rag` `gpt` `docling` `mineru` `ragas` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2024-10-02 |
| 📦 **Latest release** | [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 124.9 MB |
| 🌐 **Website** | https://arxiv.org/abs/2410.05779 |

## 📦 Recent releases

### [v1.5.8rc2](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc2)
<sub>2026-11-21 · today</sub>

> **What's Changed**
> * fix(jina): stop retrying permanent 4xx errors by @Shizoqua in https://github.com/HKUDS/LightRAG/pull/4028
> * fix(pipeline): round-trip sidecar URIs for Windows drive paths by @rtmalikian in https://github.com/HKUDS/LightRAG/pull/4273
> * fix(rerank): stop retrying permanent errors in generic_rerank_api by @danielaskdd in https://github.com/HKUDS/LightRAG/pull/4420
> * fix(query): return the failure shape from aquery_data when no keywords are extracted by @Zhuoxi2000 in https://github.com/HKUDS/LightRAG/pull/4419
> * fix(postgres): give AGE a valid graph name for long or digit-leading workspaces by @zzjiho in https://github.com/HKUDS/LightRAG/pull/4408
> …

### [v1.5.8rc1](https://github.com/HKUDS/LightRAG/releases/tag/v1.5.8rc1)
<sub>2026-11-15 · 7d ago</sub>

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
| 2026-11-22 | [Merge pull request #4593 from danielaskdd/ci/pg-smoke-paths](https://github.com/HKUDS/LightRAG/commit/b0859bafaf247b4929f0d2be608178da6baaa40c) | danielaskdd |
| 2026-11-22 | [ci: trigger PostgreSQL smoke tests on every module they exercise](https://github.com/HKUDS/LightRAG/commit/4e76157f086d28b49d0b9729a0c27abf34ab6291) | danielaskdd |
| 2026-11-22 | [Merge pull request #4549 from MohammadHijjawi97/fix/export-markdown-e…](https://github.com/HKUDS/LightRAG/commit/c5cc0b22677d0f77753464efa8ddf1b5ef07748d) | danielaskdd |
| 2026-11-22 | [fix(export): narrow the Markdown cell rewrite to pipes and line breaks](https://github.com/HKUDS/LightRAG/commit/adde9cd39e8a4e37bc133bfbfb84f0b0ccd21e2f) | danielaskdd |
| 2026-11-22 | [fix(export): render Markdown cells as literal text](https://github.com/HKUDS/LightRAG/commit/74691beedb43db5f55d9d98810a837131ee98422) | danielaskdd |
| 2026-11-22 | [fix(export): escape `<` in Markdown cells and cover every table](https://github.com/HKUDS/LightRAG/commit/49c34e6a1beae72a9f883c19b644179aba02e8c4) | danielaskdd |
| 2026-11-22 | [Merge pull request #4592 from danielaskdd/docs/test-guide-lessons](https://github.com/HKUDS/LightRAG/commit/24451381a15fb1d19221669b6aa6fdedb255574c) | danielaskdd |
| 2026-11-22 | [docs: fold the test-trim lessons into the testing guides](https://github.com/HKUDS/LightRAG/commit/a0d3493c0b42476a8245d030ed7ca88dd110f180) | danielaskdd |
| 2026-11-22 | [Merge pull request #4590 from danielaskdd/test/d2-setup](https://github.com/HKUDS/LightRAG/commit/5611581edfae716ca14c34acec87f9572e7e4ef1) | danielaskdd |
| 2026-11-22 | [Merge pull request #4591 from danielaskdd/test/d3-webui](https://github.com/HKUDS/LightRAG/commit/df987a1de8f4193efd81ee31e3801f26545f4f14) | danielaskdd |

[See all commits ↗](https://github.com/HKUDS/LightRAG/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/LightRAG.git
```
