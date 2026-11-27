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
| ⭐ **Stars** | 24.3k |
| 🍴 **Forks** | 2.7k |
| 🐞 **Open issues + PRs** | [807](https://github.com/PrefectHQ/prefect/issues) |
| 💻 **Languages** | Python 79% · TypeScript 20% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `python` `workflow` `data-engineering` `data-science` `workflow-engine` `prefect` `infrastructure` `ml-ops` `data-ops` `automation` `orchestration` `data` `observability` `pipeline` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2018-06-29 |
| 📦 **Latest release** | [3.9.5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 251.1 MB |
| 🌐 **Website** | https://prefect.io |

## 📦 Recent releases

### [3.9.6.dev2](https://github.com/PrefectHQ/prefect/releases/tag/3.9.6.dev2) — 3.9.6.dev2: Nightly Development Release _(pre-release)_
<sub>2026-11-26 · yesterday</sub>

> **What's Changed**
> **Development & Tidiness 🧹**
> * Require environment approval for Docker image releases by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24096
> **Uncategorized**
> * docs: clarify run and trigger for shell operations by @Himanshuagrawal4 in https://github.com/PrefectHQ/prefect/pull/24098
> * Parse `Retry-After` in concurrency slot acquisition services by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/24086
> …

### [3.9.6.dev1](https://github.com/PrefectHQ/prefect/releases/tag/3.9.6.dev1) — 3.9.6.dev1: Nightly Development Release _(pre-release)_
<sub>2026-11-25 · 2d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Document the 422 response bodies the API sends in the OpenAPI schema by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23880
> **Full Changelog**: https://github.com/PrefectHQ/prefect/compare/3.9.5...3.9.6.dev1

### [3.9.5](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5) — 3.9.5 - Let sleeping schedules lie
<sub>2026-11-24 · 2d ago</sub>

> **Enhancements ➕➕**
> * Speed up event trigger matching by indexing exact related-resource names by [@chuqCTC](https://github.com/chuqCTC) in [#23323](https://github.com/PrefectHQ/prefect/pull/23323)
> * Edit all parameters as JSON when copying a run to a new run by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#23861](https://github.com/PrefectHQ/prefect/pull/23861)
> * Add `prefect.runtime.get_logger()` for logging inside and outside Prefect runs by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24019](https://github.com/PrefectHQ/prefect/pull/24019)
> * Support non-root users in the official Docker image by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24027](https://github.com/PrefectHQ/prefect/pull/24027)
> * Edit `RRULE` schedules in the V2 schedule dialog by [@devin-ai-integration](https://github.com/apps/devin-ai-integration) in [#24012](https://github.com/PrefectHQ/prefect/pull/24012)
> …

### [3.9.5.dev4](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev4) — 3.9.5.dev4: Nightly Development Release _(pre-release)_
<sub>2026-11-24 · 3d ago</sub>

> **What's Changed**
> **Enhancements ➕➕**
> * Document virtual network configuration for ACI flow containers by @himanshuchawla0807-gif in https://github.com/PrefectHQ/prefect/pull/23620
> * Read V2 state colors from body so color modes apply by @zzstoatzz in https://github.com/PrefectHQ/prefect/pull/23804
> **Bug Fixes 🐞**
> * Keep the client transition id on states substituted by rejecting rules by @devin-ai-integration[bot] in https://github.com/PrefectHQ/prefect/pull/23977
> …

### [3.9.5.dev3](https://github.com/PrefectHQ/prefect/releases/tag/3.9.5.dev3) — 3.9.5.dev3: Nightly Development Release _(pre-release)_
<sub>2026-11-22 · 5d ago</sub>

> **What's Changed**
> **Bug Fixes 🐞**
> * Aggregate nested collections of states when determining the final state by @Nacl-HCl in https://github.com/PrefectHQ/prefect/pull/23474
> **Uncategorized**
> * Reject `--param` and `--job-variable` values without `=` in `prefect deployment run` by @harshit3355 in https://github.com/PrefectHQ/prefect/pull/24035
> **New Contributors**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Apply the V2 runs page's default filter before loading (#23908)](https://github.com/PrefectHQ/prefect/commit/5f7d879aa1636e42ca6697548c5c0065dafbff7a) | zzstoatzz |
| 2026-11-25 | [fix(ui): absent columns in artifacts table (#23958)](https://github.com/PrefectHQ/prefect/commit/0778e660eb86ba049f2ca6c738f6d05dbe601eae) | uinstinct |
| 2026-11-25 | [Show an invalid field error from `prefect init` for `--field` values …](https://github.com/PrefectHQ/prefect/commit/034f0e56de5f8014242c1a4f2c9bc8dec214357a) | LuisFigueroaG |
| 2026-11-25 | [docs: add MinIO example to flow code storage guide (#24101)](https://github.com/PrefectHQ/prefect/commit/bc6dcd90407345c54a2a1090f96f1fd9c3228c41) | devin-ai-integration[bot] |
| 2026-11-25 | [Show Enum member names for Enum parameters (#24094)](https://github.com/PrefectHQ/prefect/commit/0522881bf157be996b5ea6688159435482abca5e) | devin-ai-integration[bot] |
| 2026-11-25 | [Create tasks for sources in PrefectDbtRunner during `dbt source fresh…](https://github.com/PrefectHQ/prefect/commit/126ff395ad6e24dceea819697644b834edaac958) | vyagubov |
| 2026-11-25 | [Allow block references for `$defs` block types in job variable valida…](https://github.com/PrefectHQ/prefect/commit/c700ff889506ae798996eb31257af4f1bef0eb18) | devin-ai-integration[bot] |
| 2026-11-25 | [fix(server): support FastAPI 0.163 null filter bodies (#24099)](https://github.com/PrefectHQ/prefect/commit/501bd4dc7c3b6ed96f803182ef2693237ac9ab6d) | devin-ai-integration[bot] |
| 2026-11-25 | [Cache Redis messaging publisher settings (#23956)](https://github.com/PrefectHQ/prefect/commit/ed4c76fef29de8024db02c2ab3a4c63a431c715e) | fatih-acar |
| 2026-11-25 | [Parse `Retry-After` in concurrency slot acquisition services (#24086)](https://github.com/PrefectHQ/prefect/commit/7f657539c2979cf1e00d1408ab973f6e08fad494) | devin-ai-integration[bot] |

[See all commits ↗](https://github.com/PrefectHQ/prefect/commits)

## ⬇️ Get it

```bash
git clone https://github.com/PrefectHQ/prefect.git
```
