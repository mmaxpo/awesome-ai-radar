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
| ⭐ **Stars** | 63.3k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [169](https://github.com/vectorize-io/hindsight/issues) |
| 💻 **Languages** | Python 69% · TypeScript 16% · MDX 11% · Rust 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-ai` `memory` `agents` `ai-memory` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-10-30 |
| 📦 **Latest release** | [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.4 MB |
| 🌐 **Website** | https://hindsight.vectorize.io/ |

## 📦 Recent releases

### [v1.3.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.3.0)
<sub>2026-11-24 · yesterday</sub>

> **What's Changed**
> * docs: changelog for v1.2.3 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6714
> * fix(release): slim image no longer overwrites :latest by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6728
> * feat(mcp): per-bank MCP server instructions in the initialize response by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6712
> * docs: replace retired Claude Code plugin text and dead integration link in blog and guides by @chrislatimer in https://github.com/vectorize-io/hindsight/pull/6716
> * fix(knowledge): bound the work of cutting a video, and drop files that fail for good by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6711
> …

### [v1.2.3](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.3)
<sub>2026-11-19 · 5d ago</sub>

> **What's Changed**
> * docs: changelog and blog post for v1.2.2 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6678
> * fix(knowledge): ingest odd, broken and big files without failing, retrying or running out of memory by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6701
> * Fix broken 'What is Hindsight?' demo video in README by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6702
> * Use descriptive filename for the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6706
> * Update the What is Hindsight demo video by @benfrank241 in https://github.com/vectorize-io/hindsight/pull/6708
> …

### [v1.2.2](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.2)
<sub>2026-11-19 · 5d ago</sub>

> **What's Changed**
> * test(llm): fix the two-user-turns tests broken by the tool-call retry by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6492
> * docs: changelog and blog post for v1.2.1 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6486
> * feat(knowledge-banks): multimodal document banks, hidden behind a feature flag by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6478
> * fix(api): answer 422, not 500, when the LLM provider refuses the content by @cdbartholomew in https://github.com/vectorize-io/hindsight/pull/6501
> * fix(consolidation): stop the misses gemma-4 made on 1.2.1, and the judge errors that hid them by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6505
> …

### [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)
<sub>2026-11-10 · 15d ago</sub>

> **What's Changed**
> * docs drop 0.9 by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6284
> * docs: reading progress bar under the navbar by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6285
> * fix(admin): hindsight-admin cloud is listed in --help by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6286
> * fix(api): one id rule for banks, aliases and mental models; bound page max_tokens by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6282
> * fix(coding-agents): survey starts from every host again; keep terminal-manager env and color codes out by @nicoloboschi in https://github.com/vectorize-io/hindsight/pull/6287
> …

### [v1.2.0](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.0)
<sub>2026-11-03 · 22d ago</sub>

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
| 2026-11-25 | [fix(pg0): an instance another process already started is used, not a …](https://github.com/vectorize-io/hindsight/commit/61c01ecbec8026858feac51caf5a818741cdbf42) | nicoloboschi |
| 2026-11-25 | [fix(dry-run): ignore the deprecated agent_name so the dry run builds …](https://github.com/vectorize-io/hindsight/commit/c494ba4d29a14230e5c034ab05cba9150d968a35) | nicoloboschi |
| 2026-11-25 | [chore(github): delete labels outside a fixed allowlist (#6894)](https://github.com/vectorize-io/hindsight/commit/65f6e3b694247868811423ce47c5277cc8346557) | nicoloboschi |
| 2026-11-25 | [feat(hermes): tell the model to store corrections when a memory is wr…](https://github.com/vectorize-io/hindsight/commit/bd816192f0351802de9489984ffb6c14be9da907) | nicoloboschi |
| 2026-11-25 | [feat(hermes): per-chat settings with a chats map, {chat}/{thread} pla…](https://github.com/vectorize-io/hindsight/commit/7b027d5b038a1431f2206d95652feafcaf835947) | nicoloboschi |
| 2026-11-25 | [release(openclaw): v1.2.3](https://github.com/vectorize-io/hindsight/commit/b9b4c36d699a07934a77494ba21de46bc56aa6e9) | nicoloboschi |
| 2026-11-25 | [feat(hermes): page tools (search, read, list; create opt-in) (#6897)](https://github.com/vectorize-io/hindsight/commit/bfd9c57a367c006404da8a081b84ccbd6f50fe34) | nicoloboschi |
| 2026-11-25 | [fix(hooks): resolve python once in generate-docs-skill.sh (#6898)](https://github.com/vectorize-io/hindsight/commit/0e4cf230ce7322940e17014a9020b19b9ced58f8) | nicoloboschi |
| 2026-11-25 | [fix(openclaw): wizard takes the memory slot; npm: install on OpenClaw…](https://github.com/vectorize-io/hindsight/commit/6ef019d6f28be1fd696e922017c0a276b8004fd8) | nicoloboschi |
| 2026-11-25 | [fix(hermes): label turns written by another agent; exclude tags from …](https://github.com/vectorize-io/hindsight/commit/2a06f05582222b35c0eb5979d86ee125cedc1817) | nicoloboschi |

[See all commits ↗](https://github.com/vectorize-io/hindsight/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vectorize-io/hindsight.git
```
