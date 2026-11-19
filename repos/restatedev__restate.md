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
| 🍴 **Forks** | 239 |
| 🐞 **Open issues + PRs** | [476](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 118.3 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 17d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 27d ago</sub>

> **Restate v1.7.14**
> Restate v1.7.14 is a security release. Restate now rejects TLS certificates issued through compromised emSign intermediate CAs. The release also updates the bundled TLS library to fix several recently disclosed vulnerabilities, and refreshes the OS trust store shipped in the Docker image.
> **🔒 Reject Certificates from Compromised emSign Intermediates**
> The private keys of several emSign (eMudhra) intermediate certificate authorities are publicly known, so anyone can use them to issue certificates that impersonate any server.
> Restate now rejects any certificate chain that passes through these intermediates, including their cross-signed variants. This applies to all outgoing TLS connections, such as calls to service deployments, AWS Lambda, and object stores.
> **Upgrade guidance:** No action is required. A server presenting a certificate from one of these intermediates will now fail the TLS handshake. Replace such certificates with ones from a trusted CA.
> …

### [v1.8.1](https://github.com/restatedev/restate/releases/tag/v1.8.1)
<sub>2026-10-21 · 29d ago</sub>

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
| 2026-11-19 | [[PartitionStore] Call a built index complete, like a finished migration](https://github.com/restatedev/restate/commit/dc16d12952ac60112c632a10ed6ffcdba4ab482e) | AhmedSoliman |
| 2026-11-19 | [[PartitionStore] Let 1.8.2 open walks that later releases link differ…](https://github.com/restatedev/restate/commit/3502b8e35b3b49544f274ac14f761fe89ac7645a) | AhmedSoliman |
| 2026-11-19 | [[PartitionStore] Make online migrations safe across replicas and roll…](https://github.com/restatedev/restate/commit/e7fac1f810539a625e1449c4ee6f4e70d40c51bc) | AhmedSoliman |
| 2026-11-19 | [[Invoker] Put the invoker's budgeted reads behind a lendable memory p…](https://github.com/restatedev/restate/commit/51d98902ac7fdde1b4b48e3a8f9d0d61e56fa0c6) | MohamedBassem |
| 2026-11-19 | [[PartitionStore] Widen blob ref count to u64 (#5960)](https://github.com/restatedev/restate/commit/6a5a0067d61205dd48b97b6ca37de54a3a9476d1) | muhamadazmy |
| 2026-11-19 | [Store large journal entry contents in the blob table (#5935)](https://github.com/restatedev/restate/commit/e0caff7f009e34c3760d1807f36389defdeb9eae) | muhamadazmy |
| 2026-11-18 | [[QueryEngineV2] Close a held read's task only once its Next has arrived](https://github.com/restatedev/restate/commit/7e9a3b235011bf749447aa48dda80c1c71e42bb0) | AhmedSoliman |
| 2026-11-18 | [[Bifrost] Keep the local loglet's sealed tail above acknowledged appends](https://github.com/restatedev/restate/commit/c5e83e12e01e9e180b42e0d3db54df594566684f) | AhmedSoliman |
| 2026-11-18 | [[PartitionStore] Track one-time migrations in the registry](https://github.com/restatedev/restate/commit/bb0ab5f8494f70c63ec73a9916ed13c0f443d5d6) | AhmedSoliman |
| 2026-11-18 | [[PartitionStore] Store registry records under their own key kind](https://github.com/restatedev/restate/commit/1cfe8f81bdd6f04363a9297c2c4a9f92e4d60a14) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
