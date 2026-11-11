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
| ⭐ **Stars** | 105.4k |
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.2k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 66% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1676.9 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 13d ago</sub>

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
| 2026-11-11 | [[ROCm] Update rocm preview wheel to 10.3.0a20261110 (#202821)](https://github.com/pytorch/pytorch/commit/b6751f13523657eaebfc769fcb3dacd9fbaff119) | chinmaydk99 |
| 2026-11-11 | [[ROCm]: Add Operator Benchmarks for Group GEMM (#202666)](https://github.com/pytorch/pytorch/commit/d4e6027656a2a53ebfde047a31f89cd9159f67ae) | TheRealMichaelWang |
| 2026-11-11 | [Run a test shard against an editable install (#203390)](https://github.com/pytorch/pytorch/commit/b95ed4b8bd19a06890083ac6d45e7dfc5d6f3050) | zklaus |
| 2026-11-11 | [[inductor][cpu] Add cpp.vec_exp_u20 to compute vectorized float exp w…](https://github.com/pytorch/pytorch/commit/eb55b7b009b589aec37148542f8479fecc753679) | helloguo |
| 2026-11-11 | [Promote Inductor and AOTInductor test skips (#203629)](https://github.com/pytorch/pytorch/commit/ca93cf6be6a4e342b3a0cf5b28c9f1dc1fcab311) | jathu |
| 2026-11-11 | [Promote compiler frontend and compatibility test skips (#203628)](https://github.com/pytorch/pytorch/commit/e0a644d262b9139ca2ff5247eaf80d0fbc2e6540) | jathu |
| 2026-11-11 | [Promote eager and backend test skips to collection (#203627)](https://github.com/pytorch/pytorch/commit/ddcc85b9e860c1de9e5fca03ac8712edcac896aa) | jathu |
| 2026-11-11 | [Expose existing shared test skips at collection (#203626)](https://github.com/pytorch/pytorch/commit/1fb9bca7ac5e273f0ec39dd53ccbed37a590e588) | jathu |
| 2026-11-11 | [Prune existing skips before sharding (#203625)](https://github.com/pytorch/pytorch/commit/5f18a31f4379e3fbf2e779c4106b841f6a74fe11) | jathu |
| 2026-11-11 | [[headeronly] Moved TransposeType to torch/headeronly (#204244)](https://github.com/pytorch/pytorch/commit/3519cba5cb6923b734b9a59eaf4c3a2fb64f4532) | cleonard530 |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
