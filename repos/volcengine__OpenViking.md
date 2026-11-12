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
| ⭐ **Stars** | 42.1k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 66% · TypeScript 16% · Rust 11% · MDX 2% · JavaScript 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 414.6 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — openviking-sdk 0.1.20
<sub>2026-11-12 · today</sub>

> **更新**
> - 支持上下文使用次数与最近使用时间标签更新
> - 支持批量设置上下文标签
> - 支持 Python 同步与异步客户端调用 `batch_set_tags`

### [openviking-superagent@0.5.2-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.2-preview) — OpenViking SuperAgent 0.5.2-preview _(pre-release)_
<sub>2026-11-11 · yesterday</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.2-preview/install.sh | sh -s -- --version 0.5.2-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [v0.5.4.1](https://github.com/volcengine/OpenViking/releases/tag/v0.5.4.1)
<sub>2026-11-11 · yesterday</sub>

> **中文**
> **修复与改进**
> - **资源 write**：修正文件处理与父目录刷新的衔接，保留每个文件自身的摘要和索引工作；父目录独立刷新，不替代尚未完成的文件索引。`wait=true` 等待文件自身的处理完成，不等待父目录 L0/L1 和目录索引刷新，请求参数不变。[#7383](https://github.com/volcengine/OpenViking/pull/7383)
> - **目录摘要**：待刷新期间复用已有文件摘要；恢复 `semantic.overview_sample_limit` 默认 32 项的稳定采样，文件自身仍完整建立索引。[#7380](https://github.com/volcengine/OpenViking/pull/7380)、[#7387](https://github.com/volcengine/OpenViking/pull/7387)
> - **存储稳定性**：修复 `stat` 按记录 ID 查询的兼容性、向量 Collection 生命周期，以及多写元数据不完整时的启动问题。[#7377](https://github.com/volcengine/OpenViking/pull/7377)、[#7355](https://github.com/volcengine/OpenViking/pull/7355)、[#7381](https://github.com/volcengine/OpenViking/pull/7381)
> - **Connector 与流式响应**：支持带作用域的 OAuth 引用，原生导入保留 Connector Watch；修复 Gateway 流式错误的结束标记。[#7259](https://github.com/volcengine/OpenViking/pull/7259)、[#7364](https://github.com/volcengine/OpenViking/pull/7364)、[#7010](https://github.com/volcengine/OpenViking/pull/7010)
> …

### [openviking-superagent@0.5.1-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.1-preview) — OpenViking SuperAgent 0.5.1-preview _(pre-release)_
<sub>2026-11-10 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.1-preview/install.sh | sh -s -- --version 0.5.1-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [openviking-vika@0.5.0-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-vika%400.5.0-preview) — Vika 0.5.0-preview _(pre-release)_
<sub>2026-11-09 · 3d ago</sub>

> Install this version: `curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/vika/releases/0.5.0-preview/install.sh | sh -s -- --version 0.5.0-preview`

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [fix(react): use icon-only VikingBot message copy buttons (#7523)](https://github.com/volcengine/OpenViking/commit/51f0e8e262060e95a897e8480fa9fa47652f75ed) | LaamGinghong |
| 2026-11-12 | [fix(observability): 从 ov.conf 读取 Kafka 上报配置 (#7491)](https://github.com/volcengine/OpenViking/commit/5a212c28b53377ba51c4e78615781d480d5d19ca) | dingerchen |
| 2026-11-12 | [feat(user): 支持按配置预置 GLOBAL_POLICY.md (#7512)](https://github.com/volcengine/OpenViking/commit/522f4df0e4fd264fe19dabda72c218b900d91b5a) | qin-ctx |
| 2026-11-12 | [feat(skills): remove update backups and rollback (#7509)](https://github.com/volcengine/OpenViking/commit/9b16802008a9fe8edf7fc40877dca4bdf02af0b9) | yeshion23333 |
| 2026-11-12 | [feat(react): add headless VikingBot module and Console chat (#7510)](https://github.com/volcengine/OpenViking/commit/b2d7169caccf92ff06cfe21d46d47806282b89ef) | LaamGinghong |
| 2026-11-12 | [feat(react): implement the file browser search with four retrieval mo…](https://github.com/volcengine/OpenViking/commit/bcdaac0cedba25db3b63763dcfc8d3b80b692cbd) | LaamGinghong |
| 2026-11-12 | [feat(react)!: rename public components and rewrite frontend docs (#7506)](https://github.com/volcengine/OpenViking/commit/1f1fa7e273053fef386c94a964b0a3fac943f93b) | yufeng201 |
| 2026-11-12 | [fix(react): filter internal metadata in FileBrowser text reads (#7490)](https://github.com/volcengine/OpenViking/commit/ea5baaaa376763fe217e4e0f4f7ef18c0bd40fcb) | LaamGinghong |
| 2026-11-12 | [fix(parse): resolve bookmark links found inside notes in AnyDoc outpu…](https://github.com/volcengine/OpenViking/commit/82ec6d10bcf9e4dfcf8c2c39881d5c71a43df6fb) | umeGe |
| 2026-11-12 | [docs(config): explain Responses authentication with API keys (#7314)](https://github.com/volcengine/OpenViking/commit/4792249144cf82183e483c974cb85938793d4130) | r266-tech |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
