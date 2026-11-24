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
| 🐞 **Open issues + PRs** | [825](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 250.6 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.5.dev4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev4) — 3.9.5.dev4: Nightly Development Release _(pre-release)_
<sub>2026-11-24 · today</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document virtual network configuration for ACI flow containers by @himanshuchawla0807-gif in https://github.com/PrefectHQ/prefect/pull/23620
> * Read V2 state colors from body so color modes apply by @zzstoatzz in https://github.com/PrefectHQ/prefect/pull/23804
> **Bug Fixes 🐞**
> * Keep the client transition id on states substituted by rejecting rules by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23977
> …

### [3.9.5.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev3) — 3.9.5.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-22 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Aggregate nested collections of states when determining the final state by @Nacl-HCl in https://github.com/PrefectHQ/prefect/pull/23474
> **Uncategorized**
> * Reject `--param` and `--job-variable` values without `=` in `prefect deployment run` by @harshit3355 in https://github.com/PrefectHQ/prefect/pull/24035
> **New Contributors**
> …

### [3.9.5.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev2) — 3.9.5.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-21 · 3d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Run db vacuum tasks one at a time on the maintenance pool by @ShikhJohari in https://github.com/PrefectHQ/prefect/pull/23742
> **Development & Tidiness 🧹**
> * Fix `ReactiveTriggers` stop race during startup by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24021
> * Fix flaky `test_keeps_polling_while_setup_hangs` observer test by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23950
> …

### [3.9.5.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev1) — 3.9.5.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

> **What's Changed**
> **Uncategorized**
> * Add RRule schedule builder component to ui-v2 by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24009
> * Use route names as OpenAPI operation IDs by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24010
> * Reduce state cross-products in orchestration rule tests by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24007
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.4...3.9.5.dev1

### [3.9.4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4) — 3.9.4 - It’s not you, it’s `CTRL_BREAK`
<sub>2026-11-19 · 4d ago</sub>

> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by [@znicholasbrown](https://github.com/znicholasbrown) in [#23980](https://github.com/PrefectHQ/prefect/pull/23980)
> * Start the flow run suspension observer before the engine loads the flow by [@bunchesofdonald](https://github.com/bunchesofdonald) in [#23947](https://github.com/PrefectHQ/prefect/pull/23947)
> **Bug Fixes 🐞**
> * Write Dockerfiles and build context files as UTF-8 by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23923](https://github.com/PrefectHQ/prefect/pull/23923)
> * Allow nested `tmpchdir` contexts on the same thread by [@devin-ai-integration](https://github.com/devin-ai-integration) in [#23871](https://github.com/PrefectHQ/prefect/pull/23871)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Resolve API route dependencies on the event loop (#23279)](https://github.com/PrefectHQ/prefect/commit/cca7dea1f0aec1e692876d435ea03a2bc0e60683) | fatih-acar |
| 2026-11-24 | [Stop the async flow engine from blocking its event loop on the suspen…](https://github.com/PrefectHQ/prefect/commit/8222fd5abead575651beb17b044f2f8b82b00307) | fatih-acar |
| 2026-11-24 | [Add more TagBadgeGroup regression tests for a counter wider than the …](https://github.com/PrefectHQ/prefect/commit/97915452decd5b53b038cdf0e429109343370f9d) | devin-ai-integration[bot] |
| 2026-11-24 | [Show every tag inline when the last tag is narrower than the overflow…](https://github.com/PrefectHQ/prefect/commit/974398cd9ca0e80cdc999a9d192e42d59baa7c81) | burrows99 |
| 2026-11-23 | [Fix flaky artifacts empty-state and concurrency limits E2E tests (#23…](https://github.com/PrefectHQ/prefect/commit/fa6656b3db12c30df981bd7e127b7ef699fd373e) | devin-ai-integration[bot] |
| 2026-11-23 | [Read V2 state colors from body so color modes apply (#23804)](https://github.com/PrefectHQ/prefect/commit/43c6326033b02215974f033145b2136b9108f99d) | zzstoatzz |
| 2026-11-23 | [Show which worker wrote a self-hosted flow run log (#24022)](https://github.com/PrefectHQ/prefect/commit/ab123ef1bfc056afa9dbb3c18f6ccc67ccdb44ac) | devin-ai-integration[bot] |
| 2026-11-23 | [Reject negative tag-based concurrency limits (#24041)](https://github.com/PrefectHQ/prefect/commit/ff5fe2609077911a3783840ae90ef536fe9fa0b9) | DanShinde |
| 2026-11-23 | [docs: note that RRule schedules reject INTERVAL=0 on create/update (#…](https://github.com/PrefectHQ/prefect/commit/83ecbbfa6ed809e1b4bc0ebe6d0d5aa946147079) | devin-ai-integration[bot] |
| 2026-11-23 | [Trim redundant test matrices and fix v1 concurrency mock test (#24074)](https://github.com/PrefectHQ/prefect/commit/66f90d41f581f1303b776307c4cb78d54409af35) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
