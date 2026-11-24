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
| 🐞 **Open issues + PRs** | [432](https://github.com/jundot/omlx/issues) |
| 💻 **Languages** | Python 81% · Swift 8% · HTML 5% · JavaScript 2% · C++ 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `apple-silicon` `inference-server` `llm` `macos` `mlx` `openai-api` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-02-13 |
| 📦 **Latest release** | [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 100.5 MB |
| 🌐 **Website** | https://omlx.ai |

## 📦 Recent releases

### [v0.8.3](https://github.com/jundot/omlx/releases/tag/v0.8.3) — 0.8.3
<sub>2026-11-22 · yesterday</sub>

> **oMLX 0.8.3**
> oMLX 0.8.3 is an optimization release for Inkling 2 Mini and the Hy4 family, which got day-0 support in 0.8.1. Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster, Hy4 Flash starts answering sooner and needs less memory, and Claude Code's web search now works with local models.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.3/oMLX-0.8.3-macos15-sequoia.dmg)
> **Faster Inkling 2 Mini**
> Inkling 2 Mini prefills about 20% faster and decodes 10-13% faster than in 0.8.2 (#5538). Rewriting a file or other text from the context is more than twice as fast, as Lightning MTP can now copy up to 15 tokens at a time from it (#5528). A long context also needs about a sixth of the KV memory, 18 -> 3 GB at 98K tokens (-83%) (@masterfasa in #5505).
> > Inkling-2-Mini-oQ4e-mtp, Lightning MTP on, temperature 1.0, on M5 Max. The file rewrite row is on M3 Ultra and compares before and after #5528.
> …

### [v0.8.2](https://github.com/jundot/omlx/releases/tag/v0.8.2) — 0.8.2
<sub>2026-11-21 · 3d ago</sub>

> > **Hotfix release:** Fixes wrong click positions on screenshots with Qwen3.8 Flash-Next (#5474). Everything else is the same as 0.8.1.
> **oMLX 0.8.2**
> oMLX 0.8.2 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.2/oMLX-0.8.2-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> …

### [v0.8.1](https://github.com/jundot/omlx/releases/tag/v0.8.1) — 0.8.1
<sub>2026-11-21 · 3d ago</sub>

> **oMLX 0.8.1**
> oMLX 0.8.1 adds Hy4, Hy4-flash and Inkling 2 Mini, lets you apply a LoRA adapter from a model's settings, and makes MTP verify on M5, GLM-5.3 with several requests and new questions on a cached document faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.1/oMLX-0.8.1-macos15-sequoia.dmg)
> **New Models: Hy4, Hy4-flash and Inkling 2 Mini**
> Tencent's Hy4 and Hy4-flash run with image input, Lightning MTP and oQ/oQh, and their FP8 releases load as is (#5463). Lightning MTP takes Hy4-flash FP8 from 23.1 to 37.7 tok/s at 32K (+63%). Ready-made oQ4h builds are [Jundot/Hy4-flash-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-flash-oQ4h-mtp) (132 GB) and [Jundot/Hy4-oQ4h-mtp](https://huggingface.co/Jundot/Hy4-oQ4h-mtp) (452 GB).
> > M3 Ultra 512GB, 32K prompt, Lightning MTP on. MTP decode moves with draft acceptance, so single runs can differ.
> …

### [v0.8.0](https://github.com/jundot/omlx/releases/tag/v0.8.0) — 0.8.0
<sub>2026-11-18 · 6d ago</sub>

> **oMLX 0.8.0**
> oMLX 0.8.0 adds the Prefill Accelerator, which lets a PC with NVIDIA GPUs or a second Mac speed up prefill for a big model on your Mac, adds oQh for more accurate low-bit quants at the same size, and makes DeepSeek V4.1, Qwen and long-context decode faster.
> **Download:** [macOS 26 / 27](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos26-27.dmg) | [macOS 15 Sequoia](https://github.com/jundot/omlx/releases/download/v0.8.0/oMLX-0.8.0-macos15-sequoia.dmg)
> <img width="2400" height="1350" alt="image-1794476752259" src="https://github.com/user-attachments/assets/dfa46522-dd0d-425d-8a16-ca2b3eac042c" />
> **Prefill Accelerator with NVIDIA GPUs or a Mac**
> A PC with NVIDIA GPUs, a DGX Spark or a second Mac with a faster GPU runs the first layers of each prompt chunk, while your Mac runs the rest, decodes and keeps the KV cache. Auto picks how many layers the helper takes from the measured speed of both machines and the link, and keeps the prompt on the Mac when a split would be slower (#5065, #5163, #5195). oQh models and Inkling 2 Small run on both kinds of helper (#5391, #5234).
> …

### [v0.8.0rc1](https://github.com/jundot/omlx/releases/tag/v0.8.0rc1) — 0.8.0rc1
<sub>2026-11-12 · 11d ago</sub>

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
| 2026-11-24 | [build(vlm): update mlx-vlm to 0.8.1 and adapt the patches around it (…](https://github.com/jundot/omlx/commit/eff5de556c4cd11eeb5ce72241b97b7ad76e0c02) | jundot |
| 2026-11-24 | [fix(cuda-helper): admit 2, 3 and 5-bit affine expert banks (#5551) (#…](https://github.com/jundot/omlx/commit/be6129bfd08512c503c20b64df8c2cda49b32529) | begcdn |
| 2026-11-24 | [fix(ssd-cache): keep superseded writes from replacing newer blocks (#…](https://github.com/jundot/omlx/commit/10143699490a5d2e4198bb577535d9fa610dfcb8) | Atishay8192261 |
| 2026-11-24 | [fix(ssd-cache): mark an inline write-through entry clean (#5544)](https://github.com/jundot/omlx/commit/ac0fff3c967e0c29789e89536f3669f5b9c389ce) | frarredondo |
| 2026-11-24 | [perf(deepseek_v41): batch the indexer across a decode batch (#5549)](https://github.com/jundot/omlx/commit/2cc87960cdb3a1f9bb48b0f0d6f5f5ace512c71a) | bleugreen |
| 2026-11-24 | [fix(prefill-helper): log long prompts that run before the helper is r…](https://github.com/jundot/omlx/commit/8515583fe5ba4be6af435fb75bd633e9da212af5) | GumbiiDigital |
| 2026-11-24 | [feat(splash): honor max_context_window above the native window (#5578)](https://github.com/jundot/omlx/commit/9e102fa382ca7a458ef8bb46ec78b68c77b5706a) | pedily |
| 2026-11-24 | [fix(server): stop waiting for in-flight requests after 5 s at shutdow…](https://github.com/jundot/omlx/commit/7b89016ff0d08979882545fb5b6f2eaa57695d76) | lmdc45 |
| 2026-11-24 | [fix(cache): keep hot cache touches constant time on long chains (#5255)](https://github.com/jundot/omlx/commit/897a0562d3e0f66fde822aaa10db06fe2c801ab5) | jundot |
| 2026-11-24 | [feat: add opt-in macos-say TTS model (#5076)](https://github.com/jundot/omlx/commit/2bb2332d5841a763e4855d4ca22d6abcb58c5f2e) | zviratko |

[See all commits ↗](https://github.com/jundot/omlx/commits)

## ⬇️ Get it

```bash
git clone https://github.com/jundot/omlx.git
```
