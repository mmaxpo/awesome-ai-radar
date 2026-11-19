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
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.4.dev6](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev6) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 248.7 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.4.dev6](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev6) — 3.9.4.dev6: Nightly Development Release _(pre-release)_
<sub>2026-11-19 · today</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Accept only same-origin paths in the UI v2 login redirect by @znicholasbrown in https://github.com/PrefectHQ/prefect/pull/23980
> **Bug Fixes 🐞**
> * Strip credentials from repository URL in `GitRepository` clone debug log by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23969
> * fix(prefect-redis): keep unprocessed entries when trimming streams by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23965
> …

### [3.9.4.dev5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev5) — 3.9.4.dev5: Nightly Development Release _(pre-release)_
<sub>2026-11-18 · yesterday</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document `RemoteFileSystem` settings with an example by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23959
> **Uncategorized**
> * Start the flow run suspension observer before the engine loads the flow by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23947
> * Start the suspension observer early for MicroVM deployments that pull code by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23957
> …

### [3.9.4.dev4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev4) — 3.9.4.dev4: Nightly Development Release _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Write auto-generated deployment Dockerfiles as UTF-8 in `prefect-docker` by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23929
> **Documentation 📓**
> * Document AWS setup for Lambda MicroVM push work pools by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23845
> * docs: fix dead and chained redirects, CLI page titles and stale links by @madureira-gabriel in https://github.com/PrefectHQ/prefect/pull/23941
> …

### [3.9.4.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev3) — 3.9.4.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-16 · 3d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Stop served flow runs on Windows without a console-wide CTRL_BREAK by @EnesSoydan in https://github.com/PrefectHQ/prefect/pull/23895
> * Accept any task runner in `@flow` and `Flow` `task_runner` type hints by @dayan02dev in https://github.com/PrefectHQ/prefect/pull/23893
> **Development & Tidiness 🧹**
> * Fix flaky `test_read_task_workers` by resetting the in-memory task worker tracker by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23903
> …

### [3.9.4.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev2) — 3.9.4.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-15 · 4d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Clarify ECS work pool network configuration by @prabhushreyas in https://github.com/PrefectHQ/prefect/pull/23911
> * fix(ui-v2): make the subflow run count respect the state filter by @Shanmukh-l33t in https://github.com/PrefectHQ/prefect/pull/23912
> **Documentation 📓**
> * docs: Add release notes for `prefect-redis==0.3.1` by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23915
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Accept only same-origin paths in the UI v2 login redirect (#23980)](https://github.com/PrefectHQ/prefect/commit/ec4b188a19371cb79bc91afe897042bca3a3c95f) | znicholasbrown |
| 2026-11-18 | [fix(prefect-redis): keep unprocessed entries when trimming streams (#…](https://github.com/PrefectHQ/prefect/commit/67380b6d06065205ee507d23daa9bcd044ed641e) | devin-ai-integration[bot] |
| 2026-11-18 | [Keep workers alive when cancelling a run hits an API error (#23973)](https://github.com/PrefectHQ/prefect/commit/6885185d6ebace59e8aa3846bebc65afb2198239) | mansur-akhmadi |
| 2026-11-18 | [docs: document GitRepository credential redaction rule in runner AGEN…](https://github.com/PrefectHQ/prefect/commit/5c22b3faa20348ac9ca3895504517599e7ae6357) | devin-ai-integration[bot] |
| 2026-11-18 | [Remove unreachable branch and unused internal helpers (#23967)](https://github.com/PrefectHQ/prefect/commit/d0b2ae04d709e51034f57501538f29499f8f0e19) | devin-ai-integration[bot] |
| 2026-11-18 | [Strip credentials from repository URL in `GitRepository` clone debug …](https://github.com/PrefectHQ/prefect/commit/517300170ce87e8664d1b497c1414b771f175764) | devin-ai-integration[bot] |
| 2026-11-18 | [Run the TLA+ model check on Amazon Corretto 21 (#23970)](https://github.com/PrefectHQ/prefect/commit/73a37b22c25007e7b3ce63f4f678f2a378722d9b) | chrisguidry |
| 2026-11-18 | [Document `RemoteFileSystem` settings with an example (#23959)](https://github.com/PrefectHQ/prefect/commit/f6fef9f6fcb3768b9002dc48dc2ab9af824e72f0) | devin-ai-integration[bot] |
| 2026-11-17 | [Start the suspension observer early for MicroVM deployments that pull…](https://github.com/PrefectHQ/prefect/commit/5e8ca118fc514ffe9ab3355ea5cf1c28c347de11) | bunchesofdonald |
| 2026-11-17 | [Start the flow run suspension observer before the engine loads the fl…](https://github.com/PrefectHQ/prefect/commit/99ef57658a7d4231d0c6a997556e8ef29e3b4237) | bunchesofdonald |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
