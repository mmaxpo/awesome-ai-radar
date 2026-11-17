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
| ⭐ **Stars** | 61.0k |
| 🍴 **Forks** | 9.2k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 300.1 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 4d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · 5d ago</sub>

> **What's Changed**
> **Features**
> - Remove chromadb from the embedding function layer.
> - Add exact historical state lookup by row id.
> - Wire jsonl into rag data type discovery.
> - Scaffold standalone agents as JSON by default.
> …

### [1.15.39](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39)
<sub>2026-11-09 · 8d ago</sub>

> **What's Changed**
> **Documentation**
> - Document the `apps_not_connected` error on `/kickoff` and `/status`
> **Contributors**
> @joaomdmoura

### [1.15.38](https://github.com/crewAIInc/crewAI/releases/tag/1.15.38)
<sub>2026-11-08 · 8d ago</sub>

> **What's Changed**
> **Features**
> - Make gpt-6-luna crewAI's default model everywhere
> - Read spreadsheet URLs in an agent's input with tools over every row
> - Tag eval usage spans with target and a per-evaluation id
> - Add --no-open to crewai eval for headless use
> …

### [1.15.37](https://github.com/crewAIInc/crewAI/releases/tag/1.15.37)
<sub>2026-11-07 · 10d ago</sub>

> **What's Changed**
> **Features**
> - Add functionality to read spreadsheets for agents in crewai-files.
> - Scaffold and load standalone agent projects.
> **Documentation**
> - Update RagTool description for better parsing by Mintlify.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(agent): honor max_execution_time without waiting for the worker (…](https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43) | Kiko0301 |
| 2026-11-16 | [fix(crew): save task outputs that hold urls and other pydantic types …](https://github.com/crewAIInc/crewAI/commit/e26fe73c86a3e547ff75de2c3e336cedd40c086f) | adityajai119 |
| 2026-11-16 | [fix(experimental): read the experiment baseline as UTF-8 (#9297)](https://github.com/crewAIInc/crewAI/commit/758b2c1d527e433750c46a06baa93708057d9d4d) | lxcxjxhx |
| 2026-11-16 | [fix(utilities): prefix sanitized tool names that start with a digit (…](https://github.com/crewAIInc/crewAI/commit/facbad10df94611158fb76d43670046642b298eb) | HhH666-ux |
| 2026-11-16 | [fix(memory): count scoped LanceDB records exactly above 50,000 rows (…](https://github.com/crewAIInc/crewAI/commit/2817a951f308bf477d4b221d3f3047ade3f97b61) | Varshith-Kali |
| 2026-11-15 | [fix(tools): report Serply's hybrid flag from its own field (#9358)](https://github.com/crewAIInc/crewAI/commit/364b87959014b51933f59ed1a95f463d19224f36) | Kiko0301 |
| 2026-11-15 | [fix(tools): let TavilyResearchTool's configured defaults apply (#9359)](https://github.com/crewAIInc/crewAI/commit/ab8588771a6077f8620590306999f683278fb431) | Kiko0301 |
| 2026-11-15 | [fix(rag): normalize flat Chroma metadata filters (#9403)](https://github.com/crewAIInc/crewAI/commit/bf6fd3a0972dd72fe1ff568c243e87e3b8408d35) | jjhong011001 |
| 2026-11-15 | [fix(rag): handle CSV record newlines without translating cell values …](https://github.com/crewAIInc/crewAI/commit/f98e2923a0b4523fbd11994ae6b1093beb338fb2) | lakers-abing |
| 2026-11-15 | [fix(project): load json crew and agent files saved with a utf-8 bom (…](https://github.com/crewAIInc/crewAI/commit/574a09e84c3ba7823914a1df526723138d589f6f) | adityajai119 |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
