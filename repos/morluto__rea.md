# morluto/rea

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/morluto/rea)

> Reverse engineer anything with agents, from app behavior down to native binaries.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔌 MCP & SDKs |
| **Project** | — |
| **Why it's worth a look** | Reverse Engineer Anything: MCP server |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 463.3k |
| 🍴 **Forks** | 113.4k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/morluto/rea/issues) |
| 💻 **Languages** | TypeScript 91% · JavaScript 5% · Python 1% · HTML 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `cli` `mcp` `agent-skills` `dsh-plugin` `claude-code` `rea` `touhou` `android` `javascript` `python` `typescript` `nodejs` `linux` `ai` `security` `java` `cpp` `rust` `react` `html` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-04-14 |
| 📦 **Latest release** | [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 174.6 MB |
| 🌐 **Website** | https://rea.tools |

## 📦 Recent releases

### [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — rea-agents: v6.9.0
<sub>2026-11-12 · 4d ago</sub>

> **[6.9.0](https://github.com/morluto/rea/compare/rea-agents-6.8.0...rea-agents-6.9.0) (2026-11-11)**
> **Highlights**
> - Build and test desktop tasks from recorded application state, including downloaded Linux apps, reusable build computers and multiple tasks per capture.
> - Inspect more shipped artifacts offline: standalone application bundles, embedded firmware, NTFS acquisitions, API contracts and V8 code-cache containers.
> - Keep native and runtime investigations grounded in retained Evidence, with paged results, explicit coverage and recoverable resource limits.
> **Changes**
> …

### [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) — rea-agents: v6.8.0
<sub>2026-10-25 · 22d ago</sub>

> **[6.8.0](https://github.com/morluto/rea/compare/rea-agents-6.7.0...rea-agents-6.8.0) (2026-10-25)**
> **Highlights**
> - Build local agent environments from network captures, browser scenarios, or a prompt, then serve derived reads and evidence-gated writes and compare them with fresh application captures.
> - Inspect more shipped formats, including GPU code objects, BEAM, Python bytecode, Unity IL2CPP metadata, Godot PCK, PyInstaller, Node.js SEA, devicetree, and additional PE/ELF tables.
> - Keep large investigations focused with retained summaries, selected fact queries, configurable recovery limits, and row-oriented CLI exports. Complete Evidence remains available.
> **⚠ BREAKING CHANGES**
> …

### [rea-agents-6.7.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.7.0) — rea-agents: v6.7.0
<sub>2026-10-18 · 29d ago</sub>

> **[6.7.0](https://github.com/morluto/rea/compare/rea-agents-6.6.0...rea-agents-6.7.0) (2026-10-18)**
> **Highlights**
> - Client configuration edits follow the duplicate-member semantics used by MCP clients.
> **Changes**
> - Includes the [6.6.0 changes and migration notes](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0). That version was tagged but was not published to npm.
> **Fixes**
> …

### [rea-agents-6.6.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0) — rea-agents: v6.6.0
<sub>2026-10-18 · 29d ago</sub>

> **[6.6.0](https://github.com/morluto/rea/compare/rea-agents-6.5.0...rea-agents-6.6.0) (2026-10-18)**
> **Highlights**
> - Add Kuna as a caller-supplied static-analysis provider.
> - Query selected JavaScript facts and multiple APK locale tables without repeating the underlying analysis.
> - Extend Ghidra analysis to Windows ARM PE targets and explicit raw m68k images.
> - Preserve completed Evidence, cancellation reasons and retryable cleanup across provider and CLI finalization.
> …

### [rea-agents-6.5.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.5.0) — rea-agents: v6.5.0
<sub>2026-10-14 · 1mo ago</sub>

> **[6.5.0](https://github.com/morluto/rea/compare/rea-agents-6.4.0...rea-agents-6.5.0) (2026-10-13)**
> Provider prerequisites and recorded verification scope are listed in [the testing guide](docs/testing.md).
> **Highlights**
> - Analyze selected JavaScript files and recover cross-bundle relationships without expanding the selected source scope.
> - Read compact summaries and page retained Evidence across binary, managed, Android, Dart, WASM and network workflows.
> - Inspect SQLite snapshots, packet and signal recordings, WebAssembly, Rust dependency metadata and Electron fuses offline.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(ci): repair shared progress, cleanup and verifier failures (#11727)](https://github.com/morluto/rea/commit/552d1c7108b99d1c9ec15d8b629ae07dc56d4714) | ShuaixinHuang |
| 2026-11-16 | [refactor(cli): derive build catalogs from the REA command registry](https://github.com/morluto/rea/commit/4ea24b6f8e63081ec5077c8e88370a8632aeeb0c) | N0zoM1z0 |
| 2026-11-16 | [refactor(cli)!: own builtin refusals and retire per-command MCP](https://github.com/morluto/rea/commit/7d502ddb0d8d80d0e16a80b0edc813f704e3ac31) | N0zoM1z0 |
| 2026-11-16 | [refactor(mcp): bind Electron tools through shared contracts](https://github.com/morluto/rea/commit/d6bcfc10eafa3c0893c7cbd5f3dc6a90359be022) | N0zoM1z0 |
| 2026-11-16 | [feat(gdb): bind sessions to an optional executable](https://github.com/morluto/rea/commit/230db70fb473dd15928ae6c1a885f7e8a5507dae) | N0zoM1z0 |
| 2026-11-16 | [refactor(cli): report unknown commands and the update notice from REA…](https://github.com/morluto/rea/commit/a10037ef10516cf92653596512932b15f190a5c0) | morluto |
| 2026-11-16 | [test(hopper): audit producer-bound snapshots through MCP](https://github.com/morluto/rea/commit/ab16163061094a6c28e9133c9c618e0850c9cb2f) | N0zoM1z0 |
| 2026-11-16 | [fix(cli): render help in REA and list csv and tsv formats (#11688)](https://github.com/morluto/rea/commit/a8cd584ccf90fb32ce0ef14e6eeb1c040fe6db30) | morluto |
| 2026-11-16 | [test(cli): register decompile-all once in the overnight CLI schema re…](https://github.com/morluto/rea/commit/6c4e2bba9d79e54446f5fdff2ac32e54503a4a2b) | morluto |
| 2026-11-16 | [refactor(cli): read global arguments once with one REA owner (#11687)](https://github.com/morluto/rea/commit/5257a3d91278387d832aed41c96b8896c2313a46) | morluto |

[See all commits ↗](https://github.com/morluto/rea/commits)

## ⬇️ Get it

```bash
git clone https://github.com/morluto/rea.git
```
