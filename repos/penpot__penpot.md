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
| ⭐ **Stars** | 62.6k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [922](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3) — 2026-11-18 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 432.3 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 4d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 6d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 11d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 12d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 13d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [Merge remote-tracking branch 'origin/develop' into develop](https://github.com/penpot/penpot/commit/8bca3f86eef17dfd67de428e76a5051171c42394) | niwinz |
| 2026-11-20 | [:wrench: Fix CI module commands](https://github.com/penpot/penpot/commit/0572645d97004044dbd274648b3c11a6b5933bf2) | niwinz |
| 2026-11-20 | [:recycle: Reduce the frontend e2e suite by merging equivalent specs (…](https://github.com/penpot/penpot/commit/52750d14de2c7060f7ebe46ca9aa1fcf9239ad0e) | niwinz |
| 2026-11-20 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/adb61a9b968f7b4164f67c59afa702572f90121c) | niwinz |
| 2026-11-20 | [:bug: Check the page that an add-page change stores (#12675)](https://github.com/penpot/penpot/commit/678fcc071bd63e5c80428475e36b08eef26d5b04) | alvorithm |
| 2026-11-20 | [:recycle: Reduce the routes, viewer, theme and typography e2e specs (…](https://github.com/penpot/penpot/commit/f27bfdf76a02b6b0c0171d31e5e765010dc91d35) | niwinz |
| 2026-11-20 | [:sparkles: Deliver telemetry audit events independently (#13230)](https://github.com/penpot/penpot/commit/e0194ce60a637c66bbb5e1619f86cf3316d1f104) | niwinz |
| 2026-11-20 | [:recycle: Cut the shortcuts and inspect tab e2e specs (#13010)](https://github.com/penpot/penpot/commit/1439bc760573f895608ab7cf08239959231240ca) | niwinz |
| 2026-11-20 | [:bug: Repair variant property set when removing a property (#12960)](https://github.com/penpot/penpot/commit/c9c9a574a00f911d401acde0f014b7be6b056430) | pabloalba |
| 2026-11-20 | [:books: Update user guide for 2.20 features (#13149)](https://github.com/penpot/penpot/commit/fae248bb351f1136ae3484e88c4ee252c1348e43) | myfunnyandy |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
