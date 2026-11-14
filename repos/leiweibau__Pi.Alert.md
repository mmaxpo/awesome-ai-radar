# leiweibau/Pi.Alert

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/leiweibau/Pi.Alert)

> Scan the devices connected to your WIFI / LAN and alert you the connection of unknown devices. It also warns if a "always connected" device disconnects. In addition, it is possible to check web services for availability. For this purpose HTTP status codes and the response time of the service are evaluated.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Scans your Wi-Fi/LAN and alerts on new devices |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.3k |
| 🍴 **Forks** | 109 |
| 🐞 **Open issues + PRs** | [2](https://github.com/leiweibau/Pi.Alert/issues) |
| 💻 **Languages** | PHP 66% · Python 17% · JavaScript 7% · CSS 6% · Shell 4% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `arp-scan` `security` `self-hosted` `pi-hole` `pialert` `network-security` |
| 🕒 **Last activity** | 2026-10-16 (29d ago) |
| 📅 **Created** | 2022-05-20 |
| 📦 **Latest release** | [v2026-10-16](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-10-16) — 2026-10-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1086.4 MB |
| 🌐 **Website** | https://leiweibau.net |

## 📦 Recent releases

### [v2026-10-16](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-10-16) — Pi.Alert v2026-10-16
<sub>2026-10-16 · 29d ago</sub>

> New:
> * Merge function for multi-MAC devices (#547)
> Fixed:
> * UpdateCheck did not work immediately after logging in (thx to @lastsamurai26 for reporting)
> * Satellite information is not available on the System Info page immediately after logging in (thx to @lastsamurai26 for reporting)
> * OPNsense import crashes when one MAC has active Kea leases on multiple subnets (#645)
> …

### [v2026-10-01](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-10-01) — Pi.Alert v2026-10-01
<sub>2026-10-01 · 1mo ago</sub>

> New:
> * Forward/back navigation on Device and ICMP detail pages.
> * Automatic cleanup of update logs (the last 5 are retained) at the end of a successful update
> * Up to three custom URL actions can be configured for both devices and ICMP hosts. Each action supports a custom label, an icon from the locally bundled icon libraries, as well as configurable button and text colors.
> * Redesigned bulk editors with status colors, event gradients, and MQTT and presence indicators.
> * Centralized UI configuration in a dedicated file instead of individual settings or database entries.
> …

### [v2026-09-01](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-09-01) — Pi.Alert v2026-09-01
<sub>2026-09-03 · 2mo ago</sub>

> New:
> * If both "REPORT_TO_MQTT = True" and "PUBLISH_MQTT_SUBNET_STATUS = True" are set, Pi. Alert identifies the IPv4 subnets directly available on the local network interfaces, assigns the hosts managed in "Devices" and "ICMP_Mon" to exactly one of these subnets based on their IP addresses, and publishes nine counters per subnet. (https://github.com/leiweibau/Pi.Alert/issues/621)
> Fixed:
> * Add "--vlan=" to valid parameter for SCAN_SUBNETS (https://github.com/leiweibau/Pi.Alert/issues/617)
> * Parser correction for "PUSHOVER_PRIO" so that negative values are once again possible. (https://github.com/leiweibau/Pi.Alert/issues/633)
> * The OpenWrt integration is designed to use HTTPS by default for new installations and to continue working with the self-signed certificates typically used with OpenWrt. To this end, the Boolean configuration value "OPENWRT_SSL" and the integer configuration value "OPENWRT_PORT" are introduced. (https://github.com/leiweibau/Pi.Alert/issues/632)
> …

### [v2026-08-14](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-08-14) — Pi.Alert v2026-08-14
<sub>2026-08-14 · 3mo ago</sub>

> New:
> * Add "Copy to Clipboard" buttons to MAC and IP on the details page
> Fixed:
> * Bug where the download page for UI Settings operated outside the user's session (thx to @Soham-Bhalerao)
> * IPs should now be displayed again on the System Info Page, if they were not previously
> * Security Advisory (https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-66mg-wpcq-2phq) (thx to @tunelko)
> …

### [v2026-05-07](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-05-07) — Pi.Alert v2026-05-07
<sub>2026-05-07 · 6mo ago</sub>

> New:
> * Support for AdGuard Home (#516 ). Detecting active hosts using only AdGuard Home is difficult, as AdGuard Home provides very little information about the hosts it manages via the API. Pi.Alert attempts to detect active hosts itself based on the most recent DNS queries (default = 1000). Hosts that do not make regular DNS requests are therefore quickly identified as inactive, so this detection method is somewhat less accurate.
> * Support for Opnsense (#542)
> * Prepare AdGuard Home and OPNsense support for Pi.Alert-Satellite
> Fixed:
> * Security Advisory (https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-m929-j7w8-334j) (thx to @JarrodCameron)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-16 | [Merge pull request #647 from leiweibau/next_update](https://github.com/leiweibau/Pi.Alert/commit/850e40a90871816161559e136e703cf68c1c994a) | leiweibau |
| 2026-10-16 | [Update Notes: 2026-10-16](https://github.com/leiweibau/Pi.Alert/commit/4e902fe8c8187be7cf78bd177367d67201da3d45) | leiweibau |
| 2026-10-15 | [UI Tweaks](https://github.com/leiweibau/Pi.Alert/commit/8079e7ba5aed5db088ba28312cc863533a547e0c) | leiweibau |
| 2026-10-14 | [Update Notes: 2026-10-15](https://github.com/leiweibau/Pi.Alert/commit/b397253b24c17be18f1de8ffcaa9493bde6d90c2) | leiweibau |
| 2026-10-14 | [CPU Info](https://github.com/leiweibau/Pi.Alert/commit/d7649b916a71834262459313cfed3bb2551f7219) | leiweibau |
| 2026-10-14 | [Update Notes: 2026-10-15](https://github.com/leiweibau/Pi.Alert/commit/24ab9eaeead01111ced9d1275a8ba6e3b9a68589) | leiweibau |
| 2026-10-14 | [Update AdminLTE from 4.9.1 to 4.10.1 +UI Tweaks + Maintenance](https://github.com/leiweibau/Pi.Alert/commit/90640a03ccc8e47de4c2d13b5c3fe651ef184bc6) | leiweibau |
| 2026-10-13 | [Update Notes: 2026-10-15](https://github.com/leiweibau/Pi.Alert/commit/2eae39e12f4e90447955558a0bd744a6ac10f55a) | leiweibau |
| 2026-10-13 | [Fixed dropdown lists in device mapping for the Glass, Piano, and Cons…](https://github.com/leiweibau/Pi.Alert/commit/809904b072d3bf13746d40bdcae56184a3d7d759) | leiweibau |
| 2026-10-12 | [Update Notes: 2026-10-15](https://github.com/leiweibau/Pi.Alert/commit/907863963414c264c968b24a2ffe0ca49bb1ea68) | leiweibau |

[See all commits ↗](https://github.com/leiweibau/Pi.Alert/commits)

## ⬇️ Get it

```bash
git clone https://github.com/leiweibau/Pi.Alert.git
```
