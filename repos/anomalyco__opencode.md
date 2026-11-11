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
| ⭐ **Stars** | 226.1k |
| 🍴 **Forks** | 30.6k |
| 🐞 **Open issues + PRs** | [4.3k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 12% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7) — 2026-11-10 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 675.4 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · yesterday</sub>

> **Highlights**
> - **GitHub Copilot Auto**: Pick **Auto** in the model picker when your Copilot account has an Auto pool, and Copilot's router chooses the model for each session at the Auto discount. If routing fails, OpenCode falls back to the account's default chat model. ([#62997](https://github.com/anomalyco/opencode/pull/62997))
> - **Side Panel Tab Shortcuts**: Right-click a side panel tab and choose **Close tabs to the right**. `⌘W` now closes side panel tabs wherever focus is, `⌥⌘W` or `Ctrl+Alt+W` always closes the session tab, and `⌘⇧T` reopens the last closed tab of either kind where it was. ([#62922](https://github.com/anomalyco/opencode/pull/62922))
> - **Mark Sessions Read or Unread**: Open the menu on a tab, Home row, project row or inbox card and choose **Mark as unread** to keep its dot until you next visit. ([#62889](https://github.com/anomalyco/opencode/pull/62889))
> **Breaking changes**
> **`@opencode/ai`: `ImageResponse.image` is removed**
> …

### [v2.2.6](https://github.com/anomalyco/opencode/releases/tag/v2.2.6)
<sub>2026-11-06 · 4d ago</sub>

> **Highlights**
> - **Shared MCP Connections**: Turn on pooling for an MCP server to share one connection across projects with the same setup, so you run fewer processes and start faster. ([#61185](https://github.com/anomalyco/opencode/pull/61185))
> - **GUI Plugin Themes and New Slots**: GUI plugins can now add color themes, render or add actions to code blocks, and use native settings and menu components. ([#61485](https://github.com/anomalyco/opencode/pull/61485), [#61533](https://github.com/anomalyco/opencode/pull/61533), [#61527](https://github.com/anomalyco/opencode/pull/61527), [#61509](https://github.com/anomalyco/opencode/pull/61509))
> - **Mobile Composer Dock**: On phones and tablets, composer actions now sit in a touch dock above the keyboard with larger buttons. ([#61773](https://github.com/anomalyco/opencode/pull/61773))
> - **Scripted Runs in Worktrees**: Run `opencode run -w` to start the session in a new git worktree, or `--worktree=<name>` to name it. ([#60712](https://github.com/anomalyco/opencode/pull/60712))
> - **Automatically Archived Runs**: Add `--archived` to `opencode run` to keep scripted and CI sessions out of your inbox and session lists. ([#61270](https://github.com/anomalyco/opencode/pull/61270))
> …

### [process-daemon-v0.5.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.5.0) — process-daemon v0.5.0
<sub>2026-11-05 · 5d ago</sub>

> opencode-pty 0.5.0 (protocol 8) from packages/process-daemon, published to npm as @opencode/pty@0.5.0.

### [v2.2.5](https://github.com/anomalyco/opencode/releases/tag/v2.2.5)
<sub>2026-10-30 · 11d ago</sub>

> **Highlights**
> - **Worktree and Shell Mode Shortcuts**: Press `⌘⌥O` on macOS or `Ctrl+Alt+O` on Windows and Linux to choose a worktree, and `⌘⌥B` or `Ctrl+Alt+B` to choose its base branch. `⌘⇧X` or `Ctrl+Shift+X` now toggles shell mode in the composer. ([#60713](https://github.com/anomalyco/opencode/pull/60713))
> - **Send Quotes From the Comment Popup**: Hold `⌘` or `Ctrl` in the quote popup to turn its checkmark into send, or press `⌘Enter` or `Ctrl+Enter`, to send just that quote and comment while leaving the rest of the composer untouched. ([#60640](https://github.com/anomalyco/opencode/pull/60640))
> - **Percentage Compaction Buffer**: Set `"compaction": { "buffer": "20%" }` in `opencode.json` to keep a share of each model's context window free, so one setting fits models with small and large windows. Token counts still work. ([#60647](https://github.com/anomalyco/opencode/pull/60647))
> **Core**
> **Improvements**
> …

### [v2.2.4](https://github.com/anomalyco/opencode/releases/tag/v2.2.4)
<sub>2026-10-30 · 11d ago</sub>

> **Highlights**
> - **Persistent Desktop Terminals**: Desktop terminals now belong to the session, survive server restarts with their scrollback, and stay synchronized with the TUI and other windows. Renamed terminals also keep their names across restarts. ([#60346](https://github.com/anomalyco/opencode/pull/60346))
> - **Publish Interactive Artifacts**: Enable `"experimental": { "artifacts": true }` in `opencode.json` to let agents publish, update, and serve HTML or static artifacts through the built-in local provider or plugin-provided storage. ([#60351](https://github.com/anomalyco/opencode/pull/60351))
> - **Guided Claude Agent Setup**: Select **Claude Agent** from the provider picker to copy `claude auth login`, install Claude Code, and verify the connection before continuing to model selection. ([#60603](https://github.com/anomalyco/opencode/pull/60603))
> - **Choose a Base Branch Quickly**: While creating a worktree, open **Choose base branch** with `⌘⌥.` on macOS or `Ctrl+Alt+.` on Windows and Linux. The command is also available in the command palette and Settings › Shortcuts. ([#60579](https://github.com/anomalyco/opencode/pull/60579))
> **Core**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [chore(protocol): refresh generated openapi for the first-token event …](https://github.com/anomalyco/opencode/commit/aa08bb2e347e694c12293e232f0f07cb7f99c1cf) | thdxr |
| 2026-11-11 | [fix(session): measure tps from the first streamed token (#63321)](https://github.com/anomalyco/opencode/commit/99f2bea6dfd77bda4bdc8150cca71cb93ee32194) | thdxr |
| 2026-11-11 | [fix(app): accept a pasted redirect URL for provider sign-in (#63315)](https://github.com/anomalyco/opencode/commit/2ef38b2172d646c2813aee56192e7f17dd97922a) | neriousy |
| 2026-11-11 | [fix(tui): give plugins a live theme view (#63306)](https://github.com/anomalyco/opencode/commit/7b65261fcd8f75336f64e4d4f3f30127925a4893) | sidevesh |
| 2026-11-11 | [feat(app): limit Recent sidebar to 7 days and 30 rows, align its hove…](https://github.com/anomalyco/opencode/commit/e376ba0e0d0d237a70eeeecc8ac150b6837169c8) | jlongster |
| 2026-11-11 | [fix(app): snap vertical tab preview to its tab (#63074)](https://github.com/anomalyco/opencode/commit/96579e88acb79c8a9a04729dbe4138098bb97f6e) | arvsrn |
| 2026-11-11 | [feat(app): add the New timeline experiment (#63295)](https://github.com/anomalyco/opencode/commit/9e3290ab6ce24f1abfcb957a81748be48d2d5dc1) | arvsrn |
| 2026-11-11 | [fix(site): show download and install menus again after closing them (…](https://github.com/anomalyco/opencode/commit/d093e7a73cbe490c422b955f92afec9cd630279d) | thdxr |
| 2026-11-11 | [fix(ci): treat require-digests=false as off in verify-artifacts](https://github.com/anomalyco/opencode/commit/611cee9d4b667b459f19ca0cbf6e76d8647535fb) | thdxr |
| 2026-11-11 | [fix(core): fetch Console instructions and skills only when the config…](https://github.com/anomalyco/opencode/commit/d4ea024c4cfe4cf5ba972e48f28f41a017c7532f) | adamdotdevin |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
