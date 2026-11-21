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
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1412.9 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 4d ago</sub>

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
| 2026-11-21 | [[XLA:GPU] Color two-shot Triton AllGather outputs in collective symme…](https://github.com/tensorflow/tensorflow/commit/f80e9534620de429cb5f97adfd212a40b5e7390e) | sohaibiftikhar |
| 2026-11-21 | [[IFRT IR] Tighten `IfrtDialect` attribute and `IfrtArrayType` verifiers](https://github.com/tensorflow/tensorflow/commit/3ceba449fd7e1bdf3ce593b90e3adc37d3f4d420) | ICGog |
| 2026-11-21 | [[IFRT] Validate element bounds and non-zero product in `xla::ifrt::In…](https://github.com/tensorflow/tensorflow/commit/4244352d0041fb9db90f7883601998f5cf59eeb5) | hyeontaek |
| 2026-11-21 | [[IFRT] Introduce `IfrtIrExecutable` and compile-only `IfrtIrProgramCo…](https://github.com/tensorflow/tensorflow/commit/d8fd7c04e5cf172d8bff31c647431f8ace901eda) | hyeontaek |
| 2026-11-21 | [[xla:cpu/nanort] Plumb `ExecuteOptions::custom_options` through `Nano…](https://github.com/tensorflow/tensorflow/commit/944763d31ead203fb9afedf017bc01e281a11099) | cezheng |
| 2026-11-21 | [[MHLO] Extend mhlo.dot_general with block scaling and structured spar…](https://github.com/tensorflow/tensorflow/commit/2b1a2b68725aa6363c5d6c31ab131eb489a9e124) | tensorflower-gardener |
| 2026-11-21 | [[XLA] Keep latency_metadata an integer when collectives are combined](https://github.com/tensorflow/tensorflow/commit/614979f4518add3a00fa0503ab88eb39c96a49c6) | patrick-toulme |
| 2026-11-21 | [Implement `AcquireExternalDmaAccess` for PjRt GPU.](https://github.com/tensorflow/tensorflow/commit/0ad69f3577522d874b9d1b816c2489cd6d92390c) | junwhanahn |
| 2026-11-21 | [[XLA:PjRt] Add 512 bit transpose microkernels and runtime block sizing](https://github.com/tensorflow/tensorflow/commit/8112c9834ef0a323adfcc9f1b50f9d74537a4cb7) | majnemer |
| 2026-11-21 | [Integrate LLVM at llvm/llvm-project@86801a03ccc8](https://github.com/tensorflow/tensorflow/commit/3f51b4b4a3574d998ff53cf446d146416bde2152) | tensorflower-gardener |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
