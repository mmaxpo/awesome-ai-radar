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
| ⭐ **Stars** | 95.0k |
| 🍴 **Forks** | 11.7k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 541.1 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 2d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.29.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.29.1-pre) _(pre-release)_
<sub>2026-11-11 · 2d ago</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.27.0](https://github.com/zed-industries/zed/releases/tag/v1.27.0)
<sub>2026-11-04 · 10d ago</sub>

> This week's release includes syntax highlighting for Go 1.27 generic methods, an option to open README files by default, and AI commit messages that follow your repository's recent commit style.
> **Features**
> **AI**
> - Improved Agent Panel memory usage by loading tool-call diffs and parsing thread message Markdown only when first viewed, instead of when loading a thread. ([#65444](https://github.com/zed-industries/zed/pull/65444), [#65470](https://github.com/zed-industries/zed/pull/65470); thanks [Vanuan](https://github.com/Vanuan))
> - Improved AI commit message generation by using the three most recent repository commit messages as style examples. ([#61528](https://github.com/zed-industries/zed/pull/61528); thanks [matheuslrd](https://github.com/matheuslrd))
> - Improved CPU usage and disk reads while the agent was working, especially with a long thread history. ([#66015](https://github.com/zed-industries/zed/pull/66015))
> …

### [v1.28.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.28.0-pre) _(pre-release)_
<sub>2026-11-04 · 10d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.26.2](https://github.com/zed-industries/zed/releases/tag/v1.26.2)
<sub>2026-10-28 · 17d ago</sub>

> This week's release includes Pyrefly as an optional built-in Python language server, the ability to expand and inspect nested variable values directly in debugger hovers, and DWARF debugging for WebAssembly sources in the JavaScript debugger.
> **Features**
> **AI**
> - Improved ACP configuration defaults to apply only to new conversations, preserving session settings when reopening existing conversations. ([#65850](https://github.com/zed-industries/zed/pull/65850))
> - Improved fuzzy searching in agent model and configuration option pickers for Zed Agent and third-party ACP agents, while keeping search preparation off the UI thread. ([#64147](https://github.com/zed-industries/zed/pull/64147); thanks [JacobNWolf](https://github.com/JacobNWolf))
> - Improved OpenCode compatibility when replaying DeepSeek reasoning and disabling thinking for Google models. ([#65922](https://github.com/zed-industries/zed/pull/65922))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [language: Reset unused-code state when seeking buffer chunks (#66977)](https://github.com/zed-industries/zed/commit/56a157e5b01b62afd5c50a014ed15b379de8dfd6) | ptweezy |
| 2026-11-14 | [editor: Avoid cloning line text before shaping (#66978)](https://github.com/zed-industries/zed/commit/62cb1ac7b123ed6ec7be06f17b51f516583d2f8a) | ptweezy |
| 2026-11-14 | [editor: Build completion sort keys once per match (#66959)](https://github.com/zed-industries/zed/commit/4cc3e27d9d348736cc6e0cd1c32ed94416902e95) | ptweezy |
| 2026-11-14 | [fs: Optimize filesystem watcher path matching (#66973)](https://github.com/zed-industries/zed/commit/99c890d39d336052d9dae34c7914b55ee82abc5f) | RemcoSmitsDev |
| 2026-11-14 | [settings_content: Fix outdated defaults in setting doc comments (#66974)](https://github.com/zed-industries/zed/commit/2568d560f1b0ea21a6f3fc119ef8df36a0b75acb) | Toraastrta |
| 2026-11-14 | [Switch async-task back to upstream (#66968)](https://github.com/zed-industries/zed/commit/0cfc4a483dfab6ca171df0ceedaaa2a9f7954d0e) | benbrandt |
| 2026-11-14 | [worktree: Sort removed entry ids once (#66962)](https://github.com/zed-industries/zed/commit/0d3c40e1b9a6190696a25a580d755398e58cffa4) | ptweezy |
| 2026-11-14 | [proto: Split worktree updates in linear time (#66961)](https://github.com/zed-industries/zed/commit/f53c9ae3d6c7b4ab1577d296e6f03bd264f47458) | ptweezy |
| 2026-11-14 | [gpui: Match keystrokes before context predicates (#66634)](https://github.com/zed-industries/zed/commit/d0400aaf033a703a037f8fe5400bbc896db985da) | ptweezy |
| 2026-11-14 | [gpui: Fix unused import warning with bench-support (#66905)](https://github.com/zed-industries/zed/commit/f0fa51bb510fc91f6da7ec55f3e0f317f1f975ec) | jaw-sh |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
