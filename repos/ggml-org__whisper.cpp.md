# ggml-org/whisper.cpp

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ggml-org/whisper.cpp)

> Port of OpenAI's Whisper model in C/C++

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Fast local speech-to-text (Whisper in C/C++) |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 55.5k |
| 🍴 **Forks** | 6.4k |
| 🐞 **Open issues + PRs** | [368](https://github.com/ggml-org/whisper.cpp/issues) |
| 💻 **Languages** | C++ 53% · C 30% · Cuda 9% · Metal 3% · GLSL 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `openai` `speech-to-text` `transformer` `whisper` `inference` `speech-recognition` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2022-09-25 |
| 📦 **Latest release** | [v1.9.6](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.6) — 2026-11-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 51.3 MB |

## 📦 Recent releases

### [v1.9.6](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.6)
<sub>2026-11-23 · 2d ago</sub>

> **Overview**
> New version has been released.
> **More info:** [dist : releases and versioning of ggml-org projects](https://github.com/ggml-org/ggml/discussions/1579)
> **Changelog since v1.9.5**
> 96ec4d98 ggml : revert 5922450fbce (#4200)
> 5eaee0cc ci : update CUDA 11.8.0 CUBLAS version to 11.11.3.6 (#4195)
> …

### [b5907](https://github.com/ggml-org/whisper.cpp/releases/tag/b5907) _(pre-release)_
<sub>2026-11-20 · 5d ago</sub>

> _No notes._

### [v1.9.5](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.5)
<sub>2026-10-06 · 1mo ago</sub>

> **Overview**
> Maintenance release. Updates to [ggml v0.26.0](https://github.com/ggml-org/ggml/releases/tag/v0.26.0).
> **Nightly build:** [b5454](https://github.com/ggml-org/whisper.cpp/releases/tag/b5454)
> **More info:** [dist : releases and versioning of ggml-org projects](https://github.com/ggml-org/ggml/discussions/1579)
> **Changelog since v1.9.4**
> d1be6fde whisper : bump version to 1.9.5 (#4102)
> …

### [b5454](https://github.com/ggml-org/whisper.cpp/releases/tag/b5454) _(pre-release)_
<sub>2026-10-06 · 1mo ago</sub>

> _No notes._

### [v1.9.4](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.4)
<sub>2026-09-11 · 2mo ago</sub>

> **Overview**
> New version has been released.
> **Nightly build:** [b5130](https://github.com/ggml-org/whisper.cpp/releases/tag/b5130)
> **More info:** [dist : releases and versioning of ggml-org projects](https://github.com/ggml-org/ggml/discussions/1579)
> **Changelog since v1.9.3**
> 927cfce3 metal : remove leftover ggml-metal.metal kernels file (#4051)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [whisper : name greedy and beam_search structs (#4203)](https://github.com/ggml-org/whisper.cpp/commit/79b11911d9d38c4be2fc7dc8b4efeff3324c090f) | danbev |
| 2026-11-26 | [ci : attempt to fix gpu-vulkan job](https://github.com/ggml-org/whisper.cpp/commit/c807cc4c92d5286a2b0e95f902da37d519d5cd7b) | danbev |
| 2026-11-26 | [examples : remove duplicate cases from common-ggml.cpp](https://github.com/ggml-org/whisper.cpp/commit/f9c9a890bed21351eb5cae5b479b6b17a1fcf004) | danbev |
| 2026-11-26 | [sync : sync ggml](https://github.com/ggml-org/whisper.cpp/commit/bd5d85f657b1874772357306fb6109b03402fe81) | danbev |
| 2026-11-26 | [ggml : bump version to 1.1.0 (ggml/1699)](https://github.com/ggml-org/whisper.cpp/commit/1b84ebedd0578c8d92b892a95b37712ec93c3adc) | ggerganov |
| 2026-11-26 | [ggml-cpu : accept the flash_attn_ext indexed bias (llama/33016)](https://github.com/ggml-org/whisper.cpp/commit/6bdb397539b94ed175f37fe68ff2cd123d1f285b) | sanmai |
| 2026-11-26 | [metal : commit the graph in chunks with one command buffer thread (ll…](https://github.com/ggml-org/whisper.cpp/commit/8c256b235823444a41135e713899c077067e8a4c) | am17an |
| 2026-11-26 | [ggml: allow input async copies (llama/30685)](https://github.com/ggml-org/whisper.cpp/commit/0e8be6d0ef50faa58a6b2591f4d723bfa0f2ba7c) | am17an |
| 2026-11-26 | [ggml: allow reserving scratch memory in graph_optimize (llama/31898)](https://github.com/ggml-org/whisper.cpp/commit/7202c4fd9b97041ca03412c5599d1fd4bff14680) | am17an |
| 2026-11-26 | [sycl: F8 e4m3 initial support SET_ROWS, CPY, ADD, MUL_MAT, MUL_MAT_ID…](https://github.com/ggml-org/whisper.cpp/commit/cf6ad088a2acadb1eb6dacc1aae6742f3600b24c) | mctylr-gh |

[See all commits ↗](https://github.com/ggml-org/whisper.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
```
