# FlowiseAI/Flowise

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/FlowiseAI/Flowise)

> Build AI Agents, Visually

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Visual builder for LLM flows and agents |
| **Added** | 2026-11-11 |

🗄 **Archived** — no longer maintained

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 55.6k |
| 🍴 **Forks** | 25.1k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/FlowiseAI/Flowise/issues) |
| 💻 **Languages** | TypeScript 62% · JavaScript 27% · HTML 6% · Handlebars 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `artificial-intelligence` `chatgpt` `large-language-models` `low-code` `no-code` `javascript` `react` `typescript` `langchain` `openai` `rag` `chatbot` `workflow-automation` `agentic-ai` `agentic-workflow` `agents` `multiagent-systems` |
| 🕒 **Last activity** | 2026-08-13 (3mo ago) |
| 📅 **Created** | 2023-03-31 |
| 📦 **Latest release** | [flowise@3.1.4](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.4) — 2026-07-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 81.0 MB |
| 🌐 **Website** | https://flowiseai.com |

## 📦 Recent releases

### [flowise@3.1.4](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.4)
<sub>2026-07-29 · 3mo ago</sub>

> **What's Changed**
> * Fix Type Validation For Session ID by @yau-wd in https://github.com/FlowiseAI/Flowise/pull/6568
> * Fix Flowise 709 Make Custom MCP stdio command allowlist operator-controlled by @yau-wd in https://github.com/FlowiseAI/Flowise/pull/6578
> * Fix Flowise 610 openai-realtime cross-workspace authorization by @yau-wd in https://github.com/FlowiseAI/Flowise/pull/6586
> * fix: exports contain variable values by @0xi4o in https://github.com/FlowiseAI/Flowise/pull/6556
> * Fix Flowise 722 node load method workspace by @yau-wd in https://github.com/FlowiseAI/Flowise/pull/6593
> …

### [flowise@3.1.3](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.3)
<sub>2026-06-25 · 4mo ago</sub>

> **What's Changed**
> * Fix clickjacking by @yau-wd in https://github.com/FlowiseAI/Flowise/pull/6185
> * fix(agentflow): add onFlowChange notifications for deleteNode, deleteEdge, and duplicateNode actions by @jocelynlin-wd in https://github.com/FlowiseAI/Flowise/pull/6211
> * Fix: Clean and Nuke Script by @abdullah-workday in https://github.com/FlowiseAI/Flowise/pull/6213
> * feat(agentflow): add client filtering for form input options in Start node by @jocelynlin-wd in https://github.com/FlowiseAI/Flowise/pull/6212
> * feat: turn chatflow into MCP server by @prd-hoang-doan in https://github.com/FlowiseAI/Flowise/pull/5930
> …

### [flowise@3.1.2](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.2)
<sub>2026-04-14 · 7mo ago</sub>

> **What's Changed**
> * Hardcoded CORS wildcard on TTS endpoint enables cross-origin credential abuse from any webpage by @christopherholland-workday in https://github.com/FlowiseAI/Flowise/pull/5901
> * Additional Improvements to MCP Server Config security by @christopherholland-workday in https://github.com/FlowiseAI/Flowise/pull/5943
> * fix: session cleanup when using mysql for storing sessions by @0xi4o in https://github.com/FlowiseAI/Flowise/pull/5984
> * Fix Mass Assignment in Tools Endpoint by @christopherholland-workday in https://github.com/FlowiseAI/Flowise/pull/5954
> * Fix Credential Data Leak by @christopherholland-workday in https://github.com/FlowiseAI/Flowise/pull/6042
> …

### [flowise@3.1.1](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.1)
<sub>2026-03-23 · 7mo ago</sub>

> **What's Changed**
> * Traversal env var by @christopherholland-workday in https://github.com/FlowiseAI/Flowise/pull/5962
> * Fix/agentflow model parameters by @j-sanaa in https://github.com/FlowiseAI/Flowise/pull/5967
> * fix: migrate Weaviate to weaviate-client v3 for agentKnowledgeVSEmbeddings compatibility (#5991) by @aayushbaluni in https://github.com/FlowiseAI/Flowise/pull/5993
> * feat(agentflow): add Rich Text editor for Content Editing (FLOWISE-342) by @jocelynlin-wd in https://github.com/FlowiseAI/Flowise/pull/5988
> * chore: bump @flowiseai/agentflow to 0.0.0-dev.4 by @github-actions[bot] in https://github.com/FlowiseAI/Flowise/pull/5997
> …

### [flowise@3.1.0](https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.0)
<sub>2026-03-16 · 8mo ago</sub>

> **⚠️ Breaking Changes**
> **HTTP security checks enabled by default**
> Flowise now enables **HTTP security validation by default** to prevent requests to unsafe or internal domains.
> A built-in deny list blocks potentially dangerous domains (for example `localhost`, `127.0.0.1`, and other internal addresses) to mitigate SSRF and similar attacks.
> Two new environment variables control this behavior:
> ```bash
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-08-13 | [Update README.md (#6728)](https://github.com/FlowiseAI/Flowise/commit/9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb) | HenryHengZJ |
| 2026-08-10 | [Fix Flowise 746 Chat Message Route (#6719)](https://github.com/FlowiseAI/Flowise/commit/abe4a8601a058047b350c260676826e21dd14101) | yau-wd |
| 2026-08-07 | [add: permissions for bullmq endpoint (#6713)](https://github.com/FlowiseAI/Flowise/commit/1939b5f3747eff2641f3b7332e9fff33d637fbee) | 0xi4o |
| 2026-08-07 | [fix: flowise-707 (#6712)](https://github.com/FlowiseAI/Flowise/commit/4b805e051f7b952bda3b2407d4ac334f518ff460) | 0xi4o |
| 2026-08-07 | [fix: flowise-603 (#6708)](https://github.com/FlowiseAI/Flowise/commit/0b74fc07ebd2f87a7c393d442f09aab76255bbbd) | 0xi4o |
| 2026-08-07 | [fix: flowise-766 (#6709)](https://github.com/FlowiseAI/Flowise/commit/f20d0941da566cb5e5217556ea8b03908752a303) | 0xi4o |
| 2026-08-07 | [fix: upsert history permissions (#6680)](https://github.com/FlowiseAI/Flowise/commit/269a493712aee231889795cd29ddf8060f4c2283) | 0xi4o |
| 2026-08-03 | [feat(security): Sunset notice (#6692)](https://github.com/FlowiseAI/Flowise/commit/ba4c6509bbc481cc7f01aab3d1aa33a2aea886f1) | igor-magun-wd |
| 2026-07-31 | [fix: flowise-627 (#6673)](https://github.com/FlowiseAI/Flowise/commit/fe285d0b8d0ea8c51c6e0ad80fb6b2a6b5a957ac) | 0xi4o |
| 2026-07-31 | [fix: flowise-708 (#6679)](https://github.com/FlowiseAI/Flowise/commit/754f3d4747337ec27458a7848e0aa372581d7641) | 0xi4o |

[See all commits ↗](https://github.com/FlowiseAI/Flowise/commits)

## ⬇️ Get it

```bash
git clone https://github.com/FlowiseAI/Flowise.git
```
