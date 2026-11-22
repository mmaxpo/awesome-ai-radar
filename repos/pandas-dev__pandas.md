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
| 🍴 **Forks** | 20.7k |
| 🐞 **Open issues + PRs** | [1.8k](https://github.com/pandas-dev/pandas/issues) |
| 💻 **Languages** | Python 91% · Cython 6% · C 1% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | `data-analysis` `pandas` `flexible` `alignment` `python` `data-science` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 417.0 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 17d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 1mo ago</sub>

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
<sub>2026-07-22 · 4mo ago</sub>

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
| 2026-11-22 | [BUG: clear error for a scalar row after a list-like row (GH#29213) (#…](https://github.com/pandas-dev/pandas/commit/ef7d968a259a987dd9e5a6d03878f627d5fbf980) | jbrockmendel |
| 2026-11-21 | [BUG: plotting into one shared axes hid tick labels on its siblings (G…](https://github.com/pandas-dev/pandas/commit/65e672976359106dcbed3fdce142f71b13ed5cb8) | jbrockmendel |
| 2026-11-21 | [PERF: don't build the engine in Index.is_monotonic_* to check its typ…](https://github.com/pandas-dev/pandas/commit/c3e8e6fd853f56e3e448fdc46f8588d90e651356) | fangchenli |
| 2026-11-21 | [BUG: raise clear error for to_csv binary mode without a path (GH#4440…](https://github.com/pandas-dev/pandas/commit/ba8e1eec3ed70cf62772178de34e16096817b24c) | jbrockmendel |
| 2026-11-21 | [BUG: strict ISO 8601 duration parsing in Timedelta (GH#51882) (#72136)](https://github.com/pandas-dev/pandas/commit/a22c4b5f3b3c413d343c7a809f6c90504f2ef3d3) | jbrockmendel |
| 2026-11-21 | [TST: test sort=True as well in value_counts sort base EA test (#72249)](https://github.com/pandas-dev/pandas/commit/4500a5dc85b158873428ec768ef2bb39367e1d77) | jorisvandenbossche |
| 2026-11-21 | [BUG: Styler.to_excel reads border color names as widths (GH#71305) (#…](https://github.com/pandas-dev/pandas/commit/50c774dee7eb8f4dd9296f3676ed99231f41bd3f) | zeyadrabie |
| 2026-11-20 | [BUG: Grouper(freq).value_counts raising with NaT in the grouped index…](https://github.com/pandas-dev/pandas/commit/ca8d2daa1bf8f30f4d1ce26dfad6792f590e298d) | jbrockmendel |
| 2026-11-20 | [ENH: nlargest/nsmallest on non-numeric dtypes (GH#61166) (#72188)](https://github.com/pandas-dev/pandas/commit/ea9adce7db97709a477308467c90c2ee24d23d60) | jbrockmendel |
| 2026-11-20 | [DOC: document how to write a custom offset (GH#35569) (#72239)](https://github.com/pandas-dev/pandas/commit/0d1cca392cc1302ee02b797a5b42e9a4071cffce) | jbrockmendel |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
