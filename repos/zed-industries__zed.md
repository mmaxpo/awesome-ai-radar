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
| ⭐ **Stars** | 95.3k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 543.5 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 6d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.29.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.29.1-pre) _(pre-release)_
<sub>2026-11-11 · 6d ago</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.27.0](https://github.com/zed-industries/zed/releases/tag/v1.27.0)
<sub>2026-11-04 · 13d ago</sub>

> This week's release includes syntax highlighting for Go 1.27 generic methods, an option to open README files by default, and AI commit messages that follow your repository's recent commit style.
> **Features**
> **AI**
> - Improved Agent Panel memory usage by loading tool-call diffs and parsing thread message Markdown only when first viewed, instead of when loading a thread. ([#65444](https://github.com/zed-industries/zed/pull/65444), [#65470](https://github.com/zed-industries/zed/pull/65470); thanks [Vanuan](https://github.com/Vanuan))
> - Improved AI commit message generation by using the three most recent repository commit messages as style examples. ([#61528](https://github.com/zed-industries/zed/pull/61528); thanks [matheuslrd](https://github.com/matheuslrd))
> - Improved CPU usage and disk reads while the agent was working, especially with a long thread history. ([#66015](https://github.com/zed-industries/zed/pull/66015))
> …

### [v1.28.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.28.0-pre) _(pre-release)_
<sub>2026-11-04 · 13d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.26.2](https://github.com/zed-industries/zed/releases/tag/v1.26.2)
<sub>2026-10-28 · 20d ago</sub>

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
| 2026-11-18 | [git_ui: Add commit message model picker (#50674)](https://github.com/zed-industries/zed/commit/1043f4a86ab911a381d9bfe45cf6b36d3cdcc89a) | soilSpoon |
| 2026-11-18 | [agent_ui: Open tool call locations for files that are not text (#67092)](https://github.com/zed-industries/zed/commit/f88e54eed5474cab7504835e60b0c0d7d6e39485) | daejey |
| 2026-11-18 | [Add typed support for the OpenAI Ultrafast service tier (#67143)](https://github.com/zed-industries/zed/commit/f3626706fa6855274a561f8f4aebf40666051596) | bennetbo |
| 2026-11-18 | [editor: Fix crash after moving a project with a split diff to a new w…](https://github.com/zed-industries/zed/commit/da294762d69eafce1a35d224d2990c4ddf5f9abb) | Stiven-Gjekaj |
| 2026-11-18 | [docs: Mention system clipboard register in Helix's core differences (…](https://github.com/zed-industries/zed/commit/e944cfa2fe622a7a15041b9dfc7770933792857c) | dinocosta |
| 2026-11-18 | [git_ui: Fold buffers in commit view as soon as possible (#67111)](https://github.com/zed-industries/zed/commit/38f5c4af0d6bace9bbc010528452f69bdbee4179) | dinocosta |
| 2026-11-18 | [project: Retry diffs since a commit after a failed load (#67116)](https://github.com/zed-industries/zed/commit/761786a4ef7144de734e48cb2e8f99bc46b5061e) | ptweezy |
| 2026-11-18 | [settings: Make `SettingsFile::Global` compare equal to itself (#67121)](https://github.com/zed-industries/zed/commit/f070c7ff6c27d8bcec4ac14014cd2190a8b98eb0) | ptweezy |
| 2026-11-18 | [Remove dead code in client, call, channel, and collab (#67126)](https://github.com/zed-industries/zed/commit/881c618a6a990fbf6adeed42d1d52f028e3d32b8) | ptweezy |
| 2026-11-18 | [edit_prediction_cli: Fix total token percentiles (#67124)](https://github.com/zed-industries/zed/commit/1ab8b9abfb035a16afc6ba50f20b1191d1f80c73) | ptweezy |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
