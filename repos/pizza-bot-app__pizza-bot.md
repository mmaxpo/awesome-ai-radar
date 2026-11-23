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
| ⭐ **Stars** | 576 |
| 🍴 **Forks** | 62 |
| 🐞 **Open issues + PRs** | [26](https://github.com/pizza-bot-app/pizza-bot/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 5% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agentic-ai` `ai-agents` `amazon-bedrock` `deepagents` `electron` `human-in-the-loop` `langgraph` `local-first` `mcp` `typescript` |
| 🕒 **Last activity** | 2026-11-22 (yesterday) |
| 📅 **Created** | 2026-06-26 |
| 📦 **Latest release** | [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 11.6 MB |
| 🌐 **Website** | https://github.com/pizza-bot-app/pizza-bot/releases |

## 📦 Recent releases

### [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — Pizza Bot OSS 1.3.0
<sub>2026-11-10 · 12d ago</sub>

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
| 2026-11-22 | [fix: address non-blocking review notes from #205, #206 and #207 (#208)](https://github.com/pizza-bot-app/pizza-bot/commit/9c709ed9206ae1587bb784adf2a5b19ecdf8b9b9) | JoeDo |
| 2026-11-22 | [fix(inference-providers): keep streamed Anthropic refusals as refusal…](https://github.com/pizza-bot-app/pizza-bot/commit/8ba9c17fb5ff04256ce734d5385ae8805ea183c6) | JoeDo |
| 2026-11-22 | [fix(runtime-langgraph): pause the sandbox watchdog during bridged hos…](https://github.com/pizza-bot-app/pizza-bot/commit/82be4a88b86878c9e9e4ceb3639eb9c0bac27eff) | JoeDo |
| 2026-11-22 | [feat(inference-providers): route Vertex AI through a project and loca…](https://github.com/pizza-bot-app/pizza-bot/commit/09823d956225460810c79cf2e6d75af197023fcd) | JoeDo |
| 2026-11-19 | [fix(bedrock): drop blank text blocks from replayed history (#204)](https://github.com/pizza-bot-app/pizza-bot/commit/ce626e028c3eb9666789ba547b7baf76ac190590) | JoeDo |
| 2026-11-19 | [docs(bedrock): state why stripReasoningForBedrock is still needed (#201)](https://github.com/pizza-bot-app/pizza-bot/commit/aa14a2292cfad3e9b71327647e78add4e3e17b72) | JoeDo |
| 2026-11-19 | [chore: add .nvmrc and route QuickJS subagent cap through sandbox opti…](https://github.com/pizza-bot-app/pizza-bot/commit/e708ac31e9c97448dab6f1bd83ef5c21dea8b06e) | JoeDo |
| 2026-11-19 | [chore(deps): bump langgraphjs stack and drop obsolete rejection drain…](https://github.com/pizza-bot-app/pizza-bot/commit/28388afa1dc9e80c4f74b4351f6a95d5c54f90fc) | JoeDo |
| 2026-11-19 | [fix(plugin-sdk): keep Playwright browser text reads inline (#185)](https://github.com/pizza-bot-app/pizza-bot/commit/339641b9f2c9a7392ed66c7846a54831e205dde6) | CobraA1 |
| 2026-11-19 | [chore(deps): bump @hono/node-server from 2.1.3 to 2.1.9 in /plugins (…](https://github.com/pizza-bot-app/pizza-bot/commit/5e55c9850c343728c9a6028abeddbf312ca6b41d) | dependabot[bot] |

[See all commits ↗](https://github.com/pizza-bot-app/pizza-bot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
```
