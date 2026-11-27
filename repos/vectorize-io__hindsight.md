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
| ⭐ **Stars** | 63.8k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [145](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 68% · TypeScript 17% · MDX 11% · Rust 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 844.4 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0)
<sub>2026-11-24 · 3d ago</sub>

> **What's Changed**
> * docs: changelog for v1.2.3 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6714
> * fix(release): slim image no longer overwrites :latest by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6728
> * feat(mcp): per-bank MCP server instructions in the initialize response by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6712
> * docs: replace retired Claude Code plugin text and dead integration link in blog and guides by @chrislatimer in https://github.com/vectorize-io/hindsight/pull/6716
> * fix(knowledge): bound the work of cutting a video, and drop files that fail for good by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6711
> …

### [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3)
<sub>2026-11-19 · 7d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.2.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6678
> * fix(knowledge): ingest odd, broken and big files without failing, retrying or running out of memory by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6701
> * Fix broken 'What is Hindsight?' demo video in README by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6702
> * Use descriptive filename for the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6706
> * Update the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6708
> …

### [v1.2.2](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.2)
<sub>2026-11-19 · 7d ago</sub>

> **What's Changed**
> * test(llm): fix the two-user-turns tests broken by the tool-call retry by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6492
> * docs: changelog and blog post for v1.2.1 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6486
> * feat(knowledge-banks): multimodal document banks, hidden behind a feature flag by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6478
> * fix(api): answer 422, not 500, when the LLM provider refuses the content by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6501
> * fix(consolidation): stop the misses gemma-4 made on 1.2.1, and the judge errors that hid them by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6505
> …

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 17d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 24d ago</sub>

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
| 2026-11-27 | [fix(coding-agents): a capture without a page id updates the same-titl…](https://github.com/vectorize-io/hindsight/commit/18ee7d2c83d74933bef0574faa574c071c924841) | nicoloboschi |
| 2026-11-27 | [fix(coding-agents): list pages without the server's staleness scan (#…](https://github.com/vectorize-io/hindsight/commit/8fcedf86eaad658dcff177899c501a719887619f) | nicoloboschi |
| 2026-11-27 | [feat(api): detail=basic skips the staleness check on page tree and me…](https://github.com/vectorize-io/hindsight/commit/3e2fd7cfd9ff61d1db575e11f8126c3ebe03f6eb) | nicoloboschi |
| 2026-11-27 | [feat(control-plane): Hindsight Wrapped 2026, a year across every bank…](https://github.com/vectorize-io/hindsight/commit/9195f93a9a71bc6e9b4060f355da494cd491c27c) | nicoloboschi |
| 2026-11-27 | [fix(coding-agents): a write-back's operation id names the whole histo…](https://github.com/vectorize-io/hindsight/commit/8adfaaff2a95f0b481310712e77d37fcf6415b97) | nicoloboschi |
| 2026-11-27 | [feat(coding-agents): pageScope and toolGuideMoments settings for bank…](https://github.com/vectorize-io/hindsight/commit/315be3412415490872bf6dc97d393496a123df17) | nicoloboschi |
| 2026-11-27 | [feat(coding-agents): sessionContext puts chosen mental models and pag…](https://github.com/vectorize-io/hindsight/commit/2ae5fbe2ab0e1771db23c3bb04155cdb7471484e) | nicoloboschi |
| 2026-11-27 | [feat(recall): text2date finds the dates in a recall query by default;…](https://github.com/vectorize-io/hindsight/commit/8a4563fdecebec9244254abf2092af5e01ee0d50) | nicoloboschi |
| 2026-11-27 | [fix(docs): home page detection honours baseUrl, so the skill bar isn'…](https://github.com/vectorize-io/hindsight/commit/6adb988eb9fad1cfa1b7c5e2a89359fdc28d694c) | nicoloboschi |
| 2026-11-27 | [fix(coding-agents): replay a persistent-plugin session whose save fai…](https://github.com/vectorize-io/hindsight/commit/4c1727b0bc69449e5fecf30121af22afb05397cf) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
