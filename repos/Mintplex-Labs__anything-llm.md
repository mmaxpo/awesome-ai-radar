# Mintplex-Labs/anything-llm

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Mintplex-Labs/anything-llm)

> Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience 

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧠 RAG, memory & chat with your data |
| **Project** | — |
| **Why it's worth a look** | All-in-one desktop/Docker app to chat with docs, agents included |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 68.2k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [346](https://github.com/Mintplex-Labs/anything-llm/issues) |
| 💻 **Languages** | JavaScript 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `rag` `localai` `vector-database` `llm` `ai-agents` `multimodal` `agent-harness` `agentic-ai` `hermes-agent` `local-ai` `self-hosted-ai` `agent-computer` `computer-use` `agent-orchestration` `agentic-workflow` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2023-06-04 |
| 📦 **Latest release** | [v1.19.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) — 2026-10-26 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 95.1 MB |
| 🌐 **Website** | https://anythingllm.com |

## 📦 Recent releases

### [v1.19.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) — AnythingLLM v1.19.0
<sub>2026-10-26 · 16d ago</sub>

> **Built-in LLM for Docker**
> <img width="3680" height="2212" alt="AnythingLLM Docker built-in LLM powered by Lemonade and llama.cpp" src="https://github.com/user-attachments/assets/410b5784-ca15-4027-a1c4-056d9d5c748e" />
> AnythingLLM Docker now has a default local LLM experience right out of the box. The same kind of built-in engine that ships with [AnythingLLM Desktop](https://docs.anythingllm.com/setup/llm-configuration/local/built-in) can now run **inside the container**: [Lemonade](https://lemonade-server.ai), the fully [open-source](https://github.com/lemonade-sdk/lemonade) local inference server from AMD, running your models with [llama.cpp](https://github.com/ggml-org/llama.cpp). You no longer need to run Ollama, LM Studio or any other inference server next to AnythingLLM.
> Pass your GPU into the container and the engine is accelerated on whatever hardware you have. It picks the fastest backend automatically: CUDA for NVIDIA GPUs, Vulkan for AMD and Intel GPUs, or the CPU. It runs on both `amd64` and `arm64` hosts.
> When it's turned on, **Built-in** becomes the default LLM provider during onboarding, with three models recommended for your hardware. You can download any model from the model table or pull any GGUF model from Hugging Face. It works everywhere a provider can be used: the system LLM, workspace and agent LLMs, the chat window model picker, and [Model Router](https://docs.anythingllm.com/model-router/setup).
> > [!TIP]
> …

### [v1.18.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.18.0) — AnythingLLM v1.18.0
<sub>2026-10-13 · 29d ago</sub>

> **What's Changed**
> * fix: point k8s probes at the server's /api/ping by @u00dxk2 in https://github.com/Mintplex-Labs/anything-llm/pull/6592
> * fix: don't crash when removing a parsed file while an image is attached by @marmar9615-cloud in https://github.com/Mintplex-Labs/anything-llm/pull/6585
> * fix: open the clicked image when attachments share a file name by @marmar9615-cloud in https://github.com/Mintplex-Labs/anything-llm/pull/6586
> * fix: stop sending history attachments to providers that build prompts from raw chat history by @simonether in https://github.com/Mintplex-Labs/anything-llm/pull/6591
> * fix: compare embed allowlist entries as browser origins by @marmar9615-cloud in https://github.com/Mintplex-Labs/anything-llm/pull/6584
> …

### [v1.17.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.17.0) — AnythingLLM v1.17.0
<sub>2026-10-01 · 1mo ago</sub>

> **What's Changed**
> * fix(collector): read spreadsheet dates as dates, not serial numbers by @L4XB in https://github.com/Mintplex-Labs/anything-llm/pull/6478
> * Drop temp param for Anthropic models by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6472
> * Allow Generic OpenAI max tokens of 0 to omit max_tokens from request by @shatfield4 in https://github.com/Mintplex-Labs/anything-llm/pull/6470
> * fix: support SearchApi engines in agent web browsing by @evilive3000 in https://github.com/Mintplex-Labs/anything-llm/pull/6465
> * fix: ignore malformed agent WebSocket frames instead of crashing the server by @timothycarambat in https://github.com/Mintplex-Labs/anything-llm/pull/6493
> …

### [v1.16.2](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.2) — AnythingLLM v1.16.2
<sub>2026-09-22 · 1mo ago</sub>

> **New Features**
> - [x] [LLMman - OSS](https://github.com/llmmanorg/llmman) is now available as a local LLM provider, replacing Docker Model Runner
> - [x] [Google Vertex AI](https://cloud.google.com/products/gemini-enterprise-agent-platform) is now available as an LLM provider
> - [x] New `generate-image` agent skill for creating images from chat
> - [x] You.com is now the default web search provider for richer web-searches with Zero Data Retention
> - [x] Agent flow variables now support optional arguments
> …

### [v1.16.1](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.16.1) — AnythingLLM v1.16.1
<sub>2026-08-27 · 2mo ago</sub>

> **Activity and Chain of Thought Overhaul**
> <img width="3680" height="2212" alt="image" src="https://github.com/user-attachments/assets/34e52190-51e3-40b5-baeb-d1936319cb4a" />
> We overhauled our UI for long-horizon agentic tasks that show multiple thinking and tool calls to now roll up into a single clean, collapsible UI element.
> This gives you more screen real estate for the actual response while still keeping the important call stack and thoughts the model produces in an easy-to-read format.
> **Navigation Warning**
> <img width="3680" height="2212" alt="image" src="https://github.com/user-attachments/assets/dfa98c30-4bde-4321-86cc-eb0bcd7b9873" />
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [fix: keep generic types like Promise<Response> in chat exports (#7124)](https://github.com/Mintplex-Labs/anything-llm/commit/c4e4e677ec5611fb488f8d46782813ae994df59e) | Israel-Kli |
| 2026-11-12 | [Rework PowerPoint tool: themes, layouts, single-call sections (#6409)](https://github.com/Mintplex-Labs/anything-llm/commit/15602bd49074144cef0b116881cb54f7a38fe9cc) | shatfield4 |
| 2026-11-11 | [fix: log collected error details in Gemini #logAPIError (#7111)](https://github.com/Mintplex-Labs/anything-llm/commit/e8434c07c3d385411aec28e8f9758dfd073565ec) | Bensonbenyi |
| 2026-11-11 | [fix: surface the real error when a PGVector similarity search fails (…](https://github.com/Mintplex-Labs/anything-llm/commit/bc003cbbb905e1acc622038b8f8711ee7c4a7297) | Israel-Kli |
| 2026-11-11 | [fix: retain in-flight document uploads when adding files (#7117)](https://github.com/Mintplex-Labs/anything-llm/commit/18a92ee613453d13a6ab4a0c1c7799e8450ca329) | Max-Reisinger |
| 2026-11-11 | [fix: cap pending agent invocation caches (#7122)](https://github.com/Mintplex-Labs/anything-llm/commit/758a77fa8c435773c72354f2a3b6285e00f18cc9) | timothycarambat |
| 2026-11-10 | [fix: keep the Content-Type header set in an agent flow API Call block…](https://github.com/Mintplex-Labs/anything-llm/commit/728586d76c843ed25cb7a27c7403f4b79bd960c8) | Israel-Kli |
| 2026-11-10 | [fix: keep non-Latin text in raw-text document titles (#7106)](https://github.com/Mintplex-Labs/anything-llm/commit/ba22b48dd34b7c54db9ac7c43930960f83da499f) | Israel-Kli |
| 2026-11-10 | [Email approval card for Gmail and Outlook agent tools (#6970)](https://github.com/Mintplex-Labs/anything-llm/commit/6e3e6cfc901c37032b9e939fb14c50cfb0485f5a) | shatfield4 |
| 2026-11-10 | [fix: invalidate model router decisions after config edits (#7099)](https://github.com/Mintplex-Labs/anything-llm/commit/e82a80da0e5e81252cb19287ba32088233b81df4) | Max-Reisinger |

[See all commits ↗](https://github.com/Mintplex-Labs/anything-llm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Mintplex-Labs/anything-llm.git
```
