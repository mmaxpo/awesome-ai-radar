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
| 🍴 **Forks** | 530 |
| 🐞 **Open issues + PRs** | [498](https://github.com/openremote/core/issues) |
| 💻 **Languages** | Java 48% · TypeScript 26% · Groovy 19% · Shell 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `iot-platform` `iot` `energy` `building` `mqtt` `smartcity` `dashboard` `asset-management` `mqtt-broker` `dataplatform` `rules-engine` `fleet-management` `energy-monitor` `energy-management` `fleet-telematics` `device-management` `edge-computing` `iot-application` `modbus` `ota-update` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2016-02-03 |
| 📦 **Latest release** | [1.34.1](https://github.com/openremote/core/releases/tag/1.34.1) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 304.4 MB |
| 🌐 **Website** | https://openremote.io |

## 📦 Recent releases

### [1.34.1](https://github.com/openremote/core/releases/tag/1.34.1)
<sub>2026-11-17 · 6d ago</sub>

> **What's Changed**
> **🐞 Bug fixes**
> * Fix blank page when a startup request fails by @Ekhorn in https://github.com/openremote/core/pull/3549
> * Fix event subscriptions stopping after a reconnect by @Ekhorn in https://github.com/openremote/core/pull/3548
> **Other changes**
> * Bump the vaadin group with 24 updates by @dependabot[bot] in https://github.com/openremote/core/pull/3555
> …

### [1.34.0](https://github.com/openremote/core/releases/tag/1.34.0)
<sub>2026-11-06 · 17d ago</sub>

> > [!NOTE]
> > We have also recently published a new `openremote/keycloak` release, version `26.7.5.0`, that introduces a new UI design!
> > It now automatically applies your custom realm styling and images, alongside many stability improvements.
> > You can view the releases [here](https://github.com/openremote/keycloak/releases).
> **⚠️ Important notes / Before you upgrade ⚠️**
> - **MQTT X.509 auto-provisioning now requires proof of the private key** ([ef497cc](https://github.com/openremote/core/commit/ef497cc)).
> …

### [1.33.0](https://github.com/openremote/core/releases/tag/1.33.0)
<sub>2026-10-27 · 27d ago</sub>

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
> * [CVE pending](https://github.com/openremote/core/security/advisories/GHSA-gf33-2772-8gw3) on Improper Authorization Allows Realm Administrators to Access and Modify Global Resources
> * [CVE pending](https://github.com/openremote/core/security/advisories/GHSA-vgp4-96p8-3w8v) on Stored Cross-Site Scripting via Unrestricted Manager Configuration Image Upload
> **⭐ Enhancements**
> * Add manager URL to Keycloak container by @Ekhorn in https://github.com/openremote/core/pull/3412
> …

### [1.32.1](https://github.com/openremote/core/releases/tag/1.32.1)
<sub>2026-10-14 · 1mo ago</sub>

> > [!NOTE]
> > **As of October 13th, the repository has been renamed from `openremote/openremote` to `openremote/core`.**
> > **We have also renamed the `master` branch to `main`, following the latest standards.**
> > If you maintain a custom project that uses these references, we recommend updating them to prevent issues.
> > All package distributions of OpenRemote (Docker, etc) have not been changed, and are unaffected.
> **What's Changed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Clean up state left by backend specs and fix UI test role lookup (#3594)](https://github.com/openremote/core/commit/39a171a2338070449200df77105514af23183e50) | Ekhorn |
| 2026-11-23 | [Misc kubernetes related updates (#3606)](https://github.com/openremote/core/commit/8bfb786bbfac0e5cb3d414b05ba66600c27e2b06) | ebariaux |
| 2026-11-23 | [On idle remove duplicate cluster marker after zooming (#3598)](https://github.com/openremote/core/commit/a5bf13f15e4ef1b43c0ed64fc33266a227b60d3a) | Ekhorn |
| 2026-11-23 | [Fall back to the previous version of the create-ec2 CFT template (#3609)](https://github.com/openremote/core/commit/21cb91ef09c3d30cccd91f34547490b8994d4cb1) | denniskuijs |
| 2026-11-23 | [Make Grype output both sarif/table formats at once (#3595)](https://github.com/openremote/core/commit/51c8079834652e917bb6e5f0b576f0a45d4299f5) | Ekhorn |
| 2026-11-23 | [Use US English in text, preserving public APIs (#3571)](https://github.com/openremote/core/commit/de24b446bf37c76364c740d3ae5dd9b4d17b47cc) | wborn |
| 2026-11-23 | [Bump com.icegreen:greenmail from 2.1.9 to 2.1.15 (#3528)](https://github.com/openremote/core/commit/ab398eb038ca023249be125a4b05e58ec898243a) | dependabot[bot] |
| 2026-11-23 | [Set PostgreSQL idle in transaction session timeout in deploy profile …](https://github.com/openremote/core/commit/987f7655af006e12c1a6728758744dc51eec542b) | richturner |
| 2026-11-23 | [Reduce query-exporter false positives and add asset table size metric…](https://github.com/openremote/core/commit/083427b7f98685695ac8b4fa20fc14f4a0f4903a) | richturner |
| 2026-11-23 | [Add MQTT connection status to load2 fixtures (#3602)](https://github.com/openremote/core/commit/6d3a1a200eaea3509ec7d9f72818f43cb059a4ff) | ebariaux |

[See all commits ↗](https://github.com/openremote/core/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openremote/core.git
```
