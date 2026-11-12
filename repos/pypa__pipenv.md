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
| 🐞 **Open issues + PRs** | [4](https://github.com/pypa/pipenv/issues) |
| 💻 **Languages** | Python 82% · HTML 18% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `pip` `python` `packaging` `virtualenv` `pipfile` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2017-01-20 |
| 📦 **Latest release** | [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — 2026-11-09 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 251.4 MB |
| 🌐 **Website** | https://pipenv.pypa.io |

## 📦 Recent releases

### [v2026.11.0](https://github.com/pypa/pipenv/releases/tag/v2026.11.0) — Release v2026.11.0
<sub>2026-11-09 · 3d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added a new `uv` resolver backend as an alternative to the default pip-based resolver, providing faster dependency resolution
> **Changed**
> - Vendored pip 26.3 with rebased Pipenv patches
> **Fixed**
> …

### [v2026.10.6](https://github.com/pypa/pipenv/releases/tag/v2026.10.6) — Release v2026.10.6
<sub>2026-11-05 · 6d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Exit with a non-zero status code when `safety` cannot be installed or run during `check`/`scan`, ensuring failures are properly signaled to calling processes
> - Read `Pipfile` as UTF-8 in `check`, `scan`, and `--support` commands, preventing errors with non-ASCII characters in Pipfile content
> - Render dependency graph using only characters supported by the terminal's stdout encoding, avoiding display errors in non-UTF-8 environments
> **Removed**
> …

### [v2026.10.5](https://github.com/pypa/pipenv/releases/tag/v2026.10.5) — Release v2026.10.5
<sub>2026-11-01 · 10d ago</sub>

> **🤖 AI-Generated Changelog**
> **Fixed**
> - Fixed `--trusted-host` arguments being flagged as secrets in CodeQL security scanning
> - Fixed package name parsing in `pipenv update` to correctly handle requirement specifiers as arguments
> - Fixed `requirements` command to emit `--trusted-host` for sources with `verify_ssl = false`
> - Fixed `requirements` command to correctly join `os_markers` and `markers` with `and`
> …

### [v2026.10.4](https://github.com/pypa/pipenv/releases/tag/v2026.10.4) — Release v2026.10.4
<sub>2026-10-28 · 14d ago</sub>

> **🤖 AI-Generated Changelog**
> **Added**
> - Added interactive `pipenv init` command for creating a Pipfile with guided prompts
> **Fixed**
> - Fixed `pipenv install -r` to decode requirements files using the same encoding detection as pip
> - Fixed `pipenv audit` to exit with a non-zero status code when `pip-audit` cannot be run
> …

### [v2026.10.3](https://github.com/pypa/pipenv/releases/tag/v2026.10.3) — Release v2026.10.3
<sub>2026-10-25 · 18d ago</sub>

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
| 2026-11-11 | [Merge pull request #6785 from Hisernberg/fix/vendoring-license-path-f…](https://github.com/pypa/pipenv/commit/a7783051ede5ba7fc4d4ab50d4ceb63947937b2c) | matteius |
| 2026-11-11 | [Fix missing f-string in the flattened-subdep license path](https://github.com/pypa/pipenv/commit/d9a0db06d38778f98c602af7364197afa1fcb756) | Hisernberg |
| 2026-11-09 | [Release v2026.11.0](https://github.com/pypa/pipenv/commit/3c34948686a487b2728fe1d007822a37cd656d8b) | matteius |
| 2026-11-09 | [Bumped version to 2026.11.0.](https://github.com/pypa/pipenv/commit/8686678ebf2a107aeda3e8a592630492032a9f95) | matteius |
| 2026-11-09 | [Merge pull request #6773 from matteius/feat/uv-resolver-backend-6109](https://github.com/pypa/pipenv/commit/ec9b914b3bd93a2141af5bfc2bfbb9ed6565b428) | matteius |
| 2026-11-09 | [Merge pull request #6783 from pcbeingused333/fix/scan-quiet-stderr](https://github.com/pypa/pipenv/commit/afe9aaf5487e526a0bc8033993fbff9f908f821e) | matteius |
| 2026-11-09 | [fix(scan): suppress Safety warnings on quiet success](https://github.com/pypa/pipenv/commit/8564457f173a5cd5efd09893b2ad9de8531f39cc) | pcbeingused333 |
| 2026-11-09 | [fix(scan): preserve Safety stderr in quiet mode](https://github.com/pypa/pipenv/commit/831d0a5ae7bf337ea1fe70bc00ea44dee98fc433) | pcbeingused333 |
| 2026-11-07 | [Merge pull request #6782 from pcbeingused333/fix-c1828](https://github.com/pypa/pipenv/commit/ce84086dcf7695202e269a89875d9681ca233136) | matteius |
| 2026-11-07 | [fix(requirements): keep markers on VCS entries with --no-lock](https://github.com/pypa/pipenv/commit/12c2d5f4099407421d60fa353106c2742d0a76c3) | pcbeingused333 |

[See all commits ↗](https://github.com/pypa/pipenv/commits)

## ⬇️ Get it

```bash
git clone https://github.com/pypa/pipenv.git
```
