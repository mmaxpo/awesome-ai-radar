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
| ⭐ **Stars** | 123.1k |
| 🍴 **Forks** | 15.9k |
| 🐞 **Open issues + PRs** | [282](https://github.com/earendil-works/pi/issues) |
| 💻 **Languages** | TypeScript 87% · HTML 10% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-08-09 |
| 📦 **Latest release** | [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 113.4 MB |

## 📦 Recent releases

### [v1.6.0](https://github.com/earendil-works/pi/releases/tag/v1.6.0)
<sub>2026-11-20 · yesterday</sub>

> **New Features**
> - **GPT-6.2 Astra and GPT-6.2 Sol**: both models are available on the `openai`, `azure`, and `openai-codex` providers, and GPT-6.2 Sol is now the default model for all three. See [Providers](https://github.com/earendil-works/pi/blob/v1.6.0/packages/coding-agent/docs/providers.md).
> **Breaking Changes**
> - Extension components: `render()` now returns `readonly string[]`, and `Container` returns the same cached array while its children are unchanged. Extensions that modify render output in place, including `super.render()` in a `Container` subclass or an embedded component's output, must copy it first ([#9549](https://github.com/earendil-works/pi/issues/9549))
> **Added**
> - Added GPT-6.2 Astra and GPT-6.2 Sol to the `openai`, `azure`, and `openai-codex` providers. Both reject reasoning effort `none` and `minimal`, so thinking level `off` is unavailable. Azure serves them with a 1.05M context window; Codex serves GPT-6.2 Sol with 500K and GPT-6.2 Astra with 272K
> …

### [v1.5.2](https://github.com/earendil-works/pi/releases/tag/v1.5.2)
<sub>2026-11-10 · 11d ago</sub>

> **New Features**
> - **Fork sessions whose folder is gone**: when a session's original folder was moved or deleted, you can now fork it into the current folder instead of only continuing, so later resumes no longer ask. See [Continue or switch sessions](https://github.com/earendil-works/pi/blob/v1.5.2/packages/coding-agent/docs/sessions.md#continue-or-switch-sessions).
> **Changed**
> - When a session's working directory no longer exists, for example after the project folder was renamed, interactive mode now offers `Continue`, `Fork`, or `Cancel` instead of only continuing. `Continue` runs the session in the current directory without storing the choice, as before; `Fork` copies it into the current directory as a new session with a new ID, like `--fork`, so the next resume no longer asks. This applies at startup (`--session`, `--resume`), to `/resume`, to `/import`, and to `ctx.switchSession()` from extensions ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> **Fixed**
> - Fixed `/import` of a session whose working directory no longer exists leaving a copy in the session directory, and continuing it leaving a second copy with the same ID (`s.jsonl` and `s-1.jsonl`); the failed copy is now removed ([#11975](https://github.com/earendil-works/pi/pull/11975) by [@petrroll](https://github.com/petrroll), fixes [#11060](https://github.com/earendil-works/pi/issues/11060))
> …

### [v1.5.1](https://github.com/earendil-works/pi/releases/tag/v1.5.1)
<sub>2026-11-09 · 11d ago</sub>

> **New Features**
> - **Shell login and logout**: use `pi auth login <provider>` and `pi auth logout <provider>` without starting a session, with API-key and no-browser sign-in options. See [Credential commands](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/cli.md#credential-commands).
> - **Idle prompt cache warming**: eligible caches now stay warm for up to 30 minutes between runs when a refresh is expected to pay for itself. See [`cacheWarming`](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#model-and-thinking).
> - **Anthropic message threads**: requests send only new messages while the server continues the conversation, with full-request fallback when earlier context changes. See [Anthropic compatibility](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models-configuration.md#anthropic-messages).
> - **Richer Mermaid diagrams**: pie charts, author-defined styles, clickable labels on supported terminals, and diagrams in expanded branch and compaction summaries. See [Display settings](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/settings.md#terminal-and-display) and [Markdown transformers](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/extensions.md#piregistermarkdowntransformertransformer-options).
> - **GitHub Copilot classifiers**: call Microsoft-Decision-1 through codemode `models.classify()` for typed decisions and probabilities. See [Use classifier models](https://github.com/earendil-works/pi/blob/v1.5.1/packages/coding-agent/docs/models.md#use-classifier-models).
> …

### [v1.5.0](https://github.com/earendil-works/pi/releases/tag/v1.5.0)
<sub>2026-11-02 · 19d ago</sub>

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
| 2026-11-21 | [fix(p2): subagent models action lists every provider, unknown models …](https://github.com/earendil-works/pi/commit/780bf31fcaeb252fa9b68df3964c735eae75bde3) | mitsuhiko |
| 2026-11-20 | [fix(p2): MCP results reach scripts as pi's whole CallToolResult, mode…](https://github.com/earendil-works/pi/commit/1acc72acd1ab3481066fe97790ccd3cb2059ea83) | mitsuhiko |
| 2026-11-20 | [fix(coding-agent): run shutdown cleanup when the Windows console clos…](https://github.com/earendil-works/pi/commit/31b407dc6313eb3b232342d3fd59db70f661ded3) | petrroll |
| 2026-11-20 | [fix(p2): highlight file and patch lines in context, so multi-line com…](https://github.com/earendil-works/pi/commit/9d63bb7277999ac83c7b1bd8b616141b28a9f666) | badlogic |
| 2026-11-20 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/d25d134c6059173bf2677006cf75be8c041b1aad) | badlogic |
| 2026-11-20 | [fix(p2): MCP results reach code-mode scripts whole; the model's cut r…](https://github.com/earendil-works/pi/commit/51532e40c2d5884783cc3c2586844a51baa0636a) | badlogic |
| 2026-11-20 | [fix(ai): Gemini 3+ detection for prefixed Google model IDs, add compa…](https://github.com/earendil-works/pi/commit/fe8a6f5dc741e9214a20f70f359c68c72b494d1e) | petrroll |
| 2026-11-20 | [Merge branch 'main' of https://github.com/earendil-works/pi](https://github.com/earendil-works/pi/commit/e98e59334d9c85532f8762b73fd98a9468ec807d) | badlogic |
| 2026-11-20 | [fix(p2): type an agent's terminal command after the shell's first pro…](https://github.com/earendil-works/pi/commit/1ca2542572dc9ed8840ccfb927f8a5690960bb44) | badlogic |
| 2026-11-20 | [fix(ai): resolve Bedrock SSO credentials through HTTPS_PROXY (#12365)](https://github.com/earendil-works/pi/commit/be269f57b1b707399edd86f5f718d1a907ffea8b) | robopipi[bot] |

[See all commits ↗](https://github.com/earendil-works/pi/commits)

## ⬇️ Get it

```bash
git clone https://github.com/earendil-works/pi.git
```
