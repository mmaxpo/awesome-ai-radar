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
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 64% · TypeScript 17% · Rust 11% · JavaScript 3% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.1.11](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.11) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 419.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [react@0.1.11](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.11) — @openviking/react 0.1.11
<sub>2026-11-13 · today</sub>

> **en-US**
> **Patch Changes**
> - Add Console mode selection for conversations, commands, or both, plus independent `command.onOpenUri` routing. Track asynchronous tasks across both modes with status snapshots, notifications, and optional query adapters.
> - Recover Console inputs after session creation or delivery failures, preserve undelivered questions, and show theme-aware red error notices without storing client errors in conversation history or sending them to the model.
> - Open `.abstract.md` and `.overview.md` links at their parent directory's L0 and L1 preview. Fix file-only system directory listings by omitting retrieval tags.
> - Align FileBrowser search with the console design, remove the result preview panel, and retain keyboard result navigation. Keep preview bodies mounted across L0/L1/L2 transitions and update the level indicator without flashing the content.
> …

### [cli@0.5.3](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.3)
<sub>2026-11-13 · today</sub>

> _No notes._

### [v0.5.5](https://github.com/volcengine/OpenViking/releases/tag/v0.5.5)
<sub>2026-11-13 · today</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 部署选项**：新增 pgvector 向量后端（`storage.vectordb.backend: "pgvector"`，支持精确检索和 HNSW 检索，需要安装 `openviking[pgvector]`）和 PostgreSQL PathLock（`storage.agfs.pathlock.provider: "postgres"`）。多进程、多主机部署不依赖 Redis，也可以共享向量数据和路径锁租约。[#7516](https://github.com/volcengine/OpenViking/pull/7516)、[#7481](https://github.com/volcengine/OpenViking/pull/7481)
> - **多节点协调**：新增 `storage.agfs.coordination`（`memory` / `sqlite` / `cache`），统一负责 Watch 选主和语义任务版本；只有已持久化的工作才会取代旧任务，按 key 的状态保留一天后过期。[#7466](https://github.com/volcengine/OpenViking/pull/7466)
> - **快照路径历史索引**：`snapshot/log?paths=...` 改用派生索引查找改动过指定路径的提交，默认为 SQLite，多实例部署可选 MySQL，设为 `none` 则保持原来的扫描方式。快照提交、文件内容和 API 响应都不变。[#7505](https://github.com/volcengine/OpenViking/pull/7505)
> - **Gateway Context Profile**：新增 `recall_peer_scope`（`all` / `actor`），可把召回限制在当前 peer；新增 `capture_memory_types`，限制 capture 抽取的记忆类型；capture 会话保留用户自己的记忆策略。[#7389](https://github.com/volcengine/OpenViking/pull/7389)、[#7367](https://github.com/volcengine/OpenViking/pull/7367)、[#7429](https://github.com/volcengine/OpenViking/pull/7429)
> …

### [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — openviking-sdk 0.1.20
<sub>2026-11-12 · 2d ago</sub>

> **更新**
> - 支持上下文使用次数与最近使用时间标签更新
> - 支持批量设置上下文标签
> - 支持 Python 同步与异步客户端调用 `batch_set_tags`

### [openviking-superagent@0.5.2-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.2-preview) — OpenViking SuperAgent 0.5.2-preview _(pre-release)_
<sub>2026-11-11 · 3d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.2-preview/install.sh | sh -s -- --version 0.5.2-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [refactor(compile): use isolated Markdown file workers (#7682)](https://github.com/volcengine/OpenViking/commit/d462af04e651335261d4972cb546788a788b2a47) | FuJiaJie123 |
| 2026-11-14 | [fix(frontend): bound DOM assertion failures and test execution (#7673)](https://github.com/volcengine/OpenViking/commit/22fd83fec46d8fd50e4400dd471b8060cc619f05) | LaamGinghong |
| 2026-11-14 | [fix(react): remove permission badges from file tree rows (#7671)](https://github.com/volcengine/OpenViking/commit/8315e350c2f06778152862a24df8a251c5720d96) | LaamGinghong |
| 2026-11-14 | [fix(react): show directory level indicator after loading (#7672)](https://github.com/volcengine/OpenViking/commit/4e4555309cbeb685041bce36573e1cb2be9dc3a2) | LaamGinghong |
| 2026-11-14 | [fix(react): pin file tree trailing content to the viewport (#7668)](https://github.com/volcengine/OpenViking/commit/2bacd32b47713d2feeb09dadc15870c9cabc9f41) | LaamGinghong |
| 2026-11-14 | [feat(react): share scoped queries and configure request concurrency (…](https://github.com/volcengine/OpenViking/commit/8d8acfa7ac6ada62cad5f5b8dc02505684ddb0ea) | LaamGinghong |
| 2026-11-14 | [feat(react): add controlled context picker and internal VikingBot HIT…](https://github.com/volcengine/OpenViking/commit/cc2b17f975394d47ca031c8814a034f28158a43b) | LaamGinghong |
| 2026-11-14 | [feat(react): support custom experience dashboard requests (#7669)](https://github.com/volcengine/OpenViking/commit/cfb96b03f1dfeee38dd98fc54c12738c92fc753c) | leowld |
| 2026-11-14 | [fix(react): keep docs examples usable in narrow themed layouts (#7662)](https://github.com/volcengine/OpenViking/commit/9b9f8d1692f9489e1965aa84affb92417bf33a2e) | LaamGinghong |
| 2026-11-14 | [fix(react): align FileBrowser and VikingBot interactions (#7651)](https://github.com/volcengine/OpenViking/commit/9f9195e5da058b0860325e3425a581fc53518833) | leowld |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
