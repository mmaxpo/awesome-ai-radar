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
| 💻 **Languages** | Python 62% · TypeScript 17% · Rust 11% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 424.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — @openviking/react 0.1.14
<sub>2026-11-18 · today</sub>

> **en-US**
> **Minor Changes**
> - 128b63d: AgentConnect accepts `isEnterprise` to show English or Chinese team onboarding instructions for agents supported by the official installer, preserving API key masking and copying. Existing instructions remain the default.
> - 196fad5: Add OpenViking CLI session, file download, and OVPack commands to Console. Local inputs use the browser file picker. Administrator-only backup and restore require opting in through `commandOptions.allowAdminCommands`.
>   With `--read-content`, Console search results display multiline file content and fall back to the abstract when content is unavailable or blank. Search result items support an optional `content` field for the multiline body.
> - 81c42ac: Align the Console's built-in command options with the Volcengine terminal, including filesystem limits, search filters, ACL JSON, inline writes, resource import options, and task filters. Show the canonical names, aliases, and defaults in command help. `tree` now requires a directory URI, for example `ov tree viking://resources -L 2`.
> …

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · yesterday</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · yesterday</sub>

> **en-US**
> **Patch Changes**
> - ae0ce7a: Add the named compile workflow and its CLI guide. FileBrowser now reports selected tree entries so hosts can add directory references to VikingBot, whose send button uses a rounded square.
> - 62d5cd5: Support switching named compilation configurations through directory-style tabs, native Git snapshot history, and Wiki edits with explicit snapshots.
>   Propagate pending Wiki conflicts from deeply nested files to every ancestor directory, including collapsed subtrees, and refresh cleared markers. Preserve conflict tags loaded after an older empty index, and let refreshed conflict results override historical compilation counts. Skip inaccessible directory placeholders while traversing containers with readable descendants. Respect write-permission changes in open configuration editors, compare the first version against an empty baseline, and refresh the current version after a restore conflict before allowing another confirmation.
>   Align compilation settings with directory and Skill pickers, full-path tooltips, frequency radio cards and time selection. Add file selection, historical comparison and file restore to Wiki history in a full-width document panel with the FileViewer diff renderer, hide history for ordinary resource files and while editing, improve pack upload, and keep model names and dashboard tooltips readable.
> …

### [openviking-superagent@0.5.3-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.3-preview) — OpenViking SuperAgent 0.5.3-preview _(pre-release)_
<sub>2026-11-15 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.3-preview/install.sh | sh -s -- --version 0.5.3-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.12](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.12) — @openviking/react 0.1.12
<sub>2026-11-14 · 3d ago</sub>

> **en-US**
> **Patch Changes**
> - Connect Console HITL question parsing, ordered answers and conversation continuation. Display and copy readable answer summaries while preserving protocol payloads for transport and storage.
> - Support per-question field validators, control renderers and custom cards. Preserve input for retry after failed submissions and discard obsolete interactions when reloading or switching sessions.
> - Unify HITL labels, help text, error tips and invalid-control icons. Clear local errors when input values change.
> - Preserve drafts across HITL Previous/Next navigation and schedule-frequency changes, and submit all steps once.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(compile): record configuration creation time (#7970)](https://github.com/volcengine/OpenViking/commit/ee47a8f133692ef0b40768adb0a0006f36cf5153) | FuJiaJie123 |
| 2026-11-18 | [fix(react): restore Console command history after refresh (#7964)](https://github.com/volcengine/OpenViking/commit/4c11e4840338e63612a86f3ae60d297149f5cd17) | yufeng201 |
| 2026-11-18 | [fix(react): preserve full URIs in Console write results (#7962)](https://github.com/volcengine/OpenViking/commit/61a0546ce1cb9a297b0778538d912ab3cd8f352c) | yufeng201 |
| 2026-11-18 | [fix(storage): 增量更新以向量记录为准 (#7954)](https://github.com/volcengine/OpenViking/commit/0123636a88ca4c21c6e70d54a1546374e204c321) | qin-ctx |
| 2026-11-18 | [fix(react): consolidate Compile terminal help (#7958)](https://github.com/volcengine/OpenViking/commit/9dd10ecb70b22256a51ffbaafe2f432f3f256004) | yufeng201 |
| 2026-11-18 | [refactor(gateway): save each turn when its reply ends and drop the ca…](https://github.com/volcengine/OpenViking/commit/13082a92863ea56174616c51298854de74e33b59) | t0saki |
| 2026-11-18 | [fix(compile): standardize LLM Wiki conflict states (#7956)](https://github.com/volcengine/OpenViking/commit/c7659f49b4cb9db1e35d9b0257b5312e542be9a1) | FuJiaJie123 |
| 2026-11-18 | [fix(react): restore the FileBrowser search summary row (#7947)](https://github.com/volcengine/OpenViking/commit/94b18d3b02d644dabac7c6ee6495880b190974a7) | yufeng201 |
| 2026-11-18 | [fix(compile): keep drafts when routing fails (#7411)](https://github.com/volcengine/OpenViking/commit/4c439769578253e8aa73b1910be9dd01042efa78) | cocolord |
| 2026-11-18 | [refactor(logging): align retrieval core and utility logs (#7937)](https://github.com/volcengine/OpenViking/commit/fd940d8261133c0a7c2e608d5cece8f9b849600c) | MaojiaSheng |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
