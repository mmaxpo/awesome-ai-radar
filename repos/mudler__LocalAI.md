# mudler/LocalAI

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/mudler/LocalAI)

> LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Self-hosted OpenAI-compatible engine for LLMs, voice, image |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 50.5k |
| 🍴 **Forks** | 4.6k |
| 🐞 **Open issues + PRs** | [208](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 72% · JavaScript 17% · CSS 2% · C++ 2% · TypeScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `mamba` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 253.0 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [dev-master](https://github.com/mudler/LocalAI/releases/tag/dev-master) — Development build (e68e9fb) _(pre-release)_
<sub>2026-11-15 · 7d ago</sub>

> Commit: e68e9fbbab5242cc4fcd80e89b90640b03b9c68f
> Date: 2026-11-22T09:00:57Z
> Subject: fix(trace): keep persisted traces when one file cannot be read
> This is an unsupported development build of the master branch. Use a release for anything that matters.

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · yesterday</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 3d ago</sub>

> <p align="center">
>   <em>
> <img width="1920" height="1080" alt="site-release-1920x1080-v3" src="https://github.com/user-attachments/assets/92800193-8455-425c-9972-5955bb6483ae" />
> </em>
> </p>
> Run open models for chat, images, speech and video on your own machines. The API speaks the OpenAI and Anthropic formats. Your team gets chats, files and documents on top, and the assistant can write and run code. 5.0 adds a desktop app, Projects, a Files page, Office documents, a Python sandbox, team sharing and an add-on library, all built on chats that now run on the server.
> …

### [v4.12.1](https://github.com/mudler/LocalAI/releases/tag/v4.12.1)
<sub>2026-10-23 · 1mo ago</sub>

> Patch release v4.12.1. Security fix only.
> **Security**
> - Hardened the external URL policy for user-supplied URLs (chat vision image/audio/video URLs, image and audio endpoints). Redirect targets are now validated on every hop, 100.64.0.0/10 and 0.0.0.0/8 are treated as non-public, and the connection goes to the address that was validated. See #12853. Credits to @spicysharkco for the discovery.
> **Full Changelog**: https://github.com/mudler/LocalAI/compare/v4.12.0...v4.12.1

### [v4.12.0](https://github.com/mudler/LocalAI/releases/tag/v4.12.0)
<sub>2026-10-22 · 1mo ago</sub>

> **🎉 LocalAI 4.12.0 Release! 🚀**
> <h1 align="center">
>   <br>
>   <img height="300" src="https://raw.githubusercontent.com/mudler/LocalAI/refs/heads/master/core/http/static/logo.png">
>   <br>
>   <br>
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [fix(trace): keep persisted traces when one file cannot be read](https://github.com/mudler/LocalAI/commit/e68e9fbbab5242cc4fcd80e89b90640b03b9c68f) | mudler |
| 2026-11-22 | [fix(ui): list backend log processes from the workers in a cluster](https://github.com/mudler/LocalAI/commit/9e8c76d648e0894ec3b4226b79236c47f65c1a64) | mudler |
| 2026-11-22 | [test(importers): use Ginkgo for the repository ID test](https://github.com/mudler/LocalAI/commit/c332830228f69681101bb7792c6ae6bfcfa08d9f) | mudler |
| 2026-11-22 | [fix(importers): accept scheme-less Hugging Face repository URIs](https://github.com/mudler/LocalAI/commit/66f593afec5cb9a0b6d1f5fd573c45f5a75c77ff) | mudler |
| 2026-11-22 | [chore: :arrow_up: Update 0xShug0/audio.cpp to `04a37f2e80ff2dbcdd84cc…](https://github.com/mudler/LocalAI/commit/100afd737ef0c2feff13d62874312afb6d09ad4d) | localai-update-bot[bot] |
| 2026-11-22 | [chore: :arrow_up: Update CrispStrobe/CrispASR to `6974f1825e18ccd5ab7…](https://github.com/mudler/LocalAI/commit/214e8f79b66c8120a0872721d6ebfe409fb88427) | localai-update-bot[bot] |
| 2026-11-22 | [fix(importers): import Ollama models by name, params and projector, a…](https://github.com/mudler/LocalAI/commit/00ab41086592d8c24bd4b16e10373b04752f162b) | mudler-agent |
| 2026-11-22 | [feat(addons): add the Ollama search add-on (#13383)](https://github.com/mudler/LocalAI/commit/a8a7ea460a1f791b46731e0e2b5a857d12783f52) | mudler-agent |
| 2026-11-22 | [feat(modelsearch): accept ollama:// search results and list their lay…](https://github.com/mudler/LocalAI/commit/aca3d8c9f2f577e04b012d9b8ca83b702d40fdf9) | mudler-agent |
| 2026-11-22 | [chore: :arrow_up: Update ggml-org/whisper.cpp to `5eaee0cc9024eb9e9a9…](https://github.com/mudler/LocalAI/commit/63ea3075705376975b6d0978d4769e6ce0ec094f) | localai-update-bot[bot] |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
