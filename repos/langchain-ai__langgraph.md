# langchain-ai/langgraph

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/langchain-ai/langgraph)

> Build resilient agents.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | TCOS |
| **Why it's worth a look** | Build resilient, stateful agents as graphs |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 45.4k |
| 🍴 **Forks** | 7.9k |
| 🐞 **Open issues + PRs** | [490](https://github.com/langchain-ai/langgraph/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `ai-agents` `chatgpt` `deepagents` `enterprise` `framework` `gemini` `generative-ai` `langchain` `langgraph` `llm` `multiagent` `open-source` `openai` `pydantic` `python` `rag` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-08-09 |
| 📦 **Latest release** | [1.2.24](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 522.1 MB |
| 🌐 **Website** | https://docs.langchain.com/oss/python/langgraph/ |

## 📦 Recent releases

### [1.2.24](https://github.com/langchain-ai/langgraph/releases/tag/1.2.24) — langgraph==1.2.24
<sub>2026-11-20 · 5d ago</sub>

> Changes since 1.2.23
> * release(langgraph): 1.2.24 (#9752)
> * fix(langgraph): handle `REMOVE_ALL_MESSAGES` in `_messages_delta_reducer` and `None` checkpoints in `DeltaChannel` (#9735)

### [1.2.23](https://github.com/langchain-ai/langgraph/releases/tag/1.2.23) — langgraph==1.2.23
<sub>2026-11-19 · 6d ago</sub>

> Changes since 1.2.22
> * release(langgraph): 1.2.23 (#9742)
> * release(prebuilt): 1.1.3 (#9741)
> * fix(langgraph,prebuilt): give Send-dispatched tool calls the same state as an edge (#9728)
> * chore(deps): bump opentelemetry-api from 1.45.1 to 1.45.2 in /libs/langgraph (#9696)
> * fix(langgraph): avoid warning races in dynamic schemas (#9716)

### [prebuilt==1.1.3](https://github.com/langchain-ai/langgraph/releases/tag/prebuilt%3D%3D1.1.3) — langgraph-prebuilt==1.1.3
<sub>2026-11-19 · 6d ago</sub>

> Changes since prebuilt==1.1.2
> * release(prebuilt): 1.1.3 (#9741)
> * fix(langgraph,prebuilt): give Send-dispatched tool calls the same state as an edge (#9728)
> * fix(prebuilt): make wrap_tool_call state overrides reach the tool (#9730)

### [1.2.22](https://github.com/langchain-ai/langgraph/releases/tag/1.2.22) — langgraph==1.2.22
<sub>2026-11-14 · 11d ago</sub>

> Changes since 1.2.21
> * release(langgraph): 1.2.22 (#9702)
> * release(checkpoint-postgres): 3.2.1 (#9700)
> * release(prebuilt): 1.1.2 (#9701)
> * release(checkpoint): 4.3.2 (#9699)
> * fix(langgraph): stream a child graph on its own thread to a caller streaming subgraphs (#9698)
> …

### [checkpointpostgres==3.2.1](https://github.com/langchain-ai/langgraph/releases/tag/checkpointpostgres%3D%3D3.2.1) — langgraph-checkpoint-postgres==3.2.1
<sub>2026-11-14 · 11d ago</sub>

> Changes since checkpointpostgres==3.2.0
> * release(checkpoint-postgres): 3.2.1 (#9700)
> * release(checkpoint): 4.3.2 (#9699)
> * perf(checkpoint-postgres): run a lone store read outside a pipeline (#9635)
> * perf(checkpoint-postgres): skip the async saver's lock for connection pools (#9638)
> * perf(checkpoint-postgres): load no pending writes without a thread hop (#9639)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [fix(langgraph): give add_messages writes and StateGraph input message…](https://github.com/langchain-ai/langgraph/commit/f96105368f9e9385d4c9e38bffaa457aba17f095) | sera-wi |
| 2026-11-24 | [fix(langgraph): stream tool events live with stream_mode="tools" alon…](https://github.com/langchain-ai/langgraph/commit/732da52047a1658cccffca86ac27396871b3f385) | eliornl |
| 2026-11-24 | [fix(langgraph): add "tools" to the public `StreamMode` type (#9778)](https://github.com/langchain-ai/langgraph/commit/58d4a1c8d78eecdb1503a3d3d35ed2232f91c46a) | eliornl |
| 2026-11-24 | [refactor(langgraph): name the `__root__` channel with a `ROOT` consta…](https://github.com/langchain-ai/langgraph/commit/b4fe40f8108cea6a8314aaaafc7680395a257e3f) | sera-wi |
| 2026-11-20 | [fix(cli): omit an empty secrets list when updating a deployment (#9737)](https://github.com/langchain-ai/langgraph/commit/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c) | raghavverma-langchain |
| 2026-11-20 | [chore(deps): bump the minor-and-patch group across 1 directory with 8…](https://github.com/langchain-ai/langgraph/commit/01d7b9e17b3dcf803cf0df6593930534f194d546) | dependabot[bot] |
| 2026-11-20 | [release(langgraph): 1.2.24 (#9752)](https://github.com/langchain-ai/langgraph/commit/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b) | sera-wi |
| 2026-11-19 | [fix(langgraph): handle `REMOVE_ALL_MESSAGES` in `_messages_delta_redu…](https://github.com/langchain-ai/langgraph/commit/8aea1fea7fb4d23344b5c3714ab86694f7744a26) | sera-wi |
| 2026-11-19 | [fix(sdk-py): publish integration progress events on a named channel (…](https://github.com/langchain-ai/langgraph/commit/37becf152a341e21a6e391e8702659a437835a73) | sera-wi |
| 2026-11-19 | [release(langgraph): 1.2.23 (#9742)](https://github.com/langchain-ai/langgraph/commit/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93) | eliornl |

[See all commits ↗](https://github.com/langchain-ai/langgraph/commits)

## ⬇️ Get it

```bash
git clone https://github.com/langchain-ai/langgraph.git
```
