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
| ⭐ **Stars** | 60.8k |
| 🍴 **Forks** | 9.2k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/crewAIInc/crewAI/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `llms` `aiagentframework` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2023-10-27 |
| 📦 **Latest release** | [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 300.3 MB |
| 🌐 **Website** | https://crewai.com |

## 📦 Recent releases

### [1.15.40](https://github.com/crewAIInc/crewAI/releases/tag/1.15.40)
<sub>2026-11-11 · today</sub>

> **What's Changed**
> **Features**
> - Remove chromadb from the embedding function layer.
> - Add exact historical state lookup by row id.
> - Wire jsonl into rag data type discovery.
> - Scaffold standalone agents as JSON by default.
> …

### [1.15.39](https://github.com/crewAIInc/crewAI/releases/tag/1.15.39)
<sub>2026-11-09 · 3d ago</sub>

> **What's Changed**
> **Documentation**
> - Document the `apps_not_connected` error on `/kickoff` and `/status`
> **Contributors**
> @joaomdmoura

### [1.15.38](https://github.com/crewAIInc/crewAI/releases/tag/1.15.38)
<sub>2026-11-08 · 3d ago</sub>

> **What's Changed**
> **Features**
> - Make gpt-6-luna crewAI's default model everywhere
> - Read spreadsheet URLs in an agent's input with tools over every row
> - Tag eval usage spans with target and a per-evaluation id
> - Add --no-open to crewai eval for headless use
> …

### [1.15.37](https://github.com/crewAIInc/crewAI/releases/tag/1.15.37)
<sub>2026-11-07 · 5d ago</sub>

> **What's Changed**
> **Features**
> - Add functionality to read spreadsheets for agents in crewai-files.
> - Scaffold and load standalone agent projects.
> **Documentation**
> - Update RagTool description for better parsing by Mintlify.
> …

### [1.15.36](https://github.com/crewAIInc/crewAI/releases/tag/1.15.36)
<sub>2026-11-06 · 6d ago</sub>

> **What's Changed**
> **Features**
> - Add experimental conversational Agent sessions.
> - Ask for a missing API key when crewai run starts.
> - Record the error class when crewai run cannot load a project.
> - Name the apps CrewAI AMP cannot resolve for an agent.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [fix(llm): strip cache_breakpoint marker on the LiteLLM path (OSS-272)…](https://github.com/crewAIInc/crewAI/commit/34c64226526715def00afe8486d394efee0fbb48) | Vidit-Ostwal |
| 2026-11-11 | [[docs-freeze] docs: snapshot and changelog for v1.15.40 (#9377)](https://github.com/crewAIInc/crewAI/commit/7e4efa91c57a02646c9e7b7b7355d149f0783126) | lorenzejay |
| 2026-11-11 | [feat: bump versions to 1.15.40 (#9376)](https://github.com/crewAIInc/crewAI/commit/1b28f5b6ca2a7471ee6887f5b4e46e9b0d7ec85b) | lorenzejay |
| 2026-11-11 | [chore: update litellm model catalog for v1.15.40 (#9375)](https://github.com/crewAIInc/crewAI/commit/5a9aa4c81618e57771784dfa646412817fd98594) | lorenzejay |
| 2026-11-11 | [feat(rag): remove chromadb from the embedding function layer (#8934)](https://github.com/crewAIInc/crewAI/commit/71d68117e38f620dff02ec1dc358f37a1f74a740) | Vidit-Ostwal |
| 2026-11-11 | [fix(llm): run after_llm_call hooks on async calls (#9360)](https://github.com/crewAIInc/crewAI/commit/4254a835b1e5433d123e201928612bc692edbc3e) | Kiko0301 |
| 2026-11-10 | [feat(flow): add exact historical state lookup by row id (#8272)](https://github.com/crewAIInc/crewAI/commit/0b8b216db35eec36610b5e08c31eb31a29f5c9c1) | sallyw02 |
| 2026-11-10 | [feat(tools): wire jsonl into rag data type discovery (#8754)](https://github.com/crewAIInc/crewAI/commit/c358daab14fc5e6b6192365848c6e0d208d7524d) | AadeshSalecha |
| 2026-11-10 | [test(memory): add async parity and restart-persistence contract tests…](https://github.com/crewAIInc/crewAI/commit/1357d23aafb5d3a612a19562fe9b8e2b0c899307) | AadeshSalecha |
| 2026-11-10 | [test(llms): add bedrock content and usage contract tests (#9096)](https://github.com/crewAIInc/crewAI/commit/ed558c55475cbf4613b80dbf1ef7f15256774b87) | bballhaus |

[See all commits ↗](https://github.com/crewAIInc/crewAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crewAIInc/crewAI.git
```
