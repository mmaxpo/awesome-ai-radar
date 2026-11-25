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
| ⭐ **Stars** | 137.5k |
| 🍴 **Forks** | 8.8k |
| 🐞 **Open issues + PRs** | [9.8k](https://github.com/stablyai/orca/issues) |
| 💻 **Languages** | TypeScript 96% · JavaScript 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `claude-code` `codex` `ghostty` `terminal` `opencode` `orchestration` `worktrees` `pi` `mobile-app` `agent-ide` `ai-agents` `yc-backed` `automation` `bot` `grok-bot` `hermes-agent` `muse` `openclaw` `runtime` `swarm` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-03-17 |
| 📦 **Latest release** | [v1.4.274](https://github.com/stablyai/orca/releases/tag/v1.4.274) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3459.1 MB |
| 🌐 **Website** | https://orca.dev |

## 📦 Recent releases

### [v1.4.274](https://github.com/stablyai/orca/releases/tag/v1.4.274)
<sub>2026-11-24 · today</sub>

> **App Rail is on by default for new users**
> This minor update enables App Rail for new Orca users. App Rail saves sidebar space by putting app navigation in a compact icon rail. Existing users can turn it on under **Settings > Experimental > App rail**.
> ![App Rail in the Orca sidebar](https://github.com/stablyai/orca/releases/download/v1.4.274/app-rail.png)
> **In v1.4.273**
> Bot panels show upcoming runs and clearer item questions, the mobile app adds account and group controls, and streamed browser pages scroll more smoothly. [Read the full v1.4.273 release notes](https://github.com/stablyai/orca/releases/tag/v1.4.273).

### [v1.4.273](https://github.com/stablyai/orca/releases/tag/v1.4.273)
<sub>2026-11-24 · yesterday</sub>

> Thank you for using Orca and sharing your feedback. ❤️
> **Clearer bot items, more controls on the phone & smoother browser sessions ✨**
> - 🤖 **See what needs attention.** Bot panels show upcoming runs. Item links preview GitHub pull requests and issues on hover, and questions retain their labels when an answer is waiting to send.
> - 📱 **Manage more from the phone.** Open Google, GitHub and Linear account controls, find agents and groups by name, and post to groups across computers.
> - 🌐 **Work with streamed browser pages.** Scroll more smoothly over slower links, open select menus from the keyboard, and print a streamed page to PDF on the desktop.
> - 🖥️ **More room for workspace tools.** App-rail destinations fill the window. The usage meter stays visible in chat and updates with less background work when a workspace changes.
> …

### [android-v0.0.70](https://github.com/stablyai/orca/releases/tag/android-v0.0.70) — Orca Mobile Android android-v0.0.70 _(pre-release)_
<sub>2026-11-24 · yesterday</sub>

> Thank you so much for using Orca and for your continued support! ❤️
> **The short version**
> 0.0.70 builds on 0.0.69. For the big picture, read the [0.0.69 notes](https://github.com/stablyai/orca/releases/tag/android-v0.0.69). This release adds:
> - **Available on more devices:** Orca no longer counts Wi-Fi or a portrait screen as required, so Play offers it on devices without them. This also cleared the check that stopped 0.0.69 from going to Play review.
> - **More of your agents from the phone:** Manage Google, GitHub and Linear accounts on connector pages, and pick the workspace when you connect Slack. A new agent asks who it is and what it does. Search a computer's page for agents and groups.
> - **Needs you and group rooms:** Needs you counts workers and access requests, and shows the question a chat stopped on. Post in a group with agents on other computers, and group posts can carry photos.
> …

### [android-v0.0.69](https://github.com/stablyai/orca/releases/tag/android-v0.0.69) — Orca Mobile Android android-v0.0.69 _(pre-release)_
<sub>2026-11-23 · yesterday</sub>

> Thank you so much for using Orca and for your continued support! ❤️
> **The short version**
> - **Agents from your phone:** Set up an agent's automations, webhooks, tools, connectors and settings from the phone, on Settings pages laid out like the desktop's. Connect Slack, Linear, GitHub, Google and Composio, edit an agent's memory and skills, share it by link, or import one from another app.
> - **Group rooms and items:** A group's room now has threads and one combined Items list, with next and previous on item pages. Answer an agent's item questions from the chat answer card, add photos to comments, and see answers from agents on other computers.
> - **Needs you and notifications:** Tool approvals, access requests and connectors that need a sign-in now wait in one Needs you list. You get a push when an agent asks you something on an item, and Orca tells you when a wrong computer clock is blocking pushes.
> - **Chat:** Answer workers' permission prompts in the coordinator chat, mention an agent or one of its chats with @, and hand a History session to another agent. Chat cards open their page on the phone, and the chat chip shows Claude's current model and effort.
> …

### [v1.4.272](https://github.com/stablyai/orca/releases/tag/v1.4.272)
<sub>2026-11-23 · 2d ago</sub>

> **More reliable bots that pick up where they left off ✨**
> - 🤖 **Bots recover more reliably after interruptions.** Conversations paused by usage limits can continue automatically after an account switch or restart. Resume works for chats interrupted by a crash or restart, and with **Resume work on restart** enabled, terminal workers can return to their saved conversations even if their terminals were lost. [Usage-limit recovery](https://github.com/stablyai/orca/pull/47221) · [Chat recovery](https://github.com/stablyai/orca/pull/47284) · [Worker recovery](https://github.com/stablyai/orca/pull/46643)
> - 🌐 **Use the same browser tools across machines.** Extensions such as 1Password now work in SSH workspace tabs and paired-server tabs opened on **This device**. Drop files from your desktop into server-streamed pages, and let agents on SSH hosts or paired servers upload and download files using paths on their own host. [Extensions](https://github.com/stablyai/orca/pull/47347) · [Drag and drop](https://github.com/stablyai/orca/pull/47357) · [SSH files](https://github.com/stablyai/orca/pull/47399) · [Paired-server files](https://github.com/stablyai/orca/pull/47264)
> - 💬 **Take a quick detour in chat.** On supported agents, type `/btw` or `/side` to mark a draft as a side chat. The composer’s worker count now reflects who’s actively working. [Side chat](https://github.com/stablyai/orca/pull/42129) · [Worker count](https://github.com/stablyai/orca/pull/47432)
> - 💤 **Free up idle resources.** Memory Saver now unloads hidden **This device** browser tabs and restores them when you or an agent needs them. An idle WSL distro can stop while Orca stays open and wake when you need it again. [Memory Saver](https://github.com/stablyai/orca/pull/47291) · [WSL](https://github.com/stablyai/orca/pull/47434)
> - 📱 **More room to work from your phone.** With the matching mobile build, you can post photos in group rooms, handle agent requests across paired computers from **Needs you**, and delete chats from an agent’s **Chats** tab. [Group photos](https://github.com/stablyai/orca/pull/47361) · [Agent requests](https://github.com/stablyai/orca/pull/47344) · [Delete chats](https://github.com/stablyai/orca/pull/47339)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [fix(bots): include paired members in group Home items and badge (#49005)](https://github.com/stablyai/orca/commit/b96b5eb416797afb7ccb29724fcd2ac4d5d3ca67) | lafraia |
| 2026-11-25 | [fix(i18n): translate missing Spanish native-chat strings for messages…](https://github.com/stablyai/orca/commit/bc471d51c9061fde453ac35656631ecf8dffecda) | yohangwak |
| 2026-11-25 | [fix(mobile-status): stamp done frames with pane status-change time so…](https://github.com/stablyai/orca/commit/b7b2131a5671bf927f9d0ef1f4167b30e93fa714) | mmarabel |
| 2026-11-25 | [fix(i18n): translate 104 missing Japanese native-chat strings (#48980)](https://github.com/stablyai/orca/commit/cf2801a5ccfcd5df670139335c68bebdce4eb30b) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 189 missing German native-chat strings for messa…](https://github.com/stablyai/orca/commit/b5804728ddd09e255bdfb34fba4260949ec0fd14) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 156 missing Portuguese native-chat strings for m…](https://github.com/stablyai/orca/commit/b51c880e8b68f5285bf2e40c413c6e79a8b0cbeb) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 185 missing Traditional Chinese native-chat stri…](https://github.com/stablyai/orca/commit/cef2f9bdbabdc14d0a604b86f576857110c2ef32) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 188 missing Russian native-chat strings for mess…](https://github.com/stablyai/orca/commit/36fd3d769e50b8afd8402170fe4dc965c982924d) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 184 missing French native-chat strings for messa…](https://github.com/stablyai/orca/commit/c3e9664be2dbce3bd28eadf51c6b239ae306be01) | yohangwak |
| 2026-11-25 | [fix(i18n): translate 18 missing Simplified Chinese native-chat string…](https://github.com/stablyai/orca/commit/42ba9b010e12954e99de009c1381f812416322bb) | yohangwak |

[See all commits ↗](https://github.com/stablyai/orca/commits)

## ⬇️ Get it

```bash
git clone https://github.com/stablyai/orca.git
```
