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
| ⭐ **Stars** | 134.1k |
| 🍴 **Forks** | 8.6k |
| 🐞 **Open issues + PRs** | [9.3k](https://github.com/stablyai/orca/issues) |
| 💻 **Languages** | TypeScript 96% · JavaScript 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `claude-code` `codex` `ghostty` `terminal` `opencode` `orchestration` `worktrees` `pi` `mobile-app` `agent-ide` `ai-agents` `yc-backed` `automation` `bot` `grok-bot` `hermes-agent` `muse` `openclaw` `runtime` `swarm` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-03-17 |
| 📦 **Latest release** | [v1.4.272](https://github.com/stablyai/orca/releases/tag/v1.4.272) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3259.9 MB |
| 🌐 **Website** | https://orca.dev |

## 📦 Recent releases

### [v1.4.272](https://github.com/stablyai/orca/releases/tag/v1.4.272)
<sub>2026-11-23 · today</sub>

> **More reliable bots that pick up where they left off ✨**
> - 🤖 **Bots recover more reliably after interruptions.** Conversations paused by usage limits can continue automatically after an account switch or restart. Resume works for chats interrupted by a crash or restart, and with **Resume work on restart** enabled, terminal workers can return to their saved conversations even if their terminals were lost. [Usage-limit recovery](https://github.com/stablyai/orca/pull/47221) · [Chat recovery](https://github.com/stablyai/orca/pull/47284) · [Worker recovery](https://github.com/stablyai/orca/pull/46643)
> - 🌐 **Use the same browser tools across machines.** Extensions such as 1Password now work in SSH workspace tabs and paired-server tabs opened on **This device**. Drop files from your desktop into server-streamed pages, and let agents on SSH hosts or paired servers upload and download files using paths on their own host. [Extensions](https://github.com/stablyai/orca/pull/47347) · [Drag and drop](https://github.com/stablyai/orca/pull/47357) · [SSH files](https://github.com/stablyai/orca/pull/47399) · [Paired-server files](https://github.com/stablyai/orca/pull/47264)
> - 💬 **Take a quick detour in chat.** On supported agents, type `/btw` or `/side` to mark a draft as a side chat. The composer’s worker count now reflects who’s actively working. [Side chat](https://github.com/stablyai/orca/pull/42129) · [Worker count](https://github.com/stablyai/orca/pull/47432)
> - 💤 **Free up idle resources.** Memory Saver now unloads hidden **This device** browser tabs and restores them when you or an agent needs them. An idle WSL distro can stop while Orca stays open and wake when you need it again. [Memory Saver](https://github.com/stablyai/orca/pull/47291) · [WSL](https://github.com/stablyai/orca/pull/47434)
> - 📱 **More room to work from your phone.** With the matching mobile build, you can post photos in group rooms, handle agent requests across paired computers from **Needs you**, and delete chats from an agent’s **Chats** tab. [Group photos](https://github.com/stablyai/orca/pull/47361) · [Agent requests](https://github.com/stablyai/orca/pull/47344) · [Delete chats](https://github.com/stablyai/orca/pull/47339)
> …

### [v1.4.271](https://github.com/stablyai/orca/releases/tag/v1.4.271)
<sub>2026-11-22 · today</sub>

> Following [1.4.269](https://github.com/stablyai/orca/releases/tag/v1.4.269), here is the next round of Orca. Bots reach Qwen Code and span your paired computers, the phone app manages agents end to end, and chats get lighter and quicker.
> **Bots across computers, a phone that runs your agents & snappier chats ✨**
> One bot group can now hold bots from your paired computers, bots can run on Qwen Code, chats can be deleted and continue on their own after a usage limit, and the phone app can share, import and connect agents without the desktop.
> - 🤖 **Bots across computers and agents:** One bot group can hold bots from paired computers, bots can run on Qwen Code, and group rooms hand follow-up turns to every member an agent @mentions.
> - 📱 **Run agents from your phone:** Edit an agent's automations, connect Slack, Linear, GitHub, Google and Composio, share an agent by link, import one from OpenClaw or Hermes, read its soul and manage its memory and skills, and hand a history session to another agent. These need the matching mobile build.
> - 💬 **Calmer chats:** Delete a chat, continue after a usage limit by default, list folders in the @ menu, and see quieter rows and a composer that keeps its welcome text clear.
> …

### [v1.4.269](https://github.com/stablyai/orca/releases/tag/v1.4.269)
<sub>2026-11-21 · yesterday</sub>

> Following [1.4.268](https://github.com/stablyai/orca/releases/tag/v1.4.268), here is the next round of Orca. Bots learn eight more agents, and the phone app catches up with the desktop.
> **Bots on eight more agents, a fuller phone & a quieter Mac ✨**
> Bots can now run on Kiro, Kimi Code, Auggie, Gemini CLI, Kilo Code, MiMo Code, Droid and Goose, Chat opens more agents directly, and the phone app can answer, approve and set up almost everything the desktop can.
> - 🤖 **Run bots on more agents:** Bots can run on Kiro, Kimi Code, Auggie, Gemini CLI, Kilo Code, MiMo Code, Droid and Goose. Chat can open Kiro, Auggie and Goose too, and Kiro chats run your own hooks.
> - 📱 **Do more from your phone:** Answer an agent's questions and Google or Composio setup cards from its chat, review tool approvals and access requests in Needs you, manage an agent's tools and webhooks, start a new chat from +, and browse a group's threads and items. These need the matching mobile build.
> - 🔐 **Antigravity, your way:** Google account users can pick Orca's built-in Google sign-in or the agy agent, and agy has its own Sign in in Settings.
> …

### [v1.4.268](https://github.com/stablyai/orca/releases/tag/v1.4.268)
<sub>2026-11-21 · 2d ago</sub>

> We shipped more than one release today. Check out [1.4.267](https://github.com/stablyai/orca/releases/tag/v1.4.267) and [1.4.266](https://github.com/stablyai/orca/releases/tag/v1.4.266) too.
> **Bots on more agents, richer Slack & a faster Orca ✨**
> Bots can now run on Cursor, GitHub Copilot and Hermes, Slack gets scheduling and canvases, and Orca does less work in the background so it feels quicker.
> - 🤖 **Run bots on more agents:** Bots can run on Cursor, GitHub Copilot and Hermes, and OpenCode 2.x bots get their standing instructions. New bots get an identity card, and Soul & Memory have redesigned editors.
> - 🖼️ **Send images and files:** Attach images and files in bot chats, group chats and item comments, including to a bot on a paired computer. Images on a Slack request reach the agent as images.
> - 💬 **More from Slack:** `orca slack post --at` schedules a post for later, and new `pin`, `canvas`, `list` and `scheduled` commands cover pins, canvases and lists. Connecting Slack takes the copied token without extra clicks, and mentions read as names.
> …

### [v1.4.267](https://github.com/stablyai/orca/releases/tag/v1.4.267)
<sub>2026-11-20 · 2d ago</sub>

> A quick patch on [1.4.266](https://github.com/stablyai/orca/releases/tag/v1.4.266) with stability and UI improvements.
> **What's new in 1.4.267**
> - 🛠️ **Steadier status bar:** Stability improvements. by @brennanb2025 in https://github.com/stablyai/orca/pull/44647
> - 💬 **Smoother chat:** Finished turns now settle cleanly. by @AmethystLiang in https://github.com/stablyai/orca/pull/45817
> - 🤖 **Cleaner Bots card:** The sidebar intro card is simpler and fits any width. by @AmethystLiang in https://github.com/stablyai/orca/pull/45442
> **Introducing Orca Bots (Beta) <img src="https://raw.githubusercontent.com/stablyai/orca/main/src/shared/bot-mascots/A1.webp" alt="Orca" width="36" height="36" valign="middle" />**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [feat(mobile): Connect Slack asks which workspace and explains what we…](https://github.com/stablyai/orca/commit/50e0185d13aa143eca4f11b3ca9f96b472156032) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): count workers and access requests in Home's Needs you (…](https://github.com/stablyai/orca/commit/2da3c78273670deae9467f57894ce6d126a0f92d) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): match the desktop's folded-list status marks and all-cl…](https://github.com/stablyai/orca/commit/9ba26f45022d3a84f60aec755f223c06609a3bb8) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): show workers' answered prompts as lines in the chat (#4…](https://github.com/stablyai/orca/commit/4bf513a25e4ad5b71e20636d308dabcc8f8e3f55) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): list tool sign-ins in Needs you and share connector rea…](https://github.com/stablyai/orca/commit/314ccdcae6bdb9a069bcd45599af8869794320b3) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): open the computer's sign-in tab on the phone when conne…](https://github.com/stablyai/orca/commit/21a4ae2f0e1fe86bc767e631df44cd9d2f79db61) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): ask who a new agent is and what it does when making one…](https://github.com/stablyai/orca/commit/1da194c4d00cb2ae9048cde734888d4c30f920fd) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): search on a computer's page finds agents and groups by …](https://github.com/stablyai/orca/commit/a9eef4066f86948b7179d938b3c6b204cfdfec37) | AmoabaKelvin |
| 2026-11-23 | [feat(mobile): post in a group with agents on other computers from the…](https://github.com/stablyai/orca/commit/c9196eecde4844c75af807b524b4436064357826) | AmoabaKelvin |
| 2026-11-23 | [fix(mobile): say which Orca to update when neither the phone nor the …](https://github.com/stablyai/orca/commit/3b74898203e84f72d3d404215c1757d03d8a5d34) | AmoabaKelvin |

[See all commits ↗](https://github.com/stablyai/orca/commits)

## ⬇️ Get it

```bash
git clone https://github.com/stablyai/orca.git
```
