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
| 🐞 **Open issues + PRs** | [18.5k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1688.1 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 25d ago</sub>

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
| 2026-11-23 | [refactor FSDPTest and FSDPTestMininx to be device-agnostic (#205271)](https://github.com/pytorch/pytorch/commit/fcd0bf3b6fbb83d5e376f7547f5abb07914e0555) | fffrog |
| 2026-11-23 | [s390x: update tolerance thresholds for test_vjp_grid_sampler_2d_cpu_f…](https://github.com/pytorch/pytorch/commit/a8e58581263b8a27cbfbb7e8752b82eded883334) | AlekseiNikiforovIBM |
| 2026-11-23 | [[CooR] Register the device_mesh custom ops when DTensor is imported (…](https://github.com/pytorch/pytorch/commit/8389bc9d7fb1a4acbc42d6f34932a8b2828ac627) | bobrenjc93 |
| 2026-11-23 | [[dynamo] Drop redundant locals and super() calls in DiskDynamoStore/D…](https://github.com/pytorch/pytorch/commit/b956060641ef3790c20bd3008be5f25ab59db34b) | bobrenjc93 |
| 2026-11-23 | [[dynamo] Factor import-alias installation out of CompilePackage.insta…](https://github.com/pytorch/pytorch/commit/d40e925734ce312465d61a6f063ef94f86df0da8) | bobrenjc93 |
| 2026-11-23 | [[dynamo] Build the cache entry once in DynamoStore.save_package (#206…](https://github.com/pytorch/pytorch/commit/a133f1ebd0112a3b77d4c529aac81affd2632750) | bobrenjc93 |
| 2026-11-23 | [[dynamo] PrecompileCacheEntry.from_cache_entry never returns None (#2…](https://github.com/pytorch/pytorch/commit/8a80cb68b856f220aa65631fd3daab0957492734) | bobrenjc93 |
| 2026-11-23 | [[dynamo] Flatten _lookup_code's code_source walk (#206197)](https://github.com/pytorch/pytorch/commit/42277bbbee4876384659e564e905ce13a9cd2441) | bobrenjc93 |
| 2026-11-23 | [[cuDNN][conv] Derive max workspace during cuDNN conv autotuning after…](https://github.com/pytorch/pytorch/commit/130edca4ebcad531eb267df71388428f1bb87af4) | eqy |
| 2026-11-23 | [[dynamo] Use CPython-style arg checks for builtin arity errors (#205749)](https://github.com/pytorch/pytorch/commit/134033073c8d2342daf13e3b4bac833c8a92563a) | guilhermeleobas |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
