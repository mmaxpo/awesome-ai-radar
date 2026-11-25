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
| ⭐ **Stars** | 42.8k |
| 🍴 **Forks** | 3.6k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 11% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 433.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.6-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.6-preview) — OpenViking SuperAgent 0.5.6-preview _(pre-release)_
<sub>2026-11-25 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.6-preview/install.sh | sh -s -- --version 0.5.6-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21)
<sub>2026-11-24 · yesterday</sub>

> _No notes._

### [cli@0.5.4](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.4)
<sub>2026-11-24 · yesterday</sub>

> _No notes._

### [v0.5.6](https://github.com/volcengine/OpenViking/releases/tag/v0.5.6)
<sub>2026-11-24 · yesterday</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 持久化覆盖 Account、Task/Work 和 Watch**：`account_store.provider`、`storage.task_store.provider`、`storage.watch_store.provider` 均可设为 `postgres`，多进程和多节点部署可在不依赖 Redis 的情况下共享账户、用户、API Key、任务、工作记录与 Watch 状态。三个 Store 独立配置，也继续支持原有 File、SQLite、MySQL 等后端。[#7514](https://github.com/volcengine/OpenViking/pull/7514)、[#7552](https://github.com/volcengine/OpenViking/pull/7552)、[#7568](https://github.com/volcengine/OpenViking/pull/7568)、[#7968](https://github.com/volcengine/OpenViking/pull/7968)
> - **QueueFS 任务顺序与恢复**：后台消息新增按目标串行和按组固定处理归属的调度能力。External、Compile 和 Memory 任务在忙碌、重试、取消与进程恢复时保留原消息及顺序，SessionCommit 会等待已接受的记忆批次真正落稳后再确认队列消息。[#7584](https://github.com/volcengine/OpenViking/pull/7584)、[#7606](https://github.com/volcengine/OpenViking/pull/7606)、[#7531](https://github.com/volcengine/OpenViking/pull/7531)
> - **Compile 配置、执行与快照分离**：Compile 现在以 `compile_name` 管理持久配置，每次执行使用独立任务 ID、冻结输入、增量基线和 Git 快照；复杂模式改为隔离的 Markdown 文件 worker，VikingBot 另增简单编译模式。配置、定时触发、运行、输出和回滚的职责更清楚。[#7737](https://github.com/volcengine/OpenViking/pull/7737)、[#7682](https://github.com/volcengine/OpenViking/pull/7682)、[#7657](https://github.com/volcengine/OpenViking/pull/7657)
> - **Privacy 安全执行外部命令**：新增 `ov privacy run`，可在环境变量、env 文件或命令参数中解析 `{{ov_privacy:...}}` 引用，并在子进程标准输出和错误输出中重新遮蔽敏感值；解析失败时不会启动子进程。隐私检测也统一了匹配逻辑并减少误报。[#7760](https://github.com/volcengine/OpenViking/pull/7760)、[#7458](https://github.com/volcengine/OpenViking/pull/7458)
> …

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 6d ago</sub>

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
| 2026-11-25 | [feat(taskstore): 默认使用 SQLite 并支持 File 离线迁移 (#8373)](https://github.com/volcengine/OpenViking/commit/af412110b367ec404560629dada718ba1172a1cf) | hezhang-1216 |
| 2026-11-25 | [feat(admin): freeze user agent files through account metadata (#8430)](https://github.com/volcengine/OpenViking/commit/a4b083ea6e8dc12680c817990dd75c1cca2399ae) | MaojiaSheng |
| 2026-11-25 | [feat(plugins): session_history support across the memory plugins and …](https://github.com/volcengine/OpenViking/commit/f905a91ca8ef5fc678c9c4137f7853157552b409) | t0saki |
| 2026-11-25 | [feat(gateway): session_history defaults, hints after a cut and a per-…](https://github.com/volcengine/OpenViking/commit/035eae65139825d1c44e43ce50cde12cc2192f14) | t0saki |
| 2026-11-25 | [feat(session): add session_history, a read-only lookup of a session's…](https://github.com/volcengine/OpenViking/commit/36c829430f4470179d184b535cd626cf4af64a42) | t0saki |
| 2026-11-25 | [docs: add BytePlus managed OpenViking setup (#8319)](https://github.com/volcengine/OpenViking/commit/b2351cd5e19dd4ebe2d57aab2a96f9dbb2af4a12) | ehz0ah |
| 2026-11-25 | [test(frontend): 精简前端与生态测试并集中契约覆盖 (#8370)](https://github.com/volcengine/OpenViking/commit/902913a31dca9dc6d671f3bf33a6daf85ab9177e) | qin-ctx |
| 2026-11-25 | [test(client): 精简跨语言客户端通用契约测试 (#8368)](https://github.com/volcengine/OpenViking/commit/eeb807d0a4cc3017eeca9de39e514ef14533e300) | qin-ctx |
| 2026-11-25 | [refactor: 移除工作区中的 arranger 导航项 (#8439)](https://github.com/volcengine/OpenViking/commit/6f4e51a0b7666bdf1ce4a3bdcfdc39d8d9f3751f) | vikinglbx |
| 2026-11-25 | [feat(gateway): rotate the request log file hourly like the usage log …](https://github.com/volcengine/OpenViking/commit/9e74cd12ea19b89ba48aec36d4c92005451a82d1) | t0saki |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
