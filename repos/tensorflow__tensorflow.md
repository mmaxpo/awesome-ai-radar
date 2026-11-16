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
| ⭐ **Stars** | 201.6k |
| 🍴 **Forks** | 78.0k |
| 🐞 **Open issues + PRs** | [3.5k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 26% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1401.8 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc0](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc0) — TensorFlow 2.22.0-rc0 _(pre-release)_
<sub>2026-09-24 · 1mo ago</sub>

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

### [v2.19.1](https://github.com/tensorflow/tensorflow/releases/tag/v2.19.1) — TensorFlow 2.19.1
<sub>2025-08-13 · 1y ago</sub>

> **Release 2.19.1**
> **Bug Fixes and Other Changes**
> * Fix save_model.save for Serving embedding and add SparseCore Reshard.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [PR #47758: [XLA] [XLA] Return Unimplemented for non-tuple while state…](https://github.com/tensorflow/tensorflow/commit/a1777076e1ffe33114b9705ed7c8472e7bff5c0b) | kodlan |
| 2026-11-16 | [Pass LLVM library options to Triton TargetMachines through a context](https://github.com/tensorflow/tensorflow/commit/2551f9b66099c4c759aa11cee2bd4bd6ddb647fc) | vwbaker |
| 2026-11-16 | [[XLA] Simplify and speed up region live range analysis in copy removal](https://github.com/tensorflow/tensorflow/commit/516c1810de54b1a8f85897575eb50ee8c51c7203) | blakehechtman |
| 2026-11-16 | [PR #53125: [ROCm] Use specific symbols to version while leaving asan/…](https://github.com/tensorflow/tensorflow/commit/297d31f1f442567f324839d789b38e3db2e33ca9) | alekstheod |
| 2026-11-16 | [Doc formatting cleanup: add blank line before "Inputs:".](https://github.com/tensorflow/tensorflow/commit/e5f8e21a372f498c90428b0e153cb0d26ac3266e) | fergushenderson |
| 2026-11-16 | [Add an AOT compatibility tests and their goldens for the HostExecute …](https://github.com/tensorflow/tensorflow/commit/378935dce52c9bf97231804a2f1e5336910bdcb5) | khasanovaa |
| 2026-11-16 | [[XLA:GPU] Add TestThunkParams helper for thunk unit tests.](https://github.com/tensorflow/tensorflow/commit/35c90b5571c50f593a6f44efb382ddce31311b3e) | sohaibiftikhar |
| 2026-11-16 | [Merge pull request #129801 from somtri:feat-60485-xla-scan-small-ints](https://github.com/tensorflow/tensorflow/commit/c1cffcb1d6d979a14a838250e380292285401dff) | tensorflower-gardener |
| 2026-11-16 | [[Clean Up] Return the load error from HostExecuteStartThunk::Initialize](https://github.com/tensorflow/tensorflow/commit/81ed3331163454b7d4dc2bb65b77e45208525649) | khasanovaa |
| 2026-11-16 | [PR #52906: [XLA] Only rewrite max(a, clamp(a, x, b)) to clamp(a, x, b…](https://github.com/tensorflow/tensorflow/commit/5f55f63f6df0a533357aba8d2bbd4a2903f2dcdb) | Shakhtar-Sankur |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
