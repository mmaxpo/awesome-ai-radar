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
| ⭐ **Stars** | 23.9k |
| 🍴 **Forks** | 2.2k |
| 🐞 **Open issues + PRs** | [427](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 100.1 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 0.8.3
<sub>2026-11-22 · today</sub>

> **oMLX 0.8.3**
> oMLX 0.8.3 is an optimization release for Inkling 2 Mini and the Hy4 family, which got day-0 support in 0.8.1. Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster, Hy4 Flash starts answering sooner and needs less memory, and Claude Code's web search now works with local models.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos15-sequoia.dmg)
> **Faster Inkling 2 Mini**
> Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster than in 0.8.2 (#5538). Rewriting a file or other text from the context is more than twice as fast, as Lightning MTP can now copy up to 15 tokens at a time from it (#5528). A long context also needs about a sixth of the KV memory, 18 -> 3 GB at 98K tokens (-83%) (@masterfasa in #5505).
> > Inkling-2-Mini-oQ4e-mtp, Lightning MTP on, temperature 1.0, on M5 Max. The file rewrite row is on M3 Ultra and compares before and after #5528.
> …

### [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 0.8.2
<sub>2026-11-21 · 2d ago</sub>

> > **Hotfix release:** Fixes wrong click positions on screenshots with Qwen3.8 Flash-Next (#5474). Everything else is the same as 0.8.1.
> **oMLX 0.8.2**
> oMLX 0.8.2 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> …

### [v0.8.1](https://github.com/jundot/omlx/releases/tag/v0.8.1) — 0.8.1
<sub>2026-11-21 · 2d ago</sub>

> **oMLX 0.8.1**
> oMLX 0.8.1 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> > M3 Ultra 512GB, 32K prompt, Lightning MTP on. MTP decode moves with draft acceptance, so single runs can differ.
> …

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · 5d ago</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 10d ago</sub>

> **oMLX 0.8.0rc1**
> > This is a release candidate. Please report any bugs through [GitHub Issues](https://github.com/jundot/omlx/issues/new/choose). If you need a stable release, please use [oMLX 0.7.3](https://github.com/jundot/omlx/releases/tag/v0.7.3).
> The release candidate for oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, and makes DeepSeek V4.1 faster with many requests and on clusters.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0rc1/oMLX-0.8.0rc1-macos15-sequoia.dmg)
> <sub><i>* If you downloaded build 3727 right after release, the Cluster tab may not find a DGX Spark or NVIDIA PC, so please download it again.</i></sub>
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(ssd-cache): share one size limit across models (#5497) (#5554)](https://github.com/jundot/omlx/commit/04e6e8e0162617bb48218a8e69740d96b428d767) | yxshee |
| 2026-11-23 | [fix(inkling2): fall back when a fused kernel's threadgroup exceeds th…](https://github.com/jundot/omlx/commit/9c27f986adb4a5771ad4fc71ebdb9920a0e37268) | j3k0 |
| 2026-11-23 | [fix(prefill-helper): retry a helper that lost its GPU and say why (#5…](https://github.com/jundot/omlx/commit/dd14a813b5eaa877889439600fea7d02260b1363) | jundot |
| 2026-11-23 | [perf(engine): end decode bursts until a request's first visible text …](https://github.com/jundot/omlx/commit/832eca1f3ecdc580f20fa64e557c96567f14ff8f) | masterfasa |
| 2026-11-23 | [fix(specprefill): share one engine between a model and its SpecPrefil…](https://github.com/jundot/omlx/commit/69abd86fc45948f3b1c4e70648a7359c8f2ca180) | jundot |
| 2026-11-23 | [docs: credit Wikipedia for the calibration text](https://github.com/jundot/omlx/commit/95fbf3541c21b0fbbedecc0dc2e16b96bb487f20) | jundot |
| 2026-11-23 | [fix(oq): replace unsafe rows in the oQe calibration data (#5524)](https://github.com/jundot/omlx/commit/6bfbe19e688060f9ff2552fda420bd6e901218f6) | jundot |
| 2026-11-23 | [perf(inkling2): send a lone left-padded row to the decode kernel](https://github.com/jundot/omlx/commit/a1cb53cb5a712b5e3b9e4dcfd089f11f474c9045) | jundot |
| 2026-11-23 | [perf(inkling2): FlashDecoding kernel for batched decode and verify (#…](https://github.com/jundot/omlx/commit/087b9e2f40e8dbcc96953529641ab414ffe801bf) | masterfasa |
| 2026-11-23 | [perf(inkling2): run row-exact verify attention rows in one launch (#5…](https://github.com/jundot/omlx/commit/bc4a348e45107d48efd2bec850bf84d9347edf47) | fneto1977 |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
