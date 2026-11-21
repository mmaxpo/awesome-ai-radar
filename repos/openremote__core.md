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
| 🍴 **Forks** | 528 |
| 🐞 **Open issues + PRs** | [506](https://github.com/openremote/core/issues) |
| 💻 **Languages** | Java 48% · TypeScript 26% · Groovy 19% · Shell 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `iot-platform` `iot` `energy` `building` `mqtt` `smartcity` `dashboard` `asset-management` `mqtt-broker` `dataplatform` `rules-engine` `fleet-management` `energy-monitor` `energy-management` `fleet-telematics` `device-management` `edge-computing` `iot-application` `modbus` `ota-update` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2016-02-03 |
| 📦 **Latest release** | [1.34.1](https://github.com/openremote/core/releases/tag/1.34.1) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 304.2 MB |
| 🌐 **Website** | https://openremote.io |

## 📦 Recent releases

### [1.34.1](https://github.com/openremote/core/releases/tag/1.34.1)
<sub>2026-11-17 · 4d ago</sub>

> **What's Changed**
> **🐞 Bug fixes**
> * Fix blank page when a startup request fails by @Ekhorn in https://github.com/openremote/core/pull/3549
> * Fix event subscriptions stopping after a reconnect by @Ekhorn in https://github.com/openremote/core/pull/3548
> **Other changes**
> * Bump the vaadin group with 24 updates by @dependabot[bot] in https://github.com/openremote/core/pull/3555
> …

### [1.34.0](https://github.com/openremote/core/releases/tag/1.34.0)
<sub>2026-11-06 · 15d ago</sub>

> > [!NOTE]
> > We have also recently published a new `openremote/keycloak` release, version `26.7.5.0`, that introduces a new UI design!
> > It now automatically applies your custom realm styling and images, alongside many stability improvements.
> > You can view the releases [here](https://github.com/openremote/keycloak/releases).
> **⚠️ Important notes / Before you upgrade ⚠️**
> - **MQTT X.509 auto-provisioning now requires proof of the private key** ([ef497cc](https://github.com/openremote/core/commit/ef497cc)).
> …

### [1.33.0](https://github.com/openremote/core/releases/tag/1.33.0)
<sub>2026-10-27 · 25d ago</sub>

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
| 2026-11-20 | [CI/CD: Add container memory, OOM kill and restart alarms and reduce n…](https://github.com/openremote/core/commit/973c86ee2e53a9c09fbbd00114dacb4563a87880) | richturner |
| 2026-11-20 | [Bump artemis from 2.55.0 to 2.57.0 (#3529)](https://github.com/openremote/core/commit/68ec88625c1a5f463a7360158e575257de088051) | dependabot[bot] |
| 2026-11-20 | [Bump ubi10/openjdk-21-runtime in /manager (#3597)](https://github.com/openremote/core/commit/fd65895a350753e7a162d9965c925d463f8b35dc) | dependabot[bot] |
| 2026-11-19 | [Add configuration template import and export (#3380)](https://github.com/openremote/core/commit/9cab6cac24a30cc0a257f150bb46c1f24e0114d4) | Ekhorn |
| 2026-11-19 | [Upgrade OpenJDK in manager image for CVE-2026-114938 (#3592)](https://github.com/openremote/core/commit/ddf84ad507bebadac6be4c8721adcbcf85e112eb) | Ekhorn |
| 2026-11-19 | [Bump actions/setup-java from 6.2.0 to 6.3.0 in /.github/actions/get-v…](https://github.com/openremote/core/commit/e8fdef3c4e2e7ac6790ac75a17f3ccb1d1c5f28d) | dependabot[bot] |
| 2026-11-19 | [Bump actions/setup-java from 6.2.0 to 6.3.0 (#3584)](https://github.com/openremote/core/commit/8187046cb5b8558131ef823632520e05a98cd3cc) | dependabot[bot] |
| 2026-11-17 | [Fix event subscriptions stopping after a reconnect (#3548)](https://github.com/openremote/core/commit/1b72bf4db4c9d73f5f9680b5d9836a5850bfbe23) | Ekhorn |
| 2026-11-17 | [Pin browser test jobs to Ubuntu 24.04 (#3581)](https://github.com/openremote/core/commit/f74263478375d8cc4627bceffb59175e5a2c3f30) | Ekhorn |
| 2026-11-16 | [Bump ubi10/openjdk-21-runtime in /manager (#3572)](https://github.com/openremote/core/commit/6d46b473d353533ccfc3938956eed145a134f2d8) | dependabot[bot] |

[See all commits ↗](https://github.com/openremote/core/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openremote/core.git
```
