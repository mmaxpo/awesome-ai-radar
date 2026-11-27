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
| 🐞 **Open issues + PRs** | [3.0k](https://github.com/zed-industries/zed/issues) |
| 💻 **Languages** | Rust 98% |
| 📜 **License** | Other |
| 🏷 **Topics** | `text-editor` `zed` `gpui` `rust-lang` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2021-02-20 |
| 📦 **Latest release** | [v1.30.2](https://github.com/zed-industries/zed/releases/tag/v1.30.2) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 550.0 MB |
| 🌐 **Website** | https://zed.dev |

## 📦 Recent releases

### [v1.30.2](https://github.com/zed-industries/zed/releases/tag/v1.30.2)
<sub>2026-11-25 · yesterday</sub>

> This week's release includes reduced GPU usage across the app, a model picker for AI commit message generation in the Git Panel, a setting to hide the title bar, support for GPT-6.1 Terra, and faster scanning of large projects.
> **Features**
> **AI**
> - Added support for GPT-6.1 Terra to the OpenAI provider. ([#66659](https://github.com/zed-industries/zed/pull/66659); thanks [nymo](https://github.com/nymo))
> - Added keyboard navigation to the agent thread switcher (opened with `ctrl-tab` from the Agent Panel or Threads Sidebar): `up` / `down`, `ctrl-n` / `ctrl-p`, and `home` / `end` move the selection, as do `ctrl-up` / `ctrl-down` while `ctrl` is still held. ([#66951](https://github.com/zed-industries/zed/pull/66951); thanks [kinoute](https://github.com/kinoute))
> - Added support for the Extra High thinking effort level for Gemini 4 Hydrogen (`gemini-4-hydrogen`), which now defaults to High. ([#67011](https://github.com/zed-industries/zed/pull/67011); thanks [LorenzoBiassio](https://github.com/LorenzoBiassio))
> …

### [v1.31.0-pre](https://github.com/zed-industries/zed/releases/tag/v1.31.0-pre) _(pre-release)_
<sub>2026-11-25 · yesterday</sub>

> This week's release includes thread-only choices for agent models, profiles, and thinking effort, an Ultrafast response speed for supported OpenAI models, global agent skills in remote projects, faster project scanning, and performance improvements to app layout and terminal rendering.
> **Features**
> **AI**
> - Added thread-only choices in the Zed Agent's model, profile, and thinking effort pickers. Use `cmd-enter` or `cmd-click` on macOS, or `ctrl-enter` or `ctrl-click` on Linux and Windows, to change the current thread without changing your defaults. ([#66869](https://github.com/zed-industries/zed/pull/66869))
> - Added an Ultrafast response speed option for supported OpenAI and ChatGPT Subscription models. ([#67184](https://github.com/zed-industries/zed/pull/67184))
> - Added support for global skills from the remote machine's `~/.agents/skills` in SSH, WSL, and dev container projects. ([#66767](https://github.com/zed-industries/zed/pull/66767))
> …

### [v1.30.2-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.2-pre) _(pre-release)_
<sub>2026-11-20 · 6d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67253](https://github.com/zed-industries/zed/pull/67253))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67188](https://github.com/zed-industries/zed/pull/67188))

### [v1.29.3](https://github.com/zed-industries/zed/releases/tag/v1.29.3)
<sub>2026-11-20 · 6d ago</sub>

> - Fixed prompt caching for reusable OpenAI system instructions on GPT-6.2 and later. ([#67252](https://github.com/zed-industries/zed/pull/67252))
> - Fixed Text Finder showing results from the previous query when a search found no matches. ([#67189](https://github.com/zed-industries/zed/pull/67189))

### [v1.30.1-pre](https://github.com/zed-industries/zed/releases/tag/v1.30.1-pre) _(pre-release)_
<sub>2026-11-18 · 8d ago</sub>

> - Added an official Snap package for Linux ([#67163](https://github.com/zed-industries/zed/pull/67163))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [Fix TCP-based debugging in dev containers (#65778)](https://github.com/zed-industries/zed/commit/ed8dc1b6ca115f3ce70117ebb448dfb61ea030bf) | cadmi |
| 2026-11-27 | [remote: Fix switching git worktrees inside a dev container (#63613)](https://github.com/zed-industries/zed/commit/ae31872139cb5badeb879ded17ec0ac3eaf36354) | senid231 |
| 2026-11-27 | [gpui_linux: Fix X11 file drop position with display scaling (#66866)](https://github.com/zed-industries/zed/commit/46375fbf64574f01dc08fd2d2998aa7bbb7f0377) | akramcodez |
| 2026-11-27 | [agent_ui: Fix subagent card staying failed after a successful retry (…](https://github.com/zed-industries/zed/commit/b47d9288336ac4a37d6365ca753ada32dde2b618) | ManasDasri |
| 2026-11-27 | [editor: Improve performance with many cursors (#67508)](https://github.com/zed-industries/zed/commit/150c2aaeca8778c2759bba92b19247b0901d536f) | smitbarmase |
| 2026-11-27 | [outline_panel: Apply default expansion depth to outlines loaded later…](https://github.com/zed-industries/zed/commit/961ac220b8b65c293ceee59444ae0df7e2ff0708) | Chukwuebuka-2003 |
| 2026-11-26 | [vim: Show yank highlight in characterwise visual mode (#67158)](https://github.com/zed-industries/zed/commit/a0e666ae930a85ab38947e2d49222b0ea99f1c2f) | corthx |
| 2026-11-26 | [dev_container: Support array and numeric feature options (#63978) (#6…](https://github.com/zed-industries/zed/commit/be8084623bdee15143ea5d131476ec4685795e81) | harshaygadekar |
| 2026-11-26 | [dev_container: Fall back to process environment for localEnv (#66581)](https://github.com/zed-industries/zed/commit/03a874000c6e6c373a84797f0636019ce0c6f5cc) | michele-xilo |
| 2026-11-26 | [devcontainer: Only set user with chown (#67492)](https://github.com/zed-industries/zed/commit/9727b5a7f6ff3880b1addd537a603ae1809533da) | blue42u |

[See all commits ↗](https://github.com/zed-industries/zed/commits)

## ⬇️ Get it

```bash
git clone https://github.com/zed-industries/zed.git
```
