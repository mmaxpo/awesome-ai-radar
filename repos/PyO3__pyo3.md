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
| ⭐ **Stars** | 16.3k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [415](https://github.com/PyO3/pyo3/issues) |
| 💻 **Languages** | Rust 96% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `rust` `python` `binding` `ffi` `python-c-api` |
| 🕒 **Last activity** | 2026-11-08 (2d ago) |
| 📅 **Created** | 2017-05-13 |
| 📦 **Latest release** | [v0.30.1](https://github.com/PyO3/pyo3/releases/tag/v0.30.1) — 2026-10-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 62.5 MB |
| 🌐 **Website** | https://pyo3.rs |

## 📦 Recent releases

### [v0.30.1](https://github.com/PyO3/pyo3/releases/tag/v0.30.1) — PyO3 0.30.1
<sub>2026-10-14 · 27d ago</sub>

> PyO3 0.30.1 is a re-release of PyO3 0.30.0 after investments in CI security unfortunately led to a failed crates.io publish. Rather than delete the failed tag, this new tag comes after the CI issues have (hopefully) been corrected.
> Thanks to @davidhewitt @Tpt and @viicos for the investigation and fixes.

### [v0.30.0](https://github.com/PyO3/pyo3/releases/tag/v0.30.0) — PyO3 0.30.0
<sub>2026-10-13 · 28d ago</sub>

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
| 2026-11-02 | [feat: introduce stack-allocated `PyBuffer` (#5894)](https://github.com/PyO3/pyo3/commit/f41d7e8799cad7f1c393d00276a4fa7b83acf885) | winstxnhdw |
| 2026-11-02 | [build(deps): bump the github-actions group with 2 updates (#6567)](https://github.com/PyO3/pyo3/commit/3057df68bc6e3539cba9e34dc78be7473a307cbd) | dependabot[bot] |
| 2026-11-01 | [fix cases of incorrect allocator or deallocator inheritance (#6559)](https://github.com/PyO3/pyo3/commit/aa0a05f792cdac4290021ec01c9adb6fc23e4a14) | davidhewitt |
| 2026-10-26 | [build(deps): bump the github-actions group with 7 updates (#6556)](https://github.com/PyO3/pyo3/commit/26f9ec8be637d24d0dee18d51e129cc1a99f3a7c) | dependabot[bot] |
| 2026-10-26 | [build(deps): update scraper requirement in /pyo3-ffi-check (#6554)](https://github.com/PyO3/pyo3/commit/48ab34bf607ea71b0db83214b93db46840b455d1) | dependabot[bot] |
| 2026-10-25 | [build(deps): bump filelock from 3.19.1 to 3.20.3 (#6549)](https://github.com/PyO3/pyo3/commit/79627d8f830ce65a941725983fc55742160832aa) | dependabot[bot] |
| 2026-10-25 | [build(deps): bump virtualenv from 16.7.12 to 21.14.13 (#6546)](https://github.com/PyO3/pyo3/commit/cb2b7eecb5c707598bba085de8d286d6392f0bc3) | dependabot[bot] |
| 2026-10-25 | [build(deps): bump filelock from 3.19.1 to 3.20.3 (#6547)](https://github.com/PyO3/pyo3/commit/fe8531fcd58e1961ed2fc665cde363a6ba7386a6) | dependabot[bot] |
| 2026-10-24 | [build(deps): bump the github-actions group with 2 updates (#6533)](https://github.com/PyO3/pyo3/commit/fda3c5846d30042c9352885f415435c06f2e4985) | dependabot[bot] |
| 2026-10-23 | [Use `PyType_FastSubclass` on `RustPython` (#6541)](https://github.com/PyO3/pyo3/commit/424149e8a1c42128b05a090941673008fc46c478) | bschoenmaeckers |

[See all commits ↗](https://github.com/PyO3/pyo3/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PyO3/pyo3.git
```
