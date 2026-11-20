# fosrl/pangolin

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/fosrl/pangolin)

> Modern networking and security platform providing secure access and connectivity to apps, infrastructure, and AI workloads. Connect and protect your users.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Self-hosted zero-trust VPN and reverse proxy (WireGuard) |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 23.9k |
| 🍴 **Forks** | 851 |
| 🐞 **Open issues + PRs** | [135](https://github.com/fosrl/pangolin/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `reverse-proxy` `wireguard` `single-sign-on` `self-hosted` `oidc` `vpn` `zero-trust` `zero-trust-network-access` `ztna` `pam` `remote-access` `ssh` `tunneling` `nat-traversal` `sase` `sso` `wireguard-vpn` `pangolin` `ai-gateway` `gateway` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2024-09-27 |
| 📦 **Latest release** | [1.27.0](https://github.com/fosrl/pangolin/releases/tag/1.27.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 98.9 MB |
| 🌐 **Website** | https://pangolin.net |

## 📦 Recent releases

### [1.27.0](https://github.com/fosrl/pangolin/releases/tag/1.27.0)
<sub>2026-11-19 · today</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.27: Managed Client Settings, Per-Org Client Settings](https://pangolin.net/news/1-27-release)
> **What’s Changed**
> - Add ability to enforce client (user device) settings on a per-role basis (EE)
> - Add support for selecting labels for alert rules
> - Add custom css to branding
> …

### [1.27.0-rc.0](https://github.com/fosrl/pangolin/releases/tag/1.27.0-rc.0) _(pre-release)_
<sub>2026-11-18 · yesterday</sub>

> **RC**
> A Release Candidate (RC) is a near-final software version, stable but undergoing last tests before official release. It has all features and no known bugs.
> * Users: Use cautiously due to potential undiscovered bugs. Not for critical systems unless prepared for issues. Report bugs.
> * Developers/Testers: Perform crucial final validation and thorough testing, especially of recent changes, to catch last-minute major issues.
> * Backup: Always back up data before installing an RC to allow rollback if problems arise.
> * Feedback: Provide feedback; it's vital for a robust final release.
> …

### [1.26.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0)
<sub>2026-11-04 · 15d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.26: Session Management, SSH Logs, and Auto Windows Updates](https://pangolin.net/news/1-26-release)
> **What’s Changed**
> * Add option to add additional DNS records on delegated domains with Pangolin DNS (EE)
> * Add optional match on base wildcard domains
> * Add continuous session revalidation for OIDC IdPs using refresh tokens (EE)
> …

### [1.26.0-rc.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0-rc.0) _(pre-release)_
<sub>2026-11-02 · 17d ago</sub>

> **RC**
> A Release Candidate (RC) is a near-final software version, stable but undergoing last tests before official release. It has all features and no known bugs.
> * Users: Use cautiously due to potential undiscovered bugs. Not for critical systems unless prepared for issues. Report bugs.
> * Developers/Testers: Perform crucial final validation and thorough testing, especially of recent changes, to catch last-minute major issues.
> * Backup: Always back up data before installing an RC to allow rollback if problems arise.
> * Feedback: Provide feedback; it's vital for a robust final release.
> …

### [1.25.3](https://github.com/fosrl/pangolin/releases/tag/1.25.3)
<sub>2026-10-23 · 27d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.25: Redirects, mTLS, and Machine Roles](https://pangolin.net/news/1-25-release)
> **What's Changed**
> * Update node to resolve Node2Shell CVE-2026-111497
> * Improve client connection speed with many sites
> * Fix agent and olm version separate in the database
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Merge pull request #4156 from fosrl/dev](https://github.com/fosrl/pangolin/commit/c845d95cfaee26ebee334d29d32b9a679b3b1dbb) | oschwartz10612 |
| 2026-11-19 | [Fix client settings tier](https://github.com/fosrl/pangolin/commit/a0853531aab64f6a3b3e4716b117e2653eff50b4) | oschwartz10612 |
| 2026-11-19 | [Merge pull request #4154 from fosrl/dev](https://github.com/fosrl/pangolin/commit/ab0899c3ea6dad019b4e45d5f224cc09e563c0b2) | oschwartz10612 |
| 2026-11-19 | [Fix api for role settings and add to integration](https://github.com/fosrl/pangolin/commit/210082dcfd587d1764c8d5a3fa28235050e58dd2) | oschwartz10612 |
| 2026-11-19 | [Merge pull request #4153 from fosrl/dev](https://github.com/fosrl/pangolin/commit/f940ac4ecf116f0fe50b6c85a46673465cc1d072) | oschwartz10612 |
| 2026-11-19 | [Make acme load defaults](https://github.com/fosrl/pangolin/commit/c487ea384c88514a743741a036f5928297f63591) | oschwartz10612 |
| 2026-11-19 | [Dont stop the instances at the end](https://github.com/fosrl/pangolin/commit/6d1bd99cb5a980f26df5ff15740c5e0886f177bf) | oschwartz10612 |
| 2026-11-18 | [disable_login_org_names flag](https://github.com/fosrl/pangolin/commit/ff2d4f08db84cd7ac420fbe8c312ae95d95f0138) | oschwartz10612 |
| 2026-11-18 | [Support importing idps in the integration api](https://github.com/fosrl/pangolin/commit/7223e9d8cc21134d93ba1d40af2cd2cffe42f7a4) | oschwartz10612 |
| 2026-11-18 | [Merge pull request #4141 from fosrl/dev](https://github.com/fosrl/pangolin/commit/d120b5f64458fb00a9ee0b6fe78aad19ebba98ff) | oschwartz10612 |

[See all commits ↗](https://github.com/fosrl/pangolin/commits)

## ⬇️ Get it

```bash
git clone https://github.com/fosrl/pangolin.git
```
