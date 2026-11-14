# dmunozv04/iSponsorBlockTV

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/dmunozv04/iSponsorBlockTV)

> SponsorBlock client for all YouTube for TV clients.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | SponsorBlock (skip sponsor segments) on TV YouTube apps |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 7.2k |
| 🍴 **Forks** | 314 |
| 🐞 **Open issues + PRs** | [79](https://github.com/dmunozv04/iSponsorBlockTV/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | GPL-3.0 |
| 🏷 **Topics** | `python` `appletv` `youtube` `sponsorblock` `chromecast` `roku` `tizen-tv` `androidtv` `samsungtv` |
| 🕒 **Last activity** | 2026-11-10 (3d ago) |
| 📅 **Created** | 2022-01-15 |
| 📦 **Latest release** | [v2.11.0](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.11.0) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 0.7 MB |

## 📦 Recent releases

### [v2.11.0](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.11.0) — v2.11.0: fixing a blind SSRF on DIAL auto discovery
<sub>2026-08-21 · 2mo ago</sub>

> **Fixed blind SSRF on DIAL auto discovery**
> Fixes advisory: [GHSA-56v3-jrq2-4q9m](https://github.com/dmunozv04/iSponsorBlockTV/security/advisories/GHSA-56v3-jrq2-4q9m) / [CVE-2026-77597](https://www.cve.org/CVERecord?id=CVE-2026-77597)
> It's recommended for all users to update to this latest version (v2.11.0)
> This issue could allow an attacker controlled device on the same lan as iSponsorBlockTV to request an arbitrary URL by abusing the DIAL auto-discovery. It'd be able to either:
> - show a debug log  line `- __main__ - DEBUG - Discovered device at <attacker controlled URL>, processing...` (which is normally disabled and won't be shown in the actual configurator since textual doesn't show logs unless running in dev mode and launching a second terminal to inspect log output), and make a single GET request to an "attacker controlled" url which does not leak any information back to iSponsorBlockTV itself and swallows any sort of error (parsing or an invalid response from not being a real DIAL server) (`dial_client.py` L131-L133)
> - make single POST request to a partly "attacker controlled" url since it'll always have the suffix `/YouTube` appended (`dial_client.py` L139) , with predefined headers `{"Origin": "https://www.youtube.com","Content-Type": "application/x-www-form-urlencoded",}` (`dial_client.py` L158-L161) and a predefined payload `{"pairingCode": <random 12 digit code>, "theme": "cl"}` which also does not leak any information back to iSponsorBlockTV itself and swallows any sort of error (parsing or an invalid response from not being a real DIAL server with a YouTube app running on it) (`dial_client.py` L162).
> …

### [v2.10.0](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.10.0) — v2.10.0: Alternative SponsorBlock API URLs supported
<sub>2026-07-13 · 4mo ago</sub>

> **What's Changed**
> * Reuse per-instance web_session and api_helper by @dmunozv04 in https://github.com/dmunozv04/iSponsorBlockTV/pull/466
> * Fix cli configurator on python3.14 by @dmunozv04 in https://github.com/dmunozv04/iSponsorBlockTV/pull/473
> * Remove poi_highlight from configurators by @colord in https://github.com/dmunozv04/iSponsorBlockTV/pull/464
> * Add 'Hook' category; and clarify 'Preview' label by @jicetus in https://github.com/dmunozv04/iSponsorBlockTV/pull/467
> * Port PyytLounge to v3.2.0 by @sternma in https://github.com/dmunozv04/iSponsorBlockTV/pull/399
> …

### [v2.9.0](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.9.0) — V2.9.0: Pairing improved
<sub>2026-05-09 · 6mo ago</sub>

> This release improves auto discovery pairing, making it work with more devices and adds chrome cast discovery (for older chrome casts that don't support the regular auto pairing protocol).
> **What's Changed**
> * Improve pairing by @dmunozv04 in https://github.com/dmunozv04/iSponsorBlockTV/pull/438
> * Bump rich from 14.3.4 to 15.0.0 by @dependabot[bot] in https://github.com/dmunozv04/iSponsorBlockTV/pull/447
> * Bump textual from 8.2.3 to 8.2.5 by @dependabot[bot] in https://github.com/dmunozv04/iSponsorBlockTV/pull/456
> **Full Changelog**: https://github.com/dmunozv04/iSponsorBlockTV/compare/v2.8.1...v2.9.0

### [v2.8.1](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.8.1) — v2.8.1: WARNING: YouTube is revoking old screen IDs, your device might have stop…
<sub>2026-05-01 · 6mo ago</sub>

> **Warning**
> YouTube has changed the screen ID format from 26 characters to 64 hex digits. Since the 15th April 2026 YouTube apps have started generating new IDs and revoking the old ones, breaking a paired iSponsorBlockTV.
> The solution is simple, pairing the device again will (most likely) fix this.
> Read more info on #450 and https://github.com/dmunozv04/iSponsorBlockTV/wiki/new-screen-ID-format
> **What's Changed**
> * Bump aiohttp from 3.12.15 to 3.13.5 by @dependabot[bot] in https://github.com/dmunozv04/iSponsorBlockTV/pull/440
> …

### [v2.8.0](https://github.com/dmunozv04/iSponsorBlockTV/releases/tag/v2.8.0) — v2.8.0: WARNING: YouTube is revoking old screen IDs, your device might have stop…
<sub>2026-05-01 · 6mo ago</sub>

> **Warning**
> YouTube has changed the screen ID format from 26 characters to 64 hex digits. Since the 15th April 2026 YouTube apps have started generating new IDs and revoking the old ones, breaking a paired iSponsorBlockTV.
> The solution is simple, pairing the device again will (most likely) fix this.
> Read more info on #450 and https://github.com/dmunozv04/iSponsorBlockTV/wiki/new-screen-ID-format
> **What's Changed**
> * Bump aiohttp from 3.12.15 to 3.13.5 by @dependabot[bot] in https://github.com/dmunozv04/iSponsorBlockTV/pull/440
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-08 | [Merge pull request #509 from katsugtgz/deps/aiohttp-3.14.4](https://github.com/dmunozv04/iSponsorBlockTV/commit/6a73a2d9e590f0cc7684036ca8fbf26812ceca0a) | dmunozv04 |
| 2026-11-08 | [Bump aiohttp from 3.14.3 to 3.14.4](https://github.com/dmunozv04/iSponsorBlockTV/commit/966e4f0558bf629556d235d933036075fc92d3bc) | katsugtgz |
| 2026-11-08 | [Merge pull request #513 from ChiefD425/fix-dial-mx](https://github.com/dmunozv04/iSponsorBlockTV/commit/fe14d372e9953237a75fac19f3a22507e1c332dc) | dmunozv04 |
| 2026-11-08 | [Lower DIAL M-SEARCH MX so replies arrive inside the listen window](https://github.com/dmunozv04/iSponsorBlockTV/commit/c64c7968c4e76c83e7568f04e0276aa54bc18186) | ChiefD425 |
| 2026-11-08 | [Merge pull request #518 from dmunozv04/ad-skipped-event-1082](https://github.com/dmunozv04/iSponsorBlockTV/commit/fe8e6b383e92bb3f04b54bb82dd35fa2193db6fa) | dmunozv04 |
| 2026-11-08 | [Fix ad state check to use set for adState comparison](https://github.com/dmunozv04/iSponsorBlockTV/commit/be2648d01cca147da1c3cc03202c2e6444472ada) | dmunozv04 |
| 2026-11-08 | [[pre-commit.ci] auto fixes from pre-commit.com hooks](https://github.com/dmunozv04/iSponsorBlockTV/commit/764b67e2d7256bcca8fb1b50ed9d4d6d33d7c4f6) | pre-commit-ci[bot] |
| 2026-11-08 | [Handle Ad skipped event](https://github.com/dmunozv04/iSponsorBlockTV/commit/e22ebd9e78342db586b27bd8ab68f371e7b87ec8) | dmunozv04 |
| 2026-11-08 | [Merge pull request #494 from dmunozv04/dependabot/pip/pyytlounge-3.4.0](https://github.com/dmunozv04/iSponsorBlockTV/commit/1944db09e5fbf4954f002ced98d94f66171d26f5) | dmunozv04 |
| 2026-11-08 | [Add custom device_id](https://github.com/dmunozv04/iSponsorBlockTV/commit/76626e0e3a6603040542f2584cdb7b067d51cb4a) | dmunozv04 |

[See all commits ↗](https://github.com/dmunozv04/iSponsorBlockTV/commits)

## ⬇️ Get it

```bash
git clone https://github.com/dmunozv04/iSponsorBlockTV.git
```
