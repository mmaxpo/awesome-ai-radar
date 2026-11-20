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
| ⭐ **Stars** | 61.1k |
| 🍴 **Forks** | 9.2k |
| 🐞 **Open issues + PRs** | [1.2k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 301.1 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44)
<sub>2026-11-19 · today</sub>

> **What's Changed**
> **Features**
> - Add capability to save files as versioned, shareable artifacts.
> **Bug Fixes**
> - Fix inline agent and crew action references relative to the flow file.
> - Stop duplicating kept separators when merging chunks.
> …

### [1.15.43](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43)
<sub>2026-11-19 · yesterday</sub>

> **What's Changed**
> **Bug Fixes**
> - Fix detection of multimodal support for Claude 5.
> **Documentation**
> - Update snapshot and changelog for v1.15.42.
> **Contributors**
> …

### [1.15.42](https://github.com/crewAIInc/crewAI/releases/tag/1.15.42)
<sub>2026-11-18 · yesterday</sub>

> **What's Changed**
> **Features**
> - Make ChromaDB an optional extra
> - Default Knowledge to local Qdrant and decouple storage from ChromaDB
> - Pick tools for standalone agents and add them later
> **Bug Fixes**
> …

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 7d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · 8d ago</sub>

> **What's Changed**
> **Features**
> - Remove chromadb from the embedding function layer.
> - Add exact historical state lookup by row id.
> - Wire jsonl into rag data type discovery.
> - Scaffold standalone agents as JSON by default.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(artifacts): never cache save_artifact tool results (#9595)](https://github.com/crewAIInc/crewAI/commit/70a31b667dad750910ea5c006b1934a41821e05e) | MaiAditya |
| 2026-11-20 | [fix(agents): set from_cache on the native tool finished event (#9504)](https://github.com/crewAIInc/crewAI/commit/8c75a465bd2c4f68ec79aa56a8bdbee8218283ed) | sunhouy |
| 2026-11-20 | [test(utilities): cover non-dict message content blocks (#9467)](https://github.com/crewAIInc/crewAI/commit/0c31a44a5a4e2c680ca5f4fde69eade3911a4908) | Sakura-798 |
| 2026-11-19 | [[docs-freeze] docs: snapshot and changelog for v1.15.44 (#9579)](https://github.com/crewAIInc/crewAI/commit/374c05392021271cabb809868282d949e0efbbe2) | Vidit-Ostwal |
| 2026-11-19 | [feat: bump versions to 1.15.44 (#9578)](https://github.com/crewAIInc/crewAI/commit/484a6e3044a2511ee44f0eb5ff425da2eb1d6dbc) | Vidit-Ostwal |
| 2026-11-19 | [chore: update litellm model catalog for v1.15.44 (#9576)](https://github.com/crewAIInc/crewAI/commit/5605f9d89c2422ba1fae6e52fa30a8e666a731c0) | Vidit-Ostwal |
| 2026-11-19 | [docs: teach the flow skill to save and read artifacts (#9575)](https://github.com/crewAIInc/crewAI/commit/17d9ec3dfdbaf2dea593a958c9cdb3f99d773c86) | gabemilani |
| 2026-11-19 | [fix(flow): resolve inline agent and crew action refs relative to the …](https://github.com/crewAIInc/crewAI/commit/fe019e19a8065b8795bd652072a4ed2065bfc52d) | adityajai119 |
| 2026-11-19 | [fix(rag): stop duplicating kept separators when merging chunks (#9488)](https://github.com/crewAIInc/crewAI/commit/1096c2aeb2bd0c373327c49cd6ad2fc2fd0fbe54) | nurlanmnn |
| 2026-11-19 | [fix(flow): isolate nested defaults from a shared flow declaration (#9…](https://github.com/crewAIInc/crewAI/commit/8f653b25447e3af5d04a2a34bd4f6bf6664f1bf1) | HanYuanLu |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
