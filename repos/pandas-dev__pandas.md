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
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 417.0 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 21d ago</sub>

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
| 2026-11-25 | [Bump astral-sh/setup-uv from 10.3.3 to 10.4.0 (#72324)](https://github.com/pandas-dev/pandas/commit/52552c59c1bd99db676b8eb103f591ee8cf1d93d) | dependabot[bot] |
| 2026-11-24 | [CI: Add Python 3.15 CI jobs instead of python-dev; consolidate CI set…](https://github.com/pandas-dev/pandas/commit/a0885a1054bb9a91f10584944a613062cdebdc5c) | mroeschke |
| 2026-11-24 | [BUG: convert_dtypes(dtype_backend="numpy_nullable") KeyError for unma…](https://github.com/pandas-dev/pandas/commit/b048c155d9aebfafabd11bee3dd8b6ba839d6a3e) | jbrockmendel |
| 2026-11-24 | [PERF: avoid per-element group labels in nullable DataFrame axis=1 red…](https://github.com/pandas-dev/pandas/commit/6151915091dfeeb20542de7f31e21cf15782a580) | rhshadrach |
| 2026-11-23 | [BUG: MultiIndex.sortlevel ignores values of out-of-order levels (GH#5…](https://github.com/pandas-dev/pandas/commit/8c7cd24e9e03ba800d1eafcf5da21c9f3ac2861d) | jbrockmendel |
| 2026-11-23 | [PERF: wrap Arrow libjoin output directly in Index._from_join_target (…](https://github.com/pandas-dev/pandas/commit/9d8d3f4e970ae9351c4b8ed3bf1581c8e00d9f77) | fangchenli |
| 2026-11-23 | [BUG: misplaced overlay of off-period time series on a period axis (GH…](https://github.com/pandas-dev/pandas/commit/d68ece3856df62c1f29fc2ea0b80a1f49ad6383a) | jbrockmendel |
| 2026-11-23 | [BUG: Styler title-mode tooltips misplaced or IndexError when rows are…](https://github.com/pandas-dev/pandas/commit/6b828d5d82b5ba324ad6817dad0055250650cecc) | NodeX-AR |
| 2026-11-23 | [BUG: CategoricalIndex.__contains__ wrong result with RangeIndex categ…](https://github.com/pandas-dev/pandas/commit/176746ab7693e3e4eb5ee53fbc0ddc47ebe09f00) | sainimal1ba-hue |
| 2026-11-22 | [CI: Update pixi.lock (#72272)](https://github.com/pandas-dev/pandas/commit/717bcd3eda554a0b2e826889f9e30efbd88f00cd) | github-actions[bot] |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
