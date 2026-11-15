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
| ⭐ **Stars** | 227.0k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [4.0k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 12% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0) — 2026-11-13 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 713.6 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 2d ago</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

### [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — process-daemon v0.5.2
<sub>2026-11-11 · 3d ago</sub>

> opencode-pty 0.5.2 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.2.

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · 5d ago</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

### [v2.2.6](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)
<sub>2026-11-06 · 8d ago</sub>

> **Highlights**
> - **Shared MCP Connections**: Turn on pooling for an MCP server to share one connection across projects with the same setup, so you run fewer processes and start faster. ([#61185](https://github.com/anomalyco/opencode/pull/61185))
> - **GUI Plugin Themes and New Slots**: GUI plugins can now add color themes, render or add actions to code blocks, and use native settings and menu components. ([#61485](https://github.com/anomalyco/opencode/pull/61485), [#61533](https://github.com/anomalyco/opencode/pull/61533), [#61527](https://github.com/anomalyco/opencode/pull/61527), [#61509](https://github.com/anomalyco/opencode/pull/61509))
> - **Mobile Composer Dock**: On phones and tablets, composer actions now sit in a touch dock above the keyboard with larger buttons. ([#61773](https://github.com/anomalyco/opencode/pull/61773))
> - **Scripted Runs in Worktrees**: Run `opencode run -w` to start the session in a new git worktree, or `--worktree=<name>` to name it. ([#60712](https://github.com/anomalyco/opencode/pull/60712))
> - **Automatically Archived Runs**: Add `--archived` to `opencode run` to keep scripted and CI sessions out of your inbox and session lists. ([#61270](https://github.com/anomalyco/opencode/pull/61270))
> …

### [process-daemon-v0.5.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.0) — process-daemon v0.5.0
<sub>2026-11-05 · 9d ago</sub>

> opencode-pty 0.5.0 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.0.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [fix(core): preserve UTF-8 across shell output pages (#63984)](https://github.com/anomalyco/opencode/commit/d432a06b9c07bab0be4e8d642173b1cb14137f11) | rekram1-node |
| 2026-11-15 | [fix(app): never count subagents in the new timeline (#64017)](https://github.com/anomalyco/opencode/commit/0cfe2c2610ecbbdc9671464f1d4fb89563e1ff1a) | thdxr |
| 2026-11-14 | [fix: keep text cuts from splitting characters (#63967)](https://github.com/anomalyco/opencode/commit/38bd73789a43bf043599d6196af96583228035d7) | rekram1-node |
| 2026-11-14 | [fix(app): use consistent dialog sizes (#63432)](https://github.com/anomalyco/opencode/commit/46744b64692c5846ee5e21e1faefe91bba8a1597) | thdxr |
| 2026-11-14 | [fix(app): clarify hex tip copy (#63974)](https://github.com/anomalyco/opencode/commit/9f1639c73223053c7e5bc6f2204995fcd39b15ad) | thdxr |
| 2026-11-14 | [Revert "docs(go): remove Gemini 4 Argon from Go" (#63969)](https://github.com/anomalyco/opencode/commit/1fa50dd28cc860768fd89180cf40b2fb912b2813) | opencode-agent[bot] |
| 2026-11-14 | [docs(go): remove Gemini 4 Argon from Go (#63963)](https://github.com/anomalyco/opencode/commit/b4136f3902c918a9231710df299ca4fee5cd7ad5) | opencode-agent[bot] |
| 2026-11-14 | [fix(core): identify invalid filename globs in search tools (#63960)](https://github.com/anomalyco/opencode/commit/b659188ac8238bc1ef4f39cc41437aea0e250637) | rekram1-node |
| 2026-11-14 | [chore(perf): bench with strobe 0.42.0 (#63957)](https://github.com/anomalyco/opencode/commit/f61411af466a6566455a45f5a036c169e82d7c88) | Hona |
| 2026-11-14 | [perf(app): measure main-thread work to scroll history (#63923)](https://github.com/anomalyco/opencode/commit/d759c548aab33a7a6f5171cbeab40a59e91d90aa) | Hona |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
