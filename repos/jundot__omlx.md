# jundot/omlx

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/jundot/omlx)

> LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Local LLM server for Apple Silicon (batching + SSD cache) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 23.5k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [494](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 3% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 91.6 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 7d ago</sub>

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
<sub>2026-10-24 · 18d ago</sub>

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
| 2026-11-11 | [fix(scheduler): start requests that arrive mid-prefill after the runn…](https://github.com/jundot/omlx/commit/95a33f88c622f3f72f84cb9bd2a5b59e40edafe1) | jundot |
| 2026-11-11 | [fix(prefill-helper): retry an offline helper when a long prompt arriv…](https://github.com/jundot/omlx/commit/6a98f70715ff77b2328592258fdd7f6b24db7655) | jundot |
| 2026-11-11 | [fix: remove three intermittent CI failures on main (#5171)](https://github.com/jundot/omlx/commit/14fab9c049effe6d3556c95753c4608d1f846a3c) | jundot |
| 2026-11-11 | [fix(prefill-helper): retry a helper that does not answer over SSH (#5…](https://github.com/jundot/omlx/commit/6eec8d51fab1664a255aaaaa6f3f998cbf9011e3) | yanzhaohui1999 |
| 2026-11-11 | [feat(macos): simplify the model library list](https://github.com/jundot/omlx/commit/267de8e8d7dd9c84626e457571e8b7e90237b397) | jundot |
| 2026-11-11 | [fix(macos): show model aliases and prefer aliases when copying (#5091)](https://github.com/jundot/omlx/commit/a88306eb92b834c682e30cf2bd02b5155c274cb8) | ngutech21 |
| 2026-11-11 | [fix(qwen4-exp): keep g13/g14 GPUs on the MLX path (#5089)](https://github.com/jundot/omlx/commit/e03190e31af53b3fc9fa4b562f064367b9ec89aa) | begcdn |
| 2026-11-11 | [fix(tool-calling): count a declared tool name as call evidence only i…](https://github.com/jundot/omlx/commit/b3214c0da92f69b633ad141d56e5885be338429b) | Flo5k5 |
| 2026-11-11 | [fix(scheduler): keep the Metal wired limit when a batch generator clo…](https://github.com/jundot/omlx/commit/98fd1b71b5b303e00d46e0f4028a2b8414db8b40) | jundot |
| 2026-11-11 | [fix(stt): reserve realtime sessions before backend startup (#5092)](https://github.com/jundot/omlx/commit/db4b4176985277359f739655a01eae5e3a6fa412) | Aminark |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
