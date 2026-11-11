# dbos-inc/dbos-transact-py

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/dbos-inc/dbos-transact-py)

> Database-Backed Durable Python Workflows

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Project** | — |
| **Why I saved it** | — |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.7k |
| 🍴 **Forks** | 123 |
| 🐞 **Open issues + PRs** | [12](https://github.com/dbos-inc/dbos-transact-py/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agentic-workflow` `cronjob-scheduler` `dbos` `durable-execution` `microservice-orchestration` `microservices-orchestration` `orchestration` `postgresql` `python` `sqlite` `workflow-engine` `workflows` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2024-07-19 |
| 📦 **Latest release** | [3.5.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.5.0) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.0 MB |
| 🌐 **Website** | https://docs.dbos.dev |

## 📦 Recent releases

### [3.5.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.5.0)
<sub>2026-11-10 · today</sub>

> **What's Changed**
> * Better Queue Locking by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/932
> * Suspend by @maxdml in https://github.com/dbos-inc/dbos-transact-py/pull/927
> * External Storage by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/928
> * Async Suspend by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/933
> * Fast Path for Binary Serialization by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/934
> …

### [3.4.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.4.0)
<sub>2026-10-28 · 13d ago</sub>

> **What's Changed**
> * Poll only the status column for preemptible step cancellation by @buftio in https://github.com/dbos-inc/dbos-transact-py/pull/898
> * fix: do not require *args and **kwargs in pydantic argument validation by @spicysharkco in https://github.com/dbos-inc/dbos-transact-py/pull/899
> * Exit with the failing command's code from dbos start by @warun7 in https://github.com/dbos-inc/dbos-transact-py/pull/902
> * fix: index latest application-version lookup paths by @axieax in https://github.com/dbos-inc/dbos-transact-py/pull/900
> * Retry database pool checkout timeouts by @March-7 in https://github.com/dbos-inc/dbos-transact-py/pull/910
> …

### [3.3.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.3.0)
<sub>2026-10-15 · 26d ago</sub>

> **Package Change**
> This release moves the DBOS Conductor client to a separate Enterprise package. If you are using DBOS Conductor or Cloud, please install the Enterprise optional dependency when upgrading:
> ```
> pip install dbos[enterprise]
> ```
> If you are only using the open source library, without Conductor or Cloud, you don't need to make any changes.
> …

### [3.2.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.2.0)
<sub>2026-09-29 · 1mo ago</sub>

> **What's Changed**
> * Improve Workflow Conflict Resolution by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/862
> * publish preview releases when merging to main by @maxdml in https://github.com/dbos-inc/dbos-transact-py/pull/863
> * Keep the version build hook out of the wheel by @Kayvan-Zahiri in https://github.com/dbos-inc/dbos-transact-py/pull/868
> * Custom Sessionmaker by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/866
> * Delete Datasource Checkpoints by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/867
> …

### [3.1.0](https://github.com/dbos-inc/dbos-transact-py/releases/tag/3.1.0)
<sub>2026-09-24 · 1mo ago</sub>

> **What's Changed**
> * Improved Queue Index by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/857
> * Set Conductor Metadata-Only Mode Locally by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/858
> * Rewind by @maxdml in https://github.com/dbos-inc/dbos-transact-py/pull/856
> * Workflow ID Reuse Policies - #1372 by @kraftp in https://github.com/dbos-inc/dbos-transact-py/pull/859
> * drop outputs for rewound workflows by @maxdml in https://github.com/dbos-inc/dbos-transact-py/pull/861
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-10 | [Timestamp Workflows from Statement Time (#950)](https://github.com/dbos-inc/dbos-transact-py/commit/9c807ec7bf2d00e33a862ed3c18c4e0811ff7ae8) | kraftp |
| 2026-11-09 | [Fix Suspend Indexes (#948)](https://github.com/dbos-inc/dbos-transact-py/commit/0e59afe872e5974a2b79b396152accc3cd33e6c7) | kraftp |
| 2026-11-09 | [fix(serialization): restore dates in variadic workflow inputs (#944)](https://github.com/dbos-inc/dbos-transact-py/commit/b5d2f3f3e31101c03f690de4e946ecb04bdfbe91) | mkzung |
| 2026-11-09 | [Fix #940 and #939: SQLite system database/datasource reads run outside the write lock (#943)](https://github.com/dbos-inc/dbos-transact-py/commit/f86363bbff894ba9c2b8f6f9358835ae94aae968) | ApparentlyTejas |
| 2026-11-04 | [More Scalable Scheduler (#936)](https://github.com/dbos-inc/dbos-transact-py/commit/236142bd7a99ff77d04becf5f405a60d6f330591) | kraftp |
| 2026-11-02 | [patch: handle gaps in checkpoints order (#935)](https://github.com/dbos-inc/dbos-transact-py/commit/232dd751576b7d350a3614ad4ef7fc786eb282ff) | maxdml |
| 2026-11-02 | [Fast Path for Binary Serialization (#934)](https://github.com/dbos-inc/dbos-transact-py/commit/bfb57412d9b9c8ac3bfac3f1dda735c44efd6314) | kraftp |
| 2026-10-30 | [Async Suspend (#933)](https://github.com/dbos-inc/dbos-transact-py/commit/bca092dab48455effd10ef3a32f32167c24399ab) | kraftp |
| 2026-10-30 | [External Storage (#928)](https://github.com/dbos-inc/dbos-transact-py/commit/5ff2028783078dc54af2f5223ed06623760f7d2e) | kraftp |
| 2026-10-29 | [Suspend (#927)](https://github.com/dbos-inc/dbos-transact-py/commit/6b8e790f42287b120bd5c264169d3f693ee641b9) | maxdml |

[See all commits ↗](https://github.com/dbos-inc/dbos-transact-py/commits)

## 👥 Top contributors

[kraftp](https://github.com/kraftp) (406) · [qianl15](https://github.com/qianl15) (77) · [maxdml](https://github.com/maxdml) (50) · [chuck-dbos](https://github.com/chuck-dbos) (33) · [devhawk](https://github.com/devhawk) (29)

## ⬇️ Get it

```bash
git clone https://github.com/dbos-inc/dbos-transact-py.git
```
