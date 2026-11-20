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
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/volcengine/OpenViking/issues) |
| 💻 **Languages** | Python 61% · TypeScript 18% · Rust 10% · JavaScript 4% · MDX 3% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `context-database` `agentic-rag` `agent-memory` `self-evolving` `agent-plugins` `dsh-plugin` `agent-context` `memory-management` `knowledge-base` `memory` `vector-database` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-01-05 |
| 📦 **Latest release** | [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 427.3 MB |
| 🌐 **Website** | https://openviking.ai |

## 📦 Recent releases

### [openviking-superagent@0.5.5-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.5-preview) — OpenViking SuperAgent 0.5.5-preview _(pre-release)_
<sub>2026-11-19 · yesterday</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.5-preview/install.sh | sh -s -- --version 0.5.5-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.2.0](https://github.com/volcengine/OpenViking/releases/tag/react%400.2.0) — @openviking/react 0.2.0
<sub>2026-11-19 · yesterday</sub>

> **en-US**
> **Minor Changes**
> - 609baba: Let FileBrowser hosts load experience metrics and override individual experience dashboard sections.
> - 704bec6: Add optional FileBrowser props for hosts to save and restore expanded folders independently of the selected resource.
>   Hosts can also persist explicit collapses across mounts when home alias resolution is temporarily unavailable.
> **Patch Changes**
> …

### [react@0.1.14](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.14) — @openviking/react 0.1.14
<sub>2026-11-18 · 2d ago</sub>

> **en-US**
> **Minor Changes**
> - 128b63d: AgentConnect accepts `isEnterprise` to show English or Chinese team onboarding instructions for agents supported by the official installer, preserving API key masking and copying. Existing instructions remain the default.
> - 196fad5: Add OpenViking CLI session, file download, and OVPack commands to Console. Local inputs use the browser file picker. Administrator-only backup and restore require opting in through `commandOptions.allowAdminCommands`.
>   With `--read-content`, Console search results display multiline file content and fall back to the abstract when content is unavailable or blank. Search result items support an optional `content` field for the multiline body.
> - 81c42ac: Align the Console's built-in command options with the Volcengine terminal, including filesystem limits, search filters, ACL JSON, inline writes, resource import options, and task filters. Show the canonical names, aliases, and defaults in command help. `tree` now requires a directory URI, for example `ov tree viking://resources -L 2`.
> …

### [openviking-superagent@0.5.4-preview](https://github.com/volcengine/OpenViking/releases/tag/openviking-superagent%400.5.4-preview) — OpenViking SuperAgent 0.5.4-preview _(pre-release)_
<sub>2026-11-17 · 3d ago</sub>

> **Install**
> macOS / Linux / WSL2 (this version):
> ```sh
> curl -fsSL https://ovrelease.tos-cn-beijing.volces.com/superagent/releases/0.5.4-preview/install.sh | sh -s -- --version 0.5.4-preview
> ```
> Windows users: use the PowerShell one-line installer in the shared guide below. Windows previews are published separately; this command and these release assets are for macOS / Linux.
> …

### [react@0.1.13](https://github.com/volcengine/OpenViking/releases/tag/react%400.1.13) — @openviking/react 0.1.13
<sub>2026-11-16 · 3d ago</sub>

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
| 2026-11-20 | [fix(compile): preserve baseline when output is unchanged (#8109)](https://github.com/volcengine/OpenViking/commit/9fd2e02e222cd3ca9b70288d7f80f1ca93dcc8d7) | FuJiaJie123 |
| 2026-11-20 | [fix(react): show compact command names in ov help (#8099)](https://github.com/volcengine/OpenViking/commit/8a19e6b04d3bf0a3daa766febfe699b41de9f8d6) | yufeng201 |
| 2026-11-20 | [fix(react): align directory tour presets and themed artwork (#8101)](https://github.com/volcengine/OpenViking/commit/fc16795d17c242d729f96abe42cdcaf9927e71b7) | leowld |
| 2026-11-20 | [fix(react): align terminal quick actions (#8096)](https://github.com/volcengine/OpenViking/commit/22f4ff6513b4a1aec75ded1c75a8cc883c717340) | yufeng201 |
| 2026-11-20 | [fix(react): correct search scopes and VikingBot tool colors (#8098)](https://github.com/volcengine/OpenViking/commit/4a0e0fb383e3d7dbc346a2dd65f36cd7edada722) | leowld |
| 2026-11-20 | [fix(react): preserve raw FileBrowser tree names (#8100)](https://github.com/volcengine/OpenViking/commit/72d8e488346d85c154e9c16a6b37cf307940716f) | yufeng201 |
| 2026-11-20 | [fix(compile): settle exhausted submission retries (#8097)](https://github.com/volcengine/OpenViking/commit/e1f7405952504ffddc57607d9bdfc3f825e5f042) | FuJiaJie123 |
| 2026-11-20 | [fix(react): align preview copy feedback and AgentConnect scrolling (#…](https://github.com/volcengine/OpenViking/commit/ced8e8e6139b45ad77b989be849677a366f6c94e) | leowld |
| 2026-11-20 | [Feat/ls tree file uri (#8071)](https://github.com/volcengine/OpenViking/commit/f62a34de18bd8de67ffbedd836fa9dddb054bf92) | zhoujh01 |
| 2026-11-20 | [fix(react): restore VikingBot session commit status (#8089)](https://github.com/volcengine/OpenViking/commit/6f0db1f484aa33e9d85358db01ee3d2dc2972784) | yufeng201 |

[See all commits ↗](https://github.com/volcengine/OpenViking/commits)

## ⬇️ Get it

```bash
git clone https://github.com/volcengine/OpenViking.git
```
