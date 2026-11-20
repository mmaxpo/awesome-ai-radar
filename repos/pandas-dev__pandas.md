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
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2010-08-24 |
| 📦 **Latest release** | [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 417.0 MB |
| 🌐 **Website** | https://pandas.pydata.org |

## 📦 Recent releases

### [v3.1.1](https://github.com/pandas-dev/pandas/releases/tag/v3.1.1) — pandas 3.1.1
<sub>2026-11-04 · 15d ago</sub>

> We are pleased to announce the release of pandas 3.1.1.
> This is a patch release in the 3.1.x series and includes some regression fixes and bug fixes. We recommend that all users of the 3.1.x series upgrade to this version.
> See the [full whatsnew](https://pandas.pydata.org/docs/whatsnew/v3.1.1.html) for a list of all the changes.
> The release can be installed from PyPI:
>     python -m pip install --upgrade pandas==3.1.*
> Or from conda-forge
> …

### [v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0) — pandas 3.1.0
<sub>2026-10-22 · 29d ago</sub>

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
| 2026-11-19 | [CI: Update pixi.lock (#71547)](https://github.com/pandas-dev/pandas/commit/1e36a1be41ed335a5e5ba968c73ced666a883191) | github-actions[bot] |
| 2026-11-19 | [BUG: honor custom __repr__ of container subclasses in repr (GH#18843)…](https://github.com/pandas-dev/pandas/commit/5a96bfa5f03224fb5dd0d895e5eb5f1beda23cf7) | jbrockmendel |
| 2026-11-19 | [BUG: DataFrame.plot raising for DateOffset/Easter index freq (GH#2692…](https://github.com/pandas-dev/pandas/commit/84cfc0ba0fc2bf6365516c0f83bfca2ee247f903) | jbrockmendel |
| 2026-11-19 | [DEPR: indexer_between_time include_start/include_end in favor of incl…](https://github.com/pandas-dev/pandas/commit/d7fa569f2b3a3686289fb34dd9aa2e0ac7cda277) | jbrockmendel |
| 2026-11-19 | [BUG: where/mask with inplace=True ignoring labels missing from cond (…](https://github.com/pandas-dev/pandas/commit/d5f4d6536dd428e7f25734157a3343f95e0b0197) | jbrockmendel |
| 2026-11-19 | [TST: hist(by=, sharex=True) bars follow shared labels for non-numeric…](https://github.com/pandas-dev/pandas/commit/7de707e9987d0e20b7d37ecc7306fb5f797afef1) | jbrockmendel |
| 2026-11-19 | [ENH: route DataFrame._repr_html_ through to_html, add to_html(min_row…](https://github.com/pandas-dev/pandas/commit/15969a95bced0dbd303f8f0fbe1db1b7cb222b2f) | jbrockmendel |
| 2026-11-19 | [BUG: RecursionError in repr of a Series/DataFrame containing itself (…](https://github.com/pandas-dev/pandas/commit/a47e619fd19853abbbe9768826509ef2914cc405) | jbrockmendel |
| 2026-11-19 | [BUG: ewm(adjust=False) wrong result with com=1 and NaN (GH#31178) (#7…](https://github.com/pandas-dev/pandas/commit/7bea84d26835bb98e828e054ea54df1febde92c0) | jbrockmendel |
| 2026-11-18 | [CLN: import directly in pandas/io/_util.py instead of "import pandas …](https://github.com/pandas-dev/pandas/commit/264b9d8f97b579a009f77fb171bf0c24d903604a) | fangchenli |

[See all commits ↗](https://github.com/pandas-dev/pandas/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pandas-dev/pandas.git
```
