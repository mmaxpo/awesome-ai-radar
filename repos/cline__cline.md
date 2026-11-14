# cline/cline

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/cline/cline)

> Autonomous coding agent as an SDK, IDE extension, or CLI assistant.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Autonomous coding agent inside VS Code |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 71.6k |
| 🍴 **Forks** | 7.9k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/cline/cline/issues) |
| 💻 **Languages** | TypeScript 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2024-07-06 |
| 📦 **Latest release** | [v4.1.26](https://github.com/cline/cline/releases/tag/v4.1.26) — 2026-10-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 622.9 MB |
| 🌐 **Website** | https://cline.bot |

## 📦 Recent releases

### [v4.1.26](https://github.com/cline/cline/releases/tag/v4.1.26)
<sub>2026-10-26 · 19d ago</sub>

> **Added**
> - Cloud tasks: Settings > API Configuration has a Local | Cloud toggle when cloud sessions are on. Cloud picks the Cline model new cloud tasks run on, saved separately from your local models. Clicking the model label in a cloud session's composer opens it there.
> - Starting or resuming a cloud sandbox shows a progress card with the repo, branch and steps (start sandbox, clone repository, start agent). It collapses once the agent starts.
> **Changed**
> - Cloud sessions hide the Plan/Act toggle and the auto-approve bar instead of showing them disabled.
> - With no model chosen, the Cline provider uses Claude Sonnet 5.5 again, which is back at the top of Cline's recommended list.
> …

### [desktop-v0.0.49](https://github.com/cline/cline/releases/tag/desktop-v0.0.49) — Desktop v0.0.49
<sub>2026-10-26 · 19d ago</sub>

> - A new **Changes** button in the session header shows the session's line counts and opens a pane listing the files changed in the last turn or across the whole session, with a diff of each. When a turn finishes, a summary under it lists the files it changed; click it to open the pane on that turn
> - A **project files panel** (folder button in the session header) shows a file tree beside the conversation, with a read-only tabbed viewer, git status letters, and a marker on files the session changed. Files the agent edited get a File/Diff toggle. Works on local and SSH environments
> - An integrated **terminal panel** opens at the bottom of the window (toggle with Ctrl+backtick)
> - Pull request status moved from the bar above the composer into a header button. Its menu shows the PR title, merge status and checks (failing checks first), and lets you open the PR on GitHub, create a PR, copy the branch name, or refresh
> - A new **Local Models** settings page manages Ollama and LM Studio models: setup guidance, model details and storage, and a composer chip showing how much memory the loaded model uses
> - **Keybindings** are configurable in Settings (also reachable from the app and Help menus). Quit can require holding the shortcut, 1 second by default on macOS, so it's harder to quit by accident
> …

### [cli-v3.0.74](https://github.com/cline/cline/releases/tag/cli-v3.0.74) — CLI v3.0.74
<sub>2026-10-26 · 19d ago</sub>

> - Opening a task that's already running in another Cline app now attaches to that run instead of starting a second one that couldn't be stopped. If an app closes mid-task, requests waiting on it now fail with a clear message instead of hanging
> - `cline hub status` and `cline doctor` no longer hang on a Hub that has frozen. Its health check now times out after 3s and the Hub is reported as not running
> - A turn whose connection drops after the model has streamed only reasoning (for example, "The socket connection was closed unexpectedly") is now retried instead of ending the run
> - Model requests retry at most 3 times instead of 5
> - Kimi K3 now gets `max` reasoning for Extra High and Max, instead of an `xhigh` setting it rejects
> - Gemini API keys (the `gemini` provider) no longer send native Google Search. Free-tier keys failed every turn with a 429 quota error on Gemini 3+, and on Gemini 2.x every Cline tool was dropped
> …

### [sdk/sdk/v0.2.0](https://github.com/cline/cline/releases/tag/sdk/sdk/v0.2.0) — SDK v0.2.0
<sub>2026-10-26 · 19d ago</sub>

> - Starting a session that already has a run in progress now reattaches to the live session instead of replacing its runtime. Before, the original run kept going but couldn't be reached, and its transcript writes landed on a stale snapshot. A start that includes a prompt while a run is in progress is rejected
> - The hub records every client that registered a capability for a session, including clients that join a task that's already running, and sends each request to the first one still connected. If none is left, the request fails quickly with a message the user can act on, instead of waiting forever
> - A turn whose connection drops after the model has streamed only reasoning is now retried, and the partial reasoning is discarded. Turns with text, media or tool calls are still never retried
> - Model requests retry at most 3 times after the first attempt (down from 5). Failed attempts are recorded in Langfuse traces, and cancelled requests are no longer reported as Langfuse errors
> - AI SDK updated to `ai` 7.0.136 / `@ai-sdk/provider-utils` 5.0.58. `max` reasoning now reaches the provider: the gateway no longer turns it into `xhigh`, and Kimi K3 gets `max` for Extra High and Max. Empty Anthropic turns are still retried despite the new `anthropic.*` custom stream parts
> - The `gemini` provider no longer sends native Google Search. On Gemini 3+, free-tier keys failed every turn with a 429 quota error, and on Gemini 2.x it dropped every Cline tool. Vertex keeps native search
> …

### [desktop-v0.0.48](https://github.com/cline/cline/releases/tag/desktop-v0.0.48) — Desktop v0.0.48
<sub>2026-10-17 · 28d ago</sub>

> - GPT-6 models (such as `gpt-6-sol` and `gpt-6.1-sol`) work on OpenAI and Azure OpenAI-compatible endpoints. Before, every request was rejected because Cline sent `max_tokens` instead of `max_completion_tokens`
> - The Cline provider's default model is Claude Sonnet 5.5 again, which is back at the top of Cline's recommended list
> - Refreshed the model catalog. Adds the CommandCode and Reflection providers. Default models change for 302.AI (Gemini 4 Argon), Eden AI and Prime Inference (Muse Spark Open), CoreWeave (Reflection Beam 1.0), NanoGPT, Pioneer (Nemotron 3.5 Super VL), and Scaleway (DeepSeek V4.1 Flash)
> **Full Changelog**: https://github.com/cline/cline/compare/desktop-v0.0.47...desktop-v0.0.48

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [refactor(vscode): migrate xAI provider settings to GenericProviderSet…](https://github.com/cline/cline/commit/72b3d7140553a733242126e51a7c2e87efe75c64) | dominiccooney |
| 2026-11-12 | [refactor(vscode): unify generic provider fallback names with presenta…](https://github.com/cline/cline/commit/50e77bc1e8f7ab023b7986821e4b5f82ff51b8c4) | dominiccooney |
| 2026-11-12 | [fix(vscode): refresh generic provider models after saving credentials…](https://github.com/cline/cline/commit/d9a5258ba8afa9d55ccf2c43ec81f435f53132c8) | dominiccooney |
| 2026-11-11 | [refactor(vscode): remove dead LiteLLM/OpenAI model state and unused m…](https://github.com/cline/cline/commit/32075f1110841fe5c7a17e096007e26da8e958f9) | dominiccooney |
| 2026-11-11 | [refactor(vscode): remove dead onboarding models state and proto messa…](https://github.com/cline/cline/commit/c5df41f937c496ce8c8e689ba58776593c703dfa) | dominiccooney |
| 2026-11-10 | [revert(llms): back out AI/ML API ranking/attribution and Wally provid…](https://github.com/cline/cline/commit/7796dc9ce12a6377796d1c265036c4038ff3fcb6) | saoudrizwan |
| 2026-11-10 | [feat(cli): default non-interactive runs to yolo mode (#15644)](https://github.com/cline/cline/commit/d9b24c20317af6412b7a2c32f6f6453420500961) | abeatrix |
| 2026-11-10 | [Remove PostHog events (#15642)](https://github.com/cline/cline/commit/7c5bb54fcb6b66d2717016be33ce2dad692b4501) | BarreiroT |
| 2026-11-10 | [fix(desktop): preserve cloud recency across reconnects (#15637)](https://github.com/cline/cline/commit/dcccbd7712c0ee09f557f6572c9866e6bd36bc08) | johnwschoi |
| 2026-11-10 | [refactor(desktop): move MCP management to hub (#15498)](https://github.com/cline/cline/commit/500a40e7b76692153906b44dd68732520a966663) | abeatrix |

[See all commits ↗](https://github.com/cline/cline/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cline/cline.git
```
