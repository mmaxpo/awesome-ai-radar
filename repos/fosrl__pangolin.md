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
| ⭐ **Stars** | 23.7k |
| 🍴 **Forks** | 836 |
| 🐞 **Open issues + PRs** | [130](https://github.com/fosrl/pangolin/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `reverse-proxy` `wireguard` `single-sign-on` `self-hosted` `oidc` `vpn` `zero-trust` `zero-trust-network-access` `ztna` `pam` `remote-access` `ssh` `tunneling` `nat-traversal` `sase` `sso` `wireguard-vpn` `pangolin` `ai-gateway` `gateway` |
| 🕒 **Last activity** | 2026-11-13 (today) |
| 📅 **Created** | 2024-09-27 |
| 📦 **Latest release** | [1.26.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 98.9 MB |
| 🌐 **Website** | https://pangolin.net |

## 📦 Recent releases

### [1.26.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0)
<sub>2026-11-04 · 10d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.26: Session Management, SSH Logs, and Auto Windows Updates](https://pangolin.net/news/1-26-release)
> **What’s Changed**
> * Add option to add additional DNS records on delegated domains with Pangolin DNS (EE)
> * Add optional match on base wildcard domains
> * Add continuous session revalidation for OIDC IdPs using refresh tokens (EE)
> …

### [1.26.0-rc.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0-rc.0) _(pre-release)_
<sub>2026-11-02 · 11d ago</sub>

> **RC**
> A Release Candidate (RC) is a near-final software version, stable but undergoing last tests before official release. It has all features and no known bugs.
> * Users: Use cautiously due to potential undiscovered bugs. Not for critical systems unless prepared for issues. Report bugs.
> * Developers/Testers: Perform crucial final validation and thorough testing, especially of recent changes, to catch last-minute major issues.
> * Backup: Always back up data before installing an RC to allow rollback if problems arise.
> * Feedback: Provide feedback; it's vital for a robust final release.
> …

### [1.25.3](https://github.com/fosrl/pangolin/releases/tag/1.25.3)
<sub>2026-10-23 · 22d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.25: Redirects, mTLS, and Machine Roles](https://pangolin.net/news/1-25-release)
> **What's Changed**
> * Update node to resolve Node2Shell CVE-2026-111497
> * Improve client connection speed with many sites
> * Fix agent and olm version separate in the database
> …

### [1.25.2](https://github.com/fosrl/pangolin/releases/tag/1.25.2)
<sub>2026-10-22 · 23d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.25: Redirects, mTLS, and Machine Roles](https://pangolin.net/news/1-25-release)
> **What's Changed**
> * Fix include optional name in blueprint health check
> * Fix mTLS hidden by enterprise feature flag on CE
> **Full Changelog**: https://github.com/fosrl/pangolin/compare/1.25.1...1.25.2
> …

### [1.25.1](https://github.com/fosrl/pangolin/releases/tag/1.25.1)
<sub>2026-10-21 · 23d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.25: Redirects, mTLS, and Machine Roles](https://pangolin.net/news/1-25-release)
> **What's Changed**
> * Fix updated clients failing to relay
> * Fix credential generation not showing with EE features disabled
> **Full Changelog**: https://github.com/fosrl/pangolin/compare/1.25.0...1.25.1
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-12 | [Merge pull request #4097 from berndderidder/update-node](https://github.com/fosrl/pangolin/commit/a83ad5da0a24db22ac99677068dbfccc6ef76d73) | oschwartz10612 |
| 2026-11-12 | [Update to node 24.22.3](https://github.com/fosrl/pangolin/commit/212a127517f2ef02bc69387f6439b5e0d1af67d7) | berndderidder |
| 2026-11-09 | [Merge pull request #4082 from fosrl/dev](https://github.com/fosrl/pangolin/commit/6e783a21965a9b0c94926d53d83b854d786cb6bb) | oschwartz10612 |
| 2026-11-09 | [Get latest versions from the Fossorial API instead of GitHub](https://github.com/fosrl/pangolin/commit/8ae5a08b2970dc41888072870557ca7335431926) | oschwartz10612 |
| 2026-11-09 | [Check site access before adding an olm peer](https://github.com/fosrl/pangolin/commit/52dfcca0bca54bb636529cbd7cddf96764dad75b) | oschwartz10612 |
| 2026-11-09 | [Rate limit user lookups per IP](https://github.com/fosrl/pangolin/commit/34c2fb8e6bf0e42dd5c834ea62fe8ce1f46d6d07) | oschwartz10612 |
| 2026-11-09 | [Scope domain reads and rule deletes to their owner](https://github.com/fosrl/pangolin/commit/dbfb7ce4002956c1b8ad899209039a50abd3bfca) | oschwartz10612 |
| 2026-11-09 | [Strip cookies from AI gateway upstream requests](https://github.com/fosrl/pangolin/commit/3906c3633f7f4f96dedbf5242f88262a9b5ca871) | oschwartz10612 |
| 2026-11-09 | [Leave OIDC client credentials out of the internal IdP route](https://github.com/fosrl/pangolin/commit/a00bfa942d2d5657f5782bde77422b05a1b752f1) | oschwartz10612 |
| 2026-11-09 | [Block duplicate hostnames on non-inference resources](https://github.com/fosrl/pangolin/commit/856d1dd7169e359ad88c2021e5512a8d9257f3a9) | oschwartz10612 |

[See all commits ↗](https://github.com/fosrl/pangolin/commits)

## ⬇️ Get it

```bash
git clone https://github.com/fosrl/pangolin.git
```
