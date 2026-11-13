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
| 🐞 **Open issues + PRs** | [470](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 116.1 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 11d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 21d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 23d ago</sub>

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

### [v1.8.0-rc.3](https://github.com/restatedev/restate/releases/tag/v1.8.0-rc.3) _(pre-release)_
<sub>2026-10-13 · 1mo ago</sub>

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
| 2026-11-13 | [[PartitionStore] Arm fault points per partition](https://github.com/restatedev/restate/commit/a5b5a6a29c9c2e2cd251aab2328132e3b701ea80) | AhmedSoliman |
| 2026-11-13 | [[PartitionStore] Declare the statistics and maintain registered index…](https://github.com/restatedev/restate/commit/a302ef3c9d1e77d2f862458f9c257a66be3eee53) | AhmedSoliman |
| 2026-11-13 | [[PartitionStore] Execute prepared reads on a partition snapshot](https://github.com/restatedev/restate/commit/59ef8c785d6193a8cf1243f376222cdb32c8743b) | AhmedSoliman |
| 2026-11-13 | [[query] Add the in-process read contracts and schema bindings](https://github.com/restatedev/restate/commit/aef31d2988d5e1de22639942a4c9d5499f4db73b) | AhmedSoliman |
| 2026-11-13 | [[InvokerReader] Read invocation data for the invoker through a partit…](https://github.com/restatedev/restate/commit/3ae395f4e718d85fda57d6ee88754ec669f71a23) | MohamedBassem |
| 2026-11-13 | [[PartitionStore] Record the index registry and walks](https://github.com/restatedev/restate/commit/ec6c1a82e55c6385e07205566b3ac9a387629096) | AhmedSoliman |
| 2026-11-13 | [[PartitionStore] Prepare key selections over ordered keys](https://github.com/restatedev/restate/commit/8ba9b2acbe841cf270cf41d47f07289c1bebfab6) | AhmedSoliman |
| 2026-11-13 | [[query] Declare the logical tables](https://github.com/restatedev/restate/commit/19e2a428ffbe7656660150aca555c8e5fe3cd475) | AhmedSoliman |
| 2026-11-12 | [[PartitionStore] Look up partition store values by KeyKind instead of…](https://github.com/restatedev/restate/commit/d802434dcb0d50e1aaab1d9f60754e392e1828e5) | MohamedBassem |
| 2026-11-12 | [[RocksDB] Choose the column family per lookup in Reader (#5836)](https://github.com/restatedev/restate/commit/adcdf1c7ad314e6c32b11efdbe77a6fd459f8d12) | MohamedBassem |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
