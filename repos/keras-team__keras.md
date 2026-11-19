# keras-team/keras

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/keras-team/keras)

> Deep Learning for humans

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🖥 Models, local inference & gateways |
| **Project** | — |
| **Why it's worth a look** | High-level deep-learning API (runs on JAX, TensorFlow or PyTorch) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 64.4k |
| 🍴 **Forks** | 19.8k |
| 🐞 **Open issues + PRs** | [243](https://github.com/keras-team/keras/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `tensorflow` `neural-networks` `machine-learning` `data-science` `python` `jax` `pytorch` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2015-03-28 |
| 📦 **Latest release** | [v3.12.4](https://github.com/keras-team/keras/releases/tag/v3.12.4) — 2026-07-29 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 58.3 MB |
| 🌐 **Website** | http://keras.io/ |

## 📦 Recent releases

### [v3.12.4](https://github.com/keras-team/keras/releases/tag/v3.12.4) — Keras 3.12.4
<sub>2026-07-29 · 3mo ago</sub>

> **Keras 3.12.4**
> Keras 3.12.4 is a security patch release that hardens dataset loading and model file handling against insecure deserialization and decompression-bomb attacks.
> **Security Fixes**
> * **Restrict unpickling when loading IMDB and Reuters datasets** — Replaces `np.load(allow_pickle=True)` with a restricted unpickler that only permits numpy array reconstruction, preventing arbitrary code execution via crafted `.npz` files (CWE-502). ([#23047](https://github.com/keras-team/keras/pull/23047)) by @LinZiyuu
> * **Verify all intermediary H5 groups when navigating H5 files** — Manually resolves nested H5 group paths to verify group types at each step, preventing potential path traversal. ([#23168](https://github.com/keras-team/keras/pull/23168)) by @hertschuh
> * **Reject decompression-bomb members on the `.keras` asset extraction path** — Adds per-member decompression-ratio checks before extracting `.keras` archives to disk, preventing disk-exhaustion attacks via crafted archives. ([#23101](https://github.com/keras-team/keras/pull/23101)) by @LinZiyuu
> …

### [v3.15.1](https://github.com/keras-team/keras/releases/tag/v3.15.1) — Keras 3.15.1
<sub>2026-07-29 · 3mo ago</sub>

> **Release Notes**
> Keras 3.15.1 is a patch release containing important security hardening, bug fixes, and Python 3.14 compatibility improvements.
> **Security Fixes**
> * **Restrict unpickling when loading IMDB and Reuters datasets** — Prevents insecure deserialization (CWE-502) by replacing bare `np.load(allow_pickle=True)` with a restricted unpickler that only permits numpy array reconstruction. ([#23047](https://github.com/keras-team/keras/pull/23047)) by @LinZiyuu
> * **Verify all intermediary H5 groups when navigating H5 files** — Manually resolves nested H5 group paths to verify group types at each step, preventing potential path traversal issues. ([#23168](https://github.com/keras-team/keras/pull/23168)) by @hertschuh
> * **Reject decompression-bomb members on the `.keras` asset extraction path** — Adds per-member decompression-ratio checks before extracting `.keras` archives to disk, preventing disk-exhaustion attacks via crafted archives. ([#23101](https://github.com/keras-team/keras/pull/23101)) by @LinZiyuu
> …

### [v3.12.3](https://github.com/keras-team/keras/releases/tag/v3.12.3)
<sub>2026-06-26 · 4mo ago</sub>

> Keras 3.12.3 is a security patch release that hardens model saving, loading, and deserialization against a range of attack vectors.
> **HDF5 Hardening**
> * **Eject ExternalLink/SoftLink groups in KerasFileEditor** (#22899)
>   * Prevents HDF5 external/soft links from being exploited to read arbitrary files during model editing.
> * **Reject ExternalLink/SoftLink on legacy `.h5` dispatcher** (#22900)
>   * Extends HDF5 link rejection to the legacy `load_weights` path for `.h5` files.
> …

### [v3.15.0](https://github.com/keras-team/keras/releases/tag/v3.15.0)
<sub>2026-06-24 · 4mo ago</sub>

> **Highlights**
> - **Keras-to-Torch Export**: New `export_torch` enables exporting Keras models to native PyTorch `nn.Module` format, along with LiteRT (TFLite) export support for the PyTorch backend.
> - **Sliding Window Attention**: Added `sliding_window` parameter to `MultiHeadAttention` and `GroupedQueryAttention` for efficient long-context attention.
> - **Flash / Fused SDPA**: Causal-only MHA/GQA now automatically dispatches to Flash Attention (cuDNN SDPA), and the manual attention path correctly applies causal masking.
> - **Multi-Optimizer Training**: New `MultiOptimizer` supports assigning different optimizers to sub-networks.
> - **New Math Operations**: Added `unique`, `pinv`, `matrix_rank`, `fabs`, `fmax`, `fmin`, `erfc`, `dsplit`, `percentile`, `nanpercentile`, `sobel_edges`, and `ssim` (structural similarity) to `keras.ops`.
> …

### [v3.12.2](https://github.com/keras-team/keras/releases/tag/v3.12.2)
<sub>2026-05-07 · 6mo ago</sub>

> **Saving & Reloading**
> * **Harden path and link resolution when extracting files from archives (#22194 & #22839)**
>   * Fixed based folder used when validating files extracted from ZIP and TAR archives.
>   * Fixed link resolution bug when validating links extracted from TAR archives.
>   * Fixed path confusion bug when validating files extracted from ZIP and TAR archives (including `.keras` files).
>   * Added path validation when extracting assets from Orbax checkpoints.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Stop using `backend.floatx` and instead import `config` (#24292)](https://github.com/keras-team/keras/commit/9e044ad0d766ffc6a9526d23e334ad61b848acc5) | hertschuh |
| 2026-11-18 | [Check each op under bfloat16 and float16 floatx in OpTest (#24266)](https://github.com/keras-team/keras/commit/4a1c5a3c9b9af3c09a6d11aabe64fbe6ad070ace) | gaga1313 |
| 2026-11-18 | [Stop using `backend.epsilon` and instead import `config` (#24289)](https://github.com/keras-team/keras/commit/f0a2630735dccbd628a4b054ad4abfdc24bf00b4) | hertschuh |
| 2026-11-18 | [Make TensorFlow follow x64_mode (#24265)](https://github.com/keras-team/keras/commit/791137e8f8b8ee61e01dc5ccd298e81cff57122a) | gaga1313 |
| 2026-11-18 | [Remove in-place operators on tensors (#24280)](https://github.com/keras-team/keras/commit/2c9d6f34908d9c6a555d2ebf64f3da9c25c2cc2e) | SamanehSaadat |
| 2026-11-18 | [Check each op has finite gradients in OpTest (#24277)](https://github.com/keras-team/keras/commit/1fbb849cd5c3b72503ce52b5b751cb90457b6a4f) | gaga1313 |
| 2026-11-18 | [Check dtype= argument in OpTest (#24268)](https://github.com/keras-team/keras/commit/1b51c059877036354b6f8498e9d23d050f86a4c9) | gaga1313 |
| 2026-11-18 | [Convert 64-bit integers to float64 in elementwise ops under explicit_…](https://github.com/keras-team/keras/commit/da6a344b4382a04da26ec83795080c111bd24a86) | gaga1313 |
| 2026-11-17 | [Suppress spurious divide-by-zero warning in numpy divide_no_nan (#24201)](https://github.com/keras-team/keras/commit/7e7e213c1d0bf505d278d8d03516390f7e1db4e0) | SID-6921 |
| 2026-11-17 | [Honor copy argument in Variable.__array__ (#24275)](https://github.com/keras-team/keras/commit/ba23a7e4855be77d2da9f94b074c495a1c6305cb) | SamanehSaadat |

[See all commits ↗](https://github.com/keras-team/keras/commits)

## ⬇️ Get it

```bash
git clone https://github.com/keras-team/keras.git
```
