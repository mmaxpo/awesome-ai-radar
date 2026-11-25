# crewAIInc/crewAI

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/crewAIInc/crewAI)

> Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Role-based agent teams (crews) working on tasks |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 61.3k |
| 🍴 **Forks** | 9.3k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.45](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 302.4 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.45](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45)
<sub>2026-11-24 · yesterday</sub>

> **What's Changed**
> **Features**
> - Add ability to save HTML or markdown output as a PDF artifact.
> **Bug Fixes**
> - Fix dependency issue by bumping e2b for Python >=3.11 to pull patched wcmatch.
> - Wrap file-like inputs in `normalize_input_files`.
> …

### [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44)
<sub>2026-11-19 · 5d ago</sub>

> **What's Changed**
> **Features**
> - Add capability to save files as versioned, shareable artifacts.
> **Bug Fixes**
> - Fix inline agent and crew action references relative to the flow file.
> - Stop duplicating kept separators when merging chunks.
> …

### [1.15.43](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43)
<sub>2026-11-19 · 6d ago</sub>

> **What's Changed**
> **Bug Fixes**
> - Fix detection of multimodal support for Claude 5.
> **Documentation**
> - Update snapshot and changelog for v1.15.42.
> **Contributors**
> …

### [1.15.42](https://github.com/crewAIInc/crewAI/releases/tag/1.15.42)
<sub>2026-11-18 · 6d ago</sub>

> **What's Changed**
> **Features**
> - Make ChromaDB an optional extra
> - Default Knowledge to local Qdrant and decouple storage from ChromaDB
> - Pick tools for standalone agents and add them later
> **Bug Fixes**
> …

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 12d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [fix(cli): report deploy list API errors instead of no crews (#9756)](https://github.com/crewAIInc/crewAI/commit/97f2424963d829c4eb40b38e3e4bd5f57495df02) | Kiko0301 |
| 2026-11-25 | [fix(cli): exit non-zero when an API response is rejected (#9754)](https://github.com/crewAIInc/crewAI/commit/7e663547cd247f5ce76567ec7b4a0322676e65a4) | Kiko0301 |
| 2026-11-25 | [fix(gemini): send seed and penalty settings in the request config (#9…](https://github.com/crewAIInc/crewAI/commit/72a2028728c5002356ccb488fbe31b9f73dde1fa) | abhishekacharya200 |
| 2026-11-25 | [fix(bedrock): honor timeout and max_retries in the native provider (#…](https://github.com/crewAIInc/crewAI/commit/8a775f0a9cd0849f68f6816282c98b2f2123df22) | yihongkun |
| 2026-11-25 | [fix(tools): read DB2_CONNECTION_STRING when connection_string is omit…](https://github.com/crewAIInc/crewAI/commit/07e2c6996ff51563ce2d8277b0928d6e2423f8b8) | Kiko0301 |
| 2026-11-25 | [fix(tools): accept the documented api_key in BraveSearchTool (#9766)](https://github.com/crewAIInc/crewAI/commit/fffe7bc9db78e8d5b82d56b73a94d36680286b87) | Kiko0301 |
| 2026-11-25 | [fix(cli): exit 1 when a crewai tool command fails (#9767)](https://github.com/crewAIInc/crewAI/commit/23ad2674e659460e9fc00e3521b88762a4f4baa9) | Kiko0301 |
| 2026-11-25 | [feat(cli): offer crewai login when a signed-out crewai eval needs an …](https://github.com/crewAIInc/crewAI/commit/ba2bd50f70069e3079eed29bb9cbed3f777c548b) | alexmarchenko-crewai |
| 2026-11-25 | [fix(artifacts): refuse hidden files in save_artifact (#9737)](https://github.com/crewAIInc/crewAI/commit/d96633c881ce5f6e9039337e970e149b5d617815) | gabemilani |
| 2026-11-25 | [ci: re-enable pytest-split durations with per-suite files (#9728)](https://github.com/crewAIInc/crewAI/commit/5c4d23995d012736db0be8528161e24b566fdba6) | Vidit-Ostwal |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
