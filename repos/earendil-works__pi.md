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
| ⭐ **Stars** | 123.7k |
| 🍴 **Forks** | 16.0k |
| 🐞 **Open issues + PRs** | [302](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 87% · HTML 10% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 114.5 MB |

## 📦 Recent releases

### [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0)
<sub>2026-11-20 · 4d ago</sub>

> **New Features**
> - **GPT-6.2 Astra and GPT-6.2 Sol**: both models are available on the `openai`, `azure`, and `openai-codex` providers, and GPT-6.2 Sol is now the default model for all three. See [Providers](https://github.com/earendil-works/pi/blob/v1.6.0/packages/coding-agent/docs/providers.md).
> **Breaking Changes**
> - Extension components: `render()` now returns `readonly string[]`, and `Container` returns the same cached array while its children are unchanged. Extensions that modify render output in place, including `super.render()` in a `Container` subclass or an embedded component's output, must copy it first ([#9549](https://github.com/earendil-works/pi/issues/9549))
> **Added**
> - Added GPT-6.2 Astra and GPT-6.2 Sol to the `openai`, `azure`, and `openai-codex` providers. Both reject reasoning effort `none` and `minimal`, so thinking level `off` is unavailable. Azure serves them with a 1.05M context window; Codex serves GPT-6.2 Sol with 500K and GPT-6.2 Astra with 272K
> …

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 14d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 14d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 22d ago</sub>

> **New Features**
> - **Extension update changelogs**: see what changed in installed extension packages on the next fresh launch after an update. Package authors can choose the changelog path, and `collapseChangelog` condenses the notices. See [Show a changelog](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/packages.md#show-a-changelog).
> - **Faster streaming**: large tool calls are parsed incrementally, and code-heavy answers and tool rows reuse highlighting and rendered Markdown instead of repeating the work on every update. See [Keep rendering responsive](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/tui.md#keep-rendering-responsive).
> - **Custom self-update commands**: use `PI_SELF_UPDATE_COMMAND` or `selfUpdateCommand` to update pi through a wrapper or another package manager. See [Custom update command](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#custom-update-command).
> - **GPT-6.1 Terra**: available through OpenAI, Azure OpenAI Responses, and OpenAI Codex, with tool search, mid-conversation thinking-level changes, and thinking `off`. Codex offers a 500K context window. See [Models](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#models).
> **Breaking Changes**
> …

### [v1.4.0](https://github.com/earendil-works/pi/releases/tag/v1.4.0)
<sub>2026-10-21 · 1mo ago</sub>

> **New Features**
> - **Image input for classifiers**: codemode `models.classify()` accepts `images` for TypeSafe's Jev and Cloudflare's Clef models on `typesafe`, `cloudflare-workers-ai`, and OpenRouter. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/models.md#use-classifier-models) and [Codemode](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/codemode.md#models).
> - **Models Configuration reference**: every provider, model, model override, and compatibility field of `models.json`, generated from its schema. See [Models Configuration](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/models-configuration.md).
> - **Summaries without a fixed output cap**: compaction and branch summaries use the model's output limit, so long reasoning no longer makes them fail. See [Compaction](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/compaction.md#compaction).
> - **Codemode waits for a free worker**: parallel scripts and in-process subagents queue instead of failing, and `PI_CODEMODE_MAX_WORKERS` raises the limit. See [Codemode limits](https://github.com/earendil-works/pi/blob/v1.4.0/packages/coding-agent/docs/codemode.md#limits).
> - **Rex terminal support**: OSC 8 hyperlinks, truecolor, and inline images.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [fix(p2, backup): new contract to include paused](https://github.com/earendil-works/pi/commit/d4760131efe0740b9b7f7ad1f126734b96a011c0) | cristinaponcela |
| 2026-11-24 | [docs(coding-agent): document classifier responseId in codemode](https://github.com/earendil-works/pi/commit/fe1c08109d76a21c36f2ed64a41e854c05220d29) | vegarsti |
| 2026-11-24 | [feat(ai): expose OpenRouter classifier responseId and reported cost](https://github.com/earendil-works/pi/commit/bff71c70967eeefb72729c8590c786bffcd73937) | vegarsti |
| 2026-11-24 | [fix(coding-agent): rebuilt ! output follows ctrl+o (#12427)](https://github.com/earendil-works/pi/commit/0ab23c37b074252d04e31f5cfb99491f0613fb80) | acmerfight |
| 2026-11-24 | [fix(ai): record OpenRouter native_finish_reason](https://github.com/earendil-works/pi/commit/ddf5868d2866394b6b90109ea7151812d85019d5) | vegarsti |
| 2026-11-24 | [fix(tui): do not emit OSC 8 hyperlinks for URLs over 8192 characters …](https://github.com/earendil-works/pi/commit/6ca01d1e93c316b2b9da34d68807293d6fbdb5dc) | robopipi[bot] |
| 2026-11-24 | [fix(tui): skip synthetic right-click paste in Tabby on Windows (#12473)](https://github.com/earendil-works/pi/commit/165c70df953c62e82a2d0ea88f01af5267a39ef2) | robopipi[bot] |
| 2026-11-24 | [fix(tui): keep Markdown after an unclosed currency dollar sign (#12472)](https://github.com/earendil-works/pi/commit/362bf6f1bec2db70dc072e4db4eb5b2903f4e9f6) | robopipi[bot] |
| 2026-11-24 | [fix(ai): support xhigh thinking on Gemini 4 Hydrogen and Neon](https://github.com/earendil-works/pi/commit/001ffff32bbf58703c618ba598454b78501573d6) | davidbrai |
| 2026-11-24 | [feat(coding-agent): simplify first-time setup with colored logo and d…](https://github.com/earendil-works/pi/commit/f8149d1abde50b31c8cb5aed09e89319b927f247) | vegarsti |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
