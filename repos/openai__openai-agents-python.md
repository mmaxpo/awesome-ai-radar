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
| ⭐ **Stars** | 30.7k |
| 🍴 **Forks** | 5.1k |
| 🐞 **Open issues + PRs** | [37](https://github.com/openai/openai-agents-python/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `framework` `llm` `python` `openai` `harness` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2025-03-11 |
| 📦 **Latest release** | [v0.25.0](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 124.2 MB |
| 🌐 **Website** | https://openai.github.io/openai-agents-python/ |

## 📦 Recent releases

### [v0.25.0](https://github.com/openai/openai-agents-python/releases/tag/v0.25.0)
<sub>2026-11-18 · today</sub>

> **[0.25.0](https://github.com/openai/openai-agents-python/compare/v0.24.0...v0.25.0) (2026-11-17)**
> **Features**
> * expose utilities for third-party session adapters ([#5428](https://github.com/openai/openai-agents-python/issues/5428)) ([16fdb20](https://github.com/openai/openai-agents-python/commit/16fdb2091d0b18cc1200d26ba6a20ee6f1962455))
> * **sandbox:** remove Runloop provider ([#5369](https://github.com/openai/openai-agents-python/issues/5369)) ([12ce34d](https://github.com/openai/openai-agents-python/commit/12ce34d8438d6f1f7c964a261b89e069e8a0b3d3))
> **Bug Fixes**
> * avoid loading workspace startup files during internal sandbox operations ([#5406](https://github.com/openai/openai-agents-python/pull/5406)) ([841dfdd](https://github.com/openai/openai-agents-python/commit/841dfdd938bfd4ca052475eb76d6245a356868e0))
> …

### [v0.24.0-alpha.8](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — Agents SDK v0.24.0-alpha.8 _(pre-release)_
<sub>2026-11-16 · 2d ago</sub>

> **Agents SDK v0.24.0-alpha.8**
> **Highlights**
> - **Approve Python tool calls before they run.** Review the arguments and approve or reject the call. You can remember a decision for the rest of the Session. [Managed approval example](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/managed_approvals/README.md#inspect-and-decide)
> - **Connect your own model client.** The native tool loop works with async Responses and Chat Completions clients, LiteLLM, AnyLLM, and custom adapters. [Application-owned model clients](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/docs/sdk/models.md#use-an-application-owned-model-client)
> - **Add Realtime voice to a Session.** Use a server WebSocket, connect a browser over WebRTC, or attach to an existing SIP call. [Realtime connection options](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/native_voice.md#choose-a-connection)
> - **Resume more kinds of work.** Save supported pending tool requests and approvals. Request and token budgets keep the usage already spent when you restore a supported checkpoint. [Restore a checkpoint with a budget](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/budgeted-recovery.md)
> …

### [v0.24.0-alpha.7](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — Agents SDK v0.24.0-alpha.7 _(pre-release)_
<sub>2026-11-08 · 10d ago</sub>

> **Agents SDK v0.24.0-alpha.7**
> **Highlights**
> - **Use Classic workflows alongside native execution.** Import the retained v0 runtime through `agents.classic`. This alpha also changes executor write defaults; review the upgrade actions before opening existing environments.
> - **Keep conversations in your own storage.** Add durable root Sessions with `CustomStorage`, and reconcile uncertain tool effects before resuming work.
> - **Add voice and hosted tools to native agents.** Connect speech workflows to a Session, or use `FileSearch`, `CodeInterpreter`, and `ImageGeneration` through compatible Responses providers.
> - **Control context, completion, and usage.** Transform model input, retain selected context during compaction, review proposed answers, and limit observed root usage.
> …

### [v0.24.0-alpha.6](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — Agents SDK v0.24.0-alpha.6 _(pre-release)_
<sub>2026-11-03 · 14d ago</sub>

> **Install the preview**
> Use standard CPython 3.10–3.14 in a virtual environment. These wheels include the native runtime; no Rust toolchain or source build is needed. This preview is distributed through GitHub Releases, not PyPI.
> Run the command for your platform:
> **Linux x86_64 (glibc 2.39 or newer)**
> ```sh
> python -m pip install "https://github.com/openai/openai-agents-python/releases/download/v0.24.0-alpha.6/openai_agents-0.24.0a6-cp310-abi3-manylinux_2_39_x86_64.whl"
> …

### [v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0)
<sub>2026-10-15 · 1mo ago</sub>

> **[0.24.0](https://github.com/openai/openai-agents-python/compare/v0.23.1...v0.24.0) (2026-10-15)**
> **Features**
> * expose MCP annotations on converted tools ([#5356](https://github.com/openai/openai-agents-python/issues/5356)) ([75813f8](https://github.com/openai/openai-agents-python/commit/75813f83997b249e5f4b53cccaff0d8a03aa179f))
> * support run-wide tool exception formatting ([#5326](https://github.com/openai/openai-agents-python/issues/5326)) ([8fd9a7c](https://github.com/openai/openai-agents-python/commit/8fd9a7cd19a4c495c438d39c83fb03ea3fb5a7e0))
> **Bug Fixes**
> * batch OpenAI conversation session writes within the API limit ([#5334](https://github.com/openai/openai-agents-python/issues/5334)) ([26345c1](https://github.com/openai/openai-agents-python/commit/26345c1e45ebede8e2fc9b0bc7341dedab5e01fc))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix: sandbox memory selection across UTC offsets (#6066)](https://github.com/openai/openai-agents-python/commit/e7ce15a25b336bb3d0840ad16dee597f69a6e6d3) | seratch |
| 2026-11-18 | [fix: support opt-in JSON validation for Codex tool parameters (#6067)](https://github.com/openai/openai-agents-python/commit/54492d112b5c3366cc30f35abd60c46fa92140c2) | seratch |
| 2026-11-18 | [fix: allow SDK 0.25 in the external provider example (#6068)](https://github.com/openai/openai-agents-python/commit/9b17858afb5b45f48bbf695cc7c8f34778425156) | jbeckwith-oai |
| 2026-11-18 | [release: 0.25.0 (#5394)](https://github.com/openai/openai-agents-python/commit/0a74177ed23ffb0c2dba24eda3fb12fb58e3e09d) | openai-sdks[bot] |
| 2026-11-17 | [fix: limit the Daytona extra to the supported 0.x SDK (#6065)](https://github.com/openai/openai-agents-python/commit/fd78fa038f853598ed849e25eec78bab1e49aa00) | seratch |
| 2026-11-17 | [fix: align model defaults with TS SDK (#6064)](https://github.com/openai/openai-agents-python/commit/d5287b741dfd93de3ce1625f98b342cd0c4c455e) | seratch |
| 2026-11-17 | [fix(deps): bump openai from 3.29.0 to 3.48.0 (#6054)](https://github.com/openai/openai-agents-python/commit/a4a4fa4cf0e34516df57871196de360253e614fe) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update fastapi requirement from >=0.162.0 to >=0.162.2 in …](https://github.com/openai/openai-agents-python/commit/9a3bce3d0ab013d64aa5591e92a4458d1c658f8b) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update openai requirement from <4,>=3.42.1 to >=3.48.0,<4 …](https://github.com/openai/openai-agents-python/commit/5e0f94458e91eb93f619b29045f7a2ebcc1f4f3e) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update twilio requirement from <10,>=9.12.0 to >=9.13.0,<1…](https://github.com/openai/openai-agents-python/commit/e27451cdb311b389bfbf3860106abe0991cbb641) | dependabot[bot] |

[See all commits ↗](https://github.com/openai/openai-agents-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/openai-agents-python.git
```
