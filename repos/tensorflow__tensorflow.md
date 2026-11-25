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
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1420.1 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 8d ago</sub>

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
| 2026-11-25 | [[XLA] Return errors from NamedSharding::FromProto](https://github.com/tensorflow/tensorflow/commit/cbf3b35e8b397ffec3c8a7c8635d8736f149b992) | dimitar-asenov |
| 2026-11-25 | [[XLA:GPU] Raise Triton all-reduce max blocks per grid from 32 to 128](https://github.com/tensorflow/tensorflow/commit/ce8f306bc1a5569ee98396bf09785d0b08615064) | PatriosTheGreat |
| 2026-11-25 | [[XLA] Keep each operand's own batch dimensions in DotDecomposer](https://github.com/tensorflow/tensorflow/commit/b21be08f23576887db3c03709f6dbd719fda1d14) | oliness |
| 2026-11-25 | [[XLA] Use i64 scan indices when padded mhlo.scan exceeds INT32_MAX.](https://github.com/tensorflow/tensorflow/commit/c6815cf3ac564c796c28ea96b4fc9d6019415dc4) | mkuperst |
| 2026-11-25 | [Fix nondeterminism in TOCO custom op FlexBuffer attribute serialization.](https://github.com/tensorflow/tensorflow/commit/a9a33a9203ca39d6e6dcbe19c161ef3069b242e3) | tensorflower-gardener |
| 2026-11-25 | [[XLA:CPU] Use llvm::StringLiteral for kNoFpContractAttr.](https://github.com/tensorflow/tensorflow/commit/bb60d0b41bb628427520f0e447383c96ecadc3d9) | seantalts |
| 2026-11-25 | [[XLA] Remove some comparison operators that can be defaulted in C++20](https://github.com/tensorflow/tensorflow/commit/dec4290faa4dffbaa300d45c1a41e94ec49dba32) | d0k |
| 2026-11-25 | [[XLA] Reject nested TUPLE OpSharding protos in HloSharding::FromProto](https://github.com/tensorflow/tensorflow/commit/d107c3c26944a5a9c4263cd816f419c85ec4e2e6) | dimitar-asenov |
| 2026-11-25 | [[XLA] Return errors from Mesh and AxisRef FromProto](https://github.com/tensorflow/tensorflow/commit/95d4e37c426db4f31cb3708b9cf9ef7791680264) | dimitar-asenov |
| 2026-11-25 | [PR #52998: [XLA:GPU][ROCm] Use the device warp size in coalescing ana…](https://github.com/tensorflow/tensorflow/commit/af20b7503775d3f3b0098a662d2c9fb7f127fb25) | nurmukhametov |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
