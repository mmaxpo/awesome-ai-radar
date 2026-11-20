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
| 🐞 **Open issues + PRs** | [483](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2) — 2026-11-02 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 118.8 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 18d ago</sub>

> **Restate v1.8.1-hotfix.2**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.2
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.2
> …

### [v1.7.14](https://github.com/restatedev/restate/releases/tag/v1.7.14)
<sub>2026-10-22 · 28d ago</sub>

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
| 2026-11-20 | [[Scheduler] Hand partition leadership only to replicas close to the l…](https://github.com/restatedev/restate/commit/2bacf553f2b759913f61aa5a51766f7a6029b681) | StephanEwen |
| 2026-11-20 | [[PartitionStore] Read invocations by status through the status index'…](https://github.com/restatedev/restate/commit/d6e229138d9fb92e15ceb53ae1ac23a149383690) | AhmedSoliman |
| 2026-11-20 | [[PartitionStore] Map invocation status conditions to the status index…](https://github.com/restatedev/restate/commit/3a978abba35160d5fa26c6f98851762135f97906) | AhmedSoliman |
| 2026-11-20 | [[PartitionStore] Index entries by stage and status, by creation and b…](https://github.com/restatedev/restate/commit/dce2c2c63fef7257e6813f63f4e3e3950d76fad9) | AhmedSoliman |
| 2026-11-20 | [[QueryEngineV2] Read the invocation list through the hourly creation …](https://github.com/restatedev/restate/commit/a12b378847b259338f395f2db30e36816785e7c5) | AhmedSoliman |
| 2026-11-20 | [[UI] Updating Restate UI to v1.1.8 published at https://github.com/re…](https://github.com/restatedev/restate/commit/4548a2b5946531b306106e6e3d4a71d2c2e478f6) | restatedev-web-ui[bot] |
| 2026-11-20 | [[Bifrost] Limit replicated loglet read-ahead by records and bytes (#5…](https://github.com/restatedev/restate/commit/6dca3f9292d31acac099e43aafb29ff2eea412b5) | StephanEwen |
| 2026-11-20 | [[PartitionStore] Merge an index's runs one time bucket at a time](https://github.com/restatedev/restate/commit/d73c9c7e7d55a0b00e2ff8831b4fdbd2e72fa0d7) | AhmedSoliman |
| 2026-11-20 | [[PartitionStore] Index every entry by creation hour and service, with…](https://github.com/restatedev/restate/commit/de7eeac3c926bc9db436f5bba4190601a96610f8) | AhmedSoliman |
| 2026-11-20 | [[PartitionStore] Let secondary indexes store a value with each key](https://github.com/restatedev/restate/commit/4a9ca52e87951a2d02827f4a4b55fde47d14bddf) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
