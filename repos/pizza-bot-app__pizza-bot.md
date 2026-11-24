# pizza-bot-app/pizza-bot

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pizza-bot-app/pizza-bot)

> A local-first inbox for long-running AI agents, built with DeepAgents and LangGraph.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Local-first inbox for long-running AI agents (LangGraph) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 578 |
| 🍴 **Forks** | 63 |
| 🐞 **Open issues + PRs** | [28](https://github.com/pizza-bot-app/pizza-bot/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 5% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agentic-ai` `ai-agents` `amazon-bedrock` `deepagents` `electron` `human-in-the-loop` `langgraph` `local-first` `mcp` `typescript` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-06-26 |
| 📦 **Latest release** | [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 11.7 MB |
| 🌐 **Website** | https://github.com/pizza-bot-app/pizza-bot/releases |

## 📦 Recent releases

### [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — Pizza Bot OSS 1.3.0
<sub>2026-11-10 · 13d ago</sub>

> **Highlights**
> - **Opper provider.** You can use [Opper](https://opper.ai/) as a model provider. Thanks to @Felixkw12 for their first contribution! (#155)
> - **Google Workspace plugin.** Pizza Bot can work with your Gmail and Google Calendar. It ships disabled and needs your own Google Cloud OAuth client, so follow the [setup guide](https://github.com/pizza-bot-app/pizza-bot/blob/v1.3.0/docs/GOOGLE_WORKSPACE.md) to turn it on. (#153)
> - **Markdown skill import.** You can import a skill from a single Markdown file as well as a ZIP bundle. (#161)
> - **arm64 backend image.** The container image is published for linux/arm64 as well as amd64. Thanks to @PatrickSun93 for their first contribution! (#149)
> - **Desktop PATH fix.** On macOS and Linux, the desktop app reads the PATH from your login shell. MCP servers that run through `npx` or Homebrew tools start when you open the app from the Dock or your launcher. (#157)
> …

### [v1.2.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.2.0) — Pizza Bot OSS 1.2.0
<sub>2026-10-02 · 1mo ago</sub>

> **What's Changed**
> * feat(providers): add Requesty as a model provider by @Thibaultjaigu in https://github.com/pizza-bot-app/pizza-bot/pull/127
> * feat: bridge the granted filesystem into the eval sandbox by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/113
> * Unify model selection with a shared searchable combobox by @igorfil in https://github.com/pizza-bot-app/pizza-bot/pull/118
> * Show a list of tools for MCP by @igorfil in https://github.com/pizza-bot-app/pizza-bot/pull/115
> * Allow pasting of JSON to configure MCP by @igorfil in https://github.com/pizza-bot-app/pizza-bot/pull/116
> …

### [v1.1.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.1.0) — Pizza Bot OSS 1.1.0
<sub>2026-09-19 · 2mo ago</sub>

> **What's Changed**
> * fix: stop unrelated advisories and a Windows flake from blocking merges by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/78
> * docs: point container users at building the image by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/79
> * docs: describe the published image as pullable by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/80
> * fix: reject unrecognized protocol commands instead of answering 204 by @quinnypig in https://github.com/pizza-bot-app/pizza-bot/pull/84
> * fix: stop killing the sidecar while it is still starting up by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/86
> …

### [v1.0.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.0.0) — Pizza Bot OSS 1.0.0
<sub>2026-09-08 · 2mo ago</sub>

> **What's Changed**
> * Fix parallel subagent run limits by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/3
> * Leave an empty inbox unselected until New by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/5
> * docs: recognize Pizza Bot contributors by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/7
> * docs: update Pizza Bot contributors by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/8
> * fix: deny better-sqlite3 install script so npm ci works on Windows without MSVC by @JoeDo in https://github.com/pizza-bot-app/pizza-bot/pull/10
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Merge pull request #212 from pizza-bot-app/fix/surface-content-filter…](https://github.com/pizza-bot-app/pizza-bot/commit/06d6338561ac0969f0ab40a26320a7f8ec7f9ed2) | JoeDo |
| 2026-11-23 | [fix(chat): surface replies blocked by the provider's content filter](https://github.com/pizza-bot-app/pizza-bot/commit/88789e8fa95a6fcf9998271cc9cc0aeb372bc222) | JoeDo |
| 2026-11-23 | [Merge pull request #165 from pizza-bot-app/fix/bedrock-truncated-tool…](https://github.com/pizza-bot-app/pizza-bot/commit/1590bd7c1f9ba8eeda9be84d71cf9380999866b5) | JoeDo |
| 2026-11-23 | [feat(web): show a status while a cut-off tool call is retried](https://github.com/pizza-bot-app/pizza-bot/commit/2305ccffe6d7b04d39727be16b70bf45948a8aa2) | igorfil |
| 2026-11-23 | [fix(runtime): count cut-off retries against the model-call limit](https://github.com/pizza-bot-app/pizza-bot/commit/17865bf766aede6759c2017f279ac11706b7eb76) | igorfil |
| 2026-11-23 | [fix(runtime): silently retry a tool call cut off at the output-token …](https://github.com/pizza-bot-app/pizza-bot/commit/c35d0ca80ed9904a8f2b29efcfb8aac264b7c4d3) | igorfil |
| 2026-11-23 | [fix(runtime): tell the orchestrator when its tool call was cut off](https://github.com/pizza-bot-app/pizza-bot/commit/3c2e7de7913138e9fe746d03a43fd3fcaac21a0a) | igorfil |
| 2026-11-23 | [fix(bedrock): drop every assistant turn Converse cannot replay](https://github.com/pizza-bot-app/pizza-bot/commit/71774d7306d601aa34f86697d91eea5e94e78d5f) | igorfil |
| 2026-11-23 | [fix(bedrock): drop invalid tool calls before Converse replay](https://github.com/pizza-bot-app/pizza-bot/commit/0b947b3f4c3aafc644fe4cae97f4db92179bc52b) | igorfil |
| 2026-11-22 | [fix: address non-blocking review notes from #205, #206 and #207 (#208)](https://github.com/pizza-bot-app/pizza-bot/commit/9c709ed9206ae1587bb784adf2a5b19ecdf8b9b9) | JoeDo |

[See all commits ↗](https://github.com/pizza-bot-app/pizza-bot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
```
