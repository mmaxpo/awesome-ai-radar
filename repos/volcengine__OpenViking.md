# volcengine/OpenViking

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/volcengine/OpenViking)

> Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Project** | — |
| **Why I saved it** | Context database for agents: memory + RAG + skills |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 42.0k |
| 🍴 **Forks** | 3.4k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 67% · TypeScript 16% · Rust 11% · JavaScript 1% · C++ 1% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `agent-context` `agent-memory` `agent-plugins` `agentic-rag` `context-database` `dsh-plugin` `knowledge-base` `memory` `memory-management` `self-evolving` `vector-database` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [v0.5.4.1](https://github.com/volcengine/OpenViking/releases/tag/v0.5.4.1) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 410.5 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [v0.5.4.1](https://github.com/volcengine/OpenViking/releases/tag/v0.5.4.1)
<sub>2026-11-11 · today</sub>

> **中文**
> **修复与改进**
> - **资源 write**：修正文件处理与父目录刷新的衔接，保留每个文件自身的摘要和索引工作；父目录独立刷新，不替代尚未完成的文件索引。`wait=true` 等待文件自身的处理完成，不等待父目录 L0/L1 和目录索引刷新，请求参数不变。[#7383](https://github.com/volcengine/OpenViking/pull/7383)
> - **目录摘要**：待刷新期间复用已有文件摘要；恢复 `semantic.overview_sample_limit` 默认 32 项的稳定采样，文件自身仍完整建立索引。[#7380](https://github.com/volcengine/OpenViking/pull/7380)、[#7387](https://github.com/volcengine/OpenViking/pull/7387)
> - **存储稳定性**：修复 `stat` 按记录 ID 查询的兼容性、向量 Collection 生命周期，以及多写元数据不完整时的启动问题。[#7377](https://github.com/volcengine/OpenViking/pull/7377)、[#7355](https://github.com/volcengine/OpenViking/pull/7355)、[#7381](https://github.com/volcengine/OpenViking/pull/7381)
> - **Connector 与流式响应**：支持带作用域的 OAuth 引用，原生导入保留 Connector Watch；修复 Gateway 流式错误的结束标记。[#7259](https://github.com/volcengine/OpenViking/pull/7259)、[#7364](https://github.com/volcengine/OpenViking/pull/7364)、[#7010](https://github.com/volcengine/OpenViking/pull/7010)
> …

### [openviking-superagent@0.5.2-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.2-preview) — OpenViking SuperAgent 0.5.2-preview _(pre-release)_
<sub>2026-11-11 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.2-preview/install.sh | sh -s -- --version 0.5.2-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [openviking-superagent@0.5.1-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.1-preview) — OpenViking SuperAgent 0.5.1-preview _(pre-release)_
<sub>2026-11-10 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.1-preview/install.sh | sh -s -- --version 0.5.1-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [v0.5.4](https://github.com/volcengine/OpenViking/releases/tag/v0.5.4)
<sub>2026-11-09 · yesterday</sub>

> **中文**
> **主要更新**
> - **MCP 与实时上下文**：注册 Streamable HTTP MCP Server，检索、调用工具，并把工具挂载为可读取的 Markdown 节点。提供 REST、CLI 和 SDK 入口；同步上游工具后可查看受影响的挂载。[#6263](https://github.com/volcengine/OpenViking/pull/6263)
> - **Agent 规则查询**：多种 Agent 集成增加 Rule Search 入口，在执行操作前按需查找适用规则。升级插件或重连 MCP 客户端后生效；这不会自动增加每轮拦截。[#7005](https://github.com/volcengine/OpenViking/pull/7005)
> - **Watch 多节点运行**：增加 MySQL Watch 存储和列表分页；Connector 授权撤销后自动暂停，重新授权时只恢复此前自动暂停的任务。[#6756](https://github.com/volcengine/OpenViking/pull/6756)、[#6944](https://github.com/volcengine/OpenViking/pull/6944)
> - **会话恢复与记忆整理**：失败或失去执行任务的归档支持带内容哈希的显式重试；可用 `ov compile memory` 整理当前用户的已有记忆。[#5802](https://github.com/volcengine/OpenViking/pull/5802)、[#6829](https://github.com/volcengine/OpenViking/pull/6829)
> …

### [python-sdk@0.1.19](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.19)
<sub>2026-11-09 · yesterday</sub>

> _No notes._

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [ci(react): automate beta releases and keep stable releases manual (#7445)](https://github.com/volcengine/OpenViking/commit/9dc4922a92f9013f66703aa9846219da43f6e75f) | leowld |
| 2026-11-11 | [refactor(ragfs): modularize git service (#7442)](https://github.com/volcengine/OpenViking/commit/ed624589cd36b6322f648c45ac4cc954bde072d0) | baojun-zhang |
| 2026-11-11 | [fix(cli): honor OPENVIKING_LANG during language initialization (#7439)](https://github.com/volcengine/OpenViking/commit/602c2ec1d532a8a61ec43376206a430bac0641a2) | nocvalight |
| 2026-11-11 | [feat(gateway): let X-OpenViking-Context only narrow tool access (#7446)](https://github.com/volcengine/OpenViking/commit/5c8be88523753dee3b2dfa2ec068fdc95253a7a9) | t0saki |
| 2026-11-11 | [feat(gateway): enable every OpenViking tool by default in context profiles (#7436)](https://github.com/volcengine/OpenViking/commit/d9872afcbb3623ee98685d28d2d3e415d754830a) | t0saki |
| 2026-11-11 | [feat(react): align file previews with console and expose auth forms (#7438)](https://github.com/volcengine/OpenViking/commit/0d3791055b3b83e4ffc4b1fdc965231310f88749) | leowld |
| 2026-11-11 | [fix(react): harden directory tour hydration and positioning (#7344)](https://github.com/volcengine/OpenViking/commit/aeaaa0580ebb9681169468498d302d05c86aa52e) | leowld |
| 2026-11-11 | [feat(ui)!: make WikiDashboard actions host-defined (#7435)](https://github.com/volcengine/OpenViking/commit/e5d8373c1007c5bdcfc287ea7adb92a30964480d) | LaamGinghong |
| 2026-11-11 | [fix(session): preserve delete source links for memory locking (#7384)](https://github.com/volcengine/OpenViking/commit/bfb15baec1a3688333036d9722dc9a2469f5fac6) | yeshion23333 |
| 2026-11-11 | [fix(memory): resolve home URI aliases in read and ls tools (#7417)](https://github.com/volcengine/OpenViking/commit/9879a78d01e71c0f3269466c84d0c1fa2edcc278) | qin-ctx |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## 👥 Top contributors

[qin-ctx](https://github.com/qin-ctx) (333) · [ZaynJarvis](https://github.com/ZaynJarvis) (272) · [t0saki](https://github.com/t0saki) (208) · [zhoujh01](https://github.com/zhoujh01) (174) · [r266-tech](https://github.com/r266-tech) (156)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
