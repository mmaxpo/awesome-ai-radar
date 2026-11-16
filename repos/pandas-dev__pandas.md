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
| 💾 **Size** | 414.0 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 11d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 25d ago</sub>

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
| 2026-11-15 | [BUG: read_fwf raising TypeError with callable skiprows (GH#20603) (#7…](https://github.com/pandas-dev/pandas/commit/90acce7c7cb3c663c54e4286b5065fc9c8ac63df) | jbrockmendel |
| 2026-11-15 | [ENH: future.python_scalars for Series.tolist and Series.asof (#72108)](https://github.com/pandas-dev/pandas/commit/ed6da921d4059c29a6ae33f5982c561b8f6ccdef) | rhshadrach |
| 2026-11-15 | [BUG: localize zoneinfo datetimes outside the stdlib datetime range (G…](https://github.com/pandas-dev/pandas/commit/535937a3c69f457da03bf286c11251aaf571c9d7) | hatemadi15 |
| 2026-11-15 | [BUG: datetimelike add/sub with mismatched-length object array raised …](https://github.com/pandas-dev/pandas/commit/cd645faac4724e6e47b2d185efd0a8ade36aa9c1) | jbrockmendel |
| 2026-11-15 | [BUG: fix DataFrame.plot.area and Series.plot.area on timedelta64 data…](https://github.com/pandas-dev/pandas/commit/31b8d905ba690cff9b5d128e5bb4538cd42ecf96) | mutasim-rehman |
| 2026-11-15 | [BUG: DataFrame.plot raising KeyError when y includes the x column (GH…](https://github.com/pandas-dev/pandas/commit/c3d923fd790e90688322d1044c3cfe6bea21fc0d) | jbrockmendel |
| 2026-11-15 | [PERF: keep 1D extension arrays of a frame other in DataFrame.where (#…](https://github.com/pandas-dev/pandas/commit/8fc0bad7783462f0a9c07f1712926455166cbf14) | fangchenli |
| 2026-11-15 | [Sort values preserve object dtype (#72126)](https://github.com/pandas-dev/pandas/commit/03896c8905044c2061f82d279ea3bcdc77c6ea43) | mutasim-rehman |
| 2026-11-15 | [TST: in-place clip with a float64 bound float32 cannot hold raises (G…](https://github.com/pandas-dev/pandas/commit/9706798e04ad221928bfa4890e0a33b69d7e6204) | jbrockmendel |
| 2026-11-15 | [DOC: Fix minor wording in the 10 minutes to pandas guide (#72125)](https://github.com/pandas-dev/pandas/commit/b37001eda679503bac78c45b08e02c14a8b313b8) | Youeeeee |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
