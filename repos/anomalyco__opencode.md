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
| ⭐ **Stars** | 226.6k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [4.0k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 12% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) — 2026-11-13 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 706.9 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · today</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

### [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — process-daemon v0.5.2
<sub>2026-11-11 · yesterday</sub>

> opencode-pty 0.5.2 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.2.

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · 3d ago</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

### [v2.2.6](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)
<sub>2026-11-06 · 6d ago</sub>

> **Highlights**
> - **Shared MCP Connections**: Turn on pooling for an MCP server to share one connection across projects with the same setup, so you run fewer processes and start faster. ([#61185](https://github.com/anomalyco/opencode/pull/61185))
> - **GUI Plugin Themes and New Slots**: GUI plugins can now add color themes, render or add actions to code blocks, and use native settings and menu components. ([#61485](https://github.com/anomalyco/opencode/pull/61485), [#61533](https://github.com/anomalyco/opencode/pull/61533), [#61527](https://github.com/anomalyco/opencode/pull/61527), [#61509](https://github.com/anomalyco/opencode/pull/61509))
> - **Mobile Composer Dock**: On phones and tablets, composer actions now sit in a touch dock above the keyboard with larger buttons. ([#61773](https://github.com/anomalyco/opencode/pull/61773))
> - **Scripted Runs in Worktrees**: Run `opencode run -w` to start the session in a new git worktree, or `--worktree=<name>` to name it. ([#60712](https://github.com/anomalyco/opencode/pull/60712))
> - **Automatically Archived Runs**: Add `--archived` to `opencode run` to keep scripted and CI sessions out of your inbox and session lists. ([#61270](https://github.com/anomalyco/opencode/pull/61270))
> …

### [process-daemon-v0.5.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.0) — process-daemon v0.5.0
<sub>2026-11-05 · 7d ago</sub>

> opencode-pty 0.5.0 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.0.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [feat(app): wait an hour after first launch before the first tip (#63760)](https://github.com/anomalyco/opencode/commit/152115dea57bcdccfd31d50500a148ca4e0faf8b) | thdxr |
| 2026-11-13 | [fix(tui): drop ttft from the assistant footer (#63759)](https://github.com/anomalyco/opencode/commit/507c939f4115d4225122d6b82ba9899c000ecd11) | thdxr |
| 2026-11-13 | [fix(app): tidy New timeline questions, moves, compaction and shells (…](https://github.com/anomalyco/opencode/commit/191a69ad45ef0ca4925d8b7683eacdca0e8224e0) | arvsrn |
| 2026-11-13 | [fix(ui): switch submenus without blinking and keep them open on the w…](https://github.com/anomalyco/opencode/commit/f352f5e87594051784c03963130cdb1a09e50234) | neriousy |
| 2026-11-13 | [fix(session-ui): keep message meta lines visible in the New timeline …](https://github.com/anomalyco/opencode/commit/5b131f5995a9f7fad458c59a7a5e39686237beb8) | arvsrn |
| 2026-11-13 | [fix(app): hide zero session cost for OpenCode Go (#63744)](https://github.com/anomalyco/opencode/commit/46aefe3da30553099a8b8434d65aff1029a03235) | usrnk1 |
| 2026-11-13 | [feat(session-ui): make session stories configurable and preview file …](https://github.com/anomalyco/opencode/commit/a660c18c08ed1907e4ef3b197d82e3d354c50d10) | usrnk1 |
| 2026-11-13 | [feat(ui): expand interactive stories and compare icon artwork (#63735)](https://github.com/anomalyco/opencode/commit/71d63d46171b8b0d24ab3b5ebc22cb9c762b23c5) | usrnk1 |
| 2026-11-13 | [test(gui-plugins): add interactive workspace, browser, and pairing st…](https://github.com/anomalyco/opencode/commit/b3f806c2f6b35a7712f4d7b6b508d585787bcb40) | usrnk1 |
| 2026-11-13 | [feat(stories): browse app states in the standalone components lab (#6…](https://github.com/anomalyco/opencode/commit/a5170d6e019341864d948189d1420096005de8e0) | usrnk1 |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
