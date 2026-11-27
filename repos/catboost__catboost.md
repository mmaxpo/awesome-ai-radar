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
| 🐞 **Open issues + PRs** | [768](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 3% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-27 (today) |
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
| 2026-11-27 | [Intermediate changes](https://github.com/catboost/catboost/commit/22d79a902730de99f1b9a27a6f25d2f4aae7229b) | robot-piglet |
| 2026-11-27 | [do not use exceptions in neh in relativly hot path (keep-alive drop f…](https://github.com/catboost/catboost/commit/3d7cf00dd132f3b143c83415bb0b64ce5e0cd733) | ilnurkh |
| 2026-11-27 | [add TFloatStringBuf; make ToString for floats have adaptive compile-t…](https://github.com/catboost/catboost/commit/5383aa06f1b788cd210afa23aee7565420a8b4ad) | ilnurkh |
| 2026-11-26 | [добавление HTTP-заголовков при запуске d-executor](https://github.com/catboost/catboost/commit/37af7368ad550f49c653de5da40f91e28b5d11ab) | arsenoks4132 |
| 2026-11-26 | [Preserve UTF-8 Windows command lines and directory names](https://github.com/catboost/catboost/commit/179863d6b4a4cf6af1409f52540cc188623b312f) | 4JustMe4 |
| 2026-11-26 | [обновить contrib/restricted/exiv2 до 0.28.9](https://github.com/catboost/catboost/commit/3b6b97ebe7d200baba091e6a13d153e4aade346f) | everest |
| 2026-11-26 | [ability to pass some additional info about codecs; chunked output for…](https://github.com/catboost/catboost/commit/3dd74905124571ba3ca69d43f355ff14c0099600) | ilnurkh |
| 2026-11-26 | [Update OpenSSL for open source CatBoost to 3.5.9.](https://github.com/catboost/catboost/commit/ea9a3e518902ab52ec12d85ad03e5c3f7f100802) | andrey-khropov |
| 2026-11-25 | [support command files in stage0pycc bootstrap](https://github.com/catboost/catboost/commit/09d3085c6abd12d153de62e52726756fee7735d0) | 4JustMe4 |
| 2026-11-25 | [Fix shared headers for clang-cl](https://github.com/catboost/catboost/commit/b567549bf456de09ad8e7118b8f521d316a4256d) | shfdis |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
