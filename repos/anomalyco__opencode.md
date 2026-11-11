# anomalyco/opencode

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/anomalyco/opencode)

> The open source coding agent.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Project** | — |
| **Why I saved it** | — |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 226.0k |
| 🍴 **Forks** | 30.5k |
| 🐞 **Open issues + PRs** | [4.2k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 12% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7) — 2026-11-10 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 675.3 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.2.7](https://github.com/anomalyco/opencode/releases/tag/v2.2.7)
<sub>2026-11-10 · today</sub>

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
| 2026-11-11 | [feat(core): tell agents when they are in a fork (#63235)](https://github.com/anomalyco/opencode/commit/e56eff2bc01649b3aa21224876b8874e77dea4b0) | kommander |
| 2026-11-11 | [refactor(data): strict dev/production stages and data naming](https://github.com/anomalyco/opencode/commit/070b980c0b17487dcb94f381cc2eb03953dadb86) | thdxr |
| 2026-11-11 | [fix(core): send saved keys during local model discovery (#63266)](https://github.com/anomalyco/opencode/commit/f753100ad59bac0932060df6f8b2f132e9338d6e) | rekram1-node |
| 2026-11-11 | [feat(core): wake a session on MCP events with a watch tool (#63269)](https://github.com/anomalyco/opencode/commit/eb670f1e98aa11b9e4ec0b331232c5a420235e86) | rekram1-node |
| 2026-11-11 | [ci(deploy): mint short-lived cloudflare tokens from the token issuer](https://github.com/anomalyco/opencode/commit/39502786382a965ee98497c9557a0b7afe2e6f4c) | thdxr |
| 2026-11-11 | [feat(core): support MCP events in the MCP client (#63254)](https://github.com/anomalyco/opencode/commit/6b1db2759a1afac862c9c751ef82d7d7159f36cd) | rekram1-node |
| 2026-11-11 | [fix(codemode): return compact JSON results (#63258)](https://github.com/anomalyco/opencode/commit/1af61ee45c41713c47fd42e80ff775e5d060c06b) | rekram1-node |
| 2026-11-11 | [fix(ai): keep exhausted request rate limits retryable (#59816)](https://github.com/anomalyco/opencode/commit/1002a979f9eacea665e44a6a178e6593f375e888) | Kyle-j-bush |
| 2026-11-11 | [fix(site): keep the bare host as a custom domain](https://github.com/anomalyco/opencode/commit/791a2c489efd88c566df710a7e074ba7327236af) | thdxr |
| 2026-11-11 | [fix(core): refresh MCP OAuth tokens before they expire (#63028)](https://github.com/anomalyco/opencode/commit/4d49c73e026309d20d45e154cebd80cdbadfad6a) | rekram1-node |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## 👥 Top contributors

[thdxr](https://github.com/thdxr) (3051) · [opencode-agent[bot]](https://github.com/opencode-agent[bot]) (2712) · [rekram1-node](https://github.com/rekram1-node) (2696) · [kitlangton](https://github.com/kitlangton) (2441) · [adamdotdevin](https://github.com/adamdotdevin) (2183)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
