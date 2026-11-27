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
| ⭐ **Stars** | 4.8k |
| 🍴 **Forks** | 247 |
| 🐞 **Open issues + PRs** | [476](https://github.com/restatedev/restate/issues) |
| 💻 **Languages** | Rust 100% |
| 📜 **License** | Other |
| 🏷 **Topics** | `distributed-systems` `async-await` `durable-execution` `microservices` `consistent-state` `reliable-communication` `serverless` `event-driven` `cli` `workflow-engine` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-01-04 |
| 📦 **Latest release** | [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 119.6 MB |
| 🌐 **Website** | https://docs.restate.dev |

## 📦 Recent releases

### [v1.8.1-hotfix.3](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.3)
<sub>2026-11-20 · 6d ago</sub>

> **Restate v1.8.1-hotfix.3**
> **Install**
> **Pull the Docker images**
> ```sh
> docker pull docker.restate.dev/restatedev/restate:1.8.1-hotfix.3
> docker pull docker.restate.dev/restatedev/restate-cli:1.8.1-hotfix.3
> …

### [v1.8.1-hotfix.2](https://github.com/restatedev/restate/releases/tag/v1.8.1-hotfix.2)
<sub>2026-11-02 · 25d ago</sub>

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
| 2026-11-27 | [[Docs] Describe how to retire partition processor logic](https://github.com/restatedev/restate/commit/5fb156a12983b0e7e02308ff6d59e5c5c5c1e866) | tillrohrmann |
| 2026-11-27 | [[Worker] Let operators opt into retiring journal v1](https://github.com/restatedev/restate/commit/563cdfd8add8ea23a6514fdffa9cce8a61ec9720) | tillrohrmann |
| 2026-11-27 | [[Worker] Store no completions in journal v1 once journal v1 is retired](https://github.com/restatedev/restate/commit/a83a250aa44225ee95b85e94621f8ef499666cd2) | tillrohrmann |
| 2026-11-27 | [[Worker] Add the RetireJournalV1 partition feature](https://github.com/restatedev/restate/commit/5fad894b4159ad9eec7765f0c10c8c4c724be39f) | tillrohrmann |
| 2026-11-27 | [[PartitionStore] Restore partitions lacking required features from a …](https://github.com/restatedev/restate/commit/e667b46ad92583de91b29992c1417aab4afa9640) | tillrohrmann |
| 2026-11-27 | [[Worker] Apply only control commands while a required feature is missing](https://github.com/restatedev/restate/commit/806fe4d5a6da0d0b5f77bb1842c7fc43ef61ae59) | tillrohrmann |
| 2026-11-27 | [[Worker] Refuse to start partitions that lack required features](https://github.com/restatedev/restate/commit/ee44eb6a5117c48ed03e922a504c8c4c201e08df) | tillrohrmann |
| 2026-11-27 | [[Invoker] Run invocation tasks as local tasks with bounded output que…](https://github.com/restatedev/restate/commit/c554be814b67612b57300d4d643e252d980f4c82) | MohamedBassem |
| 2026-11-26 | [[QueryEngineV2] Narrow invocation status indexes by stage and effecti…](https://github.com/restatedev/restate/commit/a2d478d08b9daa50bd4ab00db9cd90a78bcd0404) | AhmedSoliman |
| 2026-11-26 | [[QueryEngineV2] Read the newest entries through the creation index](https://github.com/restatedev/restate/commit/4f4d3a6da6b697a653c813433d11252902d59c07) | AhmedSoliman |

[See all commits ↗](https://github.com/restatedev/restate/commits)

## ⬇️ Get it

```bash
git clone https://github.com/restatedev/restate.git
```
