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
| ⭐ **Stars** | 23.8k |
| 🍴 **Forks** | 2.2k |
| 🐞 **Open issues + PRs** | [430](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 98.7 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 0.8.2
<sub>2026-11-21 · yesterday</sub>

> > **Hotfix release:** Fixes wrong click positions on screenshots with Qwen3.8 Flash-Next (#5474). Everything else is the same as 0.8.1.
> **oMLX 0.8.2**
> oMLX 0.8.2 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> …

### [v0.8.1](https://github.com/jundot/omlx/releases/tag/v0.8.1) — 0.8.1
<sub>2026-11-21 · yesterday</sub>

> **oMLX 0.8.1**
> oMLX 0.8.1 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> > M3 Ultra 512GB, 32K prompt, Lightning MTP on. MTP decode moves with draft acceptance, so single runs can differ.
> …

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · 4d ago</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 9d ago</sub>

> **oMLX 0.8.0rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> The release candidate for oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, and makes DeepSeek V4.1 faster with many requests and on clusters.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos15-sequoia.dmg)
> <sub><i>* If you downloaded build 3727 right after release, the Cluster tab may not find a DGX Spark or NVIDIA PC, so please download it again.</i></sub>
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> …

### [v0.7.4.dev1](https://github.com/jundot/omlx/releases/tag/v0.7.4.dev1) — 0.7.4.dev1
<sub>2026-11-04 · 18d ago</sub>

> **oMLX 0.7.4.dev1**
> > This is a development release. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> oMLX 0.7.4.dev1 lets a second Mac with a fast GPU speed up prefill for a model that only fits on your big Mac, and makes DeepSeek V4.1 and Qwen3.8 Flash-Next faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.7.4.dev1/oMLX-0.7.4.dev1-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="prefill-accelerator" src="https://github.com/user-attachments/assets/d17d27fd-f21b-4723-9b14-0eb96fe6555b" />
> **Prefill Accelerator**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [perf(inkling2): run the flash banded attention kernel on FP16 prefill…](https://github.com/jundot/omlx/commit/8d2c9c6251241f8f752202b17bcfc44cb27ad220) | j3k0 |
| 2026-11-22 | [perf(inkling2): draft from context copies, 15 tokens on verbatim runs…](https://github.com/jundot/omlx/commit/f99a31f4c4826f9185e0b0b8be11eae28b8ec8e2) | jundot |
| 2026-11-22 | [perf(inkling2): bound sliding-window KV cache to reachable tokens and…](https://github.com/jundot/omlx/commit/7ecc946d03b53abc01a92585903fd68e090c9d3b) | masterfasa |
| 2026-11-22 | [fix(inkling2): honor enable_thinking=false and reasoning_effort=off (…](https://github.com/jundot/omlx/commit/a0ed2f5958ad9e62bcb7e84c01ea4438cc8d8554) | masterfasa |
| 2026-11-22 | [fix(inkling2): make Lightning MTP verify rows match serial decode (#5…](https://github.com/jundot/omlx/commit/16b3f79d7d30932f1ebc3c640de4ba27344764a7) | jundot |
| 2026-11-22 | [fix(inkling2): keep NVFP4 expert outputs in range with float16 activa…](https://github.com/jundot/omlx/commit/5c30bc151368258f1a91922f466705b3ff78284e) | CharlesJS |
| 2026-11-22 | [perf(inkling2): project only used in_proj slices on looped sliding vi…](https://github.com/jundot/omlx/commit/b0286dcc987685cbceaba8519d47604a126a8006) | BUKOWSKIREAL |
| 2026-11-22 | [fix(dflash): start pre-drafted recurrent Markov head from the newest …](https://github.com/jundot/omlx/commit/fb25b4ced9bd084f58df5d6ff6b45b8bf45adb68) | masterfasa |
| 2026-11-22 | [test: restore the TurboQuant verify flag after the padded-row tests (…](https://github.com/jundot/omlx/commit/c55dc81631ab20009ac12dc631ad1936051e8826) | jundot |
| 2026-11-21 | [formula: bump to 0.8.2](https://github.com/jundot/omlx/commit/ade9f20a43a8aa8d9191f6c6f130a98154306405) | github-actions[bot] |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
