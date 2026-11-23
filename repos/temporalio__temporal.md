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
| ⭐ **Stars** | 24.6k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/temporalio/temporal/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `workflows` `workflow-engine` `workflow-automation` `workflow-management` `workflow-management-system` `distributed-systems` `golang` `service-bus` `service-fabric` `microservices-architecture` `microservice-framework` `microservice-orchestration` `cronjob-scheduler` `distributed-cron` `orchestrator` `durable-execution` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 175.0 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 20d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 20d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 20d ago</sub>

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
| 2026-11-23 | [Deliver child completion to the current parent run when the reset run…](https://github.com/temporalio/temporal/commit/cd668989792406a24b72672dbbfd1e98a66e3853) | cestercian |
| 2026-11-21 | [Add internal RPC for worker heartbeats (#8600)](https://github.com/temporalio/temporal/commit/32ef011fbd1e38ecddf656fc3f5026f6641cfeab) | rkannan82 |
| 2026-11-21 | [Define a minimal CHASM entity to durably track worker liveness (#8564)](https://github.com/temporalio/temporal/commit/4e0a45f161d3889f66e212795a53bce219494e83) | rkannan82 |
| 2026-11-21 | [Fix flakes: raise deadlock detection timeout in `TestChildWorkflowInh…](https://github.com/temporalio/temporal/commit/59c4ca9a6bad1e55f02eddca4062e07b6bf15cf7) | carlydf |
| 2026-11-21 | [Optionally enforce JWT audience on Nexus HTTP handlers (#13219)](https://github.com/temporalio/temporal/commit/6af9e3901af8828156c0b6a8a8d8130209012fd0) | chrsmith |
| 2026-11-20 | [Discard history tasks if namespace is soft deleted (#13140)](https://github.com/temporalio/temporal/commit/817b67f3b25d1ff0888847efdbbc4ed2b0d836c8) | awln-temporal |
| 2026-11-20 | [Find reset anchor in history for closed workflows (#13012)](https://github.com/temporalio/temporal/commit/29b5567221b2e01b830000245f85d166e494cd91) | jiechenz |
| 2026-11-20 | [Fix flaky TestMultipleTasks_ValidateStats test (#13185)](https://github.com/temporalio/temporal/commit/ea8df3ed523e767bf663a7f442600fffa12c96ed) | veeral-patel |
| 2026-11-20 | [Fix testx bump workflow races (#13209)](https://github.com/temporalio/temporal/commit/c44a13c6d2973babd589525a3b3db7ae5f19116d) | stephanos |
| 2026-11-20 | [Use namespace.Name in TestEnv.SendSignal (#13205)](https://github.com/temporalio/temporal/commit/bb5f7e6740a2f1b3c40ac425eaa31f539b969b38) | stephanos |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
