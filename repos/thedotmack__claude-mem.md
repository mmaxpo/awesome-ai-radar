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
| ⭐ **Stars** | 118.6k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [85](https://github.com/thedotmack/claude-mem/issues) |
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
<sub>2026-11-19 · yesterday</sub>

> **Critical fixes**
> - **Signing in to Codex works again on Windows while claude-mem runs** (#6332, thanks @ffe111, closes #6331). The private Codex home that claude-mem's app-server uses got its `auth.json` through a hard link to your real `~/.codex/auth.json`. Codex refuses to replace a credential file with more than one hard link (`persist_failed: atomic credential replacement does not support hard-linked files`), so `codex login` and token refresh failed for as long as that home existed. The private home now gets a symlink, which Codex follows. Only on Windows, and only when a symlink is not permitted (no Developer Mode or elevation), it gets a private copy instead. Any other error still fails loudly.
> - **A probe answered with `<skip_summary/>` ends the quota cooldown** (#6324, thanks @vaibhav375, closes #6322). After a quota hit, the worker probes the provider and clears the cooldown once a probe stores a memory. A probe the provider answered with a valid `<skip_summary/>` stores nothing, so the cooldown never cleared and the worker re-probed every 5 minutes for as long as that session only skipped. A valid skip now releases the cooldown too, on both the store path and the early path before the memory session id is known. Observer-health success still needs a real store.
> **Fixes**
> - **Search falls back to SQLite instead of failing when Chroma is slow** (#6327, thanks @REI-330, closes #6323). The MCP client gives a search 30 s, while each Chroma read waited up to 60 s, so a slow query was still running when the caller gave up and the SQLite/FTS5 fallback never ran. A search now shares one 20 s budget across its Chroma reads and falls back when it runs out, without restarting a healthy chroma-mcp.
> - **Chroma rebuilds no longer hold a core for hours** (#6299, thanks @srieteja). A full backfill now pauses after each row for its write time times `CLAUDE_MEM_CHROMA_BACKFILL_PAUSE_RATIO` (default 1, 0 turns it off), and chroma-mcp starts under `nice` (`CLAUDE_MEM_CHROMA_PROCESS_NICE`, default 10) outside Windows. Live sync is unchanged.
> …

### [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0)
<sub>2026-11-18 · 2d ago</sub>

> **My Work puts what needs you first**
> My Work, the page that shows what your agents are doing, was rebuilt from a full UI review (#6210, #6304). What needs you sits at the top, long lists fold, and every page works on a phone, by keyboard and with a screen reader.
> - **What needs you comes first.** On the home page the first request waiting on you is at the top, with the one orange button on the screen. Requests are one-line rows; Idle and Shipped fold to one row each, with their counts.
> - **Shorter pages.** On a real install: home is about 2,600px tall instead of 5,138; the List opens with 5 rows instead of 195; My Rules is about 4,400px instead of over 17,000.
> - **Reply where you read.** A request's drawer puts the reply box right under its progress line, in every state. While a reply is on its way, "Reply here" waits, so a message can never go to a second conversation as a second paid turn.
> - **A focus area's page** reads top to bottom: what needs you, the asks not started yet, then the board. A failed save says which change failed and offers Try again on that screen only. Past focus shows the day an area was marked done.
> …

### [v15.21.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.21.0)
<sub>2026-11-17 · 2d ago</sub>

> **claude-mem no longer turns off Claude Code's Code Mode**
> - **Code Mode starts with claude-mem enabled** (#6278, thanks @naive000; reported in #6209 by @nasif-naseef). Code Mode (experimental, Claude Code 2.1.323 and later) refuses to start when a plugin's hooks module hooks `tool.call`. claude-mem's auto-clear mod did, so Code Mode was off for everyone with claude-mem enabled, even with auto-clear off. The mod now reads tool results through `session.append` instead. Auto-clear still works on every Claude Code version that runs mods (2.1.287 and later).
> **Auto-clear picks up where it left off**
> Auto-clear is still off unless you set `CLAUDE_MEM_AUTO_CLEAR_ENABLED` to `true`. When it is on:
> - **It resumes with a continuation prompt instead of the bare word "continue"** (#6294). Before clearing, Claude saves its work state one last time, naming the list it is working from, the task it just finished and the overall goal. After `/clear`, auto-clear sends: `You are working on "<list>" and recently completed "<task>". Pick back up on our overarching goal "<goal>" from where you left off.` If that save left any of the three out, it sends "continue" as before and logs why.
> - **It starts at 40% of the context window instead of 33%** (#6294). A `CLAUDE_MEM_AUTO_CLEAR_PERCENT` you set in `settings.json` or the environment still wins.
> …

### [v15.20.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.20.0)
<sub>2026-11-17 · 2d ago</sub>

> **Two critical fixes**
> - **The worker starts when settings.json is not valid JSON** (#6259). The worker refused to start when `~/.claude-mem/settings.json` couldn't be parsed, even though the database already held the device identity it was trying to save there. Nothing was captured and no context was injected. It now logs a warning, leaves the file untouched, and starts. On a first start with no saved identity, the error names the file and says to repair or delete it.
> - **Live Codex Desktop capture on macOS** (#6285, thanks @MaxWang007; reported in #6283 by @AlbertValverdeC). Under Bun on macOS, `fs.watch` gives no event while another process appends to a file it holds open, and Codex Desktop holds a rollout file open for the life of a thread. Codex sessions were read in one burst, sometimes a day later, when Codex closed the file. The transcript watcher now checks the files it already tails every 3 seconds and reads new bytes. It awaits one stat at a time, so a large `~/.codex/sessions` history never blocks the worker, and it never opens new files on its own.
> **Also on main since 15.19.0**
> Three pieces of the upcoming 16.0.0, already on main, ship in this release too:
> - **Mem0 and Supermemory import acceptance fixes** (#6206): Supermemory `--documents` reruns no longer duplicate, and documents imported by 15.19.0 still count as already imported. Mem0 expiry includes its own date. Every import limit names its source; the unsourced 100 MiB total and 10,000-record default are gone (`--max-records` stays).
> …

### [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0)
<sub>2026-11-16 · 4d ago</sub>

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
| 2026-11-19 | [fix(chroma): reconcile ambiguous collection deletes before rebuilding…](https://github.com/thedotmack/claude-mem/commit/c0f37d60b2e4860851575e3cbb003f23fc340d4e) | POWDER-RANGER |
| 2026-11-19 | [fix(chroma): restart chroma-mcp after a cancelled read once writes se…](https://github.com/thedotmack/claude-mem/commit/ec163d61d0a1e622482a85b8fc57ae5916667b98) | MaxWang007 |
| 2026-11-19 | [fix(worker): install the terminal 404 and error handlers after routes…](https://github.com/thedotmack/claude-mem/commit/aa5fac5ad2a76b4f20500845d7768170a44e892e) | DeryFerd |
| 2026-11-19 | [ci(windows): run the postinstall allowlist guard after the build (#6343)](https://github.com/thedotmack/claude-mem/commit/b0ebbb66a8317ff4a94d126a5cf0d531c7c709d0) | DeryFerd |
| 2026-11-19 | [refactor(cli): read /api/admin/doctor once for the doctor report (#6344)](https://github.com/thedotmack/claude-mem/commit/53d9224208b877bf99ff444526e2e104798f270d) | DeryFerd |
| 2026-11-19 | [test(worker): pin the Host guard ahead of CORS with a rebinding test …](https://github.com/thedotmack/claude-mem/commit/3025540a0919ba3f8afce4df81fe10b4ae12f1e6) | DeryFerd |
| 2026-11-19 | [docs(devin): connect CMEM Pro on Devin cloud with one org secret (#6335)](https://github.com/thedotmack/claude-mem/commit/495433322319fa628846cef60c1450e740d1b8a3) | devin-ai-integration[bot] |
| 2026-11-19 | [docs(docker): note the repo-root build context in the pinning example…](https://github.com/thedotmack/claude-mem/commit/4f60edd75a12cc4ae447aa0946497ea193d93da4) | DeryFerd |
| 2026-11-19 | [fix(claude-md): resolve absolute paths before the project-root check …](https://github.com/thedotmack/claude-mem/commit/592a48716d6b5aa1341d58dba26e0522d50fc3cd) | LeviReisJs |
| 2026-11-19 | [Show the Claude-Mem mark in the terminal startup card’s right column …](https://github.com/thedotmack/claude-mem/commit/4b48c5727ab62ee22e72a71b822a2fb225491fa2) | thedotmack |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
