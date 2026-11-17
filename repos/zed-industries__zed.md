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
| ⭐ **Stars** | 95.2k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 543.4 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 5d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.29.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.29.1-pre) _(pre-release)_
<sub>2026-11-11 · 5d ago</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.27.0](https://github.com/zed-industries/zed/releases/tag/v1.27.0)
<sub>2026-11-04 · 12d ago</sub>

> This week's release includes syntax highlighting for Go 1.27 generic methods, an option to open README files by default, and AI commit messages that follow your repository's recent commit style.
> **Features**
> **AI**
> - Improved Agent Panel memory usage by loading tool-call diffs and parsing thread message Markdown only when first viewed, instead of when loading a thread. ([#65444](https://github.com/zed-industries/zed/pull/65444), [#65470](https://github.com/zed-industries/zed/pull/65470); thanks [Vanuan](https://github.com/Vanuan))
> - Improved AI commit message generation by using the three most recent repository commit messages as style examples. ([#61528](https://github.com/zed-industries/zed/pull/61528); thanks [matheuslrd](https://github.com/matheuslrd))
> - Improved CPU usage and disk reads while the agent was working, especially with a long thread history. ([#66015](https://github.com/zed-industries/zed/pull/66015))
> …

### [v1.28.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.28.0-pre) _(pre-release)_
<sub>2026-11-04 · 12d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.26.2](https://github.com/zed-industries/zed/releases/tag/v1.26.2)
<sub>2026-10-28 · 19d ago</sub>

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
| 2026-11-17 | [google_ai: Add Extra High thinking level for Gemini 4 Hydrogen (#67011)](https://github.com/zed-industries/zed/commit/698368515d17a602dd51ea61297e5412ce06f52f) | LorenzoBiassio |
| 2026-11-17 | [onboarding: Keep header pinned while scrolling (#67079)](https://github.com/zed-industries/zed/commit/849b5b8e0737b7ec2ddbc96c26ba3c62a055f222) | aakashbapna |
| 2026-11-17 | [sandbox: New linux sandbox (#67062)](https://github.com/zed-industries/zed/commit/3dcdee6d2bbebc86ec2978919342a49ed9a0e11a) | cameron1024 |
| 2026-11-17 | [worktree: Only treat a directory as a bare repository when HEAD and c…](https://github.com/zed-industries/zed/commit/e5be9608ddd4cb0f2f179e1c0014f0a3a0337260) | likeaixxx |
| 2026-11-17 | [agent: Accept stringified line numbers in read_file tool (#67072)](https://github.com/zed-industries/zed/commit/6e7c5d3ae8578753601f192e72555948fd7a5e99) | ChromaxS |
| 2026-11-16 | [fix(git_graph): match log_source to CommitViewOptions reveal_file (#6…](https://github.com/zed-industries/zed/commit/482e76524bd33d8cbdfc352f1fef3eefbf2fad92) | jspwrd |
| 2026-11-16 | [agent_ui: Check only the clicked pattern in pipeline permission dropd…](https://github.com/zed-industries/zed/commit/4191aeaf50e8e255b07bdf2624d7fac17c12f695) | tredondo |
| 2026-11-16 | [Support Corgi builds on FHS Linux (#67055)](https://github.com/zed-industries/zed/commit/5709f329dc0d85b0e369d2973acb5efce6b8dea8) | kubkon |
| 2026-11-16 | [gpui_web: Drop Shift from symbol keystrokes (#67052)](https://github.com/zed-industries/zed/commit/9925feb84c0cf10a63f1641b8f9789c11fada4de) | kubkon |
| 2026-11-16 | [fs: Optimize filesystem watcher path matching by adding fast path for…](https://github.com/zed-industries/zed/commit/d833d4689d04183d1dfd1ad862dc80f6f044a41f) | RemcoSmitsDev |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
