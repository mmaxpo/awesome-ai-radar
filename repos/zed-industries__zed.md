# zed-industries/zed

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/zed-industries/zed)

> Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Fast code editor with AI agents built in |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 95.4k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 544.9 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · yesterday</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

### [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2)
<sub>2026-11-18 · yesterday</sub>

> - Added an official Snap package for Linux ([#67164](https://github.com/zed-industries/zed/pull/67164))

### [v1.29.1](https://github.com/zed-industries/zed/releases/tag/v1.29.1)
<sub>2026-11-18 · yesterday</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.30.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.0-pre) _(pre-release)_
<sub>2026-11-18 · yesterday</sub>

> This week's release includes reduced GPU usage across the app, a model picker for AI commit message generation in the Git Panel, a setting to hide the title bar, support for GPT-6.1 Terra, and faster scanning of large projects.
> **Features**
> **AI**
> - Added support for GPT-6.1 Terra to the OpenAI provider. ([#66659](https://github.com/zed-industries/zed/pull/66659); thanks [nymo](https://github.com/nymo))
> - Added keyboard navigation to the agent thread switcher (opened with `ctrl-tab` from the Agent Panel or Threads Sidebar): `up` / `down`, `ctrl-n` / `ctrl-p`, and `home` / `end` move the selection, as do `ctrl-up` / `ctrl-down` while `ctrl` is still held. ([#66951](https://github.com/zed-industries/zed/pull/66951); thanks [kinoute](https://github.com/kinoute))
> - Added support for the Extra High thinking effort level for Gemini 4 Hydrogen (`gemini-4-hydrogen`), which now defaults to High. ([#67011](https://github.com/zed-industries/zed/pull/67011); thanks [LorenzoBiassio](https://github.com/LorenzoBiassio))
> …

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 8d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Show external agent authentication status in the Agent Panel (#67243)](https://github.com/zed-industries/zed/commit/a65e743ad90acb184f86ec87b67bb82076105417) | benbrandt |
| 2026-11-20 | [Use Anthropic capability metadata and update model compatibility (#67…](https://github.com/zed-industries/zed/commit/ad1058d78d802f2fa857dee20aa2f5e123ef1ece) | bennetbo |
| 2026-11-20 | [worktree: Do less work while scan_dir holds the state lock (#67226)](https://github.com/zed-industries/zed/commit/87e6a02e1e4624a2ede355d457d513142af08cde) | ptweezy |
| 2026-11-20 | [Remove dead code and redundant checks in workspace, search, terminal,…](https://github.com/zed-industries/zed/commit/87da03ad3f7272f5258f3d1b7d638a3fc98ea555) | ptweezy |
| 2026-11-19 | [editor: Remove dead code and redundant checks (#67217)](https://github.com/zed-industries/zed/commit/7279c76ef71d45504d7cfea00ee054f852ca0fbf) | ptweezy |
| 2026-11-19 | [Remove dead code and redundant checks in agent and language model cra…](https://github.com/zed-industries/zed/commit/4e2c957a6d998e231eb2c09b45cbea35cf585a52) | ptweezy |
| 2026-11-19 | [Fix TypeScript and TSX type highlighting (#64462)](https://github.com/zed-industries/zed/commit/a246423a3b24a08e0d0c8574eab3a9de422747e0) | mchisolm0 |
| 2026-11-19 | [project: Remove dead code and redundant checks (#67200)](https://github.com/zed-industries/zed/commit/d5615304a1acd9573951aaf462bb46450b1b710b) | ptweezy |
| 2026-11-19 | [Remove dead code and no-op options from UI components (#67201)](https://github.com/zed-industries/zed/commit/5a0e9521f6e0b5c92285ea5fc851bcaecce1f885) | ptweezy |
| 2026-11-19 | [Remove dead code and stale lint suppressions in infrastructure crates…](https://github.com/zed-industries/zed/commit/925ee76e1ba1988bd7fd3f1c942f007fd439b6f2) | ptweezy |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
