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
| ⭐ **Stars** | 119.0k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [80](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.0.3](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.3) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 917.2 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.0.3](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.3)
<sub>2026-11-21 · today</sub>

> **Critical fix**
> - **The OMP hook works with the server runtime** (#6367, thanks @flipcyde101, closes #6366 reported by @walynde). When `CLAUDE_MEM_RUNTIME` was `server` or `server-beta`, the OMP hook still sent everything to the local worker, so OMP sessions were dropped. The hook now reads `CLAUDE_MEM_SERVER_URL`, `CLAUDE_MEM_SERVER_API_KEY` and `CLAUDE_MEM_SERVER_PROJECT_ID` (or the `CLAUDE_MEM_SERVER_BETA_*` names; environment variables win over `settings.json`) and talks to the server's `/v1` API directly: session start, tool and reply events, context, and session end. It applies the same rules the worker applies before it saves anything: `<private>` blocks are stripped, excluded projects and `CLAUDE_MEM_SKIP_TOOLS` are honored, every prompt is recorded, and the project name comes from git. If the server settings are incomplete, it falls back to the worker as before.
> - **OMP users: run `npx claude-mem install --ide omp` once to get this fix.** The OMP hook is a copied file, so a plugin update alone does not replace it.
> **Fixes**
> - **Knowledge queries and corpus requests can no longer hang forever** (#6368, thanks @flipcyde101, closes #6364 reported by @soarkit). A stalled Agent SDK stream used to keep the request and its Claude CLI child alive with no end. A knowledge query or prime now stops after 10 minutes and a corpus request after 15, with a 504 error. The corpus stays locked until the timed-out work has really stopped, so it cannot write after a delete or rebuild.
> - **The "paused saving memories" notice goes away once Codex is saving** (#6374, thanks @ryrenz, closes #6372 reported by @raw34). After you switched `CLAUDE_MEM_PROVIDER` to `codex` following a Claude quota pause, every new session still said capture was paused until the old Claude cooldown ran out. The notice is now recomputed when Codex stores a memory.
> …

### [v16.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.2)
<sub>2026-11-20 · yesterday</sub>

> **Critical fix**
> - **An auto-update no longer deletes the plugin version a running Claude Code session was loaded from** (#6352, thanks @0xABCD01, closes #6349 reported by @justindrp). The cache sweep keeps a version folder while the Claude Code process recorded in its `.in_use` file is alive. On macOS and BSD, a few seconds of difference between the start time Claude Code recorded and the one `ps` reports was read as PID reuse, so the sweep deleted the folder from under a live session and every hook failed for the rest of that session. A start-time mismatch no longer removes the folder while the process at that PID is still Claude Code. A PID that now belongs to another program is still pruned as before.
> - **Every cache prune now logs why and who.** The worker writes one log line per removed version with its reason (orphaned or superseded) and the `.in_use` records it rejected and why (process exited or start-time mismatch), so any removal can be traced from the log alone.
> **Fixes**
> - **The session-start card is drawn on Team and Enterprise accounts** (#6353, thanks @KeithMoc, closes #6314 reported by @TimoWestland). When an organization plugin runs first and the card's usual hooks never fire, the card now asks for itself from the `session.start` hook and the context hook answers it.
> - **My Work detects OpenCode 2.x connections** (#6340, thanks @ZedingZhang, closes #6339 reported by @Realauster). The login probe reads OpenCode's JSON output, so a connected provider is no longer reported as logged out on OpenCode 2.3.2.
> …

### [v16.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.1)
<sub>2026-11-19 · 3d ago</sub>

> **Critical fixes**
> - **Signing in to Codex works again on Windows while claude-mem runs** (#6332, thanks @ffe111, closes #6331). The private Codex home that claude-mem's app-server uses got its `auth.json` through a hard link to your real `~/.codex/auth.json`. Codex refuses to replace a credential file with more than one hard link (`persist_failed: atomic credential replacement does not support hard-linked files`), so `codex login` and token refresh failed for as long as that home existed. The private home now gets a symlink, which Codex follows. Only on Windows, and only when a symlink is not permitted (no Developer Mode or elevation), it gets a private copy instead. Any other error still fails loudly.
> - **A probe answered with `<skip_summary/>` ends the quota cooldown** (#6324, thanks @vaibhav375, closes #6322). After a quota hit, the worker probes the provider and clears the cooldown once a probe stores a memory. A probe the provider answered with a valid `<skip_summary/>` stores nothing, so the cooldown never cleared and the worker re-probed every 5 minutes for as long as that session only skipped. A valid skip now releases the cooldown too, on both the store path and the early path before the memory session id is known. Observer-health success still needs a real store.
> **Fixes**
> - **Search falls back to SQLite instead of failing when Chroma is slow** (#6327, thanks @REI-330, closes #6323). The MCP client gives a search 30 s, while each Chroma read waited up to 60 s, so a slow query was still running when the caller gave up and the SQLite/FTS5 fallback never ran. A search now shares one 20 s budget across its Chroma reads and falls back when it runs out, without restarting a healthy chroma-mcp.
> - **Chroma rebuilds no longer hold a core for hours** (#6299, thanks @srieteja). A full backfill now pauses after each row for its write time times `CLAUDE_MEM_CHROMA_BACKFILL_PAUSE_RATIO` (default 1, 0 turns it off), and chroma-mcp starts under `nice` (`CLAUDE_MEM_CHROMA_PROCESS_NICE`, default 10) outside Windows. Live sync is unchanged.
> …

### [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0)
<sub>2026-11-18 · 4d ago</sub>

> **My Work puts what needs you first**
> My Work, the page that shows what your agents are doing, was rebuilt from a full UI review (#6210, #6304). What needs you sits at the top, long lists fold, and every page works on a phone, by keyboard and with a screen reader.
> - **What needs you comes first.** On the home page the first request waiting on you is at the top, with the one orange button on the screen. Requests are one-line rows; Idle and Shipped fold to one row each, with their counts.
> - **Shorter pages.** On a real install: home is about 2,600px tall instead of 5,138; the List opens with 5 rows instead of 195; My Rules is about 4,400px instead of over 17,000.
> - **Reply where you read.** A request's drawer puts the reply box right under its progress line, in every state. While a reply is on its way, "Reply here" waits, so a message can never go to a second conversation as a second paid turn.
> - **A focus area's page** reads top to bottom: what needs you, the asks not started yet, then the board. A failed save says which change failed and offers Try again on that screen only. Past focus shows the day an area was marked done.
> …

### [v15.21.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.21.0)
<sub>2026-11-17 · 4d ago</sub>

> **claude-mem no longer turns off Claude Code's Code Mode**
> - **Code Mode starts with claude-mem enabled** (#6278, thanks @naive000; reported in #6209 by @nasif-naseef). Code Mode (experimental, Claude Code 2.1.323 and later) refuses to start when a plugin's hooks module hooks `tool.call`. claude-mem's auto-clear mod did, so Code Mode was off for everyone with claude-mem enabled, even with auto-clear off. The mod now reads tool results through `session.append` instead. Auto-clear still works on every Claude Code version that runs mods (2.1.287 and later).
> **Auto-clear picks up where it left off**
> Auto-clear is still off unless you set `CLAUDE_MEM_AUTO_CLEAR_ENABLED` to `true`. When it is on:
> - **It resumes with a continuation prompt instead of the bare word "continue"** (#6294). Before clearing, Claude saves its work state one last time, naming the list it is working from, the task it just finished and the overall goal. After `/clear`, auto-clear sends: `You are working on "<list>" and recently completed "<task>". Pick back up on our overarching goal "<goal>" from where you left off.` If that save left any of the three out, it sends "continue" as before and logs why.
> - **It starts at 40% of the context window instead of 33%** (#6294). A `CLAUDE_MEM_AUTO_CLEAR_PERCENT` you set in `settings.json` or the environment still wins.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [docs: tell OMP users to reinstall the hook for the 16.0.3 server-runt…](https://github.com/thedotmack/claude-mem/commit/79d33254e5570b43175c639c2a2ce58bd1e221b9) | thedotmack |
| 2026-11-21 | [chore: promote 16.0.3 for auto-update](https://github.com/thedotmack/claude-mem/commit/9e1450a809a4f76089f56c624d87e3b4f1ac832c) | thedotmack |
| 2026-11-21 | [docs: update CHANGELOG for v16.0.3](https://github.com/thedotmack/claude-mem/commit/36e09defa22ab3c1259b3a01c2b1056704d3913e) | thedotmack |
| 2026-11-21 | [chore: bump version to 16.0.3](https://github.com/thedotmack/claude-mem/commit/4a04765b17c46d36d6ecdd91b41f1adffffa2a81) | thedotmack |
| 2026-11-21 | [fix(worker): register standalone observer SDK children in the process…](https://github.com/thedotmack/claude-mem/commit/951fe119043727ddd3c3a8ee0a67b36ffd632f8e) | DeryFerd |
| 2026-11-21 | [fix(agent-runner): bound the collected stdout and stderr of a chatty …](https://github.com/thedotmack/claude-mem/commit/d3f65553a700c4bdf0118a93f0e7cb57f8d0d14f) | DeryFerd |
| 2026-11-21 | [fix(transcripts): skip JSONL records beyond the tail cap instead of a…](https://github.com/thedotmack/claude-mem/commit/69cbef94bcb72917fe3596dc620eedbe116792dc) | DeryFerd |
| 2026-11-21 | [fix(sync-api): compare the internal projector credential in constant …](https://github.com/thedotmack/claude-mem/commit/bcde3a977cdf0c34413f82fef6e577e321224742) | DeryFerd |
| 2026-11-21 | [fix(openclaw): only remove a claude-mem-shaped installPath from the u…](https://github.com/thedotmack/claude-mem/commit/49daf7ea08ba0afa199a15e18bbc9b52dc2e749d) | DeryFerd |
| 2026-11-21 | [fix(knowledge): enforce idle and absolute deadlines on Agent SDK quer…](https://github.com/thedotmack/claude-mem/commit/18abce9e49c36b4d95b030658392e6390745fbc7) | flipcyde101 |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
