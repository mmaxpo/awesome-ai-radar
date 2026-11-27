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
| ⭐ **Stars** | 136.5k |
| 🍴 **Forks** | 26.2k |
| 🐞 **Open issues + PRs** | [2.7k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 55% · C 18% · Python 8% · TypeScript 6% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [b12815](https://github.com/ggml-org/llama.cpp/releases/tag/b12815) — 2026-11-27 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 508.1 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12815](https://github.com/ggml-org/llama.cpp/releases/tag/b12815) _(pre-release)_
<sub>2026-11-27 · today</sub>

> <details open>
> cuda : fix NVFP4 MMQ y_scale over-read in the stream-k fixup (#33136)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12814](https://github.com/ggml-org/llama.cpp/releases/tag/b12814) _(pre-release)_
<sub>2026-11-27 · today</sub>

> <details open>
> moe-cache : support experts selected on another backend (#33133)
> When the experts are selected on another backend than the cache, e.g. the loop passes of inkling2_loop with a layer split, the lookup reads a copy of the ids made by the scheduler, which has no source to read the shape from. Take the experts per token from build_lookup instead.
> Fixes #33101
> </details>
> **Website:**
> …

### [b12812](https://github.com/ggml-org/llama.cpp/releases/tag/b12812) _(pre-release)_
<sub>2026-11-27 · today</sub>

> <details open>
> metal : check all fused nodes for concurrency (#33175)
> * metal : check all fused nodes for concurrency
> The concurrency check for a fused group only examined the last node, so
> intermediate outputs (e.g. the TOPK_MOE ids/weights) and the group's
> sources (e.g. the router logits) were ignored. This allowed the fused
> …

### [b12811](https://github.com/ggml-org/llama.cpp/releases/tag/b12811) _(pre-release)_
<sub>2026-11-27 · today</sub>

> <details open>
> ui: share conversations to Hugging Face datasets as agent traces (#32608)
> * ui: add @ggml-org/llama-huggingface, a Hugging Face account as a package
> A package in ui/lib that gives an app running in the browser, with no
> server of its own, a Hugging Face account. Its plain entry holds "Sign in
> with Hugging Face" (OAuth with PKCE and dynamic client registration) and
> …

### [b12810](https://github.com/ggml-org/llama.cpp/releases/tag/b12810) _(pre-release)_
<sub>2026-11-27 · today</sub>

> <details open>
> hex-hmx: fix accuracy issues in act and weight scaling, drop w8a8+f16 hybrid mode (no longer needed) (#33166)
> Co-authored-by: Max Krasnyansky <maxk@qti.qualcomm.com>
> </details>
> **Website:**
> - <https://llama.app>
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [[Inkling 2] Support nvfp4 pass-through (#33062)](https://github.com/ggml-org/llama.cpp/commit/4c7344447cb1727f1e2f982febc99a8f88dcb77f) | pcuenca |
| 2026-11-27 | [CUDA: fix ADD_ID launch for more than 65535 tokens (#33162)](https://github.com/ggml-org/llama.cpp/commit/3ab385146cad1a374dadc40e042dcc50edceb046) | fox5611 |
| 2026-11-27 | [vulkan: handle empty conv3d kernel, fixes validation error (#33106)](https://github.com/ggml-org/llama.cpp/commit/d67b7a99d8b3603660bdc9970f0c6383c511a5ab) | 0cc4m |
| 2026-11-27 | [vulkan: further optimize coopmat2 GDN (#32860)](https://github.com/ggml-org/llama.cpp/commit/3b103f75e93929df4fb89e5911c047fbf737ab49) | jeffbolznv |
| 2026-11-27 | [ggml-zdnn: make zTensor memory usage visible for fitting (#31849)](https://github.com/ggml-org/llama.cpp/commit/4346838ad89d2eebd51f4071df0587979b66dacd) | taronaeo |
| 2026-11-27 | [CUDA: cache the device type at init (#33142)](https://github.com/ggml-org/llama.cpp/commit/00201974578d4429047853e4ff5ad0e9e14b4cf2) | NoahOksuz |
| 2026-11-27 | [ggml: support quant scales for fp8 and nvfp4 (#28898)](https://github.com/ggml-org/llama.cpp/commit/a386950136a817a6e0368446922a48431920103c) | 0cc4m |
| 2026-11-27 | [convert : preserve pooler for BertForSequenceClassification (#33122)](https://github.com/ggml-org/llama.cpp/commit/15fcfc7357f8de73671d39e7d8c594e1beb3052d) | ApacheWang |
| 2026-11-27 | [graph : read recurrent states in place instead of copying (#28841) (#…](https://github.com/ggml-org/llama.cpp/commit/7b74cb92d67384373e87512f4ffd2dbef756b944) | luciusacarr |
| 2026-11-27 | [cuda : fix NVFP4 MMQ y_scale over-read in the stream-k fixup (#33136)](https://github.com/ggml-org/llama.cpp/commit/2a8bf0f593472159d8805e9c2a6efb482634db05) | anujj |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
