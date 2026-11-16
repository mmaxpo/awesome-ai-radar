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
| ⭐ **Stars** | 227.2k |
| 🍴 **Forks** | 30.8k |
| 🐞 **Open issues + PRs** | [4.0k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 11% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) — 2026-11-13 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 716.5 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 3d ago</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

### [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — process-daemon v0.5.2
<sub>2026-11-11 · 4d ago</sub>

> opencode-pty 0.5.2 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.2.

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · 6d ago</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

### [v2.2.6](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)
<sub>2026-11-06 · 9d ago</sub>

> **Highlights**
> - **Shared MCP Connections**: Turn on pooling for an MCP server to share one connection across projects with the same setup, so you run fewer processes and start faster. ([#61185](https://github.com/anomalyco/opencode/pull/61185))
> - **GUI Plugin Themes and New Slots**: GUI plugins can now add color themes, render or add actions to code blocks, and use native settings and menu components. ([#61485](https://github.com/anomalyco/opencode/pull/61485), [#61533](https://github.com/anomalyco/opencode/pull/61533), [#61527](https://github.com/anomalyco/opencode/pull/61527), [#61509](https://github.com/anomalyco/opencode/pull/61509))
> - **Mobile Composer Dock**: On phones and tablets, composer actions now sit in a touch dock above the keyboard with larger buttons. ([#61773](https://github.com/anomalyco/opencode/pull/61773))
> - **Scripted Runs in Worktrees**: Run `opencode run -w` to start the session in a new git worktree, or `--worktree=<name>` to name it. ([#60712](https://github.com/anomalyco/opencode/pull/60712))
> - **Automatically Archived Runs**: Add `--archived` to `opencode run` to keep scripted and CI sessions out of your inbox and session lists. ([#61270](https://github.com/anomalyco/opencode/pull/61270))
> …

### [process-daemon-v0.5.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.0) — process-daemon v0.5.0
<sub>2026-11-05 · 10d ago</sub>

> opencode-pty 0.5.0 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.0.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [test(app): check the eye hover overlay on background-image after the …](https://github.com/anomalyco/opencode/commit/56b5947eaa184eee285240ecabdbbed9599ca5d0) | opencodejr[bot] |
| 2026-11-16 | [feat(app): replace Home in the desktop Projects sidebar (#64220)](https://github.com/anomalyco/opencode/commit/e85035a36ca1139b0c76844a100f3fa6e2eb26e5) | usrnk1 |
| 2026-11-16 | [fix(app): unify dialog styles (#64216)](https://github.com/anomalyco/opencode/commit/56625a3e1f8ab68487dee4e723270876d6e840fc) | arvsrn |
| 2026-11-16 | [fix(app): hide the sidebar resize pill (#64219)](https://github.com/anomalyco/opencode/commit/a4c9642cf929077a8024cd47612541673fd624dd) | arvsrn |
| 2026-11-16 | [fix(app): enlarge image attachment thumbnails to 3:2 (#64215)](https://github.com/anomalyco/opencode/commit/26f2522e60a924b8bad95725ede56b55281fb46c) | usrnk1 |
| 2026-11-16 | [fix(browser): space URL bar action buttons 6px apart (#64214)](https://github.com/anomalyco/opencode/commit/fd95bf0d2107cda41762e20d2b55c8f35459e4d7) | usrnk1 |
| 2026-11-16 | [fix(app): confirm before disconnecting providers or removing accounts…](https://github.com/anomalyco/opencode/commit/c5f18d1616fcef8c140479c389f39e3dbc9dde36) | arvsrn |
| 2026-11-16 | [fix(app): add missing translations (#64205)](https://github.com/anomalyco/opencode/commit/b083c4d510e4dec892231ccf4fdf5ef48f6caec2) | neriousy |
| 2026-11-16 | [fix(ui): cap large dialogs at 720px and extra-large dialogs at 880px …](https://github.com/anomalyco/opencode/commit/8bb7fab26e593d3fdb69226f667221e666c4d006) | usrnk1 |
| 2026-11-16 | [fix(desktop): keep drafts storage out of the CLI database (#64203)](https://github.com/anomalyco/opencode/commit/4c3e17b9d860e9e4fcccd8b45210126177f0aaf1) | neriousy |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
