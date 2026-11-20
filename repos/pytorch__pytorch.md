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
| 🐞 **Open issues + PRs** | [18.5k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1675.2 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 22d ago</sub>

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
| 2026-11-20 | [[Profiler] Exclude XPU runtime/driver events from External id fallbac…](https://github.com/pytorch/pytorch/commit/d59e86aecf1bce34411bfe66c9e01d9257b8212b) | SlawomirLaba |
| 2026-11-20 | [  [dynamo] preserve Stream/Event subclass type across graph-break rec…](https://github.com/pytorch/pytorch/commit/9f48f43a4b9d6c006367c9e8c88bc50e479ad079) | Stevennnn |
| 2026-11-20 | [[dynamo] Raise TypeError for objects missing __enter__/__exit__ in `w…](https://github.com/pytorch/pytorch/commit/0538ec2f623ce3cec2b044526fcd391731435d3d) | guilhermeleobas |
| 2026-11-20 | [[xpu] Handle grouped_mm with empty tensor as input (#205611)](https://github.com/pytorch/pytorch/commit/cffb5c017443e7f44d5c70bffbdffd0c08add392) | LuFinch |
| 2026-11-20 | [[Testcase Refactoring] Classify Python operator typing tests as gener…](https://github.com/pytorch/pytorch/commit/d473a25fd4f88af8851bbe38eeb9ac64ec45d6af) | PAGEMRW |
| 2026-11-20 | [[profiler][cuspy] Decode buffers using saved record layouts (#205783)](https://github.com/pytorch/pytorch/commit/57ab62c9e3b2ec77869f129b666055cfbdccd94d) | ngimel |
| 2026-11-20 | [[Test][XPU] Enable `complex_tensor/test_complex_tensor.py` for XPU (#…](https://github.com/pytorch/pytorch/commit/b7f6ea368f14d8286250a1c3e8d5a461c3d3e84c) | pbielak |
| 2026-11-20 | [[Inductor] Let backends declare their ATen C shim table for AOTI (#20…](https://github.com/pytorch/pytorch/commit/4f595ce0558ee7e3037d24bd11c1848ed08aa206) | can-gaa-hou |
| 2026-11-20 | [[torchcomms] Remove torchcomms support from distributed_c10d (#205741)](https://github.com/pytorch/pytorch/commit/ededea4165730303c4dcd7d854b3f35b77a1d123) | d4l3k |
| 2026-11-20 | [[Testcase Refactoring] Split test/test_functional_autograd_benchmark.…](https://github.com/pytorch/pytorch/commit/5b48107b6c0a5c451f2a00642a56c8fe34750708) | KarhouTam |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
