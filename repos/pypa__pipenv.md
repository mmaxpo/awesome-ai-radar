# pypa/pipenv

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/pypa/pipenv)

>  Python Development Workflow for Humans.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🐍 Python & backend tooling |
| **Project** | — |
| **Why it's worth a look** | Python dependency and virtualenv manager |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 25.0k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [5](https://github.com/pypa/pipenv/issues) |
| 💻 **Languages** | Python 82% · HTML 18% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `pip` `python` `packaging` `virtualenv` `pipfile` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2017-01-20 |
| 📦 **Latest release** | [v2026.12.0](https://github.com/pypa/pipenv/releases/tag/v2026.12.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 235.9 MB |
| 🌐 **Website** | https://pipenv.pypa.io |

## 📦 Recent releases

### [v2026.12.0](https://github.com/pypa/pipenv/releases/tag/v2026.12.0) — Release v2026.12.0
<sub>2026-11-25 · today</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Dropped `cache-dir` value from constraint files to prevent invalid constraint file generation
> - Kept extras on file and path dependencies in requirements output
> - Kept `sys_platform` markers on path/file entries when using `--from-pipfile`
> - Preserved literal percent escapes in local file URL conversion; fixed double-decoding of file URLs
> …

### [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — Release v2026.11.0
<sub>2026-11-09 · 16d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added a new `uv` resolver backend as an alternative to the default pip-based resolver, providing faster dependency resolution
> **Changed**
> - Vendored pip 26.3 with rebased Pipenv patches
> **Fixed**
> …

### [v2026.10.6](https://github.com/pypa/pipenv/releases/tag/v2026.10.6) — Release v2026.10.6
<sub>2026-11-05 · 20d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Exit with a non-zero status code when `safety` cannot be installed or run during `check`/`scan`, ensuring failures are properly signaled to calling processes
> - Read `Pipfile` as UTF-8 in `check`, `scan`, and `--support` commands, preventing errors with non-ASCII characters in Pipfile content
> - Render dependency graph using only characters supported by the terminal's stdout encoding, avoiding display errors in non-UTF-8 environments
> **Removed**
> …

### [v2026.10.5](https://github.com/pypa/pipenv/releases/tag/v2026.10.5) — Release v2026.10.5
<sub>2026-11-01 · 23d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Fixed `--trusted-host` arguments being flagged as secrets in CodeQL security scanning
> - Fixed package name parsing in `pipenv update` to correctly handle requirement specifiers as arguments
> - Fixed `requirements` command to emit `--trusted-host` for sources with `verify_ssl = false`
> - Fixed `requirements` command to correctly join `os_markers` and `markers` with `and`
> …

### [v2026.10.4](https://github.com/pypa/pipenv/releases/tag/v2026.10.4) — Release v2026.10.4
<sub>2026-10-28 · 27d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added interactive `pipenv init` command for creating a Pipfile with guided prompts
> **Fixed**
> - Fixed `pipenv install -r` to decode requirements files using the same encoding detection as pip
> - Fixed `pipenv audit` to exit with a non-zero status code when `pip-audit` cannot be run
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Merge pull request #6808 from pcbeingused333/fix/pylock-normalized-names](https://github.com/pypa/pipenv/commit/43ccc4d5fcb899e0ed349f716348f49aaec9e6c7) | matteius |
| 2026-11-25 | [fix: normalize package names written to pylock.toml](https://github.com/pypa/pipenv/commit/88518d841400e996edf4e70ba3a98ec1a3e6c113) | pcbeingused333 |
| 2026-11-25 | [Merge pull request #6806 from pcbeingused333/fix/clean-print-stderr](https://github.com/pypa/pipenv/commit/1c5499f58a3d61ab44a9ae47a39e6a69bfed5d82) | matteius |
| 2026-11-25 | [fix(clean): show pip stderr when an uninstall fails](https://github.com/pypa/pipenv/commit/7768b4498af0dcba7112050875546833a9766f19) | pcbeingused333 |
| 2026-11-25 | [Release v2026.12.0](https://github.com/pypa/pipenv/commit/ccd5b291f818c12e792ca8771626938605e2eb22) | matteius |
| 2026-11-25 | [Bumped version to 2026.12.0.](https://github.com/pypa/pipenv/commit/0e1edbf7a77d638ab507ee7a74b173c53640e513) | matteius |
| 2026-11-25 | [Merge pull request #6796 from anubhavlal07/fix/constraint-cache-dir-v…](https://github.com/pypa/pipenv/commit/a02edf02568e187146f12b292a005f3bb7415a55) | matteius |
| 2026-11-25 | [Merge pull request #6805 from pypa/fix/windows-release-tag-stdin](https://github.com/pypa/pipenv/commit/26cd07bb46a2c8002fd2c1288ffc661491cc614b) | matteius |
| 2026-11-25 | [Pass release tag message via stdin to fix Windows CI](https://github.com/pypa/pipenv/commit/acea0f5566e66d4717c3f381140b05d9292ce929) | matteius |
| 2026-11-25 | [Merge pull request #6802 from Lushiyao5/fix/env-int-fallback-20261122](https://github.com/pypa/pipenv/commit/525db0ce6daeca37b702413967f7a430b407cd53) | matteius |

[See all commits ↗](https://github.com/pypa/pipenv/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pypa/pipenv.git
```
