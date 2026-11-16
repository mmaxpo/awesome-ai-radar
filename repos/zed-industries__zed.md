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
| ⭐ **Stars** | 95.1k |
| 🍴 **Forks** | 11.7k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 543.3 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 4d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.29.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.29.1-pre) _(pre-release)_
<sub>2026-11-11 · 4d ago</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.27.0](https://github.com/zed-industries/zed/releases/tag/v1.27.0)
<sub>2026-11-04 · 11d ago</sub>

> This week's release includes syntax highlighting for Go 1.27 generic methods, an option to open README files by default, and AI commit messages that follow your repository's recent commit style.
> **Features**
> **AI**
> - Improved Agent Panel memory usage by loading tool-call diffs and parsing thread message Markdown only when first viewed, instead of when loading a thread. ([#65444](https://github.com/zed-industries/zed/pull/65444), [#65470](https://github.com/zed-industries/zed/pull/65470); thanks [Vanuan](https://github.com/Vanuan))
> - Improved AI commit message generation by using the three most recent repository commit messages as style examples. ([#61528](https://github.com/zed-industries/zed/pull/61528); thanks [matheuslrd](https://github.com/matheuslrd))
> - Improved CPU usage and disk reads while the agent was working, especially with a long thread history. ([#66015](https://github.com/zed-industries/zed/pull/66015))
> …

### [v1.28.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.28.0-pre) _(pre-release)_
<sub>2026-11-04 · 11d ago</sub>

> This week's release includes optional automatic Git fetching, a resizable Refs column in the Git Graph, dragging Git Panel files into terminals and editors, and mouse-wheel font zoom in diff views and terminals.
> **Features**
> **AI**
> - Added an `edit_predictions.button` setting to toggle the edit prediction button in the status bar. ([#66450](https://github.com/zed-industries/zed/pull/66450); thanks [z0al](https://github.com/z0al))
> - Improved compatibility with the latest Agent Client Protocol, including handling of missing sessions, plan updates, diff formats, and cancellation of permission requests. ([#66425](https://github.com/zed-industries/zed/pull/66425))
> - Improved the Agent's `read_file` tool output by truncating lines longer than 2,000 characters to prevent context window overflow. ([#65395](https://github.com/zed-industries/zed/pull/65395); thanks [Antphar](https://github.com/Antphar))
> …

### [v1.26.2](https://github.com/zed-industries/zed/releases/tag/v1.26.2)
<sub>2026-10-28 · 18d ago</sub>

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
| 2026-11-16 | [agent_ui: Keep focus when background threads auto-send queued message…](https://github.com/zed-industries/zed/commit/d39178f6c9e6adeb68e7a0df0b2a5b7d7bd35877) | daejey |
| 2026-11-16 | [Preserve mid-conversation system prompt updates (#66490)](https://github.com/zed-industries/zed/commit/89d3da65789d8728d01a82d284924334418065f7) | bennetbo |
| 2026-11-16 | [Highlight high-merge-rate authors on the community PRs board (#67038)](https://github.com/zed-industries/zed/commit/99dd426cba792530d1b79ee0c4241c9076e7045f) | zelenenka |
| 2026-11-16 | [Fix duplicate language server notifications (#67021)](https://github.com/zed-industries/zed/commit/430a781076180308af99fdd94f3ffabc8bccec90) | xsadia |
| 2026-11-16 | [agent: Prompt for `always_confirm` patterns on in-project file edits …](https://github.com/zed-industries/zed/commit/12c1fc907f8f55971ecc61bd3905549f4d043f89) | benbrandt |
| 2026-11-16 | [fs: Reduce time spend for hashing WatchKey in `watcher_ids_covering` …](https://github.com/zed-industries/zed/commit/6c7508a133cba5c93fb182e9d9efdfb392abf68d) | RemcoSmitsDev |
| 2026-11-16 | [Unifying agent instructions to AGENTS.md (#66716)](https://github.com/zed-industries/zed/commit/a57e2fdc389a3e513a6d5f5a7564ebe2fd33fc88) | Sha1rholder |
| 2026-11-16 | [agent_ui: Check for an empty message without copying the text (#67020)](https://github.com/zed-industries/zed/commit/053d91cb14b5fd138f221ec02bd76efb15e7b2af) | ptweezy |
| 2026-11-16 | [util: Avoid allocating when sorting paths by extension (#67019)](https://github.com/zed-industries/zed/commit/125ca8672e928b19a62c2e4b761fb29fe2a34ae3) | ptweezy |
| 2026-11-16 | [util: Return early from natural_sort for equal strings (#67016)](https://github.com/zed-industries/zed/commit/310bba2f2f88d2bb9f2369039bdb6bf89426da1b) | ptweezy |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
