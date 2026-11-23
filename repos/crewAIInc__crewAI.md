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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 302.2 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.44](https://github.com/crewAIInc/crewAI/releases/tag/1.15.44)
<sub>2026-11-19 · 3d ago</sub>

> **What's Changed**
> **Features**
> - Add capability to save files as versioned, shareable artifacts.
> **Bug Fixes**
> - Fix inline agent and crew action references relative to the flow file.
> - Stop duplicating kept separators when merging chunks.
> …

### [1.15.43](https://github.com/crewAIInc/crewAI/releases/tag/1.15.43)
<sub>2026-11-19 · 4d ago</sub>

> **What's Changed**
> **Bug Fixes**
> - Fix detection of multimodal support for Claude 5.
> **Documentation**
> - Update snapshot and changelog for v1.15.42.
> **Contributors**
> …

### [1.15.42](https://github.com/crewAIInc/crewAI/releases/tag/1.15.42)
<sub>2026-11-18 · 4d ago</sub>

> **What's Changed**
> **Features**
> - Make ChromaDB an optional extra
> - Default Knowledge to local Qdrant and decouple storage from ChromaDB
> - Pick tools for standalone agents and add them later
> **Bug Fixes**
> …

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 10d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · 11d ago</sub>

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
| 2026-11-23 | [fix(deps): bump e2b on Python >=3.11 to pull patched wcmatch (GHSA-53…](https://github.com/crewAIInc/crewAI/commit/6a5b80c4551a562004f342f46c8d1470627f535f) | Vidit-Ostwal |
| 2026-11-23 | [fix(files): wrap file-like inputs in normalize_input_files (#9626)](https://github.com/crewAIInc/crewAI/commit/3c53d5073b5f29cfbf707cfa79e5843f11162a87) | Kiko0301 |
| 2026-11-23 | [fix(cli): reject negative checkpoint prune retention counts (#9676)](https://github.com/crewAIInc/crewAI/commit/6eceb811a6f67d945fa509057302678bef0d980c) | Kelvin-Waititu |
| 2026-11-23 | [fix(crewai-tools): report MongoDB tool's real env vars (#9622)](https://github.com/crewAIInc/crewAI/commit/6ecb873903345022637d758e7df6532b260d0a61) | Kiko0301 |
| 2026-11-23 | [fix(files): let prefer_upload enable Bedrock S3 uploads (#9624)](https://github.com/crewAIInc/crewAI/commit/2d840d0e86c11ffe00f8f9fe3a8e4fb7ea5d2186) | Kiko0301 |
| 2026-11-23 | [fix(converter): validate foreign models against the target schema (#9…](https://github.com/crewAIInc/crewAI/commit/7cc18c55e195778df2f64e9a6bd05f9cb29a5adf) | jjhong011001 |
| 2026-11-23 | [fix(files): preserve narrow dimensions when resizing images (#9605)](https://github.com/crewAIInc/crewAI/commit/e184e58cde6ad7e46eaf9ae9c9c05efaac483d18) | nazek52 |
| 2026-11-23 | [fix(a2a): reject empty credentials and use constant-time comparison i…](https://github.com/crewAIInc/crewAI/commit/77786fe99e0b183b9ce83558fb191b90fbb95382) | SDLSY |
| 2026-11-23 | [fix(tools): make HyperbrowserLoadTool params optional in its schema (…](https://github.com/crewAIInc/crewAI/commit/d84514b5eee2598816f7ea11dc0b5889cfb23dfd) | kushagra0526 |
| 2026-11-21 | [docs(files): document anthropic file blocks carry no cache_control (#…](https://github.com/crewAIInc/crewAI/commit/56c26a7fb3ece62c64de52e8b4228d15c9c81492) | joaomdmoura |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
