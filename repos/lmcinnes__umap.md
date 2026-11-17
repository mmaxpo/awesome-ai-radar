# lmcinnes/umap

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/lmcinnes/umap)

> Uniform Manifold Approximation and Projection

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | UMAP: fast dimensionality reduction and visualization |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 8.3k |
| 🍴 **Forks** | 893 |
| 🐞 **Open issues + PRs** | [541](https://github.com/lmcinnes/umap/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `umap` `dimensionality-reduction` `visualization` `machine-learning` `topological-data-analysis` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2017-07-02 |
| 📦 **Latest release** | [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0) — 2026-11-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 105.0 MB |
| 🌐 **Website** | https://umap-learn.readthedocs.io |

## 📦 Recent releases

### [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0)
<sub>2026-11-10 · 7d ago</sub>

> **What's Changed**
> * Embed combined models without densMAP instead of failing with KeyError by @raashish1601 in https://github.com/lmcinnes/umap/pull/1304
> * Read neighbours straight from the CSR arrays in breadth_first_search() by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1326
> * Initialise new points in update() from the same neighbours as the graph by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1325
> * Allow plot.show() to display interactive plots with search by @Don-Yin in https://github.com/lmcinnes/umap/pull/1321
> * 0.6.0 release version by @lmcinnes in https://github.com/lmcinnes/umap/pull/1333
> …

### [release-0.6.0rc1](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0rc1) _(pre-release)_
<sub>2026-11-03 · 13d ago</sub>

> **What's Changed**
> * Preserve input dtype in transform and fit_transform output by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1253
> * Add py.typed marker for type checkers by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1252
> * Fix _select_font_color ValueError on hex backgrounds by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1251
> * Remove fastmath=True from layouts.py optimization functions by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1255
> * Update pipelines to use uv and turn off macOS builds by @gclendenning in https://github.com/lmcinnes/umap/pull/1258
> …

### [release-0.5.12](https://github.com/lmcinnes/umap/releases/tag/release-0.5.12)
<sub>2026-04-08 · 7mo ago</sub>

> **What's Changed**
> * Remove nomic atlas reference from plotting.rst by @cakiki in https://github.com/lmcinnes/umap/pull/1238
> * [MINOR] Update README.rst by @cakiki in https://github.com/lmcinnes/umap/pull/1241
> * Remove more atlas references / fix doc build warnings by @cakiki in https://github.com/lmcinnes/umap/pull/1243
> * Fix for #1180 and #1200 - NaN loss on Parametric UMAP retraining. by @jacobgolding in https://github.com/lmcinnes/umap/pull/1244
> * Edit distance fixes + fast short ascii method (Myers) by @jh83775 in https://github.com/lmcinnes/umap/pull/1247
> …

### [release-0.5.11](https://github.com/lmcinnes/umap/releases/tag/release-0.5.11)
<sub>2026-01-12 · 10mo ago</sub>

> **What's Changed**
> * Deterministic sort for fast_knn_indices by @bohemian-miser in https://github.com/lmcinnes/umap/pull/1236
> **New Contributors**
> * @bohemian-miser made their first contribution in https://github.com/lmcinnes/umap/pull/1236
> **Full Changelog**: https://github.com/lmcinnes/umap/compare/release-0.5.10.post2...release-0.5.11

### [release-0.5.10.post2](https://github.com/lmcinnes/umap/releases/tag/release-0.5.10.post2)
<sub>2025-12-11 · 11mo ago</sub>

> **Full Changelog**: https://github.com/lmcinnes/umap/compare/release-0.5.10.post1...release-0.5.10.post2

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Add live parameter sliders to the parameters documentation (#1341)](https://github.com/lmcinnes/umap/commit/6dafbbcfbd701aeacdfb417e72712d726c21c705) | domoritz |
| 2026-11-16 | [Merge pull request #1350 from skundu42/fix/aligned-umap-pickle](https://github.com/lmcinnes/umap/commit/4f16ff100db79a73d12bea6a7a57c632945eab60) | lmcinnes |
| 2026-11-16 | [Support pickling fitted AlignedUMAP models](https://github.com/lmcinnes/umap/commit/c0f74bd70ffc9be59c4d90ea72da249113d969c8) | skundu42 |
| 2026-11-16 | [Merge pull request #1349 from sebastianbreguel/scout/transform-perf](https://github.com/lmcinnes/umap/commit/696c3822e3d7cae98e3cfddc8771fe436ee76178) | lmcinnes |
| 2026-11-16 | [Merge pull request #1342 from linjiaye929/fix/parametric-large-array-…](https://github.com/lmcinnes/umap/commit/f0edc8abb72bc7c476465d4150780c37973f954d) | lmcinnes |
| 2026-11-15 | [Loop numba metrics in numba for the small-data transform distance matrix](https://github.com/lmcinnes/umap/commit/2e3d66c5b1ce01095208844c5bf155f037d88e92) | sebastianbreguel |
| 2026-11-15 | [Merge pull request #1347 from rishi02102017/sparse-precomputed-exact-k](https://github.com/lmcinnes/umap/commit/27f4b2a096a0341371e0707a7261b2e61f3c9151) | lmcinnes |
| 2026-11-14 | [Merge pull request #1348 from lmcinnes/whats_new](https://github.com/lmcinnes/umap/commit/5113b770a4ca109b21e51edd5c88bf981a1702e3) | lmcinnes |
| 2026-11-14 | [Enhance documentation for UMAP 0.6: add details on new initialization…](https://github.com/lmcinnes/umap/commit/eccee468690c04b4a6bc4b1170c0bec6516d8552) | lmcinnes |
| 2026-11-14 | [Add 'whats_new_0_6' to the documentation table of contents](https://github.com/lmcinnes/umap/commit/059615053770dc433d419c226fb04ba44b56d7e5) | lmcinnes |

[See all commits ↗](https://github.com/lmcinnes/umap/commits)

## ⬇️ Get it

```bash
git clone https://github.com/lmcinnes/umap.git
```
