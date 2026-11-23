# assafelovic/gpt-researcher

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/assafelovic/gpt-researcher)

> An autonomous agent that conducts deep research on any data using any LLM providers

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Autonomous agent that researches and writes reports |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 30.9k |
| 🍴 **Forks** | 4.3k |
| 🐞 **Open issues + PRs** | [16](https://github.com/assafelovic/gpt-researcher/issues) |
| 💻 **Languages** | Python 68% · TypeScript 23% · JavaScript 4% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `python` `agent` `automation` `research` `search` `webscraping` `llms` `deepresearch` `mcp` `mcp-server` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-05-12 |
| 📦 **Latest release** | [v3.8.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.8.0) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 58.2 MB |
| 🌐 **Website** | https://gptr.dev |

## 📦 Recent releases

### [v3.8.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.8.0) — New paper UI, detailed reports in 3:27, and 53 community fixes
<sub>2026-11-09 · 14d ago</sub>

> **A new UI, and detailed reports in under 4 minutes**
> <a href="https://github.com/user-attachments/assets/4d3f26cf-8ccc-413a-b17c-80aa9e1b52d1">
>   <img src="https://github.com/user-attachments/assets/3a56a008-fcbd-4373-9e40-8d6027120cfb" alt="GPT Researcher turning a question into a cited report" width="800">
> </a>
> The Next.js app has a new paper design that matches [gptr.dev](https://gptr.dev). Settings live in one modal with tabs for Research, MCP, Documents and Backend; a run shows a plain-language feed, and the sources margin slides in once writing starts. The previous UI is still available at `/classic`.
> Detailed reports now finish in **3:27 instead of 9:11**. Sections are researched in parallel, and the default writer is now `gpt-6-sol`, which starts writing within seconds instead of reasoning for close to a minute per section first. Measurements and the model comparison are in #2272.
> …

### [v3.7.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.7.0) — Jev update and many bug fixes and improvements
<sub>2026-09-26 · 1mo ago</sub>

> **Smarter context, no embeddings required**
> GPT Researcher now picks the context it sends to the LLM by **usefulness, not similarity**.
> Every passage scraped for a research question is scored by [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
> on how useful it is for answering that question, and only the passages that help are kept.
> On a benchmark of 28 research tasks replayed on identical sources:
> <img width="3200" height="1800" alt="image-1790437831580" src="https://github.com/user-attachments/assets/c2a7b305-2e60-4709-ad9c-8af09e297f9f" />
> …

### [v3.6.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.6.1) — Major fixes
<sub>2026-08-24 · 3mo ago</sub>

> **What's Changed**
> * fix: restore main, add CI, and land 97 queued PRs by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/2074
> * fix(readme): restore broken star history chart by @Dessalines39394 in https://github.com/assafelovic/gpt-researcher/pull/2066
> * docs: document scholarly retriever configuration by @pikaqiu2333 in https://github.com/assafelovic/gpt-researcher/pull/1863
> * chore(deps): update python-pptx requirement from >=1.0.0 to >=1.0.2 by @dependabot[bot] in https://github.com/assafelovic/gpt-researcher/pull/1927
> * chore: remove the dead poetry dependency block, test the declared Python floor by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/2075
> …

### [v3.6.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.6.0)
<sub>2026-07-18 · 4mo ago</sub>

> Introducing a super stable version with enhanced improvements across security, stability and performance. We're also introducing a collaboration with Langchain with the latest deep agents framework here - https://github.com/assafelovic/gpt-researcher/tree/main/deep_agents
> Thank you and welcome to all the new contributors!
> **What's Changed**
> * security: sanitize untrusted content, add SECURITY.md, pin brotli by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1820
> * Fix silently dropped token limits, real usage-based cost tracking, and research pipeline robustness by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1861
> * Add Deep Agents example: GPT Researcher as the research engine in a LangChain deep agent by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1857
> …

### [v3.5.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.5.1)
<sub>2026-06-23 · 5mo ago</sub>

> **What's Changed**
> * fix: add MAX_REVISIONS guard to prevent infinite revision loop by @varshiniml7 in https://github.com/assafelovic/gpt-researcher/pull/1783
> * Improve SimpleQA eval observability with structured logging and latency metadata by @SeanHe727 in https://github.com/assafelovic/gpt-researcher/pull/1790
> * feat(retrievers): add Brave Search support by @agbocsardi in https://github.com/assafelovic/gpt-researcher/pull/1793
> * Abstain instead of fabricating a report when no content was gathered by @aaravanmay in https://github.com/assafelovic/gpt-researcher/pull/1799
> * fix(deep-research): keep oversized context from collapsing to empty by @XiaojuCH in https://github.com/assafelovic/gpt-researcher/pull/1802
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Merge pull request #2364 from assafelovic/docs/costs-page](https://github.com/assafelovic/gpt-researcher/commit/9d39a2f86d55e264f69dfeff2365f27fad3c1144) | assafelovic |
| 2026-11-23 | [docs: add a Costs page and link it from the overview](https://github.com/assafelovic/gpt-researcher/commit/8b857ff9fba30f5d5d4bb0a63f426327a8a1efa8) | assafelovic |
| 2026-11-23 | [Merge pull request #2359 from assafelovic/fix/detailed-report-costs](https://github.com/assafelovic/gpt-researcher/commit/5e95ef4b3cc476de99be98e933c13acf53c96aea) | assafelovic |
| 2026-11-22 | [fix: deliver cost_update events to custom log handlers](https://github.com/assafelovic/gpt-researcher/commit/df48d9cbb01bf19f00b0c79b83112a3bcda46ed8) | assafelovic |
| 2026-11-22 | [fix: include subtopic researcher costs in detailed report totals](https://github.com/assafelovic/gpt-researcher/commit/797bdf64e70ec6e888a31b9ff402783eb556d970) | assafelovic |
| 2026-11-22 | [Merge pull request #2358 from assafelovic/docs/cost-stats](https://github.com/assafelovic/gpt-researcher/commit/8b474fe7d92aca112601cb87e1ec0999103bc01a) | assafelovic |
| 2026-11-22 | [docs: update cost and runtime stats to measured values](https://github.com/assafelovic/gpt-researcher/commit/a390845f68069bc20a6cb8b2a2c975d5db4cd29e) | assafelovic |
| 2026-11-22 | [Merge pull request #2357 from assafelovic/docs/site-polish](https://github.com/assafelovic/gpt-researcher/commit/1f1117e460cc0e159907290235e6d8de81e579f3) | assafelovic |
| 2026-11-22 | [docs: site icons, homepage title, Discord badge and FAQ cost](https://github.com/assafelovic/gpt-researcher/commit/833ec119cf06df2040015c435fb7f93b1ad0816f) | assafelovic |
| 2026-11-22 | [Frontend follow-ups: runtime /outputs proxy and a Next.js lockfile (#…](https://github.com/assafelovic/gpt-researcher/commit/0b27488a8576415af1d1246ddc9c2364275d6c7f) | assafelovic |

[See all commits ↗](https://github.com/assafelovic/gpt-researcher/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assafelovic/gpt-researcher.git
```
