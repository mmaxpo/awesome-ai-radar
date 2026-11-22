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
| 🍴 **Forks** | 25.9k |
| 🐞 **Open issues + PRs** | [2.6k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 57% · C 16% · Python 8% · TypeScript 5% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [b12631](https://github.com/ggml-org/llama.cpp/releases/tag/b12631) — 2026-11-22 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 500.5 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12631](https://github.com/ggml-org/llama.cpp/releases/tag/b12631) _(pre-release)_
<sub>2026-11-22 · today</sub>

> <details open>
> webgpu : update GDN supports_op check (#32782)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12629](https://github.com/ggml-org/llama.cpp/releases/tag/b12629) _(pre-release)_
<sub>2026-11-22 · today</sub>

> <details open>
> opencl: add coopmat GEMM for Adreno 850 (Q4_0, Q5_0, Q8_0, Q4_K, Q5_K, Q6_K) (#32686)
> * opencl: add Q4_0 coopmat GEMM for Adreno 850
> Assisted-by: Claude Opus 5.5
> * opencl: add Q5_0 coopmat GEMM for Adreno 850
> * opencl: add Q8_0 coopmat GEMM for Adreno 850
> …

### [b12628](https://github.com/ggml-org/llama.cpp/releases/tag/b12628) _(pre-release)_
<sub>2026-11-22 · today</sub>

> <details open>
> vulkan : support non-contiguous src in SCALE (#32735)
> Assisted-By: Opus 5.5
> </details>
> **Website:**
> - <https://llama.app>
> …

### [b12627](https://github.com/ggml-org/llama.cpp/releases/tag/b12627) _(pre-release)_
<sub>2026-11-22 · today</sub>

> <details open>
> server : fit non-causal batches in one ubatch (#32713)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12626](https://github.com/ggml-org/llama.cpp/releases/tag/b12626) _(pre-release)_
<sub>2026-11-22 · today</sub>

> <details open>
> vulkan : fix memset for unaligned ranges for non-UMA devices (#32725)
> See https://github.com/ggml-org/llama.cpp/pull/32574
> </details>
> **Website:**
> - <https://llama.app>
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [ggml/gguf : avoid creating invalid enum values from untrusted file da…](https://github.com/ggml-org/llama.cpp/commit/8d60873dfb8619f2b5ed31adfbab07cccb40db5c) | mohitmishra786 |
| 2026-11-22 | [ggml : add SIGMOID backward pass (#32126)](https://github.com/ggml-org/llama.cpp/commit/ad50351f5092436f312d98d25689207df25f4802) | gianni-cor |
| 2026-11-22 | [chat : trigger lazy grammar on bare JSON tool calls (#32497)](https://github.com/ggml-org/llama.cpp/commit/42f6a58fd1bfd475d9f09ea3bf7ef671c059eaf2) | ViezeVingertjes |
| 2026-11-22 | [ggml : fix nonzero clear on WebGPU and non-UMA devices (#32727)](https://github.com/ggml-org/llama.cpp/commit/9c10c94e16ebc4f3ed7c06264a93bf7e019c3f26) | sanmai |
| 2026-11-22 | [HIP: fix double halving of NVFP4 scales on CDNA3 (#32790)](https://github.com/ggml-org/llama.cpp/commit/8cb0d98ccd0a310879ae8eaa1ce2c41e4b40a052) | TwelveNights |
| 2026-11-22 | [webgpu : update GDN supports_op check (#32782)](https://github.com/ggml-org/llama.cpp/commit/e300919cc704ddde3a8a8346a8714f57eeeee71b) | sanmai |
| 2026-11-22 | [ggml-webgpu : Update to a recent version of Dawn (#32779)](https://github.com/ggml-org/llama.cpp/commit/5d28d64bf2969d7b9c863e5001de83b30ce81557) | sanmai |
| 2026-11-22 | [opencl: add coopmat GEMM for Adreno 850 (Q4_0, Q5_0, Q8_0, Q4_K, Q5_K…](https://github.com/ggml-org/llama.cpp/commit/1fb8a269603b497fc1ce7dab2f2fc5c1be7a51cb) | shaofeiqi |
| 2026-11-22 | [vulkan : support non-contiguous src in SCALE (#32735)](https://github.com/ggml-org/llama.cpp/commit/8a97fa98ab1a454709bbf5ac979661feaeadec40) | Revertron |
| 2026-11-22 | [server : fit non-causal batches in one ubatch (#32713)](https://github.com/ggml-org/llama.cpp/commit/225a5345bbb0e0c70859af5441ba922beb666fcf) | am17an |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
