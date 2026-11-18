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
| ⭐ **Stars** | 118.2k |
| 🍴 **Forks** | 10.3k |
| 🐞 **Open issues + PRs** | [91](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 892.9 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.0.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.0)
<sub>2026-11-18 · today</sub>

> **My Work puts what needs you first**
> My Work, the page that shows what your agents are doing, was rebuilt from a full UI review (#6210, #6304). What needs you sits at the top, long lists fold, and every page works on a phone, by keyboard and with a screen reader.
> - **What needs you comes first.** On the home page the first request waiting on you is at the top, with the one orange button on the screen. Requests are one-line rows; Idle and Shipped fold to one row each, with their counts.
> - **Shorter pages.** On a real install: home is about 2,600px tall instead of 5,138; the List opens with 5 rows instead of 195; My Rules is about 4,400px instead of over 17,000.
> - **Reply where you read.** A request's drawer puts the reply box right under its progress line, in every state. While a reply is on its way, "Reply here" waits, so a message can never go to a second conversation as a second paid turn.
> - **A focus area's page** reads top to bottom: what needs you, the asks not started yet, then the board. A failed save says which change failed and offers Try again on that screen only. Past focus shows the day an area was marked done.
> …

### [v15.21.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.21.0)
<sub>2026-11-17 · today</sub>

> **claude-mem no longer turns off Claude Code's Code Mode**
> - **Code Mode starts with claude-mem enabled** (#6278, thanks @naive000; reported in #6209 by @nasif-naseef). Code Mode (experimental, Claude Code 2.1.323 and later) refuses to start when a plugin's hooks module hooks `tool.call`. claude-mem's auto-clear mod did, so Code Mode was off for everyone with claude-mem enabled, even with auto-clear off. The mod now reads tool results through `session.append` instead. Auto-clear still works on every Claude Code version that runs mods (2.1.287 and later).
> **Auto-clear picks up where it left off**
> Auto-clear is still off unless you set `CLAUDE_MEM_AUTO_CLEAR_ENABLED` to `true`. When it is on:
> - **It resumes with a continuation prompt instead of the bare word "continue"** (#6294). Before clearing, Claude saves its work state one last time, naming the list it is working from, the task it just finished and the overall goal. After `/clear`, auto-clear sends: `You are working on "<list>" and recently completed "<task>". Pick back up on our overarching goal "<goal>" from where you left off.` If that save left any of the three out, it sends "continue" as before and logs why.
> - **It starts at 40% of the context window instead of 33%** (#6294). A `CLAUDE_MEM_AUTO_CLEAR_PERCENT` you set in `settings.json` or the environment still wins.
> …

### [v15.20.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.20.0)
<sub>2026-11-17 · today</sub>

> **Two critical fixes**
> - **The worker starts when settings.json is not valid JSON** (#6259). The worker refused to start when `~/.claude-mem/settings.json` couldn't be parsed, even though the database already held the device identity it was trying to save there. Nothing was captured and no context was injected. It now logs a warning, leaves the file untouched, and starts. On a first start with no saved identity, the error names the file and says to repair or delete it.
> - **Live Codex Desktop capture on macOS** (#6285, thanks @MaxWang007; reported in #6283 by @AlbertValverdeC). Under Bun on macOS, `fs.watch` gives no event while another process appends to a file it holds open, and Codex Desktop holds a rollout file open for the life of a thread. Codex sessions were read in one burst, sometimes a day later, when Codex closed the file. The transcript watcher now checks the files it already tails every 3 seconds and reads new bytes. It awaits one stat at a time, so a large `~/.codex/sessions` history never blocks the worker, and it never opens new files on its own.
> **Also on main since 15.19.0**
> Three pieces of the upcoming 16.0.0, already on main, ship in this release too:
> - **Mem0 and Supermemory import acceptance fixes** (#6206): Supermemory `--documents` reruns no longer duplicate, and documents imported by 15.19.0 still count as already imported. Mem0 expiry includes its own date. Every import limit names its source; the unsourced 100 MiB total and 10,000-record default are gone (`--max-records` stays).
> …

### [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0)
<sub>2026-11-16 · 2d ago</sub>

> **Continue a Claude Code or Codex conversation from My Work**
> Open a request in My Work, then open "Where this came from". Under each Claude Code or Codex conversation there is now a message box. Type a message and press Send, and that same conversation takes the turn. The reply shows right there (#6191; the command shapes follow @wiesenthal's answer code in #6054, and the commit credits him).
> - Each conversation keeps the messages you sent from My Work and their replies, in order. Stop ends a running turn.
> - The box says which folder the turn runs in. When the recorded folder no longer exists (common after a worktree is cleaned up), the turn runs in the nearest existing folder above it.
> - "Copy resume command" copies `claude --resume <id>` or `codex resume <id>`. On a Mac, "Open in Claude" opens a Claude Code conversation in the Claude desktop app.
> - One Send starts one headless resume (`claude --resume <id> -p --output-format json`, or `codex exec resume <id> - --skip-git-repo-check`) with your message on stdin. A failed turn is recorded as failed and never retried. Nothing is queued or saved for replay, and nothing starts at startup, on a timer or on reconnect.
> …

### [v15.18.5](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.5)
<sub>2026-11-15 · 2d ago</sub>

> **Critical fixes**
> - **The tree-sitter CLI installs on networks where its download script keeps failing** (#6110, thanks @rigel905, closes #6109). On some networks tree-sitter-cli's own `install.js` had its request reset every time, or exited 0 on a truncated file. The pinned SHA-256 check correctly refused the file, but nothing recovered after that, so `smart_search`, `smart_outline`, `smart_unfold` and the File Read Gate stayed off on every worker start, and `npx claude-mem repair` aborted. Now, when the script fails or leaves anything but the pinned executable, claude-mem fetches the same release asset directly, once, inside the same install time budget, and runs it only after it unpacks to the same pinned SHA-256. The script still runs first, so `HTTPS_PROXY` keeps working. A script that used up the whole budget gets no second attempt.
> - **A corrupt Chroma collection is dropped once, not once per parallel backfill** (#6115, thanks @mohitdixit02 and @0xABCD01, closes #6113). When the HNSW segment of a large collection was corrupt, every parallel per-project backfill that hit it passed the "drop only once" check before the first delete finished, and queued its own delete against chroma-mcp. In #6113 that ran 19 drops at once and pushed chroma-mcp to a 312 GB memory footprint, stalling a 32 GB Mac. Callers now join the one drop already running for that collection and share its outcome. A failed drop costs one attempt from the retry budget, not one per caller, and different collections still drop independently. The remaining asks from that report (a memory bound on chroma-mcp, stopping writes when a drop can't be confirmed, measuring footprint on macOS) are tracked in #3610.
> **Fixes**
> - **`--help` prints help instead of running the command** (#6142, thanks @liuyinchu). `npx claude-mem mcp --help` used to start the stdio server, and `status`, `doctor` and `hook` entered their runtime paths; `t3code` and its aliases rejected the flag. `-h` and `--help` are now handled before dispatch for these commands. Plain `mcp` still starts the server.
> **Docs**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(my-work): a press anywhere on a focus card opens its area (#6315)](https://github.com/thedotmack/claude-mem/commit/c1dc252bda98b1310ba3fa4b195efe49070d554b) | thedotmack |
| 2026-11-18 | [chore: promote 16.0.0 for auto-update](https://github.com/thedotmack/claude-mem/commit/cc4dbf5beb4bd98623e0b842e6617115f4e74631) | thedotmack |
| 2026-11-18 | [docs: update CHANGELOG for v16.0.0](https://github.com/thedotmack/claude-mem/commit/39c259a6ebfb8f607dc4f9ee6ecdbc2ef4e6223a) | thedotmack |
| 2026-11-18 | [chore: bump version to 16.0.0](https://github.com/thedotmack/claude-mem/commit/cc0fb95154581052f3611698b6ab6ec48a08f3f0) | thedotmack |
| 2026-11-18 | [fix(my-work): touch sizes, the Decide chip's edge and 12px labels (Ph…](https://github.com/thedotmack/claude-mem/commit/dd33958aadb2c50d5ba02550551675ebe1eb20f9) | thedotmack |
| 2026-11-18 | [fix: log two failures that were dropped without a word (#6302)](https://github.com/thedotmack/claude-mem/commit/441203361d53e92f13db35abb0a402976aa3f5ab) | thedotmack |
| 2026-11-18 | [ci: state the measured run behind the job's 35-minute limit](https://github.com/thedotmack/claude-mem/commit/5150d8e84d9f92f56250c836ed5e586e1d28e4af) | thedotmack |
| 2026-11-18 | [feat(my-work): Pro Max UI for 16.0.0 — My Work (#6210)](https://github.com/thedotmack/claude-mem/commit/36875d6488921503ebd3c3e69ad37eef9f1a09e4) | thedotmack |
| 2026-11-17 | [Remove Observation TV (#6295)](https://github.com/thedotmack/claude-mem/commit/99f8bed8256050b79933abf7a5e64590bb3cce2f) | thedotmack |
| 2026-11-17 | [perf(hook-spool): read the spool in bounded parallel batches (#6260)](https://github.com/thedotmack/claude-mem/commit/bbd8fa2e7cfcc00c8c0b7b1d0c49b31ab144cd83) | Zhong-fan |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
