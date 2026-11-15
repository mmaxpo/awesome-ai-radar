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
| ⭐ **Stars** | 461.0k |
| 🍴 **Forks** | 112.9k |
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/morluto/rea/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 5% · HTML 1% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `cli` `mcp` `agent-skills` `dsh-plugin` `claude-code` `rea` `touhou` `android` `javascript` `python` `typescript` `nodejs` `linux` `ai` `security` `java` `cpp` `rust` `react` `html` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-04-14 |
| 📦 **Latest release** | [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 169.4 MB |
| 🌐 **Website** | https://rea.tools |

## 📦 Recent releases

### [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — rea-agents: v6.9.0
<sub>2026-11-12 · 3d ago</sub>

> **[6.9.0](https://github.com/morluto/rea/compare/rea-agents-6.8.0...rea-agents-6.9.0) (2026-11-11)**
> **Highlights**
> - Build and test desktop tasks from recorded application state, including downloaded Linux apps, reusable build computers and multiple tasks per capture.
> - Inspect more shipped artifacts offline: standalone application bundles, embedded firmware, NTFS acquisitions, API contracts and V8 code-cache containers.
> - Keep native and runtime investigations grounded in retained Evidence, with paged results, explicit coverage and recoverable resource limits.
> **Changes**
> …

### [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) — rea-agents: v6.8.0
<sub>2026-10-25 · 21d ago</sub>

> **[6.8.0](https://github.com/morluto/rea/compare/rea-agents-6.7.0...rea-agents-6.8.0) (2026-10-25)**
> **Highlights**
> - Build local agent environments from network captures, browser scenarios, or a prompt, then serve derived reads and evidence-gated writes and compare them with fresh application captures.
> - Inspect more shipped formats, including GPU code objects, BEAM, Python bytecode, Unity IL2CPP metadata, Godot PCK, PyInstaller, Node.js SEA, devicetree, and additional PE/ELF tables.
> - Keep large investigations focused with retained summaries, selected fact queries, configurable recovery limits, and row-oriented CLI exports. Complete Evidence remains available.
> **⚠ BREAKING CHANGES**
> …

### [rea-agents-6.7.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.7.0) — rea-agents: v6.7.0
<sub>2026-10-18 · 28d ago</sub>

> **[6.7.0](https://github.com/morluto/rea/compare/rea-agents-6.6.0...rea-agents-6.7.0) (2026-10-18)**
> **Highlights**
> - Client configuration edits follow the duplicate-member semantics used by MCP clients.
> **Changes**
> - Includes the [6.6.0 changes and migration notes](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0). That version was tagged but was not published to npm.
> **Fixes**
> …

### [rea-agents-6.6.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0) — rea-agents: v6.6.0
<sub>2026-10-18 · 28d ago</sub>

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
| 2026-11-15 | [refactor(process): read Ghidra and Hopper replies through one bounded…](https://github.com/morluto/rea/commit/a8e472967b63ee2163c2d63e9fdd0d887adbc428) | morluto |
| 2026-11-15 | [refactor(cli): project observe-native-calls onto a session target and…](https://github.com/morluto/rea/commit/781f89e6f4167a8084d80cd9415a74d1a9137809) | morluto |
| 2026-11-15 | [refactor(ci): plan change scopes through an injectable Git owner (#10…](https://github.com/morluto/rea/commit/e97b6c5282a5f809db31c1ccf6891c974f3deff4) | morluto |
| 2026-11-15 | [fix(electron): refuse captures handed off to an already-running app (…](https://github.com/morluto/rea/commit/483f53fdefac2769d17d2cc27eae7d73ee44cda9) | morluto |
| 2026-11-15 | [feat(artifacts): name integrity checks for DMG, directory and release…](https://github.com/morluto/rea/commit/7134053d27268f7e1070c867047ec59bb7fe7497) | morluto |
| 2026-11-15 | [feat(providers): let runOwned's deadline timeout carry the provider's…](https://github.com/morluto/rea/commit/598a0c403478d110d48210e0a26e0dabcbc57f53) | morluto |
| 2026-11-15 | [refactor(verify): give the failure-retaining Ghidra lanes' workspaces…](https://github.com/morluto/rea/commit/0b95e556550d76d46b23ca606e39471a3d8f694f) | morluto |
| 2026-11-15 | [refactor(verify): release the agent-experience run root through Verif…](https://github.com/morluto/rea/commit/5b5ca68bb3a0f39c24721d3b7f471e55a2bf2c9d) | morluto |
| 2026-11-15 | [fix(agentenv): record a verified teardown through the long-run releas…](https://github.com/morluto/rea/commit/144d6f959fdd9cc7e7a64feb51e34671bd844942) | morluto |
| 2026-11-15 | [refactor(setup): require the platform in client-layer readers and pri…](https://github.com/morluto/rea/commit/97ffa67f841341c36113ec7783105daf7d4d389a) | morluto |

[See all commits ↗](https://github.com/morluto/rea/commits)

## ⬇️ Get it

```bash
git clone https://github.com/morluto/rea.git
```
