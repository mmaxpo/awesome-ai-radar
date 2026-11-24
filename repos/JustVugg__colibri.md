# JustVugg/colibri

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/JustVugg/colibri)

> A hierarchical inference engine for frontier MoE models: hot experts on the GPU (CUDA, Vulkan), warm ones in RAM, cold ones streamed from NVMe. Written in C, runs on the hardware you already own.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Run huge MoE models with GPU/RAM/NVMe expert offloading |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 53.3k |
| 🍴 **Forks** | 6.4k |
| 🐞 **Open issues + PRs** | [257](https://github.com/JustVugg/colibri/issues) |
| 💻 **Languages** | C 55% · Python 30% · Cuda 7% · HTML 3% · Shell 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-07-01 |
| 📦 **Latest release** | [v2.2.0](https://github.com/JustVugg/colibri/releases/tag/v2.2.0) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 56.6 MB |
| 🌐 **Website** | https://justvugg.github.io/colibri |

## 📦 Recent releases

### [v2.2.0](https://github.com/JustVugg/colibri/releases/tag/v2.2.0) — colibri v2.2.0
<sub>2026-11-22 · yesterday</sub>

> colibri 2.2.0: everything since 2.1.0 (2026-10-31). The full list is in [CHANGELOG.md](https://github.com/JustVugg/colibri/blob/v2.2.0/CHANGELOG.md).
> **New models**
> - **Inkling-2-Small** (594B, 17B active, Apache 2.0): text, pictures and tools, from unsloth's GGUFs (UD-IQ1_S 171.7 GB to UD-Q4_K_XL 354 GB, pictures through the mmproj) or our int4 g64 converted from the NVFP4 release; CUDA and Vulkan, an MTP drafter (`INK2_MTP=1`).
> - **Inkling-2-Mini** (26.4B, 3.4B active, Apache 2.0), whose middle layers run three passes: text and pictures from unsloth's GGUFs (UD-IQ2_XXS 8.5 GB to UD-Q4_K_XL 17.6 GB; their root files and the `Mainline_Support` ones, mainline llama.cpp's `inkling2_loop` layout, alike) or our int4 g64 from the NVFP4 release; Vulkan and CUDA with a decode step in one frame of their dense chains (the routed experts on the card, the attention split over its positions), and the CPU. UD-Q4_K_XL decodes at 40.9-41.1 tok/s with CUDA, 39.2-39.4 with Vulkan and 8.0-8.1 on the CPU, and reads a 570-token prompt at 285-289 tok/s with CUDA and 270-277 with Vulkan.
> - **Qwen3.8-27B** (dense): text and images on CUDA, Vulkan and the CPU, its MTP head from a GGUF, and speculative decoding on CUDA with DFlash2.
> - **Kimi K3.1 Pro**: K3's weights with sparse attention past 2048 tokens, on the CPU, Vulkan and a new CUDA chain.
> …

### [v2.1.0](https://github.com/JustVugg/colibri/releases/tag/v2.1.0) — colibri v2.1.0
<sub>2026-10-31 · 24d ago</sub>

> **Huge open models on the machine you already have**: on the CPU, on any GPU through Vulkan, on NVIDIA cards through CUDA. Pure C, one file per model family.
> 387 pull requests since v2.0.0, 208 of them from 35 contributors. GGUF files now run natively on every engine, read exactly as published. Four new models arrive, Mistral-Large-4 (1T) among them. CUDA gets device chains of its own and a routed-expert tier for every engine. Qwen3.8-Flash-Next runs a 256k context at the speed of 64k, an agent's turns read only what is new, and there is a new chat UI.
> <p align="center">
>   <img src="https://raw.githubusercontent.com/JustVugg/colibri/v2.1.0/docs/media/ui/ui-experts.png" width="900" alt="the new chat UI with the expert map open">
> </p>
> **Highlights**
> …

### [v2.0.0](https://github.com/JustVugg/colibri/releases/tag/v2.0.0) — colibri v2.0.0
<sub>2026-10-06 · 1mo ago</sub>

> 169 pull requests since v1.12.1, 88 of them from contributors. Every MoE
> engine now runs on any GPU a Vulkan driver can see: the routed experts on a
> shared device tier, the dense layers on a device chain (all of them, or the
> first N that fit), and a second GPU for more experts. Three model families
> arrive (MiMo-V2.6, Qwen3-Coder, Qwen-Image-2.1) and one dense checkpoint
> (Qwen3.8-27B). Qwen3.8 Flash Next gets int4 experts and speculative decoding
> …

### [v1.12.1](https://github.com/JustVugg/colibri/releases/tag/v1.12.1) — colibri 1.12.1
<sub>2026-09-24 · 2mo ago</sub>

> 96 pull requests since v1.12.0, 80 of them from contributors. Two tokenizers
> brought back to the reference, brio on the ninth engine, `coli chat` working
> again at the default context on two families, and a placement decision that
> is now measured on the card in front of it instead of predicted.
> **Tokenizers, measured against the reference**
> - **#1654**: qwen36 tokenized differently from HF `tokenizers` in two ways.
> …

### [v1.12.0](https://github.com/JustVugg/colibri/releases/tag/v1.12.0) — colibri 1.12.0
<sub>2026-09-20 · 2mo ago</sub>

> **colibri 1.12.0**
> 81 pull requests since v1.11.0. A new way to ask a model a closed question,
> a redesigned dashboard and landing page, and a long run of small failures
> that used to answer 500 or die on a locale.
> **Brio mode: score a closed set instead of generating**
> - **#1632**: brio mode, on all nine engines. Hand the engine the options an
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [Merge pull request #2965 from JustVugg/dev](https://github.com/JustVugg/colibri/commit/e479104ae01bdc40ce81e675299b1d230891b321) | JustVugg |
| 2026-11-22 | [Merge pull request #2969 from JustVugg/batch/2026-11-22-c](https://github.com/JustVugg/colibri/commit/43de59227f19c065f874adf6c3adb2e3d5846edb) | JustVugg |
| 2026-11-22 | [TUI screenshots taken again on 2.2.0 at a 64K context; the expert map…](https://github.com/JustVugg/colibri/commit/66d2cb9a5a04caa96d53608d8f4f88ef7044d13e) | JustVugg |
| 2026-11-22 | [qwen38: the expert map reads the CUDA tier and the chain's slots, not…](https://github.com/JustVugg/colibri/commit/2454cbf2bce96915988c5a3f0fa2a2dec88d5de6) | JustVugg |
| 2026-11-22 | [README: coli chat is the classic line chat, coli tui the full-screen …](https://github.com/JustVugg/colibri/commit/a2ee98f1c0006b1f9d2c6aa49711c989db220225) | JustVugg |
| 2026-11-22 | [Merge pull request #2968 from JustVugg/batch/2026-11-22-b](https://github.com/JustVugg/colibri/commit/05245ef45048b837fee5ed7b5b1ab2e59161fb80) | JustVugg |
| 2026-11-22 | [changelog: #2967 in 2.2.0's fixes](https://github.com/JustVugg/colibri/commit/d516759ae8a2e9acd52332aa04b3a73ec9a6cb40) | JustVugg |
| 2026-11-22 | [Merge pull request #2967 from KairaCode/q38-gguf-ple-read](https://github.com/JustVugg/colibri/commit/6a5b9ec9d049ab0da3d69b335c83496166223b5b) | JustVugg |
| 2026-11-22 | [gguf: overlapped reads on Windows, so a thread team's reads do not queue](https://github.com/JustVugg/colibri/commit/38a345a11264c404db49546eb80607df0538781d) | KairaCode |
| 2026-11-22 | [Merge pull request #2966 from JustVugg/batch/2026-11-22-a](https://github.com/JustVugg/colibri/commit/679b34ee49b4ffaabe95fe22cfc6a61920c8781a) | JustVugg |

[See all commits ↗](https://github.com/JustVugg/colibri/commits)

## ⬇️ Get it

```bash
git clone https://github.com/JustVugg/colibri.git
```
