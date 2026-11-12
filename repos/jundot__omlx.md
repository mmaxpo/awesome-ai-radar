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
| ⭐ **Stars** | 23.6k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [484](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 3% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 91.7 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 8d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

### [v0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3) — 0.7.3
<sub>2026-10-31 · 11d ago</sub>

> **oMLX 0.7.3**
> oMLX 0.7.3 makes DeepSeek V4.1 prefill and batched decode faster, lets Ask AI hold voice conversations, search the web, read links and look at your screen, and cuts memory use when many requests run at long context. The notes below cover changes since 0.7.3rc1, and earlier 0.7.3 highlights are summarized at the end.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos15-sequoia.dmg)
> https://github.com/user-attachments/assets/d63f2dbd-a3a9-47e0-bf1f-1add45c39395
> **Ask AI Voice Mode, Web Search and Screen Capture**
> Talk to your local models. Turn on Voice under App > Ask AI, press Option-Shift-Space and speak, and the answer plays back with captions. Ask AI can also search the web, read links and look at your screen (#4976).
> …

### [v0.7.3rc1](https://github.com/jundot/omlx/releases/tag/v0.7.3rc1) — 0.7.3rc1
<sub>2026-10-27 · 16d ago</sub>

> **oMLX 0.7.3rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> The release candidate for oMLX 0.7.3 adds Ask AI, a question bar for your local models in any app, a GPU power limit for working on battery, and Ling 3.1 Flash with Lightning MTP. It also brings everything from the 0.7.3 development releases: MiniMax M3.1 Flash, faster M1 and M5 Macs, and better low-bit oQ.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos15-sequoia.dmg)
> **Ask AI**
> Ask your local models from any app. Press Option-Space and a question bar floats over whatever you are working on without taking focus, and the answer streams in as Markdown. Slash presets set the model and system prompt per command, so `/translate` can run a small model with a fixed prompt and copy the result for you. Vision models also take images pasted with Command-V. Turn it on in the macOS app under App > Ask AI. #4854
> …

### [v0.7.3.dev2](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev2) — 0.7.3.dev2
<sub>2026-10-25 · 18d ago</sub>

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
| 2026-11-12 | [perf(cuda-helper): DeepSeek V4.1 expert, attention and window cache k…](https://github.com/jundot/omlx/commit/7ab44f30db6ad9a6067928cbec889e3171499a39) | jundot |
| 2026-11-12 | [test(scheduler): isolate sdpa256 globals in prefill memory guard (#5176)](https://github.com/jundot/omlx/commit/1c94c39d5fac6b4eb0eb1f2c924a62bf858d69ca) | yanzhaohui1999 |
| 2026-11-12 | [test: stop mock cache dirs polluting the repo root (#5183)](https://github.com/jundot/omlx/commit/7e8d877065228e4aa9d600bc9bc7192a93a67b68) | shaanchander |
| 2026-11-12 | [feat(eval): let local accuracy runs raise the per-question token limi…](https://github.com/jundot/omlx/commit/fa7b45424ba675eb0c0bdf8204861bbcbd133be1) | jundot |
| 2026-11-12 | [fix(codex): skip the reverse DNS lookup in the instructions probe server](https://github.com/jundot/omlx/commit/9715639e7fceac67d53dedfac4f6a654d7297eb6) | jundot |
| 2026-11-12 | [build: use PEP 735 group for dev dependencies (#5188)](https://github.com/jundot/omlx/commit/e11bffccf78218cb28a497d69c89f7eab5be3604) | ngutech21 |
| 2026-11-12 | [fix(oq): find Spark-X (spark2_5) token embedding for oQe imatrix (#5184)](https://github.com/jundot/omlx/commit/e980721018dc4d77d68051f9bec2eefd5f9a062d) | Woody-Hu |
| 2026-11-12 | [fix(turboquant): keep the verify seam order independent of model load…](https://github.com/jundot/omlx/commit/54f67977207ad4021eb25dd87cced9f111594f29) | jundot |
| 2026-11-12 | [perf(qwen3_5): serve long left-padded batches per row with batch-1 at…](https://github.com/jundot/omlx/commit/4df1ca122f375719a0a228dde29684c11cd201c8) | StefVanG |
| 2026-11-12 | [test: trim the GPU-heavy cases that slowed CI again (#5185)](https://github.com/jundot/omlx/commit/0b7eccb4f28dee8ed3155a585fda065b9d219341) | jundot |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
