# stablyai/orca

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/stablyai/orca)

> Orca lets you run a fleet of bots with your own subscription (e.g. Claude Code, Grok, Agy, Codex). Available on desktop, mobile and remote runtime.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Run a fleet of coding agents (Claude Code, Codex) in parallel |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 135.6k |
| 🍴 **Forks** | 8.7k |
| 🐞 **Open issues + PRs** | [9.6k](https://github.com/stablyai/orca/issues) |
| 💻 **Languages** | TypeScript 96% · JavaScript 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `claude-code` `codex` `ghostty` `terminal` `opencode` `orchestration` `worktrees` `pi` `mobile-app` `agent-ide` `ai-agents` `yc-backed` `automation` `bot` `grok-bot` `hermes-agent` `muse` `openclaw` `runtime` `swarm` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-03-17 |
| 📦 **Latest release** | [v1.4.273](https://github.com/stablyai/orca/releases/tag/v1.4.273) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3343.9 MB |
| 🌐 **Website** | https://orca.dev |

## 📦 Recent releases

### [v1.4.273](https://github.com/stablyai/orca/releases/tag/v1.4.273)
<sub>2026-11-24 · today</sub>

> Thank you for using Orca and sharing your feedback. ❤️
> **Clearer bot items, more controls on the phone & smoother browser sessions ✨**
> - 🤖 **See what needs attention.** Bot panels show upcoming runs. Item links preview GitHub pull requests and issues on hover, and questions retain their labels when an answer is waiting to send.
> - 📱 **Manage more from the phone.** Open Google, GitHub and Linear account controls, find agents and groups by name, and post to groups across computers.
> - 🌐 **Work with streamed browser pages.** Scroll more smoothly over slower links, open select menus from the keyboard, and print a streamed page to PDF on the desktop.
> - 🖥️ **More room for workspace tools.** App-rail destinations fill the window. The usage meter stays visible in chat and updates with less background work when a workspace changes.
> …

### [android-v0.0.70](https://github.com/stablyai/orca/releases/tag/android-v0.0.70) — Orca Mobile Android android-v0.0.70 _(pre-release)_
<sub>2026-11-24 · today</sub>

> Thank you so much for using Orca and for your continued support! ❤️
> **The short version**
> 0.0.70 builds on 0.0.69. For the big picture, read the [0.0.69 notes](https://github.com/stablyai/orca/releases/tag/android-v0.0.69). This release adds:
> - **Available on more devices:** Orca no longer counts Wi-Fi or a portrait screen as required, so Play offers it on devices without them. This also cleared the check that stopped 0.0.69 from going to Play review.
> - **More of your agents from the phone:** Manage Google, GitHub and Linear accounts on connector pages, and pick the workspace when you connect Slack. A new agent asks who it is and what it does. Search a computer's page for agents and groups.
> - **Needs you and group rooms:** Needs you counts workers and access requests, and shows the question a chat stopped on. Post in a group with agents on other computers, and group posts can carry photos.
> …

### [android-v0.0.69](https://github.com/stablyai/orca/releases/tag/android-v0.0.69) — Orca Mobile Android android-v0.0.69 _(pre-release)_
<sub>2026-11-23 · today</sub>

> Thank you so much for using Orca and for your continued support! ❤️
> **The short version**
> - **Agents from your phone:** Set up an agent's automations, webhooks, tools, connectors and settings from the phone, on Settings pages laid out like the desktop's. Connect Slack, Linear, GitHub, Google and Composio, edit an agent's memory and skills, share it by link, or import one from another app.
> - **Group rooms and items:** A group's room now has threads and one combined Items list, with next and previous on item pages. Answer an agent's item questions from the chat answer card, add photos to comments, and see answers from agents on other computers.
> - **Needs you and notifications:** Tool approvals, access requests and connectors that need a sign-in now wait in one Needs you list. You get a push when an agent asks you something on an item, and Orca tells you when a wrong computer clock is blocking pushes.
> - **Chat:** Answer workers' permission prompts in the coordinator chat, mention an agent or one of its chats with @, and hand a History session to another agent. Chat cards open their page on the phone, and the chat chip shows Claude's current model and effort.
> …

### [v1.4.272](https://github.com/stablyai/orca/releases/tag/v1.4.272)
<sub>2026-11-23 · yesterday</sub>

> **More reliable bots that pick up where they left off ✨**
> - 🤖 **Bots recover more reliably after interruptions.** Conversations paused by usage limits can continue automatically after an account switch or restart. Resume works for chats interrupted by a crash or restart, and with **Resume work on restart** enabled, terminal workers can return to their saved conversations even if their terminals were lost. [Usage-limit recovery](https://github.com/stablyai/orca/pull/47221) · [Chat recovery](https://github.com/stablyai/orca/pull/47284) · [Worker recovery](https://github.com/stablyai/orca/pull/46643)
> - 🌐 **Use the same browser tools across machines.** Extensions such as 1Password now work in SSH workspace tabs and paired-server tabs opened on **This device**. Drop files from your desktop into server-streamed pages, and let agents on SSH hosts or paired servers upload and download files using paths on their own host. [Extensions](https://github.com/stablyai/orca/pull/47347) · [Drag and drop](https://github.com/stablyai/orca/pull/47357) · [SSH files](https://github.com/stablyai/orca/pull/47399) · [Paired-server files](https://github.com/stablyai/orca/pull/47264)
> - 💬 **Take a quick detour in chat.** On supported agents, type `/btw` or `/side` to mark a draft as a side chat. The composer’s worker count now reflects who’s actively working. [Side chat](https://github.com/stablyai/orca/pull/42129) · [Worker count](https://github.com/stablyai/orca/pull/47432)
> - 💤 **Free up idle resources.** Memory Saver now unloads hidden **This device** browser tabs and restores them when you or an agent needs them. An idle WSL distro can stop while Orca stays open and wake when you need it again. [Memory Saver](https://github.com/stablyai/orca/pull/47291) · [WSL](https://github.com/stablyai/orca/pull/47434)
> - 📱 **More room to work from your phone.** With the matching mobile build, you can post photos in group rooms, handle agent requests across paired computers from **Needs you**, and delete chats from an agent’s **Chats** tab. [Group photos](https://github.com/stablyai/orca/pull/47361) · [Agent requests](https://github.com/stablyai/orca/pull/47344) · [Delete chats](https://github.com/stablyai/orca/pull/47339)
> …

### [v1.4.271](https://github.com/stablyai/orca/releases/tag/v1.4.271)
<sub>2026-11-22 · yesterday</sub>

> Following [1.4.269](https://github.com/stablyai/orca/releases/tag/v1.4.269), here is the next round of Orca. Bots reach Qwen Code and span your paired computers, the phone app manages agents end to end, and chats get lighter and quicker.
> **Bots across computers, a phone that runs your agents & snappier chats ✨**
> One bot group can now hold bots from your paired computers, bots can run on Qwen Code, chats can be deleted and continue on their own after a usage limit, and the phone app can share, import and connect agents without the desktop.
> - 🤖 **Bots across computers and agents:** One bot group can hold bots from paired computers, bots can run on Qwen Code, and group rooms hand follow-up turns to every member an agent @mentions.
> - 📱 **Run agents from your phone:** Edit an agent's automations, connect Slack, Linear, GitHub, Google and Composio, share an agent by link, import one from OpenClaw or Hermes, read its soul and manage its memory and skills, and hand a history session to another agent. These need the matching mobile build.
> - 💬 **Calmer chats:** Delete a chat, continue after a usage limit by default, list folders in the @ menu, and see quieter rows and a composer that keeps its welcome text clear.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Group the GitHub setup dialog's repositories by organization (#48351)](https://github.com/stablyai/orca/commit/e89b3a355bcda5b9432609e739edbf34e225ebef) | AmethystLiang |
| 2026-11-24 | [fix(agent-cli-update): re-check CLI updates when the status bar popov…](https://github.com/stablyai/orca/commit/60aa5a5552c7001015ff7cacbc3b6a1c50e8455a) | 2SinceJuly |
| 2026-11-24 | [fix(connectors): keep webhook fields, actions and recent calls readab…](https://github.com/stablyai/orca/commit/55049f5745a7a6c1755e6d9c6641bb02f158fcc5) | nwparker |
| 2026-11-24 | [fix(antigravity): read usage through Orca's managed agy when it is no…](https://github.com/stablyai/orca/commit/deb818a3741bc23cdf9c0384f267fca8fcb0af5a) | Pr1p |
| 2026-11-24 | [fix(bots): keep Cancel inside the Import dialog when the bot name is …](https://github.com/stablyai/orca/commit/cd5c7e790a06b29d3fac77031db0c8227b94ee7f) | akira-fukue |
| 2026-11-24 | [fix(windows): resolve System32 paths through a validated SystemRoot (…](https://github.com/stablyai/orca/commit/150d1c3a18102c7b58c3fbb152f7d1a14e8aa31b) | Pr1p |
| 2026-11-24 | [feat(ports): restore a paired server's port forwards after a restart …](https://github.com/stablyai/orca/commit/d889dccbc35b3e812ab8378ab442da2450ba30c4) | AmoabaKelvin |
| 2026-11-24 | [fix(file-explorer): keep cached ignored paths when switching worktree…](https://github.com/stablyai/orca/commit/8b301fdc111a3d595b20df560fcf858522d9b541) | nwparker |
| 2026-11-24 | [fix(mobile): create an agent from a link with the picture its preview…](https://github.com/stablyai/orca/commit/53f86a8a832ffae6a86eae044f207a95b3c05756) | AmoabaKelvin |
| 2026-11-24 | [fix(google): a Google sign-in started from the phone survives the pho…](https://github.com/stablyai/orca/commit/9d5a6bf3e9e34ebc199db28dbcfb0d48d2f88e13) | AmoabaKelvin |

[See all commits ↗](https://github.com/stablyai/orca/commits)

## ⬇️ Get it

```bash
git clone https://github.com/stablyai/orca.git
```
