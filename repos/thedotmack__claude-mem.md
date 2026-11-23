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
| ⭐ **Stars** | 119.2k |
| 🍴 **Forks** | 10.4k |
| 🐞 **Open issues + PRs** | [94](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 66% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.1.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 918.5 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.1.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.0)
<sub>2026-11-23 · today</sub>

> **Standalone Cloud Sync in the installer**
> - Run `npx claude-mem install` and choose Cloud Sync to connect your devices while keeping your current memory provider. The monthly plan requires a card and includes a full 30-day trial, followed by $12 per month. The annual plan costs $99 upfront.
> - The installer carries your chosen plan into checkout and verifies that cmem.ai confirms the same offer. Hosted tokens are a separate, optional purchase. Existing bundled Pro setups keep their saved settings.
> - You can skip Cloud Sync during setup and keep memory local. Once the installer applies a choice, returning to the plan screen or reloading it preserves that choice.

### [v16.0.4](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.4)
<sub>2026-11-22 · today</sub>

> **Fixes**
> - **Chroma search works again while the embedding model downloads** (#6399, closes the "Invalid port" part of #6365 reported by @FengJie2004, root cause found by @kevincommits). httpx 0.28 misread a bracketed IPv6 entry such as `[::1]` in `NO_PROXY` and failed with `Invalid port: ':1]'`, so chroma-mcp could not add documents and search fell back to FTS5. The chroma-mcp child now gets the same host without brackets (`::1`). Entries with a port, and every other entry, are unchanged.
> - **Context injection keeps observations whose concepts are an old plain string** (#6393, thanks @jiangjiang248, closes #6389 reported by @soarkit). Keyword search matched a legacy concept such as `缓存`, but context injection dropped the same observation. Both now read concepts through one shared SQL expression, so they cannot drift apart again.
> - **OpenCode Go answers My Work refresh and corpus steps** (#6395, thanks @HemanRamlal). The API agent now sends the `x-opencode-session` header OpenCode Go requires (one id per run), and turns reasoning off with `reasoning_effort: none`, which Go honors. Before, every step failed with `400 MissingSessionID`, or ran out of its answer budget while thinking.
> - **Expired live observer inputs are counted and reported** (#6394, thanks @Zhong-fan, closes #6391 reported by @abhiroopb). The live buffer still drops an input nobody claims within five minutes, and still never replays it. The WARN line now carries a running total, and `/api/processing-status` returns it as `expiredObserverInputs`, so the loss is visible without reading logs.
> - **`/api/tool-uses` refuses a bad date instead of ignoring it** (#6387, thanks @kevincommits). A `dateStart` or `dateEnd` that was not a number (an ISO date, a typo, or the parameter given twice) was dropped, and the listing returned rows from every date. It now answers 400 `INVALID_DATE`. Epoch-millisecond values work as before.
> …

### [v16.0.3](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.3)
<sub>2026-11-21 · yesterday</sub>

> **Critical fix**
> - **The OMP hook works with the server runtime** (#6367, thanks @flipcyde101, closes #6366 reported by @walynde). When `CLAUDE_MEM_RUNTIME` was `server` or `server-beta`, the OMP hook still sent everything to the local worker, so OMP sessions were dropped. The hook now reads `CLAUDE_MEM_SERVER_URL`, `CLAUDE_MEM_SERVER_API_KEY` and `CLAUDE_MEM_SERVER_PROJECT_ID` (or the `CLAUDE_MEM_SERVER_BETA_*` names; environment variables win over `settings.json`) and talks to the server's `/v1` API directly: session start, tool and reply events, context, and session end. It applies the same rules the worker applies before it saves anything: `<private>` blocks are stripped, excluded projects and `CLAUDE_MEM_SKIP_TOOLS` are honored, every prompt is recorded, and the project name comes from git. If the server settings are incomplete, it falls back to the worker as before.
> - **OMP users: run `npx claude-mem install --ide omp` once to get this fix.** The OMP hook is a copied file, so a plugin update alone does not replace it.
> **Fixes**
> - **Knowledge queries and corpus requests can no longer hang forever** (#6368, thanks @flipcyde101, closes #6364 reported by @soarkit). A stalled Agent SDK stream used to keep the request and its Claude CLI child alive with no end. A knowledge query or prime now stops after 10 minutes and a corpus request after 15, with a 504 error. The corpus stays locked until the timed-out work has really stopped, so it cannot write after a delete or rebuild.
> - **The "paused saving memories" notice goes away once Codex is saving** (#6374, thanks @ryrenz, closes #6372 reported by @raw34). After you switched `CLAUDE_MEM_PROVIDER` to `codex` following a Claude quota pause, every new session still said capture was paused until the old Claude cooldown ran out. The notice is now recomputed when Codex stores a memory.
> …

### [v16.0.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.2)
<sub>2026-11-20 · 2d ago</sub>

> **Critical fix**
> - **An auto-update no longer deletes the plugin version a running Claude Code session was loaded from** (#6352, thanks @0xABCD01, closes #6349 reported by @justindrp). The cache sweep keeps a version folder while the Claude Code process recorded in its `.in_use` file is alive. On macOS and BSD, a few seconds of difference between the start time Claude Code recorded and the one `ps` reports was read as PID reuse, so the sweep deleted the folder from under a live session and every hook failed for the rest of that session. A start-time mismatch no longer removes the folder while the process at that PID is still Claude Code. A PID that now belongs to another program is still pruned as before.
> - **Every cache prune now logs why and who.** The worker writes one log line per removed version with its reason (orphaned or superseded) and the `.in_use` records it rejected and why (process exited or start-time mismatch), so any removal can be traced from the log alone.
> **Fixes**
> - **The session-start card is drawn on Team and Enterprise accounts** (#6353, thanks @KeithMoc, closes #6314 reported by @TimoWestland). When an organization plugin runs first and the card's usual hooks never fire, the card now asks for itself from the `session.start` hook and the context hook answers it.
> - **My Work detects OpenCode 2.x connections** (#6340, thanks @ZedingZhang, closes #6339 reported by @Realauster). The login probe reads OpenCode's JSON output, so a connected provider is no longer reported as logged out on OpenCode 2.3.2.
> …

### [v16.0.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.1)
<sub>2026-11-19 · 4d ago</sub>

> **Critical fixes**
> - **Signing in to Codex works again on Windows while claude-mem runs** (#6332, thanks @ffe111, closes #6331). The private Codex home that claude-mem's app-server uses got its `auth.json` through a hard link to your real `~/.codex/auth.json`. Codex refuses to replace a credential file with more than one hard link (`persist_failed: atomic credential replacement does not support hard-linked files`), so `codex login` and token refresh failed for as long as that home existed. The private home now gets a symlink, which Codex follows. Only on Windows, and only when a symlink is not permitted (no Developer Mode or elevation), it gets a private copy instead. Any other error still fails loudly.
> - **A probe answered with `<skip_summary/>` ends the quota cooldown** (#6324, thanks @vaibhav375, closes #6322). After a quota hit, the worker probes the provider and clears the cooldown once a probe stores a memory. A probe the provider answered with a valid `<skip_summary/>` stores nothing, so the cooldown never cleared and the worker re-probed every 5 minutes for as long as that session only skipped. A valid skip now releases the cooldown too, on both the store path and the early path before the memory session id is known. Observer-health success still needs a real store.
> **Fixes**
> - **Search falls back to SQLite instead of failing when Chroma is slow** (#6327, thanks @REI-330, closes #6323). The MCP client gives a search 30 s, while each Chroma read waited up to 60 s, so a slow query was still running when the caller gave up and the SQLite/FTS5 fallback never ran. A search now shares one 20 s budget across its Chroma reads and falls back when it runs out, without restarting a healthy chroma-mcp.
> - **Chroma rebuilds no longer hold a core for hours** (#6299, thanks @srieteja). A full backfill now pauses after each row for its write time times `CLAUDE_MEM_CHROMA_BACKFILL_PAUSE_RATIO` (default 1, 0 turns it off), and chroma-mcp starts under `nice` (`CLAUDE_MEM_CHROMA_PROCESS_NICE`, default 10) outside Windows. Live sync is unchanged.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [chore: promote v16.1.0 for auto-update and record its release notes](https://github.com/thedotmack/claude-mem/commit/29bc1cdf32aca60b3bfeec3b718d4ed6614b4f97) | thedotmack |
| 2026-11-23 | [feat: release standalone Cloud Sync in the installer (v16.1.0) (#6362)](https://github.com/thedotmack/claude-mem/commit/febafe47c7db20dc4825f353231b56c62b3ab269) | thedotmack |
| 2026-11-22 | [chore: promote 16.0.4 for auto-update](https://github.com/thedotmack/claude-mem/commit/b14ac567600f6d91b77d2d6e7a34bb0d9e2922a3) | thedotmack |
| 2026-11-22 | [docs: update CHANGELOG for v16.0.4](https://github.com/thedotmack/claude-mem/commit/8a79c9aaaaf9cd9a2e0bd982006d886bd01def7e) | thedotmack |
| 2026-11-22 | [chore: bump version to 16.0.4](https://github.com/thedotmack/claude-mem/commit/d0f7c0457ec61d276e1746d74dcc3e34df7323f5) | thedotmack |
| 2026-11-22 | [fix(advisor-routes): bound the advisor-calls offset like the listing …](https://github.com/thedotmack/claude-mem/commit/af2fa241d45cd6b342262f55b64e997eb62befce) | DeryFerd |
| 2026-11-22 | [refactor(listings): ask one helper whether an offset is past the cap …](https://github.com/thedotmack/claude-mem/commit/b6344d18d8357e9fe2d5db3ff06613cc4a7b91ec) | DeryFerd |
| 2026-11-22 | [fix(sync-api): validate the projector URL before sending its bearer s…](https://github.com/thedotmack/claude-mem/commit/a932aaf936e11898422604e634d19e45a44b24dd) | DeryFerd |
| 2026-11-22 | [fix(context): retain legacy string concepts during injection (#6393)](https://github.com/thedotmack/claude-mem/commit/a48ad2fb24f93bd2b3db69c889f4821d425cd937) | jiangjiang248 |
| 2026-11-22 | [fix(dedup): reject a fractional limit instead of answering 500 (#6388)](https://github.com/thedotmack/claude-mem/commit/b6070cacf2e8498d6ce76df71117f9cb66570997) | REI-330 |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
