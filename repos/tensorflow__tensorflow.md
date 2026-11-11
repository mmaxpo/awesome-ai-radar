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
| ⭐ **Stars** | 201.5k |
| 🍴 **Forks** | 77.9k |
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 26% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1396.0 MB |
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
| 2026-11-11 | [PR #52764: Bump lit from 23.1.4 to 23.1.5](https://github.com/tensorflow/tensorflow/commit/4991dc2c8a331c0be026fe6af9acd6e785608ca3) | dependabot[bot] |
| 2026-11-11 | [PR #52763: Bump github/codeql-action/upload-sarif from 4.39.1 to 4.39.3](https://github.com/tensorflow/tensorflow/commit/2284229d9e65d0ebc249c228bec7f9049846d7c2) | dependabot[bot] |
| 2026-11-11 | [PR #52782: [ROCm] Fix flaky MarkerCapturing tests due to a mixture of…](https://github.com/tensorflow/tensorflow/commit/5cf66ab106a9f9d3ea62aef1c83d3cbe9edf7430) | alekstheod |
| 2026-11-11 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/0f629522cc7cea8465d92424a26063b9e18ec820) | tensorflower-gardener |
| 2026-11-11 | [[XLA] Enable libunwind per-FDE EH frame registration on Linux libc++ …](https://github.com/tensorflow/tensorflow/commit/c4a67b1d07fddd34a357d48dd21fa9ab34d1ba26) | tensorflower-gardener |
| 2026-11-11 | [[XLA:GPU] Update RaggedAllToAll AOT compatibility goldens for fabric_…](https://github.com/tensorflow/tensorflow/commit/c354de8fe58f5424ad8ae736065f5a1013701ffc) | sohaibiftikhar |
| 2026-11-11 | [Delete the internal-only XProf forwarding targets from `tensorflow/co…](https://github.com/tensorflow/tensorflow/commit/03ff4b8100583f5ad0864cb5fda84db20029bf5e) | chsigg |
| 2026-11-11 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/16098ca6524b13d267c5a2fa329d22a13e26b6ca) | tensorflower-gardener |
| 2026-11-11 | [PR #52746: [XLA:GPU][oneAPI] Align XPU Triton hook with upstream LLVM](https://github.com/tensorflow/tensorflow/commit/694de9638506b3d3e719592a9d4a85651c597093) | akhilgoe |
| 2026-11-11 | [PR #52508: Skip main-thread async computations from layout normalization](https://github.com/tensorflow/tensorflow/commit/175b20ce65c269258939e92581ebe8700a21b22a) | rao-ashish |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
