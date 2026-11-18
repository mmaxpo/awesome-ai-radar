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
| ⭐ **Stars** | 187.5k |
| 🍴 **Forks** | 19.1k |
| 🐞 **Open issues + PRs** | [4.7k](https://github.com/ollama/ollama/issues) |
| 💻 **Languages** | Go 74% · C 18% · TypeScript 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `llm` `llms` `go` `golang` `ollama` `mistral` `gemma` `deepseek` `qwen` `gpt-oss` `glm` `minimax` `muse` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2023-06-26 |
| 📦 **Latest release** | [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 95.5 MB |
| 🌐 **Website** | https://ollama.com |

## 📦 Recent releases

### [v0.40.17-rc1](https://github.com/ollama/ollama/releases/tag/v0.40.17-rc1) — v0.40.17 _(pre-release)_
<sub>2026-11-10 · 7d ago</sub>

> **What's Changed**
> * Improve ChatGPT CLI restore and graceful restart by @hoyyeva in https://github.com/ollama/ollama/pull/19583
> * cmd/launch: use thinking metadata for OpenCode settings by @hoyyeva in https://github.com/ollama/ollama/pull/19409
> * llm: use mmap for Vulkan integrated GPUs by @dhiltgen in https://github.com/ollama/ollama/pull/19640
> * rpreslar4765/Ollama by @rpreslar4765 in https://github.com/ollama/ollama/pull/17163
> * mlx: support concurrent generation by @dhiltgen in https://github.com/ollama/ollama/pull/19197
> …

### [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16)
<sub>2026-11-09 · 8d ago</sub>

> **Ripple Preview**
> [Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.
> ```sh
> ollama run ripple-preview
> ```
> **What's Changed**
> …

### [v0.40.15](https://github.com/ollama/ollama/releases/tag/v0.40.15)
<sub>2026-11-03 · 14d ago</sub>

> **MiMo V2.6**
> Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.
> ```sh
> ollama run mimo-v2.6
> ```
> **AutoTrust decision models**
> …

### [v0.40.14](https://github.com/ollama/ollama/releases/tag/v0.40.14)
<sub>2026-11-03 · 15d ago</sub>

> **What's Changed**
> * `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
> * Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
> * OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
> * `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
> * Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
> …

### [v0.40.13](https://github.com/ollama/ollama/releases/tag/v0.40.13)
<sub>2026-10-28 · 20d ago</sub>

> **LFM3 on Linux and Windows**
> Liquid AI's [LFM3](https://ollama.com/library/lfm3) models, including text-to-speech in [lfm3-audio](https://ollama.com/library/lfm3-audio) and [lfm3-omni](https://ollama.com/library/lfm3-omni), now run on Linux and Windows as well as Apple silicon.
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.12...v0.40.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [mlxrunner: reuse saved prefixes across request slots (#19677)](https://github.com/ollama/ollama/commit/b8db8d5b5c8daedbbef7bb9ace2221a38bc384c2) | dhiltgen |
| 2026-11-17 | [Merge pull request #19731 from ollama/fix/repl-ctrl-c-multiline](https://github.com/ollama/ollama/commit/312c3c8d0c2709209ebbc816ca352bcaf52c19b5) | jaingaurav |
| 2026-11-17 | [cmd: leave multiline mode when Ctrl+C or Ctrl+G discards input](https://github.com/ollama/ollama/commit/169626b403796ce482b3de0b3dd4bc3afdb15438) | jaingaurav |
| 2026-11-16 | [mlxrunner: batch speculative verification (#19663)](https://github.com/ollama/ollama/commit/db5266a71d6413c4568208a768757b16ffd7a021) | dhiltgen |
| 2026-11-16 | [cmake: support compatible binary MLX-C and XGrammar (#19688)](https://github.com/ollama/ollama/commit/9a4b136efefecb51b428d22e79b0f3d15769a1f8) | dhiltgen |
| 2026-11-15 | [llm: keep weights out of pinned host memory on Windows iGPUs (#19636)](https://github.com/ollama/ollama/commit/15af2b261c14c494d1fe08cf9d0b9e0af1a18c84) | saman-amd |
| 2026-11-14 | [api: preserve unmodeled tool schema keywords (#19686)](https://github.com/ollama/ollama/commit/a5864fcb33969705de3c0ebfedf4b2a16c970bcc) | jberg5 |
| 2026-11-12 | [Map disabled thinking to the models lowest supported level (#19684)](https://github.com/ollama/ollama/commit/5632619189ab493c70bd3f9435214b8788cc1c80) | jberg5 |
| 2026-11-12 | [cmd: show help for noninteractive bare invocations (#19557)](https://github.com/ollama/ollama/commit/9da7dfd5c3332298a345222a2011d58426a75ca2) | ParthSareen |
| 2026-11-12 | [Support deferred tool loading in claude code (#19578)](https://github.com/ollama/ollama/commit/361b3e17fd48e4b29d862d89a278508d2e131716) | jberg5 |

[See all commits ↗](https://github.com/ollama/ollama/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ollama/ollama.git
```
