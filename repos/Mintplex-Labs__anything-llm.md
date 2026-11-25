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
| ⭐ **Stars** | 68.6k |
| 🍴 **Forks** | 7.8k |
| 🐞 **Open issues + PRs** | [337](https://github.com/Mintplex-Labs/anything-llm/issues) |
| 💻 **Languages** | JavaScript 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `rag` `localai` `vector-database` `llm` `ai-agents` `multimodal` `agent-harness` `agentic-ai` `hermes-agent` `local-ai` `self-hosted-ai` `agent-computer` `computer-use` `agent-orchestration` `agentic-workflow` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-06-04 |
| 📦 **Latest release** | [v1.20.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.20.0) — 2026-11-17 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 95.5 MB |
| 🌐 **Website** | https://anythingllm.com |

## 📦 Recent releases

### [v1.20.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.20.0) — AnythingLLM v1.20.0
<sub>2026-11-17 · 7d ago</sub>

> **Updated browser extension**
> The [browser extension](https://github.com/Mintplex-Labs/anythingllm-extension) has been improved beyond its original function of just collecting documents to now a full fledged UI chat bar with the ability to right click -> Add context (text and image) and chat directly  in Chrome. This sidebar should have mostly full parity for tooling and more with the traditional chat UI.
> While it is backward and forward compatible, only full functionality is expected when the server and extension are on version 1.20.0 or later. The [Chrome webstore](https://chromewebstore.google.com/detail/anythingllm-browser-compa/pncmdlebcopjodenlllcomedphdmeogm) has been updated to this version as well.
> https://github.com/user-attachments/assets/830069a6-34cb-4f37-80b0-6d52eb4622d0
> **PowerPoint tool overhaul**
> <img width="1990" height="1099" alt="pptx-generation" src="https://github.com/user-attachments/assets/05689972-1296-4869-b208-dd9301222dd3" />
> …

### [v1.19.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.19.0) — AnythingLLM v1.19.0
<sub>2026-10-26 · 29d ago</sub>

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
<sub>2026-09-22 · 2mo ago</sub>

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
| 2026-11-24 | [fix: preserve quoted paragraphs in Word exports (#7337)](https://github.com/Mintplex-Labs/anything-llm/commit/b01447009150507ae0cfd1304e3492fcaf2a92d8) | Israel-Kli |
| 2026-11-23 | [fix: expand system prompt variables written inside other braces (#7331)](https://github.com/Mintplex-Labs/anything-llm/commit/593c0943facbe0a5e1cfac2d7616f15707a9317a) | MohammadHijjawi97 |
| 2026-11-23 | [fix: use HTML file input for document uploads (#7309)](https://github.com/Mintplex-Labs/anything-llm/commit/92175f438fb577156c6f96ed561efa29494f0c28) | Pamalric |
| 2026-11-23 | [fix: import Paperless-ngx documents that have no original file name (…](https://github.com/Mintplex-Labs/anything-llm/commit/c5d53913eb10ec985692175e04b3ea88f02ffcc3) | Israel-Kli |
| 2026-11-23 | [fix: accept postgres:// connection strings for PGVector (#7313)](https://github.com/Mintplex-Labs/anything-llm/commit/3e0d8a7ce70bf3e493693136ce4a86fb10d7725d) | MohammadHijjawi97 |
| 2026-11-23 | [chore: update Gemini fallback model to gemini-3.1-flash-lite (#7329)](https://github.com/Mintplex-Labs/anything-llm/commit/d3b4fabf4e46fcf156392e8d1444194b95b8a437) | timothycarambat |
| 2026-11-23 | [fix: Pin encoding_format to float in Generic OpenAI embedder (#7319)](https://github.com/Mintplex-Labs/anything-llm/commit/b03ebe3f1599330c5cd191c3ea97a033943930bc) | Bensonbenyi |
| 2026-11-23 | [fix: expand multi-stage plugins in ephemeral agent toolOverrides (#7321)](https://github.com/Mintplex-Labs/anything-llm/commit/65a1f64400546f5344e7be1eedd0286cee043099) | Max-Reisinger |
| 2026-11-23 | [fix(i18n): replace unrelated Japanese chat toolbar strings (#7327)](https://github.com/Mintplex-Labs/anything-llm/commit/7690af123a87442669c9148c1543744051e905c9) | AyhamJo7 |
| 2026-11-23 | [fix: Ensure LanceDB rerank fetches at least topN candidates before re…](https://github.com/Mintplex-Labs/anything-llm/commit/bd2d71fef11cd55d0cb506952788e2cf8c5acbc7) | Bensonbenyi |

[See all commits ↗](https://github.com/Mintplex-Labs/anything-llm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Mintplex-Labs/anything-llm.git
```
