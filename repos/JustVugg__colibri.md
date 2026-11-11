# JustVugg/colibri

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/JustVugg/colibri)

> A hierarchical inference engine for frontier MoE models: hot experts on the GPU (CUDA, Vulkan), warm ones in RAM, cold ones streamed from NVMe. Written in C, runs on the hardware you already own.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why I saved it** | Run huge MoE models with GPU/RAM/NVMe expert offloading |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 49.9k |
| 🍴 **Forks** | 5.9k |
| 🐞 **Open issues + PRs** | [188](https://github.com/JustVugg/colibri/issues) |
| 💻 **Languages** | C 54% · Python 31% · Cuda 5% · HTML 4% · Shell 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-07-01 |
| 📦 **Latest release** | [v2.1.0](https://github.com/JustVugg/colibri/releases/tag/v2.1.0) — 2026-10-31 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 47.7 MB |
| 🌐 **Website** | https://justvugg.github.io/colibri |

## 📦 Recent releases

### [v2.1.0](https://github.com/JustVugg/colibri/releases/tag/v2.1.0) — colibri v2.1.0
<sub>2026-10-31 · 10d ago</sub>

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
<sub>2026-09-24 · 1mo ago</sub>

> 96 pull requests since v1.12.0, 80 of them from contributors. Two tokenizers
> brought back to the reference, brio on the ninth engine, `coli chat` working
> again at the default context on two families, and a placement decision that
> is now measured on the card in front of it instead of predicted.
> **Tokenizers, measured against the reference**
> - **#1654**: qwen36 tokenized differently from HF `tokenizers` in two ways.
> …

### [v1.12.0](https://github.com/JustVugg/colibri/releases/tag/v1.12.0) — colibri 1.12.0
<sub>2026-09-20 · 1mo ago</sub>

> **colibri 1.12.0**
> 81 pull requests since v1.11.0. A new way to ask a model a closed question,
> a redesigned dashboard and landing page, and a long run of small failures
> that used to answer 500 or die on a locale.
> **Brio mode: score a closed set instead of generating**
> - **#1632**: brio mode, on all nine engines. Hand the engine the options an
> …

### [v1.11.0](https://github.com/JustVugg/colibri/releases/tag/v1.11.0) — colibri v1.11.0
<sub>2026-09-13 · 1mo ago</sub>

> 56 pull requests since v1.10.2. A ninth model family, five real bugs closed
> across four engines, and the two platforms the C tests never built on now
> building them in CI.
> **A ninth engine: DeepSeek V4.1 Flash**
> - **#1453**: DeepSeek V4.1 Flash (552B, 510 GB on disk) runs on a CPU box
>   streaming experts from an SSD, with no conversion: the released checkpoint
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-31 | [Merge pull request #2530 from JustVugg/dev](https://github.com/JustVugg/colibri/commit/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6) | JustVugg |
| 2026-10-31 | [Merge pull request #2528 from JustVugg/fix/readme-q36-mtp-default](https://github.com/JustVugg/colibri/commit/312e52838091ff54fd3b09da386557b7a02a9932) | JustVugg |
| 2026-10-31 | [site: the version line and the project's model names](https://github.com/JustVugg/colibri/commit/ac4358632cd16eddf78e13207d6e39a8d8545e5b) | JustVugg |
| 2026-10-31 | [ui: System One opens with a generic example, in the page's language](https://github.com/JustVugg/colibri/commit/46b665bb1cad478e12c482b62aefaf4e42302bd3) | JustVugg |
| 2026-10-31 | [site: the new site, with every model of 2.1.0](https://github.com/JustVugg/colibri/commit/55f928eab6ffcf0f3ae6ae6c1bada48a4d8795e7) | JustVugg |
| 2026-10-31 | [README: Qwen3.6's MTP head drafts with Q36_MTP=1, not by default](https://github.com/JustVugg/colibri/commit/042491d52aedc761c19a430f1d8d9a017b9bdcb9) | JustVugg |
| 2026-10-31 | [Merge pull request #2526 from JustVugg/dev](https://github.com/JustVugg/colibri/commit/704a3f68184b78367a04cb5526e428dc2f90f05b) | JustVugg |
| 2026-10-31 | [Merge pull request #2527 from JustVugg/fix/vk-pool-import-windows](https://github.com/JustVugg/colibri/commit/7dd91ae363d2e1d3f030d804cebe12dd207cde4f) | JustVugg |
| 2026-10-31 | [README: every model, the GGUF table, the GPU sections and our benchmark tables](https://github.com/JustVugg/colibri/commit/563647ccf78d9569bacce849bbc5d728a1486ba7) | JustVugg |
| 2026-10-31 | [vulkan: the exit report's resident set without glibc's freed blocks](https://github.com/JustVugg/colibri/commit/2c2947bc5848d5d772a50d559f1ee436bd50e881) | JustVugg |

[See all commits ↗](https://github.com/JustVugg/colibri/commits)

## 👥 Top contributors

[JustVugg](https://github.com/JustVugg) (3085) · [ZacharyZcR](https://github.com/ZacharyZcR) (218) · [monotophic](https://github.com/monotophic) (156) · [rudycelekli](https://github.com/rudycelekli) (139) · [kreuzzelg](https://github.com/kreuzzelg) (102)

## ⬇️ Get it

```bash
git clone https://github.com/JustVugg/colibri.git
```
