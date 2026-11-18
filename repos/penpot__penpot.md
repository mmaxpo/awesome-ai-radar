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
| 🐞 **Open issues + PRs** | [931](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 75% · JavaScript 6% · Rust 6% · TypeScript 6% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3) — 2026-11-18 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 430.7 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · today</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 2d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 7d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 8d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 9d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [:wrench: Add PRs to status tech-review (#13152)](https://github.com/penpot/penpot/commit/dedd435db56dfb6efeb6b3056ab00f925089acf1) | yamila-moreno |
| 2026-11-18 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/efd95dcf0c4b9bea9bb817da3409e99d3f323819) | niwinz |
| 2026-11-18 | [Merge remote-tracking branch 'origin/staging' into staging](https://github.com/penpot/penpot/commit/dad4479b9cc02c6ed43ed3bf7339b4f7a9f5422d) | niwinz |
| 2026-11-18 | [Merge remote-tracking branch 'origin/staging-2.19.x' into staging](https://github.com/penpot/penpot/commit/2377ab0a16a597d506fd0c38a846cbd08c0cd9c0) | niwinz |
| 2026-11-18 | [:wrench: Test the direction of the move shortcuts (#13115)](https://github.com/penpot/penpot/commit/28a4794d7327662cf8a1c3ddbbc30f7ab40d8592) | EvaMarco |
| 2026-11-18 | [:bug: Show the date of a restored autosaved version in the restore no…](https://github.com/penpot/penpot/commit/eb7860fcd77a93e1f262beb46775abffa0e41ad7) | EvaMarco |
| 2026-11-18 | [:arrow_up: Update the system dependencies of the devenv and the image…](https://github.com/penpot/penpot/commit/aa12e5208136804cbf8f80870bd4f36c69bee438) | niwinz |
| 2026-11-18 | [:wrench: Require milestone in PRs (#13129)](https://github.com/penpot/penpot/commit/89d5a862b57a290d23213e4a4b749bac57a7d621) | yamila-moreno |
| 2026-11-18 | [:bug: Stop camelCase svg attributes from breaking files (#13132)](https://github.com/penpot/penpot/commit/a84d76d3971ef3ebc26f427a0fc2d92e97d49091) | alvorithm |
| 2026-11-18 | [:sparkles: Delay building schemas in check-fn in release builds (#12711)](https://github.com/penpot/penpot/commit/d563444985fb15bbe2a3ca8c4561b2f4776e082e) | lukel97 |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
