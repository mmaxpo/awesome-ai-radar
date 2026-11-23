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
| ⭐ **Stars** | 62.9k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [235](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 70% · TypeScript 16% · MDX 9% · Rust 2% · Shell 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.1 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3)
<sub>2026-11-19 · 3d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.2.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6678
> * fix(knowledge): ingest odd, broken and big files without failing, retrying or running out of memory by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6701
> * Fix broken 'What is Hindsight?' demo video in README by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6702
> * Use descriptive filename for the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6706
> * Update the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6708
> …

### [v1.2.2](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.2)
<sub>2026-11-19 · 4d ago</sub>

> **What's Changed**
> * test(llm): fix the two-user-turns tests broken by the tool-call retry by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6492
> * docs: changelog and blog post for v1.2.1 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6486
> * feat(knowledge-banks): multimodal document banks, hidden behind a feature flag by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6478
> * fix(api): answer 422, not 500, when the LLM provider refuses the content by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6501
> * fix(consolidation): stop the misses gemma-4 made on 1.2.1, and the judge errors that hid them by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6505
> …

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 13d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 20d ago</sub>

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
| 2026-11-23 | [feat(llm): add antigravity provider driving Google's agy CLI (#6830)](https://github.com/vectorize-io/hindsight/commit/3ca5b2aa92f5c66d203cf5b39719f0b45927e37b) | nicoloboschi |
| 2026-11-23 | [fix(reflect): let HINDSIGHT_API_LLM_STRICT_SCHEMA_REFLECT take the to…](https://github.com/vectorize-io/hindsight/commit/5cf3737b21e2dba0e7a36b0edaea76973fa7dbea) | nicoloboschi |
| 2026-11-23 | [fix(ci): flaky tests and CI 429s — umbrella for 10 issues (#6824)](https://github.com/vectorize-io/hindsight/commit/467378704af157a463810f2c23c4304f73b7a014) | nicoloboschi |
| 2026-11-23 | [perf(oracle): watermark index, batched link inserts, set-wise observa…](https://github.com/vectorize-io/hindsight/commit/cb54db32884dc07dc64f2e369d3aa9fde5347644) | nicoloboschi |
| 2026-11-23 | [fix(mental-models): a rate-limited refresh step neither pauses the mo…](https://github.com/vectorize-io/hindsight/commit/ea603137cc972047d1fe7b944b4f891f9cdf94aa) | nicoloboschi |
| 2026-11-23 | [fix(migrations): keep extension schemas we cannot relocate on the mig…](https://github.com/vectorize-io/hindsight/commit/fe53a31164e98e0fa883f1f00e1a116bc5f13d36) | nicoloboschi |
| 2026-11-23 | [fix(llm): read Mistral's typed content blocks as text instead of cras…](https://github.com/vectorize-io/hindsight/commit/735ace90628637f3e7b969a695803ea9a70b8bca) | nicoloboschi |
| 2026-11-23 | [feat(clients): knowledge-bank methods on the Python and TypeScript wr…](https://github.com/vectorize-io/hindsight/commit/a6fa4548bf2df640e873c0ed3e7d42da05e4d8da) | nicoloboschi |
| 2026-11-23 | [fix(mcp): an allowlist naming no built-in tool registers no built-ins…](https://github.com/vectorize-io/hindsight/commit/345ac91d5799386fd8c490efcb13e453951e8bdc) | nicoloboschi |
| 2026-11-23 | [fix(docs): FAQ links no unreleased page; production builds leave out …](https://github.com/vectorize-io/hindsight/commit/7a09eaddd257a4314e654a6d438709cf5be27b3d) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
