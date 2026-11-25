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
| 🐞 **Open issues + PRs** | [417](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 101.7 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 0.8.3
<sub>2026-11-22 · 2d ago</sub>

> **oMLX 0.8.3**
> oMLX 0.8.3 is an optimization release for Inkling 2 Mini and the Hy4 family, which got day-0 support in 0.8.1. Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster, Hy4 Flash starts answering sooner and needs less memory, and Claude Code's web search now works with local models.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos15-sequoia.dmg)
> **Faster Inkling 2 Mini**
> Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster than in 0.8.2 (#5538). Rewriting a file or other text from the context is more than twice as fast, as Lightning MTP can now copy up to 15 tokens at a time from it (#5528). A long context also needs about a sixth of the KV memory, 18 -> 3 GB at 98K tokens (-83%) (@masterfasa in #5505).
> > Inkling-2-Mini-oQ4e-mtp, Lightning MTP on, temperature 1.0, on M5 Max. The file rewrite row is on M3 Ultra and compares before and after #5528.
> …

### [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 0.8.2
<sub>2026-11-21 · 4d ago</sub>

> > **Hotfix release:** Fixes wrong click positions on screenshots with Qwen3.8 Flash-Next (#5474). Everything else is the same as 0.8.1.
> **oMLX 0.8.2**
> oMLX 0.8.2 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> …

### [v0.8.1](https://github.com/jundot/omlx/releases/tag/v0.8.1) — 0.8.1
<sub>2026-11-21 · 4d ago</sub>

> **oMLX 0.8.1**
> oMLX 0.8.1 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> > M3 Ultra 512GB, 32K prompt, Lightning MTP on. MTP decode moves with draft acceptance, so single runs can differ.
> …

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · 7d ago</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 12d ago</sub>

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
| 2026-11-25 | [test(oq): build the mlx-vlm Inkling 2 reference in a separate process](https://github.com/jundot/omlx/commit/a49ca949a2b49f4815d402788485428b020a61df) | jundot |
| 2026-11-25 | [test: trim redundant cases and slow setup to cut CI time](https://github.com/jundot/omlx/commit/9ff073ce2cd1835ccf52e6c1425306697c68c5df) | jundot |
| 2026-11-25 | [feat(inkling2): load Inkling 2 checkpoints converted by mlx-lm (#5648)](https://github.com/jundot/omlx/commit/ba925ba936e581a28437267f03be3c903bfddc7c) | jundot |
| 2026-11-25 | [feat(api): add GET /v1/models/{model_id} (#5201)](https://github.com/jundot/omlx/commit/d3d229793beac98a6ac3b583bc98cb6ea4f20149) | LXD-8 |
| 2026-11-25 | [fix(server): report late errors in the JSON keepalive body (#5310)](https://github.com/jundot/omlx/commit/90af4b8297eb09b6b8dae32d462b57431e595689) | Woody-Hu |
| 2026-11-25 | [fix(admin): stop returning the master API key on polled GETs (#5496)](https://github.com/jundot/omlx/commit/b1fbfff3325cd5f9b9c061c5cec2b241de470ada) | aywengo |
| 2026-11-25 | [fix(cache): fall back to the shared system-prefix tail when a split-G…](https://github.com/jundot/omlx/commit/3127b370165d76940ded40208b757828c07d4c36) | StefVanG |
| 2026-11-25 | [fix(cache): reject and evict non-finite vision features (#5597)](https://github.com/jundot/omlx/commit/b5d3eab94cbaff7cdb42af8f033887d98cdc9370) | begcdn |
| 2026-11-25 | [feat(splash): serve Inkling-2-Mini images on Splash 1.7.3 (#5647)](https://github.com/jundot/omlx/commit/418aab32bfe2530e5eb3b217d5780402e1a2a653) | jundot |
| 2026-11-25 | [fix(vlm): honor Trust Remote Code for checkpoint model files (#5645)](https://github.com/jundot/omlx/commit/431d9d61c3bd7afbbf6ce946969c81cab1689162) | jundot |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
