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
| 🐞 **Open issues + PRs** | [1.9k](https://github.com/pandas-dev/pandas/issues) |
| 💻 **Languages** | Python 91% · Cython 6% · C 1% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `data-analysis` `pandas` `flexible` `alignment` `python` `data-science` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 416.4 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 12d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 26d ago</sub>

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
| 2026-11-17 | [BUG: qcut raises with infinite values (#69918)](https://github.com/pandas-dev/pandas/commit/fda69e407ee1aae34997938f91984677b1539407) | fabiovincenzi |
| 2026-11-16 | [DOC: warn that to_excel writes strings starting with "=" as formulas …](https://github.com/pandas-dev/pandas/commit/3f78c15dd01c22bea029ef4e56de3cabd29e4d31) | jbrockmendel |
| 2026-11-16 | [TST: add test for DataFrame subclass _metadata propagation in arithme…](https://github.com/pandas-dev/pandas/commit/d61c278a7c7a4c9f0b90f135a1d94b86ddd25d0c) | dilksh-sharma |
| 2026-11-16 | [REF: use lib.no_default for dtype_backend in sql internals (GH#60326)…](https://github.com/pandas-dev/pandas/commit/d6ae4442e0e83ecd298eceab0737c47f8d0d0e9c) | jbrockmendel |
| 2026-11-16 | [BUG: DataFrame.corr with an array-like passed as method (GH#11260) (#…](https://github.com/pandas-dev/pandas/commit/5d60cda5b9f5839a4270f38f95d704d34d4f6a22) | jbrockmendel |
| 2026-11-16 | [DOC: document how freq affects to_timestamp (GH#59371) (#72116)](https://github.com/pandas-dev/pandas/commit/6172bbfd3d1706309d1854ad0ea8bab927ceca96) | jbrockmendel |
| 2026-11-16 | [BUG: raise ValueError for mismatched-length sparse and period arithme…](https://github.com/pandas-dev/pandas/commit/f388be6f6f64952e05556e05309c47d5a7dceaf4) | jbrockmendel |
| 2026-11-16 | [BUG: DataFrame.boxplot labels with array-like by (GH#23007) (#72130)](https://github.com/pandas-dev/pandas/commit/54182b0b3b5879337a3acd5e8ca4ab086d525d14) | jbrockmendel |
| 2026-11-16 | [BUG: validate fill value in datetimelike array fillna with no NAs (GH…](https://github.com/pandas-dev/pandas/commit/2dfd09679c3a2cfb1c5a70e8561f20abb6912895) | jbrockmendel |
| 2026-11-16 | [CI: use -n auto with mypy (#72147)](https://github.com/pandas-dev/pandas/commit/4ef16d6007b5293e04e2a957d103374e53bc780b) | rhshadrach |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
