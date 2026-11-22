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
| ⭐ **Stars** | 187.8k |
| 🍴 **Forks** | 19.1k |
| 🐞 **Open issues + PRs** | [4.7k](https://github.com/ollama/ollama/issues) |
| 💻 **Languages** | Go 75% · C 17% · TypeScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `llm` `llms` `go` `golang` `ollama` `mistral` `gemma` `deepseek` `qwen` `gpt-oss` `glm` `minimax` `muse` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-06-26 |
| 📦 **Latest release** | [v0.40.17](https://github.com/ollama/ollama/releases/tag/v0.40.17) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 96.0 MB |
| 🌐 **Website** | https://ollama.com |

## 📦 Recent releases

### [v0.40.17](https://github.com/ollama/ollama/releases/tag/v0.40.17)
<sub>2026-11-10 · 11d ago</sub>

> **Inkling 2 Mini**
> [Inkling 2 Mini](https://ollama.com/library/inkling-2-mini) from Thinking Machines is a 26B parameter model with 5.4B active.
> Its looped layers give it more computation per token than its size suggests, and it still fits on a Mac at about 20GB. It handles text and images, tool calls, and thinking, and scores 79.2% on SWE-Bench Verified).
> ```
>   ollama run inkling-2-mini
> ```
> …

### [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16)
<sub>2026-11-09 · 12d ago</sub>

> **Ripple Preview**
> [Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.
> ```sh
> ollama run ripple-preview
> ```
> **What's Changed**
> …

### [v0.40.15](https://github.com/ollama/ollama/releases/tag/v0.40.15)
<sub>2026-11-03 · 18d ago</sub>

> **MiMo V2.6**
> Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.
> ```sh
> ollama run mimo-v2.6
> ```
> **AutoTrust decision models**
> …

### [v0.40.14](https://github.com/ollama/ollama/releases/tag/v0.40.14)
<sub>2026-11-03 · 19d ago</sub>

> **What's Changed**
> * `ollama launch claude` now applies the model's output token limit for Claude Code, so cloud models no longer run into the 128k default cap
> * Cloud web search responses on `/api/chat` are now decoded correctly, including compressed responses
> * OpenAI-compatible endpoints no longer override a model's packaged sampler defaults — clients that send no `temperature`/`top_p` get the model's own values instead of 1.0, matching `/api/chat`
> * `/v1/responses` now preserves readable input content, including prior assistant refusals, instead of flattening it
> * Ollama's app can now retry ChatGPT disconnect failures instead of leaving the connection in a broken state
> …

### [v0.40.13](https://github.com/ollama/ollama/releases/tag/v0.40.13)
<sub>2026-10-28 · 24d ago</sub>

> **LFM3 on Linux and Windows**
> Liquid AI's [LFM3](https://ollama.com/library/lfm3) models, including text-to-speech in [lfm3-audio](https://ollama.com/library/lfm3-audio) and [lfm3-omni](https://ollama.com/library/lfm3-omni), now run on Linux and Windows as well as Apple silicon.
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.12...v0.40.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [mlxrunner: share tensor helpers and model setup across architectures …](https://github.com/ollama/ollama/commit/318ee284aa3b5558de57efefff730ea33c4a9bef) | jaingaurav |
| 2026-11-21 | [mlx: fuse Inkling residual mixing on Metal (#19808)](https://github.com/ollama/ollama/commit/2bd4d6aabdf4caa39e7095e201dcda4cc1a3a406) | dhiltgen |
| 2026-11-21 | [mlx: inkling follow up (#19806)](https://github.com/ollama/ollama/commit/23b94a2daf2cd1fbf6b4dcfbfd3efbaca424b7bf) | dhiltgen |
| 2026-11-21 | [mlxrunner: add Inkling 2 Mini (#19799)](https://github.com/ollama/ollama/commit/cecac8bf1bd30ba928ee7cfe53b953f9b25642ae) | dhiltgen |
| 2026-11-20 | [install: support preview channel (#19801)](https://github.com/ollama/ollama/commit/afc7c06022a86279609ac00676cc05ded5b7011c) | dhiltgen |
| 2026-11-20 | [cmd: omit bias and gamma vectors from verbose safetensors show (#19803)](https://github.com/ollama/ollama/commit/0c666ce5ee7eaaeec8c77eb7f929c29964a8f246) | pdevine |
| 2026-11-20 | [test: stabilize Pi catalog timeout regressions (#19742)](https://github.com/ollama/ollama/commit/5187f59581d5a3d502f8d89550f12314063c3a96) | hoyyeva |
| 2026-11-20 | [mlxrunner: choose default parallelism from available memory (#19785)](https://github.com/ollama/ollama/commit/0b243a141a64110ef31d47ec35900cefcd467a18) | dhiltgen |
| 2026-11-19 | [mlxrunner: adapt saved history to memory pressure (#19678)](https://github.com/ollama/ollama/commit/73ee71ddcc088451457845b22d03c349b7c4dd6b) | dhiltgen |
| 2026-11-18 | [Merge pull request #19748 from ollama/claude/sched-shift-no-reload-18950](https://github.com/ollama/ollama/commit/42ac2c0c1e132c0b4f0d9cfcd4e7950f0c5470bc) | jaingaurav |

[See all commits ↗](https://github.com/ollama/ollama/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ollama/ollama.git
```
