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
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2017-01-20 |
| 📦 **Latest release** | [v2026.12.1](https://github.com/pypa/pipenv/releases/tag/v2026.12.1) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 236.0 MB |
| 🌐 **Website** | https://pipenv.pypa.io |

## 📦 Recent releases

### [v2026.12.1](https://github.com/pypa/pipenv/releases/tag/v2026.12.1) — Release v2026.12.1
<sub>2026-11-25 · yesterday</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Preserve shorthand markers (e.g., `; sys_platform == 'win32'`) in requirements when using `--no-lock`
> - Normalize package names written to `pylock.toml` to ensure consistent formatting
> - Display pip's stderr output when a package uninstall fails during `pipenv clean`, improving error visibility
> ---
> …

### [v2026.12.0](https://github.com/pypa/pipenv/releases/tag/v2026.12.0) — Release v2026.12.0
<sub>2026-11-25 · 2d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Dropped `cache-dir` value from constraint files to prevent invalid constraint file generation
> - Kept extras on file and path dependencies in requirements output
> - Kept `sys_platform` markers on path/file entries when using `--from-pipfile`
> - Preserved literal percent escapes in local file URL conversion; fixed double-decoding of file URLs
> …

### [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — Release v2026.11.0
<sub>2026-11-09 · 18d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added a new `uv` resolver backend as an alternative to the default pip-based resolver, providing faster dependency resolution
> **Changed**
> - Vendored pip 26.3 with rebased Pipenv patches
> **Fixed**
> …

### [v2026.10.6](https://github.com/pypa/pipenv/releases/tag/v2026.10.6) — Release v2026.10.6
<sub>2026-11-05 · 22d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Exit with a non-zero status code when `safety` cannot be installed or run during `check`/`scan`, ensuring failures are properly signaled to calling processes
> - Read `Pipfile` as UTF-8 in `check`, `scan`, and `--support` commands, preventing errors with non-ASCII characters in Pipfile content
> - Render dependency graph using only characters supported by the terminal's stdout encoding, avoiding display errors in non-UTF-8 environments
> **Removed**
> …

### [v2026.10.5](https://github.com/pypa/pipenv/releases/tag/v2026.10.5) — Release v2026.10.5
<sub>2026-11-01 · 25d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Fixed `--trusted-host` arguments being flagged as secrets in CodeQL security scanning
> - Fixed package name parsing in `pipenv update` to correctly handle requirement specifiers as arguments
> - Fixed `requirements` command to emit `--trusted-host` for sources with `verify_ssl = false`
> - Fixed `requirements` command to correctly join `os_markers` and `markers` with `and`
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Merge pull request #6811 from draarivpatel-ui/fix-translate-markers-e…](https://github.com/pypa/pipenv/commit/4a5a2ce184475b8b77a04bd7c1bde23c40237774) | matteius |
| 2026-11-25 | [Fix extra marker translation](https://github.com/pypa/pipenv/commit/2080214af40413e6f1d238eb51d5c1523af6606c) | draarivpatel-ui |
| 2026-11-25 | [Release v2026.12.1](https://github.com/pypa/pipenv/commit/f2ac3c11e570a4f1b5cb1935603bfa7182c0f938) | matteius |
| 2026-11-25 | [Bumped version to 2026.12.1.](https://github.com/pypa/pipenv/commit/d665d8aa60ca6c4e7a438ce87d673fd647352567) | matteius |
| 2026-11-25 | [Merge pull request #6809 from pcbeingused333/fix/no-lock-shorthand-ma…](https://github.com/pypa/pipenv/commit/d5ce6577864a9b61694ea46a761e05b712db8c4a) | matteius |
| 2026-11-25 | [Merge pull request #6808 from pcbeingused333/fix/pylock-normalized-names](https://github.com/pypa/pipenv/commit/43ccc4d5fcb899e0ed349f716348f49aaec9e6c7) | matteius |
| 2026-11-25 | [fix(requirements): keep shorthand markers with --no-lock](https://github.com/pypa/pipenv/commit/5d572ea300492abc2cbdcf43c2c6ce0869e991ba) | pcbeingused333 |
| 2026-11-25 | [fix: normalize package names written to pylock.toml](https://github.com/pypa/pipenv/commit/88518d841400e996edf4e70ba3a98ec1a3e6c113) | pcbeingused333 |
| 2026-11-25 | [Merge pull request #6806 from pcbeingused333/fix/clean-print-stderr](https://github.com/pypa/pipenv/commit/1c5499f58a3d61ab44a9ae47a39e6a69bfed5d82) | matteius |
| 2026-11-25 | [fix(clean): show pip stderr when an uninstall fails](https://github.com/pypa/pipenv/commit/7768b4498af0dcba7112050875546833a9766f19) | pcbeingused333 |

[See all commits ↗](https://github.com/pypa/pipenv/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pypa/pipenv.git
```
