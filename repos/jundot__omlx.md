# jundot/omlx

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/jundot/omlx)

> LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Project** | — |
| **Why I saved it** | Local LLM server for Apple Silicon (batching + SSD cache) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 23.5k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [495](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 3% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 93.3 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 6d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

### [v0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3) — 0.7.3
<sub>2026-10-31 · 10d ago</sub>

> **oMLX 0.7.3**
> oMLX 0.7.3 makes DeepSeek V4.1 prefill and batched decode faster, lets Ask AI hold voice conversations, search the web, read links and look at your screen, and cuts memory use when many requests run at long context. The notes below cover changes since 0.7.3rc1, and earlier 0.7.3 highlights are summarized at the end.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos15-sequoia.dmg)
> https://github.com/user-attachments/assets/d63f2dbd-a3a9-47e0-bf1f-1add45c39395
> **Ask AI Voice Mode, Web Search and Screen Capture**
> Talk to your local models. Turn on Voice under App > Ask AI, press Option-Shift-Space and speak, and the answer plays back with captions. Ask AI can also search the web, read links and look at your screen (#4976).
> …

### [v0.7.3rc1](https://github.com/jundot/omlx/releases/tag/v0.7.3rc1) — 0.7.3rc1
<sub>2026-10-27 · 15d ago</sub>

> **oMLX 0.7.3rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> The release candidate for oMLX 0.7.3 adds Ask AI, a question bar for your local models in any app, a GPU power limit for working on battery, and Ling 3.1 Flash with Lightning MTP. It also brings everything from the 0.7.3 development releases: MiniMax M3.1 Flash, faster M1 and M5 Macs, and better low-bit oQ.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos15-sequoia.dmg)
> **Ask AI**
> Ask your local models from any app. Press Option-Space and a question bar floats over whatever you are working on without taking focus, and the answer streams in as Markdown. Slash presets set the model and system prompt per command, so `/translate` can run a small model with a fixed prompt and copy the result for you. Vision models also take images pasted with Command-V. Turn it on in the macOS app under App > Ask AI. #4854
> …

### [v0.7.3.dev2](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev2) — 0.7.3.dev2
<sub>2026-10-25 · 17d ago</sub>

> **oMLX 0.7.3.dev2**
> > This is a hotfix release that fixes an error when turning on Lightning MTP for MiniMax M3.1 (#4827). It also removes the stray `</think>` at the start of MiniMax M3.1 non-streaming replies and fixes prefill for DeepSeek V4 Flash oQ3.5e.
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> oMLX 0.7.3.dev2 adds MiniMax M3.1 Flash with Lightning MTP, makes M1 and M5 Macs, DFlash on fp16 models and GLM-5.3 faster, and gives low-bit oQ quants a better split of their bits.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos15-sequoia.dmg)
> **MiniMax M3.1 Flash**
> …

### [v0.7.3.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev1) — 0.7.3.dev1
<sub>2026-10-24 · 17d ago</sub>

> **oMLX 0.7.3.dev1**
> > Please use [oMLX 0.7.3.dev2](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev2) instead. It is a hotfix release that fixes an error when turning on Lightning MTP for MiniMax M3.1 (#4827). The download links below now point to 0.7.3.dev2.
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> oMLX 0.7.3.dev1 adds MiniMax M3.1 Flash with Lightning MTP, makes M1 and M5 Macs, DFlash on fp16 models and GLM-5.3 faster, and gives low-bit oQ quants a better split of their bits.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos15-sequoia.dmg)
> **MiniMax M3.1 Flash**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [fix(stt): reserve realtime sessions before backend startup (#5092)](https://github.com/jundot/omlx/commit/db4b4176985277359f739655a01eae5e3a6fa412) | Aminark |
| 2026-11-11 | [feat(macos): add sidebar search for global settings (#5111)](https://github.com/jundot/omlx/commit/edbcc89b8a615818fa2ad729f4db26b8e0a6a686) | ngutech21 |
| 2026-11-11 | [fix(bench): grow a short saved Splash context for the run (#4938)](https://github.com/jundot/omlx/commit/066bcaaf9da454d07b020e196dde2489c1fe4bcb) | jundot |
| 2026-11-11 | [perf(affine4): run multi-row attention chunks in one launch (#5101)](https://github.com/jundot/omlx/commit/82bb526cc8af30c7a0acd5835bd17289da37c2d6) | avifenesh |
| 2026-11-11 | [feat(macos): add MarkItDown integration settings (#5107)](https://github.com/jundot/omlx/commit/b1b173b2fe4e0966a6fec257685679e7f2ba4a6e) | ngutech21 |
| 2026-11-11 | [ci: automatically discover standalone web UI tests (#5119)](https://github.com/jundot/omlx/commit/d6e14871551a6165106de31f1fdfb3bddf90342e) | ngutech21 |
| 2026-11-11 | [ci(macos): build and test the app (#5120)](https://github.com/jundot/omlx/commit/4cac9dae65cd17fb16fbdb45a79133cae3df2ede) | ngutech21 |
| 2026-11-11 | [fix(vlm): skip Florence-2 at discovery and accept plain-string prompts (#5142)](https://github.com/jundot/omlx/commit/41f8c839dce9f71238a53ec1312cf1fbf252a0b2) | Woody-Hu |
| 2026-11-11 | [fix(dflash): restore drafter context on exact prefix hits](https://github.com/jundot/omlx/commit/22f2c43409b078b56d6a9903414f4d8a759ad3d3) | jundot |
| 2026-11-11 | [fix(web): pair serving stats and speed cards on phones (#5123)](https://github.com/jundot/omlx/commit/79b936ee5ba6259d3b48f11fe873b18ed8cfec7c) | LXD-8 |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## 👥 Top contributors

[jundot](https://github.com/jundot) (2268) · [cfbraun](https://github.com/cfbraun) (85) · [LXD-8](https://github.com/LXD-8) (62) · [jonathan308](https://github.com/jonathan308) (51) · [github-actions[bot]](https://github.com/github-actions[bot]) (37)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
