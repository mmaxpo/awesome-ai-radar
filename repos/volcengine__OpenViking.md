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
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 419.7 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — @openviking/react 0.1.12
<sub>2026-11-14 · today</sub>

> **en-US**
> **Patch Changes**
> - Connect Console HITL question parsing, ordered answers and conversation continuation. Display and copy readable answer summaries while preserving protocol payloads for transport and storage.
> - Support per-question field validators, control renderers and custom cards. Preserve input for retry after failed submissions and discard obsolete interactions when reloading or switching sessions.
> - Unify HITL labels, help text, error tips and invalid-control icons. Clear local errors when input values change.
> - Preserve drafts across HITL Previous/Next navigation and schedule-frequency changes, and submit all steps once.
> …

### [react@0.1.11](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.11) — @openviking/react 0.1.11
<sub>2026-11-13 · yesterday</sub>

> **en-US**
> **Patch Changes**
> - Add Console mode selection for conversations, commands, or both, plus independent `command.onOpenUri` routing. Track asynchronous tasks across both modes with status snapshots, notifications, and optional query adapters.
> - Recover Console inputs after session creation or delivery failures, preserve undelivered questions, and show theme-aware red error notices without storing client errors in conversation history or sending them to the model.
> - Open `.abstract.md` and `.overview.md` links at their parent directory's L0 and L1 preview. Fix file-only system directory listings by omitting retrieval tags.
> - Align FileBrowser search with the console design, remove the result preview panel, and retain keyboard result navigation. Keep preview bodies mounted across L0/L1/L2 transitions and update the level indicator without flashing the content.
> …

### [cli@0.5.3](https://github.com/volcengine/OpenViking/releases/tag/cli%400.5.3)
<sub>2026-11-13 · yesterday</sub>

> _No notes._

### [v0.5.5](https://github.com/volcengine/OpenViking/releases/tag/v0.5.5)
<sub>2026-11-13 · yesterday</sub>

> **中文**
> **主要更新**
> - **PostgreSQL 部署选项**：新增 pgvector 向量后端（`storage.vectordb.backend: "pgvector"`，支持精确检索和 HNSW 检索，需要安装 `openviking[pgvector]`）和 PostgreSQL PathLock（`storage.agfs.pathlock.provider: "postgres"`）。多进程、多主机部署不依赖 Redis，也可以共享向量数据和路径锁租约。[#7516](https://github.com/volcengine/OpenViking/pull/7516)、[#7481](https://github.com/volcengine/OpenViking/pull/7481)
> - **多节点协调**：新增 `storage.agfs.coordination`（`memory` / `sqlite` / `cache`），统一负责 Watch 选主和语义任务版本；只有已持久化的工作才会取代旧任务，按 key 的状态保留一天后过期。[#7466](https://github.com/volcengine/OpenViking/pull/7466)
> - **快照路径历史索引**：`snapshot/log?paths=...` 改用派生索引查找改动过指定路径的提交，默认为 SQLite，多实例部署可选 MySQL，设为 `none` 则保持原来的扫描方式。快照提交、文件内容和 API 响应都不变。[#7505](https://github.com/volcengine/OpenViking/pull/7505)
> - **Gateway Context Profile**：新增 `recall_peer_scope`（`all` / `actor`），可把召回限制在当前 peer；新增 `capture_memory_types`，限制 capture 抽取的记忆类型；capture 会话保留用户自己的记忆策略。[#7389](https://github.com/volcengine/OpenViking/pull/7389)、[#7367](https://github.com/volcengine/OpenViking/pull/7367)、[#7429](https://github.com/volcengine/OpenViking/pull/7429)
> …

### [python-sdk@0.1.20](https://github.com/volcengine/OpenViking/releases/tag/python-sdk%400.1.20) — openviking-sdk 0.1.20
<sub>2026-11-12 · 3d ago</sub>

> **更新**
> - 支持上下文使用次数与最近使用时间标签更新
> - 支持批量设置上下文标签
> - 支持 Python 同步与异步客户端调用 `batch_set_tags`

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [feat(studio): copy, move, and delete shared resources (#7712)](https://github.com/volcengine/OpenViking/commit/f9bf90b398df1c0ee6732d257dcdba793f02e2b5) | openviking-superagent |
| 2026-11-15 | [feat(ci): route Linux API jobs and wheel builds to dedicated runner (…](https://github.com/volcengine/OpenViking/commit/1a6e51f0c62462da43a79e9794f03efb485cc17f) | zhanglistar |
| 2026-11-14 | [chore(react): prepare 0.1.12 stable release (#7706)](https://github.com/volcengine/OpenViking/commit/00c8e7b1b8701fe0f0ee43d29b4f96667984b6d5) | LaamGinghong |
| 2026-11-14 | [feat(react): connect Console HITL flow and extensible form fields (#7…](https://github.com/volcengine/OpenViking/commit/bb70f8c7d1e90bc8ee65efe3cd3188996ae8bed1) | LaamGinghong |
| 2026-11-14 | [feat(react): unify error feedback with Toast and copyable notificatio…](https://github.com/volcengine/OpenViking/commit/34c01616eb96a5077042c76ea4502587a332d8ee) | LaamGinghong |
| 2026-11-14 | [feat(react): add opt-in frontend monitoring and target CSR (#7696)](https://github.com/volcengine/OpenViking/commit/c189fccf4941222365b404d2add51a104f375df8) | LaamGinghong |
| 2026-11-14 | [fix(react): isolate file tree dashboard tooltips (#7698)](https://github.com/volcengine/OpenViking/commit/ad4516ec9fd92405afb316248a6e1c88190f1322) | LaamGinghong |
| 2026-11-14 | [feat(react): add built-in HITL validation and step navigation (#7694)](https://github.com/volcengine/OpenViking/commit/c79d9fdb1b98330530c814ef56389aac17d49013) | LaamGinghong |
| 2026-11-14 | [fix(react): unify focus halos and adopt Arco time picker (#7683)](https://github.com/volcengine/OpenViking/commit/99418e357764753a770d97e9e50be9845de2d5d7) | LaamGinghong |
| 2026-11-14 | [refactor(compile): use isolated Markdown file workers (#7682)](https://github.com/volcengine/OpenViking/commit/d462af04e651335261d4972cb546788a788b2a47) | FuJiaJie123 |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
