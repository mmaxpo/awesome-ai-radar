# benfred/py-spy

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/benfred/py-spy)

> Sampling profiler for Python programs

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | Sampling profiler: see where a running Python program spends time |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 15.6k |
| 🍴 **Forks** | 560 |
| 🐞 **Open issues + PRs** | [235](https://github.com/benfred/py-spy/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `profiler` `python` `performance-analysis` `profiling` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2018-08-01 |
| 📦 **Latest release** | [v0.4.3](https://github.com/benfred/py-spy/releases/tag/v0.4.3) — 2026-11-02 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 3.5 MB |

## 📦 Recent releases

### [v0.4.3](https://github.com/benfred/py-spy/releases/tag/v0.4.3)
<sub>2026-11-02 · 12d ago</sub>

> **Changes**
> **🚀 Features**
> - Python 3.15 support @benfred (#878)
> - Add Windows ARM64 wheels @ndabas (#867)
> - Format function names with qualname for Python 3.11+ @jake-kramer (#825)
> - Classify 3.12+ frames by owner and mask stackref tag bits @korniltsev-grafanista (#884)
> …

### [v0.4.2](https://github.com/benfred/py-spy/releases/tag/v0.4.2)
<sub>2026-04-24 · 6mo ago</sub>

> **Changes**
> **🚀 Features**
> - Add Python 3.14 support @benfred (#833)
> - Add support for native extensions on linux aarch64  @tehrengruber (#779)
> - Use Py\_Version symbol for detecting the python version @benfred (#835)
> - Show backtrace on errors when RUST\_BACKTRACE=1 environment variable is set @benfred (#841)
> …

### [v0.4.1](https://github.com/benfred/py-spy/releases/tag/v0.4.1)
<sub>2025-07-31 · 1y ago</sub>

> **Changes**
> **🚀 Features**
> * Add support for native extensions on ARM (for linux) by @huonw (#330)
> * Add support for displaying numpy scalars by @peytondmurray (#752)
> * make remoteprocess unwind feature optional by @pavelzw (#768)
> * Update pyproject.toml to support installing with latest uv by @l1n (#739)
> …

### [v0.4.0](https://github.com/benfred/py-spy/releases/tag/v0.4.0)
<sub>2024-11-01 · 2y ago</sub>

> **Changes**
> **🚀 Features**
> - Python 3.13 Support @benfred (#708)
> - Python 3.12 support @benfred (#642)
> - Speed up --gil by skipping work for non-GIL threads @wmanley (#630)
> - Detect GIL on python 3.12 @benfred (#713)
> …

### [v0.3.14](https://github.com/benfred/py-spy/releases/tag/v0.3.14)
<sub>2022-09-07 · 4y ago</sub>

> **Changes**
> **🐛 Bug Fixes**
> - Fix shell completions @benfred (#522)

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Add support for free-threaded python interpreters (#905)](https://github.com/benfred/py-spy/commit/a2ae758b893f41925ec31d5de2659c3d655534a1) | benfred |
| 2026-11-14 | [Avoid console layout underflow in small terminals (#897)](https://github.com/benfred/py-spy/commit/d62c5ec01e0f77507bd657b908453314d114d14e) | daniyyell-dev |
| 2026-11-14 | [Re-enable tests in CI for freebsd (#910)](https://github.com/benfred/py-spy/commit/b6b66c91194ba2ca6b610937c5962a3e1ba4c8c8) | benfred |
| 2026-11-14 | [Fix panic on FreeBSD when reading undefined nonblocking flag (#903)](https://github.com/benfred/py-spy/commit/f382a5cead1a09a970bf26b93f5c755b3b140782) | KGuillemot |
| 2026-11-14 | [Fix empty interpreter section scans (#907)](https://github.com/benfred/py-spy/commit/b36c8daf2b653beed82b0446f8da1b372081bc17) | theomonnom |
| 2026-11-09 | [Refactor interpreter macros (#904)](https://github.com/benfred/py-spy/commit/c53bfe136535cb525a35ded61e9afac35754e522) | benfred |
| 2026-11-03 | [Add optional type checks for code, string and dict objects (#885)](https://github.com/benfred/py-spy/commit/7a7ac96e96e0f9b4ba3eee80de3f4d255698170b) | korniltsev-grafanista |
| 2026-11-02 | [Bump version: 0.4.2 → 0.4.3](https://github.com/benfred/py-spy/commit/77862e3027a7fef38c113bf4e9f1f2803e363bee) | benfred |
| 2026-11-02 | [Update GHA to use python 3.14 by default (#901)](https://github.com/benfred/py-spy/commit/ed39324ebbc1fd7a9ca0479905a6302b8669f2e3) | benfred |
| 2026-10-27 | [Update tested python versions (#896)](https://github.com/benfred/py-spy/commit/353afa6ff5bb322730c80abfc3372b2d1159de8c) | github-actions[bot] |

[See all commits ↗](https://github.com/benfred/py-spy/commits)

## ⬇️ Get it

```bash
git clone https://github.com/benfred/py-spy.git
```
