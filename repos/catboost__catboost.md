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
| 🐞 **Open issues + PRs** | [758](https://github.com/catboost/catboost/issues) |
| 💻 **Languages** | C++ 78% · Python 11% · Cuda 4% · CMake 3% · Scala 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `machine-learning` `decision-trees` `gradient-boosting` `gbm` `gbdt` `python` `r` `kaggle` `gpu-computing` `catboost` `tutorial` `categorical-features` `gpu` `coreml` `data-science` `big-data` `cuda` `data-mining` |
| 🕒 **Last activity** | 2026-11-10 (today) |
| 📅 **Created** | 2017-07-18 |
| 📦 **Latest release** | [node-package-v1.27.0](https://github.com/catboost/catboost/releases/tag/node-package-v1.27.0) — 2026-02-21 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1699.3 MB |
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
| 2026-11-10 | [Fix grammar](https://github.com/catboost/catboost/commit/71b27d240154132626088cf3d55aad90b3835296) | andrey-khropov |
| 2026-11-09 | [tokenizers caching](https://github.com/catboost/catboost/commit/b3ec02473f080abcd181b417de36ebcc8f0be8c8) | quezee |
| 2026-11-09 | [передавать исходник и config в rewrite_asserts для pytest 8](https://github.com/catboost/catboost/commit/47c4f4ce445cb58655170d0e6a0c9239b19bab4a) | sovetkin |
| 2026-11-09 | [Link Windows Rust build scripts and proc macros with a static CRT](https://github.com/catboost/catboost/commit/afa7715b1d0c29538a6d9338e87e49a54fd589ab) | 4JustMe4 |
| 2026-11-07 | [Revert commit rXXXXXX, YT-30299: Shared[Mutable]Ref from blob shrinks](https://github.com/catboost/catboost/commit/e2a715beaa2f13c1c798be9a9e8349fb434b1c44) | babenko |
| 2026-11-06 | [статическая таблица python-ресурсов вместо py3cc и конструкторов](https://github.com/catboost/catboost/commit/b1a76758ed68590d895f288dabf3f72751dd3d60) | pg |
| 2026-11-06 | [YT-30299: Shared[Mutable]Ref from blob shrinks](https://github.com/catboost/catboost/commit/e73afeb0dcebf1ec3a5e34d46e01ad07f68f19a6) | sabdenovch |
| 2026-11-06 | [Update contrib/restricted/google/benchmark to 1.10.0](https://github.com/catboost/catboost/commit/08b97dbb24b28fa1b261577e5006a6fd00d3bef3) | georgthegreat |
| 2026-11-06 | [Remove obsolete rseq CPU-id helpers](https://github.com/catboost/catboost/commit/fdc0557846126bd41978c9550f07f2b376486602) | yuri-pechatnov |
| 2026-11-05 | [neh: IHttpRequest::DisableCompression() for http2 lets a handler send…](https://github.com/catboost/catboost/commit/5686f8c6cc9def4b0df343488d2f887ec5609d1f) | trofimenkov |

[See all commits ↗](https://github.com/catboost/catboost/commits)

## ⬇️ Get it

```bash
git clone https://github.com/catboost/catboost.git
```
