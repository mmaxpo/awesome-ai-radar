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
| 🐞 **Open issues + PRs** | [880](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.2) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 247.8 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.3.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3.dev2) — 3.9.3.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-13 · today</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Run duration-balanced Postgres groups on every Python version by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23863
> * Run duration-balanced SQLite test groups by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23865
> **Bug Fixes 🐞**
> * Fix SQLAlchemy cursor reuse for parameterized fetches by @shion233 in https://github.com/PrefectHQ/prefect/pull/23847
> …

### [3.9.3.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3.dev1) — 3.9.3.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-10 · 3d ago</sub>

> **What's Changed**
> **Development & Tidiness 🧹**
> * Fix flaky UI E2E tests reading stale default task run names by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23829
> **Uncategorized**
> * chore(deps): Update dependency @hookform/resolvers to v7 by @prefect-renovate[bot] in https://github.com/PrefectHQ/prefect/pull/23824
> * chore(deps): Update dependency pixi-viewport to v7 by @prefect-renovate[bot] in https://github.com/PrefectHQ/prefect/pull/23825
> …

### [3.9.2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.2) — 3.9.2 - It’s okay to let go of a lock that already let go of you
<sub>2026-11-06 · 6d ago</sub>

> **3.9.2 - It’s okay to let go of a lock that already let go of you**
> *Released on November 06, 2026*
> **Enhancements ➕➕**
> * Reduce deployment writes from queue polling by [@chuqCTC](https://github.com/chuqCTC) in [#23130](https://github.com/PrefectHQ/prefect/pull/23130)
> **Bug Fixes 🐞**
> * Render list-of-lists table artifacts in `ArtifactDataView` by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#23359](https://github.com/PrefectHQ/prefect/pull/23359)
> …

### [3.9.2.dev6](https://github.com/PrefectHQ/prefect/releases/tag/3.9.2.dev6) — 3.9.2.dev6: Nightly Development Release _(pre-release)_
<sub>2026-11-06 · 7d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Stop flow run heartbeats before proposing a terminal state by @chrisguidry in https://github.com/PrefectHQ/prefect/pull/23784
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.2.dev5...3.9.2.dev6

### [3.9.2.dev5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.2.dev5) — 3.9.2.dev5: Nightly Development Release _(pre-release)_
<sub>2026-11-05 · 8d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Only write deployments that a poll actually changes by @chuqCTC in https://github.com/PrefectHQ/prefect/pull/23130
> **Bug Fixes 🐞**
> * Accept the same flow state hook signatures in the engine and the runner by @CassianoE in https://github.com/PrefectHQ/prefect/pull/23715
> * Keep deployment schedule parameter overrides on partial schedule updates by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23719
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [Fix retry restart of async generator tasks closed during finalizer fa…](https://github.com/PrefectHQ/prefect/commit/53ad34955fbcccdff163c41ad0447d52d49be9c8) | dfbustosus |
| 2026-11-12 | [Generate automatic Dockerfile in `DockerImage` build context (#23747)](https://github.com/PrefectHQ/prefect/commit/e77b19eff992f20fe394e629130fb51ef3a8b3cf) | devin-ai-integration[bot] |
| 2026-11-12 | [Detect ACI container start from the container group instead of only t…](https://github.com/PrefectHQ/prefect/commit/52c80af8dd609407c18da0add692e1451c5db8cf) | devin-ai-integration[bot] |
| 2026-11-12 | [Make the delete-block message assertions actually run (#23767)](https://github.com/PrefectHQ/prefect/commit/978605212e386ad1a09418ce706398fe65333740) | dylanpulver |
| 2026-11-12 | [docs: document form button type pitfall in ui-v2 components AGENTS.md…](https://github.com/PrefectHQ/prefect/commit/b7ca990129e74fd386b09367e0916389ad2d4c3e) | devin-ai-integration[bot] |
| 2026-11-12 | [fix(prefect-redis): keep messages published while a publisher flush i…](https://github.com/PrefectHQ/prefect/commit/1996bd00e767124ea9e65ce3b94252f15b25337c) | devin-ai-integration[bot] |
| 2026-11-12 | [Show the script error from `prefect deploy` and `prefect flow serve` …](https://github.com/PrefectHQ/prefect/commit/b73c4ee602c12a2d8a8a05e885215463e117d409) | CassianoE |
| 2026-11-12 | [Keep `Annotated[T, Field(description=...)]` descriptions in flow para…](https://github.com/PrefectHQ/prefect/commit/ff5ba09cfc6d33261c3b395a7a9d8b125b686453) | CassianoE |
| 2026-11-12 | [Reserve hosted test API server port before starting uvicorn (#23799)](https://github.com/PrefectHQ/prefect/commit/2433f8690e4c5864e51e9a2aa5e37e048f2998fe) | devin-ai-integration[bot] |
| 2026-11-12 | [Skip fetching a pinned commit that the clone already contains (#23814)](https://github.com/PrefectHQ/prefect/commit/7707eb3cd4050c841644aa8a60a3e9cb1c0a4158) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
