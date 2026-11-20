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
| 🐞 **Open issues + PRs** | [3.5k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1411.6 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 3d ago</sub>

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
| 2026-11-20 | [[XLA:GPU] Cap small-input loop unrolling at a single thread block.](https://github.com/tensorflow/tensorflow/commit/cdc1a0a6718f4a8c9e9ce4d830cd06eeb24ad955) | thomasjoerg |
| 2026-11-20 | [[XLA:GPU] Support slices in CuDnnGemmDimensions.](https://github.com/tensorflow/tensorflow/commit/db5e704598a172f5c05746a629385fe73de7b79e) | vwbaker |
| 2026-11-20 | [[XLA:GPU] Track explicit setting of xla_gpu_default_to_alg_dot_bf16_b…](https://github.com/tensorflow/tensorflow/commit/1759502b6388c9bef9421db1386272ee8f94a4ae) | loislo |
| 2026-11-20 | [[PJRT] Speed up small-dimension deinterleave with Highway.](https://github.com/tensorflow/tensorflow/commit/6e6fab69a84447f6591580031dd443963777d9a3) | hawkinsp |
| 2026-11-20 | [[XLA:Codegen] Emit SelectBufferOp on root InsertTileOp for per-peer o…](https://github.com/tensorflow/tensorflow/commit/fb8042a0d446b999dad5448cf0713e0c21e03155) | sohaibiftikhar |
| 2026-11-20 | [Add unit tests to show non-flat support on AsyncComputeOnRewriter.](https://github.com/tensorflow/tensorflow/commit/827ddce4c6daa95a92d5bd36bea3b07a190b782e) | ekayaaslan |
| 2026-11-20 | [[XLA:GPU] Raise Triton reduce-scatter max blocks per grid from 64 to 128](https://github.com/tensorflow/tensorflow/commit/ea4467ee2fbe1a2a027249c40e1b8fae78a8e176) | PatriosTheGreat |
| 2026-11-20 | [PR #53379: [XLA:GPU] Enable portable large VMM regression coverage](https://github.com/tensorflow/tensorflow/commit/26741371466f9d40c9c378f1f843c03c282dff32) | nouiz |
| 2026-11-20 | [[XLA:GPU] Add clique-level release of cached symmetric memory.](https://github.com/tensorflow/tensorflow/commit/60910b113e86ae70b487672309d283cf6dbc187c) | PatriosTheGreat |
| 2026-11-20 | [[IFRT] Validate non-negative dimensions and element-count bounds in `…](https://github.com/tensorflow/tensorflow/commit/d25591368286056170e91ac1764547cde19157c1) | hyeontaek |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
