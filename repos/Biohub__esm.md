# Biohub/esm

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Biohub/esm)

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧬 AI for science |
| **Project** | — |
| **Why it's worth a look** | ESM3 and ESM C protein language models (successor to Meta's ESM) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 3.0k |
| 🍴 **Forks** | 406 |
| 🐞 **Open issues + PRs** | [78](https://github.com/Biohub/esm/issues) |
| 💻 **Languages** | Jupyter Notebook 57% · Python 43% |
| 📜 **License** | Other |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-09 (yesterday) |
| 📅 **Created** | 2024-06-25 |
| 📦 **Latest release** | [v3.4.3](https://github.com/Biohub/esm/releases/tag/v3.4.3) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 10.9 MB |

## 📦 Recent releases

### [v3.4.3](https://github.com/Biohub/esm/releases/tag/v3.4.3)
<sub>2026-11-09 · yesterday</sub>

> * bug fixes
> * bump transformers version to >= 5.16

### [v3.4.2](https://github.com/Biohub/esm/releases/tag/v3.4.2)
<sub>2026-10-30 · 12d ago</sub>

> - Added the Batch API (`ForgeBatchClient`) for folding, plus max-accuracy folding with ESMFold2 Pro (see `cookbook/snippets/batch.md` and `cookbook/snippets/fold_max_accuracy.md`)
> - Released the 2025-cutoff ESMFold2 model
> - fp8 inference for the ESMC backbone in ESMFold2, plus faster decode and caching
> - cuequivariance and xformers are no longer dependencies; the `"fused"` Triton backend works with a plain `pip install esm`
> - Pinned biotite < 2, which broke `ProteinComplex.from_rcsb`
> - SDK clients now time out after 125s instead of waiting forever, and guided generation retries transient API errors
> …

### [v3.4.1.post1](https://github.com/Biohub/esm/releases/tag/v3.4.1.post1)
<sub>2026-09-16 · 1mo ago</sub>

> This releases brings better compatibility between different implementations (HF / esm / mlx_lm) and allows use of a single set of model weights for all implementations. It also fixes multiple bugs
> - mol_type compared against MOL_TYPE_NONPOLYMER (3), not a private constant (4)
> - ESMC fused-kernel warnings appeared for non GPU machines, now gated on torch.cuda.is_available()
> - disto_cond / disto_cond_mask accepted in the experimental forward, EsmFold2Experimental now working as intended
> - A bug in the SAE implementation produced wrong results for a subset of SAE checkpoints. Fixed (bug fix)
> - Added SAE tests
> …

### [v3.4.1](https://github.com/Biohub/esm/releases/tag/v3.4.1)
<sub>2026-09-08 · 2mo ago</sub>

> - Added support for FoldCP
> - Added support for loading HF-style checkpoints (ESMFold2)
> - Various minor bug-fixes

### [v3.4.0](https://github.com/Biohub/esm/releases/tag/v3.4.0)
<sub>2026-08-27 · 2mo ago</sub>

> - Added full support for ESMC and ESMFold2
> - Added test suite for both ESMC and ESMFold2
> - Added compatibility layer for huggingface port of ESMC and ESMFold2
> - Maintained back compatibility with legacy models such as ESMC and support legacy model weights. ESMC now runs in emulation.
> - Github actions for issue management
> - Other smaller changes

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-09 | [Bump version to 3.4.3 (#428)](https://github.com/Biohub/esm/commit/fddac936fc921445da2d099a3e4f7ae928717292) | faustomilletari |
| 2026-11-06 | [Various improvements 2026-11-06 (#427)](https://github.com/Biohub/esm/commit/90d6497a546bb55929c2d3ca2e313d4613ec1922) | faustomilletari |
| 2026-10-29 | [Sync OSS esm 3.4.2 (#426)](https://github.com/Biohub/esm/commit/8f0834cbc350aeaf507f755475873f7c61fa44a1) | ebetica |
| 2026-10-21 | [release batch API, max accuracy folding (#424)](https://github.com/Biohub/esm/commit/296637a50f9f837aaa2a2231030c13141c265bd7) | imathur1 |
| 2026-09-16 | [Esm 3.4.1.post1 (#404)](https://github.com/Biohub/esm/commit/43b4548b86762edfa747b07d5f440aad3c33acee) | faustomilletari |
| 2026-09-03 | [OSS esm 3.4.1](https://github.com/Biohub/esm/commit/bf343ba264b650dff7a073643725f9aaa1fdbe8d) | faustomilletari |
| 2026-08-27 | [Make v3.4.0 publishable to PyPI (#390)](https://github.com/Biohub/esm/commit/827ec128e4cdaf80f7d6f95fb367a08980b34918) | ebetica |
| 2026-08-27 | [Remove mentions of installing from main (#389)](https://github.com/Biohub/esm/commit/912e9fcab19d266c4513aee98483a73571d85362) | ebetica |
| 2026-08-27 | [sync 20260825 (#386)](https://github.com/Biohub/esm/commit/ab44d95db38db90c584f18433462c5213338c118) | faustomilletari |
| 2026-08-24 | [esmfold2 notebook sync (#383)](https://github.com/Biohub/esm/commit/43ccece2ad485f27db46afdb67da2a9601e8f106) | imathur1 |

[See all commits ↗](https://github.com/Biohub/esm/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Biohub/esm.git
```
