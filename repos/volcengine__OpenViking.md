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
| ⭐ **Stars** | 42.5k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 10% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 426.1 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · today</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — @openviking/react 0.2.0
<sub>2026-11-19 · today</sub>

> **en-US**
> **Minor Changes**
> - 609baba: Let FileBrowser hosts load experience metrics and override individual experience dashboard sections.
> - 704bec6: Add optional FileBrowser props for hosts to save and restore expanded folders independently of the selected resource.
>   Hosts can also persist explicit collapses across mounts when home alias resolution is temporarily unavailable.
> **Patch Changes**
> …

### [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — @openviking/react 0.1.14
<sub>2026-11-18 · yesterday</sub>

> **en-US**
> **Minor Changes**
> - 128b63d: AgentConnect accepts `isEnterprise` to show English or Chinese team onboarding instructions for agents supported by the official installer, preserving API key masking and copying. Existing instructions remain the default.
> - 196fad5: Add OpenViking CLI session, file download, and OVPack commands to Console. Local inputs use the browser file picker. Administrator-only backup and restore require opting in through `commandOptions.allowAdminCommands`.
>   With `--read-content`, Console search results display multiline file content and fall back to the abstract when content is unavailable or blank. Search result items support an optional `content` field for the multiline body.
> - 81c42ac: Align the Console's built-in command options with the Volcengine terminal, including filesystem limits, search filters, ACL JSON, inline writes, resource import options, and task filters. Show the canonical names, aliases, and defaults in command help. `tree` now requires a directory URI, for example `ov tree viking://resources -L 2`.
> …

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · 2d ago</sub>

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
| 2026-11-19 | [fix: correct Grep root scopes and search feedback (#8032)](https://github.com/volcengine/OpenViking/commit/909ac00da86570bbdebe14a78f1ad1f0a5404219) | leowld |
| 2026-11-19 | [fix(react): prevent CLI flash while checking VikingBot status (#8033)](https://github.com/volcengine/OpenViking/commit/478fefc5909980fd945bb5273dd38f8ee9745d46) | leowld |
| 2026-11-19 | [fix(react): resolve current-user directory roots locally (#8036)](https://github.com/volcengine/OpenViking/commit/a52b5d4a764c4e89cd9ac81a02a05c4a6e2424b7) | leowld |
| 2026-11-19 | [fix(grep): report capped results in VikingBot and MCP (#7938)](https://github.com/volcengine/OpenViking/commit/b0cb51a4bd0f9639c6c7576fb4029de1c6a91b24) | littleblueprince |
| 2026-11-19 | [fix(react): preserve terminal code lines (#8044)](https://github.com/volcengine/OpenViking/commit/2b1018a12013c197e1ab2f9c19eef41c3763c099) | yufeng201 |
| 2026-11-19 | [test(storage): 精简存储与索引契约测试 (#8038)](https://github.com/volcengine/OpenViking/commit/42e861f39e6bb0a6a6c08c3fd2d0ab5c9f25998e) | qin-ctx |
| 2026-11-19 | [fix(react): use compile create quick command (#8041)](https://github.com/volcengine/OpenViking/commit/8d68b163f15d16aa17398b5660ba2b5156da33cc) | yufeng201 |
| 2026-11-19 | [docs: move Changes Made below Description in the PR template (#8042)](https://github.com/volcengine/OpenViking/commit/f591acc1a4e072a658b1ca5092a30943a3291134) | qin-ctx |
| 2026-11-19 | [feat(search): support advanced args for keyword search (#7967)](https://github.com/volcengine/OpenViking/commit/7a934e59b50bb11e634d6e3021bb5eb9c656e7a0) | ByteDanceLiuYang |
| 2026-11-19 | [fix(studio): hide administration in dev mode (#8039)](https://github.com/volcengine/OpenViking/commit/b5b27720bebc7239fff2edaa24a54664c589615c) | yufeng201 |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
