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
| 🕒 **Last activity** | 2026-11-18 (3d ago) |
| 📅 **Created** | 2017-01-20 |
| 📦 **Latest release** | [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 251.5 MB |
| 🌐 **Website** | https://pipenv.pypa.io |

## 📦 Recent releases

### [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — Release v2026.11.0
<sub>2026-11-09 · 12d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added a new `uv` resolver backend as an alternative to the default pip-based resolver, providing faster dependency resolution
> **Changed**
> - Vendored pip 26.3 with rebased Pipenv patches
> **Fixed**
> …

### [v2026.10.6](https://github.com/pypa/pipenv/releases/tag/v2026.10.6) — Release v2026.10.6
<sub>2026-11-05 · 15d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Exit with a non-zero status code when `safety` cannot be installed or run during `check`/`scan`, ensuring failures are properly signaled to calling processes
> - Read `Pipfile` as UTF-8 in `check`, `scan`, and `--support` commands, preventing errors with non-ASCII characters in Pipfile content
> - Render dependency graph using only characters supported by the terminal's stdout encoding, avoiding display errors in non-UTF-8 environments
> **Removed**
> …

### [v2026.10.5](https://github.com/pypa/pipenv/releases/tag/v2026.10.5) — Release v2026.10.5
<sub>2026-11-01 · 19d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Fixed `--trusted-host` arguments being flagged as secrets in CodeQL security scanning
> - Fixed package name parsing in `pipenv update` to correctly handle requirement specifiers as arguments
> - Fixed `requirements` command to emit `--trusted-host` for sources with `verify_ssl = false`
> - Fixed `requirements` command to correctly join `os_markers` and `markers` with `and`
> …

### [v2026.10.4](https://github.com/pypa/pipenv/releases/tag/v2026.10.4) — Release v2026.10.4
<sub>2026-10-28 · 23d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added interactive `pipenv init` command for creating a Pipfile with guided prompts
> **Fixed**
> - Fixed `pipenv install -r` to decode requirements files using the same encoding detection as pip
> - Fixed `pipenv audit` to exit with a non-zero status code when `pip-audit` cannot be run
> …

### [v2026.10.3](https://github.com/pypa/pipenv/releases/tag/v2026.10.3) — Release v2026.10.3
<sub>2026-10-25 · 27d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Forward extra keyword arguments in the Windows `rmtree` test shim to ensure compatibility with Python 3.14.9
> **Security**
> - Bump `pip` dependency to latest version (includes 3 updates)
> - Bump `certifi` in the `/examples` directory to address potential security vulnerabilities
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Merge pull request #6786 from Alpenj/fix-remote-requirements-temp-file](https://github.com/pypa/pipenv/commit/00ae9dc59e00f1132d74d79d8985ae47c70dd881) | matteius |
| 2026-11-18 | [Merge pull request #6788 from pcbeingused333/fix/pipfile-path-sys-pla…](https://github.com/pypa/pipenv/commit/0a8646a201cfe5f93e91c6c2ca261cee7db16119) | matteius |
| 2026-11-18 | [Merge pull request #6789 from pcbeingused333/fix/editable-uninstall-name](https://github.com/pypa/pipenv/commit/896778ff74bcae989706c03bb3429c104d7534da) | matteius |
| 2026-11-18 | [Merge pull request #6791 from anishpentyala/fix/file-url-single-decode](https://github.com/pypa/pipenv/commit/31a6aba1ecaada89e2fc13ea5c87cc05d57abac0) | matteius |
| 2026-11-18 | [Merge pull request #6792 from pypa/fix/vendoring-ci-py315](https://github.com/pypa/pipenv/commit/b8959751011ef42feb2533f5b41d5dcd9c7d94d4) | matteius |
| 2026-11-18 | [Fix vendoring license download on Python 3.15 runners](https://github.com/pypa/pipenv/commit/ae8de4b0bc374286f9537c8d7da7a5de5352ab62) | matteius |
| 2026-11-18 | [Use double backticks in news fragment](https://github.com/pypa/pipenv/commit/f9cf30c792f57c4d1228842a84b7bc51f2afb7cb) | matteius |
| 2026-11-18 | [Merge branch 'main' into fix/editable-uninstall-name](https://github.com/pypa/pipenv/commit/32d6462a97d1f8f09a459a54089caece74d8dcf4) | matteius |
| 2026-11-17 | [fix release command](https://github.com/pypa/pipenv/commit/0de1939d69214c254c1abaa827088657ab8f9fa8) | matteius |
| 2026-11-17 | [Document local file URL decoding fix for issue 6790](https://github.com/pypa/pipenv/commit/0c9a411da3fdc93f5af6edd94aa6656f88be6ad7) | anishpentyala |

[See all commits ↗](https://github.com/pypa/pipenv/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pypa/pipenv.git
```
