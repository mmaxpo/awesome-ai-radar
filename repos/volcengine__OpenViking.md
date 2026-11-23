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
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 11% · JavaScript 5% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 433.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 4d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — @openviking/react 0.2.0
<sub>2026-11-19 · 4d ago</sub>

> **en-US**
> **Minor Changes**
> - 609baba: Let FileBrowser hosts load experience metrics and override individual experience dashboard sections.
> - 704bec6: Add optional FileBrowser props for hosts to save and restore expanded folders independently of the selected resource.
>   Hosts can also persist explicit collapses across mounts when home alias resolution is temporarily unavailable.
> **Patch Changes**
> …

### [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — @openviking/react 0.1.14
<sub>2026-11-18 · 5d ago</sub>

> **en-US**
> **Minor Changes**
> - 128b63d: AgentConnect accepts `isEnterprise` to show English or Chinese team onboarding instructions for agents supported by the official installer, preserving API key masking and copying. Existing instructions remain the default.
> - 196fad5: Add OpenViking CLI session, file download, and OVPack commands to Console. Local inputs use the browser file picker. Administrator-only backup and restore require opting in through `commandOptions.allowAdminCommands`.
>   With `--read-content`, Console search results display multiline file content and fall back to the abstract when content is unavailable or blank. Search result items support an optional `content` field for the multiline body.
> - 81c42ac: Align the Console's built-in command options with the Volcengine terminal, including filesystem limits, search filters, ACL JSON, inline writes, resource import options, and task filters. Show the canonical names, aliases, and defaults in command help. `tree` now requires a directory URI, for example `ov tree viking://resources -L 2`.
> …

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · 6d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · 6d ago</sub>

> **en-US**
> **Patch Changes**
> - ae0ce7a: Add the named compile workflow and its CLI guide. FileBrowser now reports selected tree entries so hosts can add directory references to VikingBot, whose send button uses a rounded square.
> - 62d5cd5: Support switching named compilation configurations through directory-style tabs, native Git snapshot history, and Wiki edits with explicit snapshots.
>   Propagate pending Wiki conflicts from deeply nested files to every ancestor directory, including collapsed subtrees, and refresh cleared markers. Preserve conflict tags loaded after an older empty index, and let refreshed conflict results override historical compilation counts. Skip inaccessible directory placeholders while traversing containers with readable descendants. Respect write-permission changes in open configuration editors, compare the first version against an empty baseline, and refresh the current version after a restore conflict before allowing another confirmation.
>   Align compilation settings with directory and Skill pickers, full-path tooltips, frequency radio cards and time selection. Add file selection, historical comparison and file restore to Wiki history in a full-width document panel with the FileViewer diff renderer, hide history for ordinary resource files and while editing, improve pack upload, and keep model names and dashboard tooltips readable.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(react): close command assists outside the input (#8269)](https://github.com/volcengine/OpenViking/commit/300ab8eb0746d917b7b968b7f739a28a5a5c04b5) | yufeng201 |
| 2026-11-23 | [feat(queuefs): add durable PostgreSQL backend (#8233)](https://github.com/volcengine/OpenViking/commit/484347c192a1270b42ed500148e7511e653d96d0) | zhanglistar |
| 2026-11-23 | [fix(grep): 将 Python 正则匹配迁移到 Rust (#8289)](https://github.com/volcengine/OpenViking/commit/d1b124c5d179880a907130b6703d2b3d4e295482) | qin-ctx |
| 2026-11-23 | [fix(react): align file browser history scope and root breadcrumb (#8297)](https://github.com/volcengine/OpenViking/commit/ad0f4200aa7824f17b34e17adcaa1e1206a129d3) | LaamGinghong |
| 2026-11-23 | [fix(react): align VikingBot activation copy (#8291)](https://github.com/volcengine/OpenViking/commit/951ec937407d88aa12411e2b0f5c1dc410cd8f2d) | LaamGinghong |
| 2026-11-23 | [fix(bot): preserve remote skill integrity with privacy restoration (#…](https://github.com/volcengine/OpenViking/commit/5b7c655610caef9017ed0540474dc7d49db4f2db) | LIEGU0317 |
| 2026-11-23 | [fix(react): support prelaunch agent connection instructions (#8288)](https://github.com/volcengine/OpenViking/commit/b8512a7d543271cdcd89e6adb5a56e6947934e8b) | leowld |
| 2026-11-23 | [fix(react): keep draft references removable during replies (#8284)](https://github.com/volcengine/OpenViking/commit/9acd1857fa0b216df30b3e6567495744870a9988) | LaamGinghong |
| 2026-11-23 | [fix(memory): 创建用户时预置记忆目录 (#8283)](https://github.com/volcengine/OpenViking/commit/38220ce53c3ca6659cf3f6dcdd6fba721cdd7fdf) | qin-ctx |
| 2026-11-23 | [fix(react): keep FileBrowser panes usable when resizing (#8282)](https://github.com/volcengine/OpenViking/commit/ae3952e953e60f0609a2dd5a15cb87419ce2d401) | LaamGinghong |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
