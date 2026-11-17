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
| ⭐ **Stars** | 42.4k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 62% · TypeScript 17% · Rust 11% · JavaScript 3% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 421.7 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · today</sub>

> **en-US**
> **Patch Changes**
> - ae0ce7a: Add the named compile workflow and its CLI guide. FileBrowser now reports selected tree entries so hosts can add directory references to VikingBot, whose send button uses a rounded square.
> - 62d5cd5: Support switching named compilation configurations through directory-style tabs, native Git snapshot history, and Wiki edits with explicit snapshots.
>   Propagate pending Wiki conflicts from deeply nested files to every ancestor directory, including collapsed subtrees, and refresh cleared markers. Preserve conflict tags loaded after an older empty index, and let refreshed conflict results override historical compilation counts. Skip inaccessible directory placeholders while traversing containers with readable descendants. Respect write-permission changes in open configuration editors, compare the first version against an empty baseline, and refresh the current version after a restore conflict before allowing another confirmation.
>   Align compilation settings with directory and Skill pickers, full-path tooltips, frequency radio cards and time selection. Add file selection, historical comparison and file restore to Wiki history in a full-width document panel with the FileViewer diff renderer, hide history for ordinary resource files and while editing, improve pack upload, and keep model names and dashboard tooltips readable.
> …

### [openviking-superagent@0.5.3-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.3-preview) — OpenViking SuperAgent 0.5.3-preview _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.3-preview/install.sh | sh -s -- --version 0.5.3-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — @openviking/react 0.1.12
<sub>2026-11-14 · 2d ago</sub>

> **en-US**
> **Patch Changes**
> - Connect Console HITL question parsing, ordered answers and conversation continuation. Display and copy readable answer summaries while preserving protocol payloads for transport and storage.
> - Support per-question field validators, control renderers and custom cards. Preserve input for retry after failed submissions and discard obsolete interactions when reloading or switching sessions.
> - Unify HITL labels, help text, error tips and invalid-control icons. Clear local errors when input values change.
> - Preserve drafts across HITL Previous/Next navigation and schedule-frequency changes, and submit all steps once.
> …

### [react@0.1.11](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.11) — @openviking/react 0.1.11
<sub>2026-11-13 · 3d ago</sub>

> **en-US**
> **Patch Changes**
> - Add Console mode selection for conversations, commands, or both, plus independent `command.onOpenUri` routing. Track asynchronous tasks across both modes with status snapshots, notifications, and optional query adapters.
> - Recover Console inputs after session creation or delivery failures, preserve undelivered questions, and show theme-aware red error notices without storing client errors in conversation history or sending them to the model.
> - Open `.abstract.md` and `.overview.md` links at their parent directory's L0 and L1 preview. Fix file-only system directory listings by omitting retrieval tags.
> - Align FileBrowser search with the console design, remove the result preview panel, and retain keyboard result navigation. Keep preview bodies mounted across L0/L1/L2 transitions and update the level indicator without flashing the content.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(compile): skip unchanged state writes and redundant reads (#7860)](https://github.com/volcengine/OpenViking/commit/8f113dc508ec67bd6215c5b49f12b8e910bfd00a) | FuJiaJie123 |
| 2026-11-17 | [docs(mcp): 完善检索工具参数描述 (#7841)](https://github.com/volcengine/OpenViking/commit/0d49997430356982b0474e50bfca086857e8fe8c) | hezhang-1216 |
| 2026-11-17 | [feat(react): align VikingBot and Wiki workflows (#7826)](https://github.com/volcengine/OpenViking/commit/b90eb2e7e4b9a76526b5b8681c7cd9cba98dbd1e) | leowld |
| 2026-11-17 | [feat(react): align Web CLI command options with Volcengine (#7851)](https://github.com/volcengine/OpenViking/commit/81c42ac285fedfbd0758a01cf895b6cbc2fea397) | leowld |
| 2026-11-17 | [fix(react): prevent copy-path tooltip after rollback (#7850)](https://github.com/volcengine/OpenViking/commit/3e229d1303823b8c3f7c845a4bea2650313b9d7e) | yufeng201 |
| 2026-11-17 | [feat(react): show transcripts and frames in video previews (#7833)](https://github.com/volcengine/OpenViking/commit/a8d37f35b89be41514f978d8af2c9d3c785e221c) | yufeng201 |
| 2026-11-17 | [fix(memory): honor configured thinking for training extraction (#7478)](https://github.com/volcengine/OpenViking/commit/649cf91240e1f0ce110faef47dff60c7a418447c) | deosiree |
| 2026-11-17 | [pi: bound the final commit on the exit path (#7464)](https://github.com/volcengine/OpenViking/commit/c5625ac21f3572c18d19f7d854d4b519af15f044) | Batianxieshen1 |
| 2026-11-17 | [fix(sdk/python): reject failed snapshot blob responses (#7451)](https://github.com/volcengine/OpenViking/commit/ae393af5941ff854cd04a2ebe4a7bb8a036d2247) | stefanielizeth73-art |
| 2026-11-17 | [fix(mcp): remove stale array items from string property overrides (#7…](https://github.com/volcengine/OpenViking/commit/98a744c0eae72139473250e9e85f811e4f8650a0) | codinglemom |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
