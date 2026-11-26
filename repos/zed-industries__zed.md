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
| ⭐ **Stars** | 95.8k |
| 🍴 **Forks** | 11.9k |
| 🐞 **Open issues + PRs** | [3.1k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.30.2](https://github.com/zed-industries/zed/releases/tag/v1.30.2) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 549.4 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.2](https://github.com/zed-industries/zed/releases/tag/v1.30.2)
<sub>2026-11-25 · today</sub>

> This week's release includes reduced GPU usage across the app, a model picker for AI commit message generation in the Git Panel, a setting to hide the title bar, support for GPT-6.1 Terra, and faster scanning of large projects.
> **Features**
> **AI**
> - Added support for GPT-6.1 Terra to the OpenAI provider. ([#66659](https://github.com/zed-industries/zed/pull/66659); thanks [nymo](https://github.com/nymo))
> - Added keyboard navigation to the agent thread switcher (opened with `ctrl-tab` from the Agent Panel or Threads Sidebar): `up` / `down`, `ctrl-n` / `ctrl-p`, and `home` / `end` move the selection, as do `ctrl-up` / `ctrl-down` while `ctrl` is still held. ([#66951](https://github.com/zed-industries/zed/pull/66951); thanks [kinoute](https://github.com/kinoute))
> - Added support for the Extra High thinking effort level for Gemini 4 Hydrogen (`gemini-4-hydrogen`), which now defaults to High. ([#67011](https://github.com/zed-industries/zed/pull/67011); thanks [LorenzoBiassio](https://github.com/LorenzoBiassio))
> …

### [v1.31.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.31.0-pre) _(pre-release)_
<sub>2026-11-25 · today</sub>

> This week's release includes thread-only choices for agent models, profiles, and thinking effort, an Ultrafast response speed for supported OpenAI models, global agent skills in remote projects, faster project scanning, and performance improvements to app layout and terminal rendering.
> **Features**
> **AI**
> - Added thread-only choices in the Zed Agent's model, profile, and thinking effort pickers. Use `cmd-enter` or `cmd-click` on macOS, or `ctrl-enter` or `ctrl-click` on Linux and Windows, to change the current thread without changing your defaults. ([#66869](https://github.com/zed-industries/zed/pull/66869))
> - Added an Ultrafast response speed option for supported OpenAI and ChatGPT Subscription models. ([#67184](https://github.com/zed-industries/zed/pull/67184))
> - Added support for global skills from the remote machine's `~/.agents/skills` in SSH, WSL, and dev container projects. ([#66767](https://github.com/zed-industries/zed/pull/66767))
> …

### [v1.30.2-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.2-pre) _(pre-release)_
<sub>2026-11-20 · 5d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67253](https://github.com/zed-industries/zed/pull/67253))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67188](https://github.com/zed-industries/zed/pull/67188))

### [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3)
<sub>2026-11-20 · 5d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67252](https://github.com/zed-industries/zed/pull/67252))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67189](https://github.com/zed-industries/zed/pull/67189))

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · 7d ago</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Update hosted Claude model references (#67477)](https://github.com/zed-industries/zed/commit/cd848a6671d5929eac22dd505a6ac90184cc906e) | morgankrey |
| 2026-11-26 | [markdown: Select one line on triple-click in code blocks (#67392)](https://github.com/zed-industries/zed/commit/bbde02be430d018f2c590671d22f89304be03d8b) | ptweezy |
| 2026-11-26 | [path: Find the first differing byte in RelPath::cmp with XOR (#67122)](https://github.com/zed-industries/zed/commit/8202394e984087c42906aafbf44ff267ab8aff1e) | ptweezy |
| 2026-11-26 | [Keep FIFOs in a project from stalling the scanner and git jobs (#67356)](https://github.com/zed-industries/zed/commit/e4fa16422543ab77b129d7f4ad825630b993ecdd) | SomeoneToIgnore |
| 2026-11-26 | [search: Align query input text with the filter inputs (#67493)](https://github.com/zed-industries/zed/commit/fd0b7732b8da3ef65ea210fb8d6b2eb82857df1d) | kitakitaaura |
| 2026-11-26 | [search: Replace from the editor while buffer search is open (#67470)](https://github.com/zed-industries/zed/commit/a3ce8d5e88e35697b2ba1cf9cb3c6816089b8281) | ptweezy |
| 2026-11-25 | [dev_container: Respect readonly mounts (#66071)](https://github.com/zed-industries/zed/commit/8aeb64f7444d25e91e3369bf7f4985d03bf336de) | masonliiu |
| 2026-11-25 | [crashes: Update crash-handler to fix child processes hanging on macOS…](https://github.com/zed-industries/zed/commit/6ba65ce3be7fc08eec910088ea1472174aa4a002) | ptweezy |
| 2026-11-25 | [trusted_worktrees: Fix case-sensitive path comparison on Windows (#67…](https://github.com/zed-industries/zed/commit/dc1a4bfd0582ff16f8d45ea405185dec5ef3a751) | karthik-258-code |
| 2026-11-25 | [fs: Reduce time spent matching event path ancestors in `watcher_ids_c…](https://github.com/zed-industries/zed/commit/aeabc0823d09452d4c06b4a8e6c64f86df0e0d63) | RemcoSmitsDev |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
