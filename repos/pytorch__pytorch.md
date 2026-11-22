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
| ⭐ **Stars** | 105.8k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.6k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1684.2 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 24d ago</sub>

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
<sub>2026-06-18 · 5mo ago</sub>

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
| 2026-11-22 | [[MPS] Fix conv2d and conv_transpose2d for batch sizes above 65535 (#2…](https://github.com/pytorch/pytorch/commit/ee0eed2fcd35650303548025d2378bbe2ca44a91) | Isalia20 |
| 2026-11-22 | [Revert "Round float64 to float16, bfloat16 and float8 once in default…](https://github.com/pytorch/pytorch/commit/aabd19c7bc9b1ae4922427a10ba9d3357f864611) | pytorchmergebot |
| 2026-11-22 | [Revert "Fix float32 to float8_e8m0fnu rounding of subnormals (#204208)"](https://github.com/pytorch/pytorch/commit/bd3e2c245090920d286be339942ecbe1044a1eed) | pytorchmergebot |
| 2026-11-22 | [Revert "Declare has_denorm of the float8 numeric_limits as a float_de…](https://github.com/pytorch/pytorch/commit/4324c01ab74732eebd6f90d73c08ec3996389140) | pytorchmergebot |
| 2026-11-22 | [Revert "[Dynamo] Fix state pollution in test infra and config restore…](https://github.com/pytorch/pytorch/commit/ca4a71e7ebaa6a6b5ecb0235f0cbd02209922cb7) | pytorchmergebot |
| 2026-11-22 | [Declare has_denorm of the float8 numeric_limits as a float_denorm_sty…](https://github.com/pytorch/pytorch/commit/2dcb20fa18f6d4b7deed1fca6bf16fde1370e105) | lw |
| 2026-11-22 | [Fix float32 to float8_e8m0fnu rounding of subnormals (#204208)](https://github.com/pytorch/pytorch/commit/ada8b7f5f5cd3900bfd7589d922126afe9e745a6) | lw |
| 2026-11-22 | [Round float64 to float16, bfloat16 and float8 once in default convers…](https://github.com/pytorch/pytorch/commit/642748a888d9034acb357bb7b68f105c96a5b20f) | lw |
| 2026-11-22 | [[MPS] Use MPP and a decode kernel for MXFP8 and NVFP4 _scaled_mm_v2 (…](https://github.com/pytorch/pytorch/commit/c1aec0bbeb84ca90ac5739c6452771787bee4959) | malfet |
| 2026-11-22 | [[Dynamo] Fix state pollution in test infra and config restore (#191930)](https://github.com/pytorch/pytorch/commit/6e5f53dd5be082f3be970a413e91abad29e04b26) | guan404ming |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
