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
| ⭐ **Stars** | 119.7k |
| 🍴 **Forks** | 10.4k |
| 🐞 **Open issues + PRs** | [93](https://github.com/thedotmack/claude-mem/issues) |
| 💻 **Languages** | TypeScript 67% · JavaScript 28% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `ai-agents` `ai-memory` `anthropic` `artificial-intelligence` `claude` `claude-agent-sdk` `claude-agents` `claude-code` `claude-code-plugin` `claude-skills` `long-term-memory` `mem0` `openmemory` `supermemory` `chromadb` `sqlite` `embeddings` `memory-engine` `rag` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-08-31 |
| 📦 **Latest release** | [v16.1.5](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.5) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 943.1 MB |
| 🌐 **Website** | https://claude-mem.ai |

## 📦 Recent releases

### [v16.1.5](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.5)
<sub>2026-11-25 · today</sub>

> - Eligible existing installs receive a dated holiday Cloud Sync offer from the new Messages from Claude-Mem queue on their next interactive startup. Each installation records the dispatch time locally. Agents can optionally acknowledge sharing the message with `claude-mem messages acknowledge <message-id>`.
> - The local memory timeline now offers eligible Claude-Mem users a 30-day Cloud Sync and remote Work Viewer trial with no credit card required. Dismissing the invitation hides it on that browser.
> - The remote Work Viewer now guides trial users through six workflows, including cross-agent handoffs, decision tracing, and optional weekday briefings and Friday reviews.
> - The Cloud Sync giveaway GIF at the top of the project README links to cmem.ai.

### [v16.1.4](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.4)
<sub>2026-11-25 · today</sub>

> - Setup offers a 30-day Cloud Sync trial without a credit card. People installing directly or with an agent can choose a private, signed-in My Work view. Explicit local and custom sync settings are preserved.
> - The cloud viewer uses the current account to load synced work, evidence and review changes. Returning to a tab verifies the signed-in account before showing its contents. Retrying a save after a lost response reuses the same action ID.
> - During the trial, My Work offers optional guidance for trying cross-agent sync and shows when to add a payment method to continue.

### [v16.1.3](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.3)
<sub>2026-11-24 · today</sub>

> **Critical fix**
> - **OpenRouter errors sent with HTTP 200 no longer discard queued observations** (#6448, thanks @ryrenz, closes #6447 reported by @claudemeister). OpenRouter can accept a request and then report a temporary failure ("high demand", "temporarily rate-limited upstream") in the body of a 200 response, as `{"error":{"code":<number>,...}}`. The observer classified these as unrecoverable, so it did not retry, pause or fall back: it finalized the session and discarded its queued observations. The reporter lost 8.5% to 16% of events in one day. The classifier now uses the numeric `error.code` when the HTTP status is 2xx, so code 429 is a rate limit and 5xx is transient. A litellm output failure ("Unable to get json") stays an output failure and is never resent, because the model already ran and was billed.
> **Fixes**
> - **`claude-mem server jobs retry` no longer reports `requeued` for a job it did not publish** (#6439, thanks @HEOJUNFO). If Redis was unreachable, or the shell had no `CLAUDE_MEM_QUEUE_ENGINE=bullmq`, the command printed `"outcome": "requeued"` and exited 0, and the job never ran. It now moves the row back to `failed` with `retry_republish_failed`, prints the reason and exits 1, so the same command works once the queue is reachable.
> - **Server generation jobs wait out a provider's Retry-After** (#6440, thanks @HEOJUNFO). A rate-limited job was redelivered after 5s and 10s whatever wait the provider asked for, so all three attempts could land inside the window and the job failed with no observation. When the provider sends a wait, the job is now delayed for it (capped at 60s, the same cap the worker uses). Rate limits without a wait, timeouts and 5xx keep the 5s/10s backoff.
> - **`POST /v1/events` answers 400 instead of 500 for data Postgres can never store** (#6446, thanks @alessandropcostabr). A tool result with a NUL character (for example from reading a binary file) failed every time, and a 500 sent it to the local spool to be retried until the window expired. NUL is now removed from payload and metadata before private-tag stripping and redaction, and other data exceptions (SQLSTATE class 22) answer `400 InvalidData`.
> …

### [v16.1.2](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.2)
<sub>2026-11-24 · yesterday</sub>

> **Installer improvements**
> - On phones, **Set up my agents** stays within reach while you review the detected tools or expand the agent list.
> - A fresh installation shows how many agents you set up and what Cloud Sync can remember across devices. Setup only offers scan details when it has results or a reading error to show.

### [v16.1.1](https://github.com/thedotmack/claude-mem/releases/tag/v16.1.1)
<sub>2026-11-23 · yesterday</sub>

> **Cloud Sync setup**
> - Select **Try Cloud Sync free for 30 days** from your focus areas to open monthly checkout. The trial requires a card and costs $0 today, then $12/month after 30 days.
> - Setup preselects detected agents. You can discover your recent work or start with your next session. Annual Cloud Sync ($99 upfront) and free local setup are available before checkout. If you already have Cloud Sync, connect your device with your existing plan.
> - After Cloud Sync activates, setup shows token usage from the original scan and offers optional hosted memory generation. Reloading or retrying checkout keeps the plan you selected.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Ship the Cloud Sync timeline gift and dated startup messages in 16.1.…](https://github.com/thedotmack/claude-mem/commit/11b47f9f4b8dc3614fab7452647f578886468849) | thedotmack |
| 2026-11-25 | [Merge pull request #6469 from thedotmack/feat/cloud-sync-remote-routines](https://github.com/thedotmack/claude-mem/commit/4339da34551319c976caad3f1781309803bfb1bf) | thedotmack |
| 2026-11-25 | [Publish the verified Work Viewer onboarding bundle](https://github.com/thedotmack/claude-mem/commit/a7f8f8f30d6796aa5bd289539a9f294468c16359) | thedotmack |
| 2026-11-25 | [Guide Cloud Sync trials through remote work and recurring routines](https://github.com/thedotmack/claude-mem/commit/6996017c489c20cee3eeed13ee991ef9127a980c) | thedotmack |
| 2026-11-25 | [Merge pull request #6467 from thedotmack/docs/cloud-sync-giveaway-gif](https://github.com/thedotmack/claude-mem/commit/18789c834abcade74355e48631088cf728d52a93) | thedotmack |
| 2026-11-25 | [Show the Cloud Sync giveaway GIF at the top of the README](https://github.com/thedotmack/claude-mem/commit/8ec2bd3310a96431e2351d107ac38458ee79b631) | thedotmack |
| 2026-11-25 | [Merge pull request #6456 from thedotmack/feat/shared-cloud-sync-insta…](https://github.com/thedotmack/claude-mem/commit/11fdec893eb4ece18ff946758e75e82c92aff71b) | thedotmack |
| 2026-11-25 | [Merge the credit-cap provider fallback into the Cloud Sync installer …](https://github.com/thedotmack/claude-mem/commit/4a08f6dda4fe0741b10dcfd66aec32059b7ccbdb) | thedotmack |
| 2026-11-25 | [build: prepare release bundles](https://github.com/thedotmack/claude-mem/commit/a97d89f9903520bce5c08d64042a1e7fbf7845ca) | github-actions[bot] |
| 2026-11-25 | [Use the available default backup when a regular agent plan is unavail…](https://github.com/thedotmack/claude-mem/commit/cc55c17db4e8a9714d7ad25b26accaa8cff7baef) | thedotmack |

[See all commits ↗](https://github.com/thedotmack/claude-mem/commits)

## ⬇️ Get it

```bash
git clone https://github.com/thedotmack/claude-mem.git
```
