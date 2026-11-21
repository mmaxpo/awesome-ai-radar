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
| ⭐ **Stars** | 62.4k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [242](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 70% · TypeScript 17% · MDX 9% · Rust 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 835.1 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3)
<sub>2026-11-19 · yesterday</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.2.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6678
> * fix(knowledge): ingest odd, broken and big files without failing, retrying or running out of memory by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6701
> * Fix broken 'What is Hindsight?' demo video in README by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6702
> * Use descriptive filename for the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6706
> * Update the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6708
> …

### [v1.2.2](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.2)
<sub>2026-11-19 · yesterday</sub>

> **What's Changed**
> * test(llm): fix the two-user-turns tests broken by the tool-call retry by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6492
> * docs: changelog and blog post for v1.2.1 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6486
> * feat(knowledge-banks): multimodal document banks, hidden behind a feature flag by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6478
> * fix(api): answer 422, not 500, when the LLM provider refuses the content by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6501
> * fix(consolidation): stop the misses gemma-4 made on 1.2.1, and the judge errors that hid them by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6505
> …

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 11d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 18d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.1.0 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5935
> * docs(blog): ChatGPT sign-in recording in the v1.1.0 post by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5939
> * fix(parsers): strip UTF-8 byte-order mark in markitdown text files by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5949
> * fix(embeddings): don't fail the call when the provider omits prompt_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5951
> * fix(reflect): treat a non-list id field on done as empty instead of failing the reflect by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5952
> …

### [v1.1.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.1.0)
<sub>2026-10-21 · 1mo ago</sub>

> **What's Changed**
> * docs: v1.0.0 changelog, Memlake launch post, and version-1.0 docs snapshot by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5550
> * fix(client): stop the export poll loop from overrunning its timeout on Windows by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5568
> * feat/webhook event delivery ids by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5576
> * feat(control-plane): identify dataplane requests with its own User-Agent by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5536
> * feat(extensions): LLM request extension — choose the LLM and credentials of each call server-side by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5578
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(knowledge): PDF calls queued when the pool is killed are retried,…](https://github.com/vectorize-io/hindsight/commit/62a03bfc96f175e9ac155acc72f292bed9ac4449) | nicoloboschi |
| 2026-11-20 | [fix(kb): a PDF page is its own document in the rerank; drop the page …](https://github.com/vectorize-io/hindsight/commit/80bd005fc2be5c9604a1a0c9741ea93d5ac85156) | nicoloboschi |
| 2026-11-20 | [perf(kb): time knowledge search by part, and let its vector searches …](https://github.com/vectorize-io/hindsight/commit/1ee4d90a25898afb9cb04f65e3fe8512d4759227) | nicoloboschi |
| 2026-11-20 | [fix(llm): share LLM slots fairly across tenants, banks and documents …](https://github.com/vectorize-io/hindsight/commit/7f225b52134497fb02677f1950cd103ebc780226) | nicoloboschi |
| 2026-11-20 | [fix(knowledge): a spreadsheet declaring millions of cells is read cel…](https://github.com/vectorize-io/hindsight/commit/cc963640ddae0db438ab13f403a3efa8f76ea5e0) | nicoloboschi |
| 2026-11-20 | [fix(knowledge): a cut-off video is not refused for its header's lengt…](https://github.com/vectorize-io/hindsight/commit/59ec0f0c42e1df050dd8bc1185921febd71112b1) | nicoloboschi |
| 2026-11-20 | [feat(kb): a knowledge search can skip the reranker (enable_reranking:…](https://github.com/vectorize-io/hindsight/commit/732f35e2dc5d25427e21b391959b114ae24a8d02) | nicoloboschi |
| 2026-11-20 | [test(system-evals): the knowledge edge-case sample moves to hindsight…](https://github.com/vectorize-io/hindsight/commit/ae3c142e88e5b792be11bbb07cf46ca31ffa8e23) | nicoloboschi |
| 2026-11-20 | [fix(llm): repair malformed JSON from the raw text, not the newline-es…](https://github.com/vectorize-io/hindsight/commit/385f2d232eeac13b8a23890ee4be806eb588b01b) | nicoloboschi |
| 2026-11-20 | [fix(knowledge): an Office worker converts every file with one convert…](https://github.com/vectorize-io/hindsight/commit/797c5cfe298b507efb135af3b2282261a475fdf1) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
