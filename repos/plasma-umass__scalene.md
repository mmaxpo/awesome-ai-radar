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
| 🍴 **Forks** | 448 |
| 🐞 **Open issues + PRs** | [153](https://github.com/plasma-umass/scalene/issues) |
| 💻 **Languages** | Python 59% · JavaScript 16% · C++ 9% · TypeScript 8% · Lean 7% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `profiling` `performance-analysis` `cpu-profiling` `profiler` `python-profilers` `gpu-programming` `scalene` `profiles-memory` `performance-cpu` `cpu` `memory-allocation` `gpu` `memory-consumption` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2019-12-17 |
| 📦 **Latest release** | [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — 2026-10-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 20.3 MB |

## 📦 Recent releases

### [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — Free-threaded wheels, M4 fix, safer API keys, and formal verification
<sub>2026-10-23 · 22d ago</sub>

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
<sub>2026-02-15 · 9mo ago</sub>

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
| 2026-11-15 | [Give every timer arrival the same weight (#466 follow-up) (#1142)](https://github.com/plasma-umass/scalene/commit/0b9870bfa09aecc7e2eb8826dbd483214d4a763f) | emeryberger |
| 2026-11-15 | [Charge CPU samples to the line running when the timer fired (fixes #4…](https://github.com/plasma-umass/scalene/commit/9893aa606aadf138f0bad0adf79f0265b3724a52) | emeryberger |
| 2026-11-15 | [Windows: remove the Python sampler-thread fallback (#1141)](https://github.com/plasma-umass/scalene/commit/9daac986a3b9d9799f230f1af4198115090fa99e) | emeryberger |
| 2026-11-14 | [Don't sample allocations inside native stack unwinding (fixes #1133) …](https://github.com/plasma-umass/scalene/commit/377176057b41172579937f4e71dc5bdf83a5c875) | emeryberger |
| 2026-11-14 | [Count loop body lines in function CPU totals (fixes #1131) (#1137)](https://github.com/plasma-umass/scalene/commit/37951a9611f772b8b400e4b6f4964d0baf69a35e) | emeryberger |
| 2026-11-14 | [Track line ends from the profiled frame's depth (fixes #1132) (#1138)](https://github.com/plasma-umass/scalene/commit/c1a955bddaa5428e577c81a1a6ce73829d0ddb2f) | emeryberger |
| 2026-11-14 | [Don't block SIGALRM in os functions that start programs (fixes #1134)…](https://github.com/plasma-umass/scalene/commit/07d428a1195480a49ef94aa9b883866845bcc0a2) | emeryberger |
| 2026-11-14 | [Sample Windows CPU from a native timer thread that trips the CPU sign…](https://github.com/plasma-umass/scalene/commit/e820eb1ce0dd93ef9179ae907271fe0aab685a85) | emeryberger |
| 2026-11-14 | [Classify signal-path CPU samples by when the timer signal arrived (#1…](https://github.com/plasma-umass/scalene/commit/122cdfc80d99f50b14ad3141f93f28379bd7ddc2) | emeryberger |
| 2026-11-14 | [Build and smoke-test wheels on every PR; fix CPU attribution on Windo…](https://github.com/plasma-umass/scalene/commit/057c01074f56b65c5ec941b1ef32c4346e13c3a3) | emeryberger |

[See all commits ↗](https://github.com/plasma-umass/scalene/commits)

## ⬇️ Get it

```bash
git clone https://github.com/plasma-umass/scalene.git
```
