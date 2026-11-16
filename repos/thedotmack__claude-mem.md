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
| ⭐ **Stars** | 117.5k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [94](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 64% · JavaScript 31% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 867.6 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0)
<sub>2026-11-16 · today</sub>

> **Continue a Claude Code or Codex conversation from My Work**
> Open a request in My Work, then open "Where this came from". Under each Claude Code or Codex conversation there is now a message box. Type a message and press Send, and that same conversation takes the turn. The reply shows right there (#6191; the command shapes follow @wiesenthal's answer code in #6054, and the commit credits him).
> - Each conversation keeps the messages you sent from My Work and their replies, in order. Stop ends a running turn.
> - The box says which folder the turn runs in. When the recorded folder no longer exists (common after a worktree is cleaned up), the turn runs in the nearest existing folder above it.
> - "Copy resume command" copies `claude --resume <id>` or `codex resume <id>`. On a Mac, "Open in Claude" opens a Claude Code conversation in the Claude desktop app.
> - One Send starts one headless resume (`claude --resume <id> -p --output-format json`, or `codex exec resume <id> - --skip-git-repo-check`) with your message on stdin. A failed turn is recorded as failed and never retried. Nothing is queued or saved for replay, and nothing starts at startup, on a timer or on reconnect.
> …

### [v15.18.5](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.5)
<sub>2026-11-15 · today</sub>

> **Critical fixes**
> - **The tree-sitter CLI installs on networks where its download script keeps failing** (#6110, thanks @rigel905, closes #6109). On some networks tree-sitter-cli's own `install.js` had its request reset every time, or exited 0 on a truncated file. The pinned SHA-256 check correctly refused the file, but nothing recovered after that, so `smart_search`, `smart_outline`, `smart_unfold` and the File Read Gate stayed off on every worker start, and `npx claude-mem repair` aborted. Now, when the script fails or leaves anything but the pinned executable, claude-mem fetches the same release asset directly, once, inside the same install time budget, and runs it only after it unpacks to the same pinned SHA-256. The script still runs first, so `HTTPS_PROXY` keeps working. A script that used up the whole budget gets no second attempt.
> - **A corrupt Chroma collection is dropped once, not once per parallel backfill** (#6115, thanks @mohitdixit02 and @0xABCD01, closes #6113). When the HNSW segment of a large collection was corrupt, every parallel per-project backfill that hit it passed the "drop only once" check before the first delete finished, and queued its own delete against chroma-mcp. In #6113 that ran 19 drops at once and pushed chroma-mcp to a 312 GB memory footprint, stalling a 32 GB Mac. Callers now join the one drop already running for that collection and share its outcome. A failed drop costs one attempt from the retry budget, not one per caller, and different collections still drop independently. The remaining asks from that report (a memory bound on chroma-mcp, stopping writes when a drop can't be confirmed, measuring footprint on macOS) are tracked in #3610.
> **Fixes**
> - **`--help` prints help instead of running the command** (#6142, thanks @liuyinchu). `npx claude-mem mcp --help` used to start the stdio server, and `status`, `doctor` and `hook` entered their runtime paths; `t3code` and its aliases rejected the flag. `-h` and `--help` are now handled before dispatch for these commands. Plain `mcp` still starts the server.
> **Docs**
> …

### [v15.18.4](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.4)
<sub>2026-11-15 · yesterday</sub>

> **Fixes**
> - **Claude Code gets claude-mem's rules and tools once** (#6179). Before this, a Claude Code session got the same guidance from up to three places: the MCP server instructions, a memory block the local activation script wrote into `CLAUDE.md`, and a pointer line to `RULES-AND-TOOLS.md` (whose timeline legend was never actually loaded). Now there is one path. `MY-RULES.md`, which your `CLAUDE.md` already imports, ends with an import of `RULES-AND-TOOLS.md`, and Claude Code loads it from there.
>   - When that import chain is complete in Claude Code, the MCP server sends no instructions, and the SessionStart hook drops the `Access Claude-Mem Rules + Tools:` pointer line. The server only skips its instructions when the imported file holds exactly the text it would send.
>   - Other hosts, and Claude Code users who never set up My Rules, are unchanged.
>   - The worker adds the import to an existing `MY-RULES.md` once at startup, so current users get it without doing anything. It never creates the file. Writing `MY-RULES.md` also makes sure `RULES-AND-TOOLS.md` exists, so the import never points at a missing file.
>   - `scripts/activate-progressive-memory-local.mjs` no longer writes the memory block into Claude's `CLAUDE.md`. Codex `AGENTS.md` keeps it, because `AGENTS.md` has no imports.
> …

### [v15.18.3](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.3)
<sub>2026-11-12 · 3d ago</sub>

> **Critical fixes**
> - **Codex keeps recording after claude-mem updates** (#6058, thanks @wiesenthal). Codex approves a hook that ships inside a plugin against a fingerprint of the plugin's whole folder. Every claude-mem update rewrites that folder, so after every update Codex switched all seven claude-mem hooks off ("plugin contents changed; hook approval required") and Codex sessions stopped being saved, with no message. The installer now registers claude-mem's Codex hooks in your own `~/.codex/hooks.json`, and each hook runs the on-PATH `claude-mem` launcher, which finds the newest install by itself. Codex trusts a hook in `hooks.json` by its own definition and position, so one approval now lasts across updates. Other tools' hooks in that file are kept in place, a second install changes nothing, a `hooks.json` that can't be parsed is refused and left untouched, and uninstall removes only claude-mem's entries. Turning the claude-mem plugin off in Codex still stops capture. `npx claude-mem doctor` has a new `Codex hooks` row that warns when the plugin is on but its hooks are missing from `hooks.json`.
>   **Codex users: do this once after updating.**
>   1. Run `npx claude-mem install` and select Codex. `npx claude-mem update` and auto-update don't move the hooks, because older installers saved no agent selection. The installer prints `Registered 7 claude-mem hooks in <codex home>/hooks.json`.
>   2. Open interactive Codex, run `/hooks`, and approve the seven claude-mem hooks. `codex exec` can't ask for approval, so do this in interactive Codex first.
>   After that, updates don't need a new approval. Codex asks again only when a claude-mem hook's definition changes, when claude-mem adds a hook, or when another tool's hook listed before claude-mem's is removed.
> …

### [v15.18.2](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.2)
<sub>2026-11-12 · 3d ago</sub>

> **Critical fixes**
> - **Gemini CLI on Windows records again** (#6079, thanks @tanishqbaweja). On Windows, Gemini CLI runs hook commands through PowerShell. The hook commands claude-mem wrote started with a quoted path, which PowerShell rejects as a parser error. Every claude-mem Gemini hook (SessionStart, BeforeAgent, AfterTool, AfterAgent, SessionEnd) failed on every event since 15.18.0, so Gemini sessions on Windows saved nothing and got no saved context. Hook commands on Windows now start with PowerShell's `&` call operator, as the Cursor and Windsurf hooks already do. macOS and Linux are unchanged.
>   **Windows Gemini CLI users: run `npx claude-mem gemini install` once after updating.** `npx claude-mem update` and auto-update do not rewrite Gemini's hooks, so the broken commands stay until you reinstall them. The reinstall replaces the old commands, and `npx claude-mem gemini uninstall` removes both forms.
> **Improvements**
> - **My Work shows the real state of open work** (#6038). Jev now reads each open work-state item once per version on the 10-minute My Work check and labels it: the state its notes describe, plus which of its fields holds the next step and the result. At confidence 0.8 or higher, My Work shows a judged status in place of a quiet agent's stale `doing` or missing status (finished becomes Done, not checked; waiting on you becomes Needs you; abandoned becomes Closed). A status the agent set on purpose, such as `blocked`, is kept. Labels are stored in `work-view/work-state-labels.json`; the work-state log itself is never written. Notes are redacted before Jev reads them, calls are paced one a second, and a service refusal or outage stops the run without being retried until the next check.
> **CI**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(import): Mem0 and Supermemory import acceptance for 16.0.0 (#6206)](https://github.com/thedotmack/claude-mem/commit/82d3602e2e43503ffd39c180b2af5f7521fc457b) | thedotmack |
| 2026-11-16 | [chore: promote 15.19.0 for auto-update](https://github.com/thedotmack/claude-mem/commit/f705e9b99601dd9ac03e2f77c5aded6ff3d9471b) | thedotmack |
| 2026-11-16 | [docs: say the 15.19.0 provenance tag shows on the server runtime](https://github.com/thedotmack/claude-mem/commit/8710ec4f107972d8b76ef67a41872ddda06d92b9) | thedotmack |
| 2026-11-16 | [docs: update CHANGELOG for v15.19.0](https://github.com/thedotmack/claude-mem/commit/9bf4c6564893c7284082609c086860a18f02aa13) | thedotmack |
| 2026-11-16 | [chore: bump version to 15.19.0](https://github.com/thedotmack/claude-mem/commit/01a86b235d3b9854c18e1841133d9a8e7fe1171a) | thedotmack |
| 2026-11-16 | [feat(my-work): continue a Claude Code or Codex conversation from its …](https://github.com/thedotmack/claude-mem/commit/7acc9328706a529909125f2355736f55abdb48e5) | thedotmack |
| 2026-11-15 | [feat(v16): import memories from Mem0 and Supermemory (#6106)](https://github.com/thedotmack/claude-mem/commit/5cc2fb16aa6d36b47d777d58dfd6456065510f9f) | thedotmack |
| 2026-11-15 | [Observation provenance: always know which agent made a memory (#6100)](https://github.com/thedotmack/claude-mem/commit/9ea3e0eb86f0dcf37a262d2fd7217cdcc5bc62a2) | thedotmack |
| 2026-11-15 | [docs(cline,kilo): say explicit MCP saves honor project exclusions (#6…](https://github.com/thedotmack/claude-mem/commit/63a6a95f84505bfc52415445b847bf7e1509e60f) | thedotmack |
| 2026-11-15 | [fix(deep-search): derive the child deadline from the remaining budget…](https://github.com/thedotmack/claude-mem/commit/d40d249ca3ebdafe44d070aee7ef9af311c9ffff) | DeryFerd |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
