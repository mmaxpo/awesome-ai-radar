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
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1419.5 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 10d ago</sub>

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
| 2026-11-27 | [[XLA:GPU] Use LaunchDimensions in CustomKernel and FFI kernel registry](https://github.com/tensorflow/tensorflow/commit/ef9795d60f658eb8e172b67b401870bfe1c520fd) | akuegel |
| 2026-11-27 | [[XLA] Add F8E5M3FNU primitive type, literal, and evaluator support.](https://github.com/tensorflow/tensorflow/commit/c6b99e749edaeba1b5e822f6ddf0b97df054c9df) | patrikf |
| 2026-11-27 | [[XLA] Make Mesh(TileAssignment, axes_names) private and use Mesh::Try…](https://github.com/tensorflow/tensorflow/commit/9185d1d6ec183ebe065c502af1f01e1e2103598a) | dimitar-asenov |
| 2026-11-27 | [[XLA] NFC: Clean up explicit pre-C++20 workarounds](https://github.com/tensorflow/tensorflow/commit/7be29f373ca4ae8101a42e51c347a5e9a83a5b33) | chsigg |
| 2026-11-27 | [[XLA] NFC: Use C++20 std::erase and std::erase_if instead of erase-re…](https://github.com/tensorflow/tensorflow/commit/801c7d9fc9f041b4d4b3434210ae6c1bc398b435) | chsigg |
| 2026-11-27 | [[XLA:GPU] Match softmax diamonds with the broadcast on either root op…](https://github.com/tensorflow/tensorflow/commit/f83ab84e8a1d4e13f8a4e03af018840bd01a7874) | Moerafaat |
| 2026-11-27 | [[XLA] NFC: Default operator== and drop operator!= in xla/hlo/analysis](https://github.com/tensorflow/tensorflow/commit/02c6c9e9116c77523cc1bf83d2a70f2d31bec61e) | chsigg |
| 2026-11-27 | [[XLA:GPU] Remove USE_NCCL_HOST_API macro and guards.](https://github.com/tensorflow/tensorflow/commit/bce60c5f054c3dc0b55d22cd9749dcca008a2f99) | PatriosTheGreat |
| 2026-11-27 | [Migrate XLA-internal `xla/backends/autotuner/` users and remove unuse…](https://github.com/tensorflow/tensorflow/commit/42fd6b88d4eb17cae91f64821d2a3b1f2a9cd990) | pifon2a |
| 2026-11-27 | [[XLA:GPU] Accept scalar constant operands in softmax diamonds](https://github.com/tensorflow/tensorflow/commit/91b1c67b37d894d7a3e9565d1a93e813706950c1) | Moerafaat |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
