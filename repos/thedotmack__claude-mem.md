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
| ⭐ **Stars** | 120.1k |
| 🍴 **Forks** | 10.5k |
| 🐞 **Open issues + PRs** | [104](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 30% · Python 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v17.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.2) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 946.3 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v17.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.2)
<sub>2026-11-26 · today</sub>

> **Setup fixes**
> - **Setup no longer ends in dead ends** (#6501, @thedotmack). A few setup paths could never finish, or finished without syncing:
>   - When cmem.ai refused a new install for a clear reason (rate limit or daily limit), the next run kept failing without asking again. That refusal is now cleared, so the next run asks again. Anything less certain keeps today's behaviour, so no second identity is made.
>   - After you approved Cloud Sync, a worker that was already running without sync settings only printed a warning, so nothing synced until some later restart. Setup now waits for background work to finish (up to 5 minutes) and restarts the worker once. A worker run by your own process manager (`CLAUDE_MEM_WORKER_AUTOSTART=false` or `CLAUDE_MEM_WORKER_URL`) is left alone, and you are told to restart it there.
>   - Right after checkout, setup showed the $30/month hosted plan before you had a single synced memory. That step is gone. My Work shows it as a banner you can dismiss, only after this computer's first memory syncs, and never to people who kept Pro or already have a hosted observer.
>   - The "sign in later" link at the end of install started a pairing nothing ever checked, so it never worked. It is removed.
> …

### [v17.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.1)
<sub>2026-11-26 · today</sub>

> **Critical fixes**
> - **The setup page shows your cmem.ai device code, and reopening after it expires gets a fresh one** (#6500, @thedotmack). After you pick Cloud Sync and start the free trial, cmem.ai asks for a device code. That code was only printed in the terminal, which most people never look at because setup runs in the browser. The checkout step now shows **Your device code** with a copy button, next to "Waiting for this device to connect…". If the code expired, **Reopen** sent you back to a dead link with the same expired code. It now starts a new pairing with a new code. The code is never put in a URL, log line or analytics event, and the page reads it from a route only this machine can reach.
> - **Windows: My Work reads no longer hang when a recent Bash command holds regex-shaped text** (#6471, thanks @zhangkom, closes #6470 reported by @ingermaa). Shell text such as `s.replace(/\r\n/g, ' ')` was taken for an absolute path. Resolving `/\r\n/g,` could produce a UNC network path, and project discovery stalled while Windows tried a network lookup. Text that starts with a slash and a backslash is now ignored on Windows. Drive paths and POSIX paths are read as before.
> - **Windows: OMP capture and Screenpipe saves reach the worker again** (#6481, thanks @AyhamJo7, refs #6477 reported by @Jumpstile). On Windows the OMP hook and the Screenpipe skill posted to port 37777 by default. The worker picks its default port from a hash of the data folder, so on a default Windows install nothing listened on 37777 and OMP sessions were not recorded, with no error shown. Both now work out the default port the same way the worker does. A port saved in `settings.json` is still used first, and macOS and Linux are unchanged. **OMP users on Windows: run `npx claude-mem install --ide omp` once after updating.** The OMP hook is a copied file, so an update alone does not replace it.
> **Fixes**
> - **Claude provider: condensing an oversized field now follows `CLAUDE_MEM_OBSERVER_MAX_OUTPUT_TOKENS`** (#6508, thanks @0xABCD01, closes #6503 reported by @JonT6). The setting sized the condense request on the HTTP providers, but the Claude call never passed it. The request asked for the full 12,800 characters, and the extra output was billed and then clipped. At the default setting the Claude condense request now asks for 8,192 characters, the same as the HTTP providers. The Agent SDK has no per-request output cap, so on this path the setting sizes the request and is not a hard limit.
> …

### [v17.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v17.0.0)
<sub>2026-11-26 · yesterday</sub>

> **Review Stack in My Work**
> - Open **Review Stack** in local My Work or in your signed-in Cloud Sync Work View to review files, images, links and other work your agents submit. Browse lets you flip through a stack. Switch to Work to mark a card Seen, save it for later or leave a follow-up.
> - Hold **Seen** for three seconds to mark a whole Focus Area seen. You can undo the group action, revisit a card and find saved items and follow-ups across paired devices.
> **Claude-Mem Messages for macOS**
> - Choose Messages on your Mac or an authorized Photon iMessage line in the app. For Mac Messages, select the chats and the topics to watch. For Photon, add the line to the groups you want to observe. New group conversations become searchable Claude-Mem notes in a project for each chat.
> - The read-only observer starts with new messages when you begin listening. From Terminal, use `npx claude-mem imessage mac` to check access, list chats, save picks, listen and import contact names. `npx claude-mem imessage setup` configures the Photon line.
> …

### [v16.2.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.2.1)
<sub>2026-11-26 · yesterday</sub>

> - **After a release ships, the childhood skill now watches it for 24 hours by default instead of 30 minutes** (#6480). A full day catches slow npm registry updates, late CI and reports from users in other time zones. Checks are close together in the first hour, every 30 minutes until hour 6, then every 2 hours, with a final sweep at the 24-hour mark. A new problem brings that surface back to close checks until it settles. Between checks the agent uses a scheduled check or wake-up instead of holding a session open, and if it can't come back it reports the window as still open, not as clean.

### [v16.2.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.2.0)
<sub>2026-11-26 · yesterday</sub>

> **iMessage group chats**
> - **The iMessage group chat observer keeps Claude-Mem notes on a group chat** (#6457). Add a Photon iMessage line to the group and run `npx claude-mem imessage setup`. Each group chat gets its own Claude-Mem project with what the group decided, planned, asked for and shared, and who said what. It only reads: it never sends, reacts or changes a group. See [docs/imessage-group-observer.md](imessage-group-observer.md).
> **iMessage on your Mac**
> - **Claude-Mem Messages, a Mac app that keeps notes on the iMessage chats you pick** (#6482). It lists your chats and group chats from the Messages app on your own Mac. Tick the ones to observe and write what to watch for in each ("plans and who's bringing what", "money: who paid, who owes"). New messages in those chats become notes in one Claude-Mem project per chat. It only reads: it never sends, reacts or changes a chat, and nothing is added to the group. Only new messages are read, from when it starts listening. The app needs Full Disk Access, and its setup screen walks you through turning it on. Download the unsigned build from the "iMessage Mac app" check, or build it with `integrations/imessage-mac/scripts/build-app.sh`. See [docs/imessage-mac-app.md](imessage-mac-app.md).
> - **`claude-mem imessage mac` commands** do the same from Terminal: `check`, `chats`, `pick` (with `--focus` for what to watch for), `observe` and `contacts`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [feat(launcher): add CLAUDE_MEM_SKIP_SHELL_RC to skip shell rc edits (…](https://github.com/thedotmack/claude-mem/commit/ad682a38da4cdbd2076451f595adc7db512a626c) | chck |
| 2026-11-26 | [chore: promote 17.0.2 for auto-update](https://github.com/thedotmack/claude-mem/commit/57fe84a4e7e4b6d2f6455acbc43b9bd13c585663) | claude |
| 2026-11-26 | [fix(chroma): freeze the chroma-mcp resolve with --exclude-newer so uv…](https://github.com/thedotmack/claude-mem/commit/730990b6e9de498aa7cc7dd554e9c68b5bf058db) | chris-yyau |
| 2026-11-26 | [docs: update changelog for 17.0.2](https://github.com/thedotmack/claude-mem/commit/09b16ae8c0dd34948c9294dbfe00e012d02f2cb9) | claude |
| 2026-11-26 | [chore: bump version to 17.0.2 (#6519)](https://github.com/thedotmack/claude-mem/commit/019a36df177c9e952a125d9be4a32e23dd59cbf9) | thedotmack |
| 2026-11-26 | [feat: read observer model from host OpenCode config when opted in (#6…](https://github.com/thedotmack/claude-mem/commit/7e5441bc60907eddfb89e7df4e1ff7563bff8ed2) | maxmad64bis |
| 2026-11-26 | [fix(work-view): attribute requests to their session's agent after it …](https://github.com/thedotmack/claude-mem/commit/aa7a377ad726a6e45fa847be0ad51c9681346927) | 0xABCD01 |
| 2026-11-26 | [fix(backup): publish pre-restore copies after the WAL transfer comple…](https://github.com/thedotmack/claude-mem/commit/2261078f16696ac9236b1e2e48a58216665eb1fd) | ZedingZhang |
| 2026-11-26 | [Add Russian localization for the viewer, My Work, settings, and setup…](https://github.com/thedotmack/claude-mem/commit/ee9ee88401c7fc4cc3397de258c85f47dc02a1f3) | diarworld |
| 2026-11-26 | [fix(work-view): a group the model leaves unreviewed no longer fails t…](https://github.com/thedotmack/claude-mem/commit/fb126b09fc4951d1573082d6ec303130e789ba10) | thedotmack |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
