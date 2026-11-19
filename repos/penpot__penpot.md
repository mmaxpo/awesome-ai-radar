# penpot/penpot

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/penpot/penpot)

> Penpot: The open-source design platform for Product teams that need scalable collaboration.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🎨 Design & creative |
| **Project** | — |
| **Why it's worth a look** | Open-source design tool (Figma alternative) with MCP support |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 62.5k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [948](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 75% · JavaScript 6% · Rust 6% · TypeScript 6% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3) — 2026-11-18 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 431.2 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · yesterday</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 3d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 8d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 10d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 10d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [:sparkles: Add viewers so org owners can change member role (#13163)](https://github.com/penpot/penpot/commit/b100a5e26f9b0d762ce3edbd00997d4b7f0874fb) | cocotime |
| 2026-11-19 | [:arrow_up: Update DHI base images (#13170)](https://github.com/penpot/penpot/commit/210cbd6cc7ee0c60efa182336ab47e18cd1ee61c) | penpot-renovate[bot] |
| 2026-11-19 | [Merge branch 'staging' into develop](https://github.com/penpot/penpot/commit/a6d12c5c329ca93f64ce8dbd951d76feb82d398a) | niwinz |
| 2026-11-19 | [:bug: Fix problem with Penpot plugins being blocked (#13147)](https://github.com/penpot/penpot/commit/951ebbba6ac70316c2fb41af7359a67301ef0fdb) | Alotor |
| 2026-11-19 | [:bug: Keep fill copies laid out after a component sync in the WebGL r…](https://github.com/penpot/penpot/commit/981fa0696137d40794665a45e7a8c9b362081083) | elenatorro |
| 2026-11-19 | [:sparkles: Expose the instance URL and query params to plugins (#13018)](https://github.com/penpot/penpot/commit/b6db09e2fb9cec6f6d4817c93b1b025b4b5b0497) | Alotor |
| 2026-11-19 | [:wrench: Add exemption to linked issues workflow](https://github.com/penpot/penpot/commit/be7be634d915e04f71913d5a64dd4c38f0584d5e) | yamila-moreno |
| 2026-11-19 | [:wrench: Add exemption to linked issues workflow](https://github.com/penpot/penpot/commit/03a4c73b621d3ab6ea381d45bb07679dc418d2b6) | yamila-moreno |
| 2026-11-19 | [:wrench: Prevent PRs without issue from merging](https://github.com/penpot/penpot/commit/2695434362d870249e3d26ea8022b8b1c52367ba) | yamila-moreno |
| 2026-11-19 | [:wrench: Prevent PRs without issue from merging](https://github.com/penpot/penpot/commit/172a3589e8977ffdd4f9c07a05f1f889bb835512) | yamila-moreno |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
