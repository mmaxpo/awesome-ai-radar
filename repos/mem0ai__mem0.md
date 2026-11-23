# mem0ai/mem0

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/mem0ai/mem0)

> The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | TCOS |
| **Why it's worth a look** | Drop-in memory layer for AI agents |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 69.4k |
| 🍴 **Forks** | 8.3k |
| 🐞 **Open issues + PRs** | [982](https://github.com/mem0ai/mem0/issues) |
| 💻 **Languages** | Python 58% · TypeScript 40% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai` `chatgpt` `llm` `python` `rag` `long-term-memory` `memory` `memory-management` `state-management` `ai-agents` `agents` `genai` `agentic-memory` `agentic-memory-system` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-06-20 |
| 📦 **Latest release** | [ts-v3.3.1](https://github.com/mem0ai/mem0/releases/tag/ts-v3.3.1) — 2026-09-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 68.1 MB |
| 🌐 **Website** | https://mem0.ai |

## 📦 Recent releases

### [ts-v3.3.1](https://github.com/mem0ai/mem0/releases/tag/ts-v3.3.1) — Mem0 Node SDK (v3.3.1)
<sub>2026-09-25 · 1mo ago</sub>

> **Bug Fixes:**
> - **Config (OSS):** `ConfigManager` no longer injects OpenAI's default `baseURL` and `model` into non-OpenAI LLM providers. The defaults now apply only to `openai` and `openai_structured`, so a DeepSeek, xAI, or other provider config without an explicit `baseURL` or `model` falls back to that provider's own defaults and env vars (`DEEPSEEK_API_BASE`, `XAI_API_BASE`, ...) instead of pointing at OpenAI with an OpenAI model name ([#7350](https://github.com/mem0ai/mem0/pull/7350))
> - **Vector Stores:** Turbopuffer filters now apply every operator (`eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`). Only the range operators were read before, so `eq`, `ne`, `in`, and `nin` were silently dropped. A `"*"` value now matches anything instead of nothing, an array value is treated as `in`, and an unsupported operator throws ([#6578](https://github.com/mem0ai/mem0/pull/6578))
> - **Vector Stores:** Turbopuffer `search()` with `euclidean_squared` now maps the unbounded squared distance to `1 / (1 + distance)` instead of `1 - distance`, which went negative and inverted ranking for any distance above 1 ([#6580](https://github.com/mem0ai/mem0/pull/6580))
> - **Packaging:** `pg`, `@types/pg`, and `natural` are now optional peer dependencies, and `pg` / `@types/pg` accept caret ranges instead of the exact `8.11.3` / `8.11.0` pins, so installing `mem0ai` no longer pulls in `pg` or conflicts with an app's own `pg` version. The PGVector store now imports `pg` only when it is used, so install it alongside `mem0ai` (`npm install pg`) if you use that store. `@types/jest` moved from peer dependencies to dev dependencies ([#7450](https://github.com/mem0ai/mem0/pull/7450))

### [v2.2.1](https://github.com/mem0ai/mem0/releases/tag/v2.2.1) — Mem0 Python SDK (v2.2.1)
<sub>2026-09-25 · 1mo ago</sub>

> **Bug Fixes:**
> - **Core:** `add()` (`Memory` and `AsyncMemory`) no longer reports records the vector store rejected as successful `ADD` events. Only records that were actually inserted are written to history, entity-linked, and returned. If none of the extracted memories could be inserted, `add()` now raises `VectorStoreError` instead of returning memories that were never stored ([#7066](https://github.com/mem0ai/mem0/pull/7066))
> - **Core:** Restore the context-manager protocol on `Memory` (`with Memory() as m:`) and `AsyncMemory` (`async with AsyncMemory() as m:`), which closes the instance on exit ([#7354](https://github.com/mem0ai/mem0/pull/7354))
> - **LLMs:** The AWS Bedrock Anthropic path now returns the first Converse content block that carries text instead of always reading `content[0]`. Claude reasoning models can emit a `reasoningContent` block before the text block, which previously made the call fail with a `KeyError` ([#6369](https://github.com/mem0ai/mem0/pull/6369))
> - **Vector Stores:** Turbopuffer filters now apply every operator (`eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`). Only `gte` and `lte` were read before, so any other operator was silently dropped and the query returned unfiltered results. An unsupported operator now raises `ValueError` ([#6564](https://github.com/mem0ai/mem0/pull/6564))
> - **Vector Stores:** Turbopuffer `search()` scores now respect `distance_metric`. With `euclidean_squared`, the unbounded squared distance maps to `1 / (1 + distance)` instead of `1 - distance`, which went negative and inverted ranking for any distance above 1 ([#6559](https://github.com/mem0ai/mem0/pull/6559))
> …

### [deepseek-plugin-v0.3.2](https://github.com/mem0ai/mem0/releases/tag/deepseek-plugin-v0.3.2) — Mem0 DeepSeek Plugin (v0.3.2)
<sub>2026-09-23 · 2mo ago</sub>

> **Improvements:**
> - **Search:** The `search_memory` tool description no longer asks the agent to search proactively before answering anything that may depend on earlier context. It now asks for a search before repeating investigation or when earlier decisions, fixes, commands, or results may help ([#7420](https://github.com/mem0ai/mem0/pull/7420))
> - **Automatic recall:** Injected memories are introduced as "Mem0 found these relevant memories from earlier work:". The old heading called them a shallow first pass and told the agent to search again with `mem0_memory`, a tool DeepSeek does not have ([#7420](https://github.com/mem0ai/mem0/pull/7420))

### [pi-agent-v0.3.2](https://github.com/mem0ai/mem0/releases/tag/pi-agent-v0.3.2) — Mem0 Pi Agent Plugin (v0.3.2)
<sub>2026-09-23 · 2mo ago</sub>

> **Improvements:**
> - **Search:** The memory policy, `mem0_memory` tool description, and prompt guidelines no longer ask the agent to search before answering anything that may depend on earlier context or to run several searches per question. They now ask for a search before repeating investigation or when earlier decisions, fixes, commands, or results may help ([#7420](https://github.com/mem0ai/mem0/pull/7420))
> - **Skills:** `context-loader` makes one search instead of 2-4 parallel searches, and uses the search skill description from the other coding-agent plugins ([#7420](https://github.com/mem0ai/mem0/pull/7420))
> - **Automatic recall:** Injected memories are introduced as "Mem0 found these relevant memories from earlier work in this repository:", the same heading as the Python plugins. The old heading called them a shallow first pass and told the agent to search again ([#7420](https://github.com/mem0ai/mem0/pull/7420))

### [openclaw-v1.2.1](https://github.com/mem0ai/mem0/releases/tag/openclaw-v1.2.1) — Mem0 OpenClaw Plugin (v1.2.1)
<sub>2026-09-23 · 2mo ago</sub>

> **Improvements:**
> - **Search:** The `memory_search` tool description no longer asks the agent to search proactively or to run several searches for multi-part questions. It now asks for a search before repeating investigation or when earlier decisions, fixes, commands, or results may help. Recall strategies (`smart`, `always`, `manual`) are unchanged ([#7420](https://github.com/mem0ai/mem0/pull/7420))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(security): resolve 22 Vanta HIGH/CRITICAL Dependabot alerts (mong…](https://github.com/mem0ai/mem0/commit/f93aba4b53241ccd9db32903cd19d1ff7f0066f0) | harshgupta-mem0 |
| 2026-11-18 | [fix(llms): treat bare gpt-5-* and gpt-6* as reasoning models (#7939)](https://github.com/mem0ai/mem0/commit/fff8a6472512d1bc1a4bccab8c645b65a1df7fe5) | vinayb21-work |
| 2026-11-06 | [fix(security): upgrade @azure/msal-node to 7.x via @azure/identity 4.…](https://github.com/mem0ai/mem0/commit/f1791daa86d469249c9b002f62644d58a1eb96a0) | harshgupta-mem0 |
| 2026-11-06 | [fix(security): resolve 9 Vanta HIGH Dependabot vulnerabilities (#7849)](https://github.com/mem0ai/mem0/commit/d16b8df6f97bad5b2a1ae88fcbacd31db834652e) | harshgupta-mem0 |
| 2026-11-04 | [fix(security): resolve 5 Vanta CRITICAL Dependabot vulnerabilities (#…](https://github.com/mem0ai/mem0/commit/ed1f10fc87080f0b67f99be370817504888462ab) | harshgupta-mem0 |
| 2026-10-30 | [fix(memory): never re-create a deleted memory when update races delet…](https://github.com/mem0ai/mem0/commit/753496cf1435d76c3a711f3af51303f7fdcb6420) | harsh-mem0 |
| 2026-10-30 | [fix(ts): never re-create a deleted memory when update races delete (#…](https://github.com/mem0ai/mem0/commit/d2b8432b772a5923ab5ba145cf1ae2a9f8b1c3f2) | harsh-mem0 |
| 2026-10-26 | [docs(platform): add the pricing FAQ page (#7711)](https://github.com/mem0ai/mem0/commit/26cdefb46600c0fa5953c4b5ee5003c125539fc4) | harsh-mem0 |
| 2026-10-21 | [docs(platform): rewrite the BYOK page as a feature guide (#7661)](https://github.com/mem0ai/mem0/commit/2c81af3bbe27d9bccb09c772d583df9e9be72ee5) | harsh-mem0 |
| 2026-10-14 | [Add OSS Halloween Happy Hour banner to README (#7637)](https://github.com/mem0ai/mem0/commit/0724291bd864cf807e88ee8981c8226644e8fb42) | karthik-indla |

[See all commits ↗](https://github.com/mem0ai/mem0/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mem0ai/mem0.git
```
