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
| 🍴 **Forks** | 4.7k |
| 🐞 **Open issues + PRs** | [224](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 72% · JavaScript 17% · CSS 2% · C++ 2% · TypeScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `mamba` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 260.3 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [dev-master](https://github.com/mudler/LocalAI/releases/tag/dev-master) — Development build (084a302) _(pre-release)_
<sub>2026-11-15 · 10d ago</sub>

> Commit: 084a302ae766e09e5b690adc26fa3b550dc6fd0e
> Date: 2026-11-25T12:21:49Z
> Subject: fix(worker): remove staged backend builds of a killed update at start
> This is an unsupported development build of the master branch. Use a release for anything that matters.

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · 4d ago</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 6d ago</sub>

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
| 2026-11-25 | [feat(swagger): update swagger (#13467)](https://github.com/mudler/LocalAI/commit/5c81620e63fa9133f972169036242b019b6f6862) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update mudler/parakeet.cpp to `bc9cde302230068277e1…](https://github.com/mudler/LocalAI/commit/8403d7253944d5bfdebb1a44b39f2d116272617b) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update CrispStrobe/CrispASR to `ad22a042c64e54598f5…](https://github.com/mudler/LocalAI/commit/1ac1fb140442de3fe353b67f5ff31f3da6812125) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update ikawrakow/ik_llama.cpp to `ad217a220962edae4…](https://github.com/mudler/LocalAI/commit/f3dc0feb1bf418f9bfc92fa98ce84adb81c29bdf) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update ggml-org/whisper.cpp to `c1a24047871444999b7…](https://github.com/mudler/LocalAI/commit/fcc71dc504c9e3a7fb78a8849e32962dc1171b46) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update Niko1221/Strata to `v0.2.21 (d46f5f268f8ed79…](https://github.com/mudler/LocalAI/commit/094625c2a2a78154226494c2002d461e49064b03) | localai-update-bot[bot] |
| 2026-11-25 | [chore: :arrow_up: Update 0xShug0/audio.cpp to `86d9355a8e0647d1d190ac…](https://github.com/mudler/LocalAI/commit/1b6dd75b4d9b21d593fb9aac1af84f01ada8eb4e) | localai-update-bot[bot] |
| 2026-11-25 | [fix(worker): remove staged backend builds of a killed update at start](https://github.com/mudler/LocalAI/commit/084a302ae766e09e5b690adc26fa3b550dc6fd0e) | mudler |
| 2026-11-25 | [fix(gallery): remove the meta when its concrete backend is deleted](https://github.com/mudler/LocalAI/commit/e36bbd8cebe7a577dfdfa992cc416c5d63846c72) | mudler |
| 2026-11-25 | [fix(audio-cpp): patch the SVE tail of ggml_vec_dot_f32 (#13483)](https://github.com/mudler/LocalAI/commit/0b97d03333904f3c353e3e223f08d15f0748aa64) | mudler-agent |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
