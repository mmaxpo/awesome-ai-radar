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
| ⭐ **Stars** | 95.6k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 547.6 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.2-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.2-pre) _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67253](https://github.com/zed-industries/zed/pull/67253))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67188](https://github.com/zed-industries/zed/pull/67188))

### [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3)
<sub>2026-11-20 · 2d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67252](https://github.com/zed-industries/zed/pull/67252))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67189](https://github.com/zed-industries/zed/pull/67189))

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · 4d ago</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

### [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2)
<sub>2026-11-18 · 4d ago</sub>

> - Added an official Snap package for Linux ([#67164](https://github.com/zed-industries/zed/pull/67164))

### [v1.29.1](https://github.com/zed-industries/zed/releases/tag/v1.29.1)
<sub>2026-11-18 · 4d ago</sub>

> This week's release includes a Git Panel branch mode that lists every file changed since a base branch, a bookmark picker, configurable Git date formats, support for Claude Fable 5.2 for Anthropic BYOK users (plus Claude Mythos 5.2 if your organization has access), and a setting to turn off automatic agent thread titles.
> **Features**
> **AI**
> - Added an `agent.auto_generate_thread_titles` setting (default `true`) that can be set to `false` to disable automatic title generation for Zed Agent threads. ([#63998](https://github.com/zed-industries/zed/pull/63998); thanks [FrederickGeek8](https://github.com/FrederickGeek8))
> - Added support for Claude Fable 5.2 for Anthropic BYOK users, plus Claude Mythos 5.2 if your organization has access. ([#66760](https://github.com/zed-industries/zed/pull/66760))
> - Improved the copy button on agent responses to briefly show a checkmark confirming the copy. ([#64664](https://github.com/zed-industries/zed/pull/64664); thanks [itsfuad](https://github.com/itsfuad))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [rust: Adopt `trim_{prefix,suffix}` (#67367)](https://github.com/zed-industries/zed/commit/c31063a050c987da77bf48053132600b91d383b0) | tidely |
| 2026-11-23 | [anthropic: Support per-message reasoning effort (#67365)](https://github.com/zed-industries/zed/commit/10113795dffdde78b274c9455fc9c1f3234bf564) | bennetbo |
| 2026-11-23 | [Keep local settings of remote worktrees on project updates (#67269)](https://github.com/zed-industries/zed/commit/de3827f6e91a44c52c9655e319f74e0cbea6f6eb) | SomeoneToIgnore |
| 2026-11-23 | [Do not notify settings observers when removing a worktree without set…](https://github.com/zed-industries/zed/commit/42033befe68c1a73378a3fc15b8680715232090b) | SomeoneToIgnore |
| 2026-11-23 | [compliance: Explicity install default provider (#67360)](https://github.com/zed-industries/zed/commit/5dea5cab32286f8e19bd5e2894b974a36b3ed7d2) | MrSubidubi |
| 2026-11-23 | [ci: Use edge snapcraft version (#67308)](https://github.com/zed-industries/zed/commit/0ad670e6ea1f858b37a92c3c70f0487742d5cce5) | astrojuanlu |
| 2026-11-23 | [Bump Rust to version 1.100 (#67115)](https://github.com/zed-industries/zed/commit/3a5180211a79a6157bc774d966436c56d6c1781f) | tidely |
| 2026-11-23 | [gpui_wgpu: Fall back to textures on GL without shader storage (#67323)](https://github.com/zed-industries/zed/commit/f00a94318c059f03892e04f82343e899fbfaa844) | sundermann |
| 2026-11-23 | [sum_tree: Insert keyed items in place (#67332)](https://github.com/zed-industries/zed/commit/c671f77ffdb5c2ad20246c72c4251ac65342827e) | ptweezy |
| 2026-11-23 | [agent_servers: Retry ACP initialization with v1 after a v2 decode fai…](https://github.com/zed-industries/zed/commit/ac22c37e8619a5b48e1b0b60822c63534c974cd0) | benbrandt |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
