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
| 🍴 **Forks** | 897 |
| 🐞 **Open issues + PRs** | [542](https://github.com/lmcinnes/umap/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `umap` `dimensionality-reduction` `visualization` `machine-learning` `topological-data-analysis` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2017-07-02 |
| 📦 **Latest release** | [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0) — 2026-11-10 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 106.3 MB |
| 🌐 **Website** | https://umap-learn.readthedocs.io |

## 📦 Recent releases

### [release-0.6.0](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0)
<sub>2026-11-10 · 11d ago</sub>

> **What's Changed**
> * Embed combined models without densMAP instead of failing with KeyError by @raashish1601 in https://github.com/lmcinnes/umap/pull/1304
> * Read neighbours straight from the CSR arrays in breadth_first_search() by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1326
> * Initialise new points in update() from the same neighbours as the graph by @sebastianbreguel in https://github.com/lmcinnes/umap/pull/1325
> * Allow plot.show() to display interactive plots with search by @Don-Yin in https://github.com/lmcinnes/umap/pull/1321
> * 0.6.0 release version by @lmcinnes in https://github.com/lmcinnes/umap/pull/1333
> …

### [release-0.6.0rc1](https://github.com/lmcinnes/umap/releases/tag/release-0.6.0rc1) _(pre-release)_
<sub>2026-11-03 · 17d ago</sub>

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
| 2026-11-19 | [Merge pull request #1353 from atishay-kasliwal/fix/parametric-cross-e…](https://github.com/lmcinnes/umap/commit/2157d26cefabb832e27cc66637a7b9d4e4b33f98) | lmcinnes |
| 2026-11-18 | [Merge pull request #1340 from akshatvishu/fix-precomputed-knn](https://github.com/lmcinnes/umap/commit/971cdeacc5a0b97c01fee91d4c04bcd24794fbd5) | lmcinnes |
| 2026-11-18 | [Merge pull request #1358 from sebastianbreguel/perf/sparse-precompute…](https://github.com/lmcinnes/umap/commit/299cdb87b19ae9d7e6a8452825904f9bc8b1480f) | lmcinnes |
| 2026-11-18 | [Merge pull request #1356 from phunterlau/codex/l9-adam-repulsion](https://github.com/lmcinnes/umap/commit/9db54054ad51844969b9fa1f6838a1f9bd396efb) | lmcinnes |
| 2026-11-18 | [Slice CSR arrays directly in the sparse precomputed kNN loop of fit](https://github.com/lmcinnes/umap/commit/3441ab7b3c1f532ec6eee2b3060354bbff2297cc) | sebastianbreguel |
| 2026-11-18 | [Accelerate 2D Adam repulsion with radial lookup](https://github.com/lmcinnes/umap/commit/b89f8410e367c82f79cec6e15a6346756f1be6d1) | phunterlau |
| 2026-11-18 | [Merge pull request #1355 from sebastianbreguel/fix-n-jobs-above-numba…](https://github.com/lmcinnes/umap/commit/1f7553b2d8dc54aaa2224da92b5869a3f0c91576) | lmcinnes |
| 2026-11-18 | [Cap n_jobs at the numba thread pool size (fixes #1354)](https://github.com/lmcinnes/umap/commit/447aef08d71ad1048d7b8c2c962f61f2eb48b8f4) | sebastianbreguel |
| 2026-11-18 | [Add test: fit with n_jobs above the numba thread count](https://github.com/lmcinnes/umap/commit/e5cf1995deae944855919b6c5d8771d0679cca58) | sebastianbreguel |
| 2026-11-17 | [Fix parametric UMAP cross entropy for log probabilities](https://github.com/lmcinnes/umap/commit/295981d62154a4dc9d9a1a0ee87ed50e22b19c34) | atishay-kasliwal |

[See all commits ↗](https://github.com/lmcinnes/umap/commits)

## ⬇️ Get it

```bash
git clone https://github.com/lmcinnes/umap.git
```
