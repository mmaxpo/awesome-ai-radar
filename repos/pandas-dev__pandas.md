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
| 🕒 **Last activity** | 2026-11-12 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 413.6 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 8d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 21d ago</sub>

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
| 2026-11-12 | [ENH: add numeric_only to GroupBy.ohlc and Resampler.ohlc (GH#56946) (…](https://github.com/pandas-dev/pandas/commit/e37bffd68f510abf69533d410a38de055ef9fbd2) | jbrockmendel |
| 2026-11-12 | [BUG: treat str.get_dummies separators literally (#70812)](https://github.com/pandas-dev/pandas/commit/0b99851b0d29ec23b70c9b6b04abfed08a2cd882) | AntsiferovBogdan |
| 2026-11-12 | [BUG: skip NA in object-dtype sum/prod/cumulative ops instead of filli…](https://github.com/pandas-dev/pandas/commit/b67a0ee6193a1b2eed8916871a7a30bcd48ca4fb) | jbrockmendel |
| 2026-11-12 | [BUG: ts plot redraws series removed by ax.clear()/line.remove() (GH#5…](https://github.com/pandas-dev/pandas/commit/58f3ff2b94ddf9c1e6c23eee1a6afba84fde73df) | jbrockmendel |
| 2026-11-12 | [BUG: read_fwf silently ignored unknown keyword arguments (GH#34953) (…](https://github.com/pandas-dev/pandas/commit/75a4d0e311f63777afef3f5a80c7625b7d7919ab) | jbrockmendel |
| 2026-11-12 | [BUG: to_html datetimelike column headers match row labels (GH#10640) …](https://github.com/pandas-dev/pandas/commit/626fd8b4531c341891d6a96814c37d6eb7f2f60e) | jbrockmendel |
| 2026-11-12 | [TST: to_clipboard uses Windows line terminators (GH#11720) (#72026)](https://github.com/pandas-dev/pandas/commit/2a57460ae305973b9386436e8a04d758612b66fa) | jbrockmendel |
| 2026-11-12 | [BUG: read_html reads to_html's index-names row as a column level (GH#…](https://github.com/pandas-dev/pandas/commit/9cbc26357f2908746190a8fad40123fb205b90ca) | jbrockmendel |
| 2026-11-12 | [TST: read_excel with MultiIndex header and index_col after an empty c…](https://github.com/pandas-dev/pandas/commit/4a48cb6e6cb4b3ab8315a880555f1a49ce391db0) | jbrockmendel |
| 2026-11-12 | [TST: loc setitem with scalar column key aligns DataFrame value column…](https://github.com/pandas-dev/pandas/commit/00442c1971b9f53e2657e73d36f5c92c39a2968a) | jbrockmendel |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
