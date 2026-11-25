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
| 🐞 **Open issues + PRs** | [806](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 250.3 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.6.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.6.dev1) — 3.9.6.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-25 · today</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Document the 422 response bodies the API sends in the OpenAPI schema by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23880
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.5...3.9.6.dev1

### [3.9.5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5) — 3.9.5 - Let sleeping schedules lie
<sub>2026-11-24 · today</sub>

> **Enhancements ➕➕**
> * Speed up event trigger matching by indexing exact related-resource names by [@chuqCTC](https://github.com/chuqCTC) in [#23323](https://github.com/PrefectHQ/prefect/pull/23323)
> * Edit all parameters as JSON when copying a run to a new run by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#23861](https://github.com/PrefectHQ/prefect/pull/23861)
> * Add `prefect.runtime.get_logger()` for logging inside and outside Prefect runs by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24019](https://github.com/PrefectHQ/prefect/pull/24019)
> * Support non-root users in the official Docker image by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24027](https://github.com/PrefectHQ/prefect/pull/24027)
> * Edit `RRULE` schedules in the V2 schedule dialog by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24012](https://github.com/PrefectHQ/prefect/pull/24012)
> …

### [3.9.5.dev4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev4) — 3.9.5.dev4: Nightly Development Release _(pre-release)_
<sub>2026-11-24 · yesterday</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document virtual network configuration for ACI flow containers by @himanshuchawla0807-gif in https://github.com/PrefectHQ/prefect/pull/23620
> * Read V2 state colors from body so color modes apply by @zzstoatzz in https://github.com/PrefectHQ/prefect/pull/23804
> **Bug Fixes 🐞**
> * Keep the client transition id on states substituted by rejecting rules by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23977
> …

### [3.9.5.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev3) — 3.9.5.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-22 · 3d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Aggregate nested collections of states when determining the final state by @Nacl-HCl in https://github.com/PrefectHQ/prefect/pull/23474
> **Uncategorized**
> * Reject `--param` and `--job-variable` values without `=` in `prefect deployment run` by @harshit3355 in https://github.com/PrefectHQ/prefect/pull/24035
> **New Contributors**
> …

### [3.9.5.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev2) — 3.9.5.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-21 · 4d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Run db vacuum tasks one at a time on the maintenance pool by @ShikhJohari in https://github.com/PrefectHQ/prefect/pull/23742
> **Development & Tidiness 🧹**
> * Fix `ReactiveTriggers` stop race during startup by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24021
> * Fix flaky `test_keeps_polling_while_setup_hangs` observer test by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23950
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Cache Redis messaging publisher settings (#23956)](https://github.com/PrefectHQ/prefect/commit/ed4c76fef29de8024db02c2ab3a4c63a431c715e) | fatih-acar |
| 2026-11-25 | [Parse `Retry-After` in concurrency slot acquisition services (#24086)](https://github.com/PrefectHQ/prefect/commit/7f657539c2979cf1e00d1408ab973f6e08fad494) | devin-ai-integration[bot] |
| 2026-11-25 | [docs: clarify run and trigger for shell operations (#24098)](https://github.com/PrefectHQ/prefect/commit/93dd48bb36ad61fa428ebb89ac085398622f3c16) | Himanshuagrawal4 |
| 2026-11-25 | [Require environment approval for Docker image releases (#24096)](https://github.com/PrefectHQ/prefect/commit/2306dca596775f1b81591f8316b072bd3a78ff42) | devin-ai-integration[bot] |
| 2026-11-25 | [Document the 422 response bodies the API sends in the OpenAPI schema …](https://github.com/PrefectHQ/prefect/commit/bda190753d55d950239a2f9dfda8c7cfb863343e) | devin-ai-integration[bot] |
| 2026-11-24 | [docs: Add release notes for 3.9.5 (#24095)](https://github.com/PrefectHQ/prefect/commit/77c4e31a83b18a559902dbbba174cdb7532008ff) | devin-ai-integration[bot] |
| 2026-11-24 | [fix(client): stop concurrent requests from invalidating each other's …](https://github.com/PrefectHQ/prefect/commit/6bc6ba28868ca67d99d42329361fbda60cdbe85a) | yukiyan |
| 2026-11-24 | [Trim orchestration policy and schedule tests and delete same-file dup…](https://github.com/PrefectHQ/prefect/commit/6eabbf84fcbdbdf0018c3abc729221c9fd39c0c0) | devin-ai-integration[bot] |
| 2026-11-24 | [Fix flaky `test_create_schedule_respects_max_future_time` (#24075)](https://github.com/PrefectHQ/prefect/commit/b3091bb09073b60e4bedcf06a01bc312617b5569) | devin-ai-integration[bot] |
| 2026-11-24 | [fix(tests): stabilize flaky cleanup lease-deadline tests (#24093)](https://github.com/PrefectHQ/prefect/commit/1a22fab8722ab88252c0fadebf313c4ed06722bb) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
