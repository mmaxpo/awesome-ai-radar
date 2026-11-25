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
| ⭐ **Stars** | 579 |
| 🍴 **Forks** | 63 |
| 🐞 **Open issues + PRs** | [35](https://github.com/pizza-bot-app/pizza-bot/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 5% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agentic-ai` `ai-agents` `amazon-bedrock` `deepagents` `electron` `human-in-the-loop` `langgraph` `local-first` `mcp` `typescript` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-06-26 |
| 📦 **Latest release** | [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 14.7 MB |
| 🌐 **Website** | https://github.com/pizza-bot-app/pizza-bot/releases |

## 📦 Recent releases

### [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — Pizza Bot OSS 1.3.0
<sub>2026-11-10 · 14d ago</sub>

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
| 2026-11-25 | [Merge pull request #224 from pizza-bot-app/feat/head-app-icon](https://github.com/pizza-bot-app/pizza-bot/commit/852e68257f053c1114d7f3fc580cf69e093e18b8) | JoeDo |
| 2026-11-25 | [feat: use the robot's head as the app icon](https://github.com/pizza-bot-app/pizza-bot/commit/77e4b07e85858a6e3e4ad3cde0b97cea31bb7cd4) | JoeDo |
| 2026-11-24 | [fix(runtime): refuse eval task() dispatch to approval-gated skills](https://github.com/pizza-bot-app/pizza-bot/commit/ecca27c625de3e6fdb6aca70757205ddc5e2f231) | JoeDo |
| 2026-11-24 | [fix(runtime): give each task() dispatched from eval its own tool call id](https://github.com/pizza-bot-app/pizza-bot/commit/25aa663a4d5a7c1cccfee4dd775a0fb984782da0) | JoeDo |
| 2026-11-24 | [Merge pull request #214 from pizza-bot-app/feat/trigger-names](https://github.com/pizza-bot-app/pizza-bot/commit/ef7f4c2e92a10f629d7b04562012a643998c6679) | JoeDo |
| 2026-11-24 | [Merge pull request #213 from pizza-bot-app/feat/unified-resource-deta…](https://github.com/pizza-bot-app/pizza-bot/commit/847a72b87132ee3417bdd334d9a2db9b56fcd728) | JoeDo |
| 2026-11-24 | [Merge pull request #110 from pizza-bot-app/delete-mcp](https://github.com/pizza-bot-app/pizza-bot/commit/4d70633075b65bf6de4a9275343c00025ff2f251) | JoeDo |
| 2026-11-24 | [feat: optional names for schedules and webhooks](https://github.com/pizza-bot-app/pizza-bot/commit/8f00969e1e7609bdd59019aa912df7a82573abec) | JoeDo |
| 2026-11-24 | [feat(web): read-only detail view with one header action for every res…](https://github.com/pizza-bot-app/pizza-bot/commit/86e6919ab7a9ca04a8a31ffa4d7424d91c2398c2) | JoeDo |
| 2026-11-24 | [fix(web): refetch an MCP server's config after saving it](https://github.com/pizza-bot-app/pizza-bot/commit/da1e9832aba27b43fca30699a5fe8a51820aa40d) | JoeDo |

[See all commits ↗](https://github.com/pizza-bot-app/pizza-bot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
```
