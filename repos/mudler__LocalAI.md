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
| ⭐ **Stars** | 50.6k |
| 🍴 **Forks** | 4.7k |
| 🐞 **Open issues + PRs** | [216](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 71% · JavaScript 17% · TypeScript 3% · CSS 2% · C++ 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 260.1 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · 5d ago</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 7d ago</sub>

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

### [v4.11.0](https://github.com/mudler/LocalAI/releases/tag/v4.11.0)
<sub>2026-10-02 · 1mo ago</sub>

> **🎉 LocalAI 4.11.0 Release! 🚀**
> <h1 align="center">
>   <br>
>   <img height="300" src="https://raw.githubusercontent.com/mudler/LocalAI/refs/heads/master/core/http/static/logo.png">
>   <br>
>   <br>
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [test(addons): list the new package specs in the Ginkgo inventory](https://github.com/mudler/LocalAI/commit/b30d6f841d4ec874cf82bf4ae0d797c009ad655b) | mudler |
| 2026-11-26 | [test(cli): skip the read-only add-on folder spec on Windows](https://github.com/mudler/LocalAI/commit/f8291ea4ddca5c2b2e867edc9b41539a2cc1d322) | mudler |
| 2026-11-26 | [chore: :arrow_up: Update 0xShug0/audio.cpp to `ebf98246fe52f0c2b0f7b8…](https://github.com/mudler/LocalAI/commit/25b12a411c0ebc34265bf349e8943a1ba3f2985d) | localai-update-bot[bot] |
| 2026-11-26 | [feat(ui): hide the Files button in zero-retention chats](https://github.com/mudler/LocalAI/commit/eb37cac4fefb351a3ba3778878441d0ed1722343) | mudler |
| 2026-11-26 | [ci: run the container user-setup test when the start folders change](https://github.com/mudler/LocalAI/commit/ed91222a8aaf88b6bf9afd0ec824d275383ba2f3) | mudler |
| 2026-11-26 | [test(docker): expect add-ons off in the docker --user setup](https://github.com/mudler/LocalAI/commit/0430b828cc567dd0a7955f009f1687ba1894a9b1) | mudler |
| 2026-11-26 | [fix(startup): start without add-ons when the data folder is not writable](https://github.com/mudler/LocalAI/commit/b8b015430ab1244cf63c761a6f418fe24a95bf56) | mudler |
| 2026-11-26 | [test(docker): install an add-on and a backend in each container user …](https://github.com/mudler/LocalAI/commit/fbf5fb81d83daab8d301ecb29ff277f40b157e55) | mudler |
| 2026-11-26 | [docs: match the container pages to the final entrypoint](https://github.com/mudler/LocalAI/commit/93333618526a60a2f3b374fac3f4c9401b0b921b) | mudler |
| 2026-11-26 | [docs: lead with the compose file and explain the container user](https://github.com/mudler/LocalAI/commit/8fceccef05f73db7a46c4c6a63afe782b64e153c) | mudler |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
