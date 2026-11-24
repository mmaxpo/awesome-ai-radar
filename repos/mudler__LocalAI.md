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
| 🐞 **Open issues + PRs** | [226](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 72% · JavaScript 17% · CSS 2% · C++ 2% · TypeScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `mamba` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 256.6 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [dev-master](https://github.com/mudler/LocalAI/releases/tag/dev-master) — Development build (e00e621) _(pre-release)_
<sub>2026-11-15 · 9d ago</sub>

> Commit: e00e6219f1653cabcc4b7d8fafdbaa03dc840a18
> Date: 2026-11-24T13:41:30Z
> Subject: feat(updates): run backend, model and add-on updates as server-owned runs (#13447)
> This is an unsupported development build of the master branch. Use a release for anything that matters.

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · 3d ago</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 5d ago</sub>

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
| 2026-11-24 | [chore(model-gallery): :arrow_up: update checksum (#13434)](https://github.com/mudler/LocalAI/commit/c327dd34b2b72740fd5e7cc631fb5ac3a96826a0) | localai-update-bot[bot] |
| 2026-11-24 | [chore: :arrow_up: Update leejet/stable-diffusion.cpp to `3b12781fac1a…](https://github.com/mudler/LocalAI/commit/99a2c9012dd5bc81d7ac69bc8b87379a020c8c67) | localai-update-bot[bot] |
| 2026-11-24 | [chore: :arrow_up: Update TheTom/llama-cpp-turboquant to `f7c3638e83ff…](https://github.com/mudler/LocalAI/commit/c6e2d51d3043b7b66442e4a62236a14b674b3dec) | localai-update-bot[bot] |
| 2026-11-24 | [chore: :arrow_up: Update ggml-org/whisper.cpp to `96ec4d9823e9d021194…](https://github.com/mudler/LocalAI/commit/11dd26dad472c5e4a98d4ef9b0fcc416adabdc23) | localai-update-bot[bot] |
| 2026-11-24 | [Stage audio transform files on remote workers](https://github.com/mudler/LocalAI/commit/5c5d7cfc9c6f982a679c0def441534c73b4e6607) | mudler |
| 2026-11-24 | [chore: :arrow_up: Update 0xShug0/audio.cpp to `caa060b68784596c536c3e…](https://github.com/mudler/LocalAI/commit/83a4c81b3e0e5b3d1dd6200f0d2ff3b0632f4470) | localai-update-bot[bot] |
| 2026-11-24 | [chore: :arrow_up: Update CrispStrobe/CrispASR to `ac1c1974920eb1907ce…](https://github.com/mudler/LocalAI/commit/f9698977da0272634983498657712770cfab4d2c) | localai-update-bot[bot] |
| 2026-11-24 | [ci(addons): fail early on a missing Ginkgo inventory entry (#13450)](https://github.com/mudler/LocalAI/commit/49e6932c9118bb0a85a2925eb24b5aa1a5bc950a) | mudler-agent |
| 2026-11-24 | [fix(gallery): remove the pack a Strata model built when it is deleted](https://github.com/mudler/LocalAI/commit/f8a5c5bf62aed9cb27dde4a6f1bcae77df1a8095) | mudler |
| 2026-11-24 | [fix(distributed): keep an explicit batch that equals a managed defaul…](https://github.com/mudler/LocalAI/commit/757a0eb4204781b38390b22f50d46bca4bdb86da) | mudler-agent |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
