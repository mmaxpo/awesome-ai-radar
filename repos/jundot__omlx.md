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
| ⭐ **Stars** | 24.0k |
| 🍴 **Forks** | 2.2k |
| 🐞 **Open issues + PRs** | [419](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 82% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.4](https://github.com/jundot/omlx/releases/tag/v0.8.4) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 101.1 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.4](https://github.com/jundot/omlx/releases/tag/v0.8.4) — 0.8.4
<sub>2026-11-26 · yesterday</sub>

> **oMLX 0.8.4**
> oMLX 0.8.4 makes Inkling 2 Mini much faster, adds LoopCD decoding for it, and speeds up DeepSeek V4.1 when several requests run at once. Inkling 2 Mini prefills 51-124% faster than in 0.8.3, decodes twice as fast at 128K, and now runs Lightning MTP for concurrent requests.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.4/oMLX-0.8.4-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.4/oMLX-0.8.4-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="omlx_084_p1" src="https://github.com/user-attachments/assets/215da783-8bbf-4465-a82b-39b3aeefe103" />
> **Faster Inkling 2 Mini**
> Inkling 2 Mini prefills 51-124% faster than in 0.8.3, decodes 42% faster on a short prompt and twice as fast at 128K. Lightning MTP now also runs when two or more requests decode together, so two requests at once get 2.6x the total speed (#5674). Most of the gain comes from new fused Metal kernels for attention, experts and the loop layers, and M1 and M2 Macs with Float16 Activations get faster expert kernels too.
> …

### [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 0.8.3
<sub>2026-11-22 · 4d ago</sub>

> **oMLX 0.8.3**
> oMLX 0.8.3 is an optimization release for Inkling 2 Mini and the Hy4 family, which got day-0 support in 0.8.1. Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster, Hy4 Flash starts answering sooner and needs less memory, and Claude Code's web search now works with local models.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos15-sequoia.dmg)
> **Faster Inkling 2 Mini**
> Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster than in 0.8.2 (#5538). Rewriting a file or other text from the context is more than twice as fast, as Lightning MTP can now copy up to 15 tokens at a time from it (#5528). A long context also needs about a sixth of the KV memory, 18 -> 3 GB at 98K tokens (-83%) (@masterfasa in #5505).
> > Inkling-2-Mini-oQ4e-mtp, Lightning MTP on, temperature 1.0, on M5 Max. The file rewrite row is on M3 Ultra and compares before and after #5528.
> …

### [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 0.8.2
<sub>2026-11-21 · 6d ago</sub>

> > **Hotfix release:** Fixes wrong click positions on screenshots with Qwen3.8 Flash-Next (#5474). Everything else is the same as 0.8.1.
> **oMLX 0.8.2**
> oMLX 0.8.2 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> …

### [v0.8.1](https://github.com/jundot/omlx/releases/tag/v0.8.1) — 0.8.1
<sub>2026-11-21 · 6d ago</sub>

> **oMLX 0.8.1**
> oMLX 0.8.1 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> > M3 Ultra 512GB, 32K prompt, Lightning MTP on. MTP decode moves with draft acceptance, so single runs can differ.
> …

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · 9d ago</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [formula: bump to 0.8.4](https://github.com/jundot/omlx/commit/633d6cf62971262149c2b2477361487958da3915) | github-actions[bot] |
| 2026-11-26 | [chore(cuda-helper): bump the helper to 0.1.9](https://github.com/jundot/omlx/commit/bc55984ab090682c2ea90876f5e64afe5cfd67a4) | jundot |
| 2026-11-26 | [chore: bump version to 0.8.4](https://github.com/jundot/omlx/commit/7a0d136b39d6fb7e8ff9848884ec84cc955b7834) | jundot |
| 2026-11-26 | [fix(inkling2): skip the rel load for the unused row of odd verify blocks](https://github.com/jundot/omlx/commit/0babc47b99feb86a1c4dc0f2ea26158581babdd3) | jundot |
| 2026-11-26 | [fix(inkling2): keep model_loading importable on inference workers](https://github.com/jundot/omlx/commit/dbc6a1d7f17eca8996476f7b9149598a4ac60b1f) | jundot |
| 2026-11-26 | [perf(inkling2): run Lightning MTP for concurrent requests (#5674)](https://github.com/jundot/omlx/commit/8ffa007d3c03e30372921174a144f4cd9447f093) | jundot |
| 2026-11-26 | [fix(inkling2): keep verify attention within M1/M2 threadgroup limits](https://github.com/jundot/omlx/commit/aa51fcaf2ef41ab97a8529bf3ef873b3b15ff8be) | jundot |
| 2026-11-26 | [feat(moe): allow expert offload for Ling checkpoints (#5634)](https://github.com/jundot/omlx/commit/359473412f41b0b42430453baa23b3f9ad40a66a) | hermitdave |
| 2026-11-26 | [fix(inkling2): fit long-context verify rows in one threadgroup on Ink…](https://github.com/jundot/omlx/commit/896806de9f5d6c256a71828dcb05abeb015fe291) | jundot |
| 2026-11-26 | [perf(cluster): prefill DeepSeek V4.1 prompts together on tensor-paral…](https://github.com/jundot/omlx/commit/768095a3a8d0d648329ea271fbab771c22e1963b) | jundot |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
