# unslothai/unsloth

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/unslothai/unsloth)

> Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Run and fine-tune LLMs locally, fast and low-memory |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 80.3k |
| 🍴 **Forks** | 7.5k |
| 🐞 **Open issues + PRs** | [651](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 759.6 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — Inkling finetuning + perf fixes
<sub>2026-11-25 · yesterday</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Bug fixes for finetuning Inkling 2 Mini** + other bugs, MXC sandbox upgraded
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> …

### [v0.1.924-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta) — Inkling finetuning + perf fixes
<sub>2026-11-24 · 2d ago</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> - **Faster `adamw_8bit`** up to 12% less time per step on small batches
> …

### [v0.1.923-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) — Inkling 1.9x faster inference + Training
<sub>2026-11-23 · 2d ago</sub>

> Inkling 2 Mini runs up to 1.9x faster on all GPUs for decoding + RTX Spark improvements. Also new: faster GRPO and AsyncGRPO training, Qwen-Image-Flash and FastWan, a Knowledge page in Settings and audio, subtitle and image translation.
> **Highlights**
> - **Inkling 2 Mini on 8 to 12 GB GPUs** up to 1.9x faster decoding [guide](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update)
> - Fine-tuning for Inkling in Unsloth is now available
> - **Multi-GPU diffusion LoRA training** about 2x the samples per second on two GPUs
> - **Qwen-Image-Flash + FastWan** 4-step images about 14x faster than Qwen-Image, 3-step video up to 3x faster
> …

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · 5d ago</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · 5d ago</sub>

> There will be another release today in a few hours!
> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - new 26B (5.4 active) 1M context - strongest for size. [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Studio video: load Wan LoRAs saved with musubi-tuner key names (#19740)](https://github.com/unslothai/unsloth/commit/29f31dc97a6f331a3ad33f518e328b0ff81e48ec) | danielhanchen |
| 2026-11-26 | [Studio tests: pin the host machine in the torch ceiling freeze test (…](https://github.com/unslothai/unsloth/commit/c34af0354fd615dcc8796d17423356b329b3970b) | danielhanchen |
| 2026-11-26 | [Studio: default PAL_DISABLE_SDMA=1 on Windows ROCm so copies after an…](https://github.com/unslothai/unsloth/commit/3bdff3cdd8159bc9949c4dc77d636222de012432) | danielhanchen |
| 2026-11-26 | [Opt-in GRPO partial rollouts for colocated vLLM (#19771)](https://github.com/unslothai/unsloth/commit/0fbbcca0af49a31561967844c8317c9de5dcd0ef) | danielhanchen |
| 2026-11-26 | [Studio: don't cut a `<` inside LaTeX (streaming, finished and stopped…](https://github.com/unslothai/unsloth/commit/6a3a230dcd08f00315bfd11fba5b2a49ea587ccc) | NilayYadav |
| 2026-11-26 | [Studio images: coalesce identical requests across users, batch plain …](https://github.com/unslothai/unsloth/commit/d745444b787382e20967007a858ba581aaef5703) | danielhanchen |
| 2026-11-26 | [Studio images: load gated tokenizers (Krea 2, Ideogram 4, Anima) with…](https://github.com/unslothai/unsloth/commit/6cb925b92094d848265ed6416736d31cee4a88c6) | danielhanchen |
| 2026-11-26 | [Studio: sample FLUX.3 Klein at BFL's reference shift 16 and base CFG …](https://github.com/unslothai/unsloth/commit/8b0baa892cb7b568bb80463928e601d32c3b1198) | danielhanchen |
| 2026-11-26 | [Expert parallel for per-expert MoE layouts: transformers 4.x ModuleLi…](https://github.com/unslothai/unsloth/commit/ddfe1bcd9715d86ffbaada21022f42dc8f584135) | danielhanchen |
| 2026-11-26 | [Studio tests: forget probe_devices cached card names between tests (#…](https://github.com/unslothai/unsloth/commit/5b1a7d93bae42f012e8beba4d00c1d913648e4a0) | danielhanchen |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
