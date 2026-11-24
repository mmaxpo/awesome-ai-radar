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
| ⭐ **Stars** | 119.5k |
| 🍴 **Forks** | 10.4k |
| 🐞 **Open issues + PRs** | [88](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 67% · JavaScript 29% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.1.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.2) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 931.2 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.1.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.2)
<sub>2026-11-24 · today</sub>

> **Installer improvements**
> - On phones, **Set up my agents** stays within reach while you review the detected tools or expand the agent list.
> - A fresh installation shows how many agents you set up and what Cloud Sync can remember across devices. Setup only offers scan details when it has results or a reading error to show.

### [v16.1.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.1)
<sub>2026-11-23 · today</sub>

> **Cloud Sync setup**
> - Select **Try Cloud Sync free for 30 days** from your focus areas to open monthly checkout. The trial requires a card and costs $0 today, then $12/month after 30 days.
> - Setup preselects detected agents. You can discover your recent work or start with your next session. Annual Cloud Sync ($99 upfront) and free local setup are available before checkout. If you already have Cloud Sync, connect your device with your existing plan.
> - After Cloud Sync activates, setup shows token usage from the original scan and offers optional hosted memory generation. Reloading or retrying checkout keeps the plan you selected.

### [v16.1.0](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.0)
<sub>2026-11-23 · yesterday</sub>

> **Standalone Cloud Sync in the installer**
> - Run `npx claude-mem install` and choose Cloud Sync to connect your devices while keeping your current memory provider. The monthly plan requires a card and includes a full 30-day trial, followed by $12 per month. The annual plan costs $99 upfront.
> - The installer carries your chosen plan into checkout and verifies that cmem.ai confirms the same offer. Hosted tokens are a separate, optional purchase. Existing bundled Pro setups keep their saved settings.
> - You can skip Cloud Sync during setup and keep memory local. Once the installer applies a choice, returning to the plan screen or reloading it preserves that choice.

### [v16.0.4](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.4)
<sub>2026-11-22 · yesterday</sub>

> **Fixes**
> - **Chroma search works again while the embedding model downloads** (#6399, closes the "Invalid port" part of #6365 reported by @FengJie2004, root cause found by @kevincommits). httpx 0.28 misread a bracketed IPv6 entry such as `[::1]` in `NO_PROXY` and failed with `Invalid port: ':1]'`, so chroma-mcp could not add documents and search fell back to FTS5. The chroma-mcp child now gets the same host without brackets (`::1`). Entries with a port, and every other entry, are unchanged.
> - **Context injection keeps observations whose concepts are an old plain string** (#6393, thanks @jiangjiang248, closes #6389 reported by @soarkit). Keyword search matched a legacy concept such as `缓存`, but context injection dropped the same observation. Both now read concepts through one shared SQL expression, so they cannot drift apart again.
> - **OpenCode Go answers My Work refresh and corpus steps** (#6395, thanks @HemanRamlal). The API agent now sends the `x-opencode-session` header OpenCode Go requires (one id per run), and turns reasoning off with `reasoning_effort: none`, which Go honors. Before, every step failed with `400 MissingSessionID`, or ran out of its answer budget while thinking.
> - **Expired live observer inputs are counted and reported** (#6394, thanks @Zhong-fan, closes #6391 reported by @abhiroopb). The live buffer still drops an input nobody claims within five minutes, and still never replays it. The WARN line now carries a running total, and `/api/processing-status` returns it as `expiredObserverInputs`, so the loss is visible without reading logs.
> - **`/api/tool-uses` refuses a bad date instead of ignoring it** (#6387, thanks @kevincommits). A `dateStart` or `dateEnd` that was not a number (an ISO date, a typo, or the parameter given twice) was dropped, and the listing returned rows from every date. It now answers 400 `INVALID_DATE`. Epoch-millisecond values work as before.
> …

### [v16.0.3](https://github.com/thedotmack/claude-mem/releases/tag/v16.0.3)
<sub>2026-11-21 · 2d ago</sub>

> **Critical fix**
> - **The OMP hook works with the server runtime** (#6367, thanks @flipcyde101, closes #6366 reported by @walynde). When `CLAUDE_MEM_RUNTIME` was `server` or `server-beta`, the OMP hook still sent everything to the local worker, so OMP sessions were dropped. The hook now reads `CLAUDE_MEM_SERVER_URL`, `CLAUDE_MEM_SERVER_API_KEY` and `CLAUDE_MEM_SERVER_PROJECT_ID` (or the `CLAUDE_MEM_SERVER_BETA_*` names; environment variables win over `settings.json`) and talks to the server's `/v1` API directly: session start, tool and reply events, context, and session end. It applies the same rules the worker applies before it saves anything: `<private>` blocks are stripped, excluded projects and `CLAUDE_MEM_SKIP_TOOLS` are honored, every prompt is recorded, and the project name comes from git. If the server settings are incomplete, it falls back to the worker as before.
> - **OMP users: run `npx claude-mem install --ide omp` once to get this fix.** The OMP hook is a copied file, so a plugin update alone does not replace it.
> **Fixes**
> - **Knowledge queries and corpus requests can no longer hang forever** (#6368, thanks @flipcyde101, closes #6364 reported by @soarkit). A stalled Agent SDK stream used to keep the request and its Claude CLI child alive with no end. A knowledge query or prime now stops after 10 minutes and a corpus request after 15, with a 504 error. The corpus stays locked until the timed-out work has really stopped, so it cannot write after a delete or rebuild.
> - **The "paused saving memories" notice goes away once Codex is saving** (#6374, thanks @ryrenz, closes #6372 reported by @raw34). After you switched `CLAUDE_MEM_PROVIDER` to `codex` following a Claude quota pause, every new session still said capture was paused until the old Claude cooldown ran out. The notice is now recomputed when Codex stores a memory.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Promote verified npm release v16.1.2 and date the installer changelog](https://github.com/thedotmack/claude-mem/commit/2c57eb156ee726c8f0f22502cc9bfcc0a8353526) | thedotmack |
| 2026-11-24 | [Keep mobile setup in reach and welcome fresh sessions (#6438)](https://github.com/thedotmack/claude-mem/commit/a046a6a9fd8fb1cc56466194487dca94e8212409) | thedotmack |
| 2026-11-23 | [feat(setup): open Cloud Sync checkout on first trial click (#6431)](https://github.com/thedotmack/claude-mem/commit/ecfc1c0bde70efc16839e3ffcdf02efce736512f) | thedotmack |
| 2026-11-23 | [test(build): assert the Codex no-hooks manifest ships (#6425)](https://github.com/thedotmack/claude-mem/commit/384305078d67808c95bbd6ec6c45392a5edc2e78) | DeryFerd |
| 2026-11-23 | [feat(doctor): report the database file and its WAL sidecars (#6429)](https://github.com/thedotmack/claude-mem/commit/09ee41e93da9bfa081429136582e7e3c6b58610e) | DeryFerd |
| 2026-11-23 | [fix(sync): validate TOKEN_VERIFY_URL as an https endpoint (#6427)](https://github.com/thedotmack/claude-mem/commit/bdb2c3f4bfe0f8b69e33bb3116474ba9dd30bcd5) | DeryFerd |
| 2026-11-23 | [fix(db): drain cached statements before closing the shared connection…](https://github.com/thedotmack/claude-mem/commit/2e766af97eb701ae7ec08c19364b43094845859a) | DeryFerd |
| 2026-11-23 | [fix(security): compare remote spool tokens without a length oracle (#…](https://github.com/thedotmack/claude-mem/commit/fe0c412e5287ca76cb8388a2140729e046b40498) | DeryFerd |
| 2026-11-23 | [test(backup): resolve the snapshot path expectation on Windows (#6424)](https://github.com/thedotmack/claude-mem/commit/b70f561f96ce0e15674f7689a220924a3d6e7cca) | DeryFerd |
| 2026-11-23 | [fix(context): keep all-project cache readable during catalog outages …](https://github.com/thedotmack/claude-mem/commit/74fdc443c131490de6f79453607af3b877a96ca8) | zhangkom |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
