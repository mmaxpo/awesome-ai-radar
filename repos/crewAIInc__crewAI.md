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
| ⭐ **Stars** | 61.2k |
| 🍴 **Forks** | 9.3k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.45](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 302.2 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.45](https://github.com/crewAIInc/crewAI/releases/tag/1.15.45)
<sub>2026-11-24 · today</sub>

> **What's Changed**
> **Features**
> - Add ability to save HTML or markdown output as a PDF artifact.
> **Bug Fixes**
> - Fix dependency issue by bumping e2b for Python >=3.11 to pull patched wcmatch.
> - Wrap file-like inputs in `normalize_input_files`.
> …

### [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44)
<sub>2026-11-19 · 4d ago</sub>

> **What's Changed**
> **Features**
> - Add capability to save files as versioned, shareable artifacts.
> **Bug Fixes**
> - Fix inline agent and crew action references relative to the flow file.
> - Stop duplicating kept separators when merging chunks.
> …

### [1.15.43](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43)
<sub>2026-11-19 · 5d ago</sub>

> **What's Changed**
> **Bug Fixes**
> - Fix detection of multimodal support for Claude 5.
> **Documentation**
> - Update snapshot and changelog for v1.15.42.
> **Contributors**
> …

### [1.15.42](https://github.com/crewAIInc/crewAI/releases/tag/1.15.42)
<sub>2026-11-18 · 5d ago</sub>

> **What's Changed**
> **Features**
> - Make ChromaDB an optional extra
> - Default Knowledge to local Qdrant and decouple storage from ChromaDB
> - Pick tools for standalone agents and add them later
> **Bug Fixes**
> …

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 11d ago</sub>

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
| 2026-11-24 | [test(crewai): rename Test* helper classes to avoid pytest collection …](https://github.com/crewAIInc/crewAI/commit/4772a9d9e78c5f008e221708c16c2d0ad61c18d3) | PresetyX |
| 2026-11-24 | [fix(cli): let --force bypass git validation in tool publish (#9722)](https://github.com/crewAIInc/crewAI/commit/bc9e81eb776691df1346eb1fd9acdc3203dc2014) | Kiko0301 |
| 2026-11-24 | [fix(cli): exit non-zero when tool publish refuses to run (#9724)](https://github.com/crewAIInc/crewAI/commit/881005174ffbbf5b4f9acdc02bea75426b22f1cb) | Kiko0301 |
| 2026-11-24 | [fix(files): attach Bedrock text documents the formatter supports (#9718)](https://github.com/crewAIInc/crewAI/commit/7d93587cb9998e6cea07e03ba71d06c2bfe149d1) | Kiko0301 |
| 2026-11-24 | [fix(databricks): keep result columns in schema order (#9708)](https://github.com/crewAIInc/crewAI/commit/5f2f3422df50e5967e72f0d3bdf29924225055f8) | Kiko0301 |
| 2026-11-24 | [[docs-freeze] docs: snapshot and changelog for v1.15.45 (#9714)](https://github.com/crewAIInc/crewAI/commit/29311aeb08c5ec0079d95d1fad05f3b227518f52) | joaomdmoura |
| 2026-11-24 | [feat: bump versions to 1.15.45 (#9713)](https://github.com/crewAIInc/crewAI/commit/cad1a9950ef08a58a64e3969ca205cc1c171872c) | joaomdmoura |
| 2026-11-24 | [chore: update litellm model catalog for v1.15.45 (#9712)](https://github.com/crewAIInc/crewAI/commit/e226806858b74fafe20e3241a99d5109dbf161ea) | joaomdmoura |
| 2026-11-23 | [feat: save HTML or markdown output as a PDF artifact (#9686)](https://github.com/crewAIInc/crewAI/commit/d1aa368749f932311a6c1916e63a756877cab55a) | gabemilani |
| 2026-11-23 | [fix(deps): bump e2b on Python >=3.11 to pull patched wcmatch (GHSA-53…](https://github.com/crewAIInc/crewAI/commit/6a5b80c4551a562004f342f46c8d1470627f535f) | Vidit-Ostwal |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
