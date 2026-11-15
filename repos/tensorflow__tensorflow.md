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
| 🕒 **Last activity** | 2026-11-15 (today) |
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
| 2026-11-15 | [Migrate TFRT IFRT sharding_utils host-buffer holds to std::shared_ptr.](https://github.com/tensorflow/tensorflow/commit/60cd513b82d7bb17f1992a111226221232c36411) | junwhanahn |
| 2026-11-15 | [[IFRT] Migrate Client host-buffer cleanup handles to std::shared_ptr<…](https://github.com/tensorflow/tensorflow/commit/11371bd99b78338d466e2ac9f3db54ae15d9fdf1) | junwhanahn |
| 2026-11-15 | [[IFRT] Return nullopt from Layout::ByteSize for non-fixed-size dtypes…](https://github.com/tensorflow/tensorflow/commit/f83cb027ac866c12dee71220e66752234978d592) | junwhanahn |
| 2026-11-15 | [[IFRT] Expand implementation conformance tests and reject negative sl…](https://github.com/tensorflow/tensorflow/commit/c4b83fe7e06fe639d6e99c9cea5aec7097c3051c) | junwhanahn |
| 2026-11-15 | [Set matching_files_dataset_test to medium size and 7 shards to preven…](https://github.com/tensorflow/tensorflow/commit/9417b73895fc2c9224bdad8f556db4d178bce700) | dmiltr3 |
| 2026-11-15 | [[PjRt-IFRT] Validate host buffer, addressability, and `byte_strides` …](https://github.com/tensorflow/tensorflow/commit/1e50b19dc8d2fdc0ec9fd595b0e36111c46f02f4) | hyeontaek |
| 2026-11-14 | [[PjRt-IFRT] Migrate BasicStringArray::OnDoneWithBuffer to std::shared…](https://github.com/tensorflow/tensorflow/commit/c35bf04829f308e63414087c27c39ff118b617c5) | junwhanahn |
| 2026-11-14 | [In `PartitionConvolutionWithSpatialDimensionHaloExchangeOnLHS`, `Halo…](https://github.com/tensorflow/tensorflow/commit/90336aea18c13d231ad91c3b80ced41393781b43) | SamGinzburg |
| 2026-11-14 | [[tfcompile] Emit direct shared RngState calls in AOT codegen](https://github.com/tensorflow/tensorflow/commit/89799bc471871f47f51a7d33208426b9b5079a53) | majnemer |
| 2026-11-14 | [Avoid redundant XNNPACK weight cache reloads and partition build steps.](https://github.com/tensorflow/tensorflow/commit/1b4ddd1b6442300c1e5760eb4cc95fb4c489c56b) | jdduke |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
