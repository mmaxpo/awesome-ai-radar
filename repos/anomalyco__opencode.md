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
| ⭐ **Stars** | 226.3k |
| 🍴 **Forks** | 30.6k |
| 🐞 **Open issues + PRs** | [4.3k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 12% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — 2026-11-11 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 702.7 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [process-daemon-v0.5.2](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.2) — process-daemon v0.5.2
<sub>2026-11-11 · today</sub>

> opencode-pty 0.5.2 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.2.

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · 2d ago</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

### [v2.2.6](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)
<sub>2026-11-06 · 5d ago</sub>

> **Highlights**
> - **Shared MCP Connections**: Turn on pooling for an MCP server to share one connection across projects with the same setup, so you run fewer processes and start faster. ([#61185](https://github.com/anomalyco/opencode/pull/61185))
> - **GUI Plugin Themes and New Slots**: GUI plugins can now add color themes, render or add actions to code blocks, and use native settings and menu components. ([#61485](https://github.com/anomalyco/opencode/pull/61485), [#61533](https://github.com/anomalyco/opencode/pull/61533), [#61527](https://github.com/anomalyco/opencode/pull/61527), [#61509](https://github.com/anomalyco/opencode/pull/61509))
> - **Mobile Composer Dock**: On phones and tablets, composer actions now sit in a touch dock above the keyboard with larger buttons. ([#61773](https://github.com/anomalyco/opencode/pull/61773))
> - **Scripted Runs in Worktrees**: Run `opencode run -w` to start the session in a new git worktree, or `--worktree=<name>` to name it. ([#60712](https://github.com/anomalyco/opencode/pull/60712))
> - **Automatically Archived Runs**: Add `--archived` to `opencode run` to keep scripted and CI sessions out of your inbox and session lists. ([#61270](https://github.com/anomalyco/opencode/pull/61270))
> …

### [process-daemon-v0.5.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.0) — process-daemon v0.5.0
<sub>2026-11-05 · 6d ago</sub>

> opencode-pty 0.5.0 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.0.

### [v2.2.5](https://github.com/anomalyco/opencode/releases/tag/v2.2.5)
<sub>2026-10-30 · 12d ago</sub>

> **Highlights**
> - **Worktree and Shell Mode Shortcuts**: Press `⌘⌥O` on macOS or `Ctrl+Alt+O` on Windows and Linux to choose a worktree, and `⌘⌥B` or `Ctrl+Alt+B` to choose its base branch. `⌘⇧X` or `Ctrl+Shift+X` now toggles shell mode in the composer. ([#60713](https://github.com/anomalyco/opencode/pull/60713))
> - **Send Quotes From the Comment Popup**: Hold `⌘` or `Ctrl` in the quote popup to turn its checkmark into send, or press `⌘Enter` or `Ctrl+Enter`, to send just that quote and comment while leaving the rest of the composer untouched. ([#60640](https://github.com/anomalyco/opencode/pull/60640))
> - **Percentage Compaction Buffer**: Set `"compaction": { "buffer": "20%" }` in `opencode.json` to keep a share of each model's context window free, so one setting fits models with small and large windows. Token counts still work. ([#60647](https://github.com/anomalyco/opencode/pull/60647))
> **Core**
> **Improvements**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [chore(perf): bench with strobe 0.31.0 (#63515)](https://github.com/anomalyco/opencode/commit/3d308eae2e68dc39dfc12aba9dd408f9ce1cc0a1) | Hona |
| 2026-11-12 | [fix(site): ship the link-card videos with the site's static assets (#…](https://github.com/anomalyco/opencode/commit/9d236eb0c8befba0b8c847ed7a8310d4bfd38f70) | adamdotdevin |
| 2026-11-12 | [fix(app): restore message footers in the New timeline (#63513)](https://github.com/anomalyco/opencode/commit/82e39cce289e3f0db9970ead8a8d68c37612305e) | arvsrn |
| 2026-11-12 | [fix(site): keep the page when leaving the Markdown view on static pag…](https://github.com/anomalyco/opencode/commit/d7ae4f2e3ccdbdbb1a7cb6be660713aae44a6713) | opencode-agent[bot] |
| 2026-11-12 | [fix(app): retry browser pane when server plugins finish loading (#63500)](https://github.com/anomalyco/opencode/commit/cbcd846a5718dea12e9e19ad58ea5b2142fd5686) | neriousy |
| 2026-11-12 | [chore(perf): bench with strobe 0.30.0 (#63497)](https://github.com/anomalyco/opencode/commit/df7911ab8b3602b585b6b308be54d4262000bae5) | Hona |
| 2026-11-12 | [fix(release): limit stable releases to named actors](https://github.com/anomalyco/opencode/commit/101776024cc69bafb3f9dc90027ab4d1eab40a2a) | thdxr |
| 2026-11-12 | [feat(core): publish MCP events on the bus (#63261)](https://github.com/anomalyco/opencode/commit/2c1e17b58173f3a14c927b427d3778a2fadb2f31) | rekram1-node |
| 2026-11-12 | [chore(perf): bench with strobe 0.29.0 (#63441)](https://github.com/anomalyco/opencode/commit/4f51455a5da7859e4f1a1b6abcc54b67bf7b7a4b) | Hona |
| 2026-11-12 | [fix(ai): accept System One refusals and send PDFs in the OpenRouter s…](https://github.com/anomalyco/opencode/commit/647e5a7b18c593e8c22e11fb5ba27317817b358a) | rekram1-node |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
