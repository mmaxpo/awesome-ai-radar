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
| ⭐ **Stars** | 30.9k |
| 🍴 **Forks** | 5.1k |
| 🐞 **Open issues + PRs** | [85](https://github.com/openai/openai-agents-python/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `framework` `llm` `python` `openai` `harness` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-03-11 |
| 📦 **Latest release** | [v0.26.0](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 130.6 MB |
| 🌐 **Website** | https://openai.github.io/openai-agents-python/ |

## 📦 Recent releases

### [v0.26.0](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0)
<sub>2026-11-24 · today</sub>

> **[0.26.0](https://github.com/openai/openai-agents-python/compare/v0.25.0...v0.26.0) (2026-11-24)**
> **Features**
> * Upgrade the GPT-Live demo to 1.1 ([6c4e4a2](https://github.com/openai/openai-agents-python/commit/6c4e4a29cd08eef454db6980d74da6afc8939d24))
> **Bug Fixes**
> * allow SDK 0.25 in the external provider example ([#6068](https://github.com/openai/openai-agents-python/issues/6068)) ([9b17858](https://github.com/openai/openai-agents-python/commit/9b17858afb5b45f48bbf695cc7c8f34778425156))
> * apply the Docker removal CPU limit to path inspection ([14d13f4](https://github.com/openai/openai-agents-python/commit/14d13f468b0da7e6b721379200bd150cea60add1))
> …

### [v1.0.0-alpha.2](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.2) — Agents SDK v1.0.0-alpha.2 _(pre-release)_
<sub>2026-11-23 · today</sub>

> **Agents SDK v1.0.0-alpha.2**
> **Highlights**
> - Resume conversations and pending approvals across workers with Responses or Codex.
> - Recover supported native Codex command and edit approvals.
> - Configure tool execution hooks and filter available function tools.
> - Opt into Runner text redaction and detailed operation tracing with either provider.
> …

### [v1.0.0-alpha.1](https://github.com/openai/openai-agents-python/releases/tag/v1.0.0-alpha.1) — Agents SDK v1.0.0-alpha.1 _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

> **Agents SDK v1.0.0-alpha.1**
> This first preview from `feat/simple-codex` adds Codex as an opt-in model provider for the Python Agents SDK. The prebuilt `openai-agents` wheels (version `1.0.0a1`) are available exclusively through GitHub Releases.
> **Highlights**
> - **Choose Codex per run.** Import `CodexProvider` from `agents.models.codex` and create `provider = CodexProvider()`. Pass `RunConfig(model_provider=provider)` to the Runner. Codex uses your saved login. For API key authentication, use `CodexProvider(api_key=...)`. The provider selects the model for agents that use a model name or the default model. [Run the same agent with either provider](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#run-one-agent-with-either-provider)
> - **Reuse Codex Core inside Python.** The wheel embeds unmodified Codex Core `rust-v0.166.0` through PyO3. Direct calls to Core eliminate `codex app-server` startup and JSON-RPC. Reuse the provider to share one `ThreadManager` across calls. Each call gets a fresh thread. Use an SDK session for history and close the provider with `await provider.aclose()` when you finish. [Thread lifetime and history](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#streaming-history-and-cancellation) · [Codex source](https://github.com/openai/codex/commit/6ff1e1ca3b30fc8b914720681fcf5fe62e95f856)
> - **Use SDK tools and approvals.** Stream text, hand off to a specialist, pause for approval before a Python tool runs, and validate typed output. Native commands follow Codex's sandbox and approval settings. A native approval prompt ends the model call. [Execution and approvals](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#configure-execution) · [Supported tools and model settings](https://github.com/openai/openai-agents-python/blob/87e8f533c3b457fe632a5eb38ac42590d7f4d9fc/docs/models/codex.md#supported-features-and-limits)
> …

### [v0.25.0](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0)
<sub>2026-11-18 · 6d ago</sub>

> **[0.25.0](https://github.com/openai/openai-agents-python/compare/v0.24.0...v0.25.0) (2026-11-17)**
> **Key Changes**
> Version 0.25.0 removes the beta Runloop sandbox provider and changes how Pydantic run contexts are checkpointed. Runloop users should preserve their workspace data before switching providers. Applications that share checkpoints across workers should upgrade readers first.
> **Highlights:**
> - Migrate Runloop workloads to another supported sandbox provider, such as Modal, or remain on 0.24.0 while migrating. Provider-specific sessions and snapshots require a separate data migration.
> - Resume nested agent-tool approvals with output guardrails using RunState schema `1.22`. Pydantic checkpoints now preserve default values and in-place edits. Use a custom serializer for process-local resources.
> …

### [v0.24.0-alpha.8](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — Agents SDK v0.24.0-alpha.8 _(pre-release)_
<sub>2026-11-16 · 8d ago</sub>

> **Agents SDK v0.24.0-alpha.8**
> **Highlights**
> - **Approve Python tool calls before they run.** Review the arguments and approve or reject the call. You can remember a decision for the rest of the Session. [Managed approval example](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/managed_approvals/README.md#inspect-and-decide)
> - **Connect your own model client.** The native tool loop works with async Responses and Chat Completions clients, LiteLLM, AnyLLM, and custom adapters. [Application-owned model clients](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/docs/sdk/models.md#use-an-application-owned-model-client)
> - **Add Realtime voice to a Session.** Use a server WebSocket, connect a browser over WebRTC, or attach to an existing SIP call. [Realtime connection options](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/native_voice.md#choose-a-connection)
> - **Resume more kinds of work.** Save supported pending tool requests and approvals. Request and token budgets keep the usage already spent when you restore a supported checkpoint. [Restore a checkpoint with a budget](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/budgeted-recovery.md)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [fix(deps): update openai requirement from <4,>=3.48.0 to >=3.52.0,<4 …](https://github.com/openai/openai-agents-python/commit/4e162c79a4a951c6fc8b698d5c8279c1963c099b) | dependabot[bot] |
| 2026-11-24 | [fix(deps): update httpx2 requirement from >=2.16.0 to >=2.16.2 in /ex…](https://github.com/openai/openai-agents-python/commit/0d10b5d5a619103b0c2256c596816b74dbdd1aa4) | dependabot[bot] |
| 2026-11-24 | [fix(deps): update python-multipart requirement from >=0.0.33 to >=0.0…](https://github.com/openai/openai-agents-python/commit/1b56a403b8e2e8dcc86c50717226f841c4d3062e) | dependabot[bot] |
| 2026-11-24 | [fix(deps): update httpx2 requirement from >=2.16.0 to >=2.16.2 in /ex…](https://github.com/openai/openai-agents-python/commit/cd68216a09844ba37fc5e0bcaf56a07121ae251c) | dependabot[bot] |
| 2026-11-24 | [Skip sandbox resume keys when sandboxing is disabled (#6188)](https://github.com/openai/openai-agents-python/commit/3814f975652e9f4d20c44d58ce1ee88714af0423) | markstuart-oai |
| 2026-11-24 | [Compute agent identity sort keys only for duplicate names (#6184)](https://github.com/openai/openai-agents-python/commit/c061d7e86758ae6c018f072cc333e36857c48bb8) | markstuart-oai |
| 2026-11-24 | [Skip container checks for plain strings in conversation history (#6183)](https://github.com/openai/openai-agents-python/commit/5b6b2a0f9415d57ab4ac3f76097400857f9edc47) | markstuart-oai |
| 2026-11-24 | [Reduce peak memory during SQLite session writes (#6186)](https://github.com/openai/openai-agents-python/commit/aea96a6dbe636d8d6b704c5a397aa53ce02b3e7a) | markstuart-oai |
| 2026-11-24 | [Avoid repeated identity scans for initial conversation inputs (#6187)](https://github.com/openai/openai-agents-python/commit/3a09bc1b3cb8c65091a00fb66d32df223a3730ba) | markstuart-oai |
| 2026-11-24 | [release: 0.26.0 (#6069)](https://github.com/openai/openai-agents-python/commit/0ad2d63a9371a23333a95ea6878141a826c9cdda) | openai-sdks[bot] |

[See all commits ↗](https://github.com/openai/openai-agents-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/openai-agents-python.git
```
