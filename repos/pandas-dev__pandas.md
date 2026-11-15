# pandas-dev/pandas

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pandas-dev/pandas)

> Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | The standard Python data-analysis library (cheat sheet in doc/cheatsheet) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 50.5k |
| 🍴 **Forks** | 20.7k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/pandas-dev/pandas/issues) |
| 💻 **Languages** | Python 91% · Cython 6% · C 1% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `data-analysis` `pandas` `flexible` `alignment` `python` `data-science` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 413.2 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 10d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 23d ago</sub>

> We are pleased to announce the release of pandas 3.1.0.
> This release includes some new features, bug fixes, and performance improvements. We recommend that all users upgrade to this version.
> Highlights include:
> - [New `DataFrame.select()` and updated `DataFrame.filter()` method](https://pandas.pydata.org/docs/whatsnew/v3.1.0.html#new-method-dataframe-select)
> - [Faster `pd.read_csv()`, with parallel reads of large files](https://pandas.pydata.org/docs/whatsnew/v3.1.0.html#whatsnew-310-enhancements-read-csv)
> See the [detailed release notes](https://pandas.pydata.org/docs/whatsnew/v3.1.0.html) for a list of all the changes.
> …

### [v3.1.0rc0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0rc0) — pandas 3.1.0rc0 _(pre-release)_
<sub>2026-09-30 · 1mo ago</sub>

> We are pleased to announce a release candidate for pandas 3.1.0.
> See the [whatsnew](https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade --pre pandas==3.1.0rc0
> Or from conda-forge
>     conda install -c conda-forge/label/pandas_rc pandas==3.1.0rc0
> …

### [v3.0.6](https://github.com/pandas-dev/pandas/releases/tag/v3.0.6) — pandas 3.0.6
<sub>2026-09-17 · 1mo ago</sub>

> We are pleased to announce the release of pandas 3.0.6.
> This is a patch release in the 3.0.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.0.x series upgrade to this version. This is also the first release to support Python 3.15.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.0.6.html) for a list of all the changes.
> Pandas 3.0 supports Python 3.11 and higher.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.0.*
> …

### [v3.0.5](https://github.com/pandas-dev/pandas/releases/tag/v3.0.5) — pandas 3.0.5
<sub>2026-07-22 · 3mo ago</sub>

> We are pleased to announce the release of pandas 3.0.5.
> This is a patch release in the 3.0.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.0.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.0.5.html) for a list of all the changes.
> Pandas 3.0 supports Python 3.11 and higher.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.0.*
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [ENH: future.python_scalars for __array_ufunc__ (#72115)](https://github.com/pandas-dev/pandas/commit/9b9be6d5b979cb984b765026158587c478a9a6f4) | rhshadrach |
| 2026-11-15 | [DOC: Require pandas-review self-review for AI-assisted PRs (#70954)](https://github.com/pandas-dev/pandas/commit/aa74cd30dcbd53816f451b1bb76f658a4fff6cff) | jbrockmendel |
| 2026-11-15 | [BUG: DataFrame.loc with a list of partial tuples on a MultiIndex (GH#…](https://github.com/pandas-dev/pandas/commit/ab0f0ab2d4b726b8c6c7a059cf24e5848c18b5d0) | jbrockmendel |
| 2026-11-15 | [DEPR: non-native byteorder in Series/DataFrame/Index construction (GH…](https://github.com/pandas-dev/pandas/commit/4d7eab147d9412337fdad32ac38d2b169340db20) | jbrockmendel |
| 2026-11-15 | [BUG: DataFrame.join with a list upcasting kept columns (GH#28269) (#7…](https://github.com/pandas-dev/pandas/commit/e0b4b5904b655b31a4545993952ccf89c4546343) | jbrockmendel |
| 2026-11-15 | [BUG: cut with nullable/pyarrow integers above 2**53 (GH#31389) (#72083)](https://github.com/pandas-dev/pandas/commit/debd4a7671532a4d6b671f6b5fc065e909dfe38a) | jbrockmendel |
| 2026-11-14 | [PERF: BaseMaskedArray._where with a same-dtype masked value (#72118)](https://github.com/pandas-dev/pandas/commit/99cc00d91e491d361393deea40447f66e3339ea4) | fangchenli |
| 2026-11-14 | [TST: read_parquet with dtype_backend="pyarrow" for a list of structs …](https://github.com/pandas-dev/pandas/commit/405828a8a0fa31966efd8e219d190c8a4cccb50f) | hatemadi15 |
| 2026-11-14 | [ENH: Unbox scalars from Index.min/max on EAs under future.python_scal…](https://github.com/pandas-dev/pandas/commit/ac3e45f758b847be1bb80f5aadaffcd904ac1a91) | rhshadrach |
| 2026-11-14 | [ENH: Unbox scalars from EA frame reductions under future.python_scala…](https://github.com/pandas-dev/pandas/commit/0d932715c57aa186bcb6a8e6685e5817f11f9eed) | rhshadrach |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
