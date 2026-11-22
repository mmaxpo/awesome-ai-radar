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
| ⭐ **Stars** | 80.0k |
| 🍴 **Forks** | 7.4k |
| 🐞 **Open issues + PRs** | [569](https://github.com/unslothai/unsloth/issues) |
| 💻 **Languages** | Python 73% · TypeScript 23% · PowerShell 1% · Shell 1% · Rust 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `fine-tuning` `llama` `llms` `gemma` `unsloth` `llm` `deepseek` `text-to-speech` `tts` `qwen` `agent` `openai` `reinforcement-learning` `self-hosted` `ui` `image-generation` `stable-diffusion` `chatgpt` `ai` `python` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-11-29 |
| 📦 **Latest release** | [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 721.8 MB |
| 🌐 **Website** | https://unsloth.ai/docs |

## 📦 Recent releases

### [v0.1.922-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.922-beta) — Inkling Mini + Bug fixes
<sub>2026-11-20 · yesterday</sub>

> Run the new Inkling 2 Mini model, the strongest 26.4B model that runs on 16GB RAM.
> This release makes image generation faster and lighter on small GPUs. Macs with Apple Silicon can now restyle videos, and chats that use MCP tools no longer reprocess the whole conversation on every message.
> **Highlights**
> - **Inkling 2 Mini** - less memory usage and faster. New 26B (5.4 active) 1M context - [Guide](https://unsloth.ai/docs/models/inkling-2-mini)
> - **MiniMax-H3-Image on 8GB GPUs** renders a new prompt in 36.7 s (prev 82.7 s)
> - **GGUF image models load with 52-66% less RAM** on Linux and macOS
> …

### [v0.1.921-beta](https://github.com/unslothai/unsloth/releases/tag/v0.1.921-beta) — Bug Fixes + Faster images +Inkling Mini + faster MCP chats
<sub>2026-11-20 · yesterday</sub>

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
| 2026-11-22 | [Diffusion DDP tests: rendezvous through a FileStore, not a port picke…](https://github.com/unslothai/unsloth/commit/5b4b8360917bcf79530f77b0422745e1e7f3e9e6) | danielhanchen |
| 2026-11-22 | [Tests: two reds from #18856 (exec-d _utils helper cannot do its relat…](https://github.com/unslothai/unsloth/commit/28eaeb732914dbd9972fb92af92d77702f0a036f) | danielhanchen |
| 2026-11-22 | [Studio: keep accented and non-Latin text in pages saved from Chrome (…](https://github.com/unslothai/unsloth/commit/c751a7a5576f8822114d320b8fb2d06c45ae7ddd) | NilayYadav |
| 2026-11-22 | [Private push: refuse a public repo before writing dataset metadata (#…](https://github.com/unslothai/unsloth/commit/bf082c96ad848826f8831d863761081ade62601b) | danielhanchen |
| 2026-11-22 | [Studio FLUX.2 klein 9B-KV: run KV checkpoints on their own pipeline (…](https://github.com/unslothai/unsloth/commit/acb504cbc89689867a54fdcef830a4aecd04fb7f) | danielhanchen |
| 2026-11-22 | [Studio: keep pasted screenshots in imported Cursor chats (#18703)](https://github.com/unslothai/unsloth/commit/57aafaa95472860f1271683018a37e8bf717e517) | NilayYadav |
| 2026-11-22 | [Studio: keep the audio.cpp accelerator chosen at install across updat…](https://github.com/unslothai/unsloth/commit/c6d4ef2687da2be3a09748c046dec0547515f6d6) | NilayYadav |
| 2026-11-22 | [ROCm SDPA check: run the probe children in a private directory (#18858)](https://github.com/unslothai/unsloth/commit/f03851a8e89c1d208f1070e72ddff4701170dbb0) | danielhanchen |
| 2026-11-22 | [Studio: let the model see images read in imported Claude Code chats (…](https://github.com/unslothai/unsloth/commit/94d96c084ef1bf350504daf79895dec915cfbf2d) | NilayYadav |
| 2026-11-22 | [Studio: keep the tool call cap picked with MCP on across reloads (#18…](https://github.com/unslothai/unsloth/commit/582698f7d25f2efc4ece65b8524e78afe54f66fb) | NilayYadav |

[See all commits ↗](https://github.com/unslothai/unsloth/commits)

## ⬇️ Get it

```bash
git clone https://github.com/unslothai/unsloth.git
```
