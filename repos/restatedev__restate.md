# restatedev/restate

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/restatedev/restate)

> Restate is the platform for building resilient applications that tolerate all infrastructure faults w/o the need for a PhD.

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
| ⭐ **Stars** | 4.7k |
| 🍴 **Forks** | 234 |
| 🐞 **Open issues + PRs** | [477](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `async-await` `cli` `consistent-state` `distributed-systems` `durable-execution` `event-driven` `microservices` `reliable-communication` `serverless` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 114.1 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 8d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 19d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 20d ago</sub>

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
<sub>2026-10-13 · 28d ago</sub>

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
| 2026-11-10 | [[restatectl] Show how much log lies between a snapshot and the tail](https://github.com/restatedev/restate/commit/dab17e70f0b6957416a2cde9203762d5df3a50c6) | AhmedSoliman |
| 2026-11-10 | [[partition-store] Record snapshots' log byte offsets in latest.json](https://github.com/restatedev/restate/commit/f7ac5501b08e6d6edb256b7c8733495ee54682fd) | AhmedSoliman |
| 2026-11-10 | [[worker] Auto-enable byte offsets once every worker runs v1.9.0](https://github.com/restatedev/restate/commit/67380144b20354e9166891939cc92e43585f0c3b) | AhmedSoliman |
| 2026-11-10 | [[worker] Auto-enable partition byte offsets from v1.9.0-dev](https://github.com/restatedev/restate/commit/ac0158680a47e1a736e5016a18ae43683406dcbe) | AhmedSoliman |
| 2026-11-10 | [[partition-store] Record byte offsets in snapshot metadata](https://github.com/restatedev/restate/commit/4ab0bb4615c5407f79bbf3703fbb7d777e244373) | AhmedSoliman |
| 2026-11-10 | [[worker] Show byte offsets in partition_state](https://github.com/restatedev/restate/commit/bee1cc5abbebab46fc918dc3f366b5fce6a925d6) | AhmedSoliman |
| 2026-11-10 | [[partition-store] Track the partition store byte offset](https://github.com/restatedev/restate/commit/50d36ef46843834dad1a4c61d3ade43380af00c8) | AhmedSoliman |
| 2026-11-10 | [[pp-bench] Read the applied LSN the way the partition does](https://github.com/restatedev/restate/commit/7311b77c257701d8705003b4901c7e5f889d8a87) | AhmedSoliman |
| 2026-11-10 | [[worker] Track partitions' log byte offset](https://github.com/restatedev/restate/commit/3704ba6c502fe62afe9ac1fd5973d6cde3bfb8f5) | AhmedSoliman |
| 2026-11-10 | [[pp-bench] Use the shared --json flag](https://github.com/restatedev/restate/commit/af1ac41f9f2055a4d7ee1f02eb56f4dab052eb36) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## 👥 Top contributors

[tillrohrmann](https://github.com/tillrohrmann) (1537) · [AhmedSoliman](https://github.com/AhmedSoliman) (1122) · [slinkydeveloper](https://github.com/slinkydeveloper) (626) · [jackkleeman](https://github.com/jackkleeman) (339) · [muhamadazmy](https://github.com/muhamadazmy) (308)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
