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
| ⭐ **Stars** | 79.9k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [523](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 72% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 715.8 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · today</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · today</sub>

> There will be another release today in a few hours!
> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - new 26B (5.4 active) 1M context - strongest for size. [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> …

### [v0.1.920-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.920-beta) — AMD NPU + video diffusion LoRA
<sub>2026-11-19 · 2d ago</sub>

> AMD NPU support gets a big update in Unsloth: Q4NX models you convert now load on the NPU, and every NPU model shows whether it runs. Also new: LTX-2.5 and MOSS-Image LoRA training, NVIDIA Cosmos3 FP8 video and scheduled tasks that reply in a chat.
> **Highlights**
> - **AMD NPU support** - See [guide](https://unsloth.ai/docs/get-started/install/amd/npu) and official [AMD blog](https://www.amd.com/en/blogs/2026/unlocking-the-amd-ryzen-ai-npu-for-unsloth-desktop.html) - NPUs are 2-4x more efficient per joule per token vs GPUs
> - **Faster images on Strix Halo** - FLUX.3 Klein up to 28% faster per step on Windows
> - **LTX-2.5 and MOSS-Image LoRA training** in Unsloth
> - **Diffusion LoRA training up to 42% faster** per step, and now on T4 GPUs too
> …

### [v0.1.919-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.919-beta) — Computer Use + Translate + MiniMax-H3-Image + New Model Picker
<sub>2026-11-17 · 4d ago</sub>

> This update brings **computer use (beta)**, letting local models see your screen and interact with apps, plus MCP integrations for Unity, Unreal Engine, Blender and Roblox.
> MiniMax-H3-Image now supports GGUF, FP8 and INT8, with LoRA training. We've also introduced a new model picker, redesigned Connections and improved project folders.
> **Highlights**
> - **Translate Page:** Translate any piece of text locally to any language.
> - **New model picker:** Switch models directly from the composer, with Favorites, On Device, Discover and Connected tabs.
> - **Engram:** Change and swap engrams for Qwen Flash and DeepSeek.
> …

### [v0.1.918-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.918-beta) — Computer Use, MiniMax-H3-Image + Perf fixes
<sub>2026-11-16 · 5d ago</sub>

> This update brings **computer use (beta)**, letting local models see your screen and interact with apps, plus MCP integrations for Unity, Unreal Engine, Blender and Roblox.
> MiniMax-H3-Image now supports GGUF, FP8 and INT8, with LoRA training. We've also introduced a new model picker, redesigned Connections and improved project folders.
> **Highlights**
> - **Engram:** Change and swap engrams for Qwen Flash and DeepSeek.
> - **Computer use (beta):** Local vision models and connected providers can now see your screen and interact with apps. Off by default, with permission controls.
> - **Game engines + creative apps:** Connect Unreal Engine, Unity, Godot and Roblox through MCP, alongside Blender.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [CI: hold the HF=latest legs below transformers 5.24 until unsloth-zoo…](https://github.com/unslothai/unsloth/commit/ee62cb7857ded11ecfe68a11f123a03f803ff55e) | danielhanchen |
| 2026-11-21 | [Security audit: re-review the transformers 5.24.0 testing_utils.py si…](https://github.com/unslothai/unsloth/commit/8b7cde79ebf5a901b2fd936bbee214fb8c7562c7) | danielhanchen |
| 2026-11-21 | [Studio tests: forget the served-vision answer between the two servers…](https://github.com/unslothai/unsloth/commit/fd3bbb269ea2f7db2321c8950d22a0c345dca6e6) | danielhanchen |
| 2026-11-21 | [Pipeline parallel: keep the frozen-prefix skip off on later stages (#…](https://github.com/unslothai/unsloth/commit/ed74b5983e9e3169ec1d6c9aec777d1127069f24) | danielhanchen |
| 2026-11-21 | [Studio: wallpaper chat masks only the composer's own box (#18751)](https://github.com/unslothai/unsloth/commit/6117d4c761a41db762c9d0abe2719e4ee1864f72) | shimmyshimmer |
| 2026-11-21 | [Studio: permission pill shows its icon only when collapsed (#18750)](https://github.com/unslothai/unsloth/commit/62126b447afadcd6af08eaa7759f95831193be70) | shimmyshimmer |
| 2026-11-21 | [Tests: read llama.py as UTF-8 in the vocab-parallel gloo test (#18743)](https://github.com/unslothai/unsloth/commit/c9670d85833bd1c0c02ad944fc229e51cf374b12) | danielhanchen |
| 2026-11-21 | [Studio tests: seed the dense fast-LoRA parity input and hold its inpu…](https://github.com/unslothai/unsloth/commit/ba4979c497e17b9e190da25cfcb31eff6e4069a5) | danielhanchen |
| 2026-11-21 | [Native TP: opt-in vocab-parallel lm_head and cross entropy (#18625)](https://github.com/unslothai/unsloth/commit/77f37de186a9c0483dc869360dba4845ef656605) | danielhanchen |
| 2026-11-21 | [Windows No Compiler CI: measure again when only the file watcher fail…](https://github.com/unslothai/unsloth/commit/cb27fb7c5fae07afaa608a1adf8c0cbedc609e47) | danielhanchen |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
