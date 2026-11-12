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
| 🍴 **Forks** | 886 |
| 🐞 **Open issues + PRs** | [543](https://github.com/lmcinnes/umap/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `umap` `dimensionality-reduction` `visualization` `machine-learning` `topological-data-analysis` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2017-07-02 |
| 📦 **Latest release** | [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0) — 2026-11-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 100.6 MB |
| 🌐 **Website** | https://umap-learn.readthedocs.io |

## 📦 Recent releases

### [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0)
<sub>2026-11-10 · 2d ago</sub>

> **What's Changed**
> * Embed combined models without densMAP instead of failing with KeyError by @raashish1601 in https://github.com/lmcinnes/umap/pull/1304
> * Read neighbours straight from the CSR arrays in breadth_first_search() by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1326
> * Initialise new points in update() from the same neighbours as the graph by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1325
> * Allow plot.show() to display interactive plots with search by @Don-Yin in https://github.com/lmcinnes/umap/pull/1321
> * 0.6.0 release version by @lmcinnes in https://github.com/lmcinnes/umap/pull/1333
> …

### [release-0.6.0rc1](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0rc1) _(pre-release)_
<sub>2026-11-03 · 8d ago</sub>

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
| 2026-11-11 | [Merge pull request #1338 from AnaseDouramane/fix-recursive-init-n-com…](https://github.com/lmcinnes/umap/commit/8c925ee2b2a0b8425d4a240dfbfb91eadec43c93) | lmcinnes |
| 2026-11-11 | [Merge pull request #1337 from jan-glx/fix-contiguous-knn-dists](https://github.com/lmcinnes/umap/commit/e1c346b2b7a20c4f674b12e2d041f1055dcfee77) | lmcinnes |
| 2026-11-11 | [Pad recursive-init anchor to n_components when PCA yields fewer axes](https://github.com/lmcinnes/umap/commit/f64a423996333e8e9b7707a1b3461d4c603f69b0) | AnaseDouramane |
| 2026-11-11 | [Make knn_dists contiguous in fuzzy_simplicial_set](https://github.com/lmcinnes/umap/commit/aa856d586df2cbcb6dffe52775943fb8a51856f8) | jan-glx |
| 2026-11-10 | [Merge pull request #1333 from lmcinnes/0.6release](https://github.com/lmcinnes/umap/commit/ede8827bc0926663a463629c85fb2063fa9e8dd1) | lmcinnes |
| 2026-11-10 | [Update version to 0.6.0 for release](https://github.com/lmcinnes/umap/commit/c6bf4afaae330e4f1d6baea7bedef05a997ad3d7) | lmcinnes |
| 2026-11-09 | [Merge pull request #1321 from Don-Yin/fix-show-search-layout](https://github.com/lmcinnes/umap/commit/da683537395bedc00ef254b836eadb9e81f4c360) | lmcinnes |
| 2026-11-09 | [Merge pull request #1325 from sebastianbreguel/perf/update-fast-knn-i…](https://github.com/lmcinnes/umap/commit/508a59b65f47db001705284cf80f2aac8dc0836c) | lmcinnes |
| 2026-11-09 | [Merge remote-tracking branch 'origin/master' into perf/update-fast-kn…](https://github.com/lmcinnes/umap/commit/309d51980af90d00d50ae999ade52d6e7e1a15e6) | sebastianbreguel |
| 2026-11-06 | [Merge pull request #1326 from sebastianbreguel/perf/bfs-csr-neighbors](https://github.com/lmcinnes/umap/commit/241e492966d013bce20a54858441f94449fb3553) | lmcinnes |

[See all commits ↗](https://github.com/lmcinnes/umap/commits)

## ⬇️ Get it

```bash
git clone https://github.com/lmcinnes/umap.git
```
