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
| 🐞 **Open issues + PRs** | [881](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.4.dev5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev5) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 248.7 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.4.dev5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev5) — 3.9.4.dev5: Nightly Development Release _(pre-release)_
<sub>2026-11-18 · today</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document `RemoteFileSystem` settings with an example by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23959
> **Uncategorized**
> * Start the flow run suspension observer before the engine loads the flow by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23947
> * Start the suspension observer early for MicroVM deployments that pull code by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23957
> …

### [3.9.4.dev4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev4) — 3.9.4.dev4: Nightly Development Release _(pre-release)_
<sub>2026-11-17 · yesterday</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Write auto-generated deployment Dockerfiles as UTF-8 in `prefect-docker` by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23929
> **Documentation 📓**
> * Document AWS setup for Lambda MicroVM push work pools by @bunchesofdonald in https://github.com/PrefectHQ/prefect/pull/23845
> * docs: fix dead and chained redirects, CLI page titles and stale links by @madureira-gabriel in https://github.com/PrefectHQ/prefect/pull/23941
> …

### [3.9.4.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev3) — 3.9.4.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-16 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Stop served flow runs on Windows without a console-wide CTRL_BREAK by @EnesSoydan in https://github.com/PrefectHQ/prefect/pull/23895
> * Accept any task runner in `@flow` and `Flow` `task_runner` type hints by @dayan02dev in https://github.com/PrefectHQ/prefect/pull/23893
> **Development & Tidiness 🧹**
> * Fix flaky `test_read_task_workers` by resetting the in-memory task worker tracker by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23903
> …

### [3.9.4.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev2) — 3.9.4.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-15 · 3d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Clarify ECS work pool network configuration by @prabhushreyas in https://github.com/PrefectHQ/prefect/pull/23911
> * fix(ui-v2): make the subflow run count respect the state filter by @Shanmukh-l33t in https://github.com/PrefectHQ/prefect/pull/23912
> **Documentation 📓**
> * docs: Add release notes for `prefect-redis==0.3.1` by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23915
> …

### [3.9.4.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev1) — 3.9.4.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-14 · 4d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Fix CodSpeed import benchmark timeout and fail the job on benchmark failures by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23897
> **Development & Tidiness 🧹**
> * Fix flaky test_concurrency_context_releases_slots_async by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23891
> **Documentation 📓**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Document `RemoteFileSystem` settings with an example (#23959)](https://github.com/PrefectHQ/prefect/commit/f6fef9f6fcb3768b9002dc48dc2ab9af824e72f0) | devin-ai-integration[bot] |
| 2026-11-17 | [Start the suspension observer early for MicroVM deployments that pull…](https://github.com/PrefectHQ/prefect/commit/5e8ca118fc514ffe9ab3355ea5cf1c28c347de11) | bunchesofdonald |
| 2026-11-17 | [Start the flow run suspension observer before the engine loads the fl…](https://github.com/PrefectHQ/prefect/commit/99ef57658a7d4231d0c6a997556e8ef29e3b4237) | bunchesofdonald |
| 2026-11-17 | [chore(deps): Update python dependencies (#23701)](https://github.com/PrefectHQ/prefect/commit/2b95707e76d52051e8ad8bd280ad6c8f50e36b5a) | prefect-renovate[bot] |
| 2026-11-17 | [chore(deps): Update dependency soupsieve to v4 [SECURITY] (#23932)](https://github.com/PrefectHQ/prefect/commit/543767a6e08de426012b6497f54261bddc0afb53) | prefect-renovate[bot] |
| 2026-11-16 | [chore(deps): Update Node.js (#23938)](https://github.com/PrefectHQ/prefect/commit/172fcb8e91095b619193b0c19a8cdd6c79464103) | prefect-renovate[bot] |
| 2026-11-16 | [chore(deps): Update npm dependencies (#23700)](https://github.com/PrefectHQ/prefect/commit/83bdb7c3a0f9ee8cb9cbfa639b462d8235bb3591) | prefect-renovate[bot] |
| 2026-11-16 | [chore(deps): Update dependency jsdom to v31 (#23937)](https://github.com/PrefectHQ/prefect/commit/2e4685e318a1888acf12252f538d2ba084a7f922) | prefect-renovate[bot] |
| 2026-11-16 | [chore(deps): Update dependency ruff to v0.17.4 (#23933)](https://github.com/PrefectHQ/prefect/commit/c7b2f982ac34dae35cd0cb2408ca6178be5f1c37) | prefect-renovate[bot] |
| 2026-11-16 | [chore(deps): Update github actions (#23935)](https://github.com/PrefectHQ/prefect/commit/2b833ba273f738e394a2a5944f590e0355c5bd55) | prefect-renovate[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
