# dmlc/xgboost

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/dmlc/xgboost)

> Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library,  for Python, R, Java, Scala, C and more. Runs on single machine, Hadoop, Spark, Dask, Flink and DataFlow

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Gradient boosting that wins tabular-data competitions |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 29.0k |
| 🍴 **Forks** | 9.0k |
| 🐞 **Open issues + PRs** | [452](https://github.com/dmlc/xgboost/issues) |
| 💻 **Languages** | C++ 46% · Python 21% · Cuda 17% · R 7% · Scala 5% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `gbdt` `gbrt` `gbm` `distributed-systems` `xgboost` `machine-learning` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2014-02-06 |
| 📦 **Latest release** | [v3.3.1](https://github.com/dmlc/xgboost/releases/tag/v3.3.1) — 2026-09-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 38.5 MB |
| 🌐 **Website** | https://xgboost.readthedocs.io/ |

## 📦 Recent releases

### [v3.3.1](https://github.com/dmlc/xgboost/releases/tag/v3.3.1) — 3.3.1 Patch Release
<sub>2026-09-15 · 2mo ago</sub>

> This release is identical to 3.3.0 release, except that it now support Python 3.11.

### [v3.4.2](https://github.com/dmlc/xgboost/releases/tag/v3.4.2) — 3.4.2 Patch Release
<sub>2026-09-15 · 2mo ago</sub>

> This release is identical to 3.4.1 release, except that it now supports Python 3.11.

### [v3.4.1](https://github.com/dmlc/xgboost/releases/tag/v3.4.1) — 3.4.1 Patch Release
<sub>2026-08-15 · 3mo ago</sub>

> **What's Changed**
> * [jvm] Fix batch predict for SparseVector features (#12347)
> *  Fix model slicing with category container. (#12462)
> **Full Changelog**: https://github.com/dmlc/xgboost/compare/v3.4.0...v3.4.1
> **Additional artifacts**
> You can verify the downloaded packages by running the following command on your Unix shell:
> …

### [v3.4.0](https://github.com/dmlc/xgboost/releases/tag/v3.4.0) — Release 3.4.0 stable
<sub>2026-08-04 · 3mo ago</sub>

> **Release notes**
> https://xgboost.readthedocs.io/en/latest/changes/v3.4.0.html
> **Additional artifacts**
> You can verify the downloaded packages by running the following command on your Unix shell:
> ``` sh
> echo "<hash> <artifact>" | shasum -a 256 --check
> …

### [v3.3.0](https://github.com/dmlc/xgboost/releases/tag/v3.3.0) — Release 3.3.0 stable
<sub>2026-06-17 · 5mo ago</sub>

> **Release notes**
> https://xgboost.readthedocs.io/en/latest/changes/v3.3.0.html
> **Additional artifacts:**
> You can verify the downloaded packages by running the following command on your Unix shell:
> ``` sh
> echo "<hash> <artifact>" | shasum -a 256 --check
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Revert "Cap OpenMP threads at the block count in ParallelFor2d (#1280…](https://github.com/dmlc/xgboost/commit/5f1a7cff76753d26299d2a26aab5994c33a06822) | trivialfis |
| 2026-11-17 | [Fix CUDA vector initialization after host shrink (#12840)](https://github.com/dmlc/xgboost/commit/f3b50aec9900dd13d71fd9e60cf1eb09f6c6dd45) | RAMitchell |
| 2026-11-17 | [Bound the Poisson and Cox intercepts away from zero (#12864)](https://github.com/dmlc/xgboost/commit/07179cae3ae2049dc29677874b2a8823193522d3) | caxaxa |
| 2026-11-17 | [[dask] Accept array-like feature weights in DaskDMatrix and the estim…](https://github.com/dmlc/xgboost/commit/aae18e572531e102c974292102692fdd8a0e6dc2) | caxaxa |
| 2026-11-17 | [Walk each row once when predicting from a QuantileDMatrix with missin…](https://github.com/dmlc/xgboost/commit/c95da6d3392981eb48f1d1fb8a76c6c75dd54600) | sebastianbreguel |
| 2026-11-17 | [Bound the Tweedie intercept away from zero (#12848)](https://github.com/dmlc/xgboost/commit/24eeb14c4cad5142b8bd5b36ecda656d76197f64) | caxaxa |
| 2026-11-17 | [Weight queries without relevant documents in ndcg and map (#12833)](https://github.com/dmlc/xgboost/commit/4fb39509a99daed4f360078e8bcce6b1ff00d3c2) | sohailshk |
| 2026-11-17 | [Bump vmactions/freebsd-vm (#12860)](https://github.com/dmlc/xgboost/commit/8242acb60ca4278cfa9f814f1e5ad28fd6168a62) | dependabot[bot] |
| 2026-11-16 | [Fix typos in comments and docstrings (#12605)](https://github.com/dmlc/xgboost/commit/c41b7fc0802a31e3d99890864678a68416dd0ed2) | Nityahapani |
| 2026-11-16 | [Guard max_num_features against 0 and negative values in plot_importan…](https://github.com/dmlc/xgboost/commit/c5b8b3b06a9c99e96b62543c418c05376f2ae486) | Nityahapani |

[See all commits ↗](https://github.com/dmlc/xgboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/dmlc/xgboost.git
```
