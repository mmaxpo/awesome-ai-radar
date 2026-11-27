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
| 🍴 **Forks** | 450 |
| 🐞 **Open issues + PRs** | [152](https://github.com/plasma-umass/scalene/issues) |
| 💻 **Languages** | Python 60% · JavaScript 15% · C++ 9% · TypeScript 7% · Lean 6% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `profiling` `performance-analysis` `cpu-profiling` `profiler` `python-profilers` `gpu-programming` `scalene` `profiles-memory` `performance-cpu` `cpu` `memory-allocation` `gpu` `memory-consumption` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2019-12-17 |
| 📦 **Latest release** | [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — 2026-10-23 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 20.4 MB |

## 📦 Recent releases

### [v2.4.0](https://github.com/plasma-umass/scalene/releases/tag/v2.4.0) — Free-threaded wheels, M4 fix, safer API keys, and formal verification
<sub>2026-10-23 · 1mo ago</sub>

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
<sub>2026-03-22 · 8mo ago</sub>

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
| 2026-11-26 | [Build Linux aarch64 (Graviton) wheels (#1156)](https://github.com/plasma-umass/scalene/commit/df36d924c9284b9589cc21dd2bb0134d9d110f9d) | emeryberger |
| 2026-11-26 | [Don't take asyncio's policy lock in the CPU signal handler (#1157)](https://github.com/plasma-umass/scalene/commit/1a67af4927a884256046d748feca5dbf9cb24f57) | emeryberger |
| 2026-11-25 | [Deflake test_reload_on_another_thread_is_not_another_sample (#1155)](https://github.com/plasma-umass/scalene/commit/a2f400ab2c49106d691caca813e7d2f24597a1fc) | emeryberger |
| 2026-11-24 | [Propagate --allocation-sampling-window to child processes (fixes #115…](https://github.com/plasma-umass/scalene/commit/f42a69b921a100f924d37156f3b48879c431adee) | emeryberger |
| 2026-11-22 | [Claim the pending CPU-signal arrival atomically (fixes #1151) (#1152)](https://github.com/plasma-umass/scalene/commit/557ecb3d4e8437cdf37a60547490947bcf3b9507) | emeryberger |
| 2026-11-21 | [NVIDIA: report the current per-process GPU load, not the lifetime ave…](https://github.com/plasma-umass/scalene/commit/4c9a5b8cd4350740bbf4f71600034fbbc3ed2a27) | KuzAlexey |
| 2026-11-16 | [Don't hang programs waiting for their own timer signal under Scalene …](https://github.com/plasma-umass/scalene/commit/167a3edbf4a5e39e0fdc876d4a9f65143b64eb42) | emeryberger |
| 2026-11-16 | [Never fault reading a half-pushed frame in the CPU signal handler (#1…](https://github.com/plasma-umass/scalene/commit/e5e2230850ec2838a564a3b31f08e84567b2ad39) | emeryberger |
| 2026-11-15 | [Signal smoketest: sleep instead of pause() (lost-wakeup race); enforc…](https://github.com/plasma-umass/scalene/commit/538a5187b5ef49f43b40a518d24c19fa8a1280b1) | emeryberger |
| 2026-11-15 | [Document how saved settings and --api-keys-from-env combine; list con…](https://github.com/plasma-umass/scalene/commit/9bd56dced36096c99d5529933d84d0582de43b60) | emeryberger |

[See all commits ↗](https://github.com/plasma-umass/scalene/commits)

## ⬇️ Get it

```bash
git clone https://github.com/plasma-umass/scalene.git
```
