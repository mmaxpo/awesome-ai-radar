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
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 413.7 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 7d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 20d ago</sub>

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
| 2026-11-11 | [CI: Upgrade to mypy 2.4 (#71956)](https://github.com/pandas-dev/pandas/commit/f1cc1a1bc979b83e641facf72ec6526593d61420) | rhshadrach |
| 2026-11-11 | [TST: groupby rolling with sort=False keeps group order (GH 50296) (#7…](https://github.com/pandas-dev/pandas/commit/b8f5d0c43c2b8fb9b7c897692c7191de8c71f9e5) | VividhDesign |
| 2026-11-11 | [REGR: pyarrow read_csv parse_dates stringifies a non-date index_col (…](https://github.com/pandas-dev/pandas/commit/5fa9a0224b32b35f47381ad9be0990c1fda17a70) | jbrockmendel |
| 2026-11-10 | [DOC/CHORE: Make links to documentation consistent (#71720)](https://github.com/pandas-dev/pandas/commit/862b799071c6fa18814da256dfa27ea61813ac8a) | afeld |
| 2026-11-10 | [BUG: exact Series/DataFrame.quantile for datetimelike with linear/mid…](https://github.com/pandas-dev/pandas/commit/0b07bb9af63c6bb2bee34d28cebcb15eb879b3be) | aniyow07 |
| 2026-11-10 | [BUG: read_csv dropping leading whitespace at a read boundary (GH#3408…](https://github.com/pandas-dev/pandas/commit/3c83c0502a09af1b318a91cb085055e8cee17351) | jbrockmendel |
| 2026-11-10 | [BUG: read_csv(engine="pyarrow") failed on a single line without a tra…](https://github.com/pandas-dev/pandas/commit/0d39e6e3afa2e45fb395e0b05ce3aed9fcd46e92) | jbrockmendel |
| 2026-11-10 | [DOC: move Merge intro above Concat in 10 minutes guide (#71999)](https://github.com/pandas-dev/pandas/commit/4d70fad9dc1f4403b91961c35ddcfdaff803e8e8) | laraib-b |
| 2026-11-10 | [DOC: move GH#71875 whatsnew entry from 3.1.2 to 3.2.0 (#72001)](https://github.com/pandas-dev/pandas/commit/436864644d964d907459daedb2b5f0ba8065f7da) | jbrockmendel |
| 2026-11-10 | [BUG: value_counts on nullable dtypes places NA at first appearance (#…](https://github.com/pandas-dev/pandas/commit/65b0cec89317e66f71017092891c1a81eec8ae31) | jbrockmendel |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
