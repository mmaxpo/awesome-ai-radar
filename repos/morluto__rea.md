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
| ⭐ **Stars** | 469.4k |
| 🍴 **Forks** | 114.7k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/morluto/rea/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 5% · Python 1% · HTML 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `cli` `mcp` `agent-skills` `dsh-plugin` `claude-code` `rea` `touhou` `android` `javascript` `python` `typescript` `nodejs` `linux` `ai` `security` `java` `cpp` `rust` `react` `html` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-04-14 |
| 📦 **Latest release** | [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 191.6 MB |
| 🌐 **Website** | https://rea.tools |

## 📦 Recent releases

### [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — rea-agents: v6.9.0
<sub>2026-11-12 · 7d ago</sub>

> **[6.9.0](https://github.com/morluto/rea/compare/rea-agents-6.8.0...rea-agents-6.9.0) (2026-11-11)**
> **Highlights**
> - Build and test desktop tasks from recorded application state, including downloaded Linux apps, reusable build computers and multiple tasks per capture.
> - Inspect more shipped artifacts offline: standalone application bundles, embedded firmware, NTFS acquisitions, API contracts and V8 code-cache containers.
> - Keep native and runtime investigations grounded in retained Evidence, with paged results, explicit coverage and recoverable resource limits.
> **Changes**
> …

### [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) — rea-agents: v6.8.0
<sub>2026-10-25 · 25d ago</sub>

> **[6.8.0](https://github.com/morluto/rea/compare/rea-agents-6.7.0...rea-agents-6.8.0) (2026-10-25)**
> **Highlights**
> - Build local agent environments from network captures, browser scenarios, or a prompt, then serve derived reads and evidence-gated writes and compare them with fresh application captures.
> - Inspect more shipped formats, including GPU code objects, BEAM, Python bytecode, Unity IL2CPP metadata, Godot PCK, PyInstaller, Node.js SEA, devicetree, and additional PE/ELF tables.
> - Keep large investigations focused with retained summaries, selected fact queries, configurable recovery limits, and row-oriented CLI exports. Complete Evidence remains available.
> **⚠ BREAKING CHANGES**
> …

### [rea-agents-6.7.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.7.0) — rea-agents: v6.7.0
<sub>2026-10-18 · 1mo ago</sub>

> **[6.7.0](https://github.com/morluto/rea/compare/rea-agents-6.6.0...rea-agents-6.7.0) (2026-10-18)**
> **Highlights**
> - Client configuration edits follow the duplicate-member semantics used by MCP clients.
> **Changes**
> - Includes the [6.6.0 changes and migration notes](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0). That version was tagged but was not published to npm.
> **Fixes**
> …

### [rea-agents-6.6.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.6.0) — rea-agents: v6.6.0
<sub>2026-10-18 · 1mo ago</sub>

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
| 2026-11-19 | [ci: reject merged test reports that do not confirm success (#12367)](https://github.com/morluto/rea/commit/f06c51a82a1f6fe74859656c0768efd76b88a2d7) | ShuaixinHuang |
| 2026-11-19 | [refactor(dotnet): read metadata constant scalars through BinaryReader…](https://github.com/morluto/rea/commit/091b8b0339f3ab5b1075715e9dedfce5d6df8df1) | morluto |
| 2026-11-19 | [ci(recorded-crash): bound package acquisition before install (#12365)](https://github.com/morluto/rea/commit/59c7eed91d52530ab110f9c80bd38419e5b99651) | ShuaixinHuang |
| 2026-11-19 | [fix(pe): validate resource name extents before capacity (#12368)](https://github.com/morluto/rea/commit/17ad9c14ff84f41d13d2b5cedf02a19fdd49401b) | morluto |
| 2026-11-19 | [refactor(macho): share checked segment and section framing (#12366)](https://github.com/morluto/rea/commit/5f258086b031b18b4cd65b9c35c63d0c726bfad0) | morluto |
| 2026-11-19 | [fix(environment): apply collection mappings to identifier lists (#12354)](https://github.com/morluto/rea/commit/0a55ccba71edeba515ec19d7f4b750b7a12ffce5) | ShuaixinHuang |
| 2026-11-19 | [fix(desktop): preserve exact dpkg ownership from partial queries (#12…](https://github.com/morluto/rea/commit/0fead854579542f6f8cd672d469c0667d57d8464) | morluto |
| 2026-11-19 | [refactor(python): read marshal scalars and bytecode magic through Bin…](https://github.com/morluto/rea/commit/156303f6ede33e79ee2ebf2346bc9f28529149d5) | morluto |
| 2026-11-19 | [fix(artifacts): require DOS magic before applying Windows path semant…](https://github.com/morluto/rea/commit/7758d03c5d1744057b43f4feafd5c1a3e899fe72) | morluto |
| 2026-11-19 | [ci(sigrok): use the shared Ubuntu archive setup (#12359)](https://github.com/morluto/rea/commit/f6c04b74f3f70abc47fa2394365fb05d3a5e63ce) | ShuaixinHuang |

[See all commits ↗](https://github.com/morluto/rea/commits)

## ⬇️ Get it

```bash
git clone https://github.com/morluto/rea.git
```
