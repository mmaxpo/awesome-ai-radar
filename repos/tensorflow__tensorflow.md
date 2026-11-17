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
| 🍴 **Forks** | 78.0k |
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 26% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1402.8 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · today</sub>

> **Release 2.22.0**
> **TensorFlow**
> **Breaking Changes**
> The TensorBoard dependency is no longer included by default. If you use `tf.summary.*` APIs or `tf.keras.callbacks.TensorBoard`, please install the `tensorboard` package separately (`pip install tensorboard`). Otherwise, TensorFlow will raise an ImportError.
> In `tensorflow/c/experimental/filesystem/filesystem_interface.h`, removed `TF_TransactionToken` and associated APIs.
> **Major Features and Improvements**
> …

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [PR #53153: [ROCM] Refactoring group gemm helper functions](https://github.com/tensorflow/tensorflow/commit/57ad1830fd42a902dd8d03c7a58e9746180f26ab) | pemeliya |
| 2026-11-17 | [[XLA:GPU] Move RunSPMDPasses to GetDefaultCompilationPipeline.](https://github.com/tensorflow/tensorflow/commit/a74c58a70406af22861c4162e5791f195f86ed4c) | mooskagh |
| 2026-11-17 | [[XLA:GPU] Support nested-tuple sub-kernels in horizontal fusion.](https://github.com/tensorflow/tensorflow/commit/6eb14c499fc96ce9e8743a448a012f5f726aeaca) | olegshyshkov |
| 2026-11-17 | [Back all TPUDummyInput outputs with one shared zero buffer.](https://github.com/tensorflow/tensorflow/commit/73a5f7115a922e8fe2b24397c7fd94c2d9208474) | tensorflower-gardener |
| 2026-11-17 | [[XLA:GPU] Snapshot ThunkMetadata and nested CommandBuffer thunks in P…](https://github.com/tensorflow/tensorflow/commit/7530e470a4f4e69943f2d72361458fe2bd69e876) | beckerhe |
| 2026-11-17 | [[XLA] Split flag registration in MakeDebugOptionsFlags into smaller s…](https://github.com/tensorflow/tensorflow/commit/b68e90ecc54b98c645023ef38544ecb8a51c0abd) | shyamliagrawal |
| 2026-11-17 | [Create TPU debugging overview page for openxla.](https://github.com/tensorflow/tensorflow/commit/118b51ab0e3187afaddf7522038fdcea02ab5fa1) | tensorflower-gardener |
| 2026-11-17 | [Fix a ThreadSanitizer timeout race in RpcOpsTest.test_client_timeout …](https://github.com/tensorflow/tensorflow/commit/5182e973469462c0a483356479d3c6bec8475097) | dmiltr3 |
| 2026-11-17 | [Update the TFLite GPU allowlist with new device models.](https://github.com/tensorflow/tensorflow/commit/547f3f03e181a07092d6198578a4b6e3f49b4552) | apaiu-dev |
| 2026-11-17 | [PR #52443: [XLA:GPU] Add support probe and dense fallback for cuDNN r…](https://github.com/tensorflow/tensorflow/commit/cd71766e48d695df4d80b9917c1bd2755a982cda) | Cjkkkk |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
