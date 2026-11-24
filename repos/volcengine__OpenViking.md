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
| ⭐ **Stars** | 42.7k |
| 🍴 **Forks** | 3.6k |
| 🐞 **Open issues + PRs** | [1.7k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 11% · JavaScript 5% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 433.7 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [python-sdk@0.1.21](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.21)
<sub>2026-11-24 · today</sub>

> _No notes._

### [cli@0.5.4](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.4)
<sub>2026-11-24 · today</sub>

> _No notes._

### [v0.5.6](https://github.com/volcengine/OpenViking/releases/tag/v0.5.6)
<sub>2026-11-24 · today</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 持久化覆盖 Account、Task/Work 和 Watch**：`account_store.provider`、`storage.task_store.provider`、`storage.watch_store.provider` 均可设为 `postgres`，多进程和多节点部署可在不依赖 Redis 的情况下共享账户、用户、API Key、任务、工作记录与 Watch 状态。三个 Store 独立配置，也继续支持原有 File、SQLite、MySQL 等后端。[#7514](https://github.com/volcengine/OpenViking/pull/7514)、[#7552](https://github.com/volcengine/OpenViking/pull/7552)、[#7568](https://github.com/volcengine/OpenViking/pull/7568)、[#7968](https://github.com/volcengine/OpenViking/pull/7968)
> - **QueueFS 任务顺序与恢复**：后台消息新增按目标串行和按组固定处理归属的调度能力。External、Compile 和 Memory 任务在忙碌、重试、取消与进程恢复时保留原消息及顺序，SessionCommit 会等待已接受的记忆批次真正落稳后再确认队列消息。[#7584](https://github.com/volcengine/OpenViking/pull/7584)、[#7606](https://github.com/volcengine/OpenViking/pull/7606)、[#7531](https://github.com/volcengine/OpenViking/pull/7531)
> - **Compile 配置、执行与快照分离**：Compile 现在以 `compile_name` 管理持久配置，每次执行使用独立任务 ID、冻结输入、增量基线和 Git 快照；复杂模式改为隔离的 Markdown 文件 worker，VikingBot 另增简单编译模式。配置、定时触发、运行、输出和回滚的职责更清楚。[#7737](https://github.com/volcengine/OpenViking/pull/7737)、[#7682](https://github.com/volcengine/OpenViking/pull/7682)、[#7657](https://github.com/volcengine/OpenViking/pull/7657)
> - **Privacy 安全执行外部命令**：新增 `ov privacy run`，可在环境变量、env 文件或命令参数中解析 `{{ov_privacy:...}}` 引用，并在子进程标准输出和错误输出中重新遮蔽敏感值；解析失败时不会启动子进程。隐私检测也统一了匹配逻辑并减少误报。[#7760](https://github.com/volcengine/OpenViking/pull/7760)、[#7458](https://github.com/volcengine/OpenViking/pull/7458)
> …

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 5d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — @openviking/react 0.2.0
<sub>2026-11-19 · 5d ago</sub>

> **en-US**
> **Minor Changes**
> - 609baba: Let FileBrowser hosts load experience metrics and override individual experience dashboard sections.
> - 704bec6: Add optional FileBrowser props for hosts to save and restore expanded folders independently of the selected resource.
>   Hosts can also persist explicit collapses across mounts when home alias resolution is temporarily unavailable.
> **Patch Changes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [fix(acl): restore empty-string grant decoding (#8371)](https://github.com/volcengine/OpenViking/commit/e13f0441eaf2a1beacba9002b5720aeb8bae970e) | chuanbao666 |
| 2026-11-24 | [fix(react): 保持未知预览类型并修复前端测试 (#8369)](https://github.com/volcengine/OpenViking/commit/6b42f562583c132deb09a61cea57e02573f9f094) | cocolord |
| 2026-11-24 | [test(react): 修复当前用户目录展开测试卡死 (#8367)](https://github.com/volcengine/OpenViking/commit/0a4e2d46fc6acec09496b2dfda8ca625b7d9c16c) | cocolord |
| 2026-11-24 | [fix(compile): 修复增量编译漏处理和重复执行 (#7813)](https://github.com/volcengine/OpenViking/commit/dfad651fee8fede13dda3915477a452e1b31032a) | cocolord |
| 2026-11-24 | [feat(parse): forward Feishu nested import options to Understanding AP…](https://github.com/volcengine/OpenViking/commit/6ebab8e04d2afc544ec487d177e65a3e04c37a8d) | ShaoZegangByte |
| 2026-11-24 | [fix(docker): 移除已删除的 redis-mysql 构建依赖 (#8347)](https://github.com/volcengine/OpenViking/commit/39db38ac3c7f726f87b7f08e5488739ff6c24313) | qin-ctx |
| 2026-11-24 | [test(client): 精简 Python HTTP 客户端契约测试 (#8343)](https://github.com/volcengine/OpenViking/commit/0c826b74a39f74fe2089bec4bf97172d90e2640f) | qin-ctx |
| 2026-11-24 | [fix(auth): 将 OIDC 验签迁移到 PyJWT (#8330)](https://github.com/volcengine/OpenViking/commit/d925c6e7f922264f18c88d9f5e9942b5e2939e33) | qin-ctx |
| 2026-11-24 | [test(server): 梳理服务端业务模块单测 (#8300)](https://github.com/volcengine/OpenViking/commit/0b19c82840c7a456e20a127f1447fd3eb7e8bb7a) | qin-ctx |
| 2026-11-24 | [test(observability): 精简接入与可观测性契约测试 (#8301)](https://github.com/volcengine/OpenViking/commit/d2f47ca74ec8e5c945e9ebfc31926aaa503bc185) | qin-ctx |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
