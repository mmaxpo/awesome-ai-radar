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
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1683.2 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 15d ago</sub>

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
| 2026-11-13 | [Optimize CSR SpMM CPU grain size and inner accumulation (#188237)](https://github.com/pytorch/pytorch/commit/9192590aacc83d4f2d7d2c987fa7f59f6532ed88) | zhengjun-xing |
| 2026-11-13 | [[Testcase Refactoring] Gate flop counter device tests by capability (…](https://github.com/pytorch/pytorch/commit/e4d1b4754f7561c81e49ed5294a993c0358e6d7c) | danieldale2026 |
| 2026-11-13 | [[XPU] Support release branch refs for torch-xpu-ops (#202608)](https://github.com/pytorch/pytorch/commit/559518f34d65241ac1fd61ce02f9ae23946b1355) | chuanqi129 |
| 2026-11-13 | [[fsdp] Fix double gradient division for singleton groups (#203693)](https://github.com/pytorch/pytorch/commit/f34bbf7b50a40b714683eaf898da94086d5fbd6b) | shuhuayu |
| 2026-11-13 | [[dynamo] Guard LazyComputedConstant operands at reconstruction time (…](https://github.com/pytorch/pytorch/commit/a1b3d1af97e987060803654d38ddfbfdc0bec8f5) | rtimpe |
| 2026-11-13 | [[6/N] Refactor `TestPartitioningDevice` and enable for XPU (#196447)](https://github.com/pytorch/pytorch/commit/0522dc9f0a3faeedbb0c470985e737d98d1bbc59) | pbielak |
| 2026-11-13 | [[MKLDNN][CPU] Fix zero_ buffer overflow for low-precision tensors (#2…](https://github.com/pytorch/pytorch/commit/e3ac352d3a99cf5333c3c2be0ae3e586c436157a) | tangyuan499-commits |
| 2026-11-13 | [[CPP FakeTensor] Add a temporary check for ops that still need Python…](https://github.com/pytorch/pytorch/commit/3e401a7960544973cdc1c7d5dbcc4d1340e6c160) | liangel-02 |
| 2026-11-13 | [[CPP FakeTensor] Record the ops Python decomposes under static shapes…](https://github.com/pytorch/pytorch/commit/95b7ec73ce50567a4f9086cd3f0421f5606b1de5) | liangel-02 |
| 2026-11-13 | [[ROCm] Support CUDAExtension(dlink=True) via -fgpu-rdc and hipcc link…](https://github.com/pytorch/pytorch/commit/f255efb835b43871d164c9752f27c179bf49d921) | umechand-amd |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
