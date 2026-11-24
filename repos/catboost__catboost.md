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
| 🐞 **Open issues + PRs** | [763](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 3% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2017-07-18 |
| 📦 **Latest release** | [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — 2026-02-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1700.3 MB |
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
| 2026-11-24 | [Bump ajv from 6.12.6 to 6.15.0 in /catboost/python-package/catboost/w…](https://github.com/catboost/catboost/commit/289312d23d063a2c0dbfff166ab4ea47c883c96e) | dependabot[bot] [49699333+dependabot |
| 2026-11-24 | [some avoiding copy optimizations](https://github.com/catboost/catboost/commit/c4e49bcae7c0ffcec51d4d503fdc03317ca79022) | ilnurkh |
| 2026-11-24 | [Bump fast-uri from 3.1.7 to 3.1.9 in /catboost/python-package/catboos…](https://github.com/catboost/catboost/commit/b4310b26fb7ce5a08b08cf1b2bb2674dc89fc1be) | dependabot[bot] [49699333+dependabot |
| 2026-11-24 | [Enable Cython resources by default](https://github.com/catboost/catboost/commit/5d13e30a02830d26be0320a521c403685a250d00) | dimdim1177 |
| 2026-11-23 | [Use Pool group weights in CatBoostRanker.score](https://github.com/catboost/catboost/commit/31efad70f9c57c64bb20273f23286b4e8026b2dd) | ViderStar |
| 2026-11-23 | [Python 3.14 in now installed by default on windows-2022 images.](https://github.com/catboost/catboost/commit/7778f73acb2207dd93842dbd31a3ad749fcf9bae) | andrey-khropov |
| 2026-11-23 | [Use cheaper memory ordering in library/cpp/par](https://github.com/catboost/catboost/commit/a12f377e0b5a1f5b1a426ad5a26a34764b0b2289) | georgthegreat |
| 2026-11-23 | [migrate some libs to std::atomic](https://github.com/catboost/catboost/commit/defa8794294a0f73a8f5714e14187c3d9b02f3a5) | tobo |
| 2026-11-23 | [Intermediate changes](https://github.com/catboost/catboost/commit/0e82d2f6000f19aa58f1b18c437fac74479c60db) | robot-piglet |
| 2026-11-23 | [Intermediate changes](https://github.com/catboost/catboost/commit/05014682a5b96af2c71fea1b1259cdbab2529a3c) | robot-piglet |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
