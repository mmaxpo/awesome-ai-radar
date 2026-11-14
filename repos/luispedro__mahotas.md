# luispedro/mahotas

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/luispedro/mahotas)

> Computer Vision in Python

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📈 Classic ML, data science & vision |
| **Project** | — |
| **Why it's worth a look** | Fast image-processing and computer-vision functions for Python |
| **Added** | 2026-11-11 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 891 |
| 🍴 **Forks** | 152 |
| 🐞 **Open issues + PRs** | [19](https://github.com/luispedro/mahotas/issues) |
| 💻 **Languages** | Python 63% · C++ 35% · Meson 1% |
| 📜 **License** | Other |
| 🏷 **Topics** | `computer-vision` `numpy` `python` `c-plus-plus` `python-2` `python-3` |
| 🕒 **Last activity** | 2026-10-16 (29d ago) |
| 📅 **Created** | 2010-01-31 |
| 📦 **Latest release** | [v1.4.19](https://github.com/luispedro/mahotas/releases/tag/v1.4.19) — 2026-09-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.2 MB |
| 🌐 **Website** | https://mahotas.rtfd.io |

## 📦 Recent releases

### [v1.4.19](https://github.com/luispedro/mahotas/releases/tag/v1.4.19) — Version 1.4.19
<sub>2026-09-22 · 1mo ago</sub>

> Bugfix release
> - Require Python 3.10+; support Python 3.14 and NumPy 2.x
> - Build with meson-python (`setup.py` removed)
> - Fix incorrect results in colour conversions (`rgb2xyz`, `xyz2rgb`, `xyz2lab`), `gbernsen`, `dog`, and `find`
> - Fix `gaussian_filter1d` ignoring `out` and failing with default `axis=-1`; fix `gaussian_filter` on some 3-D inputs
> - `center_of_mass` returns NaN for zero-sum labels
> …

### [v1.4.14](https://github.com/luispedro/mahotas/releases/tag/v1.4.14) — Version 1.4.14
<sub>2024-03-23 · 2y ago</sub>

> Removes use of outdated C++ function

### [v1.4.13](https://github.com/luispedro/mahotas/releases/tag/v1.4.13) — Version 1.4.13
<sub>2022-06-28 · 4y ago</sub>

> Update for newer NumPy (version 1.22 and above).

### [v1.4.12](https://github.com/luispedro/mahotas/releases/tag/v1.4.12) — Version 1.4.12
<sub>2022-06-27 · 4y ago</sub>

> Updated for newer NumPy versions

### [v1.4.8](https://github.com/luispedro/mahotas/releases/tag/v1.4.8) — Version 1.4.8
<sub>2019-10-10 · 7y ago</sub>

> Bugfix release: fixes co-occurrence matrix computation (important for Haralick features computation), contributed by @databaaz (PR #105)

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-16 | [TST Skip PEP 649 __annotate__ in typing test](https://github.com/luispedro/mahotas/commit/be88f6bd66028fad804a10bf55594b8b181c9def) | luispedro |
| 2026-10-16 | [ENH Add Python 3.11 type hints to the Python API](https://github.com/luispedro/mahotas/commit/6447643d1be5d31e4d0325a0a505112a63d601cc) | luispedro |
| 2026-10-16 | [MIN Use importlib.resources for demo data](https://github.com/luispedro/mahotas/commit/1462413a948d5f1344f1cf104213674b5812aead) | luispedro |
| 2026-10-16 | [BUG Load superpixels demo image independently of the CWD](https://github.com/luispedro/mahotas/commit/d6cc59bba170dc5f10b00f0d745388bf79d3cf53) | luispedro |
| 2026-10-16 | [MIN Use zip(strict=True) and itertools.pairwise](https://github.com/luispedro/mahotas/commit/cea9a448bb21bdbd6fe305d53260a0bb19358745) | luispedro |
| 2026-10-16 | [MIN Remove Python 2 module init from DECLARE_MODULE](https://github.com/luispedro/mahotas/commit/eba2239a9ef08295141da1570a63de62d9c70a6e) | luispedro |
| 2026-10-16 | [DOC Add doctest examples to core functions](https://github.com/luispedro/mahotas/commit/a313d3a84fce468c19d26af6f1116182a0a76752) | luispedro |
| 2026-10-16 | [DOC Add submodule functions to API documentation](https://github.com/luispedro/mahotas/commit/0fb1a9c00c2f458deeee3e6af9afa33dd638ef31) | luispedro |
| 2026-10-16 | [DOC Document missing behaviour and fix docstring formatting](https://github.com/luispedro/mahotas/commit/93c37a87ba41315cb6ca6be6aa657cc5d29fd05b) | luispedro |
| 2026-10-16 | [BUG Reject unknown metrics in distance()](https://github.com/luispedro/mahotas/commit/7b01996cd51e2fb987359839c14ac504656d8310) | luispedro |

[See all commits ↗](https://github.com/luispedro/mahotas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/luispedro/mahotas.git
```
