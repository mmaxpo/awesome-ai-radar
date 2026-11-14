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
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 414.2 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 9d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 22d ago</sub>

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
| 2026-11-13 | [API: make bool[pyarrow] arithmetic match numpy/masked bools (GH#63064…](https://github.com/pandas-dev/pandas/commit/039a4f7a5207fcd41ab4699b49b4abf701e3bc26) | jbrockmendel |
| 2026-11-13 | [BUG: read_csv true_values ignored for boolean EAs other than BooleanD…](https://github.com/pandas-dev/pandas/commit/0d4d199e5be5927c3369c6fbda5e1f6c2eb5fa8d) | jbrockmendel |
| 2026-11-13 | [BUG: treat NaN as missing in a str list passed to ArrowDtype (GH#6457…](https://github.com/pandas-dev/pandas/commit/c1cc047cfede6271a49491e813a60bb2b05cc3ab) | jbrockmendel |
| 2026-11-13 | [DEPR: DataFrame.agg with a callable producing a DataFrame (GH#49673) …](https://github.com/pandas-dev/pandas/commit/28f4539a08e1bbfe5ed61203f2c7897eff558dd1) | jbrockmendel |
| 2026-11-13 | [DOC: explain that a multiplied Period freq does not bin timestamps (G…](https://github.com/pandas-dev/pandas/commit/ff36f3782158e049f6ab1d1889666b9d53cbee6a) | jbrockmendel |
| 2026-11-13 | [BUG: drop with a bytes or __getitem__-only label (GH#11740) (#72039)](https://github.com/pandas-dev/pandas/commit/f3ac88afebf835ad00f96ec1196045c794234f43) | jbrockmendel |
| 2026-11-13 | [ENH: Python fallback for groupby cumulative ops (GH#49758) (#72073)](https://github.com/pandas-dev/pandas/commit/f1aaba400a372459303f4e9a8233a247520b3498) | jbrockmendel |
| 2026-11-13 | [BUG: unary -, +, abs on object dtype with None (GH#42862) (#72045)](https://github.com/pandas-dev/pandas/commit/6435169b60254bd7695ac9c476b83b69e41d13ff) | jbrockmendel |
| 2026-11-13 | [Bump prefix-dev/setup-pixi from 0.11.2 to 0.11.3 (#72018)](https://github.com/pandas-dev/pandas/commit/48c41c727e3f286f53d622381a0c82eefdde74fd) | dependabot[bot] |
| 2026-11-13 | [BUG: failed .loc/.at setitem with a new row leaves the row behind (GH…](https://github.com/pandas-dev/pandas/commit/327a750b75093d944f69902925e3e3ba711e39d1) | jbrockmendel |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
