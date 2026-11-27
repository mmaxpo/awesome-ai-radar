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
| 🐞 **Open issues + PRs** | [638](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 763.9 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.925-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.925-beta) — Inkling finetuning + perf fixes
<sub>2026-11-25 · 2d ago</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Bug fixes for finetuning Inkling 2 Mini** + other bugs, MXC sandbox upgraded
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> …

### [v0.1.924-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta) — Inkling finetuning + perf fixes
<sub>2026-11-24 · 3d ago</sub>

> **Inkling Fine-tuning**
> You can now fine-tune Inkling 2 Mini 1.8 to 3.1x faster and use 50% less VRAM in Unsloth with LoRA or QLoRA, then export it to GGUF or a merged 16-bit model. It trains on Kaggle's free 2x T4 and now supports tensor, pipeline and context parallel across GPUs. Also new: faster `adamw_8bit` steps, faster Z-Image LoRA training on T4 and fixes for thinking models in chat.
> **Highlights**
> - **Fine-tune Inkling 2 Mini 3x faster + 50% less VRAM** in Unsloth Desktop. [Guide](https://unsloth.ai/docs/models/inkling-2-mini/finetuning-inkling-2-mini)
> - **Faster Inkling 2 Mini inference** Fixed incorrect max context length (2-3x faster inference)
> - **Faster `adamw_8bit`** up to 12% less time per step on small batches
> …

### [v0.1.923-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) — Inkling 1.9x faster inference + Training
<sub>2026-11-23 · 3d ago</sub>

> Inkling 2 Mini runs up to 1.9x faster on all GPUs for decoding + RTX Spark improvements. Also new: faster GRPO and AsyncGRPO training, Qwen-Image-Flash and FastWan, a Knowledge page in Settings and audio, subtitle and image translation.
> **Highlights**
> - **Inkling 2 Mini on 8 to 12 GB GPUs** up to 1.9x faster decoding [guide](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update)
> - Fine-tuning for Inkling in Unsloth is now available
> - **Multi-GPU diffusion LoRA training** about 2x the samples per second on two GPUs
> - **Qwen-Image-Flash + FastWan** 4-step images about 14x faster than Qwen-Image, 3-step video up to 3x faster
> …

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · 6d ago</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · 6d ago</sub>

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
| 2026-11-27 | [Merge reloaded PiSSA and OLoRA adapters relative to the original base…](https://github.com/unslothai/unsloth/commit/8e7827d025c916773298d118c8d138be4d525c83) | vineethsaivs |
| 2026-11-27 | [Studio: hybrid token count (superseded by #15900) (#15857)](https://github.com/unslothai/unsloth/commit/05f72fe50356c2d37f6695119c54cb57eb4ede83) | fredjt |
| 2026-11-27 | [Studio: keep the Qwen-Image and Wan VAE encoders stock so edits and i…](https://github.com/unslothai/unsloth/commit/15a57d17d47290139c99ca696b82a741a655d8d4) | danielhanchen |
| 2026-11-27 | [fix(studio): count spliced media columns in MLX VLM chat usage (#19909)](https://github.com/unslothai/unsloth/commit/781e6c6bc5fe3954cea663a867db50587ef4f283) | Lyxot |
| 2026-11-27 | [Studio RAG: re-embed with one stale-document scan and one vector-row …](https://github.com/unslothai/unsloth/commit/d36364a3df84fcfc0219ae00a7f17cd2c799537a) | danielhanchen |
| 2026-11-27 | [FSDP2 auto GA: replicated gradients wait for the last micro-batch aga…](https://github.com/unslothai/unsloth/commit/d31951a3bb01ec498a63ef9156de7f27aecdbbed) | danielhanchen |
| 2026-11-27 | [DoRA FP8 test: read the source as utf-8 (encoding guard red on main) …](https://github.com/unslothai/unsloth/commit/486ede896bcab6354feb6050e0d4f80482d98c63) | danielhanchen |
| 2026-11-27 | [Studio: show the backend's error message, not [object Object], when a…](https://github.com/unslothai/unsloth/commit/e29080864f88497e44e6716c32a3372eebc5747d) | oobabooga |
| 2026-11-27 | [Honor DDP common CUDA training dtype (#13030)](https://github.com/unslothai/unsloth/commit/9e531e15583b27e3f3eeee7ef415c34f4ea9228c) | cezartolvai |
| 2026-11-27 | [fix(studio): rebuild @skill manifests into the system prompt on every…](https://github.com/unslothai/unsloth/commit/f106b195591ecdb7b8022b72f41ef50f665b4f65) | Lyxot |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
