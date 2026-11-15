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
| ⭐ **Stars** | 117.2k |
| 🍴 **Forks** | 10.2k |
| 🐞 **Open issues + PRs** | [166](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 63% · JavaScript 32% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v15.18.4](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.4) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 852.0 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v15.18.4](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.4)
<sub>2026-11-15 · today</sub>

> **Fixes**
> - **Claude Code gets claude-mem's rules and tools once** (#6179). Before this, a Claude Code session got the same guidance from up to three places: the MCP server instructions, a memory block the local activation script wrote into `CLAUDE.md`, and a pointer line to `RULES-AND-TOOLS.md` (whose timeline legend was never actually loaded). Now there is one path. `MY-RULES.md`, which your `CLAUDE.md` already imports, ends with an import of `RULES-AND-TOOLS.md`, and Claude Code loads it from there.
>   - When that import chain is complete in Claude Code, the MCP server sends no instructions, and the SessionStart hook drops the `Access Claude-Mem Rules + Tools:` pointer line. The server only skips its instructions when the imported file holds exactly the text it would send.
>   - Other hosts, and Claude Code users who never set up My Rules, are unchanged.
>   - The worker adds the import to an existing `MY-RULES.md` once at startup, so current users get it without doing anything. It never creates the file. Writing `MY-RULES.md` also makes sure `RULES-AND-TOOLS.md` exists, so the import never points at a missing file.
>   - `scripts/activate-progressive-memory-local.mjs` no longer writes the memory block into Claude's `CLAUDE.md`. Codex `AGENTS.md` keeps it, because `AGENTS.md` has no imports.
> …

### [v15.18.3](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.3)
<sub>2026-11-12 · 2d ago</sub>

> **Critical fixes**
> - **Codex keeps recording after claude-mem updates** (#6058, thanks @wiesenthal). Codex approves a hook that ships inside a plugin against a fingerprint of the plugin's whole folder. Every claude-mem update rewrites that folder, so after every update Codex switched all seven claude-mem hooks off ("plugin contents changed; hook approval required") and Codex sessions stopped being saved, with no message. The installer now registers claude-mem's Codex hooks in your own `~/.codex/hooks.json`, and each hook runs the on-PATH `claude-mem` launcher, which finds the newest install by itself. Codex trusts a hook in `hooks.json` by its own definition and position, so one approval now lasts across updates. Other tools' hooks in that file are kept in place, a second install changes nothing, a `hooks.json` that can't be parsed is refused and left untouched, and uninstall removes only claude-mem's entries. Turning the claude-mem plugin off in Codex still stops capture. `npx claude-mem doctor` has a new `Codex hooks` row that warns when the plugin is on but its hooks are missing from `hooks.json`.
>   **Codex users: do this once after updating.**
>   1. Run `npx claude-mem install` and select Codex. `npx claude-mem update` and auto-update don't move the hooks, because older installers saved no agent selection. The installer prints `Registered 7 claude-mem hooks in <codex home>/hooks.json`.
>   2. Open interactive Codex, run `/hooks`, and approve the seven claude-mem hooks. `codex exec` can't ask for approval, so do this in interactive Codex first.
>   After that, updates don't need a new approval. Codex asks again only when a claude-mem hook's definition changes, when claude-mem adds a hook, or when another tool's hook listed before claude-mem's is removed.
> …

### [v15.18.2](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.2)
<sub>2026-11-12 · 2d ago</sub>

> **Critical fixes**
> - **Gemini CLI on Windows records again** (#6079, thanks @tanishqbaweja). On Windows, Gemini CLI runs hook commands through PowerShell. The hook commands claude-mem wrote started with a quoted path, which PowerShell rejects as a parser error. Every claude-mem Gemini hook (SessionStart, BeforeAgent, AfterTool, AfterAgent, SessionEnd) failed on every event since 15.18.0, so Gemini sessions on Windows saved nothing and got no saved context. Hook commands on Windows now start with PowerShell's `&` call operator, as the Cursor and Windsurf hooks already do. macOS and Linux are unchanged.
>   **Windows Gemini CLI users: run `npx claude-mem gemini install` once after updating.** `npx claude-mem update` and auto-update do not rewrite Gemini's hooks, so the broken commands stay until you reinstall them. The reinstall replaces the old commands, and `npx claude-mem gemini uninstall` removes both forms.
> **Improvements**
> - **My Work shows the real state of open work** (#6038). Jev now reads each open work-state item once per version on the 10-minute My Work check and labels it: the state its notes describe, plus which of its fields holds the next step and the result. At confidence 0.8 or higher, My Work shows a judged status in place of a quiet agent's stale `doing` or missing status (finished becomes Done, not checked; waiting on you becomes Needs you; abandoned becomes Closed). A status the agent set on purpose, such as `blocked`, is kept. Labels are stored in `work-view/work-state-labels.json`; the work-state log itself is never written. Notes are redacted before Jev reads them, calls are paced one a second, and a service refusal or outage stops the run without being retried until the next check.
> **CI**
> …

### [v15.18.1](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.1)
<sub>2026-11-12 · 3d ago</sub>

> **Critical fixes**
> - **The worker no longer fails to start when the database is busy at startup** (#6041). If the My Work refresh record was left as "running" by a restart and the database was locked at that moment, the repair write threw and took down the worker's whole startup, so memory stayed off until the next restart. The repair failure is now logged, and the next scheduled check tries again (whether or not scheduled refresh is on).
> - **`npx claude-mem update` and the daily auto-update keep your setup** (#6045). Before this, an unattended update reset a server or server-beta runtime back to the local worker, so capture moved off your server. A legacy install with no saved provider could also have its cloud sync turned off and its Anthropic env keys cleared. Updates now reuse your saved runtime, provider, model and agents. They don't reopen the browser setup or ask the setup questions again, and only ask for a Gemini or OpenRouter key if one is missing. `npx claude-mem install` is unchanged.
> - **My Work summaries stop retrying unusable model answers forever** (#6039, thanks @mohitdixit02, reported by @adminwat in #6037). When the model's answer failed validation, wasn't JSON or came back empty, the same unchanged request was resent every minute with no end. One report measured 104,869 calls, and the constant load starved a local Ollama runner. Each request version now gets at most 3 tries with a growing wait, then waits until its input or settings change. The card shows the actual reason. Thanks @balabommablock-cpu for testing and finding the empty-answer case.
> **Fixes**
> - **Lower observer cost by default** (#6031, thanks @kartik70, closes #5023). The observer's conversation budget drops from 400,000 to 100,000 characters (about 100K to about 26K tokens per turn in the issue's measurement). Installs that still hold the old shipped default move once; a value you set yourself is kept.
> …

### [v15.18.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.18.0)
<sub>2026-11-12 · 3d ago</sub>

> **eve agents get the same memory as Claude Code and Codex**
> `claude-mem/eve` now gives an eve agent the full claude-mem memory loop through your cmem.ai account (#6042).
> - **Session context:** each turn starts with the recent timeline from your memory. It is refreshed every turn under one message id, so it replaces itself instead of piling up.
> - **Recall each turn:** one search before the turn, as before.
> - **Recording is now on by default.** After each completed turn the provider sends the prompt, one observation per tool call, and a turn summary to cmem.ai as platform `eve`. Recorded tool calls and summaries come out of your cmem.ai observer allowance, the same allowance your other clients use. Pass `capture: false` to keep the old read-only behaviour; session context, recall, search and `remember` keep working.
>   - `<private>…</private>` regions and secret-shaped text are removed on your deployment before anything is sent, with the same rules the Cowork plugin uses.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [chore: promote 15.18.4 for auto-update](https://github.com/thedotmack/claude-mem/commit/62ca1eb865ddc08daad6a23e64f1418b928df7d0) | thedotmack |
| 2026-11-15 | [docs: update CHANGELOG for v15.18.4](https://github.com/thedotmack/claude-mem/commit/1fe538f4bee15c9e39c8f1d761bfbf7aa677c742) | thedotmack |
| 2026-11-15 | [chore: bump version to 15.18.4](https://github.com/thedotmack/claude-mem/commit/0f75ee66ea5811e448858b7af6220d44b8f1c617) | thedotmack |
| 2026-11-15 | [fix: deliver claude-mem rules and tools once, through the CLAUDE.md-i…](https://github.com/thedotmack/claude-mem/commit/ff25f7f3e8e101b9240ca1bbc9b2b922a95f7774) | thedotmack |
| 2026-11-13 | [docs: update README logo mark and preserve original lettering (#6104)](https://github.com/thedotmack/claude-mem/commit/0c488b54e761d7f6f4091b3a6e1958712f13b19d) | thedotmack |
| 2026-11-12 | [feat(vercel-chat): add explicit project memory example (#6084)](https://github.com/thedotmack/claude-mem/commit/b0a0e2f9d2098b46d7be38d7d4c2cb862b553e37) | Kirat0201 |
| 2026-11-12 | [fix(cost-report): take the owner name from config (#6085)](https://github.com/thedotmack/claude-mem/commit/218e649399adb94fb6138bf4dbb7934b8ea414c3) | MaxWang007 |
| 2026-11-12 | [chore: promote 15.18.3 for auto-update](https://github.com/thedotmack/claude-mem/commit/22c2fe14e07fe9fffaa663db5cf8b254d23d8413) | thedotmack |
| 2026-11-12 | [fix(worker): bound listing offsets on the worker plane at 10k (#5495 …](https://github.com/thedotmack/claude-mem/commit/ce07140989f25e4d76f9faa3c880b72ec30805c5) | xunguangzlj-cloud |
| 2026-11-12 | [perf(dedup): bound full-scan pair counting to one title (#6052)](https://github.com/thedotmack/claude-mem/commit/68122cd8ad41fe5a67cd07e715f42c08fde0a459) | Afloat16 |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
