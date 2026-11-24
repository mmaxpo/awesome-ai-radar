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
| ⭐ **Stars** | 188.0k |
| 🍴 **Forks** | 19.2k |
| 🐞 **Open issues + PRs** | [4.7k](https://github.com/ollama/ollama/issues) |
| 💻 **Languages** | Go 75% · C 17% · TypeScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `llm` `llms` `go` `golang` `ollama` `mistral` `gemma` `deepseek` `qwen` `gpt-oss` `glm` `minimax` `muse` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-06-26 |
| 📦 **Latest release** | [v0.40.18](https://github.com/ollama/ollama/releases/tag/v0.40.18) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 96.0 MB |
| 🌐 **Website** | https://ollama.com |

## 📦 Recent releases

### [v0.40.18](https://github.com/ollama/ollama/releases/tag/v0.40.18)
<sub>2026-11-24 · today</sub>

> **What's Changed**
> * mlx: fuse Inkling residual mixing on Metal by @dhiltgen in https://github.com/ollama/ollama/pull/19808
> * mlxrunner: share tensor helpers and model setup across architectures by @jaingaurav in https://github.com/ollama/ollama/pull/19805
> * llama.cpp: version bump b12651 + remove jetpack5 support by @pdevine in https://github.com/ollama/ollama/pull/19865
> * inkling2: faster Metal decode, prefill and draft rounds by @dhiltgen in https://github.com/ollama/ollama/pull/19843
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.17...v0.40.18-rc0

### [v0.40.17](https://github.com/ollama/ollama/releases/tag/v0.40.17)
<sub>2026-11-10 · 13d ago</sub>

> **Inkling 2 Mini**
> [Inkling 2 Mini](https://ollama.com/library/inkling-2-mini) from Thinking Machines is a 26B parameter model with 5.4B active.
> Its looped layers give it more computation per token than its size suggests, and it still fits on a Mac at about 20GB. It handles text and images, tool calls, and thinking, and scores 79.2% on SWE-Bench Verified).
> ```
>   ollama run inkling-2-mini
> ```
> …

### [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16)
<sub>2026-11-09 · 14d ago</sub>

> **Ripple Preview**
> [Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.
> ```sh
> ollama run ripple-preview
> ```
> **What's Changed**
> …

### [v0.40.15](https://github.com/ollama/ollama/releases/tag/v0.40.15)
<sub>2026-11-03 · 20d ago</sub>

> **MiMo V2.6**
> Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.
> ```sh
> ollama run mimo-v2.6
> ```
> **AutoTrust decision models**
> …

### [v0.40.14](https://github.com/ollama/ollama/releases/tag/v0.40.14)
<sub>2026-11-03 · 21d ago</sub>

> **What's Changed**
> * `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
> * Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
> * OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
> * `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
> * Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [inkling2: faster Metal decode, prefill and draft rounds (#19843)](https://github.com/ollama/ollama/commit/924cc286cc592f49c481fa84e15fa60dbc75989e) | dhiltgen |
| 2026-11-24 | [llama.cpp: version bump b12651 + remove jetpack5 support (#19865)](https://github.com/ollama/ollama/commit/900e1469fbb8c78ac9be0b22e2ccf77927195eec) | pdevine |
| 2026-11-22 | [mlxrunner: share tensor helpers and model setup across architectures …](https://github.com/ollama/ollama/commit/318ee284aa3b5558de57efefff730ea33c4a9bef) | jaingaurav |
| 2026-11-21 | [mlx: fuse Inkling residual mixing on Metal (#19808)](https://github.com/ollama/ollama/commit/2bd4d6aabdf4caa39e7095e201dcda4cc1a3a406) | dhiltgen |
| 2026-11-21 | [mlx: inkling follow up (#19806)](https://github.com/ollama/ollama/commit/23b94a2daf2cd1fbf6b4dcfbfd3efbaca424b7bf) | dhiltgen |
| 2026-11-21 | [mlxrunner: add Inkling 2 Mini (#19799)](https://github.com/ollama/ollama/commit/cecac8bf1bd30ba928ee7cfe53b953f9b25642ae) | dhiltgen |
| 2026-11-20 | [install: support preview channel (#19801)](https://github.com/ollama/ollama/commit/afc7c06022a86279609ac00676cc05ded5b7011c) | dhiltgen |
| 2026-11-20 | [cmd: omit bias and gamma vectors from verbose safetensors show (#19803)](https://github.com/ollama/ollama/commit/0c666ce5ee7eaaeec8c77eb7f929c29964a8f246) | pdevine |
| 2026-11-20 | [test: stabilize Pi catalog timeout regressions (#19742)](https://github.com/ollama/ollama/commit/5187f59581d5a3d502f8d89550f12314063c3a96) | hoyyeva |
| 2026-11-20 | [mlxrunner: choose default parallelism from available memory (#19785)](https://github.com/ollama/ollama/commit/0b243a141a64110ef31d47ec35900cefcd467a18) | dhiltgen |

[See all commits ↗](https://github.com/ollama/ollama/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ollama/ollama.git
```
