# ollama/ollama

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ollama/ollama)

> Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Run open models locally with one command |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 186.9k |
| 🍴 **Forks** | 19.1k |
| 🐞 **Open issues + PRs** | [4.7k](https://github.com/ollama/ollama/issues) |
| 💻 **Languages** | Go 74% · C 18% · TypeScript 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `llm` `llms` `go` `golang` `ollama` `mistral` `gemma` `deepseek` `qwen` `gpt-oss` `glm` `minimax` `muse` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2023-06-26 |
| 📦 **Latest release** | [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 95.5 MB |
| 🌐 **Website** | https://ollama.com |

## 📦 Recent releases

### [v0.40.17-rc0](https://github.com/ollama/ollama/releases/tag/v0.40.17-rc0) — v0.40.17 _(pre-release)_
<sub>2026-11-10 · 3d ago</sub>

> **What's Changed**
> * Improve ChatGPT CLI restore and graceful restart by @hoyyeva in https://github.com/ollama/ollama/pull/19583
> * cmd/launch: use thinking metadata for OpenCode settings by @hoyyeva in https://github.com/ollama/ollama/pull/19409
> * llm: use mmap for Vulkan integrated GPUs by @dhiltgen in https://github.com/ollama/ollama/pull/19640
> * rpreslar4765/Ollama by @rpreslar4765 in https://github.com/ollama/ollama/pull/17163
> * mlx: support concurrent generation by @dhiltgen in https://github.com/ollama/ollama/pull/19197
> …

### [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16)
<sub>2026-11-09 · 4d ago</sub>

> **Ripple Preview**
> [Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.
> ```sh
> ollama run ripple-preview
> ```
> **What's Changed**
> …

### [v0.40.15](https://github.com/ollama/ollama/releases/tag/v0.40.15)
<sub>2026-11-03 · 10d ago</sub>

> **MiMo V2.6**
> Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.
> ```sh
> ollama run mimo-v2.6
> ```
> **AutoTrust decision models**
> …

### [v0.40.14](https://github.com/ollama/ollama/releases/tag/v0.40.14)
<sub>2026-11-03 · 11d ago</sub>

> **What's Changed**
> * `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
> * Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
> * OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
> * `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
> * Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
> …

### [v0.40.13](https://github.com/ollama/ollama/releases/tag/v0.40.13)
<sub>2026-10-28 · 16d ago</sub>

> **LFM3 on Linux and Windows**
> Liquid AI's [LFM3](https://ollama.com/library/lfm3) models, including text-to-speech in [lfm3-audio](https://ollama.com/library/lfm3-audio) and [lfm3-omni](https://ollama.com/library/lfm3-omni), now run on Linux and Windows as well as Apple silicon.
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.12...v0.40.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [api: preserve unmodeled tool schema keywords (#19686)](https://github.com/ollama/ollama/commit/a5864fcb33969705de3c0ebfedf4b2a16c970bcc) | jberg5 |
| 2026-11-12 | [Map disabled thinking to the models lowest supported level (#19684)](https://github.com/ollama/ollama/commit/5632619189ab493c70bd3f9435214b8788cc1c80) | jberg5 |
| 2026-11-12 | [cmd: show help for noninteractive bare invocations (#19557)](https://github.com/ollama/ollama/commit/9da7dfd5c3332298a345222a2011d58426a75ca2) | ParthSareen |
| 2026-11-12 | [Support deferred tool loading in claude code (#19578)](https://github.com/ollama/ollama/commit/361b3e17fd48e4b29d862d89a278508d2e131716) | jberg5 |
| 2026-11-12 | [Merge pull request #18972 from ollama/docs_restructuring](https://github.com/ollama/ollama/commit/4a7b194120c7463c243582b7bfa0b4eac2271919) | anra8571 |
| 2026-11-10 | [launch: refresh Pi metadata after sign-in and honor prompt args (#19575)](https://github.com/ollama/ollama/commit/8a89b76cc7359805e48357ba7e5b99e845a4c211) | hoyyeva |
| 2026-11-10 | [MLX, MLX-C: version bump (#19647)](https://github.com/ollama/ollama/commit/6140670fd1952941041dce5fb3f8932091bc22e4) | dhiltgen |
| 2026-11-10 | [llama.cpp: version bump b12257 (#19646)](https://github.com/ollama/ollama/commit/9b390157f2a9807e7d6748d31aa86ceba6c01b8c) | dhiltgen |
| 2026-11-10 | [mlx: support concurrent generation (#19197)](https://github.com/ollama/ollama/commit/ab9295d03c549cdfb23245d84382ae450d8f1439) | dhiltgen |
| 2026-11-10 | [llm: use mmap for Vulkan integrated GPUs (#19640)](https://github.com/ollama/ollama/commit/3f3fa58f7fcf18de43ec126ad8676b4281b6923c) | dhiltgen |

[See all commits ↗](https://github.com/ollama/ollama/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ollama/ollama.git
```
