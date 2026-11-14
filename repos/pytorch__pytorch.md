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
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1688.5 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 16d ago</sub>

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
| 2026-11-14 | [[compile] fix complex foreach inputs (#201839)](https://github.com/pytorch/pytorch/commit/7bfdc24bc8deebbe7cc64c42488c6af92a6d674a) | khushi-411 |
| 2026-11-14 | [[ROCm][TunableOp] Include activation epilogue in GemmAndBiasParams si…](https://github.com/pytorch/pytorch/commit/a2cf87e07e05677d63975102843f82656633786a) | menglcai |
| 2026-11-14 | [[inductor] Decompose small-k topk into fused argmax-and-remove rounds…](https://github.com/pytorch/pytorch/commit/f627724fb5e7c6987da31701b1b5552d3673439f) | anijain2305 |
| 2026-11-14 | [[inductor] Don't let reads broadcast along the reduction vote OUTER i…](https://github.com/pytorch/pytorch/commit/e4369d6d1a1ac759108f8bde0c55d906bb81ea9e) | anijain2305 |
| 2026-11-14 | [[Testcase Refactoring] Refactor test_minifier.py and test_dynamic_sha…](https://github.com/pytorch/pytorch/commit/f7ba74e4c9e19455c8e530d7df581e5506914e3c) | littlexiaozhang |
| 2026-11-14 | [[CPP FakeTensor] Convert or reject non-fake inputs in the native fall…](https://github.com/pytorch/pytorch/commit/77533284cb528b0f9e4a12f1515f99b33ef958be) | liangel-02 |
| 2026-11-14 | [[CPP FakeTensor] Apply Python's common-device rules in the C++ fallba…](https://github.com/pytorch/pytorch/commit/e59695ef091874f82de0c61495713f93958c82d2) | liangel-02 |
| 2026-11-14 | [[CPP FakeTensor] Run registered custom fake kernels on C++ fakes (#20…](https://github.com/pytorch/pytorch/commit/0d9fa45ec9e05cf853d9a2c6dbcffead3838d4f7) | liangel-02 |
| 2026-11-14 | [[CPP FakeTensor] Run prim meta implementations on C++ fakes (#204658)](https://github.com/pytorch/pytorch/commit/662536725f43d95ebeccafc8b58c5bac2ab10ab0) | liangel-02 |
| 2026-11-14 | [[CPP FakeTensor] Run ops on C++ fakes through FakeTensorMode's op_imp…](https://github.com/pytorch/pytorch/commit/ec942e6e653e5f60ae13dbcaa4f56124aed9dc88) | liangel-02 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
