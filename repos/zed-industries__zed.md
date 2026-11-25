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
| ⭐ **Stars** | 95.7k |
| 🍴 **Forks** | 11.8k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 545.1 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.2-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.2-pre) _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67253](https://github.com/zed-industries/zed/pull/67253))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67188](https://github.com/zed-industries/zed/pull/67188))

### [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3)
<sub>2026-11-20 · 4d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67252](https://github.com/zed-industries/zed/pull/67252))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67189](https://github.com/zed-industries/zed/pull/67189))

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · 6d ago</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

### [v1.29.2](https://github.com/zed-industries/zed/releases/tag/v1.29.2)
<sub>2026-11-18 · 6d ago</sub>

> - Added an official Snap package for Linux ([#67164](https://github.com/zed-industries/zed/pull/67164))

### [v1.29.1](https://github.com/zed-industries/zed/releases/tag/v1.29.1)
<sub>2026-11-18 · 6d ago</sub>

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
| 2026-11-25 | [gpui: Bump resvg and usvg to 0.49 to fix an SVG filter crash (#67423)](https://github.com/zed-industries/zed/commit/cd585371e8bf275664f4ae3434bb1e0a7fe6b7e9) | SomeoneToIgnore |
| 2026-11-25 | [Document hosted Gemini 4 and GPT-6.2 models (#67457)](https://github.com/zed-industries/zed/commit/e84c6c61adb54bc6140a85b307d18cf970c24ab5) | tomhoule |
| 2026-11-25 | [Update Docker logo (#67425)](https://github.com/zed-industries/zed/commit/f38d614b4b58bb44cc19d08ef5dd3efba918f9a3) | ashraf7hossain |
| 2026-11-25 | [bedrock: Rework the provider around run-time model discovery (#67258)](https://github.com/zed-industries/zed/commit/ced6b5e2cd906fc432b98965572e2bac674647ab) | 5herlocked |
| 2026-11-25 | [gpui: Add BoundsTree test suite (#67443)](https://github.com/zed-industries/zed/commit/77228009dd267dcf8ab9a20eef5802b2a8ea4afa) | Anthony-Eid |
| 2026-11-25 | [gpui: Remove `.unwrap()` on every GPUI entity borrow (#67361)](https://github.com/zed-industries/zed/commit/fa6e2e98c703d6fa65aef299d4f07ddc28b8a466) | tidely |
| 2026-11-24 | [agent: Speed up locating old text in large files (#67395)](https://github.com/zed-industries/zed/commit/2664a0aa1eae5dabf8f8273c03f88d53061ca7dc) | ptweezy |
| 2026-11-24 | [terminal: Highlight links on hover in mouse mode (#67319)](https://github.com/zed-industries/zed/commit/f98c2c100d217ace3ca99564cfc4573612d43d47) | ptweezy |
| 2026-11-24 | [sandbox: Let embedders name the Windows sandbox launcher (#67437)](https://github.com/zed-industries/zed/commit/335d29c6d93bccf0814e52dd1445e13c5b204e57) | rtfeldman |
| 2026-11-24 | [Remove deprecated `package.authors` from Cargo manifests (#67435)](https://github.com/zed-industries/zed/commit/0be6d5990f9f6e3917464603a99808502cc824af) | Sha1rholder |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
