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
| 🍴 **Forks** | 131 |
| 🐞 **Open issues + PRs** | [17](https://github.com/chriswritescode-dev/opencode-manager/issues) |
| 💻 **Languages** | TypeScript 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent` `web` `mobile` `ai-agents` `ai-coding` `coding-agent` `developer-tools` `docker` `llm` `opencode` `pwa` `react` `remote-development` `self-hosted` `terminal` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2025-11-24 |
| 📦 **Latest release** | [v1.1.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.1.0) — 2026-10-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 38.5 MB |
| 🌐 **Website** | https://opencodemanager.app |

## 📦 Recent releases

### [v1.1.0](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.1.0) — OpenCode Manager v1.1.0
<sub>2026-10-26 · 19d ago</sub>

> **Highlights**
> - **Linked OpenCode servers**: pair any machine running `opencode serve` with `ocm link` and a QR code, then run sessions, terminals, schedules, multi-runs, goals and permission modes on it from Manager. Linked servers' projects appear on the home page.
> - **Repository secrets and variables**: GitHub Actions–style global, repository and environment secrets and variables, mapped through `.ocm/project.json` into agent shells, terminals, project actions and sandboxed shells, with secret values masked in tool output.
> - **QR device pairing**: Settings → Account → Connect a device signs in a phone or browser with a QR code, each with its own session.
> - **Sandboxed schedules**: a schedule can run each run in its own microVM, with optional CPU and memory limits.
> - **Voice conversation mode**: hands-free talk with the agent from the composer, with replies read aloud (now also on iOS).
> …

### [v1.0.1](https://github.com/chriswritescode-dev/opencode-manager/releases/tag/v1.0.1) — OpenCode Manager v1.0.1
<sub>2026-10-16 · 28d ago</sub>

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
| 2026-11-13 | [Merge pull request #485 from chriswritescode-dev/chore/prune-redundan…](https://github.com/chriswritescode-dev/opencode-manager/commit/eba86dc3fc3c95de448ee0c24d462194679b1ea6) | chriswritescode-dev |
| 2026-11-13 | [Remove duplicated and constant-only tests](https://github.com/chriswritescode-dev/opencode-manager/commit/71bde0378af2ce1bc115a0a7b39e58d8e8288fa2) | chriswritescode-dev |
| 2026-11-13 | [Merge pull request #484 from chriswritescode-dev/chore/oxlint-anti-slop](https://github.com/chriswritescode-dev/opencode-manager/commit/ee4ef8217db2a991dd2f494d1a455c798c1acca8) | chriswritescode-dev |
| 2026-11-13 | [Remove the unreachable agent and command rename plumbing](https://github.com/chriswritescode-dev/opencode-manager/commit/d153bc0d21fbb0329b63b38aa6c16168473ff489) | chriswritescode-dev |
| 2026-11-13 | [Scope goal reads to the session directory and stabilize the backgroun…](https://github.com/chriswritescode-dev/opencode-manager/commit/80e013ec81ce13443e0a78cce9823dbe0c77cc0d) | chriswritescode-dev |
| 2026-11-13 | [Fix remote session delete, unknown commit responses, restart errors a…](https://github.com/chriswritescode-dev/opencode-manager/commit/fc00273645d6f52801728ed088b1b6ba40729500) | chriswritescode-dev |
| 2026-11-13 | [Assert the event stream exists in the deferred bootstrap test](https://github.com/chriswritescode-dev/opencode-manager/commit/51fb4fd12ff395007e1f3a14b9e0916d44ef977d) | chriswritescode-dev |
| 2026-11-13 | [Isolate test state and inject the restart-pending check into config r…](https://github.com/chriswritescode-dev/opencode-manager/commit/76ca65ec5e90e87da7649d0681315b737eea9200) | chriswritescode-dev |
| 2026-11-13 | [fix: apply 1 pr-agent suggestions](https://github.com/chriswritescode-dev/opencode-manager/commit/26fd21250a3197412775dcb0812f835d60a17a10) | lil-worker-cstech[bot] |
| 2026-11-13 | [refactor: satisfy no-array-filter-map and no-accumulating-spread](https://github.com/chriswritescode-dev/opencode-manager/commit/19ee1d917382137ea6c65c075022c93d971d2f14) | chriswritescode-dev |

[See all commits ↗](https://github.com/chriswritescode-dev/opencode-manager/commits)

## ⬇️ Get it

```bash
git clone https://github.com/chriswritescode-dev/opencode-manager.git
```
