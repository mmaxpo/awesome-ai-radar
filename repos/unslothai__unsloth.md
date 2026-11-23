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
| ⭐ **Stars** | 80.1k |
| 🍴 **Forks** | 7.5k |
| 🐞 **Open issues + PRs** | [536](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.923-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 735.9 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.923-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.923-beta) — Inkling 1.9x faster inference
<sub>2026-11-23 · today</sub>

> Inkling 2 Mini runs up to 1.9x faster on all GPUs for decoding + RTX Spark improvements. Also new: faster GRPO and AsyncGRPO training, Qwen-Image-Flash and FastWan, a Knowledge page in Settings and audio, subtitle and image translation.
> **Highlights**
> - **Inkling 2 Mini on 8 to 12 GB GPUs** up to 1.9x faster decoding [guide](https://unsloth.ai/docs/models/inkling-2-mini#id-23rd-november-update)
> - **Multi-GPU diffusion LoRA training** about 2x the samples per second on two GPUs
> - **Qwen-Image-Flash + FastWan** 4-step images about 14x faster than Qwen-Image, 3-step video up to 3x faster
> - **GRPO improvements** AsyncGRPO 40% less time + 2x faster GRPO rollouts on Strix Halo**
> …

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · 2d ago</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · 2d ago</sub>

> There will be another release today in a few hours!
> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - new 26B (5.4 active) 1M context - strongest for size. [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> …

### [v0.1.920-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.920-beta) — AMD NPU + video diffusion LoRA
<sub>2026-11-19 · 4d ago</sub>

> AMD NPU support gets a big update in Unsloth: Q4NX models you convert now load on the NPU, and every NPU model shows whether it runs. Also new: LTX-2.5 and MOSS-Image LoRA training, NVIDIA Cosmos3 FP8 video and scheduled tasks that reply in a chat.
> **Highlights**
> - **AMD NPU support** - See [guide](https://unsloth.ai/docs/get-started/install/amd/npu) and official [AMD blog](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html) - NPUs are 2-4x more efficient per joule per token vs GPUs
> - **Faster images on Strix Halo** - FLUX.3 Klein up to 28% faster per step on Windows
> - **LTX-2.5 and MOSS-Image LoRA training** in Unsloth
> - **Diffusion LoRA training up to 42% faster** per step, and now on T4 GPUs too
> …

### [v0.1.919-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.919-beta) — Computer Use + Translate + MiniMax-H3-Image + New Model Picker
<sub>2026-11-17 · 6d ago</sub>

> This update brings **computer use (beta)**, letting local models see your screen and interact with apps, plus MCP integrations for Unity, Unreal Engine, Blender and Roblox.
> MiniMax-H3-Image now supports GGUF, FP8 and INT8, with LoRA training. We've also introduced a new model picker, redesigned Connections and improved project folders.
> **Highlights**
> - **Translate Page:** Translate any piece of text locally to any language.
> - **New model picker:** Switch models directly from the composer, with Favorites, On Device, Discover and Connected tabs.
> - **Engram:** Change and swap engrams for Qwen Flash and DeepSeek.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Studio: wait longer for a long summary prompt and retry a cut-off sum…](https://github.com/unslothai/unsloth/commit/5bdf38eacdfa3513b217409dcc70b7b8840a6622) | shimmyshimmer |
| 2026-11-23 | [Bump install.sh / install.ps1 pins to unsloth>=2026.11.10 (#19097)](https://github.com/unslothai/unsloth/commit/f5407c052a224792f1f1bdc549b3bdfc2cccf02c) | danielhanchen |
| 2026-11-23 | [Tensor parallel for Inkling 2: shard the wrapper attention by heads (…](https://github.com/unslothai/unsloth/commit/11801a62a47daf6c691528bd15ec87dbd2530f2a) | danielhanchen |
| 2026-11-23 | [Context parallel (Ulysses) for Inkling 2 (#19074)](https://github.com/unslothai/unsloth/commit/b0dea7145223444b237e9081c12e344028ae38a1) | danielhanchen |
| 2026-11-23 | [Update pyproject.toml](https://github.com/unslothai/unsloth/commit/699c0c3337fba1781328d6d6f0ebdf9b91af5e0d) | danielhanchen |
| 2026-11-23 | [Studio: let Max Tokens reach the model's window on Ollama and Custom …](https://github.com/unslothai/unsloth/commit/90a95e1f76f132a99897b8c1f64db3806ca476f8) | shimmyshimmer |
| 2026-11-23 | [Native FSDP2: shard a bitsandbytes 4-bit quantize-on-load while it lo…](https://github.com/unslothai/unsloth/commit/5a285dcfc2ab0b70e15d3725faade8263b5058e8) | danielhanchen |
| 2026-11-23 | [Diffusion backend tests: the apply_attention_backend stubs take fallb…](https://github.com/unslothai/unsloth/commit/4f4d6c589a63ccc7d25e55868c3ca476f276dad7) | danielhanchen |
| 2026-11-23 | [Studio: give local thinking a window budget, and compact after a thou…](https://github.com/unslothai/unsloth/commit/bf48fd932d847fcf61447e002bdb5b75c99f8c42) | danielhanchen |
| 2026-11-23 | [Cap Studio paging reserve on Windows integrated CUDA GPUs (#19081)](https://github.com/unslothai/unsloth/commit/169e4427a6901517e121ad4496728d81a7fe7601) | danielhanchen |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
