# pizza-bot-app/pizza-bot

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pizza-bot-app/pizza-bot)

> A local-first inbox for long-running AI work.

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
| ⭐ **Stars** | 580 |
| 🍴 **Forks** | 65 |
| 🐞 **Open issues + PRs** | [30](https://github.com/pizza-bot-app/pizza-bot/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 5% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agentic-ai` `ai-agents` `amazon-bedrock` `deepagents` `electron` `human-in-the-loop` `langgraph` `local-first` `mcp` `typescript` `langchain` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-06-26 |
| 📦 **Latest release** | [v1.4.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.4.0) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 16.0 MB |
| 🌐 **Website** | https://github.com/pizza-bot-app/pizza-bot/releases |

## 📦 Recent releases

### [v1.4.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.4.0) — Pizza Bot OSS 1.4.0
<sub>2026-11-26 · yesterday</sub>

> **Highlights**
> - **Three new model providers.** You can use [UberLLM](https://uberllm.dev), Cheaper Inference, and [LiteLLM](https://docs.litellm.ai/docs/simple_proxy) as model providers. LiteLLM works with your own self-hosted proxy. Thanks to @al-global-tech, @aiapienthusiast, and @prodmanpd for their first contributions! (#193, #173, #172)
> - **Advanced request JSON.** OpenAI, OpenRouter, and the OpenAI-compatible gateways have an optional **Advanced request JSON** setting that adds fields, like `service_tier`, to every request. It's checked when you save, and fields Pizza Bot controls are rejected. Thanks to @JacobJans for suggesting it in [discussion #95](https://github.com/pizza-bot-app/pizza-bot/discussions/95)! (#232)
> - **Gemini 4 on Vertex AI.** The Google provider has optional **Vertex AI project ID** and **location** settings. Set a project under Settings > Providers to reach Gemini 4 models, which Vertex AI Express can't serve. (#207, #252)
> - **Google Workspace on headless and container backends.** The Gmail and Calendar plugin can read its credentials from environment variables, and `npm run auth -- --print` and `--no-browser` help you get them on a host without a browser. See [the guide](https://github.com/pizza-bot-app/pizza-bot/blob/v1.4.0/docs/GOOGLE_WORKSPACE.md#run-the-backend-in-a-container-or-on-a-headless-host). (#197)
> - **Clearer resource screens.** Selecting an MCP server, skill, memory, schedule, webhook, or plugin opens a read-only view with one action to change it: **Edit**, **Customize**, or a link to the plugin that manages it. Thanks to @igorfil for starting this with the MCP server screen. (#110, #213)
> …

### [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — Pizza Bot OSS 1.3.0
<sub>2026-11-10 · 16d ago</sub>

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
| 2026-11-27 | [Merge pull request #273 from JoeDo/docs/env-example-missing-settings](https://github.com/pizza-bot-app/pizza-bot/commit/d60abd59086d4a6da4ce21e7a35ad03261216909) | JoeDo |
| 2026-11-27 | [docs: describe the Playwright browser path as an override](https://github.com/pizza-bot-app/pizza-bot/commit/e7e8c4c6d21170075998d3635d7da42330b9364f) | JoeDo |
| 2026-11-27 | [docs: rewrap the first fork review step](https://github.com/pizza-bot-app/pizza-bot/commit/346462b6e1cf5a9bde2421fffe0acea30af54d7b) | JoeDo |
| 2026-11-27 | [docs: describe what npm test runs and which packages resolve to dist](https://github.com/pizza-bot-app/pizza-bot/commit/ac320897399488098bca10b5e65edf759dc15d04) | JoeDo |
| 2026-11-27 | [docs: list the operator settings .env.example was missing](https://github.com/pizza-bot-app/pizza-bot/commit/944208a495955cc90d109904c36190df5b2ba338) | JoeDo |
| 2026-11-27 | [Merge pull request #272 from pizza-bot-app/fix/fork-review-single-che…](https://github.com/pizza-bot-app/pizza-bot/commit/01bc9dfa8dbc0b9376c9fd11a9f351a8f5b49699) | JoeDo |
| 2026-11-27 | [Merge branch 'main' into fix/fork-review-single-check-run](https://github.com/pizza-bot-app/pizza-bot/commit/32694d6a8942fa8642c9af9ac74406033df0eff7) | JoeDo |
| 2026-11-27 | [Merge pull request #271 from pizza-bot-app/docs/stale-image-and-attac…](https://github.com/pizza-bot-app/pizza-bot/commit/27e4110635931951e9e69f5271f5f7ba444a086b) | JoeDo |
| 2026-11-27 | [ci: give a fork commit one agent-review check that the labeled review…](https://github.com/pizza-bot-app/pizza-bot/commit/2e7e029ac573cc6dfa362a83c75009ae86e96c26) | JoeDo |
| 2026-11-27 | [ci: name the review session check after the gate that enforces it](https://github.com/pizza-bot-app/pizza-bot/commit/036f80dc8921d5a0c571f11fc06cc6be168a3863) | JoeDo |

[See all commits ↗](https://github.com/pizza-bot-app/pizza-bot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
```
