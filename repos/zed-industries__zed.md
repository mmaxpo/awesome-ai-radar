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
| ⭐ **Stars** | 95.5k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 545.8 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.2-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.2-pre) _(pre-release)_
<sub>2026-11-20 · today</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67253](https://github.com/zed-industries/zed/pull/67253))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67188](https://github.com/zed-industries/zed/pull/67188))

### [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3)
<sub>2026-11-20 · today</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67252](https://github.com/zed-industries/zed/pull/67252))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67189](https://github.com/zed-industries/zed/pull/67189))

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · 2d ago</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

### [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2)
<sub>2026-11-18 · 2d ago</sub>

> - Added an official Snap package for Linux ([#67164](https://github.com/zed-industries/zed/pull/67164))

### [v1.29.1](https://github.com/zed-industries/zed/releases/tag/v1.29.1)
<sub>2026-11-18 · 2d ago</sub>

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
| 2026-11-21 | [text: Resolve min and max anchors without walking the rope (#67280)](https://github.com/zed-industries/zed/commit/2f808b3c2de049ecfdbad0fdb26763cebfcaa3b4) | ptweezy |
| 2026-11-21 | [terminal_view: Memoize the minimum contrast check per color pair (#67…](https://github.com/zed-industries/zed/commit/167f53b58f005516b3904fe6a75013d8658d5d03) | ptweezy |
| 2026-11-20 | [Wire up crates.io client in GPUI publishing xtask (#67278)](https://github.com/zed-industries/zed/commit/4f5e323e25e4eaf141483c011ba159ea54063b77) | MrSubidubi |
| 2026-11-20 | [Unify git merge URL, both for command and output toast action (#66408)](https://github.com/zed-industries/zed/commit/852edce6f804961f6f6176be3a62665b9df00504) | HannesGitH |
| 2026-11-20 | [component: Remove no-op grow and vertical options (#67220)](https://github.com/zed-industries/zed/commit/54fff2ff5b2f9fdbe1b99c0c2566e15dcb6cfcb9) | ptweezy |
| 2026-11-20 | [Bump bundled macOS git to 2.56.1 and verify its checksum (#67264)](https://github.com/zed-industries/zed/commit/34639504475cef1677149ad351b3788a89dba865) | SomeoneToIgnore |
| 2026-11-20 | [Remove actions that do nothing (#67227)](https://github.com/zed-industries/zed/commit/0a514d7ef59c6357878a244fdf8365d03c504767) | ptweezy |
| 2026-11-20 | [Remove write-only fields and dead test plumbing (#67228)](https://github.com/zed-industries/zed/commit/a68d67e0580460cc8806cc7d27b6e1adbc29f27c) | ptweezy |
| 2026-11-20 | [Preserve prompt caching for OpenAI Responses (#67245)](https://github.com/zed-industries/zed/commit/10d1b2a564604dba7b8f05b157b7f9e8ed35255b) | bennetbo |
| 2026-11-20 | [crates_io_client: Add `team_id` query parameter and basic logging (#6…](https://github.com/zed-industries/zed/commit/46d97170084bfc5516e5e2a9058ff8d390343c4b) | MrSubidubi |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
