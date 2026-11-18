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
| 🐞 **Open issues + PRs** | [515](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 96.9 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · today</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 5d ago</sub>

> **oMLX 0.8.0rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> The release candidate for oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, and makes DeepSeek V4.1 faster with many requests and on clusters.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos15-sequoia.dmg)
> <sub><i>* If you downloaded build 3727 right after release, the Cluster tab may not find a DGX Spark or NVIDIA PC, so please download it again.</i></sub>
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> …

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 14d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

### [v0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3) — 0.7.3
<sub>2026-10-31 · 17d ago</sub>

> **oMLX 0.7.3**
> oMLX 0.7.3 makes DeepSeek V4.1 prefill and batched decode faster, lets Ask AI hold voice conversations, search the web, read links and look at your screen, and cuts memory use when many requests run at long context. The notes below cover changes since 0.7.3rc1, and earlier 0.7.3 highlights are summarized at the end.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3/oMLX-0.7.3-macos15-sequoia.dmg)
> https://github.com/user-attachments/assets/d63f2dbd-a3a9-47e0-bf1f-1add45c39395
> **Ask AI Voice Mode, Web Search and Screen Capture**
> Talk to your local models. Turn on Voice under App > Ask AI, press Option-Shift-Space and speak, and the answer plays back with captions. Ask AI can also search the web, read links and look at your screen (#4976).
> …

### [v0.7.3rc1](https://github.com/jundot/omlx/releases/tag/v0.7.3rc1) — 0.7.3rc1
<sub>2026-10-27 · 22d ago</sub>

> **oMLX 0.7.3rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.2](https://github.com/jundot/omlx/releases/tag/v0.7.2).
> The release candidate for oMLX 0.7.3 adds Ask AI, a question bar for your local models in any app, a GPU power limit for working on battery, and Ling 3.1 Flash with Lightning MTP. It also brings everything from the 0.7.3 development releases: MiniMax M3.1 Flash, faster M1 and M5 Macs, and better low-bit oQ.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.3rc1/oMLX-0.7.3rc1-macos15-sequoia.dmg)
> **Ask AI**
> Ask your local models from any app. Press Option-Space and a question bar floats over whatever you are working on without taking focus, and the answer streams in as Markdown. Slash presets set the model and system prompt per command, so `/translate` can run a small model with a fixed prompt and copy the result for you. Vision models also take images pasted with Command-V. Turn it on in the macOS app under App > Ask AI. #4854
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [formula: bump to 0.8.0](https://github.com/jundot/omlx/commit/b1bb94a6d53fdb2a48b6fb5afc0e8d5e33f76913) | github-actions[bot] |
| 2026-11-18 | [chore: bump version to 0.8.0](https://github.com/jundot/omlx/commit/7fad36ca030fa6500a660f3d6f4323b2cd3b0073) | jundot |
| 2026-11-18 | [test(oq): skip oQh kernel cases without the extension and pass hadama…](https://github.com/jundot/omlx/commit/bafa6403ab1a9f889e2325d1b55944456d857345) | jundot |
| 2026-11-18 | [fix(cuda-helper): read DeepSeek V4.1 oQh experts](https://github.com/jundot/omlx/commit/8e4ed6c66fc39460db706f698349db693d312156) | jundot |
| 2026-11-18 | [feat(prefill): run oQh models on the Prefill Accelerator (#5391)](https://github.com/jundot/omlx/commit/c77138a138beae6a4cf87957c1c1cefb6454a15c) | jundot |
| 2026-11-18 | [feat(oq): add oQh for more accurate low-bit quants at the same size (…](https://github.com/jundot/omlx/commit/a57ed319047aefa92ea22958377bbdc1003302a3) | jundot |
| 2026-11-18 | [feat(oq): refine oQe rounding with layer input correlations (#5292)](https://github.com/jundot/omlx/commit/6bc44d816d750b6f8339623bc74d79cd4fc8f6c9) | jundot |
| 2026-11-18 | [fix(moe): release only the offload slots a prefill needs (#4842)](https://github.com/jundot/omlx/commit/bb5ae7d66193be775ebc2140ffb3e4ce1f26ba77) | JarJarFran |
| 2026-11-18 | [perf(deepseek_v41): wait on the previous layer during wide prefill (#…](https://github.com/jundot/omlx/commit/ae12f01ea52ba09517deb0840ab89998729e8cad) | junmo-kim |
| 2026-11-18 | [fix(mac): the hidden menu bar icon alert names the camera notch inste…](https://github.com/jundot/omlx/commit/322840c5dedd722ebdee7fd8cb0f6990bb345356) | fabriziosalmi |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
