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
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1407.4 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · yesterday</sub>

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
| 2026-11-18 | [[PjRt-IFRT] Validate HloSharding invariants in HloShardingSpec](https://github.com/tensorflow/tensorflow/commit/1fb8340c1f4060f7fea7e3b723553329866cc1b5) | dimitar-asenov |
| 2026-11-18 | [[XLA:GPU] Add non-fatal `--xla_gpu_[device_]execution_warn_stuck_time…](https://github.com/tensorflow/tensorflow/commit/dc52dd6fc694503dea4d76d3953fe89814d65e6e) | beckerhe |
| 2026-11-18 | [[XLA:CPU] Lower 0-D dot_general through vector.contract.](https://github.com/tensorflow/tensorflow/commit/72403ed8a60911e673bee1acdc20adb235ba70dd) | pifon2a |
| 2026-11-18 | [[XLA:SDY] Add need replication sharding rule for EighTpu custom call](https://github.com/tensorflow/tensorflow/commit/6cc19738169971dbf5053177141ed99f36e93ebd) | SamGinzburg |
| 2026-11-18 | [Migrate XLA call sites to the direct `HloInstruction` frontend attrib…](https://github.com/tensorflow/tensorflow/commit/a035eab92b628443ba4aedf540ea101e83a9cc18) | toli-y |
| 2026-11-18 | [[XLA:GPU] Import cuda-tile v13.5.0 (25732e3308abd43c0aa9007a7b3b01259…](https://github.com/tensorflow/tensorflow/commit/a0133b8decfe74e5c8caca9b5843abad9dacdc50) | chsigg |
| 2026-11-18 | [[XLA:SPMD] Align permuted contracting shardings in windowed dot](https://github.com/tensorflow/tensorflow/commit/6647fb43ff626b9b66468e4703b311978157a2c1) | SamGinzburg |
| 2026-11-18 | [[XLA:GPU] Add runtime and proto support for persistent BufferAllocation](https://github.com/tensorflow/tensorflow/commit/e78b8e0be024954786bca1b65c01b485b556e954) | majnemer |
| 2026-11-18 | [PR #50727: [CPU] Flush subnormal inputs in the atan2 builtins](https://github.com/tensorflow/tensorflow/commit/16b08e8b04b56dbe4f8eaa4872096debc6f1fdf9) | Jaydeng75 |
| 2026-11-18 | [Remove obsolete linkstatic = 1 workarounds from TensorFlow C++ rules](https://github.com/tensorflow/tensorflow/commit/60fd6de81dc9f2d61cd26e873a08511a4a8956b3) | tensorflower-gardener |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
