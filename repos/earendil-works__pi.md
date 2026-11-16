# earendil-works/pi

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/earendil-works/pi)

> AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Agent toolkit: unified LLM API, agent loop, TUI and the pi coding-agent CLI |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 122.3k |
| 🍴 **Forks** | 15.8k |
| 🐞 **Open issues + PRs** | [259](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 88% · HTML 9% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 110.3 MB |

## 📦 Recent releases

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 6d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 6d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 14d ago</sub>

> **New Features**
> - **Extension update changelogs**: see what changed in installed extension packages on the next fresh launch after an update. Package authors can choose the changelog path, and `collapseChangelog` condenses the notices. See [Show a changelog](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/packages.md#show-a-changelog).
> - **Faster streaming**: large tool calls are parsed incrementally, and code-heavy answers and tool rows reuse highlighting and rendered Markdown instead of repeating the work on every update. See [Keep rendering responsive](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/tui.md#keep-rendering-responsive).
> - **Custom self-update commands**: use `PI_SELF_UPDATE_COMMAND` or `selfUpdateCommand` to update pi through a wrapper or another package manager. See [Custom update command](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#custom-update-command).
> - **GPT-6.1 Terra**: available through OpenAI, Azure OpenAI Responses, and OpenAI Codex, with tool search, mid-conversation thinking-level changes, and thinking `off`. Codex offers a 500K context window. See [Models](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#models).
> **Breaking Changes**
> …

### [v1.4.0](https://github.com/earendil-works/pi/releases/tag/v1.4.0)
<sub>2026-10-21 · 25d ago</sub>

> **New Features**
> - **Image input for classifiers**: codemode `models.classify()` accepts `images` for TypeSafe's Jev and Cloudflare's Clef models on `typesafe`, `cloudflare-workers-ai`, and OpenRouter. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/models.md#use-classifier-models) and [Codemode](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/codemode.md#models).
> - **Models Configuration reference**: every provider, model, model override, and compatibility field of `models.json`, generated from its schema. See [Models Configuration](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/models-configuration.md).
> - **Summaries without a fixed output cap**: compaction and branch summaries use the model's output limit, so long reasoning no longer makes them fail. See [Compaction](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/compaction.md#compaction).
> - **Codemode waits for a free worker**: parallel scripts and in-process subagents queue instead of failing, and `PI_CODEMODE_MAX_WORKERS` raises the limit. See [Codemode limits](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/codemode.md#limits).
> - **Rex terminal support**: OSC 8 hyperlinks, truecolor, and inline images.
> …

### [v1.3.0](https://github.com/earendil-works/pi/releases/tag/v1.3.0)
<sub>2026-10-15 · 1mo ago</sub>

> **New Features**
> - **Choose where `/share` uploads**: `sessionShareDestination` selects `auto`, `gist`, or `radius`. See [Sessions and context](https://github.com/earendil-works/pi/blob/v1.3.0/packages/coding-agent/docs/settings.md#sessions-and-context) and [Export or share a session](https://github.com/earendil-works/pi/blob/v1.3.0/packages/coding-agent/docs/sessions.md#export-or-share-a-session).
> - **Cache-preserving thinking level changes on OpenAI GPT-6**: changing the thinking level mid-session with an API key keeps the prompt cache.
> - **Kimi Code over Chat Completions**: tools added mid-conversation no longer invalidate the prompt cache. `models.json` base URL overrides must now include `/v1`. See [Providers](https://github.com/earendil-works/pi/blob/v1.3.0/packages/coding-agent/docs/providers.md).
> - **Clean model switching**: thinking from a previous model is dropped instead of being shown to the new model as text.
> - **Resumed sessions keep their active tools**: `--tools +name`/`-name` applies on top of them. See [Tools](https://github.com/earendil-works/pi/blob/v1.3.0/packages/coding-agent/docs/settings.md#tools).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [docs(p3): practices for the renamed package; mutation copies and leak…](https://github.com/earendil-works/pi/commit/747c217b81980206063a89e46645b362de7ac8b1) | badlogic |
| 2026-11-16 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/9cd49d2c00ac446f774b878d25923bdb3739dadd) | badlogic |
| 2026-11-16 | [docs(p3): Fable plans and reviews, Opus builds](https://github.com/earendil-works/pi/commit/7f8229d6e0659f4c07d7cd8c04e00b2faeec6dcb) | badlogic |
| 2026-11-16 | [feat(p2): create a project from the sidebar's Projects options](https://github.com/earendil-works/pi/commit/0826f9f39f42bb252e4b6ea51015b63f00f63deb) | davidbrai |
| 2026-11-16 | [fix(p2): show every project in the sidebar, sessions or not](https://github.com/earendil-works/pi/commit/c17ff512f7c5a6d5738d0803e3b44b34aa7c11da) | davidbrai |
| 2026-11-16 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/1e9bebc089ba5394a53064571cb6a73c115dc99e) | badlogic |
| 2026-11-16 | [docs(p3): the basics before iterating: slices 26, 27, 25](https://github.com/earendil-works/pi/commit/865881c110320b6f8ce2709c1b019b590d497c66) | badlogic |
| 2026-11-16 | [fix(coding-agent): update undici to 8.12.4 for security advisories](https://github.com/earendil-works/pi/commit/efbcd5adb4bc89f66a9694093be5785511e3eef6) | davidbrai |
| 2026-11-16 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/9bd70ea1d044c57d412fef6d23ba53afb976dd80) | badlogic |
| 2026-11-16 | [docs(p3): practices: p3 runs two ways, from the checkout and as a rel…](https://github.com/earendil-works/pi/commit/110c854f4708666036176d936bb57cb7aa7e1973) | badlogic |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
