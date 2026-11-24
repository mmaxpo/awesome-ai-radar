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
| 🐞 **Open issues + PRs** | [473](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 118.2 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3)
<sub>2026-11-20 · 3d ago</sub>

> **Restate v1.8.1-hotfix.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.3
> …

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 22d ago</sub>

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
| 2026-11-24 | [[DataFusion] Show scheduled_start_at whenever it is selected](https://github.com/restatedev/restate/commit/7667acf7527cd1a75acc2d052ebda0d903f09b00) | AhmedSoliman |
| 2026-11-24 | [[QueryEngineV2] Ship index candidates to partitions instead of one index](https://github.com/restatedev/restate/commit/7f97e9727761f88102f7b56d34b415c556c15c36) | AhmedSoliman |
| 2026-11-24 | [[Types] Derive record and invoker size overheads from one source](https://github.com/restatedev/restate/commit/69c7e0c56e247920ce2a3c69ea4c8e05bfb28056) | tillrohrmann |
| 2026-11-24 | [[Invoker] Keep the per-invocation memory limit above the accepted mes…](https://github.com/restatedev/restate/commit/dc09481a413e07f8a30e59cca7e93b82c390ffb7) | tillrohrmann |
| 2026-11-24 | [Write stage keys with entry statuses in the vqueue entry fixtures](https://github.com/restatedev/restate/commit/f48e373386e967289bb51d6683a310be25d0d43d) | AhmedSoliman |
| 2026-11-24 | [[QueryEngineV2] Let a sort's demand pass projections with computed co…](https://github.com/restatedev/restate/commit/8e38ace030fe37f78b81f694ce3214238c18f3e5) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Scan only the listed partition keys of invocations an…](https://github.com/restatedev/restate/commit/64c32a03f809ddf4c1c70c1c0b980594abc0c64a) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Check partition keys on every index read before fetching](https://github.com/restatedev/restate/commit/bc6e03fb11dcb1615142ad1c702752a10bccf8e4) | AhmedSoliman |
| 2026-11-23 | [[QueryEngineV2] Fetch only the named objects' statuses from an entry …](https://github.com/restatedev/restate/commit/641900c359d5aedb0bc704261a2453e8cdf63173) | AhmedSoliman |
| 2026-11-23 | [Show each invocation's stage and effective status in V1](https://github.com/restatedev/restate/commit/6bfe5e966060d4b34db79a296714656b3a587ffa) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
