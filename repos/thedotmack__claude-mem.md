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
| ⭐ **Stars** | 118.8k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [89](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.2) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 910.6 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.2)
<sub>2026-11-20 · today</sub>

> **Critical fix**
> - **An auto-update no longer deletes the plugin version a running Claude Code session was loaded from** (#6352, thanks @0xABCD01, closes #6349 reported by @justindrp). The cache sweep keeps a version folder while the Claude Code process recorded in its `.in_use` file is alive. On macOS and BSD, a few seconds of difference between the start time Claude Code recorded and the one `ps` reports was read as PID reuse, so the sweep deleted the folder from under a live session and every hook failed for the rest of that session. A start-time mismatch no longer removes the folder while the process at that PID is still Claude Code. A PID that now belongs to another program is still pruned as before.
> - **Every cache prune now logs why and who.** The worker writes one log line per removed version with its reason (orphaned or superseded) and the `.in_use` records it rejected and why (process exited or start-time mismatch), so any removal can be traced from the log alone.
> **Fixes**
> - **The session-start card is drawn on Team and Enterprise accounts** (#6353, thanks @KeithMoc, closes #6314 reported by @TimoWestland). When an organization plugin runs first and the card's usual hooks never fire, the card now asks for itself from the `session.start` hook and the context hook answers it.
> - **My Work detects OpenCode 2.x connections** (#6340, thanks @ZedingZhang, closes #6339 reported by @Realauster). The login probe reads OpenCode's JSON output, so a connected provider is no longer reported as logged out on OpenCode 2.3.2.
> …

### [v16.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.1)
<sub>2026-11-19 · 2d ago</sub>

> **Critical fixes**
> - **Signing in to Codex works again on Windows while claude-mem runs** (#6332, thanks @ffe111, closes #6331). The private Codex home that claude-mem's app-server uses got its `auth.json` through a hard link to your real `~/.codex/auth.json`. Codex refuses to replace a credential file with more than one hard link (`persist_failed: atomic credential replacement does not support hard-linked files`), so `codex login` and token refresh failed for as long as that home existed. The private home now gets a symlink, which Codex follows. Only on Windows, and only when a symlink is not permitted (no Developer Mode or elevation), it gets a private copy instead. Any other error still fails loudly.
> - **A probe answered with `<skip_summary/>` ends the quota cooldown** (#6324, thanks @vaibhav375, closes #6322). After a quota hit, the worker probes the provider and clears the cooldown once a probe stores a memory. A probe the provider answered with a valid `<skip_summary/>` stores nothing, so the cooldown never cleared and the worker re-probed every 5 minutes for as long as that session only skipped. A valid skip now releases the cooldown too, on both the store path and the early path before the memory session id is known. Observer-health success still needs a real store.
> **Fixes**
> - **Search falls back to SQLite instead of failing when Chroma is slow** (#6327, thanks @REI-330, closes #6323). The MCP client gives a search 30 s, while each Chroma read waited up to 60 s, so a slow query was still running when the caller gave up and the SQLite/FTS5 fallback never ran. A search now shares one 20 s budget across its Chroma reads and falls back when it runs out, without restarting a healthy chroma-mcp.
> - **Chroma rebuilds no longer hold a core for hours** (#6299, thanks @srieteja). A full backfill now pauses after each row for its write time times `CLAUDE_MEM_CHROMA_BACKFILL_PAUSE_RATIO` (default 1, 0 turns it off), and chroma-mcp starts under `nice` (`CLAUDE_MEM_CHROMA_PROCESS_NICE`, default 10) outside Windows. Live sync is unchanged.
> …

### [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0)
<sub>2026-11-18 · 3d ago</sub>

> **My Work puts what needs you first**
> My Work, the page that shows what your agents are doing, was rebuilt from a full UI review (#6210, #6304). What needs you sits at the top, long lists fold, and every page works on a phone, by keyboard and with a screen reader.
> - **What needs you comes first.** On the home page the first request waiting on you is at the top, with the one orange button on the screen. Requests are one-line rows; Idle and Shipped fold to one row each, with their counts.
> - **Shorter pages.** On a real install: home is about 2,600px tall instead of 5,138; the List opens with 5 rows instead of 195; My Rules is about 4,400px instead of over 17,000.
> - **Reply where you read.** A request's drawer puts the reply box right under its progress line, in every state. While a reply is on its way, "Reply here" waits, so a message can never go to a second conversation as a second paid turn.
> - **A focus area's page** reads top to bottom: what needs you, the asks not started yet, then the board. A failed save says which change failed and offers Try again on that screen only. Past focus shows the day an area was marked done.
> …

### [v15.21.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.21.0)
<sub>2026-11-17 · 3d ago</sub>

> **claude-mem no longer turns off Claude Code's Code Mode**
> - **Code Mode starts with claude-mem enabled** (#6278, thanks @naive000; reported in #6209 by @nasif-naseef). Code Mode (experimental, Claude Code 2.1.323 and later) refuses to start when a plugin's hooks module hooks `tool.call`. claude-mem's auto-clear mod did, so Code Mode was off for everyone with claude-mem enabled, even with auto-clear off. The mod now reads tool results through `session.append` instead. Auto-clear still works on every Claude Code version that runs mods (2.1.287 and later).
> **Auto-clear picks up where it left off**
> Auto-clear is still off unless you set `CLAUDE_MEM_AUTO_CLEAR_ENABLED` to `true`. When it is on:
> - **It resumes with a continuation prompt instead of the bare word "continue"** (#6294). Before clearing, Claude saves its work state one last time, naming the list it is working from, the task it just finished and the overall goal. After `/clear`, auto-clear sends: `You are working on "<list>" and recently completed "<task>". Pick back up on our overarching goal "<goal>" from where you left off.` If that save left any of the three out, it sends "continue" as before and logs why.
> - **It starts at 40% of the context window instead of 33%** (#6294). A `CLAUDE_MEM_AUTO_CLEAR_PERCENT` you set in `settings.json` or the environment still wins.
> …

### [v15.20.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.20.0)
<sub>2026-11-17 · 3d ago</sub>

> **Two critical fixes**
> - **The worker starts when settings.json is not valid JSON** (#6259). The worker refused to start when `~/.claude-mem/settings.json` couldn't be parsed, even though the database already held the device identity it was trying to save there. Nothing was captured and no context was injected. It now logs a warning, leaves the file untouched, and starts. On a first start with no saved identity, the error names the file and says to repair or delete it.
> - **Live Codex Desktop capture on macOS** (#6285, thanks @MaxWang007; reported in #6283 by @AlbertValverdeC). Under Bun on macOS, `fs.watch` gives no event while another process appends to a file it holds open, and Codex Desktop holds a rollout file open for the life of a thread. Codex sessions were read in one burst, sometimes a day later, when Codex closed the file. The transcript watcher now checks the files it already tails every 3 seconds and reads new bytes. It awaits one stat at a time, so a large `~/.codex/sessions` history never blocks the worker, and it never opens new files on its own.
> **Also on main since 15.19.0**
> Three pieces of the upcoming 16.0.0, already on main, ship in this release too:
> - **Mem0 and Supermemory import acceptance fixes** (#6206): Supermemory `--documents` reruns no longer duplicate, and documents imported by 15.19.0 still count as already imported. Mem0 expiry includes its own date. Every import limit names its source; the unsourced 100 MiB total and 10,000-record default are gone (`--max-records` stays).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(agent-runner): run the My Work OpenCode step on OpenCode 2.x (#6361)](https://github.com/thedotmack/claude-mem/commit/f1bb834527637231e23575e2a70c57375efdac04) | thedotmack |
| 2026-11-20 | [chore: promote 16.0.2 for auto-update](https://github.com/thedotmack/claude-mem/commit/2eeda5052ff030711aa8ada22c65e5bdae8943fc) | thedotmack |
| 2026-11-20 | [docs: update CHANGELOG for v16.0.2](https://github.com/thedotmack/claude-mem/commit/96658712bd46d0062eb19bbfb18723a364a9b0ef) | thedotmack |
| 2026-11-20 | [test(transcripts): count the append poll's poke instead of racing its…](https://github.com/thedotmack/claude-mem/commit/1ba7227cab1147e423e4a1e70d2b4fcd96a754ee) | thedotmack |
| 2026-11-20 | [chore: bump version to 16.0.2](https://github.com/thedotmack/claude-mem/commit/66688aa5e3c1d4386cb6f02c518cd3fba06f05b4) | thedotmack |
| 2026-11-20 | [fix(prune): keep a cache version while its recorded Claude process is…](https://github.com/thedotmack/claude-mem/commit/ea1cfde657d6796bfa6c5d7de9d1e4570c3290eb) | 0xABCD01 |
| 2026-11-20 | [fix(npx-cli): give the async host-observer probe the same 1s budget a…](https://github.com/thedotmack/claude-mem/commit/e469a8cd5405c29eb39e2de8dcb3f63c096f1263) | rtmalikian |
| 2026-11-20 | [fix(my-work): prefer MXC for isolated Codex refresh on Windows (#6348)](https://github.com/thedotmack/claude-mem/commit/0ce495b0371caf2f0f1ca3fb0531efa0417d8723) | QuantScorpus |
| 2026-11-20 | [fix(session-start-card): draw the card on Team and Enterprise account…](https://github.com/thedotmack/claude-mem/commit/a34ce9890be418eb6b0b4eb1235d13e968e3408a) | KeithMoc |
| 2026-11-20 | [fix: detect OpenCode 2.x connections for My Work refresh (#6340)](https://github.com/thedotmack/claude-mem/commit/f52388ef75c2ba4ee684b507c3fd7ad502cfab56) | ZedingZhang |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
