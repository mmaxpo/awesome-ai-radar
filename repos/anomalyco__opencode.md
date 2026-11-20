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
| ⭐ **Stars** | 228.2k |
| 🍴 **Forks** | 31.0k |
| 🐞 **Open issues + PRs** | [4.0k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 11% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) — 2026-11-18 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 744.1 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · 2d ago</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · 2d ago</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · 3d ago</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

### [process-daemon-v0.6.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.6.0) — process-daemon v0.6.0
<sub>2026-11-16 · 3d ago</sub>

> opencode-pty 0.6.0 (protocol 9) from packages/process-daemon, published to npm as @opencode/pty@0.6.0.

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 7d ago</sub>

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
| 2026-11-20 | [fix(app): keep the pinned group name field inside its menu without a …](https://github.com/anomalyco/opencode/commit/b958fc84d73e34a2fa021c285cd38c6de674adb9) | usrnk1 |
| 2026-11-20 | [fix(app): stop buttons from flashing dark on keyboard focus (#65177)](https://github.com/anomalyco/opencode/commit/e440d29274caf25fc844bc0461e1b246f2bce50c) | usrnk1 |
| 2026-11-20 | [fix(browser): show browser profiles inline and tidy settings copy (#6…](https://github.com/anomalyco/opencode/commit/22ecda23a923d30b64f4c74cc9a90bfabeb6a695) | usrnk1 |
| 2026-11-20 | [fix(session-ui): show subagent status as a colored bar and word in th…](https://github.com/anomalyco/opencode/commit/85951cb08614dfe6443905552cae49d59d2d6615) | arvsrn |
| 2026-11-20 | [feat(browser): open a link's new tab beside the tab it came from (#65…](https://github.com/anomalyco/opencode/commit/80d7c17d8e24b64deed205d166c7de812eeb3c64) | Hona |
| 2026-11-20 | [fix(browser): confirm before clearing browsing data (#65124)](https://github.com/anomalyco/opencode/commit/bfee96a859aa0d225b845d67625d34ea6ae773d2) | Hona |
| 2026-11-20 | [fix(install): stream curl download via stdout for confined curl (#65132)](https://github.com/anomalyco/opencode/commit/8b36735d5159e02a317cb57850122adc1f507354) | neriousy |
| 2026-11-20 | [fix(app): go back and forward with the mouse buttons on desktop (#65129)](https://github.com/anomalyco/opencode/commit/13efefcfd373be7c433762c5447b471a6da711d3) | neriousy |
| 2026-11-20 | [fix(app): recover child session permissions after reconnect (#65120)](https://github.com/anomalyco/opencode/commit/f0df6070f9fa54159d082f7539b8fb80e10688ba) | neriousy |
| 2026-11-20 | [fix(ui): show text field and line comment focus in high contrast mode…](https://github.com/anomalyco/opencode/commit/10e26d9d6cf8a16f78517e2da2ea6e3543e40085) | usrnk1 |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
