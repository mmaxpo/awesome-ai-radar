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
| 🐞 **Open issues + PRs** | [754](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 4% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2017-07-18 |
| 📦 **Latest release** | [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — 2026-02-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1699.5 MB |
| 🌐 **Website** | https://catboost.ai |

## 📦 Recent releases

### [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — Node package release 1.27.0 
<sub>2026-02-21 · 8mo ago</sub>

> (uses `catboostmodel` native libraries from the main CatBoost release v1.2.10)
> * Fix prediction of type `Probability` on CPUs that do not have SSE4 instruction set (that includes all ARM CPUs).
>   Values with probability 0 have been erroneously computed as `nan`.
> * Fix a race condition in error messages in exceptions in multithreaded programs.
> * \[Performance\]\[Windows\] `__SSE__` compiler flag was not enabled for Windows builds with MSVC compiler. This affected code that relied on this flag including quantization during model inference. It is important to note that the compiler itself was configured for SSE support and could still apply automatic SSE optimizations.
> * \[Build\] Switch to Conan 2.x. #2582
> …

### [v1.2.10](https://github.com/catboost/catboost/releases/tag/v1.2.10) — 1.2.10
<sub>2026-02-19 · 8mo ago</sub>

> **New features**
> * \[JVM applier\] Add `predictTransposed` method #2927. Thanks to @levs2001.
> * \[Spark\]: Support Spark 4.0.x and 4.1.x #2946. Thanks to @jdries.

### [v1.2.9](https://github.com/catboost/catboost/releases/tag/v1.2.9) — 1.2.9
<sub>2026-02-18 · 8mo ago</sub>

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
| 2026-11-14 | [Skip redundant chmod on cached executables](https://github.com/catboost/catboost/commit/bd7076faf5ec41c3bcf31982b770ab508f4d3063) | bgaifullin |
| 2026-11-14 | [Direct learn features indexing for an unshuffled fold](https://github.com/catboost/catboost/commit/8aa4f90084a99ac50a8d0dbb7f44a47b05b5d287) | ArseniyVarlamov |
| 2026-11-14 | [Do not mutate the caller's feature_tags in Pool](https://github.com/catboost/catboost/commit/ce149380154d7ad39dc715f06ae79ba1e0c8cccb) | davrens101 |
| 2026-11-14 | [Fix classifier score for single-column labels](https://github.com/catboost/catboost/commit/0a8d91fee6d4209a215f5319b400d8516b91a5fe) | parlorsky |
| 2026-11-14 | [Fix PEP8 issues in GPU vs CPU benchmark scripts (#3239)](https://github.com/catboost/catboost/commit/de00cae234a97bc1aad8ac81817accb072432de0) | nysib |
| 2026-11-13 | [Fix grammar](https://github.com/catboost/catboost/commit/f8a251bb1f61d80dc515affcf5534a36b512c49b) | andrey-khropov |
| 2026-11-13 | [Bump scikit-learn from 0.23.1 to 1.5.0 in /catboost/benchmarks/traini…](https://github.com/catboost/catboost/commit/57ac3928271a0c611464c5f21a9a2ce07e2c7681) | dependabot[bot] [49699333+dependabot |
| 2026-11-13 | [Import pyroscope-io 1.4.0 from source](https://github.com/catboost/catboost/commit/dedc903d5ac3012834258ff18bb58f9010a19f21) | serjflint |
| 2026-11-13 | [heterogeneous lookups fixes for TMap](https://github.com/catboost/catboost/commit/bdd1a257932981e597546bf5789d4e400294a4f1) | ilnurkh |
| 2026-11-13 | [Take the arm64 Linux tick rate from CNTFRQ_EL0](https://github.com/catboost/catboost/commit/6f7c79340c87e627c66e3f8dc3923a8628359f10) | mironenkovb |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
