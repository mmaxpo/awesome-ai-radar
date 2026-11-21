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
| ⭐ **Stars** | 228.4k |
| 🍴 **Forks** | 31.0k |
| 🐞 **Open issues + PRs** | [4.1k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 10% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) — 2026-11-18 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 747.3 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · 3d ago</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · 3d ago</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · 4d ago</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

### [process-daemon-v0.6.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.6.0) — process-daemon v0.6.0
<sub>2026-11-16 · 4d ago</sub>

> opencode-pty 0.6.0 (protocol 9) from packages/process-daemon, published to npm as @opencode/pty@0.6.0.

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 8d ago</sub>

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
| 2026-11-21 | [docs(console): document embedding models (#65402)](https://github.com/anomalyco/opencode/commit/a61f2670442c951a7ea76c5a6a406ed2e2912c02) | vimtor |
| 2026-11-21 | [fix(desktop): draw the Windows caption buttons in the contrast theme'…](https://github.com/anomalyco/opencode/commit/ba5bbef82c9fc27e033a12ca50657f4ec8d629da) | Hona |
| 2026-11-21 | [fix(desktop): resync server event streams after Windows resumes from …](https://github.com/anomalyco/opencode/commit/32ae0197715f822fb1247504f81e3eefc7d3c8fb) | Hona |
| 2026-11-21 | [fix(desktop): reopen snapped, moved and minimized windows where they …](https://github.com/anomalyco/opencode/commit/3aff591323f73d8032f73fa7bb8a152bc230b328) | Hona |
| 2026-11-21 | [fix(desktop): open projects and new sessions from opencode:// links a…](https://github.com/anomalyco/opencode/commit/b310a05b5452b2d79a7ad3d49251c15876c2e54c) | Hona |
| 2026-11-21 | [fix(core): shell tool's structured result says why a command has no e…](https://github.com/anomalyco/opencode/commit/dcb24c74dc04fe6fdbe5a2515e18efa6bd39c9e1) | kitlangton |
| 2026-11-21 | [feat(desktop): show a count badge for sessions that need you on the W…](https://github.com/anomalyco/opencode/commit/edacc8686a8b89ed5aae75b2833fd99fcd8da7f9) | Hona |
| 2026-11-21 | [feat(desktop): flash the Windows taskbar button for requests that wai…](https://github.com/anomalyco/opencode/commit/844a6aa6feeb1a1e56f05af2436eec3ee8582653) | Hona |
| 2026-11-21 | [feat(desktop): open in Windows Terminal and list only installed apps …](https://github.com/anomalyco/opencode/commit/f05c0fdc0666618dbae69068a19cb310de84c911) | Hona |
| 2026-11-21 | [feat(core): a paired machine needs no approval (#65356)](https://github.com/anomalyco/opencode/commit/44593c514ec56444a5f49954fa6a30d27cb5270f) | kitlangton |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
