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
| 🐞 **Open issues + PRs** | [453](https://github.com/dmlc/xgboost/issues) |
| 💻 **Languages** | C++ 46% · Python 21% · Cuda 17% · R 7% · Scala 5% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `gbdt` `gbrt` `gbm` `distributed-systems` `xgboost` `machine-learning` |
| 🕒 **Last activity** | 2026-11-11 (yesterday) |
| 📅 **Created** | 2014-02-06 |
| 📦 **Latest release** | [v3.3.1](https://github.com/dmlc/xgboost/releases/tag/v3.3.1) — 2026-09-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 38.5 MB |
| 🌐 **Website** | https://xgboost.readthedocs.io/ |

## 📦 Recent releases

### [v3.3.1](https://github.com/dmlc/xgboost/releases/tag/v3.3.1) — 3.3.1 Patch Release
<sub>2026-09-15 · 1mo ago</sub>

> This release is identical to 3.3.0 release, except that it now support Python 3.11.

### [v3.4.2](https://github.com/dmlc/xgboost/releases/tag/v3.4.2) — 3.4.2 Patch Release
<sub>2026-09-15 · 1mo ago</sub>

> This release is identical to 3.4.1 release, except that it now supports Python 3.11.

### [v3.4.1](https://github.com/dmlc/xgboost/releases/tag/v3.4.1) — 3.4.1 Patch Release
<sub>2026-08-15 · 2mo ago</sub>

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
<sub>2026-06-17 · 4mo ago</sub>

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
| 2026-11-11 | [Skip unused features in GPU SHAP interaction finalization (#12825)](https://github.com/dmlc/xgboost/commit/293cad1a89ab749e3266e190c68118af2db09982) | RAMitchell |
| 2026-11-10 | [Only zero and accumulate split-feature columns in CPU SHAP contributi…](https://github.com/dmlc/xgboost/commit/889205cb8e4d779ba50f79da406020f04f6a04a1) | sebastianbreguel |
| 2026-11-10 | [Use fewer threads for small multiclass prediction transforms (#12821)](https://github.com/dmlc/xgboost/commit/e15fb94fccc2341233c51b5c7a4df4389cdeda9e) | sebastianbreguel |
| 2026-11-10 | [Sort only partition-based categorical histogram segments on GPU (#12723)](https://github.com/dmlc/xgboost/commit/5a67748d59fdb919ac834b86f030a48999a2b885) | siqi-he |
| 2026-11-09 | [Run elementwise prediction transforms in blocks of rows (#12819)](https://github.com/dmlc/xgboost/commit/b6e36234ea28926d9b8d9776e0795cebef281070) | sebastianbreguel |
| 2026-11-09 | [[python] Dedupe training callbacks by identity so an unhashable callb…](https://github.com/dmlc/xgboost/commit/c0ed8b34f97d735ec63a537814ed0e7ae3ce3b5b) | paolo-perrone |
| 2026-11-09 | [[python] Iterate pandas columns with items() instead of a name lookup…](https://github.com/dmlc/xgboost/commit/7b41d9c363be560f43a68538cd6566cccb7c39df) | sebastianbreguel |
| 2026-11-09 | [Keep the global configuration unchanged when an update is rejected (#…](https://github.com/dmlc/xgboost/commit/e4ed53962e69c4008512a7de62765ebbfb16db66) | rishi02102017 |
| 2026-11-07 | [Push a batch with no more threads than rows (#12816)](https://github.com/dmlc/xgboost/commit/c43256076009bcf25669c0de119d52fecd510751) | sebastianbreguel |
| 2026-11-06 | [Align the GPU monotone constraint implementation to the CPU. (#12809)](https://github.com/dmlc/xgboost/commit/1f95e05447ba3e7a2722fbbfb571ead6d078e3ee) | trivialfis |

[See all commits ↗](https://github.com/dmlc/xgboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/dmlc/xgboost.git
```
