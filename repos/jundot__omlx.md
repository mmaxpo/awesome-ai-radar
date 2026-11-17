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
| ⭐ **Stars** | 23.7k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [510](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 96.0 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 4d ago</sub>

> **oMLX 0.8.0rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> The release candidate for oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, and makes DeepSeek V4.1 faster with many requests and on clusters.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos15-sequoia.dmg)
> <sub><i>* If you downloaded build 3727 right after release, the Cluster tab may not find a DGX Spark or NVIDIA PC, so please download it again.</i></sub>
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> …

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 13d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

### [v0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3) — 0.7.3
<sub>2026-10-31 · 16d ago</sub>

> **oMLX 0.7.3**
> oMLX 0.7.3 makes DeepSeek V4.1 prefill and batched decode faster, lets Ask AI hold voice conversations, search the web, read links and look at your screen, and cuts memory use when many requests run at long context. The notes below cover changes since 0.7.3rc1, and earlier 0.7.3 highlights are summarized at the end.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos15-sequoia.dmg)
> https://github.com/user-attachments/assets/d63f2dbd-a3a9-47e0-bf1f-1add45c39395
> **Ask AI Voice Mode, Web Search and Screen Capture**
> Talk to your local models. Turn on Voice under App > Ask AI, press Option-Shift-Space and speak, and the answer plays back with captions. Ask AI can also search the web, read links and look at your screen (#4976).
> …

### [v0.7.3rc1](https://github.com/jundot/omlx/releases/tag/v0.7.3rc1) — 0.7.3rc1
<sub>2026-10-27 · 21d ago</sub>

> **oMLX 0.7.3rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> The release candidate for oMLX 0.7.3 adds Ask AI, a question bar for your local models in any app, a GPU power limit for working on battery, and Ling 3.1 Flash with Lightning MTP. It also brings everything from the 0.7.3 development releases: MiniMax M3.1 Flash, faster M1 and M5 Macs, and better low-bit oQ.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos15-sequoia.dmg)
> **Ask AI**
> Ask your local models from any app. Press Option-Space and a question bar floats over whatever you are working on without taking focus, and the answer streams in as Markdown. Slash presets set the model and system prompt per command, so `/translate` can run a small model with a fixed prompt and copy the result for you. Vision models also take images pasted with Command-V. Turn it on in the macOS app under App > Ask AI. #4854
> …

### [v0.7.3.dev2](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev2) — 0.7.3.dev2
<sub>2026-10-25 · 23d ago</sub>

> **oMLX 0.7.3.dev2**
> > This is a hotfix release that fixes an error when turning on Lightning MTP for MiniMax M3.1 (#4827). It also removes the stray `</think>` at the start of MiniMax M3.1 non-streaming replies and fixes prefill for DeepSeek V4 Flash oQ3.5e.
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> oMLX 0.7.3.dev2 adds MiniMax M3.1 Flash with Lightning MTP, makes M1 and M5 Macs, DFlash on fp16 models and GLM-5.3 faster, and gives low-bit oQ quants a better split of their bits.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3.dev2/oMLX-0.7.3.dev2-macos15-sequoia.dmg)
> **MiniMax M3.1 Flash**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [perf(moe): run Qwen MoE verify and multi-request decode on the fused …](https://github.com/jundot/omlx/commit/5382e7480e6158573593044734e52bda0c459637) | jundot |
| 2026-11-17 | [fix(qwen35): keep gs64 prefill projections on stock MLX without NAX q…](https://github.com/jundot/omlx/commit/f6782ad79dc384576412db2d067acb6e9d2df12a) | jundot |
| 2026-11-17 | [feat(oq): stream oQe calibration for Qwen3.5 and Qwen3.5-MoE (#5332)](https://github.com/jundot/omlx/commit/eec2544c62c6bcdd2b3d3ff33d5fed2535d2c83f) | keefar |
| 2026-11-17 | [fix: show the actual upload skip reason in bench banners](https://github.com/jundot/omlx/commit/ed045bbc0ab42a2e450bf49fcfb6454acd948259) | jundot |
| 2026-11-17 | [feat(benchmark): skip leaderboard upload for non-default generation l…](https://github.com/jundot/omlx/commit/93044574086342a669fdb27d7ec1e704ef9a9753) | OmVidana |
| 2026-11-17 | [fix: detect the thinking default by rendering the chat template](https://github.com/jundot/omlx/commit/44b0525533564702b56dc8620510207408d4ebf1) | jundot |
| 2026-11-17 | [fix(distributed): recover a reply that arrives only as reasoning (#5328)](https://github.com/jundot/omlx/commit/48f7ead559c0188c7b96d5a27028946ed2646a24) | joshuaswarren |
| 2026-11-17 | [fix(discovery): tolerate an undecodable byte in a Hugging Face refs f…](https://github.com/jundot/omlx/commit/a0e8ce180d7f02150c2ec03ecaffc9509eebd063) | joshuaswarren |
| 2026-11-17 | [feat(splash): expose --activations and default attention to bf16 on M…](https://github.com/jundot/omlx/commit/c8213a1dbdd4790a4ec2e47d411b115f84929c01) | Woody-Hu |
| 2026-11-17 | [test(qwen35): prevent Qwen4 import-order failures (#5277)](https://github.com/jundot/omlx/commit/1c4afcac9c62c2de0057576f8f563e2749a07236) | contrapuntal |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
