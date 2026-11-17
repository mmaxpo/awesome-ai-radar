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
| ⭐ **Stars** | 122.5k |
| 🍴 **Forks** | 15.8k |
| 🐞 **Open issues + PRs** | [255](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 88% · HTML 9% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 110.4 MB |

## 📦 Recent releases

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 7d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 7d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 15d ago</sub>

> **New Features**
> - **Extension update changelogs**: see what changed in installed extension packages on the next fresh launch after an update. Package authors can choose the changelog path, and `collapseChangelog` condenses the notices. See [Show a changelog](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/packages.md#show-a-changelog).
> - **Faster streaming**: large tool calls are parsed incrementally, and code-heavy answers and tool rows reuse highlighting and rendered Markdown instead of repeating the work on every update. See [Keep rendering responsive](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/tui.md#keep-rendering-responsive).
> - **Custom self-update commands**: use `PI_SELF_UPDATE_COMMAND` or `selfUpdateCommand` to update pi through a wrapper or another package manager. See [Custom update command](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#custom-update-command).
> - **GPT-6.1 Terra**: available through OpenAI, Azure OpenAI Responses, and OpenAI Codex, with tool search, mid-conversation thinking-level changes, and thinking `off`. Codex offers a 500K context window. See [Models](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#models).
> **Breaking Changes**
> …

### [v1.4.0](https://github.com/earendil-works/pi/releases/tag/v1.4.0)
<sub>2026-10-21 · 26d ago</sub>

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
| 2026-11-17 | [feat(p3): slice 1 redo and slice 26, the release build and the p3 com…](https://github.com/earendil-works/pi/commit/5f89cc0a7df669813650bfdac498f8ff865e8233) | badlogic |
| 2026-11-17 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/4afe78de1e51162c01c946dcf080e6a266685a01) | badlogic |
| 2026-11-17 | [docs(p3): worker memory budget 50 MiB](https://github.com/earendil-works/pi/commit/bddf3d9ae9e3e156d58daa17776e9a985b4a65ca) | badlogic |
| 2026-11-17 | [feat(p2): tree panel beside the transcript](https://github.com/earendil-works/pi/commit/1f6f319bb28992a40b99c147fffb23b65a23129d) | christianklotz |
| 2026-11-16 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/5a2febe5d7638ab05540b44a60518b41201be170) | badlogic |
| 2026-11-16 | [docs(p3): slice 1 approved; worker memory levers and a 45 MiB budget](https://github.com/earendil-works/pi/commit/8114439c855bd3ae96850876a09fca31c9eebde6) | badlogic |
| 2026-11-16 | [fix(coding-agent): capture git and npm output while the interactive T…](https://github.com/earendil-works/pi/commit/b513b64d8ac88b66d3501bf5a872b6a7afb3be67) | petrroll |
| 2026-11-16 | [fix(tui,coding-agent): make fullscreen scroll frames O(viewport) (#11…](https://github.com/earendil-works/pi/commit/b7bb7ca905b818bcd6734cb013bb00e5a3d89be9) | petrroll |
| 2026-11-16 | [fix(coding-agent): report pi.events handler errors like other extensi…](https://github.com/earendil-works/pi/commit/18e99051be241de2a0ad65714718354c9407db74) | petrroll |
| 2026-11-16 | [fix(coding-agent): report model fallback after /resume and in every m…](https://github.com/earendil-works/pi/commit/c8c456c85c6e0256be620ab73dc59d3522dbfeaa) | petrroll |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
