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
| 🐞 **Open issues + PRs** | [873](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 248.8 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.4.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.4.dev1) — 3.9.4.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-14 · today</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Fix CodSpeed import benchmark timeout and fail the job on benchmark failures by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23897
> **Development & Tidiness 🧹**
> * Fix flaky test_concurrency_context_releases_slots_async by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23891
> **Documentation 📓**
> …

### [3.9.3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3) — 3.9.3 - `aclose()`ing time
<sub>2026-11-13 · today</sub>

> **Enhancements ➕➕**
> * Add search and ordering to the automations page by [@uinstinct](https://github.com/uinstinct) in [#23048](https://github.com/PrefectHQ/prefect/pull/23048)
> * Align flow runs timeline ticks to local time boundaries by [@theluckystrike](https://github.com/theluckystrike) in [#23272](https://github.com/PrefectHQ/prefect/pull/23272)
> **Bug Fixes 🐞**
> * Fix early closure of async generator flows by [@desertaxle](https://github.com/desertaxle) in [#23886](https://github.com/PrefectHQ/prefect/pull/23886)
> * Fix retry restart of async generator tasks closed during finalizer failure by [@dfbustosus](https://github.com/dfbustosus) in [#23739](https://github.com/PrefectHQ/prefect/pull/23739)
> …

### [3.9.3.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3.dev2) — 3.9.3.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-13 · yesterday</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Run duration-balanced Postgres groups on every Python version by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23863
> * Run duration-balanced SQLite test groups by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23865
> **Bug Fixes 🐞**
> * Fix SQLAlchemy cursor reuse for parameterized fetches by @shion233 in https://github.com/PrefectHQ/prefect/pull/23847
> …

### [3.9.3.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.3.dev1) — 3.9.3.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-10 · 4d ago</sub>

> **What's Changed**
> **Development & Tidiness 🧹**
> * Fix flaky UI E2E tests reading stale default task run names by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23829
> **Uncategorized**
> * chore(deps): Update dependency @hookform/resolvers to v7 by @prefect-renovate[bot] in https://github.com/PrefectHQ/prefect/pull/23824
> * chore(deps): Update dependency pixi-viewport to v7 by @prefect-renovate[bot] in https://github.com/PrefectHQ/prefect/pull/23825
> …

### [3.9.2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.2) — 3.9.2 - It’s okay to let go of a lock that already let go of you
<sub>2026-11-06 · 7d ago</sub>

> **3.9.2 - It’s okay to let go of a lock that already let go of you**
> *Released on November 06, 2026*
> **Enhancements ➕➕**
> * Reduce deployment writes from queue polling by [@chuqCTC](https://github.com/chuqCTC) in [#23130](https://github.com/PrefectHQ/prefect/pull/23130)
> **Bug Fixes 🐞**
> * Render list-of-lists table artifacts in `ArtifactDataView` by [@devin-ai-integration](https://github.com/devin-ai-integration)[bot] in [#23359](https://github.com/PrefectHQ/prefect/pull/23359)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [Update prefect-aws integration pin (#23902)](https://github.com/PrefectHQ/prefect/commit/29241a3aff4ad41bf79ed5782ea4059cb74d0b4d) | prefect-ci-bot-public[bot] |
| 2026-11-13 | [Fix flaky test_concurrency_context_releases_slots_async (#23891)](https://github.com/PrefectHQ/prefect/commit/f7f89c5a884192406dd33fd1c7ece09072bfb79e) | devin-ai-integration[bot] |
| 2026-11-13 | [docs: document worker submission bookkeeping contract in workers AGEN…](https://github.com/PrefectHQ/prefect/commit/22747733faa9827a4e53e0e9bb9b9881f6073581) | devin-ai-integration[bot] |
| 2026-11-13 | [Fix CodSpeed import benchmark timeout and fail the job on benchmark f…](https://github.com/PrefectHQ/prefect/commit/b39bb40ea7ba52e7ce2ee3de7880aecf44081cd2) | devin-ai-integration[bot] |
| 2026-11-13 | [Bump tornado from 6.6 to 6.6.1 (#23901)](https://github.com/PrefectHQ/prefect/commit/34505b4fd82521ee0525f21804585d25574a5d62) | dependabot[bot] |
| 2026-11-13 | [docs: document rrule wall-clock timezone contract in server AGENTS.md…](https://github.com/PrefectHQ/prefect/commit/c1bd94996f1835272aa0f937257a2e5d2a9ff030) | devin-ai-integration[bot] |
| 2026-11-13 | [docs: document ScriptError traceback convention in CLI AGENTS.md (#23…](https://github.com/PrefectHQ/prefect/commit/911a64f7556c1964ce593aa392f694e1163a7ad1) | devin-ai-integration[bot] |
| 2026-11-13 | [docs: note integrations' reliance on private core engine APIs in AGEN…](https://github.com/PrefectHQ/prefect/commit/73f06799ed9822497a472a9be5c22701afb6237d) | devin-ai-integration[bot] |
| 2026-11-13 | [docs: note floating aws-cdk-lib release risk in prefect-aws AGENTS.md…](https://github.com/PrefectHQ/prefect/commit/91be1bb01e8d395c3f81cd691520b07a32e6625c) | devin-ai-integration[bot] |
| 2026-11-13 | [docs: update NormalizedSchedule guidance in server AGENTS.md (#23889)](https://github.com/PrefectHQ/prefect/commit/04eb540298554b13d12c3aa65ff9abfc936907ec) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
