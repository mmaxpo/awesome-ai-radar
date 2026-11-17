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
| ⭐ **Stars** | 227.5k |
| 🍴 **Forks** | 30.8k |
| 🐞 **Open issues + PRs** | [4.1k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 11% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6) — 2026-11-17 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 724.1 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · today</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

### [process-daemon-v0.6.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.6.0) — process-daemon v0.6.0
<sub>2026-11-16 · today</sub>

> opencode-pty 0.6.0 (protocol 9) from packages/process-daemon, published to npm as @opencode/pty@0.6.0.

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 4d ago</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

### [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — process-daemon v0.5.2
<sub>2026-11-11 · 5d ago</sub>

> opencode-pty 0.5.2 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.2.

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · 7d ago</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(app): keep the browser pane live while resizing panels on macOS (…](https://github.com/anomalyco/opencode/commit/09b7b1e726ec4098ab063b51c76d2ecdc30003e7) | usrnk1 |
| 2026-11-17 | [fix(session-ui): improve spacing for wrapped question descriptions (#…](https://github.com/anomalyco/opencode/commit/ee5dfa9d416282fd5dc5dc800bf957f54e65879c) | usrnk1 |
| 2026-11-17 | [feat(desktop): browser toolbar with mobile and custom viewport sizes …](https://github.com/anomalyco/opencode/commit/1cb0633c8b2ed95ec2af645a4c541c5e219e98ed) | usrnk1 |
| 2026-11-17 | [fix(app): open settings on the first sidebar item by listing preferen…](https://github.com/anomalyco/opencode/commit/0d901e21056c8a8671835ebd882fb8cd4651ee12) | usrnk1 |
| 2026-11-17 | [feat(app): move long message folding to Timeline preferences (#64441)](https://github.com/anomalyco/opencode/commit/4048ff9feec9845328648edfd0a448356ef0ed52) | usrnk1 |
| 2026-11-17 | [docs(console): list Google as a ZDR exception (#64435)](https://github.com/anomalyco/opencode/commit/95b0de8aa3154c293bccd7d5b324e2b44dac4ad8) | MrMushrooooom |
| 2026-11-17 | [feat(opencode): publish artifacts to OpenCode Console through a conso…](https://github.com/anomalyco/opencode/commit/1f01f83797d1ab5f096ea6fcaf03c9368e72848c) | adamdotdevin |
| 2026-11-17 | [fix(app): show either the variant or the budget on a model row, never…](https://github.com/anomalyco/opencode/commit/887f6cd44bbb5e68826ef53e76047b7e9e34c3ca) | arvsrn |
| 2026-11-17 | [fix(session-ui): select diff text and comment on it from a toolbar (#…](https://github.com/anomalyco/opencode/commit/a9a35b4b4ce35573d71207e246e770cfa26ff0e1) | arvsrn |
| 2026-11-17 | [feat(app): open the model picker flyout from the keyboard and show bu…](https://github.com/anomalyco/opencode/commit/1e6bf4c34acf7a6b467cade161e4a917a05b753e) | arvsrn |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
