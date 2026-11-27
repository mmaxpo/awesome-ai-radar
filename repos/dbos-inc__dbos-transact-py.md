# dbos-inc/dbos-transact-py

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/dbos-inc/dbos-transact-py)

> Database-Backed Durable Python Workflows

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why it's worth a look** | Durable Python workflows backed by Postgres |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.7k |
| 🍴 **Forks** | 128 |
| 🐞 **Open issues + PRs** | [11](https://github.com/dbos-inc/dbos-transact-py/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `python` `dbos` `postgresql` `microservice-orchestration` `orchestration` `workflow-engine` `durable-execution` `microservices-orchestration` `agentic-workflow` `cronjob-scheduler` `workflows` `sqlite` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-07-19 |
| 📦 **Latest release** | [3.7.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.7.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.1 MB |
| 🌐 **Website** | https://docs.dbos.dev |

## 📦 Recent releases

### [3.7.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.7.0)
<sub>2026-11-24 · 2d ago</sub>

> **What's Changed**
> * Batch Async Result Polling by @oleksii-tumanov in https://github.com/dbos-inc/dbos-transact-py/pull/962
> * Delete By Level by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/969
> * Workflow Archiving by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/959
> * Bulk rewind by @lanice in https://github.com/dbos-inc/dbos-transact-py/pull/971
> * Suspend Workflow GetResult by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/970
> …

### [3.6.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.6.0)
<sub>2026-11-17 · 9d ago</sub>

> **Behavior Changes**
> This release changes how DBOS workflow management operations (cancel, resume, fork rewind) interact with queues. Previously, these operations would clear queue information, so the workflow was no longer associated with any queue. Now, these operations do not clear queue operations, so cancelling and resuming a workflow re-enqueues the workflow to its original queue, and rewinding or forking a workflow similarly re-enqueues it (a cancelled or otherwise terminated workflow still does not consume a queue slot until resumed and re-enqueued). You can override this behavior by passing a different queue into resume, rewind, or fork. We made this change because of consistent user feedback that the original behavior (clearing queue information) was unintuitive.
> **What's Changed**
> * Timestamp Workflows from Statement Time by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/950
> * DBOS.recover_workflows by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/951
> * Consistently Make DBOS Methods Durable Steps by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/955
> …

### [3.5.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.5.0)
<sub>2026-11-10 · 16d ago</sub>

> **What's Changed**
> * Better Queue Locking by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/932
> * Suspend by @maxdml in https://github.com/dbos-inc/dbos-transact-py/pull/927
> * External Storage by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/928
> * Async Suspend by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/933
> * Fast Path for Binary Serialization by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/934
> …

### [3.4.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.4.0)
<sub>2026-10-28 · 29d ago</sub>

> **What's Changed**
> * Poll only the status column for preemptible step cancellation by @buftio in https://github.com/dbos-inc/dbos-transact-py/pull/898
> * fix: do not require *args and **kwargs in pydantic argument validation by @spicysharkco in https://github.com/dbos-inc/dbos-transact-py/pull/899
> * Exit with the failing command's code from dbos start by @warun7 in https://github.com/dbos-inc/dbos-transact-py/pull/902
> * fix: index latest application-version lookup paths by @axieax in https://github.com/dbos-inc/dbos-transact-py/pull/900
> * Retry database pool checkout timeouts by @March-7 in https://github.com/dbos-inc/dbos-transact-py/pull/910
> …

### [3.3.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.3.0)
<sub>2026-10-15 · 1mo ago</sub>

> **Package Change**
> This release moves the DBOS Conductor client to a separate Enterprise package. If you are using DBOS Conductor or Cloud, please install the Enterprise optional dependency when upgrading:
> ```
> pip install dbos[enterprise]
> ```
> If you are only using the open source library, without Conductor or Cloud, you don't need to make any changes.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Conductor client (#972)](https://github.com/dbos-inc/dbos-transact-py/commit/4d237499282adc2bef1cfc33ccf26f72bfadc740) | maxdml |
| 2026-11-25 | [stop auto-upgrader after the drain but before releasing the backgroun…](https://github.com/dbos-inc/dbos-transact-py/commit/2a2a9a6d0d0deb25fffa3d672b92b5c50d494a1e) | maxdml |
| 2026-11-25 | [Stop the auto-upgrade loop before the workflow drain (#979)](https://github.com/dbos-inc/dbos-transact-py/commit/d3cd0882afb074601b9840e284c466d0bc4c9257) | maxdml |
| 2026-11-24 | [Skip the wait setup for zero-timeout recv and get_event (#977)](https://github.com/dbos-inc/dbos-transact-py/commit/da90502e8e850f83e4e6bbe4bc18a7cc46cea9b4) | buftio |
| 2026-11-24 | [Pin the partitioned dequeue's PENDING check to index probes (#976)](https://github.com/dbos-inc/dbos-transact-py/commit/e9fe7d7033ee0207ea2ba0f20a049cadf9164ece) | buftio |
| 2026-11-20 | [Suspend Workflow GetResult (#970)](https://github.com/dbos-inc/dbos-transact-py/commit/28192bd87ee81891546803fb583ea6a22c08d1ce) | kraftp |
| 2026-11-20 | [Bulk rewind (#971)](https://github.com/dbos-inc/dbos-transact-py/commit/bad3353fd43d943b3a095073d28d8724382c093b) | lanice |
| 2026-11-19 | [Workflow Archiving (#959)](https://github.com/dbos-inc/dbos-transact-py/commit/95d25eb51a93e6794935bf0ee96403273416b91c) | kraftp |
| 2026-11-18 | [Delete By Level (#969)](https://github.com/dbos-inc/dbos-transact-py/commit/afef3f7d396a14a14801bfc9ac865b7bdbff996e) | kraftp |
| 2026-11-17 | [Batch Async Result Polling (#962)](https://github.com/dbos-inc/dbos-transact-py/commit/9924fe6b6018f08304341d100adeb60c42712808) | oleksii-tumanov |

[See all commits ↗](https://github.com/dbos-inc/dbos-transact-py/commits)

## ⬇️ Get it

```bash
git clone https://github.com/dbos-inc/dbos-transact-py.git
```
