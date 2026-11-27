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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 435.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.6-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.6-preview) — OpenViking SuperAgent 0.5.6-preview _(pre-release)_
<sub>2026-11-25 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.6-preview/install.sh | sh -s -- --version 0.5.6-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21)
<sub>2026-11-24 · 3d ago</sub>

> _No notes._

### [cli@0.5.4](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.4)
<sub>2026-11-24 · 3d ago</sub>

> _No notes._

### [v0.5.6](https://github.com/volcengine/OpenViking/releases/tag/v0.5.6)
<sub>2026-11-24 · 3d ago</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 持久化覆盖 Account、Task/Work 和 Watch**：`account_store.provider`、`storage.task_store.provider`、`storage.watch_store.provider` 均可设为 `postgres`，多进程和多节点部署可在不依赖 Redis 的情况下共享账户、用户、API Key、任务、工作记录与 Watch 状态。三个 Store 独立配置，也继续支持原有 File、SQLite、MySQL 等后端。[#7514](https://github.com/volcengine/OpenViking/pull/7514)、[#7552](https://github.com/volcengine/OpenViking/pull/7552)、[#7568](https://github.com/volcengine/OpenViking/pull/7568)、[#7968](https://github.com/volcengine/OpenViking/pull/7968)
> - **QueueFS 任务顺序与恢复**：后台消息新增按目标串行和按组固定处理归属的调度能力。External、Compile 和 Memory 任务在忙碌、重试、取消与进程恢复时保留原消息及顺序，SessionCommit 会等待已接受的记忆批次真正落稳后再确认队列消息。[#7584](https://github.com/volcengine/OpenViking/pull/7584)、[#7606](https://github.com/volcengine/OpenViking/pull/7606)、[#7531](https://github.com/volcengine/OpenViking/pull/7531)
> - **Compile 配置、执行与快照分离**：Compile 现在以 `compile_name` 管理持久配置，每次执行使用独立任务 ID、冻结输入、增量基线和 Git 快照；复杂模式改为隔离的 Markdown 文件 worker，VikingBot 另增简单编译模式。配置、定时触发、运行、输出和回滚的职责更清楚。[#7737](https://github.com/volcengine/OpenViking/pull/7737)、[#7682](https://github.com/volcengine/OpenViking/pull/7682)、[#7657](https://github.com/volcengine/OpenViking/pull/7657)
> - **Privacy 安全执行外部命令**：新增 `ov privacy run`，可在环境变量、env 文件或命令参数中解析 `{{ov_privacy:...}}` 引用，并在子进程标准输出和错误输出中重新遮蔽敏感值；解析失败时不会启动子进程。隐私检测也统一了匹配逻辑并减少误报。[#7760](https://github.com/volcengine/OpenViking/pull/7760)、[#7458](https://github.com/volcengine/OpenViking/pull/7458)
> …

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 8d ago</sub>

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
| 2026-11-27 | [fix(queuefs): preserve task work consistency on enqueue cancellation …](https://github.com/volcengine/OpenViking/commit/600babf130a8dcb1b2ec811e8211c582ca0ae83b) | Leeminjing |
| 2026-11-27 | [fix(vikingdb): support BytePlus endpoints and STS embeddings (#8569)](https://github.com/volcengine/OpenViking/commit/26dbce367a96f177c67255ad24574780807968f9) | ehz0ah |
| 2026-11-27 | [docs(gateway): end the cache-hit range where memory A is missing (#8590)](https://github.com/volcengine/OpenViking/commit/56e568f4b1e181ac597e465c73e36b59bb9b93dd) | openviking-superagent |
| 2026-11-27 | [fix(snapshot-log)!: limit mysql branches to 128 bytes (#8566)](https://github.com/volcengine/OpenViking/commit/99959ebb5038aba827038b28c430f9e7a9cf2704) | baojun-zhang |
| 2026-11-27 | [fix(snapshot-log)!: scope postgres indexes and use full paths (#8562)](https://github.com/volcengine/OpenViking/commit/bab3333686b7e5adf132ca10a0ba08a9c2857022) | baojun-zhang |
| 2026-11-27 | [fix(ovpack): 修复向量备份校验并补齐 agent/tools 索引 (#8584)](https://github.com/volcengine/OpenViking/commit/7ed0008d802f74dd394b8340e43ca2724b2bac0e) | qin-ctx |
| 2026-11-27 | [feat(privacy): widen built-in detectors with Betterleaks rules and Op…](https://github.com/volcengine/OpenViking/commit/d421d520f5027110792598a44c3c5e17cd23a0d4) | t0saki |
| 2026-11-27 | [feat(pgvector): select native or enhanced search explicitly (#8582)](https://github.com/volcengine/OpenViking/commit/1f19e59b8c07fd9ed98c3780f08af0b2ab3ffe74) | zhanglistar |
| 2026-11-27 | [Revert "fix(ovpack): 修复向量备份校验与目录索引重建 (#8555)" (#8581)](https://github.com/volcengine/OpenViking/commit/e64faf4d298cf7d572709e0a9222cddb31a6cc95) | qin-ctx |
| 2026-11-27 | [fix(ovpack): 修复向量备份校验与目录索引重建 (#8555)](https://github.com/volcengine/OpenViking/commit/219ade00ca180ed00372e8937adeb234844294a7) | qin-ctx |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
