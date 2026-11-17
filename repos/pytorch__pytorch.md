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
| ⭐ **Stars** | 105.7k |
| 🍴 **Forks** | 30.8k |
| 🐞 **Open issues + PRs** | [18.4k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1682.2 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 19d ago</sub>

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
| 2026-11-17 | [[inductor] Add a non-overlapping fast path for max_pool2d backward. (…](https://github.com/pytorch/pytorch/commit/4777739420c9dc6d667d2b271ef343e1b3a23422) | orrangetabby17 |
| 2026-11-17 | [[CD] Remove redundant libgomp NEEDED replacement (#201032)](https://github.com/pytorch/pytorch/commit/6af6987aa3603504c75df85c0906be686e0b8454) | JoshuaZhuwj |
| 2026-11-17 | [[HOP] Keep node meta when scan re-traces its body for autograd (#203334)](https://github.com/pytorch/pytorch/commit/012eb2b6a70aba7fffcb0b567f57e02a0d6f70a8) | jack8558 |
| 2026-11-17 | [[CPP FakeTensor] Handle symbolic shapes and data-dependent outputs (#…](https://github.com/pytorch/pytorch/commit/3f915f45bf5af116f418578034e2a8442e72425e) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Propagate constants and invalidate written aliases (…](https://github.com/pytorch/pytorch/commit/99d95de06648647efaf0605c8dd756834ca46478) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Create constants from numbers-as-tensors operations …](https://github.com/pytorch/pytorch/commit/3a69ddd3e0487af613346fe4ab012e197b260db5) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Handle lift conversion and initial lift constants (#…](https://github.com/pytorch/pytorch/commit/3097d3d61f78fdabe7f866792a28c0d208378658) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Move the fake fallback into libtorch_python (#205161)](https://github.com/pytorch/pytorch/commit/9c699801a5173fe8ec5d0fe04281280e4f2d5248) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Select native modes in FakeTensorMode.__new__ (#205160)](https://github.com/pytorch/pytorch/commit/0d44fe1d02dff4562acaacef3632f1e712cfe42d) | liangel-02 |
| 2026-11-17 | [[CPP FakeTensor] Route data access through fake detach handling (#204…](https://github.com/pytorch/pytorch/commit/98fac19a8ae52d1bc9aa17aa377db18953a26641) | liangel-02 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
