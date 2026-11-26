# ggml-org/llama.cpp

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ggml-org/llama.cpp)

> LLM inference in C/C++

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | The core C/C++ engine for running LLMs locally |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 136.3k |
| 🍴 **Forks** | 26.1k |
| 🐞 **Open issues + PRs** | [2.7k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 55% · C 18% · Python 8% · TypeScript 6% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [v1.1.0](https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0) — 2026-11-26 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 507.6 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12777](https://github.com/ggml-org/llama.cpp/releases/tag/b12777) _(pre-release)_
<sub>2026-11-26 · today</sub>

> <details open>
> CUDA: loop over ne2/ne3 in non-contiguous concat (#33006)
> The non-contiguous concat kernel mapped dst ne[2] and ne[3] directly to
> gridDim.y and gridDim.z, which are limited to 65535. Larger tensors made
> the launch fail with "invalid configuration argument". Cap the grid and
> loop over the remaining rows in the kernel.
> …

### [b12776](https://github.com/ggml-org/llama.cpp/releases/tag/b12776) _(pre-release)_
<sub>2026-11-26 · today</sub>

> <details open>
> CUDA: fix ROCm CI, do not pick the tile FA kernel for DKQ 576 with a GQA ratio not divisible by 4 (#33045)
> * CUDA: flash attention tile kernel for DKQ 576 with a GQA ratio of 2
> The tile kernel for 576/512 only had variants for GQA ratios that are
> multiples of 4, while the kernel selection accepts any ratio from 2,
> so an MLA attention with a ratio of 2 aborted on GPUs that use the
> …

### [v1.1.0](https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0)
<sub>2026-11-26 · today</sub>

> **Overview**
> llama.cpp v1.1.0 adds the Inkling 2 family (base, Mini and DSpark), Domyn Edge 4B, Zaya1 8B, RAON-1-mini and Hy4 flash, splits DFlash speculative decoding into separate draft methods, and deprecates the old `llama_batch` API in favour of `llama_batch_ext`. It brings a large set of TTS and audio models (Kokoro, Zonos3-Mini, tiny-voca, VoxCPM2, MiniMax-Music3, YuE2, Fish S2, Higgs v3/VibeVoice-ASR and Kyutai Hibiki), token-aware chat parsing, named tool choice, automatic per-tensor quantization targeting a bpw or size budget, a slot-scheduling refactor in `llama-server`, a redesigned Llama Chat web UI with voice messages and agent traces, and updates `ggml` to v1.1.1.
> **API changes**
> - llama.h: deprecate the old `llama_batch` API in favour of `llama_batch_ext` and `llama_process` ([#32306](https://github.com/ggml-org/llama.cpp/pull/32306), [#32356](https://github.com/ggml-org/llama.cpp/pull/32356))
> - llama.h: add `llama_dflash_variant` and `llama_model_dflash_variant()` for the four DFlash draft heads ([#32016](https://github.com/ggml-org/llama.cpp/pull/32016))
> - llama.h: add `llama_model_meta_arr_n()` and `llama_model_meta_arr_str()` to read GGUF string arrays ([#32397](https://github.com/ggml-org/llama.cpp/pull/32397))
> …

### [b12774](https://github.com/ggml-org/llama.cpp/releases/tag/b12774) _(pre-release)_
<sub>2026-11-26 · today</sub>

> <details open>
> sync : ggml
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12760](https://github.com/ggml-org/llama.cpp/releases/tag/b12760) _(pre-release)_
<sub>2026-11-26 · today</sub>

> <details open>
> opencl: Adreno E17 compiler quirks off by default (#33013)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [CUDA: fuse the Inkling 2 short conv, depth mix, loop controller, L2 c…](https://github.com/ggml-org/llama.cpp/commit/0e4e925e8fa3d784b39f450050511576a0c8869b) | am17an |
| 2026-11-26 | [nix : remove x86_64-darwin support (#33114)](https://github.com/ggml-org/llama.cpp/commit/6aad4c7efd31860208ce643b8f3a84844911e20e) | Aigeruth |
| 2026-11-26 | [vulkan: fix Windows driver RDNA1 architecture misclassification (#33123)](https://github.com/ggml-org/llama.cpp/commit/46ba8b7008584804391038e9e6e3621c561ee677) | 0cc4m |
| 2026-11-26 | [DPI setting for PDF as Images - Inkling-2-Mini-BF16's work (#33061)](https://github.com/ggml-org/llama.cpp/commit/436d7e81ca593e294761428b4fe3d6cafef6800f) | createthis |
| 2026-11-26 | [ui: pass theme to toasts (#33082)](https://github.com/ggml-org/llama.cpp/commit/a866b4ade63921826c530307a368fbca3a334a0b) | ntowle |
| 2026-11-26 | [tests : add RPC support to test-llama-archs (#33112)](https://github.com/ggml-org/llama.cpp/commit/4ba835c637d863c00f54b59b8a0285d8d4db04cd) | rgerganov |
| 2026-11-26 | [quantize : include clocale for std::setlocale (#33105)](https://github.com/ggml-org/llama.cpp/commit/689194808a926219d9c68e733a04250afdb357cc) | xojy |
| 2026-11-26 | [CI: add Hip occupancy check and small static analysis report (#32365)](https://github.com/ggml-org/llama.cpp/commit/fd4b137e38c9fdb24b3f4fe3bc9e5fcc3c8f0002) | thelittlefireman |
| 2026-11-26 | [DFlash2: support Inkling-2-Mini DFlash2 (#33073)](https://github.com/ggml-org/llama.cpp/commit/55d482814bb3b985daa7bfa175c6d628fc27beac) | ruixiang63 |
| 2026-11-26 | [tests : take the test-fusion moe flag from the fixture name (#33104)](https://github.com/ggml-org/llama.cpp/commit/7365e4793c6c913c2be45c743c9f77e4af9a39de) | ServeurpersoCom |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
