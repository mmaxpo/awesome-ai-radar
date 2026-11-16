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
| 🍴 **Forks** | 236 |
| 🐞 **Open issues + PRs** | [460](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 117.1 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 14d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 24d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 26d ago</sub>

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
| 2026-11-16 | [[QueryEngineV2] Pin datafusion-distributed to our fork with the termi…](https://github.com/restatedev/restate/commit/18314d9e43df9ea524b38e533962cd59c31f35b8) | AhmedSoliman |
| 2026-11-16 | [[QueryEngineV2] Select the V2 engine in Admin queries and the SQL CLI](https://github.com/restatedev/restate/commit/d128849a5859fda62017f48437e8eaeb4faaa2e8) | AhmedSoliman |
| 2026-11-16 | [[QueryEngineV2] Serve the indexes and migration_jobs tables from V2](https://github.com/restatedev/restate/commit/5f4e9362d75698f5664269ff2c56c10d8035c937) | AhmedSoliman |
| 2026-11-16 | [[QueryEngineV2] Add the V2 query engine crate](https://github.com/restatedev/restate/commit/dcb3ab659fe655467f6453acd63604ba1620e9af) | AhmedSoliman |
| 2026-11-16 | [[Storage] Universal compaction for partition stores and the log-server](https://github.com/restatedev/restate/commit/64a6b2d19a8f53bddf1faa53c841667d72dd67c9) | AhmedSoliman |
| 2026-11-15 | [[QueryEngineV2] Admit query reads through the partition processor](https://github.com/restatedev/restate/commit/756a74ed50eb965b91b8bae248980d17ff47a906) | AhmedSoliman |
| 2026-11-15 | [[QueryEngineV2] Add network protocol V7 and the distributed query tas…](https://github.com/restatedev/restate/commit/c2214c2b5fec9ac0beb5a3c1b725c671ed5a81de) | AhmedSoliman |
| 2026-11-15 | [[DataFusion] Report remote scan failures as external errors, not Data…](https://github.com/restatedev/restate/commit/12adfb14c497b1577b1bba117f769e5eba941ee6) | AhmedSoliman |
| 2026-11-15 | [[CI] Lock rust-toolchain from master instead of stable](https://github.com/restatedev/restate/commit/b0ac8748bc92513ee27b6e0c07202fefab601f26) | AhmedSoliman |
| 2026-11-14 | [[Query] Show why a background migration isn't progressing in migratio…](https://github.com/restatedev/restate/commit/123f98b53e35343be85f952e67b62cda2ed511a7) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
