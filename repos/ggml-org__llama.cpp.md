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
| ⭐ **Stars** | 136.2k |
| 🍴 **Forks** | 26.1k |
| 🐞 **Open issues + PRs** | [2.6k](https://github.com/ggml-org/llama.cpp/issues) |
| 💻 **Languages** | C++ 57% · C 16% · Python 8% · TypeScript 6% · Cuda 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ggml` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-03-10 |
| 📦 **Latest release** | [b12728](https://github.com/ggml-org/llama.cpp/releases/tag/b12728) — 2026-11-25 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 506.8 MB |
| 🌐 **Website** | https://llama.app |

## 📦 Recent releases

### [b12728](https://github.com/ggml-org/llama.cpp/releases/tag/b12728) _(pre-release)_
<sub>2026-11-25 · today</sub>

> <details open>
> ggml: allow reserving scratch memory in graph_optimize (#31898)
> * ggml: allow reserving scratch memory in graph_optimize
> Add add_scratch to ggml_backend_graph_optimize_params. A backend can
> reserve compute buffer memory that is allocated before a node `first`
> and kept until a node `last` has been computed, e.g. for data that
> …

### [b12726](https://github.com/ggml-org/llama.cpp/releases/tag/b12726) _(pre-release)_
<sub>2026-11-25 · today</sub>

> <details open>
> sycl: F8 e4m3 initial support SET_ROWS, CPY, ADD, MUL_MAT, MUL_MAT_ID (#31871)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12723](https://github.com/ggml-org/llama.cpp/releases/tag/b12723) _(pre-release)_
<sub>2026-11-25 · today</sub>

> <details open>
> model : inkling2 graph with fewer ops in mix() and control() (#32948)
> Assisted-by: Claude Opus 5.5
> </details>
> **Website:**
> - <https://llama.app>
> …

### [b12722](https://github.com/ggml-org/llama.cpp/releases/tag/b12722) _(pre-release)_
<sub>2026-11-25 · today</sub>

> <details open>
> opencl: add clc coopmat moe kernel for q4_0/q4_1/q4_k/q5_0/q5_1/q5_k/q6_k/mxfp4 (#32971)
> </details>
> **Website:**
> - <https://llama.app>
> **Attestations:**
> …

### [b12721](https://github.com/ggml-org/llama.cpp/releases/tag/b12721) _(pre-release)_
<sub>2026-11-25 · today</sub>

> <details open>
> tests : fix MSVC static build of test-batch-alloc and test-server-component (#32870)
> Fixes #32868
> </details>
> **Website:**
> - <https://llama.app>
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [llama.cpp : bump version to 1.1.0 (#33043)](https://github.com/ggml-org/llama.cpp/commit/beb9d49339ee29af52428577103b27a4d6f46d7d) | ggerganov |
| 2026-11-25 | [vocab : implement Metaspace prepend_scheme always for BPE (#33038)](https://github.com/ggml-org/llama.cpp/commit/532d67426bb874f06a8acc6959af81b34206f7f9) | ApacheWang |
| 2026-11-25 | [ui: fix for a chat form update loop with large fonts and long model n…](https://github.com/ggml-org/llama.cpp/commit/5e4fda8ed04607671e9a993a7f029515620c0989) | maxipesfix |
| 2026-11-25 | [sync : ggml](https://github.com/ggml-org/llama.cpp/commit/a28feb45892a417176f5c3665c786715aff3c12a) | ggerganov |
| 2026-11-25 | [ggml : bump version to 1.1.0 (ggml/1699)](https://github.com/ggml-org/llama.cpp/commit/3125043613c13b1bd6327a31e9dbdb8a8c122405) | ggerganov |
| 2026-11-25 | [llama : honor metaspace_prepend_scheme for SPM (#31986)](https://github.com/ggml-org/llama.cpp/commit/98f870c220a7d09a95e5476c1ad2cea6b2cd2c1e) | angt |
| 2026-11-25 | [model : load YaRN hparams in llama_model_base::load_hparams (#33032)](https://github.com/ggml-org/llama.cpp/commit/2e2f5a03730e4549377762b740c012fbcc1473bb) | ApacheWang |
| 2026-11-25 | [ui: fix tool result media shown twice, uncapped and dropped after its…](https://github.com/ggml-org/llama.cpp/commit/41c7a1b49d1ec314305f0e50019faac3b2bcbec3) | allozaur |
| 2026-11-25 | [ui: open the warm microphone only once the pointer rests on its butto…](https://github.com/ggml-org/llama.cpp/commit/77026f6e6184730c060727c52dd0fe306cd77f2e) | allozaur |
| 2026-11-25 | [ui: add file extensions to the Vite config's local imports (#33023)](https://github.com/ggml-org/llama.cpp/commit/c8eda101c1d5def0694a62606d12cf542b68f655) | allozaur |

[See all commits ↗](https://github.com/ggml-org/llama.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/llama.cpp.git
```
