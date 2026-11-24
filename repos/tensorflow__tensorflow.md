# tensorflow/tensorflow

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/tensorflow/tensorflow)

> An Open Source Machine Learning Framework for Everyone

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | Google's end-to-end machine-learning framework |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 201.7k |
| 🍴 **Forks** | 77.4k |
| 🐞 **Open issues + PRs** | [3.5k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1417.1 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 7d ago</sub>

> **Release 2.22.0**
> **TensorFlow**
> **Breaking Changes**
> The TensorBoard dependency is no longer included by default. If you use `tf.summary.*` APIs or `tf.keras.callbacks.TensorBoard`, please install the `tensorboard` package separately (`pip install tensorboard`). Otherwise, TensorFlow will raise an ImportError.
> In `tensorflow/c/experimental/filesystem/filesystem_interface.h`, removed `TF_TransactionToken` and associated APIs.
> **Major Features and Improvements**
> …

### [v2.22.0-rc0](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc0) — TensorFlow 2.22.0-rc0 _(pre-release)_
<sub>2026-09-24 · 2mo ago</sub>

> **Release 2.22.0**
> **TensorFlow**
> **Breaking Changes**
> The TensorBoard dependency is no longer included by default. If you use `tf.summary.*` APIs or `tf.keras.callbacks.TensorBoard`, please install the `tensorboard` package separately (`pip install tensorboard`). Otherwise, TensorFlow will raise an ImportError.
> In `tensorflow/c/experimental/filesystem/filesystem_interface.h`, removed `TF_TransactionToken` and associated APIs.
> **Major Features and Improvements**
> …

### [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — TensorFlow 2.21.0
<sub>2026-03-06 · 8mo ago</sub>

> **Release 2.21.0**
> **TensorFlow**
> **Breaking Changes**
> * Support for Python 3.9 has been removed starting with TF 2.21.
> * The TensorBoard (TB) dependency has been removed starting with TF 2.21.
> **Major Features and Improvements**
> …

### [v2.21.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0-rc1) — TensorFlow 2.21.0-rc1 _(pre-release)_
<sub>2026-03-02 · 8mo ago</sub>

> **Release 2.21.0**
> **TensorFlow**
> **Breaking Changes**
> * Support for Python 3.9 has been removed starting with TF 2.21.
> **Major Features and Improvements**
> * `tf.lite`
> …

### [v2.21.0-rc0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0-rc0) — TensorFlow 2.21.0-rc0 _(pre-release)_
<sub>2026-02-09 · 9mo ago</sub>

> **Release 2.21.0**
> **TensorFlow**
> **Breaking Changes**
> * Support for Python 3.9 has been removed starting with TF 2.21.
> **Major Features and Improvements**
> * `tf.lite`
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [[XLA:GPU] Use a sorted address index in BufferAllocations::FindAlloca…](https://github.com/tensorflow/tensorflow/commit/b3c936a60c42008dd4c612a4779d87cccabc83a2) | PatriosTheGreat |
| 2026-11-24 | [[XLA] Add missing root and control-dependency checks in ConditionalCo…](https://github.com/tensorflow/tensorflow/commit/4590b1667859f2c0643f375d3756b2f3af12012f) | mkuperst |
| 2026-11-24 | [PR #53736: [XLA] Fix special-case copies for a value repeated at seve…](https://github.com/tensorflow/tensorflow/commit/1a0ce4f7095d35905ef1599f392c42e4ba1e8388) | Srivatsan6923 |
| 2026-11-24 | [[XLA:GPU] Enable reduction dimension tiling by default.](https://github.com/tensorflow/tensorflow/commit/99b23e7440d5a8ec2707c24161a268a92844a041) | Moerafaat |
| 2026-11-24 | [[XLA:GPU][NFC] Move GPU HLO transforms to backends/gpu/hlo/transforms](https://github.com/tensorflow/tensorflow/commit/f043705c24ea9944eee04e6d946e8cbd76fa5dbd) | pifon2a |
| 2026-11-24 | [Update XNNPAK in XLA](https://github.com/tensorflow/tensorflow/commit/11354a049bdea7dc28bf79300ff510b686b41633) | Aelphy |
| 2026-11-24 | [PR #53551: [ROCm] Fix __oclc_ISA_version callculation](https://github.com/tensorflow/tensorflow/commit/a30b67cb33ae5ac65a070f94ffdb4334ae33fdcd) | draganmladjenovic |
| 2026-11-24 | [PR #53727: [XLA:GPU][oneAPI] Override platform_comm() on oneCCL backend](https://github.com/tensorflow/tensorflow/commit/9effe9264882cb982c9c9dba313cf1b0e80826f9) | nhatleSummer22 |
| 2026-11-24 | [PR #53791: [ROCm] Update BES results URL in rocm_xla.bazelrc](https://github.com/tensorflow/tensorflow/commit/d1df977efc6210707722490ea29c11251d1e6d6e) | alekstheod |
| 2026-11-24 | [PR #53545: Add skills to update rules_ml_toolchain reference](https://github.com/tensorflow/tensorflow/commit/6af12e91af52c96981a6acf5c92b563ddf140dea) | alekstheod |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
