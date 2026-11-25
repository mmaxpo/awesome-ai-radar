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
| 🍴 **Forks** | 246 |
| 🐞 **Open issues + PRs** | [475](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 118.7 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3)
<sub>2026-11-20 · 4d ago</sub>

> **Restate v1.8.1-hotfix.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.3
> …

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 23d ago</sub>

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
| 2026-11-25 | [[UI] Updating Restate UI to v1.1.9 published at https://github.com/re…](https://github.com/restatedev/restate/commit/40ec026463640d09df12c36fd2d1d71dd922b048) | restatedev-web-ui[bot] |
| 2026-11-25 | [Update connection pool readme to match implementation (#6049)](https://github.com/restatedev/restate/commit/53ac888901bcc4d57a960d50787eb0efed77b38c) | muhamadazmy |
| 2026-11-24 | [[PartitionStore] Keep only the entry indexes in use](https://github.com/restatedev/restate/commit/f1f3fede8baf740ea8b966aa52617283180543f5) | AhmedSoliman |
| 2026-11-24 | [[QueryEngineV2] Name indexes after their storage definitions](https://github.com/restatedev/restate/commit/d0c6ad2046cd27f6b7e594e28a8939aac11446d4) | AhmedSoliman |
| 2026-11-24 | [[Admin] Report in /version whether the statistics tables can answer](https://github.com/restatedev/restate/commit/82f204c839f1cd0dedc1d0aa54b08df18c59438d) | AhmedSoliman |
| 2026-11-24 | [Enable indexes and statistics with one option](https://github.com/restatedev/restate/commit/570b2131c776a235113a9cc4887d20e9888724d9) | AhmedSoliman |
| 2026-11-24 | [[DataFusion] Never return partial statistics totals, also without num…](https://github.com/restatedev/restate/commit/885610a971233aa28b9aaf2149a11f4ba948758c) | AhmedSoliman |
| 2026-11-24 | [[QueryEngineV2] Move the leader at admission in the stale-owner tests](https://github.com/restatedev/restate/commit/94d699c7fd9f22c6aa719b4f3b3be37243cda9de) | AhmedSoliman |
| 2026-11-24 | [Always decode blobs even with large values](https://github.com/restatedev/restate/commit/407288eb1fa5ab0d0c30e5bce1dae97d2a645e45) | muhamadazmy |
| 2026-11-24 | [Store invocation results in a dedicated blob table (#5198)](https://github.com/restatedev/restate/commit/ac2ba0c34747572252db13c4d3281b6208f45f88) | muhamadazmy |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
