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
| 🐞 **Open issues + PRs** | [36](https://github.com/openai/openai-agents-python/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `framework` `llm` `python` `openai` `harness` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2025-03-11 |
| 📦 **Latest release** | [v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 2026-10-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 122.9 MB |
| 🌐 **Website** | https://openai.github.io/openai-agents-python/ |

## 📦 Recent releases

### [v0.24.0-alpha.8](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — Agents SDK v0.24.0-alpha.8 _(pre-release)_
<sub>2026-11-16 · yesterday</sub>

> **Agents SDK v0.24.0-alpha.8**
> **Highlights**
> - **Approve Python tool calls before they run.** Review the arguments and approve or reject the call. You can remember a decision for the rest of the Session. [Managed approval example](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/managed_approvals/README.md#inspect-and-decide)
> - **Connect your own model client.** The native tool loop works with async Responses and Chat Completions clients, LiteLLM, AnyLLM, and custom adapters. [Application-owned model clients](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/docs/sdk/models.md#use-an-application-owned-model-client)
> - **Add Realtime voice to a Session.** Use a server WebSocket, connect a browser over WebRTC, or attach to an existing SIP call. [Realtime connection options](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/native_voice.md#choose-a-connection)
> - **Resume more kinds of work.** Save supported pending tool requests and approvals. Request and token budgets keep the usage already spent when you restore a supported checkpoint. [Restore a checkpoint with a budget](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/budgeted-recovery.md)
> …

### [v0.24.0-alpha.7](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — Agents SDK v0.24.0-alpha.7 _(pre-release)_
<sub>2026-11-08 · 9d ago</sub>

> **Agents SDK v0.24.0-alpha.7**
> **Highlights**
> - **Use Classic workflows alongside native execution.** Import the retained v0 runtime through `agents.classic`. This alpha also changes executor write defaults; review the upgrade actions before opening existing environments.
> - **Keep conversations in your own storage.** Add durable root Sessions with `CustomStorage`, and reconcile uncertain tool effects before resuming work.
> - **Add voice and hosted tools to native agents.** Connect speech workflows to a Session, or use `FileSearch`, `CodeInterpreter`, and `ImageGeneration` through compatible Responses providers.
> - **Control context, completion, and usage.** Transform model input, retain selected context during compaction, review proposed answers, and limit observed root usage.
> …

### [v0.24.0-alpha.6](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — Agents SDK v0.24.0-alpha.6 _(pre-release)_
<sub>2026-11-03 · 13d ago</sub>

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

### [v0.23.1](https://github.com/openai/openai-agents-python/releases/tag/v0.23.1)
<sub>2026-10-02 · 1mo ago</sub>

> **[0.23.1](https://github.com/openai/openai-agents-python/compare/v0.23.0...v0.23.1) (2026-10-02)**
> **Bug Fixes**
> * restore release tests and refresh required readiness check ([#5278](https://github.com/openai/openai-agents-python/issues/5278)) ([730deb4](https://github.com/openai/openai-agents-python/commit/730deb419c0a2e9e5ebd739499744e4a6bf89ed1))
> **Release readiness review (v0.23.0 -> TARGET 0a5a08b21cd44808d73e8a9e732212dd33b3690d)**
> This is a release readiness report done by `$final-release-review` skill.
> **Diff**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(deps): update fastapi requirement from >=0.162.0 to >=0.162.2 in …](https://github.com/openai/openai-agents-python/commit/9a3bce3d0ab013d64aa5591e92a4458d1c658f8b) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update openai requirement from <4,>=3.42.1 to >=3.48.0,<4 …](https://github.com/openai/openai-agents-python/commit/5e0f94458e91eb93f619b29045f7a2ebcc1f4f3e) | dependabot[bot] |
| 2026-11-17 | [fix(deps): update twilio requirement from <10,>=9.12.0 to >=9.13.0,<1…](https://github.com/openai/openai-agents-python/commit/e27451cdb311b389bfbf3860106abe0991cbb641) | dependabot[bot] |
| 2026-11-17 | [fix(deps-dev): bump fastapi from 0.141.1 to 0.162.2 (#6053)](https://github.com/openai/openai-agents-python/commit/494c0c0c13c8a08c83161848c275365febe90601) | dependabot[bot] |
| 2026-11-17 | [fix(deps-dev): bump rich from 14.3.3 to 15.0.0 (#6055)](https://github.com/openai/openai-agents-python/commit/18d979bf218016a86cbbba1bd38165c87f7c2233) | dependabot[bot] |
| 2026-11-17 | [fix(deps): bump pydantic from 2.14.2 to 2.14.3 (#6052)](https://github.com/openai/openai-agents-python/commit/4bb2637dcdc2c27da7a0d1820d416cb7e0eab4ab) | dependabot[bot] |
| 2026-11-17 | [fix: preserve pending async calls in committed sessions (#6039)](https://github.com/openai/openai-agents-python/commit/f48003a6dba448be21f195c7508ca77e683fe08c) | ashwinnathan-openai |
| 2026-11-17 | [fix: preserve pending input history across streamed retries (#6042)](https://github.com/openai/openai-agents-python/commit/9e05bd5bf299a5ddbb25f7fec8da10bf2baf6133) | ashwinnathan-openai |
| 2026-11-16 | [fix: preserve wire aliases when reading Conversations session history…](https://github.com/openai/openai-agents-python/commit/5789c7c555b5d3e26104859d84286e412d7b6a9b) | seratch |
| 2026-11-16 | [fix: preserve usage from failed and incomplete Responses calls (#6046)](https://github.com/openai/openai-agents-python/commit/6e6707cdcf63c2466f2bc8c6cb026ce3813bdf26) | seratch |

[See all commits ↗](https://github.com/openai/openai-agents-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/openai-agents-python.git
```
