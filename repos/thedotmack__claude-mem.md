# thedotmack/claude-mem

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/thedotmack/claude-mem)

> Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Long-term memory for Claude Code |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 119.9k |
| 🍴 **Forks** | 10.4k |
| 🐞 **Open issues + PRs** | [117](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 65% · JavaScript 30% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v17.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.0) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 936.2 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v17.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.0)
<sub>2026-11-26 · today</sub>

> **Review Stack in My Work**
> - Open **Review Stack** in local My Work or in your signed-in Cloud Sync Work View to review files, images, links and other work your agents submit. Browse lets you flip through a stack. Switch to Work to mark a card Seen, save it for later or leave a follow-up.
> - Hold **Seen** for three seconds to mark a whole Focus Area seen. You can undo the group action, revisit a card and find saved items and follow-ups across paired devices.
> **Claude-Mem Messages for macOS**
> - Choose Messages on your Mac or an authorized Photon iMessage line in the app. For Mac Messages, select the chats and the topics to watch. For Photon, add the line to the groups you want to observe. New group conversations become searchable Claude-Mem notes in a project for each chat.
> - The read-only observer starts with new messages when you begin listening. From Terminal, use `npx claude-mem imessage mac` to check access, list chats, save picks, listen and import contact names. `npx claude-mem imessage setup` configures the Photon line.
> …

### [v16.2.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.2.1)
<sub>2026-11-26 · today</sub>

> - **After a release ships, the childhood skill now watches it for 24 hours by default instead of 30 minutes** (#6480). A full day catches slow npm registry updates, late CI and reports from users in other time zones. Checks are close together in the first hour, every 30 minutes until hour 6, then every 2 hours, with a final sweep at the 24-hour mark. A new problem brings that surface back to close checks until it settles. Between checks the agent uses a scheduled check or wake-up instead of holding a session open, and if it can't come back it reports the window as still open, not as clean.

### [v16.2.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.2.0)
<sub>2026-11-26 · today</sub>

> **iMessage group chats**
> - **The iMessage group chat observer keeps Claude-Mem notes on a group chat** (#6457). Add a Photon iMessage line to the group and run `npx claude-mem imessage setup`. Each group chat gets its own Claude-Mem project with what the group decided, planned, asked for and shared, and who said what. It only reads: it never sends, reacts or changes a group. See [docs/imessage-group-observer.md](imessage-group-observer.md).
> **iMessage on your Mac**
> - **Claude-Mem Messages, a Mac app that keeps notes on the iMessage chats you pick** (#6482). It lists your chats and group chats from the Messages app on your own Mac. Tick the ones to observe and write what to watch for in each ("plans and who's bringing what", "money: who paid, who owes"). New messages in those chats become notes in one Claude-Mem project per chat. It only reads: it never sends, reacts or changes a chat, and nothing is added to the group. Only new messages are read, from when it starts listening. The app needs Full Disk Access, and its setup screen walks you through turning it on. Download the unsigned build from the "iMessage Mac app" check, or build it with `integrations/imessage-mac/scripts/build-app.sh`. See [docs/imessage-mac-app.md](imessage-mac-app.md).
> - **`claude-mem imessage mac` commands** do the same from Terminal: `check`, `chats`, `pick` (with `--focus` for what to watch for), `observe` and `contacts`.

### [v16.1.6](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.6)
<sub>2026-11-26 · today</sub>

> - Cloud Sync trial links now identify whether a user followed the GitHub README, the local timeline invitation, the startup message or the installer’s terminal link.

### [v16.1.5](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.5)
<sub>2026-11-25 · yesterday</sub>

> - Eligible existing installs receive a dated holiday Cloud Sync offer from the new Messages from Claude-Mem queue on their next interactive startup. Each installation records the dispatch time locally. Agents can optionally acknowledge sharing the message with `claude-mem messages acknowledge <message-id>`.
> - The local memory timeline now offers eligible Claude-Mem users a 30-day Cloud Sync and remote Work Viewer trial with no credit card required. Dismissing the invitation hides it on that browser.
> - The remote Work Viewer now guides trial users through six workflows, including cross-agent handoffs, decision tracing, and optional weekday briefings and Friday reviews.
> - The Cloud Sync giveaway GIF at the top of the project README links to cmem.ai.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [chore: promote 17.0.0 for auto-update](https://github.com/thedotmack/claude-mem/commit/9b3b78dfa53f80e7c9c447b9269ceda255ee99d9) | thedotmack |
| 2026-11-26 | [Merge pull request #6491 from thedotmack/feat/v17-work-view-review](https://github.com/thedotmack/claude-mem/commit/94474143a3d5bb6f1f25d8049194d675d724310e) | thedotmack |
| 2026-11-26 | [build: prepare release bundles](https://github.com/thedotmack/claude-mem/commit/6b1514951af175d17675c1fc9a891f8dae627692) | github-actions[bot] |
| 2026-11-26 | [fix(work-view): use shared buttons for review modes and previews](https://github.com/thedotmack/claude-mem/commit/0aabfe7a2373dd273fb663e846710149a5e2fd9d) | thedotmack |
| 2026-11-26 | [fix(release): refresh staged release notes on a full workflow retry](https://github.com/thedotmack/claude-mem/commit/ee50d4faea43f631c8d813b2cfaa6c08ff089ae0) | thedotmack |
| 2026-11-26 | [fix(release): verify the Mac download before publishing tagged versions](https://github.com/thedotmack/claude-mem/commit/b37b8aa956f63056fca4819d0c5359d8e9785642) | thedotmack |
| 2026-11-26 | [build: prepare release bundles](https://github.com/thedotmack/claude-mem/commit/6e1842faa36c51cfcc4e1bc2429f880d79b73a44) | github-actions[bot] |
| 2026-11-26 | [Refresh open review decks and keep authenticated thumbnails with thei…](https://github.com/thedotmack/claude-mem/commit/d720ae371503fa9c3c95ff6621ca893c918fc599) | thedotmack |
| 2026-11-26 | [chore: promote 16.2.1 for auto-update and date its changelog entry](https://github.com/thedotmack/claude-mem/commit/50e3bc6f6d70ac1e80b884ff0a48618f9728fdf7) | claude |
| 2026-11-26 | [Merge the released Mac observer and 16.2.1 history into Claude-Mem 17](https://github.com/thedotmack/claude-mem/commit/ab384debd74c175587f0bf5d399b9a6ff24c7fb9) | thedotmack |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
