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
| 🐞 **Open issues + PRs** | [3.4k](https://github.com/tensorflow/tensorflow/issues) |
| 💻 **Languages** | C++ 56% · Python 25% · MLIR 7% · Starlark 4% · HTML 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `tensorflow` `machine-learning` `python` `deep-learning` `deep-neural-networks` `neural-network` `ml` `distributed` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2015-11-07 |
| 📦 **Latest release** | [v2.21.0](https://github.com/tensorflow/tensorflow/releases/tag/v2.21.0) — 2026-03-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 1411.7 MB |
| 🌐 **Website** | https://tensorflow.org |

## 📦 Recent releases

### [v2.22.0-rc1](https://github.com/tensorflow/tensorflow/releases/tag/v2.22.0-rc1) — TensorFlow 2.22.0-rc1 _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

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
| 2026-11-19 | [PR #46000: [GPU][Triton][RaggedDot] Backend selection and fusion wiri…](https://github.com/tensorflow/tensorflow/commit/00d86779c4dff9d1d1d3fca1d07df96e9fb529f3) | mfrancepillois |
| 2026-11-19 | [[XLA:GPU] Lower expm1 and log1p directly to TensorIR ops.](https://github.com/tensorflow/tensorflow/commit/40dbee6f67d1a0a9823a11f13d7f742c7ab6d88d) | chsigg |
| 2026-11-19 | [[XLA:GPU] Reuse FfiKernelRegistry arg packing and launch dims in reco…](https://github.com/tensorflow/tensorflow/commit/bb1a778221b1a3b2b61bd6528fb7b511ef9529b5) | sohaibiftikhar |
| 2026-11-19 | [PR #52961: [XLA:GPU] Add forward FFT support for the Intel GPU backen…](https://github.com/tensorflow/tensorflow/commit/9bf957892a2e602600d951c7ddaf75e685ec640e) | Nikhita-P-Hegde |
| 2026-11-19 | [[XLA:GPU] Migrate XLA tests, build rules and docs to the new autotune…](https://github.com/tensorflow/tensorflow/commit/285c81b7365a6eed49b20e6daebe11c8bc3c430c) | shyamliagrawal |
| 2026-11-19 | [[XLA:GPU] Disable external NCCL net plugins by default in multi-proce…](https://github.com/tensorflow/tensorflow/commit/8722a560a8dfe522be85952fab3345c42e9a589a) | sohaibiftikhar |
| 2026-11-19 | [[XLA][NFC] Move expander HLO passes from xla/service to xla/hlo/trans…](https://github.com/tensorflow/tensorflow/commit/f689520fdcd25ff662a976950af81bb32c3317a0) | pifon2a |
| 2026-11-19 | [PR #53299: [XLA:GPU] Auto-enable keeping recorded collectives out of …](https://github.com/tensorflow/tensorflow/commit/df8565ed75cff38169801a32aacc730d31c19392) | shawnwang18 |
| 2026-11-19 | [[XLA][NFC] Move service/fusion_explorer to tools/fusion_explorer](https://github.com/tensorflow/tensorflow/commit/7be697dadf313c7835acb128ccd9d26b435839af) | pifon2a |
| 2026-11-19 | [Link `test_main` in `traceme_encode_test` and `scoped_annotation_test`.](https://github.com/tensorflow/tensorflow/commit/f147279fd998f80a86ca57b4307a7b081c80fa16) | chsigg |

[See all commits ↗](https://github.com/tensorflow/tensorflow/commits)

## ⬇️ Get it

```bash
git clone https://github.com/tensorflow/tensorflow.git
```
