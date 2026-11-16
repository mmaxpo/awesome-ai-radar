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
| 🐞 **Open issues + PRs** | [46](https://github.com/openai/openai-agents-python/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `framework` `llm` `python` `openai` `harness` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2025-03-11 |
| 📦 **Latest release** | [v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) — 2026-10-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 118.5 MB |
| 🌐 **Website** | https://openai.github.io/openai-agents-python/ |

## 📦 Recent releases

### [v0.24.0-alpha.8](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.8) — Agents SDK v0.24.0-alpha.8 _(pre-release)_
<sub>2026-11-16 · today</sub>

> **Agents SDK v0.24.0-alpha.8**
> **Highlights**
> - **Approve Python tool calls before they run.** Review the arguments and approve or reject the call. You can remember a decision for the rest of the Session. [Managed approval example](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/managed_approvals/README.md#inspect-and-decide)
> - **Connect your own model client.** The native tool loop works with async Responses and Chat Completions clients, LiteLLM, AnyLLM, and custom adapters. [Application-owned model clients](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/docs/sdk/models.md#use-an-application-owned-model-client)
> - **Add Realtime voice to a Session.** Use a server WebSocket, connect a browser over WebRTC, or attach to an existing SIP call. [Realtime connection options](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/native_voice.md#choose-a-connection)
> - **Resume more kinds of work.** Save supported pending tool requests and approvals. Request and token budgets keep the usage already spent when you restore a supported checkpoint. [Restore a checkpoint with a budget](https://github.com/openai/openai-agents-python/blob/d6a81c997eabdc56108633eb3132fb3907f87d7e/examples/codex/budgeted-recovery.md)
> …

### [v0.24.0-alpha.7](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.7) — Agents SDK v0.24.0-alpha.7 _(pre-release)_
<sub>2026-11-08 · 8d ago</sub>

> **Agents SDK v0.24.0-alpha.7**
> **Highlights**
> - **Use Classic workflows alongside native execution.** Import the retained v0 runtime through `agents.classic`. This alpha also changes executor write defaults; review the upgrade actions before opening existing environments.
> - **Keep conversations in your own storage.** Add durable root Sessions with `CustomStorage`, and reconcile uncertain tool effects before resuming work.
> - **Add voice and hosted tools to native agents.** Connect speech workflows to a Session, or use `FileSearch`, `CodeInterpreter`, and `ImageGeneration` through compatible Responses providers.
> - **Control context, completion, and usage.** Transform model input, retain selected context during compaction, review proposed answers, and limit observed root usage.
> …

### [v0.24.0-alpha.6](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0-alpha.6) — Agents SDK v0.24.0-alpha.6 _(pre-release)_
<sub>2026-11-03 · 12d ago</sub>

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
| 2026-11-11 | [fix(deps): update python-multipart requirement from >=0.0.32 to >=0.0…](https://github.com/openai/openai-agents-python/commit/64fbde5d02b42ae5f9db668eb0184cdb3fc9d775) | dependabot[bot] |
| 2026-11-10 | [docs: update translated pages (#5388)](https://github.com/openai/openai-agents-python/commit/d68961657843c7d81dfc25834484f8aac2957eb3) | seratch |
| 2026-11-10 | [fix(deps-dev): bump pytest from 9.0.3 to 9.2.0 (#5710)](https://github.com/openai/openai-agents-python/commit/b0051a736fec104ee8b4d254de3e0c13758ecaec) | dependabot[bot] |
| 2026-11-09 | [fix: use gpt-6-luna for session compaction by default (#5646)](https://github.com/openai/openai-agents-python/commit/1fc77bbc8ac1446690f6ba62dd0d52779bdcf43f) | seratch |
| 2026-11-09 | [fix: skip streamed model attempts after an input guardrail trips (#5644)](https://github.com/openai/openai-agents-python/commit/8ea4333b4f223340739c3039e1a7720082493580) | seratch |
| 2026-11-09 | [fix: retain tool guardrail results after approval and resume (#5643)](https://github.com/openai/openai-agents-python/commit/3a0c89c8e4ac42fe4134695d3ca5d0275f138f06) | seratch |
| 2026-11-09 | [fix: preserve append order in SQLAlchemy sessions (#5645)](https://github.com/openai/openai-agents-python/commit/89a3ea4b279925d9d7720027dc872eeba6925224) | seratch |
| 2026-11-09 | [fix: allow concurrent Streamable HTTP requests on MCP v2 (#5641)](https://github.com/openai/openai-agents-python/commit/2b90566eb2adc7d94e8fd8f234b007a937a98989) | seratch |
| 2026-11-09 | [docs: clarify forced tool choice for read-only requests (#5640)](https://github.com/openai/openai-agents-python/commit/21ec412130103e7ffcc3fdf4c1368caba7fe9fe1) | seratch |
| 2026-11-09 | [fix: Responses tool choice for functions named after hosted tools (#5…](https://github.com/openai/openai-agents-python/commit/3ac005f29919210f9c3f78668008477497c0d0ea) | seratch |

[See all commits ↗](https://github.com/openai/openai-agents-python/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/openai-agents-python.git
```
