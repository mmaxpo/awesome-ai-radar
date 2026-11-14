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
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 26% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1400.1 MB |
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
| 2026-11-14 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/91dd9b0a3662435a109fd5636fc08597eba895f0) | tensorflower-gardener |
| 2026-11-14 | [Integrate LLVM at llvm/llvm-project@de574ff51d4f](https://github.com/tensorflow/tensorflow/commit/3a5226287d65206ae46a4bc5c31fff9bbf83c60b) | nigham |
| 2026-11-14 | [Add MakeSharedCleanup utility in IFRT for shared RAII cleanup.](https://github.com/tensorflow/tensorflow/commit/d51ea3e9d9a822d276f148c256b0a42f708c3efd) | junwhanahn |
| 2026-11-14 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/00694701894fc0f08f6225dfbbf7f77ece22e004) | tensorflower-gardener |
| 2026-11-14 | [Merge pull request #130060 from bodapatisaikrishna:fix/gather-pfor-ne…](https://github.com/tensorflow/tensorflow/commit/5f3f7768e6529d4506bd0cb32d67a375b08bf4dc) | tensorflower-gardener |
| 2026-11-14 | [Give the StableHLO converter C++ entry its own options proto.](https://github.com/tensorflow/tensorflow/commit/4a1fcad16a65b6ebff1528634f55bbf0faa05538) | majiddadashi |
| 2026-11-14 | [Integrate LLVM at llvm/llvm-project@c54ccc6bbe29](https://github.com/tensorflow/tensorflow/commit/ac459e18523f6b3873efe19ea1c52ce5104a09ea) | tensorflower-gardener |
| 2026-11-14 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/ff39a90d22a5cfa24be3954a4685d7e5d3bb1087) | tensorflower-gardener |
| 2026-11-14 | [Support `activation="silu"` (`x / (1 + exp(-x))`) in the XNNPACK CPU …](https://github.com/tensorflow/tensorflow/commit/95bd2218aa600eedc9a29fbb4a6ec53037c21941) | tensorflower-gardener |
| 2026-11-14 | [Update backend layout tiling when sinking host-offload copies.](https://github.com/tensorflow/tensorflow/commit/d8a5e99434b9a2453e8da725978df0d5b8e57016) | tensorflower-gardener |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
