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
| ⭐ **Stars** | 123.8k |
| 🍴 **Forks** | 16.0k |
| 🐞 **Open issues + PRs** | [309](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 87% · HTML 10% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.6.1](https://github.com/earendil-works/pi/releases/tag/v1.6.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 115.2 MB |

## 📦 Recent releases

### [v1.6.1](https://github.com/earendil-works/pi/releases/tag/v1.6.1)
<sub>2026-11-25 · today</sub>

> **New Features**
> - **Decision models in codemode**: GitHub Copilot's `gpt-6-luna-decisions` and Radius decision models can be called from codemode `models.classify()`, and results include the provider's `responseId`. See [Classify](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/codemode.md#classify).
> - **One setting per transcript notice**: cache misses, cache warming, compaction costs, and reasoning drops each have their own setting under Notices in `/settings`. See [Model and thinking](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Dialog status kind for extensions**: `ctx.ui.select()`, `ctx.ui.confirm()`, and `ctx.ui.input()` accept `blockedKind`, so terminals with program status can show a dialog as a permission request, question, or login. See [Program Status Kind](https://github.com/earendil-works/pi/blob/v1.6.1/packages/coding-agent/docs/extensions.md#program-status-kind).
> **Breaking Changes**
> - Replaced the `showCacheMissNotices` setting with one setting per transcript notice: `notices.cacheMisses`, `notices.cacheWarming`, `notices.compactionCosts`, and `notices.reasoningDrops`, configured under Notices in `/settings`. An existing `showCacheMissNotices` value is migrated to all four. `SettingsManager.getShowCacheMissNotices()` and `setShowCacheMissNotices()` are removed; use `getNotices()` and `setNotice()` instead
> …

### [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0)
<sub>2026-11-20 · 5d ago</sub>

> **New Features**
> - **GPT-6.2 Astra and GPT-6.2 Sol**: both models are available on the `openai`, `azure`, and `openai-codex` providers, and GPT-6.2 Sol is now the default model for all three. See [Providers](https://github.com/earendil-works/pi/blob/v1.6.0/packages/coding-agent/docs/providers.md).
> **Breaking Changes**
> - Extension components: `render()` now returns `readonly string[]`, and `Container` returns the same cached array while its children are unchanged. Extensions that modify render output in place, including `super.render()` in a `Container` subclass or an embedded component's output, must copy it first ([#9549](https://github.com/earendil-works/pi/issues/9549))
> **Added**
> - Added GPT-6.2 Astra and GPT-6.2 Sol to the `openai`, `azure`, and `openai-codex` providers. Both reject reasoning effort `none` and `minimal`, so thinking level `off` is unavailable. Azure serves them with a 1.05M context window; Codex serves GPT-6.2 Sol with 500K and GPT-6.2 Astra with 272K
> …

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 15d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 15d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 23d ago</sub>

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
| 2026-11-25 | [fix(coding-agent,tui): name the configured keys in key hints (#12541)](https://github.com/earendil-works/pi/commit/b882d08f34f8a245c8d3ea8b057759e1b8b2054c) | petrroll |
| 2026-11-25 | [fix(coding-agent): name the interrupt key in the ! command cancel hin…](https://github.com/earendil-works/pi/commit/745338811405a31831005300aedac173a512e0e4) | acmerfight |
| 2026-11-25 | [fix(chord): wait for macOS file events to start in two plugins tests](https://github.com/earendil-works/pi/commit/e4cd354e6f3ce317a9dd4a8ab1dd4fb6500ebc98) | davidbrai |
| 2026-11-25 | [fix(coding-agent): confirm the highlighted /llama search result after…](https://github.com/earendil-works/pi/commit/bfafd8ed5168bca1f1ca88ef0529cfd326664d16) | robopipi[bot] |
| 2026-11-25 | [fix(p2, backups): stream to save server memory](https://github.com/earendil-works/pi/commit/2e4deff6b3b8e2317bd59b8f8ba96ac5f9b47f13) | cristinaponcela |
| 2026-11-25 | [Add [Unreleased] section for next cycle](https://github.com/earendil-works/pi/commit/dbc8075abb0c1dc6da679c5bdbb730efc09a2cec) | davidbrai |
| 2026-11-25 | [Release v1.6.1](https://github.com/earendil-works/pi/commit/ef4a1cfcca62b77ad3558337ff3e1c7f6beeadfe) | davidbrai |
| 2026-11-25 | [feat(p3): export chord sync and add backup marker](https://github.com/earendil-works/pi/commit/7cf1443c1318fe670870fd342d24cbd23eba8cae) | cristinaponcela |
| 2026-11-25 | [docs(coding-agent): audit changelog since v1.6.0, add New Features](https://github.com/earendil-works/pi/commit/ad403d7d3e5d6f2c24e961cfdbe758796ce44888) | davidbrai |
| 2026-11-25 | [fix(coding-agent): make output file failure test independent of temp …](https://github.com/earendil-works/pi/commit/3511d455419e868faf76a71246add4f611d48c61) | davidbrai |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
