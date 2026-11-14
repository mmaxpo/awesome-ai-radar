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
| ⭐ **Stars** | 30.7k |
| 🍴 **Forks** | 4.2k |
| 🐞 **Open issues + PRs** | [36](https://github.com/assafelovic/gpt-researcher/issues) |
| 💻 **Languages** | Python 66% · TypeScript 24% · JavaScript 4% · CSS 4% · HCL 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `python` `agent` `automation` `research` `search` `webscraping` `llms` `deepresearch` `mcp` `mcp-server` |
| 🕒 **Last activity** | 2026-11-12 (yesterday) |
| 📅 **Created** | 2023-05-12 |
| 📦 **Latest release** | [v3.8.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.8.0) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.1 MB |
| 🌐 **Website** | https://gptr.dev |

## 📦 Recent releases

### [v3.8.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.8.0) — New paper UI, detailed reports in 3:27, and 53 community fixes
<sub>2026-11-09 · 4d ago</sub>

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
<sub>2026-08-24 · 2mo ago</sub>

> **What's Changed**
> * fix: restore main, add CI, and land 97 queued PRs by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/2074
> * fix(readme): restore broken star history chart by @Dessalines39394 in https://github.com/assafelovic/gpt-researcher/pull/2066
> * docs: document scholarly retriever configuration by @pikaqiu2333 in https://github.com/assafelovic/gpt-researcher/pull/1863
> * chore(deps): update python-pptx requirement from >=1.0.0 to >=1.0.2 by @dependabot[bot] in https://github.com/assafelovic/gpt-researcher/pull/1927
> * chore: remove the dead poetry dependency block, test the declared Python floor by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/2075
> …

### [v3.6.0](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.6.0)
<sub>2026-07-18 · 3mo ago</sub>

> Introducing a super stable version with enhanced improvements across security, stability and performance. We're also introducing a collaboration with Langchain with the latest deep agents framework here - https://github.com/assafelovic/gpt-researcher/tree/main/deep_agents
> Thank you and welcome to all the new contributors!
> **What's Changed**
> * security: sanitize untrusted content, add SECURITY.md, pin brotli by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1820
> * Fix silently dropped token limits, real usage-based cost tracking, and research pipeline robustness by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1861
> * Add Deep Agents example: GPT Researcher as the research engine in a LangChain deep agent by @assafelovic in https://github.com/assafelovic/gpt-researcher/pull/1857
> …

### [v3.5.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v3.5.1)
<sub>2026-06-23 · 4mo ago</sub>

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
| 2026-11-09 | [ci: remove the AWS ECR build and Terraform deploy workflows (#2276)](https://github.com/assafelovic/gpt-researcher/commit/ddd4db36208d9c8e49f3b2436efda97baecb5433) | assafelovic |
| 2026-11-09 | [Merge pull request #2274 from assafelovic/triage/2026-11-release](https://github.com/assafelovic/gpt-researcher/commit/597a99e2ef879606229754ec0d575a89eb587464) | assafelovic |
| 2026-11-09 | [ci(docker): use the Node 24 majors of the Docker actions](https://github.com/assafelovic/gpt-researcher/commit/5016a09e4ffb238f176f8ff5ed4e2584c68e4d6b) | assafelovic |
| 2026-11-09 | [chore(release): 0.17.0, single [project] metadata table](https://github.com/assafelovic/gpt-researcher/commit/273a073938ae62c86cfd5083c9900220ebacf735) | assafelovic |
| 2026-11-09 | [chore(frontend): stop tracking the next-pwa service worker build output](https://github.com/assafelovic/gpt-researcher/commit/dc1c4c42af6340493b7d9a5b748fa99b4eecf714) | assafelovic |
| 2026-11-09 | [Merge PR #2222: docs: sync Chinese README (README-zh_CN.md) with the …](https://github.com/assafelovic/gpt-researcher/commit/937dac255ec9dc6908ed0355d22b37170344027d) | assafelovic |
| 2026-11-09 | [Merge PR #1924: feat: update MiniMax regional providers and Flash def…](https://github.com/assafelovic/gpt-researcher/commit/08013dffbd33db5010738a9f5ca368260c1b4786) | assafelovic |
| 2026-11-09 | [Merge PR #2184: feat: add Deploy on Render page and render.yaml](https://github.com/assafelovic/gpt-researcher/commit/f98e0054d74db9a6710394ae23678d12c82d2584) | assafelovic |
| 2026-11-09 | [Merge PR #2231: fix(scraper): retry HTTP 403 with a transparent user …](https://github.com/assafelovic/gpt-researcher/commit/07b262feff37e3f559fb1a687a0e895f94a00ad0) | assafelovic |
| 2026-11-09 | [Merge PR #2232: feat: add an optional research lifecycle observer](https://github.com/assafelovic/gpt-researcher/commit/3537a245e76e449100be1bb1930ea9931aa3fe8b) | assafelovic |

[See all commits ↗](https://github.com/assafelovic/gpt-researcher/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assafelovic/gpt-researcher.git
```
