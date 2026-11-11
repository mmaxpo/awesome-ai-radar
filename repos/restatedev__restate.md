# restatedev/restate

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/restatedev/restate)

> Restate is the platform for building resilient applications that tolerate all infrastructure faults w/o the need for a PhD.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🔁 Durable workflows & orchestration |
| **Project** | — |
| **Why it's worth a look** | Durable execution platform for resilient apps/workflows |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.7k |
| 🍴 **Forks** | 234 |
| 🐞 **Open issues + PRs** | [474](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 115.0 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 9d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 20d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 21d ago</sub>

> **Restate v1.8.1**
> v1.8.1 is a drop-in upgrade from v1.8.0, and you can roll back to v1.8.0 unless you enable signal recording. If you are still on v1.7.x, follow the [v1.8.0 upgrade requirements](https://github.com/restatedev/restate/blob/main/release-notes/v1.8.0.md#upgrade--rollback-guidance).
> **✨ Highlights**
> **🌊 Smoother Hand-Over When Migrating to the Kafka Ingress Integration**
> When you delete a Kafka subscription, Restate now finishes ingesting the records it has already read before it stops. It then logs the last ingested offset of every topic partition. When you [migrate a topic to the Kafka ingress integration](https://docs.restate.dev/services/integrations/kafka#migrating-from-the-old-kafka-support), you can use these offsets to start the integration exactly where Restate stopped. That way no record is processed twice and none is skipped.
> **🗑️ Bulk Deployment Removal**
> …

### [v1.8.0](https://github.com/restatedev/restate/releases/tag/v1.8.0)
<sub>2026-10-14 · 28d ago</sub>

> **Restate v1.8.0 🎉**
> **✨ Release Highlights**
> **🚦 VQueues On by Default**
> Virtual Queues, the new invocation scheduler powering Restate's [flow control features](https://docs.restate.dev/services/flow-control), are now on for every cluster, no opt-in required. Scopes, limit keys and scoped Virtual Object targets work out of the box.
> > ⚠️ **Read before upgrading**: all nodes must run **v1.7.3 or newer** first, and each partition runs a one-time migration during which it is unavailable. See [Upgrade & Rollback Guidance →](https://github.com/restatedev/restate/blob/main/release-notes/v1.8.0.md#upgrade--rollback-guidance)
> **🤖 A CLI Built for Scripts, CI and AI Agents**
> …

### [v1.8.0-rc.3](https://github.com/restatedev/restate/releases/tag/v1.8.0-rc.3) _(pre-release)_
<sub>2026-10-13 · 29d ago</sub>

> **Restate v1.8.0-rc.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.0-rc.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.0-rc.3
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [[VQueues] Test immediate and retained completion](https://github.com/restatedev/restate/commit/2347460189bbea4b68f2b856f42f27e8a8119d55) | AhmedSoliman |
| 2026-11-11 | [[VQueues] Delete entries that finish without retention in one storage…](https://github.com/restatedev/restate/commit/00a458cf3703933aa859df4a2625dc8427d07451) | AhmedSoliman |
| 2026-11-11 | [[Core] Require network protocol V3 or newer](https://github.com/restatedev/restate/commit/e8c09e07418d6adc809275f003c51db85f425452) | AhmedSoliman |
| 2026-11-11 | [[Scheduler] Pick first replica with the highest score as leader](https://github.com/restatedev/restate/commit/25a9154d967d662b4f9a03f153fc1ecabad2e553) | tillrohrmann |
| 2026-11-11 | [[Invoker] Remove unused InvocationReader methods (#5811)](https://github.com/restatedev/restate/commit/bca481cbb6db337b4f3499a6b453cbaaed6f95d1) | MohamedBassem |
| 2026-11-11 | [Bump gardal to 0.1.0](https://github.com/restatedev/restate/commit/b47b542d5726112b55ee42d013fffd554a8cbff9) | AhmedSoliman |
| 2026-11-11 | [[chore] Bump rustix to 1.1.6 for RUSTSEC-2026-0486](https://github.com/restatedev/restate/commit/8838b42caa86862988ff36b552c733ef61e56192) | AhmedSoliman |
| 2026-11-10 | [[restatectl] Show how much log lies between a snapshot and the tail](https://github.com/restatedev/restate/commit/dab17e70f0b6957416a2cde9203762d5df3a50c6) | AhmedSoliman |
| 2026-11-10 | [[partition-store] Record snapshots' log byte offsets in latest.json](https://github.com/restatedev/restate/commit/f7ac5501b08e6d6edb256b7c8733495ee54682fd) | AhmedSoliman |
| 2026-11-10 | [[worker] Auto-enable byte offsets once every worker runs v1.9.0](https://github.com/restatedev/restate/commit/67380144b20354e9166891939cc92e43585f0c3b) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
