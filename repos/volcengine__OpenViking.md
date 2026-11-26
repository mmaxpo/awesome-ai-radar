# volcengine/OpenViking

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/volcengine/OpenViking)

> Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | Context database for agents: memory + RAG + skills |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 42.9k |
| 🍴 **Forks** | 3.6k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 11% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 434.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.6-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.6-preview) — OpenViking SuperAgent 0.5.6-preview _(pre-release)_
<sub>2026-11-25 · yesterday</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.6-preview/install.sh | sh -s -- --version 0.5.6-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21)
<sub>2026-11-24 · 2d ago</sub>

> _No notes._

### [cli@0.5.4](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.4)
<sub>2026-11-24 · 2d ago</sub>

> _No notes._

### [v0.5.6](https://github.com/volcengine/OpenViking/releases/tag/v0.5.6)
<sub>2026-11-24 · 2d ago</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 持久化覆盖 Account、Task/Work 和 Watch**：`account_store.provider`、`storage.task_store.provider`、`storage.watch_store.provider` 均可设为 `postgres`，多进程和多节点部署可在不依赖 Redis 的情况下共享账户、用户、API Key、任务、工作记录与 Watch 状态。三个 Store 独立配置，也继续支持原有 File、SQLite、MySQL 等后端。[#7514](https://github.com/volcengine/OpenViking/pull/7514)、[#7552](https://github.com/volcengine/OpenViking/pull/7552)、[#7568](https://github.com/volcengine/OpenViking/pull/7568)、[#7968](https://github.com/volcengine/OpenViking/pull/7968)
> - **QueueFS 任务顺序与恢复**：后台消息新增按目标串行和按组固定处理归属的调度能力。External、Compile 和 Memory 任务在忙碌、重试、取消与进程恢复时保留原消息及顺序，SessionCommit 会等待已接受的记忆批次真正落稳后再确认队列消息。[#7584](https://github.com/volcengine/OpenViking/pull/7584)、[#7606](https://github.com/volcengine/OpenViking/pull/7606)、[#7531](https://github.com/volcengine/OpenViking/pull/7531)
> - **Compile 配置、执行与快照分离**：Compile 现在以 `compile_name` 管理持久配置，每次执行使用独立任务 ID、冻结输入、增量基线和 Git 快照；复杂模式改为隔离的 Markdown 文件 worker，VikingBot 另增简单编译模式。配置、定时触发、运行、输出和回滚的职责更清楚。[#7737](https://github.com/volcengine/OpenViking/pull/7737)、[#7682](https://github.com/volcengine/OpenViking/pull/7682)、[#7657](https://github.com/volcengine/OpenViking/pull/7657)
> - **Privacy 安全执行外部命令**：新增 `ov privacy run`，可在环境变量、env 文件或命令参数中解析 `{{ov_privacy:...}}` 引用，并在子进程标准输出和错误输出中重新遮蔽敏感值；解析失败时不会启动子进程。隐私检测也统一了匹配逻辑并减少误报。[#7760](https://github.com/volcengine/OpenViking/pull/7760)、[#7458](https://github.com/volcengine/OpenViking/pull/7458)
> …

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 7d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(snapshot-log): isolate sqlite/mysql index by service_name (#8452)](https://github.com/volcengine/OpenViking/commit/fe354f744a74affcbd85a0c88f1c0b600bcc6ec6) | baojun-zhang |
| 2026-11-26 | [fix(task): make periodic task history cleanup configurable (#8469)](https://github.com/volcengine/OpenViking/commit/2faf02a617a205b2652deeea9683dcbe17b50209) | fujiajie666 |
| 2026-11-26 | [feat(gateway): seal secrets out of model requests and unseal tool cal…](https://github.com/volcengine/OpenViking/commit/35dfb20d5390d2916a9b43a0b07741613bd7a640) | t0saki |
| 2026-11-26 | [feat(plugins): seal secrets in Claude Code and pi (#8445)](https://github.com/volcengine/OpenViking/commit/659a0271298c62b7575da3c02aa4b7fee588b52d) | t0saki |
| 2026-11-26 | [feat(gateway,plugins): one table for the server features clients depe…](https://github.com/volcengine/OpenViking/commit/019b351bf3e2a872fdfa65de6482537314f0853b) | t0saki |
| 2026-11-26 | [feat(privacy): seal endpoint, auto-enrolled credentials and reference…](https://github.com/volcengine/OpenViking/commit/83afb6d3b76523505d20a29906f19be2c02f5122) | t0saki |
| 2026-11-26 | [feat(pdf): prefer a configured remote parser in auto, add hosted Mine…](https://github.com/volcengine/OpenViking/commit/3e67888a92643d5587b32b2595bd5cb315e4f9ee) | q2000s |
| 2026-11-26 | [feat(compile): limit source directories to 100 (#8520)](https://github.com/volcengine/OpenViking/commit/27beb0a3f649315f35bb20cc5af71e9456ffdcd6) | fujiajie666 |
| 2026-11-26 | [feat(expiry)!: use CacheRuntime for distributed scheduling (#8270)](https://github.com/volcengine/OpenViking/commit/326d2d54b4b7e56fb0a5deb6b26116b1d96c8aa7) | baojun-zhang |
| 2026-11-26 | [fix(claude-code-plugin): honor skipSubagentSessions in subagent hooks…](https://github.com/volcengine/OpenViking/commit/52269f89ed83515cd24823d51ac9b8651aeb5e7c) | diaozxin007 |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
