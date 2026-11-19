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
| ⭐ **Stars** | 50.6k |
| 🍴 **Forks** | 20.8k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/pandas-dev/pandas/issues) |
| 💻 **Languages** | Python 91% · Cython 6% · C 1% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `data-analysis` `pandas` `flexible` `alignment` `python` `data-science` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 416.7 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 14d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 28d ago</sub>

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
<sub>2026-09-17 · 2mo ago</sub>

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
| 2026-11-18 | [CLN: import directly in pandas/io/_util.py instead of "import pandas …](https://github.com/pandas-dev/pandas/commit/264b9d8f97b579a009f77fb171bf0c24d903604a) | fangchenli |
| 2026-11-18 | [TYP: consistent columns annotations for DataFrame writers (GH#30449) …](https://github.com/pandas-dev/pandas/commit/c4220638b83b3a879560b6024cda6efa2c67fd2b) | jbrockmendel |
| 2026-11-18 | [BUG: ufunc with a pandas object as `where` recursed infinitely (GH#60…](https://github.com/pandas-dev/pandas/commit/13fa1b31da2f31bb24eb1c432ed25147e3a283f8) | jbrockmendel |
| 2026-11-18 | [BUG: read_csv c engine header=None with callable usecols (GH#71880) (…](https://github.com/pandas-dev/pandas/commit/4f02479444c1da515b14c27fa028f521665ba98d) | jbrockmendel |
| 2026-11-18 | [BUG: quantile on all-NA third-party ExtensionArray raising (GH#45968)…](https://github.com/pandas-dev/pandas/commit/9edea0116d91409ee38c8a5c0be2a1c325e01532) | jbrockmendel |
| 2026-11-18 | [BUG: DataFrame.to_latex/to_csv with Index, Series or array columns (#…](https://github.com/pandas-dev/pandas/commit/68dda2544d640d5183124bd26e2ffe4e9bab6823) | jbrockmendel |
| 2026-11-18 | [BUG: describe raising for EAs whose statistics can't be cast to float…](https://github.com/pandas-dev/pandas/commit/5339de05e4c2ac160f38a1805220df1735b938c7) | jbrockmendel |
| 2026-11-18 | [DEPR: timedelta_range closed in favor of inclusive (GH#40245) (#72057)](https://github.com/pandas-dev/pandas/commit/3e52539e2786878c9fe47c6cd90f5a50484d5858) | jbrockmendel |
| 2026-11-18 | [DOC/MNT: update maintainer release guidelines (#71901)](https://github.com/pandas-dev/pandas/commit/e45c04ac31d448a2f38d7eb0420f05a2391f323f) | jorisvandenbossche |
| 2026-11-18 | [CLN: move _arrow_dtype_mapping from pandas.io into pandas.core (#72203)](https://github.com/pandas-dev/pandas/commit/29765f135c637a4890c9e62be84d63c1ba38809c) | fangchenli |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
