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
| ⭐ **Stars** | 201.8k |
| 🍴 **Forks** | 77.4k |
| 🐞 **Open issues + PRs** | [3.5k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1414.7 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 6d ago</sub>

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
| 2026-11-23 | [[XLA:GPU] Order producer-consumer adaptor instructions like the fused…](https://github.com/tensorflow/tensorflow/commit/a16aa301ecbd8ffa964e40d401b35cfe1300f39f) | Moerafaat |
| 2026-11-23 | [[XLA:GPU] Use CuDnnGemmDimensions instead of TritonFusionAnalysis in …](https://github.com/tensorflow/tensorflow/commit/87f4eab9436cf4d4937de7b5f707d9d819416674) | vwbaker |
| 2026-11-23 | [[XLA:GPU] Remove hlo_fusion_stats.](https://github.com/tensorflow/tensorflow/commit/ea084cc5869e8c1e8216bc8f0cf5d9562c82082c) | pifon2a |
| 2026-11-23 | [[XLA:GPU] Preserve gpu_device_info.name in GpuTargetConfig::FromProto](https://github.com/tensorflow/tensorflow/commit/d760b5dcdc11a1aaef9a446a75f9b624a3cec773) | tucan9389 |
| 2026-11-23 | [[XLA:GPU] Support split M dimensions in CuDnnGemmDimensions.](https://github.com/tensorflow/tensorflow/commit/dbfb9c00138c3364668a6090938b75696f08ff29) | vwbaker |
| 2026-11-23 | [[XLA] Prevent int64_t overflow in AxisRef sub-axis next_pre_size](https://github.com/tensorflow/tensorflow/commit/d1e88f60a279ae74bf17c583366a053f06dd81cc) | dimitar-asenov |
| 2026-11-23 | [[XLA:GPU] Configure two-shot AllGather kernel spec and peer-table out…](https://github.com/tensorflow/tensorflow/commit/53280aebedf641d22900c94594fd098e4b6a2814) | sohaibiftikhar |
| 2026-11-23 | [[XLA:CPU] Forward kTiledLlvmIrGemv dots to xtile.](https://github.com/tensorflow/tensorflow/commit/6ebd77854f79dfd94c71aeab6f126af11b1c07e4) | pifon2a |
| 2026-11-23 | [PR #52971: [AlgebraicSimplifier] Gate constant reciprocal division re…](https://github.com/tensorflow/tensorflow/commit/f658875f7c96a60db69578e69872170d1e5fc1ff) | JarvisDing-sdu |
| 2026-11-23 | [[XLA] Fix int64 truncation in IotaTileAssignment::value_at](https://github.com/tensorflow/tensorflow/commit/24c6d53dd5091c02c8ff7c6cf0de56077fe82423) | dimitar-asenov |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
