# google-deepmind/alphafold

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/google-deepmind/alphafold)

> Open source code for AlphaFold 2.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧬 AI for science |
| **Project** | — |
| **Why it's worth a look** | AlphaFold 2: predicts 3D protein structures (Nobel-winning work) |
| **Added** | 2026-11-11 |

💤 **Quiet** — no activity for 6mo

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 14.9k |
| 🍴 **Forks** | 3.0k |
| 🐞 **Open issues + PRs** | [311](https://github.com/google-deepmind/alphafold/issues) |
| 💻 **Languages** | Python 97% · Shell 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-04-22 (6mo ago) |
| 📅 **Created** | 2021-06-17 |
| 📦 **Latest release** | [v2.3.2](https://github.com/google-deepmind/alphafold/releases/tag/v2.3.2) — 2023-04-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 16.4 MB |

## 📦 Recent releases

### [v2.3.2](https://github.com/google-deepmind/alphafold/releases/tag/v2.3.2) — Alphafold v2.3.2
<sub>2023-04-05 · 3y ago</sub>

> **Change log**
> - More robust download in Colab with shutil (thanks @gmihaila).
> - Added ability to only run relax for the best unrelaxed model in the run_alphafold.py.
> - Improved documentation for the ranked outputs (thanks @ulupo).
> - Removed jax dependency from results pkl.
> - Updated tensorflow to 2.11.0.
> …

### [v2.3.1](https://github.com/google-deepmind/alphafold/releases/tag/v2.3.1) — Alphafold v2.3.1
<sub>2023-01-12 · 3y ago</sub>

> Version v2.3.1 combines a few small updates.
> **Change log**
> - Add option for eval time dropout.
> - Add A100 inference timings to README.
> - Speed up MSA lookups in Colab for multimers.
> - Increase max allowed sequence length in Colab to 4,000.
> …

### [v2.3.0](https://github.com/google-deepmind/alphafold/releases/tag/v2.3.0) — AlphaFold v2.3.0
<sub>2022-12-13 · 3y ago</sub>

> Version v2.3.0 updates the AlphaFold-Multimer model parameters. These new models are expected to be more accurate on large protein complexes but use the same model architecture and training methodology as our previously released AlphaFold-Multimer paper. See [the v2.3.0 release note](https://github.com/deepmind/alphafold/blob/main/docs/technical_note_v2.3.0.md) for more details.
> Thanks to various memory optimisations, AlphaFold-Multimer now uses less GPU memory and it can therefore handle longer proteins.
> A number of other bug fixes and small improvements have been made.
> **Change log**
> * Added new AlphaFold-Multimer models with better accuracy on large protein complexes.
> * Added early stopping to recycling.
> …

### [v2.2.4](https://github.com/google-deepmind/alphafold/releases/tag/v2.2.4) — AlphaFold v2.2.4
<sub>2022-09-21 · 4y ago</sub>

> Version v2.2.4 is a bug fix release
> **Change log**
> * Bump versions of third party libraries: jax 0.3.17, absl-py 1.0.0, haiku 0.0.7, numpy 1.21.6, tensorflow 2.9.0
> * Adapt `jnp.take` to account for behaviour with the new jax version, see https://github.com/deepmind/alphafold/issues/513 (thanks @sokrypton).
> * Reduce size of docker image by removing package caches, see https://github.com/deepmind/alphafold/pull/526 (thanks @TheDen).
> * Fix incorrect argument in `backbone_loss`, see https://github.com/deepmind/alphafold/issues/570 (thanks @sokrypton).

### [v2.2.3](https://github.com/google-deepmind/alphafold/releases/tag/v2.2.3) — AlphaFold v2.2.3
<sub>2022-08-25 · 4y ago</sub>

> Version v2.2.3 is a bug fix release.
> **Change log**
> * Pin Conda version to 4.13.0 to prevent Docker/Colab setup issues (thanks @Meghpal, @michaelkeith18).
> * Change the Colab PAE json output to new format that matches the format used in the new release of the AlphaFold Protein Structure Database (AFDB). See the [AFDB FAQ](https://alphafold.ebi.ac.uk/faq/#faq-7) for a description of the new format.
> * Add a readme file for AFDB.
> * Type hint improvements.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-04-22 | [Update AFS custom template JSON input description](https://github.com/google-deepmind/alphafold/commit/c77e5d2a8961d1a353632c462914ff0a32a950f6) | DeepMind |
| 2026-04-14 | [Remove dead TF data transform functions](https://github.com/google-deepmind/alphafold/commit/7e1e321dfd7f9df5c8cf17b3f2a64fc794d18b1a) | Augustin-Zidek |
| 2026-04-13 | [Remove unused transform](https://github.com/google-deepmind/alphafold/commit/425615ec1a198a8b3e3fa29901f7c7af0c0ad9dd) | Augustin-Zidek |
| 2026-04-07 | [Update the AFDB readme to use gcloud storage instead of gsutil](https://github.com/google-deepmind/alphafold/commit/27fb0c0b898af876f2801168ab22899d043389f5) | Augustin-Zidek |
| 2026-04-02 | [Remove support for Python versions that are no longer supported](https://github.com/google-deepmind/alphafold/commit/4593e8c4118b12ae2260a268a18a42deb7569a31) | Augustin-Zidek |
| 2026-03-31 | [Update AFS custom template JSON input description](https://github.com/google-deepmind/alphafold/commit/c015a39b990b22a64c24281f39674fa0272ac31d) | DeepMind |
| 2026-03-12 | [Update technical note for v2.3.0 to mention the change in distillatio…](https://github.com/google-deepmind/alphafold/commit/42719e135a62438aa651d2bc1d143626083c3703) | joshabramson |
| 2026-03-10 | [Stop using Conda to install OpenMM and PDBfixer - both now on PyPI](https://github.com/google-deepmind/alphafold/commit/a4315dd7b8f9f543ad5f4080af4a42d431ef3b35) | Augustin-Zidek |
| 2026-03-03 | [Inline softmax implementation so that we don't break with old JAX](https://github.com/google-deepmind/alphafold/commit/636a18bae7137ffe7b4d946f1be12e25adc877fc) | Augustin-Zidek |
| 2026-02-03 | [Fix Numpy 2.4 compatibility](https://github.com/google-deepmind/alphafold/commit/dc61fb4a31bd15c4b3363281217e125d34748892) | Augustin-Zidek |

[See all commits ↗](https://github.com/google-deepmind/alphafold/commits)

## ⬇️ Get it

```bash
git clone https://github.com/google-deepmind/alphafold.git
```
