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
| ⭐ **Stars** | 64.5k |
| 🍴 **Forks** | 19.8k |
| 🐞 **Open issues + PRs** | [274](https://github.com/keras-team/keras/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `tensorflow` `neural-networks` `machine-learning` `data-science` `python` `jax` `pytorch` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2015-03-28 |
| 📦 **Latest release** | [v3.12.4](https://github.com/keras-team/keras/releases/tag/v3.12.4) — 2026-07-29 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 58.5 MB |
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
<sub>2026-06-26 · 5mo ago</sub>

> Keras 3.12.3 is a security patch release that hardens model saving, loading, and deserialization against a range of attack vectors.
> **HDF5 Hardening**
> * **Eject ExternalLink/SoftLink groups in KerasFileEditor** (#22899)
>   * Prevents HDF5 external/soft links from being exploited to read arbitrary files during model editing.
> * **Reject ExternalLink/SoftLink on legacy `.h5` dispatcher** (#22900)
>   * Extends HDF5 link rejection to the legacy `load_weights` path for `.h5` files.
> …

### [v3.15.0](https://github.com/keras-team/keras/releases/tag/v3.15.0)
<sub>2026-06-24 · 5mo ago</sub>

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
| 2026-11-26 | [Use conv in the backend-agnostic correlate (#24350)](https://github.com/keras-team/keras/commit/769752132143bc2601207b20941f1ac711bb9357) | SamanehSaadat |
| 2026-11-26 | [Disable `jit_compile` with multi-replica `tf.distribute` strategies (…](https://github.com/keras-team/keras/commit/579bad6a022a0faef964ad35fddb46a81476d555) | SamanehSaadat |
| 2026-11-26 | [Move unrelated code out of `variables.py`. (#24366)](https://github.com/keras-team/keras/commit/d001afc9245250c9e5ed18c369b92973d7f7c1fe) | hertschuh |
| 2026-11-25 | [Explicitly import individual core ops in each `ops/__init__.py`. (#24…](https://github.com/keras-team/keras/commit/082c2e291519f36109a9e913d007d03e1d795974) | hertschuh |
| 2026-11-25 | [Use dev0 version suffix on master (#24347)](https://github.com/keras-team/keras/commit/21c66708d8c6355ffcd9f964ee2140ef06c06f40) | laxmareddyp |
| 2026-11-25 | [Move `random_seed_dtype` from `core` to `random`. (#24354)](https://github.com/keras-team/keras/commit/ad1de1b7da0203d6d9f312c11e274bc7edd24ba3) | hertschuh |
| 2026-11-25 | [Add backend-agnostic implementation for hypot (#24346)](https://github.com/keras-team/keras/commit/d0aece6d3b9d1b9b0b607d437581280ab462d9f6) | SamanehSaadat |
| 2026-11-25 | [Add backend-agnostic implementation for histogram (#24344)](https://github.com/keras-team/keras/commit/53a837ad0b2323b88e0bc85b1aa7d0f57103d410) | SamanehSaadat |
| 2026-11-25 | [Speed up backend-agnostic exp2 by using exp instead of power (#24349)](https://github.com/keras-team/keras/commit/9ecd05d7e3d16902e37e3a6c5c164b03ea006d3e) | SamanehSaadat |
| 2026-11-24 | [Stop using `backend.config` and use `config` directly instead. (#24351)](https://github.com/keras-team/keras/commit/48d0f6f10238441608fe5b33261bd72676a783f5) | hertschuh |

[See all commits ↗](https://github.com/keras-team/keras/commits)

## ⬇️ Get it

```bash
git clone https://github.com/keras-team/keras.git
```
