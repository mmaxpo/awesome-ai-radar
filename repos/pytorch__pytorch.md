# pytorch/pytorch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pytorch/pytorch)

> Tensors and Dynamic neural networks in Python with strong GPU acceleration

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | The leading deep-learning framework |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 105.5k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.2k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1679.9 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 14d ago</sub>

> **PyTorch 2.15.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.14.1](https://github.com/pytorch/pytorch/releases/tag/v2.14.1) — PyTorch 2.14.1 Release
<sub>2026-09-30 · 1mo ago</sub>

> This release is meant to fix the following regressions and silent correctness issues:
> **Silent correctness fixes**
> - Fix incorrect `torch.linalg.lstsq` solutions on MPS for complex batched underdetermined systems ([#196113](https://github.com/pytorch/pytorch/issues/196113)), fixed by [#196128](https://github.com/pytorch/pytorch/pull/196128)
> - Fix non-orthogonal `U` and inaccurate small singular values from `torch.linalg.svd` on MPS for rank-deficient and ill-conditioned inputs ([#196112](https://github.com/pytorch/pytorch/issues/196112)), fixed by [#196139](https://github.com/pytorch/pytorch/pull/196139) and [#199063](https://github.com/pytorch/pytorch/pull/199063)
> - Update the CUDA 13.2 Linux binaries to CUDA 13.2.2 ([#196351](https://github.com/pytorch/pytorch/pull/196351)). This NVIDIA update resolves two critical issues that could produce incorrect results ([CUDA 13.2.2 release notes](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html#overview)):
>   - cuBLAS: `cublasLtMatmul()` could ignore tensor-wide scaling for NVFP4 matrix multiplications (introduced in CUDA 13.2 Update 1)
> …

### [v2.14.0](https://github.com/pytorch/pytorch/releases/tag/v2.14.0) — PyTorch 2.14.0 Release
<sub>2026-09-02 · 2mo ago</sub>

> **PyTorch 2.14.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.13.0](https://github.com/pytorch/pytorch/releases/tag/v2.13.0) — PyTorch 2.13.0 Release
<sub>2026-07-08 · 4mo ago</sub>

> **PyTorch 2.13.0 Release Notes**
> - [Highlights](#highlights)
> - [Backwards Incompatible Changes](#backwards-incompatible-changes)
> - [Deprecations](#deprecations)
> - [New Features](#new-features)
> - [Improvements](#improvements)
> …

### [v2.12.1](https://github.com/pytorch/pytorch/releases/tag/v2.12.1) — PyTorch 2.12.1 Release, bug fix release
<sub>2026-06-18 · 4mo ago</sub>

> This release is meant to fix the following regressions and silent correctness issues:
> **Regression fixes**
> - Fix nondeterministic outputs in test_batch_invariance with FLASH_ATTN on NVIDIA B200 GPUs ([#181248](https://github.com/pytorch/pytorch/issues/181248)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
> - Fix illegal memory access in the Triton convolution2d_bwd_weight kernel on B100/B200 (sm100) GPUs ([#187081](https://github.com/pytorch/pytorch/issues/187081)), fixed by updating Triton to 3.7.1 ([#186814](https://github.com/pytorch/pytorch/pull/186814))
> - Fix fill_ on byte-dtype views with misaligned storage offset ([#186821](https://github.com/pytorch/pytorch/pull/186821))
> **Releng / Build**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [[xpu] Fix LOW priority XPU streams failing with "Unrecognized stream"…](https://github.com/pytorch/pytorch/commit/afab3f0f6c5e2d897b4843b6900f779911a82c8f) | chaojun-zhang |
| 2026-11-12 | [[dynamo] Update custom `hash(o)` normalization (#201180)](https://github.com/pytorch/pytorch/commit/0a115260d2300d9b5b3d29dee98373a725c338ff) | riccardofelluga |
| 2026-11-12 | [[CUDA] Keep Python headers first in storage sharing (#201935) (#201935)](https://github.com/pytorch/pytorch/commit/185e8d4bf23f414aca6a2842fd415446e47e4ef8) | q10 |
| 2026-11-12 | [[inductor] Skip SDPA fusion when the matched scale is zero (#203330)](https://github.com/pytorch/pytorch/commit/5291044bad04f9f0606e330377be25ae8e83aaaf) | KarhouTam |
| 2026-11-12 | [Add RBLN-SW/torch-rbln to CRCR allowlist as L1 (#193925)](https://github.com/pytorch/pytorch/commit/dd002fbd68c6d39bd55af91dc39b27c91f09eb0d) | rebel-tskim |
| 2026-11-12 | [[dynamo] Check a compile package against the GPU arch, not the GPU na…](https://github.com/pytorch/pytorch/commit/f0129b28468940c9ac202e685910e080fd6d2fdb) | bobrenjc93 |
| 2026-11-12 | [[Testcase Refactoring][cpp_extensions] Add GENERIC hw_classification …](https://github.com/pytorch/pytorch/commit/39ac148da6c5e4d3746a68990096ca34afba5b2c) | njjtan |
| 2026-11-12 | [[Testcase Refactoring] Make test_subgraph_choice device-agnostic via …](https://github.com/pytorch/pytorch/commit/38a27739de967ffe838bc312ca36b817172d0a46) | gavinwang269 |
| 2026-11-12 | [Fix `sample_kwargs` in `polygamma` op info (#174771)](https://github.com/pytorch/pytorch/commit/42d1654dbdd571d6fedbbedada099edbe30b9e7d) | pbielak |
| 2026-11-12 | [[Testcase Refactoring] Add hardware classification to glob group test…](https://github.com/pytorch/pytorch/commit/d358ead46e23445ad9586f600ca817a84d818f55) | anning-2026 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
