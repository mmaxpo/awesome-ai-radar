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
| 🍴 **Forks** | 243 |
| 🐞 **Open issues + PRs** | [477](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 120.2 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3)
<sub>2026-11-20 · 2d ago</sub>

> **Restate v1.8.1-hotfix.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.3
> …

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 21d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 1mo ago</sub>

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
| 2026-11-23 | [[partition-store] Remove unused Scan*Table traits and background iter…](https://github.com/restatedev/restate/commit/ac7349729ed9436f17933346dc5f267484589eb0) | MohamedBassem |
| 2026-11-23 | [[cleaner] Change the cleaner to use the new cooperative iterator (#6021)](https://github.com/restatedev/restate/commit/2b36fb6b052ff055bce8e425c080efce2516af98) | MohamedBassem |
| 2026-11-23 | [[cluster controller] Check the metadata store quorum in the safety ch…](https://github.com/restatedev/restate/commit/f7d7f5732c6eedcced761c85bdde0fab13a3ce19) | MohamedBassem |
| 2026-11-23 | [[QueryEngineV2] Merge ID joins on key fields the reads emit](https://github.com/restatedev/restate/commit/de59663b1f75c56a20a85377d13abbf0ef309045) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Merge shard-local ID joins on their native order](https://github.com/restatedev/restate/commit/e39b0af0fe157e4aa14e9933fbe94790e42fb646) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Declare the native orders of every storage table's reads](https://github.com/restatedev/restate/commit/43a79a405809005effae9f3a9052ba77f9919416) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Wait for failed task cleanup before test teardown](https://github.com/restatedev/restate/commit/e6a3cd53f2a7ba2c03f4a299cbfb5805a3a5cb4d) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Join shard-locally over a union of a table's layouts](https://github.com/restatedev/restate/commit/400ebf47fc9a1d57244c7e44c578f95dff7e9db6) | AhmedSoliman |
| 2026-11-22 | [[QueryEngineV2] Join shard-locally on sharding columns that imply sha…](https://github.com/restatedev/restate/commit/3ce07ba1457c4a8f5cff611201b9e7c65e6cf2d5) | AhmedSoliman |
| 2026-11-22 | [[DataFusion] Optionally compress the batches of query tasks](https://github.com/restatedev/restate/commit/510b3a79c61c67519d07a6287779b24774dda643) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
