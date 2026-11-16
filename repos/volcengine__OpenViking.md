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
| ⭐ **Stars** | 42.3k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 63% · TypeScript 17% · Rust 11% · JavaScript 3% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 421.1 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.3-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.3-preview) — OpenViking SuperAgent 0.5.3-preview _(pre-release)_
<sub>2026-11-15 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.3-preview/install.sh | sh -s -- --version 0.5.3-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — @openviking/react 0.1.12
<sub>2026-11-14 · yesterday</sub>

> **en-US**
> **Patch Changes**
> - Connect Console HITL question parsing, ordered answers and conversation continuation. Display and copy readable answer summaries while preserving protocol payloads for transport and storage.
> - Support per-question field validators, control renderers and custom cards. Preserve input for retry after failed submissions and discard obsolete interactions when reloading or switching sessions.
> - Unify HITL labels, help text, error tips and invalid-control icons. Clear local errors when input values change.
> - Preserve drafts across HITL Previous/Next navigation and schedule-frequency changes, and submit all steps once.
> …

### [react@0.1.11](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.11) — @openviking/react 0.1.11
<sub>2026-11-13 · 2d ago</sub>

> **en-US**
> **Patch Changes**
> - Add Console mode selection for conversations, commands, or both, plus independent `command.onOpenUri` routing. Track asynchronous tasks across both modes with status snapshots, notifications, and optional query adapters.
> - Recover Console inputs after session creation or delivery failures, preserve undelivered questions, and show theme-aware red error notices without storing client errors in conversation history or sending them to the model.
> - Open `.abstract.md` and `.overview.md` links at their parent directory's L0 and L1 preview. Fix file-only system directory listings by omitting retrieval tags.
> - Align FileBrowser search with the console design, remove the result preview panel, and retain keyboard result navigation. Keep preview bodies mounted across L0/L1/L2 transitions and update the level indicator without flashing the content.
> …

### [cli@0.5.3](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.3)
<sub>2026-11-13 · 3d ago</sub>

> _No notes._

### [v0.5.5](https://github.com/volcengine/OpenViking/releases/tag/v0.5.5)
<sub>2026-11-13 · 3d ago</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 部署选项**：新增 pgvector 向量后端（`storage.vectordb.backend: "pgvector"`，支持精确检索和 HNSW 检索，需要安装 `openviking[pgvector]`）和 PostgreSQL PathLock（`storage.agfs.pathlock.provider: "postgres"`）。多进程、多主机部署不依赖 Redis，也可以共享向量数据和路径锁租约。[#7516](https://github.com/volcengine/OpenViking/pull/7516)、[#7481](https://github.com/volcengine/OpenViking/pull/7481)
> - **多节点协调**：新增 `storage.agfs.coordination`（`memory` / `sqlite` / `cache`），统一负责 Watch 选主和语义任务版本；只有已持久化的工作才会取代旧任务，按 key 的状态保留一天后过期。[#7466](https://github.com/volcengine/OpenViking/pull/7466)
> - **快照路径历史索引**：`snapshot/log?paths=...` 改用派生索引查找改动过指定路径的提交，默认为 SQLite，多实例部署可选 MySQL，设为 `none` 则保持原来的扫描方式。快照提交、文件内容和 API 响应都不变。[#7505](https://github.com/volcengine/OpenViking/pull/7505)
> - **Gateway Context Profile**：新增 `recall_peer_scope`（`all` / `actor`），可把召回限制在当前 peer；新增 `capture_memory_types`，限制 capture 抽取的记忆类型；capture 会话保留用户自己的记忆策略。[#7389](https://github.com/volcengine/OpenViking/pull/7389)、[#7367](https://github.com/volcengine/OpenViking/pull/7367)、[#7429](https://github.com/volcengine/OpenViking/pull/7429)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix: filebrowser ux (#7775)](https://github.com/volcengine/OpenViking/commit/3e93b8290726d6b3f2d0ccf5169ae0a7dc733bec) | leowld |
| 2026-11-16 | [chore(sdk): 准备上下文统计能力发布 (#7511)](https://github.com/volcengine/OpenViking/commit/2b9d8c3b2114e4facb89e9329539eeb0cc2e8662) | hezhang-1216 |
| 2026-11-16 | [fix(server): validate message parts before creating the session (#7640)](https://github.com/volcengine/OpenViking/commit/fd6e83523663ca55296a145f1cec03abed8c8bca) | Kiko0301 |
| 2026-11-16 | [fix(server): make task list cursors portable across workers (#7615)](https://github.com/volcengine/OpenViking/commit/e6e5848b889f998a308e90001ef44bb63a57728d) | Kiko0301 |
| 2026-11-16 | [fix(parse): keep multiline PDF table cells within their row (#7653)](https://github.com/volcengine/OpenViking/commit/5a19d4ec125a7c6bc98d7e0ccd2cf60cd1ef76b6) | 123XieC |
| 2026-11-16 | [fix(parse): clean up the whole temp root after a web import (#7610)](https://github.com/volcengine/OpenViking/commit/a086bcdb29c991dc425cc4a5ca97c16eb0e5c1eb) | Kiko0301 |
| 2026-11-16 | [fix(server): validate pack import parent before materializing upload …](https://github.com/volcengine/OpenViking/commit/a5fd018b5ad413bcc12bbe77e1634c1131a9ec48) | Kiko0301 |
| 2026-11-16 | [fix(server): roll back an in-memory role change when persistence fail…](https://github.com/volcengine/OpenViking/commit/a220873878d1df711963896ad4af67c454405aa1) | Kiko0301 |
| 2026-11-16 | [fix(parse): preserve multiline link targets (#7642)](https://github.com/volcengine/OpenViking/commit/f2b5ec7fdace452e87b7cdb64983c3f6b86e3340) | r266-tech |
| 2026-11-16 | [refactor(logging): apply model logging policy (1/8) (#7769)](https://github.com/volcengine/OpenViking/commit/056c2f1c87d0d5bf7fd3d982fbd6f24df0b12ada) | MaojiaSheng |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
