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
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 301.3 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.41](https://github.com/crewAIInc/crewAI/releases/tag/1.15.41)
<sub>2026-11-12 · 5d ago</sub>

> **What's Changed**
> **Features**
> - Allow approved private URL hosts.
> **Bug Fixes**
> - Fix projects to depend on PyMuPDF 2.x.
> - Drop a real storage URL from the URL read tests.
> …

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · 6d ago</sub>

> **What's Changed**
> **Features**
> - Remove chromadb from the embedding function layer.
> - Add exact historical state lookup by row id.
> - Wire jsonl into rag data type discovery.
> - Scaffold standalone agents as JSON by default.
> …

### [1.15.39](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39)
<sub>2026-11-09 · 9d ago</sub>

> **What's Changed**
> **Documentation**
> - Document the `apps_not_connected` error on `/kickoff` and `/status`
> **Contributors**
> @joaomdmoura

### [1.15.38](https://github.com/crewAIInc/crewAI/releases/tag/1.15.38)
<sub>2026-11-08 · 9d ago</sub>

> **What's Changed**
> **Features**
> - Make gpt-6-luna crewAI's default model everywhere
> - Read spreadsheet URLs in an agent's input with tools over every row
> - Tag eval usage spans with target and a per-evaluation id
> - Add --no-open to crewai eval for headless use
> …

### [1.15.37](https://github.com/crewAIInc/crewAI/releases/tag/1.15.37)
<sub>2026-11-07 · 11d ago</sub>

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
| 2026-11-18 | [fix(task): store output_json values as JSON so dates don't break .jso…](https://github.com/crewAIInc/crewAI/commit/435262c638173ef9a97e4ed58bbde16af33f254b) | adityajai119 |
| 2026-11-18 | [test(task): stop a timed-out worker leaking into the next test's cass…](https://github.com/crewAIInc/crewAI/commit/d1ea657a33661aa2d5354d6f69016ad8a582f298) | Vidit-Ostwal |
| 2026-11-18 | [fix(flow): give each Flow its own id from an initial_state instance (…](https://github.com/crewAIInc/crewAI/commit/999badb1979634e8d03506bc0789a44bae99c171) | bballhaus |
| 2026-11-17 | [ci: route community-tool issues (#8283)](https://github.com/crewAIInc/crewAI/commit/2688bb6b8c329a4af72ef822c8056f2eaa83c995) | Vidit-Ostwal |
| 2026-11-17 | [feat(knowledge): default Knowledge to local Qdrant and decouple stora…](https://github.com/crewAIInc/crewAI/commit/ea5616d032505e0cfce89b0430411442fcee4a4a) | Vidit-Ostwal |
| 2026-11-17 | [fix(deps): bump mail-parser to 4.6.3+ to fix GHSA advisories (#9522)](https://github.com/crewAIInc/crewAI/commit/b8dcb3d7dd7dcf28be319880cfd1ca2677642850) | Vidit-Ostwal |
| 2026-11-16 | [fix(agent): honor max_execution_time without waiting for the worker (…](https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43) | Kiko0301 |
| 2026-11-16 | [fix(crew): save task outputs that hold urls and other pydantic types …](https://github.com/crewAIInc/crewAI/commit/e26fe73c86a3e547ff75de2c3e336cedd40c086f) | adityajai119 |
| 2026-11-16 | [fix(experimental): read the experiment baseline as UTF-8 (#9297)](https://github.com/crewAIInc/crewAI/commit/758b2c1d527e433750c46a06baa93708057d9d4d) | lxcxjxhx |
| 2026-11-16 | [fix(utilities): prefix sanitized tool names that start with a digit (…](https://github.com/crewAIInc/crewAI/commit/facbad10df94611158fb76d43670046642b298eb) | HhH666-ux |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
