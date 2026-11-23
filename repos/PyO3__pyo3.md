# PyO3/pyo3

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/PyO3/pyo3)

> Rust bindings for the Python interpreter

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | Write fast Python extensions in Rust |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 16.4k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [420](https://github.com/PyO3/pyo3/issues) |
| 💻 **Languages** | Rust 96% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `rust` `python` `binding` `ffi` `python-c-api` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2017-05-13 |
| 📦 **Latest release** | [v0.30.1](https://github.com/PyO3/pyo3/releases/tag/v0.30.1) — 2026-10-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 61.6 MB |
| 🌐 **Website** | https://pyo3.rs |

## 📦 Recent releases

### [v0.30.1](https://github.com/PyO3/pyo3/releases/tag/v0.30.1) — PyO3 0.30.1
<sub>2026-10-14 · 1mo ago</sub>

> PyO3 0.30.1 is a re-release of PyO3 0.30.0 after investments in CI security unfortunately led to a failed crates.io publish. Rather than delete the failed tag, this new tag comes after the CI issues have (hopefully) been corrected.
> Thanks to @davidhewitt @Tpt and @viicos for the investigation and fixes.

### [v0.30.0](https://github.com/PyO3/pyo3/releases/tag/v0.30.0) — PyO3 0.30.0
<sub>2026-10-13 · 1mo ago</sub>

> This release brings confirmed testing against Python 3.15.0 final. Support for Python 3.8 has been dropped. The minimum supported Rust version has also been increased to 1.85.
> The largest sets of improvements come to PyO3 0.29.0's `experimental-inspect` feature, which has received substantial feedback since 0.29.0 and subsequently has seen many refinements to improve the quality and coverage to the generated stubs. Thank you to everyone who has helped to continue to drive this feature towards completion.
> New safe wrappers for `PyFrozenDict` (3.15+) and `PyContext` have been added.
> PyO3 now contains meson build files, which should make it possible for projects using meson-python to more straightforwardly use Rust and PyO3 for additional components.
> Additionally, a number of small optimizations have landed, including:
> - simplifications to core implementations of `PyAnyMethods`,
> …

### [v0.29.3](https://github.com/PyO3/pyo3/releases/tag/v0.29.3) — PyO3 0.29.3
<sub>2026-09-30 · 1mo ago</sub>

> This release is a series of fixes worth landing to the PyO3 0.29 series; the PyO3 0.30 release is planned to follow within a few weeks, however during the development cycle a number of rough edges were discovered which were deemed worth a backport.
> The patch broadly includes:
> - a further fix the to the opt-out of `raw-dylib` linking for Windows introduced in PyO3 0.29.1 (the switch to `raw-dylib` linking was introduced in PyO3 0.29.0),
> - fixes to support GraalPy on windows,
> - a handful of small performance optimizations,
> - a number of non-breaking fixes to the `experimental-inspect` type stub generation (expect more improvements in 0.30), and
> …

### [v0.29.2](https://github.com/PyO3/pyo3/releases/tag/v0.29.2) — PyO3 0.29.2
<sub>2026-08-05 · 3mo ago</sub>

> This patch fixes a regression in PyO3 0.29.1 which broke PyPy 3.11 compatibility (`#[pyclass]` types would crash PyPy on instance deletion).
> A few further fixes have also landed with similar themes to PyO3 0.29.1: fixes to minor reference counting bugs, rough edges which would cause crashes, issues which would cause failed builds, and fixes to `experimental-inspect` type stub generation.
> For a full list of the exact fixes please consult the CHANGELOG.
> Thank you to the following contributors for the improvements:
> @davidhewitt
> @dependabot[bot]
> …

### [v0.29.1](https://github.com/PyO3/pyo3/releases/tag/v0.29.1) — PyO3 0.29.1
<sub>2026-08-02 · 3mo ago</sub>

> This patch is a stack of fixes for PyO3 0.29. Particular themes include:
> - Fixes addressing build failures with newer interpreters such as GraalPy 3.13 and CPython 3.15
> - Fixes resolving potential memory leaks inside `#[pyclass]` implementation internals
> - Fixes to the new `experimental-inspect` type stub machinery
> For a full list of the fixes in these above themes and more, please consult the CHANGELOG.
> Thank you to the following contributors for the improvements:
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Also let dependabot update github actions in `/.github/actions/` (#6599)](https://github.com/PyO3/pyo3/commit/f6aeac96014895c0773230e3c23795f7b9b477e1) | bschoenmaeckers |
| 2026-11-23 | [build(deps): update codspeed-criterion-compat requirement (#6553)](https://github.com/PyO3/pyo3/commit/ddab9f931a014ea3939142274177111fd3645be1) | dependabot[bot] |
| 2026-11-23 | [build(deps): bump the github-actions group with 2 updates (#6595)](https://github.com/PyO3/pyo3/commit/77598f4562cdf49b941cb9bca2eb95f76b94dc61) | dependabot[bot] |
| 2026-11-23 | [Add support for `jiff` V1 (#6584)](https://github.com/PyO3/pyo3/commit/172078950af2d89898cc1297f405dacf85593bcf) | bschoenmaeckers |
| 2026-11-23 | [Introspection: make __new__ return Self (#6384)](https://github.com/PyO3/pyo3/commit/99fafb333f00971b26aa43d5ebe2dbb4ee8229f3) | Tpt |
| 2026-11-23 | [perf: read abi3 `datetime` fields through the descriptor `tp_descr_ge…](https://github.com/PyO3/pyo3/commit/3acfb9b802129301c0d7011e4775038af15554eb) | alexander-beedie |
| 2026-11-19 | [docs: add llm-token-visualizer to README examples (#6586)](https://github.com/PyO3/pyo3/commit/be9e428ab7573552c65aa9e7a7a0c6d14b06fd5d) | Mattbusel |
| 2026-11-19 | [Make `PyFrame` available on `abi3`/`graalpy`/`pypy` (#6589)](https://github.com/PyO3/pyo3/commit/b122a1237643aedf89f16a33a92b6204a498957e) | bschoenmaeckers |
| 2026-11-19 | [Introspection: add `pyprotocol!` to declare protocols in the stubs (#…](https://github.com/PyO3/pyo3/commit/2432980aa4aa42618e4423c449cc8acab8040cc7) | jonasdedden |
| 2026-11-17 | [Use `cfg_select` in `OsStr` conversions (#6587)](https://github.com/PyO3/pyo3/commit/a6addae8948adedafd09b2832edf3fa23d282b16) | bschoenmaeckers |

[See all commits ↗](https://github.com/PyO3/pyo3/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PyO3/pyo3.git
```
