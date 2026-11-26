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
| ⭐ **Stars** | 201.9k |
| 🍴 **Forks** | 77.4k |
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1418.9 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 9d ago</sub>

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
| 2026-11-26 | [PR #53709: [XLA:GPU] Fix copy insertion to add the correct parallel t…](https://github.com/tensorflow/tensorflow/commit/474c5b85e8f029293246296185105e36eb54b366) | Tixxx |
| 2026-11-26 | [[XLA:GPU] Allow reverse scans in Triton.](https://github.com/tensorflow/tensorflow/commit/921846ca23aab896f64107772e80b6b8f88c103c) | chsigg |
| 2026-11-26 | [[XLA:GPU] Plumb AllGatherStrategy and tile-size guard in BuildAllGath…](https://github.com/tensorflow/tensorflow/commit/03620cc386fb2fed53e5a8148439d08223440a60) | sohaibiftikhar |
| 2026-11-26 | [[XLA:XTile] Handle equal-bitwidth integer converts in LowerStablehloT…](https://github.com/tensorflow/tensorflow/commit/83fa0adc32fb87308f64c357d3442a1b0c10b187) | pifon2a |
| 2026-11-26 | [PR #53963: [ROCm] Add minimal debug info for tsan builds](https://github.com/tensorflow/tensorflow/commit/02c69b0f4064f1652f0744245f22dcf6dcd38823) | alekstheod |
| 2026-11-26 | [PR #49692: [xla:gpu] Cancel in-progress GPU clique init on task failure](https://github.com/tensorflow/tensorflow/commit/14fe3fd2a7da72540869568c309f5d54f02d9be4) | Liauuu |
| 2026-11-26 | [PR #53920: [ROCm] Fix TSAN data race in RecoverExp2Pattern static log…](https://github.com/tensorflow/tensorflow/commit/0c8f1929a783751c2a99fbf65c1e45fe4406b5a5) | alekstheod |
| 2026-11-26 | [Fix dropdown display in Megascale debugging guide.](https://github.com/tensorflow/tensorflow/commit/0fe579af89373e0037cd36bd4f217bc9fbf47040) | tensorflower-gardener |
| 2026-11-26 | [Move autotuner directories under backends/core, cpu/core, and gpu/core](https://github.com/tensorflow/tensorflow/commit/58c1fd0334441a63082f7eb84cc71a4c54bd3c86) | pifon2a |
| 2026-11-26 | [[XLA] Return errors from replica group list FromProto](https://github.com/tensorflow/tensorflow/commit/7f4b76e26c1fcec0ad8e9756d1976015b55f8f76) | dimitar-asenov |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
