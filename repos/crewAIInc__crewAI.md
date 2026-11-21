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
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 301.4 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44)
<sub>2026-11-19 · yesterday</sub>

> **What's Changed**
> **Features**
> - Add capability to save files as versioned, shareable artifacts.
> **Bug Fixes**
> - Fix inline agent and crew action references relative to the flow file.
> - Stop duplicating kept separators when merging chunks.
> …

### [1.15.43](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43)
<sub>2026-11-19 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes**
> - Fix detection of multimodal support for Claude 5.
> **Documentation**
> - Update snapshot and changelog for v1.15.42.
> **Contributors**
> …

### [1.15.42](https://github.com/crewAIInc/crewAI/releases/tag/1.15.42)
<sub>2026-11-18 · 2d ago</sub>

> **What's Changed**
> **Features**
> - Make ChromaDB an optional extra
> - Default Knowledge to local Qdrant and decouple storage from ChromaDB
> - Pick tools for standalone agents and add them later
> **Bug Fixes**
> …

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 8d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · 9d ago</sub>

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
| 2026-11-21 | [docs(files): document anthropic file blocks carry no cache_control (#…](https://github.com/crewAIInc/crewAI/commit/56c26a7fb3ece62c64de52e8b4228d15c9c81492) | joaomdmoura |
| 2026-11-20 | [fix(a2a): require a secret for HMAC webhook signatures (#9459)](https://github.com/crewAIInc/crewAI/commit/f6f01ddf4300e88134bbac6dfb1762b4d75c19b0) | Kiko0301 |
| 2026-11-20 | [fix(schema): keep fields with explicit non-null defaults non-nullable…](https://github.com/crewAIInc/crewAI/commit/b84960112ba19b110d9a49fd905f037894b0d0d4) | lkuko |
| 2026-11-20 | [fix(llms): keep a streamed Azure delta when its chunk also carries us…](https://github.com/crewAIInc/crewAI/commit/0da44f6f7815a7e476b9c5f5bce50cc7d462952c) | YeChenglin8888 |
| 2026-11-20 | [fix(files): reject non-positive text chunk sizes (#9520)](https://github.com/crewAIInc/crewAI/commit/9812f6c1c536e487e4e2612d45099fff1c054798) | Kiko0301 |
| 2026-11-20 | [fix(tools): drop credentials on cross-origin redirects (#9516)](https://github.com/crewAIInc/crewAI/commit/3aeb98a271bb1d32ba1991ba2def1afb7aa82e89) | Kiko0301 |
| 2026-11-20 | [fix(knowledge): stop chunking once a chunk reaches the end of the tex…](https://github.com/crewAIInc/crewAI/commit/fdbffa0ca3138a1e7c169e739ae9c2c6a41ab405) | Ayushraj06-bit |
| 2026-11-20 | [fix: serialize enums by value in CrewJSONEncoder (#9582)](https://github.com/crewAIInc/crewAI/commit/c24960bda1d34d9038d7da92c3eee18275331feb) | nurlanmnn |
| 2026-11-20 | [fix(artifacts): never cache save_artifact tool results (#9595)](https://github.com/crewAIInc/crewAI/commit/70a31b667dad750910ea5c006b1934a41821e05e) | MaiAditya |
| 2026-11-20 | [fix(agents): set from_cache on the native tool finished event (#9504)](https://github.com/crewAIInc/crewAI/commit/8c75a465bd2c4f68ec79aa56a8bdbee8218283ed) | sunhouy |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
