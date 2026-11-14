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
| 🍴 **Forks** | 892 |
| 🐞 **Open issues + PRs** | [545](https://github.com/lmcinnes/umap/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `umap` `dimensionality-reduction` `visualization` `machine-learning` `topological-data-analysis` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2017-07-02 |
| 📦 **Latest release** | [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0) — 2026-11-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 100.4 MB |
| 🌐 **Website** | https://umap-learn.readthedocs.io |

## 📦 Recent releases

### [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0)
<sub>2026-11-10 · 4d ago</sub>

> **What's Changed**
> * Embed combined models without densMAP instead of failing with KeyError by @raashish1601 in https://github.com/lmcinnes/umap/pull/1304
> * Read neighbours straight from the CSR arrays in breadth_first_search() by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1326
> * Initialise new points in update() from the same neighbours as the graph by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1325
> * Allow plot.show() to display interactive plots with search by @Don-Yin in https://github.com/lmcinnes/umap/pull/1321
> * 0.6.0 release version by @lmcinnes in https://github.com/lmcinnes/umap/pull/1333
> …

### [release-0.6.0rc1](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0rc1) _(pre-release)_
<sub>2026-11-03 · 10d ago</sub>

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
| 2026-11-14 | [Merge pull request #1345 from sebastianbreguel/scout/parallel-project…](https://github.com/lmcinnes/umap/commit/aee7eefc9d022abf64b8d87fc32188b71f0f526d) | lmcinnes |
| 2026-11-14 | [Sort the hard-negative projection in parallel when its order is unique](https://github.com/lmcinnes/umap/commit/74e0b12d2dcb5dbcacf65ce7936a86ba1e238d1e) | sebastianbreguel |
| 2026-11-14 | [Merge pull request #1343 from sebastianbreguel/scout/blas-limit-proje…](https://github.com/lmcinnes/umap/commit/1b4d1dd26871a67fe7f531984d7d2aba64584f9c) | lmcinnes |
| 2026-11-14 | [Merge pull request #1344 from gclendenning/master](https://github.com/lmcinnes/umap/commit/99e7e507f773d7b8d1e4e9105c9aa89c87d7360f) | lmcinnes |
| 2026-11-14 | [Try running tests on 3.14/3.15 without parametric](https://github.com/lmcinnes/umap/commit/6384e6689739c40d55d1440d2b402c3f985fe5ea) | gclendenning |
| 2026-11-13 | [Limit BLAS threads around the hard-negative projection](https://github.com/lmcinnes/umap/commit/ce56664b5816ef7e8888aeeb12232988565ebad2) | sebastianbreguel |
| 2026-11-12 | [Merge pull request #1331 from sebastianbreguel/perf/inverse-layout-co…](https://github.com/lmcinnes/umap/commit/17ce948977b3410f71ca58a1a291356f66ad1f2e) | lmcinnes |
| 2026-11-12 | [Remove deprecated "standard" optimizer name and update documentation …](https://github.com/lmcinnes/umap/commit/69863fe456bce79ae87d2e396c16819d06007fb4) | lmcinnes |
| 2026-11-11 | [Merge pull request #1338 from AnaseDouramane/fix-recursive-init-n-com…](https://github.com/lmcinnes/umap/commit/8c925ee2b2a0b8425d4a240dfbfb91eadec43c93) | lmcinnes |
| 2026-11-11 | [Merge pull request #1337 from jan-glx/fix-contiguous-knn-dists](https://github.com/lmcinnes/umap/commit/e1c346b2b7a20c4f674b12e2d041f1055dcfee77) | lmcinnes |

[See all commits ↗](https://github.com/lmcinnes/umap/commits)

## ⬇️ Get it

```bash
git clone https://github.com/lmcinnes/umap.git
```
