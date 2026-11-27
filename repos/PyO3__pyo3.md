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
| 🐞 **Open issues + PRs** | [406](https://github.com/PyO3/pyo3/issues) |
| 💻 **Languages** | Rust 96% · Python 4% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `rust` `python` `binding` `ffi` `python-c-api` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2017-05-13 |
| 📦 **Latest release** | [v0.30.1](https://github.com/PyO3/pyo3/releases/tag/v0.30.1) — 2026-10-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 61.9 MB |
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
| 2026-11-27 | [internal: tests: fixes a name conflict between capsules (#6608)](https://github.com/PyO3/pyo3/commit/143012921bf66cb36e964a1e38b1292a4ed919d8) | Tpt |
| 2026-11-27 | [fix: wrap slot method calls in unsafe blocks (#6612)](https://github.com/PyO3/pyo3/commit/250c626587ad0562e3ab501fad9d461c072900d5) | rytheo |
| 2026-11-27 | [pypy3.12 v8.1 uses CPython's datetime, buffer structs (#6611)](https://github.com/PyO3/pyo3/commit/69d9ba67b479888706c0bb9a0048ac014b537a1f) | mattip |
| 2026-11-27 | [conditionally include `std` crate (#6511)](https://github.com/PyO3/pyo3/commit/49dfe58e9e142bba0efdf6733009d10473c6d3fb) | Person-93 |
| 2026-11-26 | [build(deps-dev): bump rumdl from 0.3.4 to 0.3.5 in the uv-tools group…](https://github.com/PyO3/pyo3/commit/a7f891a1c598322cd86fd6f1a5585000e8ced9d1) | dependabot[bot] |
| 2026-11-26 | [build(deps): bump fast-uri in /ci/tools/netlify (#6623)](https://github.com/PyO3/pyo3/commit/191f98b28b2a01cb7147a7a36d6bdd762f5d5faa) | dependabot[bot] |
| 2026-11-26 | [build(deps): bump follow-redirects in /ci/tools/netlify (#6617)](https://github.com/PyO3/pyo3/commit/4a8f7c560e2f819d911f0238121b4c6c6003a14b) | dependabot[bot] |
| 2026-11-26 | [Fix attachment during interpreter finalization (#6564) (#6578)](https://github.com/PyO3/pyo3/commit/1999ba861fab73c9292cc44faf325f4ba30e0fd0) | exg |
| 2026-11-26 | [build(deps): bump body-parser from 2.3.0 to 2.4.0 in /ci/tools/netlif…](https://github.com/PyO3/pyo3/commit/2f0191dd67094290be8ea2693e5297006c8fadbb) | dependabot[bot] |
| 2026-11-26 | [build(deps): bump qs from 6.16.0 to 6.17.1 in /ci/tools/netlify (#6624)](https://github.com/PyO3/pyo3/commit/6208a7b806b2b50c76db33cafb028e87e012cbe2) | dependabot[bot] |

[See all commits ↗](https://github.com/PyO3/pyo3/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PyO3/pyo3.git
```
