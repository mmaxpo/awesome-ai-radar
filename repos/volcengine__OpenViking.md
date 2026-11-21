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
| ⭐ **Stars** | 42.6k |
| 🍴 **Forks** | 3.5k |
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 10% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 431.4 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · 2d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — @openviking/react 0.2.0
<sub>2026-11-19 · 2d ago</sub>

> **en-US**
> **Minor Changes**
> - 609baba: Let FileBrowser hosts load experience metrics and override individual experience dashboard sections.
> - 704bec6: Add optional FileBrowser props for hosts to save and restore expanded folders independently of the selected resource.
>   Hosts can also persist explicit collapses across mounts when home alias resolution is temporarily unavailable.
> **Patch Changes**
> …

### [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — @openviking/react 0.1.14
<sub>2026-11-18 · 3d ago</sub>

> **en-US**
> **Minor Changes**
> - 128b63d: AgentConnect accepts `isEnterprise` to show English or Chinese team onboarding instructions for agents supported by the official installer, preserving API key masking and copying. Existing instructions remain the default.
> - 196fad5: Add OpenViking CLI session, file download, and OVPack commands to Console. Local inputs use the browser file picker. Administrator-only backup and restore require opting in through `commandOptions.allowAdminCommands`.
>   With `--read-content`, Console search results display multiline file content and fall back to the abstract when content is unavailable or blank. Search result items support an optional `content` field for the multiline body.
> - 81c42ac: Align the Console's built-in command options with the Volcengine terminal, including filesystem limits, search filters, ACL JSON, inline writes, resource import options, and task filters. Show the canonical names, aliases, and defaults in command help. `tree` now requires a directory URI, for example `ov tree viking://resources -L 2`.
> …

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · 4d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · 4d ago</sub>

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
| 2026-11-21 | [fix(react): refresh preview permissions with file tree (#8156)](https://github.com/volcengine/OpenViking/commit/000f0765d7ec183886fbabbc22e69bc289cc429d) | leowld |
| 2026-11-21 | [fix(react): clarify recurring weekly compilation schedules (#8125)](https://github.com/volcengine/OpenViking/commit/6454707105d6ad98205b0bd23c46944bde9e1e53) | leowld |
| 2026-11-21 | [fix(react): keep VikingBot tool icons neutral after sending (#8132)](https://github.com/volcengine/OpenViking/commit/217b663b7537303dcf0f36a81a7df4fdf10ce95e) | leowld |
| 2026-11-21 | [fix(react): restrict ovpack export to directories (#8139)](https://github.com/volcengine/OpenViking/commit/8a3b133b22ff4cde1334e5257af313dcfa58638e) | leowld |
| 2026-11-21 | [fix(react): distinguish compile and experience dashboard colors (#8152)](https://github.com/volcengine/OpenViking/commit/5949a04cf36b4e105d0723a70fef2f9739a752de) | leowld |
| 2026-11-21 | [fix(acl): reject principals outside the resource account (#8117)](https://github.com/volcengine/OpenViking/commit/8d4daaae5819821bbcf18e6b0d8ea6c313a86e58) | xixi-box |
| 2026-11-21 | [fix(crypto): reject malformed local root key files (#8126)](https://github.com/volcengine/OpenViking/commit/a0c00a4fd8bbb7997dad5ef54f20e3b02ebc3b6b) | Kiko0301 |
| 2026-11-21 | [fix(react): only offer ovpack export for directories (#8141)](https://github.com/volcengine/OpenViking/commit/cfc32d6cf18194471fea53082b127e9e802e07a2) | leowld |
| 2026-11-21 | [fix(react): keep ACL search placeholder stable (#8140)](https://github.com/volcengine/OpenViking/commit/3e3fd930d18b2e5b10f8e4e20d2bd3fc4f2de3c5) | leowld |
| 2026-11-21 | [feat(react): allow hiding denied FileBrowser entries (#8136)](https://github.com/volcengine/OpenViking/commit/f5066cf5bf4277c79109a33ecdcc714fa0b2824a) | leowld |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
