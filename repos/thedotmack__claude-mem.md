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
| ⭐ **Stars** | 118.3k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [78](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 895.1 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.1)
<sub>2026-11-19 · today</sub>

> **Critical fixes**
> - **Signing in to Codex works again on Windows while claude-mem runs** (#6332, thanks @ffe111, closes #6331). The private Codex home that claude-mem's app-server uses got its `auth.json` through a hard link to your real `~/.codex/auth.json`. Codex refuses to replace a credential file with more than one hard link (`persist_failed: atomic credential replacement does not support hard-linked files`), so `codex login` and token refresh failed for as long as that home existed. The private home now gets a symlink, which Codex follows. Only on Windows, and only when a symlink is not permitted (no Developer Mode or elevation), it gets a private copy instead. Any other error still fails loudly.
> - **A probe answered with `<skip_summary/>` ends the quota cooldown** (#6324, thanks @vaibhav375, closes #6322). After a quota hit, the worker probes the provider and clears the cooldown once a probe stores a memory. A probe the provider answered with a valid `<skip_summary/>` stores nothing, so the cooldown never cleared and the worker re-probed every 5 minutes for as long as that session only skipped. A valid skip now releases the cooldown too, on both the store path and the early path before the memory session id is known. Observer-health success still needs a real store.
> **Fixes**
> - **Search falls back to SQLite instead of failing when Chroma is slow** (#6327, thanks @REI-330, closes #6323). The MCP client gives a search 30 s, while each Chroma read waited up to 60 s, so a slow query was still running when the caller gave up and the SQLite/FTS5 fallback never ran. A search now shares one 20 s budget across its Chroma reads and falls back when it runs out, without restarting a healthy chroma-mcp.
> - **Chroma rebuilds no longer hold a core for hours** (#6299, thanks @srieteja). A full backfill now pauses after each row for its write time times `CLAUDE_MEM_CHROMA_BACKFILL_PAUSE_RATIO` (default 1, 0 turns it off), and chroma-mcp starts under `nice` (`CLAUDE_MEM_CHROMA_PROCESS_NICE`, default 10) outside Windows. Live sync is unchanged.
> …

### [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0)
<sub>2026-11-18 · yesterday</sub>

> **My Work puts what needs you first**
> My Work, the page that shows what your agents are doing, was rebuilt from a full UI review (#6210, #6304). What needs you sits at the top, long lists fold, and every page works on a phone, by keyboard and with a screen reader.
> - **What needs you comes first.** On the home page the first request waiting on you is at the top, with the one orange button on the screen. Requests are one-line rows; Idle and Shipped fold to one row each, with their counts.
> - **Shorter pages.** On a real install: home is about 2,600px tall instead of 5,138; the List opens with 5 rows instead of 195; My Rules is about 4,400px instead of over 17,000.
> - **Reply where you read.** A request's drawer puts the reply box right under its progress line, in every state. While a reply is on its way, "Reply here" waits, so a message can never go to a second conversation as a second paid turn.
> - **A focus area's page** reads top to bottom: what needs you, the asks not started yet, then the board. A failed save says which change failed and offers Try again on that screen only. Past focus shows the day an area was marked done.
> …

### [v15.21.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.21.0)
<sub>2026-11-17 · yesterday</sub>

> **claude-mem no longer turns off Claude Code's Code Mode**
> - **Code Mode starts with claude-mem enabled** (#6278, thanks @naive000; reported in #6209 by @nasif-naseef). Code Mode (experimental, Claude Code 2.1.323 and later) refuses to start when a plugin's hooks module hooks `tool.call`. claude-mem's auto-clear mod did, so Code Mode was off for everyone with claude-mem enabled, even with auto-clear off. The mod now reads tool results through `session.append` instead. Auto-clear still works on every Claude Code version that runs mods (2.1.287 and later).
> **Auto-clear picks up where it left off**
> Auto-clear is still off unless you set `CLAUDE_MEM_AUTO_CLEAR_ENABLED` to `true`. When it is on:
> - **It resumes with a continuation prompt instead of the bare word "continue"** (#6294). Before clearing, Claude saves its work state one last time, naming the list it is working from, the task it just finished and the overall goal. After `/clear`, auto-clear sends: `You are working on "<list>" and recently completed "<task>". Pick back up on our overarching goal "<goal>" from where you left off.` If that save left any of the three out, it sends "continue" as before and logs why.
> - **It starts at 40% of the context window instead of 33%** (#6294). A `CLAUDE_MEM_AUTO_CLEAR_PERCENT` you set in `settings.json` or the environment still wins.
> …

### [v15.20.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.20.0)
<sub>2026-11-17 · yesterday</sub>

> **Two critical fixes**
> - **The worker starts when settings.json is not valid JSON** (#6259). The worker refused to start when `~/.claude-mem/settings.json` couldn't be parsed, even though the database already held the device identity it was trying to save there. Nothing was captured and no context was injected. It now logs a warning, leaves the file untouched, and starts. On a first start with no saved identity, the error names the file and says to repair or delete it.
> - **Live Codex Desktop capture on macOS** (#6285, thanks @MaxWang007; reported in #6283 by @AlbertValverdeC). Under Bun on macOS, `fs.watch` gives no event while another process appends to a file it holds open, and Codex Desktop holds a rollout file open for the life of a thread. Codex sessions were read in one burst, sometimes a day later, when Codex closed the file. The transcript watcher now checks the files it already tails every 3 seconds and reads new bytes. It awaits one stat at a time, so a large `~/.codex/sessions` history never blocks the worker, and it never opens new files on its own.
> **Also on main since 15.19.0**
> Three pieces of the upcoming 16.0.0, already on main, ship in this release too:
> - **Mem0 and Supermemory import acceptance fixes** (#6206): Supermemory `--documents` reruns no longer duplicate, and documents imported by 15.19.0 still count as already imported. Mem0 expiry includes its own date. Every import limit names its source; the unsourced 100 MiB total and 10,000-record default are gone (`--max-records` stays).
> …

### [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0)
<sub>2026-11-16 · 3d ago</sub>

> **Continue a Claude Code or Codex conversation from My Work**
> Open a request in My Work, then open "Where this came from". Under each Claude Code or Codex conversation there is now a message box. Type a message and press Send, and that same conversation takes the turn. The reply shows right there (#6191; the command shapes follow @wiesenthal's answer code in #6054, and the commit credits him).
> - Each conversation keeps the messages you sent from My Work and their replies, in order. Stop ends a running turn.
> - The box says which folder the turn runs in. When the recorded folder no longer exists (common after a worktree is cleaned up), the turn runs in the nearest existing folder above it.
> - "Copy resume command" copies `claude --resume <id>` or `codex resume <id>`. On a Mac, "Open in Claude" opens a Claude Code conversation in the Claude desktop app.
> - One Send starts one headless resume (`claude --resume <id> -p --output-format json`, or `codex exec resume <id> - --skip-git-repo-check`) with your message on stdin. A failed turn is recorded as failed and never retried. Nothing is queued or saved for replay, and nothing starts at startup, on a timer or on reconnect.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Show the Claude-Mem mark in the terminal startup card’s right column …](https://github.com/thedotmack/claude-mem/commit/4b48c5727ab62ee22e72a71b822a2fb225491fa2) | thedotmack |
| 2026-11-19 | [feat(observer): support Codex as a quota fallback (#6326)](https://github.com/thedotmack/claude-mem/commit/2f4ed384376420be4f75a5fc2c27ce1bbfb77f81) | QuantScorpus |
| 2026-11-19 | [chore: promote 16.0.1 for auto-update](https://github.com/thedotmack/claude-mem/commit/46e5bf526dc7951dd3f851af76c6b0a220d3f8a8) | thedotmack |
| 2026-11-19 | [docs: update CHANGELOG for v16.0.1](https://github.com/thedotmack/claude-mem/commit/7214c5b5a44e7040fdd4def46adee543493ad6c3) | thedotmack |
| 2026-11-19 | [chore: bump version to 16.0.1](https://github.com/thedotmack/claude-mem/commit/e22c58353b950b15e6e16d98719801224840f046) | thedotmack |
| 2026-11-19 | [fix(chroma): end read calls before the worker's search budget (#6327)](https://github.com/thedotmack/claude-mem/commit/08bad9f906a1308a7bf76ac85e51c6bef3daae97) | REI-330 |
| 2026-11-19 | [fix(codex): never hard-link the user's auth.json into the private Cod…](https://github.com/thedotmack/claude-mem/commit/833a0a834c8c91e6b4843cdba5c8bbe9035fb6d9) | ffe111 |
| 2026-11-19 | [feat(devin): claude-mem in Devin cloud sessions and Devin Bots via an…](https://github.com/thedotmack/claude-mem/commit/b5c57a1a8d43195aa04be93d4776c88bd8d6695c) | devin-ai-integration[bot] |
| 2026-11-19 | [feat(work-view): run the My Work refresh on OpenCode (#5535) (#6330)](https://github.com/thedotmack/claude-mem/commit/6bef24671b63e211af971e0b614c109f24b4ffdc) | REI-330 |
| 2026-11-19 | [feat(search): match unsegmented scripts by substring on PostgreSQL (#…](https://github.com/thedotmack/claude-mem/commit/0b4e183408770db68628a453d7dac39d5d489375) | REI-330 |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
