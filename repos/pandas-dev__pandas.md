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
| 💾 **Size** | 416.6 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 13d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 27d ago</sub>

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
| 2026-11-18 | [BUG: raise MemoryError instead of crashing when a khash table cannot …](https://github.com/pandas-dev/pandas/commit/269b4876efc1bfc114db37e465fb008512670b9e) | jbrockmendel |
| 2026-11-18 | [TST: DataFrameGroupBy.transform keeps dtypes beside a string column (…](https://github.com/pandas-dev/pandas/commit/5b8bfd3c55b55f46d88d87aae27cbc8dbe61cc9f) | jbrockmendel |
| 2026-11-18 | [DOC: fix Timedelta/Timestamp docstrings claiming nanosecond storage (…](https://github.com/pandas-dev/pandas/commit/ec8c397f676c3689b253c771af89ab95243b2bd0) | jbrockmendel |
| 2026-11-17 | [DOC: Add MultiIndex.to_list() to docs and indicate that it returns a …](https://github.com/pandas-dev/pandas/commit/47a82bc9c7c50b1cc360eb1a505546be5fde457e) | Prem-gosavi45 |
| 2026-11-17 | [DOC: document how to format a long set of accepted values (GH#28784) …](https://github.com/pandas-dev/pandas/commit/ce59b5ad86978d76fcf93488e95e9d46896fe7b6) | jbrockmendel |
| 2026-11-17 | [DOC: document differences between python and pyarrow string storage (…](https://github.com/pandas-dev/pandas/commit/06071de90b02d0efac5c4b0e819d33f95a61e492) | jbrockmendel |
| 2026-11-17 | [DOC: fix HDFStore.put/append and to_hdf `index` parameter docs (GH#60…](https://github.com/pandas-dev/pandas/commit/d91dc497e35e1576c51d3ccf4d6c8c6824701485) | jbrockmendel |
| 2026-11-17 | [TST: read_parquet with dtype_backend="pyarrow" and a tz-aware index (…](https://github.com/pandas-dev/pandas/commit/6dfef9f240fdb85099745fc8ef55b8a53f966bda) | jbrockmendel |
| 2026-11-17 | [BUG: qcut raises with infinite values (#69918)](https://github.com/pandas-dev/pandas/commit/fda69e407ee1aae34997938f91984677b1539407) | fabiovincenzi |
| 2026-11-16 | [DOC: warn that to_excel writes strings starting with "=" as formulas …](https://github.com/pandas-dev/pandas/commit/3f78c15dd01c22bea029ef4e56de3cabd29e4d31) | jbrockmendel |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
