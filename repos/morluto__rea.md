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
| ⭐ **Stars** | 471.0k |
| 🍴 **Forks** | 115.0k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/morluto/rea/issues) |
| 💻 **Languages** | TypeScript 92% · JavaScript 5% · Python 1% · HTML 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `cli` `mcp` `agent-skills` `dsh-plugin` `claude-code` `rea` `touhou` `android` `javascript` `python` `typescript` `nodejs` `linux` `ai` `security` `java` `cpp` `rust` `react` `html` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-04-14 |
| 📦 **Latest release** | [rea-agents-6.10.1](https://github.com/morluto/rea/releases/tag/rea-agents-6.10.1) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 193.0 MB |
| 🌐 **Website** | https://rea.tools |

## 📦 Recent releases

### [rea-agents-6.10.1](https://github.com/morluto/rea/releases/tag/rea-agents-6.10.1) — rea-agents: v6.10.1
<sub>2026-11-20 · today</sub>

> **[6.10.1](https://github.com/morluto/rea/compare/rea-agents-6.10.0...rea-agents-6.10.1) (2026-11-20)**
> This is the first 6.10 release published to npm. It includes the changes, migration notes, and contributor credits from 6.10.0 below, plus the patch fix.
> **Bug Fixes**
> * **kuna:** use one constant for the serial job count ([#12735](https://github.com/morluto/rea/issues/12735)) ([3e3faf2](https://github.com/morluto/rea/commit/3e3faf2fc32dbadc96a45f51f4361eb64ce6ed32))
> ---
> **[6.10.0](https://github.com/morluto/rea/compare/rea-agents-6.9.0...rea-agents-6.10.0) (2026-11-20)**
> …

### [rea-agents-6.10.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.10.0) — rea-agents: v6.10.0
<sub>2026-11-20 · today</sub>

> **[6.10.0](https://github.com/morluto/rea/compare/rea-agents-6.9.0...rea-agents-6.10.0) (2026-11-20)**
> **Highlights**
> - Inspect and extract UEFI firmware volumes, files, and AMI NVRAM with three offline CLI and MCP tools. [#12342](https://github.com/morluto/rea/pull/12342). Thanks @bartman081523.
> - Inspect Android boot images and OTA payloads, NES 2.0 containers, and Maven, Gradle, and NuGet package metadata. [a88c0a5](https://github.com/morluto/rea/commit/a88c0a55544e16a710ddaad2feb5a2c6e7011f4e) [#9487](https://github.com/morluto/rea/pull/9487) [#11378](https://github.com/morluto/rea/pull/11378) [#10674](https://github.com/morluto/rea/pull/10674) [05be423](https://github.com/morluto/rea/commit/05be423acbdf3a56673bdbd3004e4b500c0f5217) [#10353](https://github.com/morluto/rea/pull/10353) [43b9fa8](https://github.com/morluto/rea/commit/43b9fa87fbbaa74224731a1fe3a8e67a2d336ae3) [#10351](https://github.com/morluto/rea/pull/10351) [#8144](https://github.com/morluto/rea/issues/8144). Thanks @Davmunrey, @gensokyo-dev, @jayykernel, @mvanhorn.
> - Evidence revision 2 gives file, process, debugger, and browser observations explicit subject identities. See the migration details below.
> - The verified Ghidra 12.2 lane opens recognized DOS COM files and supports more RISC-V, MIPS32, and PowerPC64 ELF targets. [#4811](https://github.com/morluto/rea/pull/4811) [#4487](https://github.com/morluto/rea/issues/4487) [#2362](https://github.com/morluto/rea/pull/2362) [#2338](https://github.com/morluto/rea/issues/2338) [#12517](https://github.com/morluto/rea/pull/12517) [#12085](https://github.com/morluto/rea/issues/12085). Thanks @abhay-2108, @AurelioB, @Davmunrey, @kaoru0822-kitauji, @Rinkia.
> …

### [rea-agents-6.9.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.9.0) — rea-agents: v6.9.0
<sub>2026-11-12 · 8d ago</sub>

> **[6.9.0](https://github.com/morluto/rea/compare/rea-agents-6.8.0...rea-agents-6.9.0) (2026-11-11)**
> **Highlights**
> - Build and test desktop tasks from recorded application state, including downloaded Linux apps, reusable build computers and multiple tasks per capture.
> - Inspect more shipped artifacts offline: standalone application bundles, embedded firmware, NTFS acquisitions, API contracts and V8 code-cache containers.
> - Keep native and runtime investigations grounded in retained Evidence, with paged results, explicit coverage and recoverable resource limits.
> **Changes**
> …

### [rea-agents-6.8.0](https://github.com/morluto/rea/releases/tag/rea-agents-6.8.0) — rea-agents: v6.8.0
<sub>2026-10-25 · 26d ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [test(reference): consolidate reader scheduling and failure checks (#1…](https://github.com/morluto/rea/commit/4f5d1b250c0d90d6cb53009ffb56a0fdd0a7a929) | morluto |
| 2026-11-20 | [test(android): consolidate ADB and Apktool boundary checks (#12837)](https://github.com/morluto/rea/commit/79525a7c3eb0fe333463a2c76265a5f9fcdd7e2c) | morluto |
| 2026-11-20 | [test(mcp): consolidate result delivery and capture checks (#12836)](https://github.com/morluto/rea/commit/11c951228c6ae466c8391a0871164ab11d89aa5e) | morluto |
| 2026-11-20 | [test(pcap): consolidate tool admission coverage (#12834)](https://github.com/morluto/rea/commit/15d53aecb0ad8e5442414c43c44b44293c199266) | morluto |
| 2026-11-20 | [test(formats): consolidate BEAM and DOL boundary checks (#12832)](https://github.com/morluto/rea/commit/c9caa0aa5b60e049ac5284b7f9efaad4d793c3ff) | morluto |
| 2026-11-20 | [test(mcp): consolidate admission and lifecycle checks (#12833)](https://github.com/morluto/rea/commit/bb7bdd2fba4cbdd72e3c82df93fa64b7f0575799) | morluto |
| 2026-11-20 | [test(erlang): consolidate BEAM budget and truncation coverage (#12830)](https://github.com/morluto/rea/commit/01895d33efd70d3291e91e89907db058e90b135e) | morluto |
| 2026-11-20 | [test(reference): verify exclusion and missing-root outcomes (#12831)](https://github.com/morluto/rea/commit/68e6953897c1100faed203ad8af22c41c2a823a0) | morluto |
| 2026-11-20 | [test(cli): consolidate launcher alias readiness checks (#12827)](https://github.com/morluto/rea/commit/53a23c0f0ddb3edca0a34ae29632407ab2974de0) | morluto |
| 2026-11-20 | [test(compression): use a small authored framing fixture (#12829)](https://github.com/morluto/rea/commit/14bc8720c9a49dc35ff2aae8713f27a56218c259) | morluto |

[See all commits ↗](https://github.com/morluto/rea/commits)

## ⬇️ Get it

```bash
git clone https://github.com/morluto/rea.git
```
