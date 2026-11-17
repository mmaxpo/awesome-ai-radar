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
| 🐞 **Open issues + PRs** | [245](https://github.com/keras-team/keras/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `deep-learning` `tensorflow` `neural-networks` `machine-learning` `data-science` `python` `jax` `pytorch` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2015-03-28 |
| 📦 **Latest release** | [v3.12.4](https://github.com/keras-team/keras/releases/tag/v3.12.4) — 2026-07-29 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 58.1 MB |
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
| 2026-11-17 | [Resolve weak floats and cbrt to floatx under bfloat16 and float16 (#2…](https://github.com/keras-team/keras/commit/34de92f06f2e15ae02261df9c49e03d98ba21adc) | gaga1313 |
| 2026-11-16 | [Reword Fashion-MNIST license note in fashion_mnist.load_data docstrin…](https://github.com/keras-team/keras/commit/66f8c0db4f36c5b3c9adcdd127d88d93b76e7f65) | SamanehSaadat |
| 2026-11-16 | [Use float32 inputs in SqueezeTest (#24253)](https://github.com/keras-team/keras/commit/b5f5bb86732663959a6f00825a700aafa5b740e7) | MarcosAsh |
| 2026-11-16 | [Test 64-bit dtypes in the OpTest harness (#24230)](https://github.com/keras-team/keras/commit/beb2168589484df34514aa715825b1609a7b34ee) | gaga1313 |
| 2026-11-16 | [Make `__array__` functions compliant with NumPy 2.x. (#24242)](https://github.com/keras-team/keras/commit/39559cc2888d43c12cbc3a853afa59dab9ecbfae) | hertschuh |
| 2026-11-16 | [Check each op on NumPy arrays, Variables and Python lists in OpTest (…](https://github.com/keras-team/keras/commit/dc0ad94d2d5eedf3a56491c067786186ce2b4387) | gaga1313 |
| 2026-11-16 | [Fix NumPy logsumexp for bfloat16 with ml_dtypes 0.7.0 (#24263)](https://github.com/keras-team/keras/commit/6d9a24a57adf3e4774426885ad1693c91526d6b5) | SamanehSaadat |
| 2026-11-14 | [Add backend-agnostic implementation for geomspace (#24235)](https://github.com/keras-team/keras/commit/50be564d7d833537b789b0359ec709f5a7267c33) | SamanehSaadat |
| 2026-11-14 | [Add backend-agnostic implementation for hamming (#24241)](https://github.com/keras-team/keras/commit/5521f19d5863a8744ef27ab6c83f4c4e57a5c4bf) | SamanehSaadat |
| 2026-11-14 | [Remove unused train graph code (#24243)](https://github.com/keras-team/keras/commit/5c43c7c9d3b30a3725f0b4e716f7a5f6548af540) | SamanehSaadat |

[See all commits ↗](https://github.com/keras-team/keras/commits)

## ⬇️ Get it

```bash
git clone https://github.com/keras-team/keras.git
```
