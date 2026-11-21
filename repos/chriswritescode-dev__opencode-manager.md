# chriswritescode-dev/opencode-manager

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/chriswritescode-dev/opencode-manager)

> A self-hosted command center for OpenCode. Sessions, git, terminal, and schedules in one web app, from your phone or desktop. 

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | OpenCode sessions, git and terminal in one web app |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.1k |
| 🍴 **Forks** | 132 |
| 🐞 **Open issues + PRs** | [14](https://github.com/chriswritescode-dev/opencode-manager/issues) |
| 💻 **Languages** | TypeScript 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent` `web` `mobile` `ai-agents` `ai-coding` `coding-agent` `developer-tools` `docker` `llm` `opencode` `pwa` `react` `remote-development` `self-hosted` `terminal` |
| 🕒 **Last activity** | 2026-11-20 (yesterday) |
| 📅 **Created** | 2025-11-24 |
| 📦 **Latest release** | [v1.1.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.1.0) — 2026-10-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 38.9 MB |
| 🌐 **Website** | https://opencodemanager.app |

## 📦 Recent releases

### [v1.1.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.1.0) — OpenCode Manager v1.1.0
<sub>2026-10-26 · 26d ago</sub>

> **Highlights**
> - **Linked OpenCode servers**: pair any machine running `opencode serve` with `ocm link` and a QR code, then run sessions, terminals, schedules, multi-runs, goals and permission modes on it from Manager. Linked servers' projects appear on the home page.
> - **Repository secrets and variables**: GitHub Actions–style global, repository and environment secrets and variables, mapped through `.ocm/project.json` into agent shells, terminals, project actions and sandboxed shells, with secret values masked in tool output.
> - **QR device pairing**: Settings → Account → Connect a device signs in a phone or browser with a QR code, each with its own session.
> - **Sandboxed schedules**: a schedule can run each run in its own microVM, with optional CPU and memory limits.
> - **Voice conversation mode**: hands-free talk with the agent from the composer, with replies read aloud (now also on iOS).
> …

### [v1.0.1](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.0.1) — OpenCode Manager v1.0.1
<sub>2026-10-16 · 1mo ago</sub>

> **Highlights**
> - **Active work**: one place to see which sessions need input, are running, or finished recently, across every repository. It appears as an Activity tool on the desktop tool rail, as an Active tab in the session picker, and at the top of the mobile More drawer.
> - **Per-session sandboxing**: each sandboxed session runs its agent shell in its own microVM, which mounts only that session's repository or worktree. You can toggle it per session from the composer and set CPU and memory per session.
> - **Agent-built change walkthroughs**: a separate walkthrough agent session reads the diff and builds an interactive HTML walkthrough. You can stop it, refine it, or open its session.
> - **HTML artifacts**: an agent can write a self-contained HTML page and show it inline in the chat with the `ocm` tool's `show_artifact` action.
> - **Session picker tabs**: switch between Active, Sessions and Projects with `Ctrl+S`.
> …

### [v1.0.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.0.0) — OpenCode Manager v1.0.0
<sub>2026-10-09 · 1mo ago</sub>

> **Highlights**
> - **Desktop tool panel**: Files, Source Control, Terminal, Walkthrough, Preview, MCP, Skills, Actions and Schedules dock in a right-side panel on desktop. Mobile keeps its drawers.
> - **Change walkthroughs**: an agent explains a session's changes stop by stop. You can walk through the session, uncommitted, staged, unstaged, branch or pull request changes, and an agent can open the walkthrough itself.
> - **Multi-run fusion**: combine two to five completed multi-run results into one fused session, from a new runs sheet.
> - **App-wide keyboard shortcuts**, with import of your OpenCode TUI keybinds.
> - **Model selection that matches the TUI**: chat, schedules, agents, the goal auditor and the walkthrough all share the TUI's model preferences, favorites and recents.
> …

### [v0.21.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v0.21.0) — OpenCode Manager v0.21.0
<sub>2026-10-05 · 1mo ago</sub>

> **Highlights**
> - **One-line install** — `curl -fsSL https://opencodemanager.app/install | sh` sets up and starts OpenCode Manager with Docker. No clone and no `.env` required.
> - **Integrated terminal and project actions** — run shells, dev servers and watchers from the WebUI, including on mobile.
> - **Session automation** — per-session auto-accept, session goals that keep working until an objective is met, and multi-run across up to five models.
> - **Expanded source control** — worktrees from existing branches, merge or cherry-pick integration, stashes, conflict continue/abort, AI commit messages and git identities.
> - **Docs moved to [opencodemanager.app/docs](https://opencodemanager.app/docs)**.
> …

### [v0.20.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v0.20.0) — OpenCode Manager v0.20.0
<sub>2026-10-03 · 1mo ago</sub>

> **What's Changed**
> **Features**
> - **feat(themes): apply OpenCode color themes app-wide with a settings picker (#364)** — Vendors the 36 OpenCode theme palettes into the shared package (synced via `pnpm themes:sync`), adds a `colorTheme` preference, and applies the theme across messages, repos, sessions, settings, agent colors, git status, and diff viewers through a ThemeProvider. Adds a theme picker to General settings; model quick-select follows the active theme (fixes #355).
> - **feat(themes): drive code block syntax highlighting from active theme** — Code blocks now use the active theme's syntax colors.
> - **feat(files): fullscreen preview, relative markdown links, and preinstalled Chromium (#369)** — Desktop file preview gains a fullscreen toggle with a minimal close control. Relative and absolute markdown links resolve against the previewed file and open in the file browser, while external links open in a new tab. Playwright and Chromium are preinstalled in the Manager image so agents can run browser automation without a project-local install.
> - **feat(opencode-config): redact secrets and add MCP listing to the internal config API (#366)**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Merge pull request #490 from chriswritescode-dev/om-219-cold-catalog-…](https://github.com/chriswritescode-dev/opencode-manager/commit/750faf13614371b019770f1b630c99ff149ed97d) | chriswritescode-dev |
| 2026-11-19 | [Wait for plugins before using the OpenCode default model on cold loca…](https://github.com/chriswritescode-dev/opencode-manager/commit/afde60ddf7b15c8c61eaec6030a4c75b93612bc1) | chriswritescode-dev |
| 2026-11-19 | [Merge pull request #489 from chriswritescode-dev/fix/remote-schedule-…](https://github.com/chriswritescode-dev/opencode-manager/commit/3796ba15ebe166c17fd4ad6765f3fb4a7de2eaa4) | chriswritescode-dev |
| 2026-11-19 | [fix(schedules): accept absolute Windows directories for remote schedules](https://github.com/chriswritescode-dev/opencode-manager/commit/742660ecfa6b22dbd7d6efdbb615b76dd94288a8) | chriswritescode-dev |
| 2026-11-17 | [Merge pull request #488 from chriswritescode-dev/om-207-validate-goal…](https://github.com/chriswritescode-dev/opencode-manager/commit/5c5de012db81b59b51182a75ba9837a19d52bff1) | chriswritescode-dev |
| 2026-11-17 | [Fix the OpenCode 2.3.0 reload Goal assertion found validating cb4204d…](https://github.com/chriswritescode-dev/opencode-manager/commit/50d1958d43f18fa79579f187e819387f81707cfd) | chriswritescode-dev |
| 2026-11-17 | [Apply remaining changes](https://github.com/chriswritescode-dev/opencode-manager/commit/f737511ba31f74ab9a79438023afba361281783f) | chriswritescode-dev |
| 2026-11-17 | [Refresh Goal reads on plugin.updated, with recovery coverage](https://github.com/chriswritescode-dev/opencode-manager/commit/edd083e4178c8b50bc941f323041e447170017b4) | chriswritescode-dev |
| 2026-11-17 | [Version-aware real-binary proof of the cold-Location Goal](https://github.com/chriswritescode-dev/opencode-manager/commit/47066b33b282c0c2377c7ba5cf5c6269dbb2b741) | chriswritescode-dev |
| 2026-11-17 | [Move the OpenCode pin and supported floor to 2.3.0](https://github.com/chriswritescode-dev/opencode-manager/commit/23d9d1c945e2c080e3b2969407268e83cae8277d) | chriswritescode-dev |

[See all commits ↗](https://github.com/chriswritescode-dev/opencode-manager/commits)

## ⬇️ Get it

```bash
git clone https://github.com/chriswritescode-dev/opencode-manager.git
```
