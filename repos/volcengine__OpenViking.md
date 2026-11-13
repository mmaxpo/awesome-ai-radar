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
| ⭐ **Stars** | 42.2k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 65% · TypeScript 16% · Rust 11% · JavaScript 2% · MDX 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 415.8 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — openviking-sdk 0.1.20
<sub>2026-11-12 · yesterday</sub>

> **更新**
> - 支持上下文使用次数与最近使用时间标签更新
> - 支持批量设置上下文标签
> - 支持 Python 同步与异步客户端调用 `batch_set_tags`

### [openviking-superagent@0.5.2-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.2-preview) — OpenViking SuperAgent 0.5.2-preview _(pre-release)_
<sub>2026-11-11 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.2-preview/install.sh | sh -s -- --version 0.5.2-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [v0.5.4.1](https://github.com/volcengine/OpenViking/releases/tag/v0.5.4.1)
<sub>2026-11-11 · 2d ago</sub>

> **中文**
> **修复与改进**
> - **资源 write**：修正文件处理与父目录刷新的衔接，保留每个文件自身的摘要和索引工作；父目录独立刷新，不替代尚未完成的文件索引。`wait=true` 等待文件自身的处理完成，不等待父目录 L0/L1 和目录索引刷新，请求参数不变。[#7383](https://github.com/volcengine/OpenViking/pull/7383)
> - **目录摘要**：待刷新期间复用已有文件摘要；恢复 `semantic.overview_sample_limit` 默认 32 项的稳定采样，文件自身仍完整建立索引。[#7380](https://github.com/volcengine/OpenViking/pull/7380)、[#7387](https://github.com/volcengine/OpenViking/pull/7387)
> - **存储稳定性**：修复 `stat` 按记录 ID 查询的兼容性、向量 Collection 生命周期，以及多写元数据不完整时的启动问题。[#7377](https://github.com/volcengine/OpenViking/pull/7377)、[#7355](https://github.com/volcengine/OpenViking/pull/7355)、[#7381](https://github.com/volcengine/OpenViking/pull/7381)
> - **Connector 与流式响应**：支持带作用域的 OAuth 引用，原生导入保留 Connector Watch；修复 Gateway 流式错误的结束标记。[#7259](https://github.com/volcengine/OpenViking/pull/7259)、[#7364](https://github.com/volcengine/OpenViking/pull/7364)、[#7010](https://github.com/volcengine/OpenViking/pull/7010)
> …

### [openviking-superagent@0.5.1-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.1-preview) — OpenViking SuperAgent 0.5.1-preview _(pre-release)_
<sub>2026-11-10 · 3d ago</sub>

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
| 2026-11-13 | [feat(account): support PostgreSQL as an account store (#7514)](https://github.com/volcengine/OpenViking/commit/40fd42f105388410b016eaa2d4a04e5afa1bf785) | zhanglistar |
| 2026-11-13 | [fix(react): reveal directory summary links at the requested level (#7…](https://github.com/volcengine/OpenViking/commit/26f35c6626f8aea73df2acf8f6016723e5efab80) | LaamGinghong |
| 2026-11-13 | [fix(react): align the file browser search dialog with the console des…](https://github.com/volcengine/OpenViking/commit/cf14a0cbe5cde0e89e7de9eb6265bf086415fde0) | LaamGinghong |
| 2026-11-13 | [feat(react): add bilingual release notes and align demo controls (#7578)](https://github.com/volcengine/OpenViking/commit/9a22056d7041bcc7c7c5411312e1f73c204517fd) | LaamGinghong |
| 2026-11-13 | [fix(git): replace source markers consistently (#7589)](https://github.com/volcengine/OpenViking/commit/ce2280a762c8280ce41b0be3f512f7ee4b7f6d80) | qin-ctx |
| 2026-11-13 | [fix(claude-plugin): capture the final answer missing from the transcr…](https://github.com/volcengine/OpenViking/commit/7fe0f92bdb8481b34e7ce7706e943780fc6e0fa2) | t0saki |
| 2026-11-13 | [fix(opencode): load bundled skills on OpenCode v2 and run v2 prompt c…](https://github.com/volcengine/OpenViking/commit/297847cddb0ca311f2e205f0a7773639593f7916) | t0saki |
| 2026-11-13 | [fix(react): keep the quick command tooltip when the description is tr…](https://github.com/volcengine/OpenViking/commit/dbb224282bdfdfa12fcfc1bdd8c94672c2004720) | LaamGinghong |
| 2026-11-13 | [feat(dsh): let a workspace opt out of memory with enabled: false (#7482)](https://github.com/volcengine/OpenViking/commit/87be17c2512886db6109a940ced5942d2956f0ba) | dongasai |
| 2026-11-13 | [test(docs): count the live context walkthrough in the onboarding cata…](https://github.com/volcengine/OpenViking/commit/773bc17203706eef845023d1aca8ff9174d224a1) | t0saki |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
