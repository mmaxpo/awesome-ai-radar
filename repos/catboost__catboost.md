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
| 🐞 **Open issues + PRs** | [759](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 4% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2017-07-18 |
| 📦 **Latest release** | [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — 2026-02-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1699.4 MB |
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
| 2026-11-13 | [Take the arm64 Linux tick rate from CNTFRQ_EL0](https://github.com/catboost/catboost/commit/6f7c79340c87e627c66e3f8dc3923a8628359f10) | mironenkovb |
| 2026-11-13 | [Backport IWYU exports in google benchmark header](https://github.com/catboost/catboost/commit/e6bc3a5c2a27c0ec3c8384f386a8edc4f5fc38cf) | vadim-xd |
| 2026-11-13 | [rapidjson, бэкпорт фиксов strtod для kParseFullPrecisionFlag](https://github.com/catboost/catboost/commit/c2deefbaf682be0d129258dcb470666813260e23) | semasazhin |
| 2026-11-12 | [Intermediate changes](https://github.com/catboost/catboost/commit/31148e85b1563179b1b0484bee4095097cddeb03) | robot-piglet |
| 2026-11-12 | [Remove remaining eMudhra roots from certs](https://github.com/catboost/catboost/commit/f19604bb4a118c1cdd24c9f08c3a0da23ee3bd4a) | nik-lucky |
| 2026-11-12 | [переписывать assert тестовых модулей PY3TEST при сборке](https://github.com/catboost/catboost/commit/91e1b726cf715bc675358f7f2404f35b5021c36b) | sovetkin |
| 2026-11-11 | [fix copying instead of moving in some insert methods; better heteroge…](https://github.com/catboost/catboost/commit/8d797fad544091e60e830e0987e00ddf5bc3b411) | ilnurkh |
| 2026-11-10 | [Fix grammar](https://github.com/catboost/catboost/commit/71b27d240154132626088cf3d55aad90b3835296) | andrey-khropov |
| 2026-11-09 | [tokenizers caching](https://github.com/catboost/catboost/commit/b3ec02473f080abcd181b417de36ebcc8f0be8c8) | quezee |
| 2026-11-09 | [передавать исходник и config в rewrite_asserts для pytest 8](https://github.com/catboost/catboost/commit/47c4f4ce445cb58655170d0e6a0c9239b19bab4a) | sovetkin |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
