# anomalyco/opencode

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/anomalyco/opencode)

> The open source coding agent.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Open-source AI coding agent |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 228.0k |
| 🍴 **Forks** | 30.9k |
| 🐞 **Open issues + PRs** | [4.0k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 11% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) — 2026-11-18 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 738.1 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · yesterday</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · yesterday</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · 2d ago</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

### [process-daemon-v0.6.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.6.0) — process-daemon v0.6.0
<sub>2026-11-16 · 2d ago</sub>

> opencode-pty 0.6.0 (protocol 9) from packages/process-daemon, published to npm as @opencode/pty@0.6.0.

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 6d ago</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [fix(core): respect repository line endings and symlinks in git diffs …](https://github.com/anomalyco/opencode/commit/0a297bf15de78acc4dce99b837b7e5879c1ff20b) | neriousy |
| 2026-11-19 | [test: fix Windows timeouts in server and sdk contract tests (#64879)](https://github.com/anomalyco/opencode/commit/b8928b93605e925b189bb26b480586b8d9d8df38) | neriousy |
| 2026-11-19 | [fix(app): match integrations dialog to palette width (#64882)](https://github.com/anomalyco/opencode/commit/40f7e4da2b6063121995c4afcda799341bda28c6) | arvsrn |
| 2026-11-19 | [test(core): fix Windows unit flakes in video, shell, and session-tabs…](https://github.com/anomalyco/opencode/commit/354afc493ebde19701f14b8b800d28fb9f8ffce7) | neriousy |
| 2026-11-19 | [test(tui): fix shell output, session link and terminal pane flakes (#…](https://github.com/anomalyco/opencode/commit/e3ee0821677672c5db793d82f669f14406afadc3) | neriousy |
| 2026-11-19 | [test(app): measure the subagent indicator's exit in the task that sta…](https://github.com/anomalyco/opencode/commit/299193f88dbac910558ae73b29db81eaaa24c88b) | neriousy |
| 2026-11-19 | [fix(desktop): open PowerShell 7 from Open in PowerShell on Windows (#…](https://github.com/anomalyco/opencode/commit/09cc0c7a59e08dda5fdfb09696f565b52f3cd10e) | neriousy |
| 2026-11-19 | [Opentui 0.9.0 (#63989)](https://github.com/anomalyco/opencode/commit/4c5298bce4c48c2a3510809e8f15fa549fadd7bf) | simonklee |
| 2026-11-19 | [feat(app): add previous and next match buttons to conversation search…](https://github.com/anomalyco/opencode/commit/88c90d08add7dd899a0caefc15609fdbb1d4b2ed) | neriousy |
| 2026-11-19 | [fix(ai): default MiniMax text video ratio (#64822)](https://github.com/anomalyco/opencode/commit/d33b5783338b8b350aafc09f7dc2701eeba52a9a) | heimoshuiyu |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
