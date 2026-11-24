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
| 🐞 **Open issues + PRs** | [543](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.924-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 735.7 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.924-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.924-beta) — Inkling finetuning + perf fixes
<sub>2026-11-24 · today</sub>

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
<sub>2026-11-20 · 3d ago</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · 3d ago</sub>

> There will be another release today in a few hours!
> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - new 26B (5.4 active) 1M context - strongest for size. [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> …

### [v0.1.920-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.920-beta) — AMD NPU + video diffusion LoRA
<sub>2026-11-19 · 5d ago</sub>

> AMD NPU support gets a big update in Unsloth: Q4NX models you convert now load on the NPU, and every NPU model shows whether it runs. Also new: LTX-2.5 and MOSS-Image LoRA training, NVIDIA Cosmos3 FP8 video and scheduled tasks that reply in a chat.
> **Highlights**
> - **AMD NPU support** - See [guide](https://unsloth.ai/docs/get-started/install/amd/npu) and official [AMD blog](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html) - NPUs are 2-4x more efficient per joule per token vs GPUs
> - **Faster images on Strix Halo** - FLUX.3 Klein up to 28% faster per step on Windows
> - **LTX-2.5 and MOSS-Image LoRA training** in Unsloth
> - **Diffusion LoRA training up to 42% faster** per step, and now on T4 GPUs too
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Studio: keep the composer's right controls across keystrokes (#19248)](https://github.com/unslothai/unsloth/commit/345bf28e48bb05a765e9bf20d650b12ae3441ee4) | danielhanchen |
| 2026-11-24 | [Studio i18n: translate the llama.cpp backend picker unavailable reaso…](https://github.com/unslothai/unsloth/commit/88ffd00c5d6d2780446408da96f656bb36727a5b) | danielhanchen |
| 2026-11-24 | [Studio chat sync: compare a generated reply's stored JSON by string f…](https://github.com/unslothai/unsloth/commit/58e31c2cfba28ab3e0ff06be29b1aee0b446d5e7) | danielhanchen |
| 2026-11-24 | [Tests: pin the host RAM the llama.cpp placement tests launch on (#19283)](https://github.com/unslothai/unsloth/commit/f28190a19d4806405c9fed14aac7c6f766fb74c4) | danielhanchen |
| 2026-11-24 | [GGUF LoRA export: read quantization_method case insensitively (#19113)](https://github.com/unslothai/unsloth/commit/55bafc96ba2cd6c0f2e9218880f0f1b12da75765) | abhishekacharya200 |
| 2026-11-24 | [Studio: skip the vLLM / SGLang port ownership scan until the engine i…](https://github.com/unslothai/unsloth/commit/2400b2e77f531672f95f90bde5c02dab9f7482ac) | danielhanchen |
| 2026-11-24 | [feat(mlx): start a vllm-metal engine for fast_inference on Apple Sili…](https://github.com/unslothai/unsloth/commit/58e381a2f9f27090eb59950ded05e1c0b6bfb62a) | Lyxot |
| 2026-11-24 | [Studio chat history: decode a large whole-thread save body off the ev…](https://github.com/unslothai/unsloth/commit/36ef20a3a681b2edba3f5c2b4c7c5736252a073c) | danielhanchen |
| 2026-11-24 | [Bump install.sh / install.ps1 pins to unsloth>=2026.11.11 (#19279)](https://github.com/unslothai/unsloth/commit/411d774af75f7de1f83908ac16d7503f140c38f8) | danielhanchen |
| 2026-11-24 | [Studio logs: add the managed vLLM log family to the reviewed list (#1…](https://github.com/unslothai/unsloth/commit/3e93897193d7843cd1a916eee2cf6bad9a02a513) | danielhanchen |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
