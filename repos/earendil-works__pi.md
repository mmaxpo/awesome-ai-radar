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
| ⭐ **Stars** | 124.2k |
| 🍴 **Forks** | 16.1k |
| 🐞 **Open issues + PRs** | [315](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 88% · HTML 9% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.6.1](https://github.com/earendil-works/pi/releases/tag/v1.6.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 121.3 MB |

## 📦 Recent releases

### [v1.6.1](https://github.com/earendil-works/pi/releases/tag/v1.6.1)
<sub>2026-11-25 · 2d ago</sub>

> **New Features**
> - **Decision models in codemode**: GitHub Copilot's `gpt-6-luna-decisions` and Radius decision models can be called from codemode `models.classify()`, and results include the provider's `responseId`. See [Classify](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/codemode.md#classify).
> - **One setting per transcript notice**: cache misses, cache warming, compaction costs, and reasoning drops each have their own setting under Notices in `/settings`. See [Model and thinking](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Dialog status kind for extensions**: `ctx.ui.select()`, `ctx.ui.confirm()`, and `ctx.ui.input()` accept `blockedKind`, so terminals with program status can show a dialog as a permission request, question, or login. See [Program Status Kind](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/extensions.md#program-status-kind).
> **Breaking Changes**
> - Replaced the `showCacheMissNotices` setting with one setting per transcript notice: `notices.cacheMisses`, `notices.cacheWarming`, `notices.compactionCosts`, and `notices.reasoningDrops`, configured under Notices in `/settings`. An existing `showCacheMissNotices` value is migrated to all four. `SettingsManager.getShowCacheMissNotices()` and `setShowCacheMissNotices()` are removed; use `getNotices()` and `setNotice()` instead
> …

### [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0)
<sub>2026-11-20 · 7d ago</sub>

> **New Features**
> - **GPT-6.2 Astra and GPT-6.2 Sol**: both models are available on the `openai`, `azure`, and `openai-codex` providers, and GPT-6.2 Sol is now the default model for all three. See [Providers](https://github.com/earendil-works/pi/blob/v1.6.0/packages/coding-agent/docs/providers.md).
> **Breaking Changes**
> - Extension components: `render()` now returns `readonly string[]`, and `Container` returns the same cached array while its children are unchanged. Extensions that modify render output in place, including `super.render()` in a `Container` subclass or an embedded component's output, must copy it first ([#9549](https://github.com/earendil-works/pi/issues/9549))
> **Added**
> - Added GPT-6.2 Astra and GPT-6.2 Sol to the `openai`, `azure`, and `openai-codex` providers. Both reject reasoning effort `none` and `minimal`, so thinking level `off` is unavailable. Azure serves them with a 1.05M context window; Codex serves GPT-6.2 Sol with 500K and GPT-6.2 Astra with 272K
> …

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 17d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 17d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 25d ago</sub>

> **New Features**
> - **Extension update changelogs**: see what changed in installed extension packages on the next fresh launch after an update. Package authors can choose the changelog path, and `collapseChangelog` condenses the notices. See [Show a changelog](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/packages.md#show-a-changelog).
> - **Faster streaming**: large tool calls are parsed incrementally, and code-heavy answers and tool rows reuse highlighting and rendered Markdown instead of repeating the work on every update. See [Keep rendering responsive](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/tui.md#keep-rendering-responsive).
> - **Custom self-update commands**: use `PI_SELF_UPDATE_COMMAND` or `selfUpdateCommand` to update pi through a wrapper or another package manager. See [Custom update command](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#custom-update-command).
> - **GPT-6.1 Terra**: available through OpenAI, Azure OpenAI Responses, and OpenAI Codex, with tool search, mid-conversation thinking-level changes, and thinking `off`. Codex offers a 500K context window. See [Models](https://github.com/earendil-works/pi/blob/v1.5.0/packages/coding-agent/docs/cli.md#models).
> **Breaking Changes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [fix(ai): price image output tokens at the image rate](https://github.com/earendil-works/pi/commit/ccda1f74b805ccb9ed32a5a9100604c0c071f4b4) | vegarsti |
| 2026-11-27 | [Merge branch 'main' of https://github.com/earendil-works/pi into HEAD](https://github.com/earendil-works/pi/commit/6bec0ca53f482d928f31a02a27c78594a0d616e1) | badlogic |
| 2026-11-27 | [test(p3): terminals e2e revokes its sign-in through the scoped revoke…](https://github.com/earendil-works/pi/commit/49a749c02f7f0b235c1b198206136dfcc64e73be) | badlogic |
| 2026-11-27 | [feat(ai): add Radius decision and image models to static catalog](https://github.com/earendil-works/pi/commit/5c0917b7a9c3a2ecc0fb3e8c75f98cb4f72bef35) | vegarsti |
| 2026-11-27 | [feat(ai): report image output tokens in usage](https://github.com/earendil-works/pi/commit/a512c3fe22c760b8e3d1b271952f3291b40a2423) | vegarsti |
| 2026-11-27 | [fix(coding-agent): reword /bug hint](https://github.com/earendil-works/pi/commit/e3c6326334318d15127460ce189ad76bcda671f6) | vegarsti |
| 2026-11-27 | [fix(ai): report reasoning tokens in image and decision usage](https://github.com/earendil-works/pi/commit/d02145c491e152eab8324c7fc0fc598b19ceb9fe) | vegarsti |
| 2026-11-27 | [Merge branch 'main' of https://github.com/earendil-works/pi into HEAD](https://github.com/earendil-works/pi/commit/c424af4623945cae5e4332338a8b1605e164ae51) | badlogic |
| 2026-11-27 | [Merge branch 'main' of https://github.com/earendil-works/pi into HEAD](https://github.com/earendil-works/pi/commit/1822f1ccddb4686a2afb5d8e16d32467689e405b) | badlogic |
| 2026-11-27 | [Merge branch 'main' of https://github.com/earendil-works/pi into k-pty](https://github.com/earendil-works/pi/commit/cd8d77b5d3a67fa5805cb38e2e70fc27c14d2e81) | badlogic |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
