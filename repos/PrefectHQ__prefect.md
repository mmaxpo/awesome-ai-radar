# PrefectHQ/prefect

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/PrefectHQ/prefect)

> Prefect is a workflow orchestration framework for building resilient data pipelines in Python.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why it's worth a look** | Python workflow orchestration with scheduling and retries |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 24.2k |
| 🍴 **Forks** | 2.7k |
| 🐞 **Open issues + PRs** | [870](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 249.7 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.5.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev2) — 3.9.5.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-21 · today</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Run db vacuum tasks one at a time on the maintenance pool by @ShikhJohari in https://github.com/PrefectHQ/prefect/pull/23742
> **Development & Tidiness 🧹**
> * Fix `ReactiveTriggers` stop race during startup by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24021
> * Fix flaky `test_keeps_polling_while_setup_hangs` observer test by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23950
> …

### [3.9.5.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev1) — 3.9.5.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-20 · yesterday</sub>

> **What's Changed**
> **Uncategorized**
> * Add RRule schedule builder component to ui-v2 by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24009
> * Use route names as OpenAPI operation IDs by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24010
> * Reduce state cross-products in orchestration rule tests by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24007
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.4...3.9.5.dev1

### [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 3.9.4 - It’s not you, it’s `CTRL_BREAK`
<sub>2026-11-19 · yesterday</sub>

> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by [@znicholasbrown](https://github.com/znicholasbrown) in [#23980](https://github.com/PrefectHQ/prefect/pull/23980)
> * Start the flow run suspension observer before the engine loads the flow by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#23947](https://github.com/PrefectHQ/prefect/pull/23947)
> **Bug Fixes 🐞**
> * Write Dockerfiles and build context files as UTF-8 by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23923](https://github.com/PrefectHQ/prefect/pull/23923)
> * Allow nested `tmpchdir` contexts on the same thread by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23871](https://github.com/PrefectHQ/prefect/pull/23871)
> …

### [3.9.4.dev6](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev6) — 3.9.4.dev6: Nightly Development Release _(pre-release)_
<sub>2026-11-19 · 2d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by @znicholasbrown in https://github.com/PrefectHQ/prefect/pull/23980
> **Bug Fixes 🐞**
> * Strip credentials from repository URL in `GitRepository` clone debug log by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23969
> * fix(prefect-redis): keep unprocessed entries when trimming streams by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23965
> …

### [3.9.4.dev5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev5) — 3.9.4.dev5: Nightly Development Release _(pre-release)_
<sub>2026-11-18 · 3d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document `RemoteFileSystem` settings with an example by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23959
> **Uncategorized**
> * Start the flow run suspension observer before the engine loads the flow by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23947
> * Start the suspension observer early for MicroVM deployments that pull code by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23957
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Support non-root users in the official Docker image (#24027)](https://github.com/PrefectHQ/prefect/commit/5513abc4df1f20a02bb810849477b64c989c3160) | devin-ai-integration[bot] |
| 2026-11-20 | [Fix flaky subscriber setup cancellation tests (#23881)](https://github.com/PrefectHQ/prefect/commit/1693b8386b6de14a58f9fac524d65a38541261cf) | devin-ai-integration[bot] |
| 2026-11-20 | [Add `registry_credentials` to the Kubernetes worker (#23852)](https://github.com/PrefectHQ/prefect/commit/d44d9f745c1942c33c51f5dd4af3820956573b8b) | polwayne |
| 2026-11-20 | [Run db vacuum tasks one at a time on the maintenance pool (#23742)](https://github.com/PrefectHQ/prefect/commit/b76e190895121aa8a204d3c493f342e1253a97bc) | ShikhJohari |
| 2026-11-20 | [docs: clarify tmpchdir process-wide scope (#23998)](https://github.com/PrefectHQ/prefect/commit/7e19e94405e269d4c1e044b7ac4e7c6f7c1cab1b) | devin-ai-integration[bot] |
| 2026-11-20 | [Stop pointing users at removed `prefect agent start` for `prefect-age…](https://github.com/PrefectHQ/prefect/commit/a328ffc14df285f84ac6887cff74128588d7734a) | devin-ai-integration[bot] |
| 2026-11-20 | [Fix flaky `test_keeps_polling_while_setup_hangs` observer test (#23950)](https://github.com/PrefectHQ/prefect/commit/f7f20d77131ab6131c245747d178ad234e622139) | devin-ai-integration[bot] |
| 2026-11-20 | [Fix `ReactiveTriggers` stop race during startup (#24021)](https://github.com/PrefectHQ/prefect/commit/4207eda2abcc55930aaa745085de360cbe8339bc) | devin-ai-integration[bot] |
| 2026-11-20 | [Store text files with LF line endings (#24023)](https://github.com/PrefectHQ/prefect/commit/d0e4bb721f90fe0c107a5b3b67a146fc41be8342) | gaker |
| 2026-11-20 | [Refresh the Python and UI dependency lockfiles (#24020)](https://github.com/PrefectHQ/prefect/commit/b57286cec5377e6a1ee0f0e71359bd083aedf897) | gaker |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
