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
| ⭐ **Stars** | 63.6k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [148](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 69% · TypeScript 16% · MDX 11% · Rust 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.5 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0)
<sub>2026-11-24 · 2d ago</sub>

> **What's Changed**
> * docs: changelog for v1.2.3 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6714
> * fix(release): slim image no longer overwrites :latest by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6728
> * feat(mcp): per-bank MCP server instructions in the initialize response by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6712
> * docs: replace retired Claude Code plugin text and dead integration link in blog and guides by @chrislatimer in https://github.com/vectorize-io/hindsight/pull/6716
> * fix(knowledge): bound the work of cutting a video, and drop files that fail for good by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6711
> …

### [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3)
<sub>2026-11-19 · 6d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.2.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6678
> * fix(knowledge): ingest odd, broken and big files without failing, retrying or running out of memory by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6701
> * Fix broken 'What is Hindsight?' demo video in README by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6702
> * Use descriptive filename for the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6706
> * Update the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6708
> …

### [v1.2.2](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.2)
<sub>2026-11-19 · 6d ago</sub>

> **What's Changed**
> * test(llm): fix the two-user-turns tests broken by the tool-call retry by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6492
> * docs: changelog and blog post for v1.2.1 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6486
> * feat(knowledge-banks): multimodal document banks, hidden behind a feature flag by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6478
> * fix(api): answer 422, not 500, when the LLM provider refuses the content by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6501
> * fix(consolidation): stop the misses gemma-4 made on 1.2.1, and the judge errors that hid them by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6505
> …

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 16d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 23d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.1.0 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5935
> * docs(blog): ChatGPT sign-in recording in the v1.1.0 post by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5939
> * fix(parsers): strip UTF-8 byte-order mark in markitdown text files by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5949
> * fix(embeddings): don't fail the call when the provider omits prompt_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5951
> * fix(reflect): treat a non-list id field on done as empty instead of failing the reflect by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/5952
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [docs(blog): what's new in the Hindsight Hermes plugin 2.0.0 (#6925)](https://github.com/vectorize-io/hindsight/commit/47831d5c39010a5c30e9ac2aa16145f7048e930f) | nicoloboschi |
| 2026-11-26 | [release(hermes): v2.0.0](https://github.com/vectorize-io/hindsight/commit/0aca9f80ec87237756c445ac27bf9e5affdc67fe) | nicoloboschi |
| 2026-11-26 | [fix(knowledge): audio/video ingest works with PyAV 19 (#6921) (#6947)](https://github.com/vectorize-io/hindsight/commit/720ba345437a8c434084c46b1c623e27e4cfec80) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): support Prime Agent 0.10+ (Rust rewrite), drop 0.…](https://github.com/vectorize-io/hindsight/commit/22cff88f1e64feea8bae90249fc5a8df88ae0413) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): injected text follows the config and stops repeat…](https://github.com/vectorize-io/hindsight/commit/e09735ad0d1a6aff59386169d662b0d3b70db95b) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): inject Antigravity recall as systemMessage, not d…](https://github.com/vectorize-io/hindsight/commit/53e0f48a6707c90e2f2ab542a29de42c7fa0c998) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): Bun-hosted plugin fixes — write-back after compac…](https://github.com/vectorize-io/hindsight/commit/b77a1453986c4a06f031e957489b26c97bd3674b) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): a forked Claude Code session no longer re-saves i…](https://github.com/vectorize-io/hindsight/commit/937cacc48cffd58219ae235690cc3f75c5e4c66d) | nicoloboschi |
| 2026-11-26 | [feat(system-evals): Hermes evals — a real Hermes Agent, every default…](https://github.com/vectorize-io/hindsight/commit/93deb09396471f384f5f48befcfc04c2ff3ea70b) | nicoloboschi |
| 2026-11-26 | [fix(coding-agents): Codex reader memory, Kimi session index, DSH v4 i…](https://github.com/vectorize-io/hindsight/commit/63d08b0cc571305eb0ccc9d8e1d17694fa54ac36) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
