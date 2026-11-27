# aaif-goose/goose

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/aaif-goose/goose)

> an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Extensible open-source agent that installs, runs, edits and tests code |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 57.1k |
| 🍴 **Forks** | 6.7k |
| 🐞 **Open issues + PRs** | [532](https://github.com/aaif-goose/goose/issues) |
| 💻 **Languages** | Rust 72% · TypeScript 23% · Python 1% · JavaScript 1% · Shell 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `mcp` `acp` `ai` `ai-agents` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-08-23 |
| 📦 **Latest release** | [v1.61.1](https://github.com/aaif-goose/goose/releases/tag/v1.61.1) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 980.4 MB |
| 🌐 **Website** | https://goose-docs.ai/ |

## 📦 Recent releases

### [v1.61.1](https://github.com/aaif-goose/goose/releases/tag/v1.61.1)
<sub>2026-11-26 · yesterday</sub>

> **🐛 **Bug Fixes****
> - Drop tool approval state from imported sessions to prevent automatic tool execution on session load
> - Import sessions with local extensions and goose mode, dropping recipe retry, recipe values, container and provider session IDs
> - Remove recipe template re-rendering on session load and fork
> - Remove dotenv from desktop app to prevent unintended environment variable loading
> **🔧 **Improvements****
> …

### [v1.61.0](https://github.com/aaif-goose/goose/releases/tag/v1.61.0)
<sub>2026-11-25 · 2d ago</sub>

> **✨ Features**
> - Show the provider before the model on the model button [#13491](https://github.com/aaif-goose/goose/pull/13491)
> - Gemini 4 Neon added to the model catalog [#13684](https://github.com/aaif-goose/goose/pull/13684)
> - Treat all headers as secret in mcpServers configs over ACP [#13435](https://github.com/aaif-goose/goose/pull/13435)
> - MCP extension operation for goose-agent [#13620](https://github.com/aaif-goose/goose/pull/13620)
> - Import MCP's server.json format into goose config [#11934](https://github.com/aaif-goose/goose/pull/11934)
> …

### [v1.60.2](https://github.com/aaif-goose/goose/releases/tag/v1.60.2)
<sub>2026-11-20 · 7d ago</sub>

> **✨ Features**
> - Gemini 4 Neon added to the model catalog [#13684](https://github.com/aaif-goose/goose/pull/13684)
> **🐛 Bug Fixes**
> - Thinking levels now sent to Gemini 4 and later, including xhigh [#13673](https://github.com/aaif-goose/goose/pull/13673)

### [v1.60.1](https://github.com/aaif-goose/goose/releases/tag/v1.60.1)
<sub>2026-11-18 · 9d ago</sub>

> **🐛 Bug Fixes**
> - Compaction: drop the `<analysis>` scratchpad that Claude models refuse [#13572](https://github.com/aaif-goose/goose/pull/13572)

### [v1.60.0](https://github.com/aaif-goose/goose/releases/tag/v1.60.0)
<sub>2026-11-17 · 9d ago</sub>

> **✨ Features**
> - SkillOperation and drop the Skills extension [#13574](https://github.com/aaif-goose/goose/pull/13574)
> - Executable commands and SlashCommandOperation in oi-kit [#13533](https://github.com/aaif-goose/goose/pull/13533)
> - Bang command operation in oi-kit [#13535](https://github.com/aaif-goose/goose/pull/13535)
> - Steering operation in oi-kit [#13502](https://github.com/aaif-goose/goose/pull/13502)
> - Dutch (nl) translation [#13240](https://github.com/aaif-goose/goose/pull/13240)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(desktop): stop usage-chip tooltip from flickering on hover (#13845)](https://github.com/aaif-goose/goose/commit/c546eaa1cd02696e4cd628e203df51429e158175) | nako-ruru |
| 2026-11-26 | [chore(deps-dev): bump typescript from 5.9.3 to 6.0.3 in /ui (#13796)](https://github.com/aaif-goose/goose/commit/fc176803fc22385d267fddea958cc8cf1b459f28) | dependabot[bot] |
| 2026-11-26 | [fix(desktop): auto-hide the menu bar on Linux (#13713)](https://github.com/aaif-goose/goose/commit/d1438fde28d6669e0f34cbd2ae90c5fbe903f8d1) | Abhijay007 |
| 2026-11-26 | [Add a daily new-model check workflow (#13839)](https://github.com/aaif-goose/goose/commit/162f1f5015132d04b758ebfdbf8599bc404aef0d) | lifeizhou-ap |
| 2026-11-26 | [Load Node types explicitly in goose-acp so it builds with TypeScript …](https://github.com/aaif-goose/goose/commit/9a16d1c5a3c54fc08403f1834e9b4eeabff1bc7a) | lifeizhou-ap |
| 2026-11-26 | [chore(deps-dev): bump knip from 5.88.1 to 6.48.0 in /ui (#13795)](https://github.com/aaif-goose/goose/commit/51f875e6628623ab7a378255b86b6519a4f0c17f) | dependabot[bot] |
| 2026-11-26 | [chore(deps): bump @mcp-ui/client from 6.1.0 to 7.1.1 in /ui (#13798)](https://github.com/aaif-goose/goose/commit/ef143b604409c92b501aff8010ef9fa2068ddb15) | dependabot[bot] |
| 2026-11-26 | [chore(deps-dev): bump @testing-library/jest-dom from 7.0.1 to 8.0.0 i…](https://github.com/aaif-goose/goose/commit/be4e7ebe6c43aab440bd2144ba706679d53eba51) | dependabot[bot] |
| 2026-11-26 | [chore(deps): bump jsonschema from 0.61.2 to 0.62.0 (#13800)](https://github.com/aaif-goose/goose/commit/ab7abd5645979f34616a3cda86041e883b769a0c) | dependabot[bot] |
| 2026-11-26 | [chore(deps): bump lru from 0.19.0 to 0.19.1 in the cargo-minor-and-pa…](https://github.com/aaif-goose/goose/commit/d1ff699d34339063db4d8676b9e31303b8b620b8) | dependabot[bot] |

[See all commits ↗](https://github.com/aaif-goose/goose/commits)

## ⬇️ Get it

```bash
git clone https://github.com/aaif-goose/goose.git
```
