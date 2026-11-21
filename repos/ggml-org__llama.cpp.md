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
| ⭐ **Stars** | 135.9k |
| 🍴 **Forks** | 25.9k |
| 🐞 **Open issues + PRs** | [2.6k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 57% · C 16% · Python 8% · TypeScript 5% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [b12606](https://github.com/ggml-org/llama.cpp/releases/tag/b12606) — 2026-11-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 500.6 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12606](https://github.com/ggml-org/llama.cpp/releases/tag/b12606) _(pre-release)_
<sub>2026-11-21 · today</sub>

> <details open>
> llama : remove fused lightning indexer gating (#32650)
> The fused lightning indexer is always used now, so drop the cparams flags, the auto probe and the non-fused fallbacks.
> Assisted-by: dsh:llama.cpp/ggml-org/DeepSeek-V4.1-Flash-1017-GGUF (Mac Studio, M5 Ultra, 256GB)
> </details>
> **Website:**
> …

### [b12604](https://github.com/ggml-org/llama.cpp/releases/tag/b12604) _(pre-release)_
<sub>2026-11-21 · today</sub>

> <details open>
> llama-grammar: Fix integer overflow (#32551)
> * llama-grammar: Fix integer overflow
> * Check incorrect values at parsing and bail out nicely
> * fix style
> </details>
> …

### [b12603](https://github.com/ggml-org/llama.cpp/releases/tag/b12603) _(pre-release)_
<sub>2026-11-21 · today</sub>

> <details open>
> llama : score only the k-pools of the ubatch sequences in QSA (#32519)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12602](https://github.com/ggml-org/llama.cpp/releases/tag/b12602) _(pre-release)_
<sub>2026-11-21 · today</sub>

> <details open>
> sycl: Improve Grouped XMX GEMM by avoiding SLM staging (#31428)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12600](https://github.com/ggml-org/llama.cpp/releases/tag/b12600) _(pre-release)_
<sub>2026-11-20 · today</sub>

> <details open>
> model : Inkling 2 Mini (#32694)
> * Conversion
> * Separate model_type
> * Add gate_rank to allow building from metadata while testing
> * Base model
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [model: apply .scale tensors automatically + fix correctness (#32669)](https://github.com/ggml-org/llama.cpp/commit/19bc41dbb41e858eebc269b49ccdec1f0d28880c) | ngxson |
| 2026-11-21 | [sycl: bound CONV_TRANSPOSE_1D input iteration (#31109)](https://github.com/ggml-org/llama.cpp/commit/e50c254a22c590c9d2a60db86690d48d42497e2b) | newjordan |
| 2026-11-21 | [ggml : improvements to the memory access pattern in `ggml_compute_for…](https://github.com/ggml-org/llama.cpp/commit/660be5506b15eae512f0df3ae0cc168712555319) | kazutoshi-ak |
| 2026-11-21 | [mtmd: support kyutai/hibiki realtime full-duplex (#32491)](https://github.com/ggml-org/llama.cpp/commit/c622f623fca9f0f085eb82f38874d1ab4a1791cd) | ngxson |
| 2026-11-21 | [sycl: add IQ4_NL and IQ4_XS weight reorder (#31998)](https://github.com/ggml-org/llama.cpp/commit/c6610333490e1d28d2700982064b76baf2bcb08c) | Titaniumtown |
| 2026-11-21 | [sycl: column-blocked gated_delta_net kernel (#32456)](https://github.com/ggml-org/llama.cpp/commit/44c20b1c0a1c77fd629fc5d032a5d7fa5843ebca) | Titaniumtown |
| 2026-11-21 | [ui: open the context gauge panel on click as a popover (#32685)](https://github.com/ggml-org/llama.cpp/commit/80325823d47ce8d02ae487de4b5563b2695684e4) | allozaur |
| 2026-11-21 | [sycl: add fused ADD, RMS_NORM, MUL and vectorize rms norm (#31753)](https://github.com/ggml-org/llama.cpp/commit/a818a46f3df4b6dee7f59f174283deaeae083c4b) | clemenswasser |
| 2026-11-21 | [CUDA: abort on UB in fastdiv (#32698)](https://github.com/ggml-org/llama.cpp/commit/b019be0c86e8adaf8b46627c091c24c1597b95f9) | JohannesGaessler |
| 2026-11-21 | [vulkan: unroll FA coopmat1 array due to a driver bug on AMD Windows (…](https://github.com/ggml-org/llama.cpp/commit/362ac929749d56e433878585a8506f24968698b4) | 0cc4m |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
