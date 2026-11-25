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
| ⭐ **Stars** | 80.2k |
| 🍴 **Forks** | 7.5k |
| 🐞 **Open issues + PRs** | [567](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 745.5 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — Inkling finetuning + perf fixes
<sub>2026-11-25 · today</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Bug fixes for finetuning Inkling 2 Mini** + other bugs, MXC sandbox upgraded
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> …

### [v0.1.924-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta) — Inkling finetuning + perf fixes
<sub>2026-11-24 · yesterday</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> - **Faster `adamw_8bit`** up to 12% less time per step on small batches
> …

### [v0.1.923-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) — Inkling 1.9x faster inference + Training
<sub>2026-11-23 · yesterday</sub>

> Inkling 2 Mini runs up to 1.9x faster on all GPUs for decoding + RTX Spark improvements. Also new: faster GRPO and AsyncGRPO training, Qwen-Image-Flash and FastWan, a Knowledge page in Settings and audio, subtitle and image translation.
> **Highlights**
> - **Inkling 2 Mini on 8 to 12 GB GPUs** up to 1.9x faster decoding [guide](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update)
> - Fine-tuning for Inkling in Unsloth is now available
> - **Multi-GPU diffusion LoRA training** about 2x the samples per second on two GPUs
> - **Qwen-Image-Flash + FastWan** 4-step images about 14x faster than Qwen-Image, 3-step video up to 3x faster
> …

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · 4d ago</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · 4d ago</sub>

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
| 2026-11-25 | [ROCm: keep the static flex compile and Inkling 2 eager policy on AMD …](https://github.com/unslothai/unsloth/commit/3507646f9ad6762038099451edbb70a3d0c55512) | danielhanchen |
| 2026-11-25 | [fix(studio): replay Inkling tool turns cleanly in the server tool loo…](https://github.com/unslothai/unsloth/commit/2f509d180716a241e1bb2fa169d3005629eaf4ad) | Lyxot |
| 2026-11-25 | [Tests: gate the PP router sync-free GPU test on the real CUDA probe (…](https://github.com/unslothai/unsloth/commit/074399d78f324911aac11c6840e4d184dded8bce) | danielhanchen |
| 2026-11-25 | [Ulysses CP: query-chunked sdpa mask for long packed or windowed seque…](https://github.com/unslothai/unsloth/commit/662dfdda2eb2d7ef5d7953edc570efad8d210799) | danielhanchen |
| 2026-11-25 | [Optimizer state offload: overlap chunk copies on FSDP2 DTensor state …](https://github.com/unslothai/unsloth/commit/5e1ecf903e740f5f1da84ce533589f5ba6d293e2) | danielhanchen |
| 2026-11-25 | [GRPO scoring: free each padded-loop chunk's logits before the next fo…](https://github.com/unslothai/unsloth/commit/4fd4c6b378cb3874f4d5de5704f92fb8ab3b92ee) | danielhanchen |
| 2026-11-25 | [Fix chat jumping after scrolling to the bottom (#19485)](https://github.com/unslothai/unsloth/commit/105013764b983f92558efe87c4d0fcf61f722f1c) | Imagineer99 |
| 2026-11-25 | [GRPO: manual DDP gradient sync skips DDP-ignored parameters (expert p…](https://github.com/unslothai/unsloth/commit/7e0ce4facb1cf6116e57c1de88eea98d030488a5) | danielhanchen |
| 2026-11-25 | [Tests: lift _model_forced_float32 into the forced float32 scaler harn…](https://github.com/unslothai/unsloth/commit/2d4916a28f4164d1473352819eeb976ad130ac3a) | danielhanchen |
| 2026-11-25 | [Studio: keep the AppImage on its bundled runtime without autoaudiosin…](https://github.com/unslothai/unsloth/commit/bc3d967c20ba2769839af47349e894366d587a72) | Etherll |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
