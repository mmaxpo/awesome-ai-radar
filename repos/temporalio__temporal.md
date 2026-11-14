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
| ⭐ **Stars** | 24.4k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/temporalio/temporal/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `workflows` `workflow-engine` `workflow-automation` `workflow-management` `workflow-management-system` `distributed-systems` `golang` `service-bus` `service-fabric` `microservices-architecture` `microservice-framework` `microservice-orchestration` `cronjob-scheduler` `distributed-cron` `orchestrator` `durable-execution` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 171.1 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 11d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 11d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 11d ago</sub>

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
| 2026-11-14 | [WHN metrics 2: add Update-aware WHN metrics with read-only registry c…](https://github.com/temporalio/temporal/commit/170fb83dca48fe82d69aa3ec3b6fe25acfc1791b) | feiyang3cat |
| 2026-11-14 | [Expose Nexus caller RPS throttle status in Describe (#13000)](https://github.com/temporalio/temporal/commit/623e5f171d11a33750818326519f8cb9738257db) | prathyushpv |
| 2026-11-14 | [Use CHASM UpdateWithStart in SANO. (#13070)](https://github.com/temporalio/temporal/commit/98925be15707693868c3a900a5d41df126da7fdf) | chanric |
| 2026-11-13 | [schedulertest: CHASM scheduler lifecycle driver, start ledger invaria…](https://github.com/temporalio/temporal/commit/e0bcb743c4549198417326b2bcd45fcb8ccda9c7) | davidporter-id-au |
| 2026-11-13 | [Tag Nexus operation failures by reason (#12340)](https://github.com/temporalio/temporal/commit/73f1acad34605ae6fe973579129adf45fb8c1dee) | stephanos |
| 2026-11-13 | [Chasm request id cleanup (#13029)](https://github.com/temporalio/temporal/commit/d577f5d58511b164fb91a4d1d96c2e4a8608d673) | chanric |
| 2026-11-13 | [Require matching request IDs for Nexus completions (#13077)](https://github.com/temporalio/temporal/commit/cbeb97f432b69ca02d5a2e5f4112b70bbaf7edf6) | tekkaya |
| 2026-11-13 | [Keep CHASM schedule buffers progressing after discarded or failed sta…](https://github.com/temporalio/temporal/commit/3aec1dcef0c08a19868983c97f577eeeec3083fc) | chaptersix |
| 2026-11-12 | [WHN metrics 1: add metrics of events that may generate workflow heart…](https://github.com/temporalio/temporal/commit/d2d307a0e06eb83f15d1301d39249b1c7554530c) | feiyang3cat |
| 2026-11-12 | [Use SQLite by default for mixed brain tests (#13048)](https://github.com/temporalio/temporal/commit/f16ceaa388296c2e412d79395a99444174319596) | stephanos |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
