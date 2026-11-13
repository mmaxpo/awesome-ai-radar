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
| ⭐ **Stars** | 558 |
| 🍴 **Forks** | 61 |
| 🐞 **Open issues + PRs** | [27](https://github.com/pizza-bot-app/pizza-bot/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 5% · CSS 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agentic-ai` `ai-agents` `amazon-bedrock` `deepagents` `electron` `human-in-the-loop` `langgraph` `local-first` `mcp` `typescript` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2026-06-26 |
| 📦 **Latest release** | [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 12.3 MB |
| 🌐 **Website** | https://github.com/pizza-bot-app/pizza-bot/releases |

## 📦 Recent releases

### [v1.3.0](https://github.com/pizza-bot-app/pizza-bot/releases/tag/v1.3.0) — Pizza Bot OSS 1.3.0
<sub>2026-11-10 · 2d ago</sub>

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
<sub>2026-09-19 · 1mo ago</sub>

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
| 2026-11-10 | [chore: release v1.3.0 (#192)](https://github.com/pizza-bot-app/pizza-bot/commit/7268cf14a509c37951b58e152d6688fe326ba4a3) | JoeDo |
| 2026-11-10 | [fix(deps): bump zod to 4.6.7 in the plugins lockfile (#191)](https://github.com/pizza-bot-app/pizza-bot/commit/d03efc44bf96b67da77f2d358118b8d503e91127) | JoeDo |
| 2026-11-07 | [feat(ci): publish the backend image for linux/arm64 as well as amd64](https://github.com/pizza-bot-app/pizza-bot/commit/e911bb8b8f20790820d9be6a8f0ceadf5af038e3) | kdgac |
| 2026-11-06 | [chore(deps): bump @vitest/mocker and vitest](https://github.com/pizza-bot-app/pizza-bot/commit/e50609f32d0967db83aba1d6d546111ffb2bd812) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump hono from 4.13.10 to 4.13.16](https://github.com/pizza-bot-app/pizza-bot/commit/cf1b910ae2422b89e0a7807c992dfc7e27f363c1) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump fast-uri from 3.1.8 to 3.1.9 in /plugins](https://github.com/pizza-bot-app/pizza-bot/commit/06db85748270d0947bf27345bdf73fdbe36c0128) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump fast-uri from 3.1.8 to 3.1.9](https://github.com/pizza-bot-app/pizza-bot/commit/2d70375254c56d71f9f157e9170793830ac12556) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump body-parser from 2.3.0 to 2.4.0 in /plugins](https://github.com/pizza-bot-app/pizza-bot/commit/eb8becf3809e7f49067667a373f65c386b990397) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump ip-address from 10.7.2 to 10.7.6](https://github.com/pizza-bot-app/pizza-bot/commit/51690a99e4990b301980a1d6433c4622f439c5fc) | dependabot[bot] |
| 2026-11-06 | [chore(deps): bump @hono/node-server from 2.1.1 to 2.1.6](https://github.com/pizza-bot-app/pizza-bot/commit/ab0f16407deb92f5bed8a7bd48f62df57aaa0dfe) | dependabot[bot] |

[See all commits ↗](https://github.com/pizza-bot-app/pizza-bot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pizza-bot-app/pizza-bot.git
```
