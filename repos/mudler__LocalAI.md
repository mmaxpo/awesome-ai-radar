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
| 🐞 **Open issues + PRs** | [212](https://github.com/mudler/LocalAI/issues) |
| 💻 **Languages** | Go 72% · JavaScript 17% · CSS 2% · C++ 2% · TypeScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llama` `ai` `llm` `stable-diffusion` `api` `tts` `musicgen` `mamba` `audio-generation` `image-generation` `text-generation` `rerank` `distributed` `libp2p` `decentralized` `object-detection` `mcp` `agents` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-03-18 |
| 📦 **Latest release** | [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1) — 2026-11-20 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 251.5 MB |
| 🌐 **Website** | https://localai.io |

## 📦 Recent releases

### [dev-master](https://github.com/mudler/LocalAI/releases/tag/dev-master) — Development build (077dd65) _(pre-release)_
<sub>2026-11-15 · 6d ago</sub>

> Commit: 077dd65dd964ebdde60fc97a6e25aa8e3b4906ab
> Date: 2026-11-21T13:10:51Z
> Subject: test(addons): list the new cases and document the signer in the apps spec
> This is an unsupported development build of the master branch. Use a release for anything that matters.

### [v5.0.1](https://github.com/mudler/LocalAI/releases/tag/v5.0.1)
<sub>2026-11-20 · today</sub>

> **What's Changed**
> **Other Changes**
> * feat(rocm): build the hipblas images on ROCm 10.1 by default by @walcz-de in https://github.com/mudler/LocalAI/pull/13169
> * feat(ui): call the middle network choice Custom and show its domains by @mudler-agent in https://github.com/mudler/LocalAI/pull/13294
> * feat(launcher): show desktop notifications for the server inbox by @mudler-agent in https://github.com/mudler/LocalAI/pull/13298
> * feat(i18n): add Bangla (bn) translation for React UI and add-ons by @AnythingLinux in https://github.com/mudler/LocalAI/pull/13304
> …

### [v5.0.0](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)
<sub>2026-11-18 · 2d ago</sub>

> <p align="center">
>   <em>
> <img width="1920" height="1080" alt="site-release-1920x1080-v3" src="https://github.com/user-attachments/assets/92800193-8455-425c-9972-5955bb6483ae" />
> </em>
> </p>
> Run open models for chat, images, speech and video on your own machines. The API speaks the OpenAI and Anthropic formats. Your team gets chats, files and documents on top, and the assistant can write and run code. 5.0 adds a desktop app, Projects, a Files page, Office documents, a Python sandbox, team sharing and an add-on library, all built on chats that now run on the server.
> …

### [v4.12.1](https://github.com/mudler/LocalAI/releases/tag/v4.12.1)
<sub>2026-10-23 · 29d ago</sub>

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
| 2026-11-21 | [test(ui): hold the estimate until the sizing state is seen](https://github.com/mudler/LocalAI/commit/e2ce44372bebd4ee8f71108690484ab421094303) | mudler |
| 2026-11-21 | [test(p2prelay): keep a pass pending when checking that refusals look …](https://github.com/mudler/LocalAI/commit/2951b3228fcf4c89bb79102a7ae57ee489d28b0a) | mudler |
| 2026-11-21 | [test(addons): list the two signer cases in the gateway and apps inven…](https://github.com/mudler/LocalAI/commit/ca795d214c256a2df6f7349820fb567f9504bfce) | mudler |
| 2026-11-21 | [test(addons): list the new cases and document the signer in the apps …](https://github.com/mudler/LocalAI/commit/077dd65dd964ebdde60fc97a6e25aa8e3b4906ab) | mudler |
| 2026-11-21 | [Remove the cluster-wide change of carrier](https://github.com/mudler/LocalAI/commit/0b1e21e9d2f0f805f5c2968ef0be654fa84f6ba0) | mudler |
| 2026-11-21 | [fix(importer): pair a repo's speculative drafter with the model](https://github.com/mudler/LocalAI/commit/ae2083366d3d55f085e34820022b526c6d8a7e1f) | mudler |
| 2026-11-21 | [Judge the health of a node by the routes it holds](https://github.com/mudler/LocalAI/commit/db133cfc364234d74db46a83ef478598fb594f9b) | mudler |
| 2026-11-21 | [fix(addons): stop asking for approval once the upgrade is approved](https://github.com/mudler/LocalAI/commit/e7fa6f7fa156774a30cd8cad57e317fb13296413) | mudler |
| 2026-11-21 | [Send requests between processes over the peer link only](https://github.com/mudler/LocalAI/commit/c67e6f7e8d187fd40985e9a2579c0bc92e57827b) | mudler |
| 2026-11-21 | [fix(localaitools): fit the admin turn prompt in its budget again](https://github.com/mudler/LocalAI/commit/4333b5c1feaa40fe501200c05b7a18611570d0f9) | mudler |

[See all commits ↗](https://github.com/mudler/LocalAI/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mudler/LocalAI.git
```
