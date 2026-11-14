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
| 🐞 **Open issues + PRs** | [497](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 93.7 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · yesterday</sub>

> **oMLX 0.8.0rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> The release candidate for oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, and makes DeepSeek V4.1 faster with many requests and on clusters.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos15-sequoia.dmg)
> <sub><i>* If you downloaded build 3727 right after release, the Cluster tab may not find a DGX Spark or NVIDIA PC, so please download it again.</i></sub>
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> …

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 10d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

### [v0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3) — 0.7.3
<sub>2026-10-31 · 13d ago</sub>

> **oMLX 0.7.3**
> oMLX 0.7.3 makes DeepSeek V4.1 prefill and batched decode faster, lets Ask AI hold voice conversations, search the web, read links and look at your screen, and cuts memory use when many requests run at long context. The notes below cover changes since 0.7.3rc1, and earlier 0.7.3 highlights are summarized at the end.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos15-sequoia.dmg)
> https://github.com/user-attachments/assets/d63f2dbd-a3a9-47e0-bf1f-1add45c39395
> **Ask AI Voice Mode, Web Search and Screen Capture**
> Talk to your local models. Turn on Voice under App > Ask AI, press Option-Shift-Space and speak, and the answer plays back with captions. Ask AI can also search the web, read links and look at your screen (#4976).
> …

### [v0.7.3rc1](https://github.com/jundot/omlx/releases/tag/v0.7.3rc1) — 0.7.3rc1
<sub>2026-10-27 · 18d ago</sub>

> **oMLX 0.7.3rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> The release candidate for oMLX 0.7.3 adds Ask AI, a question bar for your local models in any app, a GPU power limit for working on battery, and Ling 3.1 Flash with Lightning MTP. It also brings everything from the 0.7.3 development releases: MiniMax M3.1 Flash, faster M1 and M5 Macs, and better low-bit oQ.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos15-sequoia.dmg)
> **Ask AI**
> Ask your local models from any app. Press Option-Space and a question bar floats over whatever you are working on without taking focus, and the answer streams in as Markdown. Slash presets set the model and system prompt per command, so `/translate` can run a small model with a fixed prompt and copy the result for you. Vision models also take images pasted with Command-V. Turn it on in the macOS app under App > Ask AI. #4854
> …

### [v0.7.3.dev2](https://github.com/jundot/omlx/releases/tag/v0.7.3.dev2) — 0.7.3.dev2
<sub>2026-10-25 · 20d ago</sub>

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
| 2026-11-13 | [fix(minimax-m3): probe MSA prefill kernel threadgroup before use (#5239)](https://github.com/jundot/omlx/commit/624cff0e23519ba46a4d5ed2802c2c236ad1a9ac) | begcdn |
| 2026-11-13 | [fix(inkling2): round the expert activation to its input dtype](https://github.com/jundot/omlx/commit/5063be44db095ad362a566b4dd8312a2459bf6c0) | jundot |
| 2026-11-13 | [feat(prefill-helper): Inkling 2 Small on Mac and NVIDIA Prefill Accel…](https://github.com/jundot/omlx/commit/c0814f623f247f91120a7df22b8e6d9dea1d8268) | jundot |
| 2026-11-13 | [feat: add Inkling 2 Small support (#5229)](https://github.com/jundot/omlx/commit/adc3daa6712290316853686ded47e6da109ba6a4) | jundot |
| 2026-11-13 | [fix: keep completed Harmony messages when the last one is malformed (…](https://github.com/jundot/omlx/commit/8b24a5b946deacb6bfec8c207c773d8c2a2750fb) | jundot |
| 2026-11-13 | [perf(qwen4_exp): advise a decode token's SSD table pages before copyi…](https://github.com/jundot/omlx/commit/605e864f278e16db04d5909a361741da809f91f7) | yohann-bearzi |
| 2026-11-13 | [fix: run profile reference repair on older settings files (#5216)](https://github.com/jundot/omlx/commit/90ba3b9d9fe6767bfec1853afb0a0c096aca700b) | jundot |
| 2026-11-13 | [fix(admin): show recent decode speed per request, not the lifetime av…](https://github.com/jundot/omlx/commit/b0758fba02cea57e82e87525b7d8fdcaadd2bdfd) | jundot |
| 2026-11-12 | [test(brew): expect the cluster extra in the Homebrew install spec](https://github.com/jundot/omlx/commit/c74f1b18558842e6b10fcfa6e2e901bb382129d4) | jundot |
| 2026-11-12 | [fix(brew): install the cluster extra so the Cluster tab finds NVIDIA …](https://github.com/jundot/omlx/commit/f265b65e59ed701f70b9c14f79b3c8dc54976082) | jundot |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
