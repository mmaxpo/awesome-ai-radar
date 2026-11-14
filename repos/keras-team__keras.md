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
| 🐞 **Open issues + PRs** | [238](https://github.com/keras-team/keras/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `tensorflow` `neural-networks` `machine-learning` `data-science` `python` `jax` `pytorch` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2015-03-28 |
| 📦 **Latest release** | [v3.12.4](https://github.com/keras-team/keras/releases/tag/v3.12.4) — 2026-07-29 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 57.9 MB |
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
| 2026-11-13 | [Check each op inside a functional Model in OpTest (#24240)](https://github.com/keras-team/keras/commit/abbab4c030e31476a069844fa64e53ba9368423b) | gaga1313 |
| 2026-11-13 | [Fix torch linspace, logspace and geomspace returning nan for num=1 (#…](https://github.com/keras-team/keras/commit/426e315e67005f97d4cca0f4e68335e7fbf28fc8) | SamanehSaadat |
| 2026-11-13 | [Write histograms and images with tensorboardX (#24238)](https://github.com/keras-team/keras/commit/de276338f5a158ea407fe07ad6667c80946be66d) | SamanehSaadat |
| 2026-11-13 | [Add compile check to evaluate() in torch and numpy trainers (#24153)](https://github.com/keras-team/keras/commit/c93a34654c4d158dc3be4caea1d0bbc279373871) | vnayakde |
| 2026-11-13 | [Calibrate third-party layers that declare GPTQ or AWQ support (#24237)](https://github.com/keras-team/keras/commit/397de7e1e7bf7e3c32c89f22d51251417b4e64c2) | JyotinderSingh |
| 2026-11-13 | [Eliminate host-to-device tensor copies in quantized layers for CUDA g…](https://github.com/keras-team/keras/commit/e1089a6f4da475dd33331785890ec44b32f35b07) | JyotinderSingh |
| 2026-11-13 | [Support loading unlisted backends via KERAS_ALLOW_UNOFFICIAL_BACKEND …](https://github.com/keras-team/keras/commit/bff018622b0066b90e19cb7614dd117ea0f220fc) | laxmareddyp |
| 2026-11-13 | [Stop using `backend.result_type` and instead import it from... (#24234)](https://github.com/keras-team/keras/commit/c1f0afefd48ac8db4f2a90453f1926e0dedf1801) | hertschuh |
| 2026-11-13 | [Accept NumPy integers as layer arguments (#24226)](https://github.com/keras-team/keras/commit/1b327e722f7fc76394aa327c48973c4a27283bb9) | JyotinderSingh |
| 2026-11-13 | [Keep no config on a calibrated GPTQ or AWQ layer (#24233)](https://github.com/keras-team/keras/commit/9b4de37de7dea2d63246c78b7ddc437a161a3a08) | JyotinderSingh |

[See all commits ↗](https://github.com/keras-team/keras/commits)

## ⬇️ Get it

```bash
git clone https://github.com/keras-team/keras.git
```
