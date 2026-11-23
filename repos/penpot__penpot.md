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
| ⭐ **Stars** | 62.7k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [929](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4) — 2026-11-23 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 433.2 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4)
<sub>2026-11-23 · today</sub>

> **:bug: Bugs fixed**
> - Fix importing large `.penpot` files in Chrome [#13165](https://github.com/penpot/penpot/issues/13165) (PR: [#13183](https://github.com/penpot/penpot/pull/13183))

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 5d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 7d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 12d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 14d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [:books: Simplify issue and changelog memories](https://github.com/penpot/penpot/commit/3a1f17834efe1390d8d614b7bf8a1eb93a2700bc) | niwinz |
| 2026-11-23 | [:books: Organize frontend memories by task](https://github.com/penpot/penpot/commit/e23901a36f6eb4d9c90fa7d3d0d4b87940b1211b) | niwinz |
| 2026-11-23 | [:books: Trim backend memories and split out job guidance](https://github.com/penpot/penpot/commit/8f2405bb8de4339d96636247e840d15b1fdd9baa) | niwinz |
| 2026-11-23 | [:books: Trim agent guidance while keeping required memory reads](https://github.com/penpot/penpot/commit/d40fe15a317f85cd22876cee043f3c5604f0d629) | niwinz |
| 2026-11-23 | [:arrow_up: update actions/create-github-app-token action to v3.4.0 (#…](https://github.com/penpot/penpot/commit/6c482b04356e9e7c764bbd693b3112a57142dfaa) | penpot-renovate[bot] |
| 2026-11-23 | [:arrow_up: Update DHI base images (#13240)](https://github.com/penpot/penpot/commit/1bd1594ff591623b8d3c9576c62f62bbb8293db3) | penpot-renovate[bot] |
| 2026-11-23 | [:bug: Fix batch edit of colors in the selected colors menu (#13087)](https://github.com/penpot/penpot/commit/340f5e36cf1f4289c04dda0a19fe68fcf5341d93) | luisddm |
| 2026-11-23 | [:wrench: Improve PRs validations](https://github.com/penpot/penpot/commit/8fe1b9c659c96f012e251db604eaa5365b7cd3a9) | yamila-moreno |
| 2026-11-23 | [:sparkles: Add Copy link to the file and project menus in the dashboa…](https://github.com/penpot/penpot/commit/3346c67a3b50386550a544400f8d565891ff68cc) | myfunnyandy |
| 2026-11-23 | [:wrench: Test applying dimension and spacing tokens (#13215)](https://github.com/penpot/penpot/commit/888e2d936844e6f3eb859f599e1a1f7137877268) | floscr |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
