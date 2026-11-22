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
| 🍴 **Forks** | 77.4k |
| 🐞 **Open issues + PRs** | [3.5k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1413.0 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 5d ago</sub>

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
| 2026-11-22 | [Automated Code Change](https://github.com/tensorflow/tensorflow/commit/75cf5f742ef3b5fec501269669fac40b77a6387b) | tensorflower-gardener |
| 2026-11-22 | [[XLA:GPU][NFC] Move GPU alias_info libraries to backends/gpu/hlo/anal…](https://github.com/tensorflow/tensorflow/commit/cf89af92e0fb46de21c9675f169bcee4fec735c4) | pifon2a |
| 2026-11-21 | [[XLA:CPU] Remove legacy prebuilt tfcompile RngState shims](https://github.com/tensorflow/tensorflow/commit/73720b3e45428c614c0cb5019935ca5b24330ecf) | majnemer |
| 2026-11-21 | [[XLA:GPU][NFC] Move GPU fusion passes to backends/gpu/transforms/fusion](https://github.com/tensorflow/tensorflow/commit/de10f3b94079b19634662ce7148cbf6c25a93a68) | pifon2a |
| 2026-11-21 | [[XLA:GPU] Delete unused hlo_algorithm_denylist and gpu_autotuning_proto](https://github.com/tensorflow/tensorflow/commit/48cee7f27c798c18210f72491877a8b9b639edd3) | pifon2a |
| 2026-11-21 | [[IFRT IR] Tighten IFRT IR op verifiers and factor shared checks onto …](https://github.com/tensorflow/tensorflow/commit/c7e516a88d55f704e8c99983b3de45780d00412d) | ICGog |
| 2026-11-21 | [[XLA] Peel bitcasts when checking buffer aliasing in ShouldFuseInPlaceOp](https://github.com/tensorflow/tensorflow/commit/5d4f214c54e90627bda9c866935044cdca352d68) | blakehechtman |
| 2026-11-21 | [[IFRT IR] Enforce direct `FuncOp` nesting in `NestedInIfrtFuncTrait` …](https://github.com/tensorflow/tensorflow/commit/2deff6661c853fe610762db39006e172e0ca3c56) | ICGog |
| 2026-11-21 | [[XLA:GPU] Color two-shot Triton AllGather outputs in collective symme…](https://github.com/tensorflow/tensorflow/commit/f80e9534620de429cb5f97adfd212a40b5e7390e) | sohaibiftikhar |
| 2026-11-21 | [[IFRT IR] Tighten `IfrtDialect` attribute and `IfrtArrayType` verifiers](https://github.com/tensorflow/tensorflow/commit/3ceba449fd7e1bdf3ce593b90e3adc37d3f4d420) | ICGog |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
