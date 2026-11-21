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
| 🍴 **Forks** | 240 |
| 🐞 **Open issues + PRs** | [474](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 119.5 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3)
<sub>2026-11-20 · today</sub>

> **Restate v1.8.1-hotfix.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.3
> …

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 19d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 29d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 1mo ago</sub>

> **Restate v1.8.1**
> v1.8.1 is a drop-in upgrade from v1.8.0, and you can roll back to v1.8.0 unless you enable signal recording. If you are still on v1.7.x, follow the [v1.8.0 upgrade requirements](https://github.com/restatedev/restate/blob/main/release-notes/v1.8.0.md#upgrade--rollback-guidance).
> **✨ Highlights**
> **🌊 Smoother Hand-Over When Migrating to the Kafka Ingress Integration**
> When you delete a Kafka subscription, Restate now finishes ingesting the records it has already read before it stops. It then logs the last ingested offset of every topic partition. When you [migrate a topic to the Kafka ingress integration](https://docs.restate.dev/services/integrations/kafka#migrating-from-the-old-kafka-support), you can use these offsets to start the integration exactly where Restate stopped. That way no record is processed twice and none is skipped.
> **🗑️ Bulk Deployment Removal**
> …

### [v1.8.0](https://github.com/restatedev/restate/releases/tag/v1.8.0)
<sub>2026-10-14 · 1mo ago</sub>

> **Restate v1.8.0 🎉**
> **✨ Release Highlights**
> **🚦 VQueues On by Default**
> Virtual Queues, the new invocation scheduler powering Restate's [flow control features](https://docs.restate.dev/services/flow-control), are now on for every cluster, no opt-in required. Scopes, limit keys and scoped Virtual Object targets work out of the box.
> > ⚠️ **Read before upgrading**: all nodes must run **v1.7.3 or newer** first, and each partition runs a one-time migration during which it is unavailable. See [Upgrade & Rollback Guidance →](https://github.com/restatedev/restate/blob/main/release-notes/v1.8.0.md#upgrade--rollback-guidance)
> **🤖 A CLI Built for Scripts, CI and AI Agents**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [[QueryEngine] Treat `unknown` as a sentinel, never as a value](https://github.com/restatedev/restate/commit/2aaabe8cf63d4efa4ee1f99c7d1234ec5776eeea) | AhmedSoliman |
| 2026-11-21 | [[PartitionStore] Skip probe keys of pairs no status-index lane reads](https://github.com/restatedev/restate/commit/4272d581f6a0b42777ea493c616a8b002fea6ebc) | AhmedSoliman |
| 2026-11-21 | [[QueryEngine] Show canonical_id in sys_invocation](https://github.com/restatedev/restate/commit/963b8b8e1ac810d002a4ecf2e76d9b1c78adb03d) | AhmedSoliman |
| 2026-11-21 | [[QueryEngine] Show the stats tables' effective status](https://github.com/restatedev/restate/commit/0ac43558abc896d462beae1d10d3373e2f466a4d) | AhmedSoliman |
| 2026-11-20 | [[DataFusion] Encode task replies directly into Bytes](https://github.com/restatedev/restate/commit/7b61a76b2cc1188bcceaf569e55dc94140d45288) | AhmedSoliman |
| 2026-11-20 | [[QueryEngine] Show vqueue entries' effective status](https://github.com/restatedev/restate/commit/d4e1f615daf8f6c6cf2e7b88987ab06a880977b6) | AhmedSoliman |
| 2026-11-20 | [[PartitionStore] Retire finished_entry_by_outcome/1](https://github.com/restatedev/restate/commit/bc082154786182148ea10ffd2f4d0bf3463e0e38) | AhmedSoliman |
| 2026-11-20 | [[Types] Add the effective status of vqueue entries](https://github.com/restatedev/restate/commit/9adadb7d17c2d312b5a960e315a3adfe1b65b4fa) | AhmedSoliman |
| 2026-11-20 | [[Types] Move vqueue entries' Stage and Status to restate-types](https://github.com/restatedev/restate/commit/e052ec54144317b18300d88f8eaabcb3d67f297c) | AhmedSoliman |
| 2026-11-20 | [[Metadata] Add restate.schema.size.bytes gauge](https://github.com/restatedev/restate/commit/cf50c3e299e5e479bd907bff8a40b66f62c27c31) | tillrohrmann |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
