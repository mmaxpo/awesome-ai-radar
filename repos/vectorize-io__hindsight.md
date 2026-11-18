# vectorize-io/hindsight

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/vectorize-io/hindsight)

> Hindsight: Agent Memory That Learns

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Memory system for AI agents |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 61.8k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [261](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 70% · TypeScript 17% · MDX 9% · Rust 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 828.6 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 7d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 15d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.1.0 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5935
> * docs(blog): ChatGPT sign-in recording in the v1.1.0 post by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5939
> * fix(parsers): strip UTF-8 byte-order mark in markitdown text files by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5949
> * fix(embeddings): don't fail the call when the provider omits prompt_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5951
> * fix(reflect): treat a non-list id field on done as empty instead of failing the reflect by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5952
> …

### [v1.1.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.1.0)
<sub>2026-10-21 · 27d ago</sub>

> **What's Changed**
> * docs: v1.0.0 changelog, Memlake launch post, and version-1.0 docs snapshot by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5550
> * fix(client): stop the export poll loop from overrunning its timeout on Windows by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5568
> * feat/webhook event delivery ids by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5576
> * feat(control-plane): identify dataplane requests with its own User-Agent by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5536
> * feat(extensions): LLM request extension — choose the LLM and credentials of each call server-side by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5578
> …

### [v1.0.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.0.0)
<sub>2026-10-13 · 1mo ago</sub>

> **What's Changed**
> * fix(docs): overview hero reaches the window edges on wide screens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5440
> * docs: changelog and blog post for v0.10.3 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5435
> * docs: fix the home page link preview by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5441
> * docs(blog): plain post titles with a description subtitle and byline row by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5460
> * fix(ui): hide the no-op '+field' button at the entity-label root level by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/5450
> …

### [v0.10.3](https://github.com/vectorize-io/hindsight/releases/tag/v0.10.3)
<sub>2026-10-08 · 1mo ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v0.10.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/4915
> * fix(coding-agents): hold the deepen lock with a heartbeat, not a 30-minute TTL by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/4920
> * feat(coding-agents): treat memory as a past record, and let teams add their own guidance (#4791) by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/4922
> * feat(coding-agents): add TraeCode (TRAE CN) harness by @cq-guojia in https://github.com/vectorize-io/hindsight/pull/4535
> * fix(coding-agents): filter non-conversation Codex content by @gfreschi in https://github.com/vectorize-io/hindsight/pull/4688
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [perf(local): drop the per-call gc.collect() on GPU inference (#6648)](https://github.com/vectorize-io/hindsight/commit/082822aa0bcfa069f3bffc8cef79480ce79e7c02) | nicoloboschi |
| 2026-11-18 | [refactor(operations): a job's bank comes from its queue row; restored…](https://github.com/vectorize-io/hindsight/commit/3a0fc72717790be8c739252596453ba72b228358) | nicoloboschi |
| 2026-11-18 | [fix(reflect): place a new section after another new one by its headin…](https://github.com/vectorize-io/hindsight/commit/f85e2475ca821ef93737926f348cc6ecf3960f9c) | nicoloboschi |
| 2026-11-18 | [fix(llm): merge configured extra-body objects instead of replacing th…](https://github.com/vectorize-io/hindsight/commit/7430349142da1007c1fe34d1f61412211c4e584b) | nicoloboschi |
| 2026-11-18 | [fix(retain): retry the completion outbox write when the store sheds i…](https://github.com/vectorize-io/hindsight/commit/f6038a742743243c2df4a90b5b0542715f320359) | nicoloboschi |
| 2026-11-18 | [feat(knowledge): rerank knowledge-bank search with the decision model…](https://github.com/vectorize-io/hindsight/commit/0e9c72c86aa650b282af4f93f8eda6e0b672b70e) | nicoloboschi |
| 2026-11-17 | [Knowledge-bank per-document content-token count for metering (#6616)](https://github.com/vectorize-io/hindsight/commit/9fb28dbd724dc1ce4da7cb4c49008e601db76c5f) | benfrank241 |
| 2026-11-17 | [Index a newly created page after the create answers (#6628)](https://github.com/vectorize-io/hindsight/commit/b5f5968ebf2a7dbe6363809fac0b31e428008171) | nicoloboschi |
| 2026-11-17 | [feat(kb): decision model sees knowledge-bank pictures; knowledge-bank…](https://github.com/vectorize-io/hindsight/commit/4ff0362f00169b054c429499e31453bd3bdb6b4a) | nicoloboschi |
| 2026-11-17 | [fix(tracing): a timed-out retried attempt and a cancelled LLM call ea…](https://github.com/vectorize-io/hindsight/commit/cf3616b36a8c3a48cf3e9d102febdc7dddc119a0) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
