# openremote/core

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/openremote/core)

> 100% open-source IoT Platform - Integrate your devices, add intelligence, build custom apps

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Open-source IoT platform |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 2.2k |
| 🍴 **Forks** | 537 |
| 🐞 **Open issues + PRs** | [493](https://github.com/openremote/core/issues) |
| 💻 **Languages** | Java 48% · TypeScript 26% · Groovy 20% · Shell 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `iot-platform` `iot` `energy` `building` `mqtt` `smartcity` `dashboard` `asset-management` `mqtt-broker` `dataplatform` `rules-engine` `fleet-management` `energy-monitor` `energy-management` `fleet-telematics` `device-management` `edge-computing` `iot-application` `modbus` `ota-update` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2016-02-03 |
| 📦 **Latest release** | [1.35.0](https://github.com/openremote/core/releases/tag/1.35.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 304.9 MB |
| 🌐 **Website** | https://openremote.io |

## 📦 Recent releases

### [1.35.0](https://github.com/openremote/core/releases/tag/1.35.0)
<sub>2026-11-24 · 3d ago</sub>

> > [!IMPORTANT]
> > We have addressed the CVE-2026-114938 Java4Shell vulnerability in this latest Docker image, with an OpenJDK upgrade in #3592.
> > Unless manually resolved, it's recommended to upgrade OpenRemote to this version, to prevent misuse of an exploit.
> **⚠️ Important notes / Before you upgrade ⚠️**
> - **`sendAttributeEvent` now fails fast when event processing is unavailable** ([#3593](https://github.com/openremote/core/pull/3593)).
>   `AssetProcessingService.sendAttributeEvent(...)` throws `AttributeEventProcessorUnavailableException` (an `IllegalStateException`) on the calling thread if Camel or the attribute-processing route is unavailable; previously the event was silently dropped. Move startup attribute writes from `ContainerService.start()` to `startProducers()`, and handle the exception at submission in tasks that must keep running across a route outage.
> …

### [1.34.1](https://github.com/openremote/core/releases/tag/1.34.1)
<sub>2026-11-17 · 10d ago</sub>

> **What's Changed**
> **🐞 Bug fixes**
> * Fix blank page when a startup request fails by @Ekhorn in https://github.com/openremote/core/pull/3549
> * Fix event subscriptions stopping after a reconnect by @Ekhorn in https://github.com/openremote/core/pull/3548
> **Other changes**
> * Bump the vaadin group with 24 updates by @dependabot[bot] in https://github.com/openremote/core/pull/3555
> …

### [1.34.0](https://github.com/openremote/core/releases/tag/1.34.0)
<sub>2026-11-06 · 21d ago</sub>

> > [!NOTE]
> > We have also recently published a new `openremote/keycloak` release, version `26.7.5.0`, that introduces a new UI design!
> > It now automatically applies your custom realm styling and images, alongside many stability improvements.
> > You can view the releases [here](https://github.com/openremote/keycloak/releases).
> **⚠️ Important notes / Before you upgrade ⚠️**
> - **MQTT X.509 auto-provisioning now requires proof of the private key** ([ef497cc](https://github.com/openremote/core/commit/ef497cc)).
> …

### [1.33.0](https://github.com/openremote/core/releases/tag/1.33.0)
<sub>2026-10-27 · 1mo ago</sub>

> **⚠️  Important notes / Before you upgrade ⚠️**
> - **Minor behavior changes in datapoint query requests.**
> We've introduced bugfixes for querying datapoints with `NULL` values in #3447, so the behavior has altered slightly.
> Be aware that graphs, data exports, and every other system that makes use of datapoints might be affected.
> However, **no database migration or rewrite of stored datapoints is required.**
>   * With gap filling enabled, `DIFFERENCE` now returns an unavailable delta for the first available reading after a leading empty bucket, rather than returning that reading's absolute value. Charts may show a gap where they previously showed an artificial spike.
> …

### [1.32.2](https://github.com/openremote/core/releases/tag/1.32.2)
<sub>2026-10-21 · 1mo ago</sub>

> **What's Changed**
> **🔒 Security updates**
> * CVE-2026-124436 on Improper Authorization Allows Realm Administrators to Access and Modify Global Resources
> * CVE-2026-124435 on Stored Cross-Site Scripting via Unrestricted Manager Configuration Image Upload
> **⭐ Enhancements**
> * Add manager URL to Keycloak container by @Ekhorn in https://github.com/openremote/core/pull/3412
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [Bugfix for dashboards in the database being altered on every GET requ…](https://github.com/openremote/core/commit/1f5c93ed04d955a71043ccaa4873033207d6da94) | MartinaeyNL |
| 2026-11-27 | [Refresh pages when switching back to a visited realm (#3591)](https://github.com/openremote/core/commit/017178708c6208ad4d75c4fb600095c732221235) | Ekhorn |
| 2026-11-27 | [Share the push user query and drop the unused FCM token blacklist (#3…](https://github.com/openremote/core/commit/9dca27aae208fa5f3d945c39c85be4861f0d858b) | Ekhorn |
| 2026-11-27 | [Reject MQTT authentication on a closed transport (#3608)](https://github.com/openremote/core/commit/98973aeda904c1f226ee9c2f482dc2c3d626687b) | ebariaux |
| 2026-11-26 | [Fix GatewayAttributeFilter equality check for JPA dirty checking (#3624)](https://github.com/openremote/core/commit/ae3975b4b80fd9855c01f2ba1a30c3e4069714e0) | ebariaux |
| 2026-11-26 | [Document downstream compatibility and standardize PR labeling (#3623)](https://github.com/openremote/core/commit/0059156561754a54877f3d90b06653bfc64bdcc6) | wborn |
| 2026-11-26 | [Show sortable gateway asset links in the tunnels table (#3618)](https://github.com/openremote/core/commit/02f04a17a2ffd7648633a63dd63b004ef084c344) | wborn |
| 2026-11-24 | [Update `AGENTS.md` to prevent AI accreditation on commits (#3615)](https://github.com/openremote/core/commit/3617eba26f8553c50de2a25757825e307e9804ad) | denniskuijs |
| 2026-11-24 | [Improve startup sequence to avoid starvation on event processing (#3593)](https://github.com/openremote/core/commit/c748e4f6eb76e5cb9e9a96cd5a8bdca8dc244649) | ebariaux |
| 2026-11-24 | [Assert the value descriptor schema hash in AssetModelTest (#3586)](https://github.com/openremote/core/commit/028bff97be5493274d4d2eb66ef9dae272d4f3b1) | costajohnt |

[See all commits ↗](https://github.com/openremote/core/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openremote/core.git
```
