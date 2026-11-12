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
| 🍴 **Forks** | 77.9k |
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 26% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1397.2 MB |
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
| 2026-11-12 | [[XLA] Reject shardings with more last_tile_dims than tile assignment …](https://github.com/tensorflow/tensorflow/commit/05b250351b59b6cfc41724f9de1ea3d8b5161b31) | dimitar-asenov |
| 2026-11-12 | [[XLA:GPU] Migrate Triton collectives to explicit xtile.entry_func arg…](https://github.com/tensorflow/tensorflow/commit/2972cd0b2c77136e4cc95ad5f523877e651a4d67) | sohaibiftikhar |
| 2026-11-12 | [Merge pull request #128930 from teerthsharma:tf-nms-total-order](https://github.com/tensorflow/tensorflow/commit/d409fa6849055593a16410187b6344d2dfe24ed6) | tensorflower-gardener |
| 2026-11-12 | [Remove deprecated PjRtDevice::id() from PjRtDevice.](https://github.com/tensorflow/tensorflow/commit/f403da29162d16ab17e9d6d3a02855325420c66a) | ilya-biryukov |
| 2026-11-12 | [PR #52698: [XLA:TSL] Reject negative byte counts in SnappyInputStream](https://github.com/tensorflow/tensorflow/commit/d9a9a36f22f4f2f89f22b9b572d5c43ab7697004) | professor-moody |
| 2026-11-12 | [[XLA:GPU] Handle root GemmFusion outputs like any other output.](https://github.com/tensorflow/tensorflow/commit/7ea63e4d5a4588e033e51beb2f8e1b6da319fe10) | vwbaker |
| 2026-11-12 | [[XLA] Bounds-check table lookup indices in collective_opt_utils](https://github.com/tensorflow/tensorflow/commit/1235e274983c9d1781d4abb88b6c66bb93b2fd58) | dimitar-asenov |
| 2026-11-12 | [PR #52787: [XLA:TSL] Reject negative byte counts in SnappyInputBuffer](https://github.com/tensorflow/tensorflow/commit/a169e8d63cdef6714f92da5f24245b158ac60be2) | professor-moody |
| 2026-11-12 | [PR #52704: Fix nan checker assert on modules that return tuple](https://github.com/tensorflow/tensorflow/commit/0bef8595d6fce35424031cb6cf20700eec49f9fb) | draganmladjenovic |
| 2026-11-12 | [Add unit tests to show non-flat support on HostOffloadingPrepare with…](https://github.com/tensorflow/tensorflow/commit/c2e3e2749aadaac45f7299ffb3648d21fde877ec) | ekayaaslan |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
