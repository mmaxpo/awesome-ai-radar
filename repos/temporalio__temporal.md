# temporalio/temporal

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/temporalio/temporal)

> Temporal service

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why it's worth a look** | Durable workflow execution engine (Temporal server) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 24.5k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/temporalio/temporal/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `workflows` `workflow-engine` `workflow-automation` `workflow-management` `workflow-management-system` `distributed-systems` `golang` `service-bus` `service-fabric` `microservices-architecture` `microservice-framework` `microservice-orchestration` `cronjob-scheduler` `distributed-cron` `orchestrator` `durable-execution` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 175.9 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 17d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 17d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 17d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.30 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12828
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.30.8...v1.30.9

### [v1.30.8](https://github.com/temporalio/temporal/releases/tag/v1.30.8)
<sub>2026-10-12 · 1mo ago</sub>

> **What's Changed**
> * Bump default CLI to 1.9.1 on release/v1.30.x by @chaptersix in https://github.com/temporalio/temporal/pull/12274
> * [v1.30.x] Configure CHASM internal callback namespace binding (#11876) by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12318
> * Backport #12323 to release/v1.30.x by @michaely520 in https://github.com/temporalio/temporal/pull/12330
> * Make fair task gc conditional on rangeid (#12283) by @carlydf in https://github.com/temporalio/temporal/pull/12427
> * Bump ServerVersion to 1.30.8 by @rkannan82 in https://github.com/temporalio/temporal/pull/12459
> …

### [v1.31.4](https://github.com/temporalio/temporal/releases/tag/v1.31.4)
<sub>2026-10-12 · 1mo ago</sub>

> **What's Changed**
> * Bump default CLI to 1.9.1 on release/v1.31.x by @chaptersix in https://github.com/temporalio/temporal/pull/12275
> * [v1.31.x] Configure CHASM internal callback namespace binding (#11876) by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12319
> * [v1.31.x] Validate both token readings in internal callback namespace check by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12382
> * Backport #12323 to release/v1.31.x by @michaely520 in https://github.com/temporalio/temporal/pull/12329
> * Make fair task gc conditional on rangeid (#12283) by @carlydf in https://github.com/temporalio/temporal/pull/12415
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Bump go.temporal.io/testx to 4d3f3f0b9](https://github.com/temporalio/temporal/commit/2c8ae4e89b37d69e50aad460f4264b03447e6054) | temporal-data |
| 2026-11-19 | [WHN impl 1: the overall framework (#12991)](https://github.com/temporalio/temporal/commit/a8f8328b001bd3302e658cdd062e18a5e92cf50f) | feiyang3cat |
| 2026-11-19 | [Flow control (S): add concurrency service handler (#12895)](https://github.com/temporalio/temporal/commit/c524d769c40a6cdfd359a3fc9981ec5c5c5f4b58) | dnr |
| 2026-11-19 | [Flow control (W): add limiter release transfer tasks (#12898)](https://github.com/temporalio/temporal/commit/32dd6ab362eb5fef0fc33f8d69bf1344882036ad) | dnr |
| 2026-11-19 | [Flow control (R): add readiness cache foundation (#12958)](https://github.com/temporalio/temporal/commit/1c16be9604ea0601c6e00c22c76e512f52ebd2d9) | dnr |
| 2026-11-19 | [Fix CHASM scheduler creation rollout in feature tests (#12448)](https://github.com/temporalio/temporal/commit/cead54f6b59ad88f2495ec10fd7d68ebcbfa8bbb) | chaptersix |
| 2026-11-19 | [Migrate remaining functional test entrypoints to parallel suites (#13…](https://github.com/temporalio/temporal/commit/4d3f3f0b973d55215996324e489322b8af80d315) | stephanos |
| 2026-11-19 | [namespace replication: add verification tooling (PR4a) (#12416)](https://github.com/temporalio/temporal/commit/2433d4e477e6d74a108eff4f9bf0d04aa0c8076a) | qyc5937 |
| 2026-11-19 | [Bump go.temporal.io/testx to 4d2eaffb4](https://github.com/temporalio/temporal/commit/fd193d32ec42e2ed8785e251669ce0336bb6bc8a) | temporal-data |
| 2026-11-19 | [Add Await for parallelsuite Scope helpers (#13151)](https://github.com/temporalio/temporal/commit/4d2eaffb4719cbc6072eddce4a623611c1b06f3b) | stephanos |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
