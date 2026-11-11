# temporalio/temporal

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/temporalio/temporal)

> Temporal service

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why I saved it** | Durable workflow execution engine (Temporal server) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 24.3k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/temporalio/temporal/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `cronjob-scheduler` `distributed-cron` `distributed-systems` `durable-execution` `golang` `microservice-framework` `microservice-orchestration` `microservices-architecture` `orchestrator` `service-bus` `service-fabric` `workflow-automation` `workflow-engine` `workflow-management` `workflow-management-system` `workflows` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 170.0 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 8d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 8d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 8d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.30 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12828
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.30.8...v1.30.9

### [v1.31.4](https://github.com/temporalio/temporal/releases/tag/v1.31.4)
<sub>2026-10-12 · 29d ago</sub>

> **What's Changed**
> * Bump default CLI to 1.9.1 on release/v1.31.x by @chaptersix in https://github.com/temporalio/temporal/pull/12275
> * [v1.31.x] Configure CHASM internal callback namespace binding (#11876) by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12319
> * [v1.31.x] Validate both token readings in internal callback namespace check by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12382
> * Backport #12323 to release/v1.31.x by @michaely520 in https://github.com/temporalio/temporal/pull/12329
> * Make fair task gc conditional on rangeid (#12283) by @carlydf in https://github.com/temporalio/temporal/pull/12415
> …

### [v1.30.8](https://github.com/temporalio/temporal/releases/tag/v1.30.8)
<sub>2026-10-12 · 29d ago</sub>

> **What's Changed**
> * Bump default CLI to 1.9.1 on release/v1.30.x by @chaptersix in https://github.com/temporalio/temporal/pull/12274
> * [v1.30.x] Configure CHASM internal callback namespace binding (#11876) by @davidporter-id-au in https://github.com/temporalio/temporal/pull/12318
> * Backport #12323 to release/v1.30.x by @michaely520 in https://github.com/temporalio/temporal/pull/12330
> * Make fair task gc conditional on rangeid (#12283) by @carlydf in https://github.com/temporalio/temporal/pull/12427
> * Bump ServerVersion to 1.30.8 by @rkannan82 in https://github.com/temporalio/temporal/pull/12459
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [Fix V2 schedules closing before their final action starts (#13016)](https://github.com/temporalio/temporal/commit/03ecd1d228d2b8d9d433da55785afc9aeeead918) | davidporter-id-au |
| 2026-11-11 | [CHASM UpdateWithStart now takes a start hint and handle conflict polices (#12856)](https://github.com/temporalio/temporal/commit/85b80a1836dbc73741cb52586297dc35e6c937ca) | chanric |
| 2026-11-10 | [Emit the SDK-reported poller target in worker metrics (#13021)](https://github.com/temporalio/temporal/commit/7d614b5e3611856b7c9c8a92bbe78686745181b2) | veeral-patel |
| 2026-11-10 | [Handle duplicate shard reports during namespace handover (#12980)](https://github.com/temporalio/temporal/commit/c37c3dbc80c959e8ea07c4cc7738a04b4286324c) | yux0 |
| 2026-11-10 | [Update go.temporal.io/api to v1.64.3 (#13022)](https://github.com/temporalio/temporal/commit/935d22f1981147b57fcf5ff58335e8a114514237) | veeral-patel |
| 2026-11-10 | [Fix history_size/history_count CompletionStats double emitting (#12931)](https://github.com/temporalio/temporal/commit/915dbdc6ee6419c0cb0be25c80b45d3fe44226c3) | buildwithmalik |
| 2026-11-10 | [Add temporal_with_cassandra build tag to compile out Cassandra persistence (#12795)](https://github.com/temporalio/temporal/commit/64246670a6ad35f4e2e1a5fa4d961d75af1ba8ea) | stephanos |
| 2026-11-10 | [rename and add more time-skipping util functions (#13008)](https://github.com/temporalio/temporal/commit/de692e219b98757ef0e74ab5baa99877361e9250) | feiyang3cat |
| 2026-11-10 | [Fix await accepting cancelled attempts as successful (#12868)](https://github.com/temporalio/temporal/commit/862b2db4c869a27607710238c52182658220041e) | stephanos |
| 2026-11-10 | [Support passwordCommand in temporal-sql-tool (#12719)](https://github.com/temporalio/temporal/commit/1934fd8b1965904d17af3fe5a3221f3d0a0b943b) | riggggo |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## 👥 Top contributors

[wxing1292](https://github.com/wxing1292) (935) · [alexshtin](https://github.com/alexshtin) (932) · [yycptt](https://github.com/yycptt) (682) · [stephanos](https://github.com/stephanos) (660) · [dnr](https://github.com/dnr) (530)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
