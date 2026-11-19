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
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 544.8 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · today</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

### [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2)
<sub>2026-11-18 · today</sub>

> - Added an official Snap package for Linux ([#67164](https://github.com/zed-industries/zed/pull/67164))

### [v1.29.1](https://github.com/zed-industries/zed/releases/tag/v1.29.1)
<sub>2026-11-18 · today</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

### [v1.30.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.0-pre) _(pre-release)_
<sub>2026-11-18 · today</sub>

> This week's release includes reduced GPU usage across the app, a model picker for AI commit message generation in the Git Panel, a setting to hide the title bar, support for GPT-6.1 Terra, and faster scanning of large projects.
> **Features**
> **AI**
> - Added support for GPT-6.1 Terra to the OpenAI provider. ([#66659](https://github.com/zed-industries/zed/pull/66659); thanks [nymo](https://github.com/nymo))
> - Added keyboard navigation to the agent thread switcher (opened with `ctrl-tab` from the Agent Panel or Threads Sidebar): `up` / `down`, `ctrl-n` / `ctrl-p`, and `home` / `end` move the selection, as do `ctrl-up` / `ctrl-down` while `ctrl` is still held. ([#66951](https://github.com/zed-industries/zed/pull/66951); thanks [kinoute](https://github.com/kinoute))
> - Added support for the Extra High thinking effort level for Gemini 4 Hydrogen (`gemini-4-hydrogen`), which now defaults to High. ([#67011](https://github.com/zed-industries/zed/pull/67011); thanks [LorenzoBiassio](https://github.com/LorenzoBiassio))
> …

### [v1.28.1](https://github.com/zed-industries/zed/releases/tag/v1.28.1)
<sub>2026-11-11 · 7d ago</sub>

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
| 2026-11-19 | [agent_ui: Organize ACP config options in the agent composer (#67190)](https://github.com/zed-industries/zed/commit/df1ba676f214cb9fdc19bef6cc024a47dc77c4f7) | benbrandt |
| 2026-11-19 | [sandbox_linux: Remove timeout (#67186)](https://github.com/zed-industries/zed/commit/4a7d10473a3ed32c10026e549381f064dd020114) | cameron1024 |
| 2026-11-19 | [Remove dead code and redundant checks in edit prediction (#67150)](https://github.com/zed-industries/zed/commit/886dab4069106e0f7a0a2c78f921f6a64d3fcd76) | ptweezy |
| 2026-11-19 | [Remove dead code and redundant checks in language and text crates (#6…](https://github.com/zed-industries/zed/commit/36acea54c5d61ace6a9318f8244d66790f9a7872) | ptweezy |
| 2026-11-19 | [Remove dead code and redundant checks in git, debugger, and panel UIs…](https://github.com/zed-industries/zed/commit/0c5af8c5634df7069a7b51794920e80128bf1081) | ptweezy |
| 2026-11-19 | [search: Ensure text finder clears on no results (#67147)](https://github.com/zed-industries/zed/commit/b51ffab0153f3372b71d1bd565d48d5203fefe6a) | dinocosta |
| 2026-11-19 | [Fix private value redaction in remote projects (#66525)](https://github.com/zed-industries/zed/commit/740e018b70dcf9035ab3c1983cd0fc1105a73cb4) | sigkillme0 |
| 2026-11-19 | [google_ai: Add Extra High thinking level for Gemini 4 Neon (#67173)](https://github.com/zed-industries/zed/commit/4e161e70b5c02b0f63a50beb6937f9cd249c1678) | LorenzoBiassio |
| 2026-11-19 | [Bump tree-sitter to cf5d3a63 (#67174)](https://github.com/zed-industries/zed/commit/4a4c8150f03ef3c5e0c4f837dc0263c137f5b0ce) | reflectronic |
| 2026-11-19 | [gpui: Normalize clipboard line endings on Windows (#66945)](https://github.com/zed-industries/zed/commit/2eff23878ef4b91c558cd8ae72498ac8838d27d9) | reflectronic |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
