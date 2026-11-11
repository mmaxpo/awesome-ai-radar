# zylon-ai/private-gpt

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/zylon-ai/private-gpt)

> Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why I saved it** | Private, local Q&A over your documents |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 57.6k |
| 🍴 **Forks** | 7.6k |
| 🐞 **Open issues + PRs** | [15](https://github.com/zylon-ai/private-gpt/issues) |
| 💻 **Languages** | Python 87% · HTML 9% · MDX 2% · Jinja 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-tools` `on-premise` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-05-02 |
| 📦 **Latest release** | [v1.0.1](https://github.com/zylon-ai/private-gpt/releases/tag/v1.0.1) — 2026-06-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 221.4 MB |
| 🌐 **Website** | https://www.zylon.ai/private-gpt |

## 📦 Recent releases

### [v1.0.1](https://github.com/zylon-ai/private-gpt/releases/tag/v1.0.1)
<sub>2026-06-18 · 4mo ago</sub>

> **[1.0.1](https://github.com/zylon-ai/private-gpt/compare/v1.0.0...v1.0.1) (2026-06-16)**
> **Bug Fixes**
> * add missing docker database deps ([#2264](https://github.com/zylon-ai/private-gpt/issues/2264)) ([4302bd6](https://github.com/zylon-ai/private-gpt/commit/4302bd629a4ca5fcee23e9064a0448cd110eb523))
> * ensure that the publisher is ready to publish new messages ([#2266](https://github.com/zylon-ai/private-gpt/issues/2266)) ([4c0c500](https://github.com/zylon-ai/private-gpt/commit/4c0c500bbd34a06feedb52e1d267d9b7b918554b))
> * make embedding API key optional for local OpenAI-compatible engines ([#2261](https://github.com/zylon-ai/private-gpt/issues/2261)) ([c120a90](https://github.com/zylon-ai/private-gpt/commit/c120a90603f78bb28b19f758a9ba4b40c37480ff)), closes [#2260](https://github.com/zylon-ai/private-gpt/issues/2260)
> * use PGPT_HOME for local data, caches, and cleanup paths ([#2267](https://github.com/zylon-ai/private-gpt/issues/2267)) ([4021cf4](https://github.com/zylon-ai/private-gpt/commit/4021cf4e203d4c309f496a8fbf95271f6084834c))
> …

### [v1.0.0](https://github.com/zylon-ai/private-gpt/releases/tag/v1.0.0)
<sub>2026-06-03 · 5mo ago</sub>

> **PrivateGPT 1.0.0**
> This release merges two years of work from our private fork back into the open source repo.
> The original PrivateGPT was a semantic search pipeline wrapped by a minimal API: ingest documents, embed chunks, retrieve by similarity, pass context to a local model. It proved the concept. PrivateGPT 1.0 is the full application backend that turns local models into production AI applications.
> ---
> **What's new**
> - A standard messages API
> …

### [v1.0.0-rc7](https://github.com/zylon-ai/private-gpt/releases/tag/v1.0.0-rc7) _(pre-release)_
<sub>2026-06-03 · 5mo ago</sub>

> _No notes._

### [v1.0.0-rc6](https://github.com/zylon-ai/private-gpt/releases/tag/v1.0.0-rc6) _(pre-release)_
<sub>2026-06-02 · 5mo ago</sub>

> _No notes._

### [v0.6.2](https://github.com/zylon-ai/private-gpt/releases/tag/v0.6.2)
<sub>2024-08-08 · 2y ago</sub>

> **[0.6.2](https://github.com/zylon-ai/private-gpt/compare/v0.6.1...v0.6.2) (2024-08-08)**
> We are excited to announce the release of PrivateGPT 0.6.2, a “minor” version, which brings significant enhancements to our Docker setup, making it easier than ever to deploy and manage PrivateGPT in various environments.
> **Key Improvements**
> Our latest version introduces several key improvements that will streamline your deployment process:
> * **Simplified cold-start with a better Docker Compose Integration**: Easily manage multiple services with improved Docker Compose configurations, reducing complexity and increasing efficiency.
> * **Environment-Specific Profiles**: Tailor your setup to different environments, including CPU, CUDA (Nvidia GPU), and MacOS, ensuring optimal performance and compatibility in one click.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [fix(ingest): keep code and snake_case words intact when sanitizing markdown (#2425)](https://github.com/zylon-ai/private-gpt/commit/44fa6598a10f2c29cd5d8745bf29cc04b75cb3ad) | MohammadHijjawi97 |
| 2026-11-11 | [perf(citations): skip plain text between citation markers while streaming (#2451)](https://github.com/zylon-ai/private-gpt/commit/6bb62ed7f2a85c427b4405860553e2240ae30160) | b84330808 |
| 2026-11-11 | [chore(deps): bump docker/login-action from 4.6.0 to 4.8.0 (#2454)](https://github.com/zylon-ai/private-gpt/commit/a0e65a68f0a9ced1265ba98d31f3a4c58673ccbe) | dependabot[bot] |
| 2026-11-11 | [chore(deps): bump astral-sh/setup-uv from 10.3.0 to 10.3.3 (#2443)](https://github.com/zylon-ai/private-gpt/commit/924958f7b54d2b88ec5b36536f6f54c0caaa6a3c) | dependabot[bot] |
| 2026-11-11 | [fix(llm): honor temperature 0 for openailike models (#2442)](https://github.com/zylon-ai/private-gpt/commit/3f26feb2b366bb2bbfded21a31e52814653b7424) | pcbeingused333 |
| 2026-11-11 | [docs: add PopNow OpenAI-compatible gateway configuration example (#2447)](https://github.com/zylon-ai/private-gpt/commit/b6044e5a8beee154ddafcedcd38ed3e2b018ce3d) | kyuminjo |
| 2026-11-11 | [fix(ingest): keep the content of blockquotes when parsing markdown (#2448)](https://github.com/zylon-ai/private-gpt/commit/69556ede12f24e3285da0b6f54862c13b425243b) | MohammadHijjawi97 |
| 2026-11-11 | [docs: add Standard Compute OpenAI-compatible provider guide (#2453)](https://github.com/zylon-ai/private-gpt/commit/90e58a6f7d9d556c281f5f03a971e001e7bb0904) | henrikdukefoss |
| 2026-11-11 | [fix(chat): keep structured blocks of server tool results in history (#2456)](https://github.com/zylon-ai/private-gpt/commit/fab986f54d41ac155661176a6b1b69907811fef9) | jaluma |
| 2026-11-10 | [fix(files): download files whose names are not ASCII (#2426)](https://github.com/zylon-ai/private-gpt/commit/5f8aca68a11d6eb27cdef19cda03a64773e9d3ad) | MaxFreedomPollard |

[See all commits ↗](https://github.com/zylon-ai/private-gpt/commits)

## 👥 Top contributors

[imartinez](https://github.com/imartinez) (123) · [jaluma](https://github.com/jaluma) (96) · [dependabot[bot]](https://github.com/dependabot[bot]) (21) · [lopagela](https://github.com/lopagela) (16) · [pabloogc](https://github.com/pabloogc) (15)

## ⬇️ Get it

```bash
git clone https://github.com/zylon-ai/private-gpt.git
```
