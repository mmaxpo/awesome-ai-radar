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
| 🐞 **Open issues + PRs** | [222](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 71% · JavaScript 17% · TypeScript 3% · CSS 2% · C++ 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 266.9 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · 6d ago</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 8d ago</sub>

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
| 2026-11-27 | [fix(plugins): pin the localai entry to its commit after the rebase](https://github.com/mudler/LocalAI/commit/08f74d12b20cfd212b3d287d5c50f65aed917fe2) | mudler |
| 2026-11-27 | [test(assistant): raise the admin prompt budget to 10,600 bytes](https://github.com/mudler/LocalAI/commit/e2730c807d06ef0a61f4b847281524b3a2bb3f60) | mudler |
| 2026-11-27 | [fix(plugins): pin the localai entry to its commit after the rebase](https://github.com/mudler/LocalAI/commit/5737d6b5b42a1cbffe85dc6a8c67b0b047d48b67) | mudler |
| 2026-11-27 | [revert(plugins): keep the Add-ons page off with the add-on runtime](https://github.com/mudler/LocalAI/commit/5719c318a50098b8fa634ebaf15bd6870408d6c7) | mudler |
| 2026-11-27 | [fix(plugins): build the HTTP clients with pkg/httpclient](https://github.com/mudler/LocalAI/commit/bb40d742af55b57f6253f5aeb5178e43a922fb84) | mudler |
| 2026-11-27 | [fix(plugins): refuse trailing data after a plugin change](https://github.com/mudler/LocalAI/commit/e329476a3655d1a4b289ad5178fffd0165a5d0d4) | mudler |
| 2026-11-27 | [fix(plugins): keep a turn's plugins when one package has no model](https://github.com/mudler/LocalAI/commit/8fff58e2ab0309bab66500a6c660031dd5fe3d26) | mudler |
| 2026-11-27 | [fix(plugins): log a failed operation record of a plugin change](https://github.com/mudler/LocalAI/commit/6b39f422a7d8cde94459b596b213173a5b9e15dd) | mudler |
| 2026-11-27 | [fix(plugins): refuse a stray Sec-Fetch-Dest or mode without the site](https://github.com/mudler/LocalAI/commit/796fb1272a1cd3e5459e9f84de0e8a7e1a79158a) | mudler |
| 2026-11-27 | [fix(plugins): stop the refresh loop at shutdown and wait for it](https://github.com/mudler/LocalAI/commit/dfd8422184236034cad9eb4cca5ddecfaae3a6af) | mudler |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
