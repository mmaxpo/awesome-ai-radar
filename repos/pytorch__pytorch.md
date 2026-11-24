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
| 🍴 **Forks** | 30.7k |
| 🐞 **Open issues + PRs** | [18.6k](https://github.com/pytorch/pytorch/issues) |
| 💻 **Languages** | Python 67% · C++ 27% · Cuda 3% · C 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `neural-network` `autograd` `gpu` `numpy` `deep-learning` `tensor` `python` `machine-learning` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2016-08-13 |
| 📦 **Latest release** | [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — 2026-10-28 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1693.0 MB |
| 🌐 **Website** | https://pytorch.org |

## 📦 Recent releases

### [v2.15.0](https://github.com/pytorch/pytorch/releases/tag/v2.15.0) — PyTorch 2.15.0 Release
<sub>2026-10-28 · 26d ago</sub>

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
| 2026-11-24 | [[Stable ABI] Add cpublas shims (#204470)](https://github.com/pytorch/pytorch/commit/304eed355e40bf1a1688ae94ede5ee6d0e16bdbe) | cleonard530 |
| 2026-11-24 | [[inductor][cutlass] Gate the CUTLASS C++ backend on supported CUDA ar…](https://github.com/pytorch/pytorch/commit/40a3237bbf9de00e0496973f7bd17a223b9de31c) | crcrpar |
| 2026-11-24 | [[CUDA] Skip garbage collection of cached blocks during graph capture …](https://github.com/pytorch/pytorch/commit/df5fb4949fa9d5656b79aab2839b3ddb467313c2) | kapilsh |
| 2026-11-24 | [[CUDA] Keep cached segments during graph capture when an allocation f…](https://github.com/pytorch/pytorch/commit/06c79b1e5b4b6a8aa1a62f0b7d9f783c466896c2) | kapilsh |
| 2026-11-24 | [`F.interpolate`: Add `inter-area` mode on CPU, matching opencv (#205844)](https://github.com/pytorch/pytorch/commit/f29b6d519223d9b95d601b3b08d9145bc34947c1) | NicolasHug |
| 2026-11-24 | [[MPS] Fix silently wrong depthwise conv2d output for large filters (#…](https://github.com/pytorch/pytorch/commit/a4742da251b6429f96b5a016fdfc893cbb1deb0f) | Isalia20 |
| 2026-11-24 | [Add WaitCounter instrumentation to CUDA availability checks (#206319)…](https://github.com/pytorch/pytorch/commit/f8be190f31bb148e90804c964a48ac3ccbc4e8a8) | dsesh |
| 2026-11-24 | [[MPS] Add _scaled_grouped_mm_v2 (#206066)](https://github.com/pytorch/pytorch/commit/1d28e3a704d1d634d240e8fe0566c0c6df975458) | malfet |
| 2026-11-24 | [[pytorch][typing] Declare pci_bus_id, pci_device_id and pci_domain_id…](https://github.com/pytorch/pytorch/commit/4db54c7ee2e3a048a97ec16fac5a41013578663c) | lovetoburnswhen |
| 2026-11-24 | [[profiler][cuspy] Use native CUDA event graph node IDs (#206322)](https://github.com/pytorch/pytorch/commit/c9fdc83eb4d3f53c3a3f2356cd8885c111e653ad) | ngimel |

[See all commits ↗](https://github.com/pytorch/pytorch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pytorch/pytorch.git
```
