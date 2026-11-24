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
| ⭐ **Stars** | 136.1k |
| 🍴 **Forks** | 26.0k |
| 🐞 **Open issues + PRs** | [2.7k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 57% · C 16% · Python 8% · TypeScript 6% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [b12676](https://github.com/ggml-org/llama.cpp/releases/tag/b12676) — 2026-11-24 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 505.9 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12676](https://github.com/ggml-org/llama.cpp/releases/tag/b12676) _(pre-release)_
<sub>2026-11-24 · today</sub>

> <details open>
> GDN: use replay instead of rollback (#31669)
> * GDN: use replay instead of rollback [WIP]
> * memory : move rs_max with the sequence when find_slot swaps cells
> find_slot swapped pos/src/rs_pend/seq_id of the cell it moves out of the
> way, but not rs_max, so that sequence inherited the rollback depth of the
> …

### [b12675](https://github.com/ggml-org/llama.cpp/releases/tag/b12675) _(pre-release)_
<sub>2026-11-24 · today</sub>

> <details open>
> server : preserve a prompt-cache entry until restores succeed (#32828)
> Assisted-by: Codex
> </details>
> **Website:**
> - <https://llama.app>
> …

### [b12674](https://github.com/ggml-org/llama.cpp/releases/tag/b12674) _(pre-release)_
<sub>2026-11-24 · today</sub>

> <details open>
> opencl: fetch the Adreno binary kernel library at configure time for Windows on Snapdragon (#31759)
> * opencl: fetch the Adreno binary kernel library at configure time
> Make GGML_OPENCL_USE_ADRENO_BIN_KERNELS an option, default ON, and add
> GGML_OPENCL_ADRENO_BIN_KERNELS_FETCH, default ON. On Windows, CMake
> downloads the pinned adreno-opencl-kernels release from the Qualcomm
> …

### [b12671](https://github.com/ggml-org/llama.cpp/releases/tag/b12671) _(pre-release)_
<sub>2026-11-24 · today</sub>

> <details open>
> metal : batch concat rows and copy them in vector chunks (#32824)
> * metal : batch concat rows and copy them in vector chunks
> The concat kernel copied one element per thread, so wide rows with many rows ran at a
> fraction of the memory bandwidth. Batch several rows per threadgroup and copy the
> contiguous dim-0 elements in 4-element chunks when the row is contiguous.
> …

### [b12670](https://github.com/ggml-org/llama.cpp/releases/tag/b12670) _(pre-release)_
<sub>2026-11-24 · today</sub>

> <details open>
> ggml: compact bias on the existing FLASH_ATTN_EXT (#32740)
> * compact bias on the existing FLASH_ATTN_EXT for CUDA, ROCm and Vulkan
> * fixup! compact bias on the existing FLASH_ATTN_EXT for CUDA, ROCm and Vulkan
> * remove the Vulkan support from this PR
> * move the CUDA/HIP and Inkling 2 graph changes out of this PR
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [ggml-cpu: add SVE-optimized q5_0 and q5_1 dot-product kernels (#30867)](https://github.com/ggml-org/llama.cpp/commit/5fddd0b99888a90260736e0f734fa8e160064e03) | t-kusanagi |
| 2026-11-24 | [server : include MCP image and audio data in tool results (#32064)](https://github.com/ggml-org/llama.cpp/commit/66a3b01b0a243f119b144abfa7122b1677ea9114) | hmblair |
| 2026-11-24 | [context : prevent excessive CPU polling without OpenMP (#32378)](https://github.com/ggml-org/llama.cpp/commit/d3c257a493b31cf06a4e724ab4648d6f1a3e5e1e) | sanmai |
| 2026-11-24 | [metal : reserve the top-k scratch only for short rows (#32942)](https://github.com/ggml-org/llama.cpp/commit/3090e45a8675ebdefbc722f80609c75e5fa259ad) | ggerganov |
| 2026-11-24 | [ui: smooth chat form height and working directory chip across routes …](https://github.com/ggml-org/llama.cpp/commit/ba8521a44eaa91c5ecab0e5571cb75fc84c106b8) | allozaur |
| 2026-11-24 | [vulkan: add chunked GDN replay support (#32721)](https://github.com/ggml-org/llama.cpp/commit/72cda4a2228c254f95a556fa238488a1324b04d8) | 0cc4m |
| 2026-11-24 | [cuda : fuse RMS_NORM + MUL + MROPE/IMROPE and tune block size (#32500)](https://github.com/ggml-org/llama.cpp/commit/922cff91e9f60db1afc5c00cef444f3af7f882c4) | losewayy |
| 2026-11-24 | [Webui nix fix (#32645)](https://github.com/ggml-org/llama.cpp/commit/2e779d5e708660c5a399135cac8d769b4e8f86f1) | ZhaolunYin |
| 2026-11-24 | [model : Inkling 2 Mini mix() weighted sum with the scores as src0 (#3…](https://github.com/ggml-org/llama.cpp/commit/396ed2ccea7dc5e02adde8f154261b9f6d1047f0) | TwelveNights |
| 2026-11-24 | [ui: make Llama Chat a plain chat unless llama-server offers agent fea…](https://github.com/ggml-org/llama.cpp/commit/97bbf98fdfeb311e50e313fc807d3af1a1ff32d4) | allozaur |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
