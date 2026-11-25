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
| 🐞 **Open issues + PRs** | [367](https://github.com/ggml-org/whisper.cpp/issues) |
| 💻 **Languages** | C++ 52% · C 30% · Cuda 9% · Metal 3% · GLSL 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `openai` `speech-to-text` `transformer` `whisper` `inference` `speech-recognition` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2022-09-25 |
| 📦 **Latest release** | [v1.9.6](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.6) — 2026-11-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 48.2 MB |

## 📦 Recent releases

### [v1.9.6](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.9.6)
<sub>2026-11-23 · yesterday</sub>

> **Overview**
> New version has been released.
> **More info:** [dist : releases and versioning of ggml-org projects](https://github.com/ggml-org/ggml/discussions/1579)
> **Changelog since v1.9.5**
> 96ec4d98 ggml : revert 5922450fbce (#4200)
> 5eaee0cc ci : update CUDA 11.8.0 CUBLAS version to 11.11.3.6 (#4195)
> …

### [b5907](https://github.com/ggml-org/whisper.cpp/releases/tag/b5907) _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

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
| 2026-11-25 | [ci : move gpu-cuda, gpu-vulkan-nvidia-{cm,cm2} to DGX (#4209)](https://github.com/ggml-org/whisper.cpp/commit/092fa10992dec2a91680591697c857b566db7150) | danbev |
| 2026-11-25 | [Revert "ci : disable main-musa.Dockerfile from docker.yml (#4201)" (#…](https://github.com/ggml-org/whisper.cpp/commit/c8cbc3eda7afdbc4bda5381a544350a5272a9ecd) | danbev |
| 2026-11-25 | [cli : return non-zero on invalid language and diarize flags (#4085) (…](https://github.com/ggml-org/whisper.cpp/commit/adf50b68c113a4db234a2711bc678a92cb13b8a2) | goldnode |
| 2026-11-24 | [ci : add check for SPIRV-HeadersConfig for gpu-vulkan (#4204)](https://github.com/ggml-org/whisper.cpp/commit/c1a24047871444999b79f5e8612828f45881ae12) | danbev |
| 2026-11-24 | [ci : move ARM64 high-perf jobs to DGX Spark runners (#4206)](https://github.com/ggml-org/whisper.cpp/commit/3e2e46a43e39a25e4377bbc0fec4099a141f0f49) | danbev |
| 2026-11-24 | [ci : split deploy wasm job into build and deploy (#4205)](https://github.com/ggml-org/whisper.cpp/commit/bdcbc08e4ba295d71852df983998414d42d8e78f) | danbev |
| 2026-11-24 | [examples : add device option to whisper-bench (#4135)](https://github.com/ggml-org/whisper.cpp/commit/e96e4ce124940a83dfa4c11b2424467046a5ecd2) | danbev |
| 2026-11-24 | [examples : fix stereo to mono averaging with diarization (#4181)](https://github.com/ggml-org/whisper.cpp/commit/60fff93bce64888a5425466088bf96714aad9108) | rishi02102017 |
| 2026-11-24 | [ci : disable main-musa.Dockerfile from docker.yml (#4201)](https://github.com/ggml-org/whisper.cpp/commit/20ffd918a291745a0deddfaa25ba73fedc2c21f7) | danbev |
| 2026-11-24 | [whisper : remove unused logits_id sort in whisper_sample_token_topk (…](https://github.com/ggml-org/whisper.cpp/commit/0d7733f7dffea2af7598be202c640ddbd4a75f62) | mpermino |

[See all commits ↗](https://github.com/ggml-org/whisper.cpp/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
```
