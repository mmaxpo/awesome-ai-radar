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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 254.0 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [dev-master](https://github.com/mudler/LocalAI/releases/tag/dev-master) — Development build (83d36f8) _(pre-release)_
<sub>2026-11-15 · 8d ago</sub>

> Commit: 83d36f88ab43e2ab44f4c0c69fa1e22527f0710e
> Date: 2026-11-23T13:41:56Z
> Subject: fix(grammars): exclude unescaped control characters in JSON string rules (#13417)
> This is an unsupported development build of the master branch. Use a release for anything that matters.

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · 2d ago</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 4d ago</sub>

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
| 2026-11-23 | [feat(ui): add video as a background kind (#13419)](https://github.com/mudler/LocalAI/commit/bad4daa93e8303ab5a9c12e7f3689449fb090f64) | mudler-agent |
| 2026-11-23 | [fix(grammars): exclude unescaped control characters in JSON string ru…](https://github.com/mudler/LocalAI/commit/83d36f88ab43e2ab44f4c0c69fa1e22527f0710e) | Kirep-06 |
| 2026-11-23 | [[llama-cpp] fix: catch all JSON exceptions when normalizing message c…](https://github.com/mudler/LocalAI/commit/d9b9019162cd18b742bcebb31b7446b2048cebc5) | leilei3167 |
| 2026-11-23 | [test(studio): find the wait message after a sub-agent report in wait_…](https://github.com/mudler/LocalAI/commit/e62bb30b5208aa600490116509775d647e6dae18) | mudler |
| 2026-11-23 | [test(addons): list the launch diagnostics specs in the case inventories](https://github.com/mudler/LocalAI/commit/9b377d230f7b317f411963243423d9dba90214f0) | mudler |
| 2026-11-23 | [docs(addons): tell where the reason of a failed upgrade is](https://github.com/mudler/LocalAI/commit/5e07944c986c638f3e29ee60767db8e9dd6e11d2) | mudler |
| 2026-11-23 | [fix(addons): put the launch cause in the log of a failed upgrade](https://github.com/mudler/LocalAI/commit/e1b1db069fa5b2eedf428937f9833d42953ed2c4) | mudler |
| 2026-11-23 | [fix(addons): say why an add-on process did not launch](https://github.com/mudler/LocalAI/commit/403b90a1bbb643fe25aa41c3cd6fa7fd1971c670) | mudler |
| 2026-11-23 | [fix(ui): keep the list picker menu inside the panel that holds it](https://github.com/mudler/LocalAI/commit/fc6c68f2007239cb873b7fd852b5815ab781dbc3) | mudler |
| 2026-11-23 | [test(addons): list the lifecycle and gateway specs in the case invent…](https://github.com/mudler/LocalAI/commit/e428a08006164fd0c3094e9867648a34bda9b2df) | mudler |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
