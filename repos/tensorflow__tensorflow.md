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
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1396.5 MB |
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
| 2026-11-13 | [[XLA:GPU] Use named barrier 1 for single-block phase transitions.](https://github.com/tensorflow/tensorflow/commit/86b3f740733bf0f23e041b7bc1084e20903c4a2f) | thomasjoerg |
| 2026-11-13 | [[XLA:GPU] Make the scatter emitter independent of the updates operand…](https://github.com/tensorflow/tensorflow/commit/37a2faaf1ff33cee66e65de3863c8cae9e04b19f) | pifon2a |
| 2026-11-13 | [PR #46248: Fix collective-permute cycle decomposer for multiple cycles](https://github.com/tensorflow/tensorflow/commit/777e3bf41666e86dd815ee8450a666b3dfbdd7a9) | Ashutosh0x |
| 2026-11-13 | [[XLA:GPU] Rename general, debugging, and Triton autotuner flags.](https://github.com/tensorflow/tensorflow/commit/db6dad0625e38ad2a184336ec65dfa196d8e4f84) | shyamliagrawal |
| 2026-11-13 | [PR #52970: [ROCm] Add noasan notsan filters](https://github.com/tensorflow/tensorflow/commit/5f2620bc8f7f408a7fcff8636e7f7c26e35d153b) | alekstheod |
| 2026-11-13 | [PR #52926: [oneAPI] Build the SYCL backend as C++20 with the glibc 2.…](https://github.com/tensorflow/tensorflow/commit/2915f87885f94c1d90534b2a63d797b5d7797449) | mraunak |
| 2026-11-13 | [PR #50417: [XLA:GPU][oneAPI] Implement complex matmul using oneMKL.](https://github.com/tensorflow/tensorflow/commit/148bc0501cb2520b7b0cf0336af1ce46ec46f65a) | agramesh1 |
| 2026-11-13 | [PR #52201: [XLA:GPU][Triton] Fix collective while-loop command buffer…](https://github.com/tensorflow/tensorflow/commit/026aecd1da3c45f5688c22e5220abbe3619ce639) | mfrancepillois |
| 2026-11-13 | [PR #52604: [XLA:GPU] Refresh the B300 target spec from a live B300](https://github.com/tensorflow/tensorflow/commit/a4228299ab49a8cbcd83200ff1ba1ea5512f43f2) | 0z5a |
| 2026-11-13 | [PR #52104: [ROCm] [CUDA] Keep recorded collectives out of output allo…](https://github.com/tensorflow/tensorflow/commit/98834e2a7a0b46b99873c5e282c0806ddbfe972f) | magaonka-amd |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
