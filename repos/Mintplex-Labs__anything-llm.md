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
| ⭐ **Stars** | 68.4k |
| 🍴 **Forks** | 7.7k |
| 🐞 **Open issues + PRs** | [355](https://github.com/Mintplex-Labs/anything-llm/issues) |
| 💻 **Languages** | JavaScript 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `rag` `localai` `vector-database` `llm` `ai-agents` `multimodal` `agent-harness` `agentic-ai` `hermes-agent` `local-ai` `self-hosted-ai` `agent-computer` `computer-use` `agent-orchestration` `agentic-workflow` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2023-06-04 |
| 📦 **Latest release** | [v1.20.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.20.0) — 2026-11-17 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 94.2 MB |
| 🌐 **Website** | https://anythingllm.com |

## 📦 Recent releases

### [v1.20.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.20.0) — AnythingLLM v1.20.0
<sub>2026-11-17 · yesterday</sub>

> **Updated browser extension**
> The [browser extension](https://github.com/Mintplex-Labs/anythingllm-extension) has been improved beyond its original function of just collecting documents to now a full fledged UI chat bar with the ability to right click -> Add context (text and image) and chat directly  in Chrome. This sidebar should have mostly full parity for tooling and more with the traditional chat UI.
> While it is backward and forward compatible, only full functionality is expected when the server and extension are on version 1.20.0 or later. The [Chrome webstore](https://chromewebstore.google.com/detail/anythingllm-browser-compa/pncmdlebcopjodenlllcomedphdmeogm) has been updated to this version as well.
> https://github.com/user-attachments/assets/830069a6-34cb-4f37-80b0-6d52eb4622d0
> **PowerPoint tool overhaul**
> <img width="1990" height="1099" alt="pptx-generation" src="https://github.com/user-attachments/assets/05689972-1296-4869-b208-dd9301222dd3" />
> …

### [v1.19.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) — AnythingLLM v1.19.0
<sub>2026-10-26 · 23d ago</sub>

> **Built-in LLM for Docker**
> <img width="3680" height="2212" alt="AnythingLLM Docker built-in LLM powered by Lemonade and llama.cpp" src="https://github.com/user-attachments/assets/410b5784-ca15-4027-a1c4-056d9d5c748e" />
> AnythingLLM Docker now has a default local LLM experience right out of the box. The same kind of built-in engine that ships with [AnythingLLM Desktop](https://docs.anythingllm.com/setup/llm-configuration/local/built-in) can now run **inside the container**: [Lemonade](https://lemonade-server.ai), the fully [open-source](https://github.com/lemonade-sdk/lemonade) local inference server from AMD, running your models with [llama.cpp](https://github.com/ggml-org/llama.cpp). You no longer need to run Ollama, LM Studio or any other inference server next to AnythingLLM.
> Pass your GPU into the container and the engine is accelerated on whatever hardware you have. It picks the fastest backend automatically: CUDA for NVIDIA GPUs, Vulkan for AMD and Intel GPUs, or the CPU. It runs on both `amd64` and `arm64` hosts.
> When it's turned on, **Built-in** becomes the default LLM provider during onboarding, with three models recommended for your hardware. You can download any model from the model table or pull any GGUF model from Hugging Face. It works everywhere a provider can be used: the system LLM, workspace and agent LLMs, the chat window model picker, and [Model Router](https://docs.anythingllm.com/model-router/setup).
> > [!TIP]
> …

### [v1.18.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.18.0) — AnythingLLM v1.18.0
<sub>2026-10-13 · 1mo ago</sub>

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [docs: no PRs for issues labeled core-team-only](https://github.com/Mintplex-Labs/anything-llm/commit/2f6a451f55aca970311af2579088fe0c27af3ce8) | timothycarambat |
| 2026-11-18 | [fix(ollama): stop replaying saved reasoning and keep native agent thi…](https://github.com/Mintplex-Labs/anything-llm/commit/1046dc061d9314f817d9c27782dc65328e0da6e3) | timothycarambat |
| 2026-11-18 | [feat(agents): hint when filesystem search results are truncated (#7270)](https://github.com/Mintplex-Labs/anything-llm/commit/972b44747cf22e6bfa79c3fe6ff1779e68ee3f27) | timothycarambat |
| 2026-11-18 | [fix(collector): run ffmpeg WAV conversion asynchronously (#7269)](https://github.com/Mintplex-Labs/anything-llm/commit/40ec73a5d53c05ed0e2273113ccf2975f49ba448) | timothycarambat |
| 2026-11-18 | [fix(agents): run filesystem search ripgrep asynchronously (#7267)](https://github.com/Mintplex-Labs/anything-llm/commit/0d252cd6f02b3d92923ec43e86f61109c1c80e8c) | timothycarambat |
| 2026-11-18 | [docs: dependency bumps are core-team only](https://github.com/Mintplex-Labs/anything-llm/commit/8db1c00b60b75b14a91a055edeab4976046de1e1) | timothycarambat |
| 2026-11-18 | [Fix: misleading Model Router delete confirmation and surface workspac…](https://github.com/Mintplex-Labs/anything-llm/commit/64b599fc92a9c2f4d60f2f9244d278acfff73204) | Bensonbenyi |
| 2026-11-17 | [fix(i18n): correct Turkish translations and refresh README (#7247)](https://github.com/Mintplex-Labs/anything-llm/commit/807aaebbd3fa98368319546305e1c6f2e275cad9) | alkank |
| 2026-11-17 | [fix: reject fractional keep-alive timeouts in isInteger validator (#7…](https://github.com/Mintplex-Labs/anything-llm/commit/b0cfa51578169293078b0a8c25bfed22db64c8dc) | rtmalikian |
| 2026-11-17 | [fix: prefer PDF Author over Creator for document author (#7248)](https://github.com/Mintplex-Labs/anything-llm/commit/a30b7e2095e43dcef259196e477a5da9ab59e168) | timothycarambat |

[See all commits ↗](https://github.com/Mintplex-Labs/anything-llm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Mintplex-Labs/anything-llm.git
```
