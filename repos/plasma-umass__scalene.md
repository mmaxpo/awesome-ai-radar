# plasma-umass/scalene

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/plasma-umass/scalene)

> Scalene: a high-performance, high-precision CPU, GPU, and memory profiler for Python with AI-powered optimization proposals

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | CPU/GPU/memory profiler for Python with AI optimization tips |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 13.6k |
| 🍴 **Forks** | 447 |
| 🐞 **Open issues + PRs** | [156](https://github.com/plasma-umass/scalene/issues) |
| 💻 **Languages** | Python 60% · JavaScript 16% · C++ 8% · TypeScript 7% · Lean 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `cpu` `cpu-profiling` `gpu` `gpu-programming` `memory-allocation` `memory-consumption` `performance-analysis` `performance-cpu` `profiler` `profiles-memory` `profiling` `python` `python-profilers` `scalene` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2019-12-17 |
| 📦 **Latest release** | [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — 2026-10-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 19.5 MB |

## 📦 Recent releases

### [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — Free-threaded wheels, M4 fix, safer API keys, and formal verification
<sub>2026-10-23 · 18d ago</sub>

> **What's Changed**
> **Headlines**
> * **Free-threaded Python wheels on PyPI:** `cp313t` and `cp314t` wheels for macOS and Windows, and `cp314t` for Linux. Release builds now check that every wheel's native modules import, and that on free-threaded builds they don't re-enable the GIL.
> * **Apple Silicon M4+ fix:** on chips with SME, profiling numpy/Accelerate code could silently corrupt numerical results (#1056). CPU sampling on those chips no longer uses signals.
> * **Safer AI-provider keys:** API keys are never embedded in generated HTML. The new opt-in `scalene view --api-keys-from-env` serves them from memory over localhost instead. The GUI is now served from a private directory rather than the whole temp dir.
> * **Correctness:** fixes found by new formal models (TLA+ and Lean) of Scalene's sampling and attribution, including several divide-by-zero and unbounded-sampling bugs.
> …

### [v2.3.0](https://github.com/plasma-umass/scalene/releases/tag/v2.3.0) — New visualizations, accuracy improvements, and bug fixes
<sub>2026-05-12 · 6mo ago</sub>

> **What's Changed**
> **Headlines**
> * Adds call graphs ("flame graphs") spanning from Python to native code, organized by % of time
> * Timeline view of call graphs ("flame chart"), including GIL, I/O, and GC activity
> * Flame graph for memory allocations, attributing memory to call stacks
> * Improved memory attribution (now tracked per-thread)
> …

### [v2.2.1](https://github.com/plasma-umass/scalene/releases/tag/v2.2.1) — Scalene v2.2.1
<sub>2026-03-22 · 7mo ago</sub>

> **Scalene v2.2.1**
> **Bug Fixes**
> - **sys.monitoring tool ID conflict with PyTorch** (#1015, #1019): Fixed SIGSEGV crash when using Scalene with PyTorch Lightning on Python 3.12+. When PROFILER_ID is already claimed by another tool, Scalene now falls back to alternative tool IDs (3 or 4), or gracefully uses the legacy `PyEval_SetTrace` tracer.
> - **TensorFlow 2.21+ compatibility** (#1018): Fixed compatibility with TensorFlow 2.21+ where `trace.enabled` changed from a callable to a bool. Scalene now applies a compatibility fix at profiler start time.
> - **Multiprocessing resource tracker** (#1017): Fixed `BrokenPipeError` on NixOS with Python 3.13/3.14 when the resource tracker subprocess dies during semaphore creation. Scalene now falls back from `spawn`/`forkserver` to `fork` context.
> - **Subprocess profiling** (#1013): Fixed profiling failing when Python interpreter flags (like `-B` or `-u`) precede `-c` or `-m` in subprocess invocations.
> …

### [v2.1.4](https://github.com/plasma-umass/scalene/releases/tag/v2.1.4) — Maintenance release with bugfixes and performance improvements
<sub>2026-02-15 · 8mo ago</sub>

> **What's Changed**
> * Refined attribution approach for C vs. Python by @emeryberger in https://github.com/plasma-umass/scalene/pull/1001
> * Fix Python 3.14 compatibility for eval()/exec() keyword arguments by @emeryberger in https://github.com/plasma-umass/scalene/pull/1002
> * Fix memory explosion and extreme slowness during profiling by @emeryberger in https://github.com/plasma-umass/scalene/pull/1004
> **Full Changelog**: https://github.com/plasma-umass/scalene/compare/v2.1.3...v2.1.4

### [v2.1.3](https://github.com/plasma-umass/scalene/releases/tag/v2.1.3) — Improved attribution, off-line mode, and fix for Jupyter
<sub>2026-01-31 · 9mo ago</sub>

> **What's Changed**
> * Fix loop backward-jump sampling bias with even redistribution by @emeryberger in https://github.com/plasma-umass/scalene/pull/995
> * Fix Google Analytics loading delay in offline/standalone mode by @Copilot in https://github.com/plasma-umass/scalene/pull/996
> * Fixed Jupyter magics. by @emeryberger in https://github.com/plasma-umass/scalene/pull/997
> **Full Changelog**: https://github.com/plasma-umass/scalene/compare/v2.1.2...v2.1.3

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [Stop unrecognized `scalene run` options leaking into the program's argv (#1115)](https://github.com/plasma-umass/scalene/commit/da91e587fa5a0f5a4416250a628c88ff02638f30) | emeryberger |
| 2026-11-10 | [Reuse the memory sample log and stop @profile churn (fixes #1122) (#1124)](https://github.com/plasma-umass/scalene/commit/9ed244c78241ef364446288add351912e7bcf206) | emeryberger |
| 2026-11-10 | [Fix badge formatting in README.md](https://github.com/plasma-umass/scalene/commit/b8a58ca6f932ca2ab683d7795790ebf489a37d82) | emeryberger |
| 2026-11-10 | [Don't import inside the CPU signal handler (fixes intermittent KeyError) (#1114)](https://github.com/plasma-umass/scalene/commit/4ed3e601f87bffdc1e868c8aedf4f919344c4710) | emeryberger |
| 2026-11-09 | [Reference-count the TraceConfig instance instead of deleting it in place (#1121)](https://github.com/plasma-umass/scalene/commit/d5b59aff9ceeb0b3335a1253d83568f3348778bb) | emeryberger |
| 2026-11-09 | [Stop SampleFile writing past the end of the sample log (#1120)](https://github.com/plasma-umass/scalene/commit/ba0896d85ede0c799545e3bc5589729c73738571) | emeryberger |
| 2026-11-09 | [Stop TraceConfig leaking references to its Python arguments (fixes #1116) (#1119)](https://github.com/plasma-umass/scalene/commit/65f5c604432cd934275831e3a56a41c3a64bb639) | emeryberger |
| 2026-11-09 | [Bound get_line_atomic's newline search by the signal buffer (fixes #1117) (#1118)](https://github.com/plasma-umass/scalene/commit/75f784f5b72be60ae634dd72f9cc7ae42bab003d) | emeryberger |
| 2026-11-01 | [CI: check black formatting instead of auto-committing it (#1112)](https://github.com/plasma-umass/scalene/commit/0ca44cd4345b07104ed05f37c8849b51db35f2e5) | emeryberger |
| 2026-11-01 | [ci: move workflows to current action versions and read-only tokens (#1111)](https://github.com/plasma-umass/scalene/commit/52f8c4c24b892c883e7f9f2c7e8291063498ce67) | jakob1379 |

[See all commits ↗](https://github.com/plasma-umass/scalene/commits)

## 👥 Top contributors

[emeryberger](https://github.com/emeryberger) (2814) · [jaltmayerpizzorno](https://github.com/jaltmayerpizzorno) (346) · [sternj](https://github.com/sternj) (149) · [dependabot[bot]](https://github.com/dependabot[bot]) (17) · [Insutanto](https://github.com/Insutanto) (11)

## ⬇️ Get it

```bash
git clone https://github.com/plasma-umass/scalene.git
```
