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
| ⭐ **Stars** | 2.1k |
| 🍴 **Forks** | 523 |
| 🐞 **Open issues + PRs** | [490](https://github.com/openremote/core/issues) |
| 💻 **Languages** | Java 49% · TypeScript 25% · Groovy 19% · Shell 5% |
| 📜 **License** | Other |
| 🏷 **Topics** | `iot-platform` `iot` `energy` `building` `mqtt` `smartcity` `dashboard` `asset-management` `mqtt-broker` `dataplatform` `rules-engine` `fleet-management` `energy-monitor` `energy-management` `fleet-telematics` `device-management` `edge-computing` `iot-application` `modbus` `ota-update` |
| 🕒 **Last activity** | 2026-11-13 (yesterday) |
| 📅 **Created** | 2016-02-03 |
| 📦 **Latest release** | [1.34.0](https://github.com/openremote/core/releases/tag/1.34.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 304.1 MB |
| 🌐 **Website** | https://openremote.io |

## 📦 Recent releases

### [1.34.0](https://github.com/openremote/core/releases/tag/1.34.0)
<sub>2026-11-06 · 8d ago</sub>

> > [!NOTE]
> > We have also recently published a new `openremote/keycloak` release, version `26.7.5.0`, that introduces a new UI design!
> > It now automatically applies your custom realm styling and images, alongside many stability improvements.
> > You can view the releases [here](https://github.com/openremote/keycloak/releases).
> **⚠️ Important notes / Before you upgrade ⚠️**
> - **MQTT X.509 auto-provisioning now requires proof of the private key** ([ef497cc](https://github.com/openremote/core/commit/ef497cc)).
> …

### [1.33.0](https://github.com/openremote/core/releases/tag/1.33.0)
<sub>2026-10-27 · 18d ago</sub>

> **⚠️  Important notes / Before you upgrade ⚠️**
> - **Minor behavior changes in datapoint query requests.**
> We've introduced bugfixes for querying datapoints with `NULL` values in #3447, so the behavior has altered slightly.
> Be aware that graphs, data exports, and every other system that makes use of datapoints might be affected.
> However, **no database migration or rewrite of stored datapoints is required.**
>   * With gap filling enabled, `DIFFERENCE` now returns an unavailable delta for the first available reading after a leading empty bucket, rather than returning that reading's absolute value. Charts may show a gap where they previously showed an artificial spike.
> …

### [1.32.2](https://github.com/openremote/core/releases/tag/1.32.2)
<sub>2026-10-21 · 24d ago</sub>

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

### [1.32.0](https://github.com/openremote/core/releases/tag/1.32.0)
<sub>2026-10-12 · 1mo ago</sub>

> > [!NOTE]
> > **As of October 13th, the repository has been renamed from `openremote/openremote` to `openremote/core`.**
> > **We have also renamed the `master` branch to `main`, following the latest standards.**
> > If you maintain a custom project that uses these references, we recommend updating them to prevent issues.
> > All package distributions of OpenRemote (Docker, etc) have not been changed, and are unaffected.
> **⚠️  Important notes / Before you upgrade ⚠️**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [Remove Balena files (#3570)](https://github.com/openremote/core/commit/c7652131fe2b36f7b4341a0d8a20a94fc8107667) | denniskuijs |
| 2026-11-11 | [Migrate JSONSchemaUtil snapshot tests to spock snapshot (#3220)](https://github.com/openremote/core/commit/1ee1ed7db8d09d45b8865a3e85eb5fa2be4604f1) | Ekhorn |
| 2026-11-10 | [Bump actions/setup-java from 6.1.0 to 6.2.0 in /.github/actions/get-v…](https://github.com/openremote/core/commit/14f389eae677421400084d1589cd548c3cb66ca4) | dependabot[bot] |
| 2026-11-10 | [Align Gradle root project name with repository (#3559)](https://github.com/openremote/core/commit/a239f2988ebb010b5fb9806f249216a5b4ae2982) | wborn |
| 2026-11-10 | [Stabilize gateway rejection assertions in GatewayTest (#3507)](https://github.com/openremote/core/commit/1d6246374dd0c01d6c2486afebf6db10745e1bdf) | wborn |
| 2026-11-10 | [Bump github/codeql-action/upload-sarif from 4.39.2 to 4.39.3 (#3562)](https://github.com/openremote/core/commit/8e7e753cc50934d05156dcd53d518ed1d4ae4b02) | dependabot[bot] |
| 2026-11-10 | [Bump docker/login-action from 4.7.0 to 4.8.0 (#3561)](https://github.com/openremote/core/commit/7782c7ae67b38a2e48aba5e43efdd045e8e3f1d7) | dependabot[bot] |
| 2026-11-10 | [Bump actions/setup-java from 6.1.0 to 6.2.0 (#3560)](https://github.com/openremote/core/commit/214a5cc579410a3b80493cfdfda4f7db24628481) | dependabot[bot] |
| 2026-11-09 | [Bump github/codeql-action/upload-sarif from 4.39.1 to 4.39.2 (#3550)](https://github.com/openremote/core/commit/718469671337aa028005cb63278a1cca0e49717b) | dependabot[bot] |
| 2026-11-09 | [Bump tspascoal/get-user-teams-membership from 4.0.2 to 4.0.3 (#3551)](https://github.com/openremote/core/commit/676a198d0c3161ba9238544d672f5f3b4a7e45f9) | dependabot[bot] |

[See all commits ↗](https://github.com/openremote/core/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openremote/core.git
```
