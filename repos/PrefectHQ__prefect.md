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
| 🐞 **Open issues + PRs** | [888](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 249.7 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.5.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev3) — 3.9.5.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-22 · yesterday</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Aggregate nested collections of states when determining the final state by @Nacl-HCl in https://github.com/PrefectHQ/prefect/pull/23474
> **Uncategorized**
> * Reject `--param` and `--job-variable` values without `=` in `prefect deployment run` by @harshit3355 in https://github.com/PrefectHQ/prefect/pull/24035
> **New Contributors**
> …

### [3.9.5.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev2) — 3.9.5.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-21 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Run db vacuum tasks one at a time on the maintenance pool by @ShikhJohari in https://github.com/PrefectHQ/prefect/pull/23742
> **Development & Tidiness 🧹**
> * Fix `ReactiveTriggers` stop race during startup by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24021
> * Fix flaky `test_keeps_polling_while_setup_hangs` observer test by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23950
> …

### [3.9.5.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev1) — 3.9.5.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

> **What's Changed**
> **Uncategorized**
> * Add RRule schedule builder component to ui-v2 by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24009
> * Use route names as OpenAPI operation IDs by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24010
> * Reduce state cross-products in orchestration rule tests by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24007
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.4...3.9.5.dev1

### [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 3.9.4 - It’s not you, it’s `CTRL_BREAK`
<sub>2026-11-19 · 3d ago</sub>

> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by [@znicholasbrown](https://github.com/znicholasbrown) in [#23980](https://github.com/PrefectHQ/prefect/pull/23980)
> * Start the flow run suspension observer before the engine loads the flow by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#23947](https://github.com/PrefectHQ/prefect/pull/23947)
> **Bug Fixes 🐞**
> * Write Dockerfiles and build context files as UTF-8 by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23923](https://github.com/PrefectHQ/prefect/pull/23923)
> * Allow nested `tmpchdir` contexts on the same thread by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23871](https://github.com/PrefectHQ/prefect/pull/23871)
> …

### [3.9.4.dev6](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev6) — 3.9.4.dev6: Nightly Development Release _(pre-release)_
<sub>2026-11-19 · 4d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by @znicholasbrown in https://github.com/PrefectHQ/prefect/pull/23980
> **Bug Fixes 🐞**
> * Strip credentials from repository URL in `GitRepository` clone debug log by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23969
> * fix(prefect-redis): keep unprocessed entries when trimming streams by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23965
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Update prefect-kubernetes integration pin (#24070)](https://github.com/PrefectHQ/prefect/commit/f89e93e21714fea40ca44057af99d4014808293e) | prefect-ci-bot-public[bot] |
| 2026-11-23 | [Sweep stale integration pins in uv.lock (#24058)](https://github.com/PrefectHQ/prefect/commit/5dbcb7b418eac4edc4df2f067a074f49b1386303) | prefect-ci-bot-public[bot] |
| 2026-11-23 | [Stop Escape from opening the flow run graph in fullscreen (#24046)](https://github.com/PrefectHQ/prefect/commit/ba4c3897e6e9f0f200402b6557c659732050c374) | burrows99 |
| 2026-11-23 | [docs: Add release notes for `prefect-kubernetes==0.8.2` (#24068)](https://github.com/PrefectHQ/prefect/commit/d4abc8d71586831207093a73eddc73671d1513c0) | devin-ai-integration[bot] |
| 2026-11-23 | [Only initialize Amplitude in UI v2 when server analytics are enabled …](https://github.com/PrefectHQ/prefect/commit/4cabb0d2924b4710ca6e7b679c94ae133882c1e3) | devin-ai-integration[bot] |
| 2026-11-22 | [Aggregate nested collections of states when determining the final sta…](https://github.com/PrefectHQ/prefect/commit/b055980caf24955eebcb51fe6c9088522f48208a) | Nacl-HCl |
| 2026-11-21 | [docs: document safe redirect search params in routes AGENTS.md (#23983)](https://github.com/PrefectHQ/prefect/commit/dfc66c657dc1181ef701e4606a0fff5718c457d5) | devin-ai-integration[bot] |
| 2026-11-21 | [Reject `--param` and `--job-variable` values without `=` in `prefect …](https://github.com/PrefectHQ/prefect/commit/d29e3536b2aef90cac26d32d1e78e65cc289dff1) | harshit3355 |
| 2026-11-21 | [docs: document legacy prefect-agent pool handling in CLI AGENTS.md (#…](https://github.com/PrefectHQ/prefect/commit/7e6e8d84d1972f442171050a4aa9b77385db8d7a) | devin-ai-integration[bot] |
| 2026-11-20 | [Support non-root users in the official Docker image (#24027)](https://github.com/PrefectHQ/prefect/commit/5513abc4df1f20a02bb810849477b64c989c3160) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
