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
| ⭐ **Stars** | 24.0k |
| 🍴 **Forks** | 865 |
| 🐞 **Open issues + PRs** | [142](https://github.com/fosrl/pangolin/issues) |
| 💻 **Languages** | TypeScript 99% |
| 📜 **License** | Other |
| 🏷 **Topics** | `reverse-proxy` `wireguard` `single-sign-on` `self-hosted` `oidc` `vpn` `zero-trust` `zero-trust-network-access` `ztna` `pam` `remote-access` `ssh` `tunneling` `nat-traversal` `sase` `sso` `wireguard-vpn` `pangolin` `ai-gateway` `gateway` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2024-09-27 |
| 📦 **Latest release** | [1.27.1](https://github.com/fosrl/pangolin/releases/tag/1.27.1) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 102.5 MB |
| 🌐 **Website** | https://pangolin.net |

## 📦 Recent releases

### [1.27.1](https://github.com/fosrl/pangolin/releases/tag/1.27.1)
<sub>2026-11-20 · 5d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.27: Managed Client Settings, Per-Org Client Settings](https://pangolin.net/news/1-27-release)
> **What' Changed**
> * Fix change CSS input not appearing in UI
> * Fix IDP across multiple orgs breaking wildcard resources with custom auth pages
> **Full Changelog**: https://github.com/fosrl/pangolin/compare/1.27.0...1.27.1
> …

### [1.27.0](https://github.com/fosrl/pangolin/releases/tag/1.27.0)
<sub>2026-11-19 · 6d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.27: Managed Client Settings, Per-Org Client Settings](https://pangolin.net/news/1-27-release)
> **What’s Changed**
> - Add ability to enforce client (user device) settings on a per-role basis (EE)
> - Add support for selecting labels for alert rules
> - Add custom css to branding
> …

### [1.27.0-rc.0](https://github.com/fosrl/pangolin/releases/tag/1.27.0-rc.0) _(pre-release)_
<sub>2026-11-18 · 7d ago</sub>

> **RC**
> A Release Candidate (RC) is a near-final software version, stable but undergoing last tests before official release. It has all features and no known bugs.
> * Users: Use cautiously due to potential undiscovered bugs. Not for critical systems unless prepared for issues. Report bugs.
> * Developers/Testers: Perform crucial final validation and thorough testing, especially of recent changes, to catch last-minute major issues.
> * Backup: Always back up data before installing an RC to allow rollback if problems arise.
> * Feedback: Provide feedback; it's vital for a robust final release.
> …

### [1.26.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0)
<sub>2026-11-04 · 21d ago</sub>

> **Read the Announcement**
> Read the full announcement with discussion of new features: [Pangolin 1.26: Session Management, SSH Logs, and Auto Windows Updates](https://pangolin.net/news/1-26-release)
> **What’s Changed**
> * Add option to add additional DNS records on delegated domains with Pangolin DNS (EE)
> * Add optional match on base wildcard domains
> * Add continuous session revalidation for OIDC IdPs using refresh tokens (EE)
> …

### [1.26.0-rc.0](https://github.com/fosrl/pangolin/releases/tag/1.26.0-rc.0) _(pre-release)_
<sub>2026-11-02 · 23d ago</sub>

> **RC**
> A Release Candidate (RC) is a near-final software version, stable but undergoing last tests before official release. It has all features and no known bugs.
> * Users: Use cautiously due to potential undiscovered bugs. Not for critical systems unless prepared for issues. Report bugs.
> * Developers/Testers: Perform crucial final validation and thorough testing, especially of recent changes, to catch last-minute major issues.
> * Backup: Always back up data before installing an RC to allow rollback if problems arise.
> * Feedback: Provide feedback; it's vital for a robust final release.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Merge pull request #4189 from fosrl/cross-org-fixes](https://github.com/fosrl/pangolin/commit/c50155384beed9fac7d896502369152640f114a4) | oschwartz10612 |
| 2026-11-26 | [Stop local sites attaching to another org's remote exit node](https://github.com/fosrl/pangolin/commit/c8d6fd2430874549c6680554bb3be7e334b8bd63) | oschwartz10612 |
| 2026-11-26 | [Leave local sites on remote exit nodes alone](https://github.com/fosrl/pangolin/commit/f44148c68738662b404b1b5f35f68b9e4777d8d1) | oschwartz10612 |
| 2026-11-26 | [Add traefik.disable_http_config to turn off GET /traefik-config](https://github.com/fosrl/pangolin/commit/721f150f6b1ebd67e2dc25ae60792d4c9176512f) | oschwartz10612 |
| 2026-11-26 | [Let bannedEmails ban whole domains and plus-addressed variants](https://github.com/fosrl/pangolin/commit/b6bbf36be5d24f88d74e65ac1828e2aa0fa8579a) | oschwartz10612 |
| 2026-11-26 | [Require Traefik trust and a site-resource grant on the private AI gat…](https://github.com/fosrl/pangolin/commit/98e4824b18ae6295f666ee29b649490dfb5c2e18) | oschwartz10612 |
| 2026-11-26 | [Guard tenant-supplied outbound URLs against SSRF](https://github.com/fosrl/pangolin/commit/9eb421cd1b41a1a77d596b0a38d1ae6f629abeca) | oschwartz10612 |
| 2026-11-26 | [Keep tenants from publishing Pangolin's internal services via local s…](https://github.com/fosrl/pangolin/commit/8419370e5b60e48ccacfe5d91c56394361f6b1fe) | oschwartz10612 |
| 2026-11-26 | [Reserve the dashboard host and other orgs' hosts for redirects and bl…](https://github.com/fosrl/pangolin/commit/6497e6d8cf2ce456dde2486ceb1d26c704b423b6) | oschwartz10612 |
| 2026-11-26 | [Scope device approval decisions to the org in the URL](https://github.com/fosrl/pangolin/commit/734c90fa634555e59691b8ae32b73816fabbedf1) | oschwartz10612 |

[See all commits ↗](https://github.com/fosrl/pangolin/commits)

## ⬇️ Get it

```bash
git clone https://github.com/fosrl/pangolin.git
```
