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
| 🍴 **Forks** | 2.2k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/temporalio/temporal/issues) |
| 💻 **Languages** | Go 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `workflows` `workflow-engine` `workflow-automation` `workflow-management` `workflow-management-system` `distributed-systems` `golang` `service-bus` `service-fabric` `microservices-architecture` `microservice-framework` `microservice-orchestration` `cronjob-scheduler` `distributed-cron` `orchestrator` `durable-execution` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2019-10-16 |
| 📦 **Latest release** | [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 176.5 MB |
| 🌐 **Website** | https://docs.temporal.io |

## 📦 Recent releases

### [v1.32.2](https://github.com/temporalio/temporal/releases/tag/v1.32.2)
<sub>2026-11-02 · 21d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.32 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12831
> * [release/v1.32.x] Bump auto-scaled-workers to v0.2.1-1.32.0.158.0 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12849
> * Fix sticky queue stats zeroed out by @rkannan82 in https://github.com/temporalio/temporal/pull/11527
> * Fix a race condition that can leave a poll to not get cancelled during shutdown by @rkannan82 in https://github.com/temporalio/temporal/pull/11841
> * Fix priority backlog acknowledgement after expired tasks by @cbsandeep10 in https://github.com/temporalio/temporal/pull/12595
> …

### [v1.31.5](https://github.com/temporalio/temporal/releases/tag/v1.31.5)
<sub>2026-11-02 · 21d ago</sub>

> **What's Changed**
> * Fix security vulnerabilities for 1.31 minor release by @yycptt in https://github.com/temporalio/temporal/pull/12829
> * [release/v1.31.x] Bump auto-scaled-workers to v0.0.1-1.31.2 by @gcristea-temporal in https://github.com/temporalio/temporal/pull/12850
> **Potential Breaking Change**
> - `ValidateWorkerDeploymentVersionComputeConfig` now requires Write access to the namespace. The API has persistent side-effects inconsistent with read-only access, so this requirement is aligned with the API bahavior. Please refer to https://github.com/temporalio/temporal/pull/12843 for details.
> **Full Changelog**: https://github.com/temporalio/temporal/compare/v1.31.4...v1.31.5

### [v1.30.9](https://github.com/temporalio/temporal/releases/tag/v1.30.9)
<sub>2026-11-02 · 21d ago</sub>

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
| 2026-11-23 | [Add keepalive dial option to local frontend gRPC connection (#12819)](https://github.com/temporalio/temporal/commit/4197dfdd52eb338c932e64db209e3853fc7a032d) | AdamMagued |
| 2026-11-23 | [Defer V1->V2 schedule auto-migration while a backfill is in progress …](https://github.com/temporalio/temporal/commit/170953cf9b8f11ac5344cd6ec58f8673adfa0403) | davidporter-id-au |
| 2026-11-23 | [Measure workflow cache entry size under the workflow lock (#13214)](https://github.com/temporalio/temporal/commit/0f9d8d7400483a33e382809ed7d42afe8fc572c7) | abenn135 |
| 2026-11-23 | [Reject HTTP redirects on outbound Nexus requests (#13221)](https://github.com/temporalio/temporal/commit/411dadbd9fdfe0997d2ac9d79867763f6a3e305c) | chrsmith |
| 2026-11-23 | [Check eager namespace refresh membership with the namespace's replica…](https://github.com/temporalio/temporal/commit/b12de7289e7768eafa9ea0fc4756d571133ef486) | michaely520 |
| 2026-11-23 | [Make admin rate limiting the default and add RawHistory endpoints (#1…](https://github.com/temporalio/temporal/commit/c69a19148744830943ec22dd49139d58c4ab4f99) | ratdaddy |
| 2026-11-23 | [WHN impl 2: store worker control queue when workflow task starts (#12…](https://github.com/temporalio/temporal/commit/5208234bde6867e25c1a9b984d4652505b4c5e23) | feiyang3cat |
| 2026-11-23 | [Decide legacy namespace replication from resolver membership (#13218)](https://github.com/temporalio/temporal/commit/10f3a667e7132426d41dc4af802a0aaab174876d) | qyc5937 |
| 2026-11-23 | [Deliver child completion to the current parent run when the reset run…](https://github.com/temporalio/temporal/commit/cd668989792406a24b72672dbbfd1e98a66e3853) | cestercian |
| 2026-11-21 | [Add internal RPC for worker heartbeats (#8600)](https://github.com/temporalio/temporal/commit/32ef011fbd1e38ecddf656fc3f5026f6641cfeab) | rkannan82 |

[See all commits ↗](https://github.com/temporalio/temporal/commits)

## ⬇️ Get it

```bash
git clone https://github.com/temporalio/temporal.git
```
