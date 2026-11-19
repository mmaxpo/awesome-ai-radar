# catboost/catboost

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/catboost/catboost)

> A fast, scalable, high performance Gradient Boosting on Decision Trees library, used for ranking, classification, regression and other machine learning tasks for Python, R, Java, C++. Supports computation on CPU and GPU.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Gradient boosting that handles categorical features well |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 9.2k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [760](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 3% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2017-07-18 |
| 📦 **Latest release** | [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — 2026-02-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1699.7 MB |
| 🌐 **Website** | https://catboost.ai |

## 📦 Recent releases

### [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — Node package release 1.27.0 
<sub>2026-02-21 · 9mo ago</sub>

> (uses `catboostmodel` native libraries from the main CatBoost release v1.2.10)
> * Fix prediction of type `Probability` on CPUs that do not have SSE4 instruction set (that includes all ARM CPUs).
>   Values with probability 0 have been erroneously computed as `nan`.
> * Fix a race condition in error messages in exceptions in multithreaded programs.
> * \[Performance\]\[Windows\] `__SSE__` compiler flag was not enabled for Windows builds with MSVC compiler. This affected code that relied on this flag including quantization during model inference. It is important to note that the compiler itself was configured for SSE support and could still apply automatic SSE optimizations.
> * \[Build\] Switch to Conan 2.x. #2582
> …

### [v1.2.10](https://github.com/catboost/catboost/releases/tag/v1.2.10) — 1.2.10
<sub>2026-02-19 · 9mo ago</sub>

> **New features**
> * \[JVM applier\] Add `predictTransposed` method #2927. Thanks to @levs2001.
> * \[Spark\]: Support Spark 4.0.x and 4.1.x #2946. Thanks to @jdries.

### [v1.2.9](https://github.com/catboost/catboost/releases/tag/v1.2.9) — 1.2.9
<sub>2026-02-18 · 9mo ago</sub>

> > :warning: **There are no JVM artifacts for this release due to issues with publishing.**: They are available in the next release 1.2.10.
> **Major changes**
> * \[Python-package\] Add [`polars`](https://docs.pola.rs/api/python/stable/reference/index.html) input data support. #2524.
>   `Polars` data structures are supported for features, labels and auxiliary data like `weight`, `timestamp` etc.
> **New features**
> * \[R-package\] Make 'predict' an S3 method #1657. Thanks to @david-cortes.
> …

### [v1.2.8](https://github.com/catboost/catboost/releases/tag/v1.2.8) — 1.2.8
<sub>2025-04-13 · 1y ago</sub>

> **Python package**
> * Support Python 3.13 #2748. Thanks to @jeremy010203.
> * Support NumPy 2.x. #2671
> * Drop support for obsolete Python 3.7.
> * Use the proper name of the implementation class as a string id when storing values calculated for custom metrics on GPU. #1792
> * Propagate exceptions from custom metrics code on GPU. #1792
> …

### [node-package-v1.26.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.26.0) — Node package release 1.26.0
<sub>2024-12-07 · 1y ago</sub>

> (uses `catboostmodel` native libraries from the main CatBoost release v1.2.7)
> * Fix MultiClassification models support. #1903
> * Fix predict on GPU. #1901, #1923.
> * Make specifying categorical features parameter optional.
> * Support text and embedding features. #2523
> * Add support for 'MultiProbability' prediction type
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [. Microsoft Visual Studio 2019 C++ build tools versions v14.28 - 16.x…](https://github.com/catboost/catboost/commit/40cbf3862e623b28d72e7b2f33fc6346f5972d76) | andrey-khropov |
| 2026-11-18 | [Intermediate changes](https://github.com/catboost/catboost/commit/8ca2402e60bcd5f5833a1f2f3767b8b2412a9f42) | robot-piglet |
| 2026-11-18 | [StringSplitter: add unittest with split by C-string](https://github.com/catboost/catboost/commit/6a4c439b17c99a4f65aa7fa043fa151e675ca341) | ubyte |
| 2026-11-18 | [preserve directory entries in javac daemon JARs](https://github.com/catboost/catboost/commit/c483c0e2bd63912b3420a58892df0bfb1574352a) | IlyaNiklyaev |
| 2026-11-17 | [fix javac daemon JDK isolation in Larry](https://github.com/catboost/catboost/commit/5c40b22e4a2ad31bfd5d4b9f373798a5c3675025) | IlyaNiklyaev |
| 2026-11-17 | [Document the AUC value when there are no pairs to compare](https://github.com/catboost/catboost/commit/190631e1096afdc5c01ad3ed6ad2d8aabe36f86e) | gopain185 |
| 2026-11-17 | [Fix append-only file access on Windows](https://github.com/catboost/catboost/commit/e20efe9274fbff7d5819c977d7cd2e88deca6070) | ilikepugs |
| 2026-11-17 | [Intermediate changes](https://github.com/catboost/catboost/commit/c732045504234f781c377165b66264c41a48e947) | robot-piglet |
| 2026-11-17 | [Package self-contained Python 3 Cython tool](https://github.com/catboost/catboost/commit/cc0ce40bee61db190a9d1ebc67d442ad5d89862c) | dimdim1177 |
| 2026-11-17 | [Package self-contained Python 2 Cython tool](https://github.com/catboost/catboost/commit/1c963ad239c0a80a466a1ef52e6d5cb4a3aae547) | dimdim1177 |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
