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
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 172.3 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 14d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 14d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 14d ago</sub>

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
| 2026-11-17 | [fix: refuse polls that arrive after ShutdownWorker of an unloaded tas…](https://github.com/temporalio/temporal/commit/a1e005230fbe050c83c8c285dcbf0bbfbd7093b4) | moetemp |
| 2026-11-17 | [Add CHASM Speculative Transition (#13025)](https://github.com/temporalio/temporal/commit/23e4eab0337a0df7c65e4e1132651941f8a8209b) | chanric |
| 2026-11-17 | [Align Schedules V1/V2 metric label sets for Prometheus (#12270)](https://github.com/temporalio/temporal/commit/b116145b754d87a12463434ce33bf9afc89bde20) | davidporter-id-au |
| 2026-11-17 | [Sanitize Nexus return-path links (#12956)](https://github.com/temporalio/temporal/commit/38e5535f2448b2670878867618726a9c3a472487) | chrsmith |
| 2026-11-17 | [Cap the total size of links attached to a CHASM execution (#12955)](https://github.com/temporalio/temporal/commit/763c820eb3487af077d801f102e617c1975b3196) | chrsmith |
| 2026-11-17 | [Standardize link validation on an injected links.Validator (#12954)](https://github.com/temporalio/temporal/commit/3bbfa0bbc0d27645e5ce813e4c64d8b03645f568) | chrsmith |
| 2026-11-16 | [Validate migrated schedule state (#13125)](https://github.com/temporalio/temporal/commit/5d3e50a91f2b8b6fff6ab486a0b904e2639785f7) | chaptersix |
| 2026-11-16 | [verify query task (#13097)](https://github.com/temporalio/temporal/commit/8b1df85d697287095b3f2156e4a14bb7587fdb66) | feiyang3cat |
| 2026-11-16 | [Bump temporal-auto-scaled-workers to 782664acf475 to skip task add ho…](https://github.com/temporalio/temporal/commit/a6d5f5feb3d9a81fec59a77c56a7ddc8f3f5dd12) | mani-j9 |
| 2026-11-16 | [Accept SOFT_DELETE namespace state in metadata manager (#13002)](https://github.com/temporalio/temporal/commit/d07491318a628f477a9369c8eaa183bb3de31459) | awln-temporal |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
