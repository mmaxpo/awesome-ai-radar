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
| 🐞 **Open issues + PRs** | [868](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 248.1 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.4.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev3) — 3.9.4.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-16 · today</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Stop served flow runs on Windows without a console-wide CTRL_BREAK by @EnesSoydan in https://github.com/PrefectHQ/prefect/pull/23895
> * Accept any task runner in `@flow` and `Flow` `task_runner` type hints by @dayan02dev in https://github.com/PrefectHQ/prefect/pull/23893
> **Development & Tidiness 🧹**
> * Fix flaky `test_read_task_workers` by resetting the in-memory task worker tracker by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23903
> …

### [3.9.4.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev2) — 3.9.4.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Clarify ECS work pool network configuration by @prabhushreyas in https://github.com/PrefectHQ/prefect/pull/23911
> * fix(ui-v2): make the subflow run count respect the state filter by @Shanmukh-l33t in https://github.com/PrefectHQ/prefect/pull/23912
> **Documentation 📓**
> * docs: Add release notes for `prefect-redis==0.3.1` by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23915
> …

### [3.9.4.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev1) — 3.9.4.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-14 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Fix CodSpeed import benchmark timeout and fail the job on benchmark failures by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23897
> **Development & Tidiness 🧹**
> * Fix flaky test_concurrency_context_releases_slots_async by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23891
> **Documentation 📓**
> …

### [3.9.3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3) — 3.9.3 - `aclose()`ing time
<sub>2026-11-13 · 2d ago</sub>

> **Enhancements ➕➕**
> * Add search and ordering to the automations page by [@uinstinct](https://github.com/uinstinct) in [#23048](https://github.com/PrefectHQ/prefect/pull/23048)
> * Align flow runs timeline ticks to local time boundaries by [@theluckystrike](https://github.com/theluckystrike) in [#23272](https://github.com/PrefectHQ/prefect/pull/23272)
> **Bug Fixes 🐞**
> * Fix early closure of async generator flows by [@desertaxle](https://github.com/desertaxle) in [#23886](https://github.com/PrefectHQ/prefect/pull/23886)
> * Fix retry restart of async generator tasks closed during finalizer failure by [@dfbustosus](https://github.com/dfbustosus) in [#23739](https://github.com/PrefectHQ/prefect/pull/23739)
> …

### [3.9.3.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3.dev2) — 3.9.3.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-13 · 3d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Run duration-balanced Postgres groups on every Python version by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23863
> * Run duration-balanced SQLite test groups by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23865
> **Bug Fixes 🐞**
> * Fix SQLAlchemy cursor reuse for parameterized fetches by @shion233 in https://github.com/PrefectHQ/prefect/pull/23847
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [docs: note parent transactions roll back when a child fails to commit…](https://github.com/PrefectHQ/prefect/commit/8decde08a77cebcf5932a87a48efa9bc8ce39d54) | devin-ai-integration[bot] |
| 2026-11-15 | [Bump opentelemetry-api from 1.45.1 to 1.45.2 (#23883)](https://github.com/PrefectHQ/prefect/commit/bf195ab012384574141cce118f15ca4be92841e2) | dependabot[bot] |
| 2026-11-15 | [Accept any task runner in `@flow` and `Flow` `task_runner` type hints…](https://github.com/PrefectHQ/prefect/commit/e93ee85672ac7bf5bbcd4ad335de3bee11977545) | dayan02dev |
| 2026-11-15 | [Stop served flow runs on Windows without a console-wide CTRL_BREAK (#…](https://github.com/PrefectHQ/prefect/commit/3682cf2120c7aafda3804d1aeae2ecad27de55d3) | EnesSoydan |
| 2026-11-15 | [Fix flaky `test_read_task_workers` by resetting the in-memory task wo…](https://github.com/PrefectHQ/prefect/commit/e63f41e13d2b40f83f10c619a4bc89457abbf7b6) | devin-ai-integration[bot] |
| 2026-11-15 | [Quote attachment filenames in email_send_message (#23905)](https://github.com/PrefectHQ/prefect/commit/5460c3a8b23b1a70e810bf521a5433c71070a488) | anishmehta24 |
| 2026-11-15 | [Sync UI V2 OpenAPI types with the locked schema (#23907)](https://github.com/PrefectHQ/prefect/commit/7633e3ec7acf12d820c995404f65b2d3f3f8189c) | zzstoatzz |
| 2026-11-15 | [docs: fix ECS work pool network_configuration example key structure (…](https://github.com/PrefectHQ/prefect/commit/ad0ed765da3483bd7cda86fc82fd89b2f5271c18) | devin-ai-integration[bot] |
| 2026-11-15 | [Document custom work pool defaults with the CLI (#23914)](https://github.com/PrefectHQ/prefect/commit/c784446f70768d62ff23f7026b6e16541e5aacf3) | prabhushreyas |
| 2026-11-15 | [fix(ui-v2): make the subflow run count respect the state filter (#23912)](https://github.com/PrefectHQ/prefect/commit/7abf97a1d7a077cd7ce50b72a31b706511ecd03f) | Shanmukh-l33t |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
