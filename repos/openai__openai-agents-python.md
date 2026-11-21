# openai/openai-agents-python

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/openai/openai-agents-python)

> A lightweight, powerful framework for multi-agent workflows

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | OpenAI's official lightweight multi-agent SDK |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 30.8k |
| 🍴 **Forks** | 5.1k |
| 🐞 **Open issues + PRs** | [69](https://github.com/openai/openai-agents-python/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `framework` `llm` `python` `openai` `harness` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-03-11 |
| 📦 **Latest release** | [v0.25.0](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 131.3 MB |
| 🌐 **Website** | https://openai.github.io/openai-agents-python/ |

## 📦 Recent releases

### [v1.0.0-alpha.1](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) — Agents SDK v1.0.0-alpha.1 _(pre-release)_
<sub>2026-11-20 · today</sub>

> **Agents SDK v1.0.0-alpha.1**
> This first preview from `feat/simple-codex` adds Codex as an opt-in model provider for the Python Agents SDK. The prebuilt `openai-agents` wheels (version `1.0.0a1`) are available exclusively through GitHub Releases.
> **Highlights**
> - **Choose Codex per run.** Import `CodexProvider` from `agents.models.codex` and create `provider = CodexProvider()`. Pass `RunConfig(model_provider=provider)` to the Runner. Codex uses your saved login. For API key authentication, use `CodexProvider(api_key=...)`. The provider selects the model for agents that use a model name or the default model. [Run the same agent with either provider](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#run-one-agent-with-either-provider)
> - **Reuse Codex Core inside Python.** The wheel embeds unmodified Codex Core `rust-v0.166.0` through PyO3. Direct calls to Core eliminate `codex app-server` startup and JSON-RPC. Reuse the provider to share one `ThreadManager` across calls. Each call gets a fresh thread. Use an SDK session for history and close the provider with `await provider.aclose()` when you finish. [Thread lifetime and history](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#streaming-history-and-cancellation) · [Codex source](https://github.com/openai/codex/commit/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856)
> - **Use SDK tools and approvals.** Stream text, hand off to a specialist, pause for approval before a Python tool runs, and validate typed output. Native commands follow Codex's sandbox and approval settings. A native approval prompt ends the model call. [Execution and approvals](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#configure-execution) · [Supported tools and model settings](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#supported-features-and-limits)
> …

### [v0.25.0](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0)
<sub>2026-11-18 · 3d ago</sub>

> **[0.25.0](https://github.com/openai/openai-agents-python/compare/v0.24.0...v0.25.0) (2026-11-17)**
> **Key Changes**
> Version 0.25.0 removes the beta Runloop sandbox provider and changes how Pydantic run contexts are checkpointed. Runloop users should preserve their workspace data before switching providers. Applications that share checkpoints across workers should upgrade readers first.
> **Highlights:**
> - Migrate Runloop workloads to another supported sandbox provider, such as Modal, or remain on 0.24.0 while migrating. Provider-specific sessions and snapshots require a separate data migration.
> - Resume nested agent-tool approvals with output guardrails using RunState schema `1.22`. Pydantic checkpoints now preserve default values and in-place edits. Use a custom serializer for process-local resources.
> …

### [v0.24.0-alpha.8](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — Agents SDK v0.24.0-alpha.8 _(pre-release)_
<sub>2026-11-16 · 5d ago</sub>

> **Agents SDK v0.24.0-alpha.8**
> **Highlights**
> - **Approve Python tool calls before they run.** Review the arguments and approve or reject the call. You can remember a decision for the rest of the Session. [Managed approval example](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/managed_approvals/README.md#inspect-and-decide)
> - **Connect your own model client.** The native tool loop works with async Responses and Chat Completions clients, LiteLLM, AnyLLM, and custom adapters. [Application-owned model clients](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/docs/sdk/models.md#use-an-application-owned-model-client)
> - **Add Realtime voice to a Session.** Use a server WebSocket, connect a browser over WebRTC, or attach to an existing SIP call. [Realtime connection options](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/native_voice.md#choose-a-connection)
> - **Resume more kinds of work.** Save supported pending tool requests and approvals. Request and token budgets keep the usage already spent when you restore a supported checkpoint. [Restore a checkpoint with a budget](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/budgeted-recovery.md)
> …

### [v0.24.0-alpha.7](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — Agents SDK v0.24.0-alpha.7 _(pre-release)_
<sub>2026-11-08 · 13d ago</sub>

> **Agents SDK v0.24.0-alpha.7**
> **Highlights**
> - **Use Classic workflows alongside native execution.** Import the retained v0 runtime through `agents.classic`. This alpha also changes executor write defaults; review the upgrade actions before opening existing environments.
> - **Keep conversations in your own storage.** Add durable root Sessions with `CustomStorage`, and reconcile uncertain tool effects before resuming work.
> - **Add voice and hosted tools to native agents.** Connect speech workflows to a Session, or use `FileSearch`, `CodeInterpreter`, and `ImageGeneration` through compatible Responses providers.
> - **Control context, completion, and usage.** Transform model input, retain selected context during compaction, review proposed answers, and limit observed root usage.
> …

### [v0.24.0-alpha.6](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — Agents SDK v0.24.0-alpha.6 _(pre-release)_
<sub>2026-11-03 · 17d ago</sub>

> **Install the preview**
> Use standard CPython 3.10–3.14 in a virtual environment. These wheels include the native runtime; no Rust toolchain or source build is needed. This preview is distributed through GitHub Releases, not PyPI.
> Run the command for your platform:
> **Linux x86_64 (glibc 2.39 or newer)**
> ```sh
> python -m pip install "https://github.com/openai/openai-agents-python/releases/download/v0.24.0-alpha.6/openai_agents-0.24.0a6-cp310-abi3-manylinux_2_39_x86_64.whl"
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [docs: Upgrade the GPT-Live demo to 1.1 (#6101)](https://github.com/openai/openai-agents-python/commit/6c4e4a29cd08eef454db6980d74da6afc8939d24) | seratch |
| 2026-11-18 | [ci: run PyPI publish checks once on Python 3.14 (#6070)](https://github.com/openai/openai-agents-python/commit/91fb508a8931016efa793b033147d08cd20308cf) | seratch |
| 2026-11-18 | [fix: sandbox memory selection across UTC offsets (#6066)](https://github.com/openai/openai-agents-python/commit/e7ce15a25b336bb3d0840ad16dee597f69a6e6d3) | seratch |
| 2026-11-18 | [fix: support opt-in JSON validation for Codex tool parameters (#6067)](https://github.com/openai/openai-agents-python/commit/54492d112b5c3366cc30f35abd60c46fa92140c2) | seratch |
| 2026-11-18 | [fix: allow SDK 0.25 in the external provider example (#6068)](https://github.com/openai/openai-agents-python/commit/9b17858afb5b45f48bbf695cc7c8f34778425156) | jbeckwith-oai |
| 2026-11-18 | [release: 0.25.0 (#5394)](https://github.com/openai/openai-agents-python/commit/0a74177ed23ffb0c2dba24eda3fb12fb58e3e09d) | openai-sdks[bot] |
| 2026-11-17 | [fix: limit the Daytona extra to the supported 0.x SDK (#6065)](https://github.com/openai/openai-agents-python/commit/fd78fa038f853598ed849e25eec78bab1e49aa00) | seratch |
| 2026-11-17 | [fix: align model defaults with TS SDK (#6064)](https://github.com/openai/openai-agents-python/commit/d5287b741dfd93de3ce1625f98b342cd0c4c455e) | seratch |
| 2026-11-17 | [fix(deps): bump openai from 3.29.0 to 3.48.0 (#6054)](https://github.com/openai/openai-agents-python/commit/a4a4fa4cf0e34516df57871196de360253e614fe) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update fastapi requirement from >=0.162.0 to >=0.162.2 in …](https://github.com/openai/openai-agents-python/commit/9a3bce3d0ab013d64aa5591e92a4458d1c658f8b) | dependabot[bot] |

[See all commits ↗](https://github.com/openai/openai-agents-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/openai-agents-python.git
```
