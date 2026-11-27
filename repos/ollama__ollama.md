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
| ⭐ **Stars** | 188.3k |
| 🍴 **Forks** | 19.2k |
| 🐞 **Open issues + PRs** | [4.8k](https://github.com/ollama/ollama/issues) |
| 💻 **Languages** | Go 75% · C 17% · TypeScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `llm` `llms` `go` `golang` `ollama` `mistral` `gemma` `deepseek` `qwen` `gpt-oss` `glm` `minimax` `muse` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-06-26 |
| 📦 **Latest release** | [v0.40.18](https://github.com/ollama/ollama/releases/tag/v0.40.18) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 96.0 MB |
| 🌐 **Website** | https://ollama.com |

## 📦 Recent releases

### [v0.40.19-rc0](https://github.com/ollama/ollama/releases/tag/v0.40.19-rc0) — v0.40.19 _(pre-release)_
<sub>2026-11-26 · today</sub>

> **What's Changed**
> * inkling2: faster short histories, draft proposals and conv snapshots by @dhiltgen in https://github.com/ollama/ollama/pull/19881
> * mlxrunner: compact Engram history buffers by @pdevine in https://github.com/ollama/ollama/pull/19913
> * bump llama-server by @pdevine in https://github.com/ollama/ollama/pull/19917
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.18...v0.40.19-rc0

### [v0.40.18](https://github.com/ollama/ollama/releases/tag/v0.40.18)
<sub>2026-11-24 · 3d ago</sub>

> **What's Changed**
> * mlx: fuse Inkling residual mixing on Metal by @dhiltgen in https://github.com/ollama/ollama/pull/19808
> * mlxrunner: share tensor helpers and model setup across architectures by @jaingaurav in https://github.com/ollama/ollama/pull/19805
> * llama.cpp: version bump b12651 + remove jetpack5 support by @pdevine in https://github.com/ollama/ollama/pull/19865
> * inkling2: faster Metal decode, prefill and draft rounds by @dhiltgen in https://github.com/ollama/ollama/pull/19843
> **Full Changelog**: https://github.com/ollama/ollama/compare/v0.40.17...v0.40.18-rc0

### [v0.40.17](https://github.com/ollama/ollama/releases/tag/v0.40.17)
<sub>2026-11-10 · 16d ago</sub>

> **Inkling 2 Mini**
> [Inkling 2 Mini](https://ollama.com/library/inkling-2-mini) from Thinking Machines is a 26B parameter model with 5.4B active.
> Its looped layers give it more computation per token than its size suggests, and it still fits on a Mac at about 20GB. It handles text and images, tool calls, and thinking, and scores 79.2% on SWE-Bench Verified).
> ```
>   ollama run inkling-2-mini
> ```
> …

### [v0.40.16](https://github.com/ollama/ollama/releases/tag/v0.40.16)
<sub>2026-11-09 · 17d ago</sub>

> **Ripple Preview**
> [Ripple Preview](https://ollama.com/library/ripple-preview) from Ricursive Intelligence is a 65B dense model built for agentic coding.
> ```sh
> ollama run ripple-preview
> ```
> **What's Changed**
> …

### [v0.40.15](https://github.com/ollama/ollama/releases/tag/v0.40.15)
<sub>2026-11-03 · 23d ago</sub>

> **MiMo V2.6**
> Xiaomi MiMo's [mimo-v2.6](https://ollama.com/library/mimo-v2.6), a 9B model built for code and agent workflows, is now supported in Ollama.
> ```sh
> ollama run mimo-v2.6
> ```
> **AutoTrust decision models**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [bump llama-server (#19917)](https://github.com/ollama/ollama/commit/8ae8acb81afba9c3c67adf08190964eb7d1207ef) | pdevine |
| 2026-11-26 | [mlxrunner: compact Engram history buffers (#19913)](https://github.com/ollama/ollama/commit/b207a5a319ba8bd21d5ca607cfb460b46ad6f946) | pdevine |
| 2026-11-25 | [inkling2: faster short histories, draft proposals and conv snapshots …](https://github.com/ollama/ollama/commit/784dd544291825e8f5f064672dc2bd7f4d9345ed) | dhiltgen |
| 2026-11-24 | [inkling2: faster Metal decode, prefill and draft rounds (#19843)](https://github.com/ollama/ollama/commit/924cc286cc592f49c481fa84e15fa60dbc75989e) | dhiltgen |
| 2026-11-24 | [llama.cpp: version bump b12651 + remove jetpack5 support (#19865)](https://github.com/ollama/ollama/commit/900e1469fbb8c78ac9be0b22e2ccf77927195eec) | pdevine |
| 2026-11-22 | [mlxrunner: share tensor helpers and model setup across architectures …](https://github.com/ollama/ollama/commit/318ee284aa3b5558de57efefff730ea33c4a9bef) | jaingaurav |
| 2026-11-21 | [mlx: fuse Inkling residual mixing on Metal (#19808)](https://github.com/ollama/ollama/commit/2bd4d6aabdf4caa39e7095e201dcda4cc1a3a406) | dhiltgen |
| 2026-11-21 | [mlx: inkling follow up (#19806)](https://github.com/ollama/ollama/commit/23b94a2daf2cd1fbf6b4dcfbfd3efbaca424b7bf) | dhiltgen |
| 2026-11-21 | [mlxrunner: add Inkling 2 Mini (#19799)](https://github.com/ollama/ollama/commit/cecac8bf1bd30ba928ee7cfe53b953f9b25642ae) | dhiltgen |
| 2026-11-20 | [install: support preview channel (#19801)](https://github.com/ollama/ollama/commit/afc7c06022a86279609ac00676cc05ded5b7011c) | dhiltgen |

[See all commits ↗](https://github.com/ollama/ollama/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ollama/ollama.git
```
