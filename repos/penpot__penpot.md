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
| 🐞 **Open issues + PRs** | [936](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2) — 2026-11-16 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 430.2 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · yesterday</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 6d ago</sub>

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
<sub>2026-11-09 · 8d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

### [2.18.6](https://github.com/penpot/penpot/releases/tag/2.18.6)
<sub>2026-11-04 · 12d ago</sub>

> **:bug: Bugs fixed**
> - Fix upload endpoints storing server files when the path points outside the temp dir [#12771](https://github.com/penpot/penpot/issues/12771) (PR: [#12772](https://github.com/penpot/penpot/pull/12772))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [:zap: Avoid redundant copy of tile atlas (#13104)](https://github.com/penpot/penpot/commit/0bfcaa41094fa6e37c9390a45d975642cfc478ed) | lukel97 |
| 2026-11-17 | [:recycle: Share WASM modifier bindings (#13016)](https://github.com/penpot/penpot/commit/6043edb95a846489a3f9155f2c0ab18d59d3c5c4) | mdbenito |
| 2026-11-17 | [:sparkles: Read and write token files with the tokenscript package (#…](https://github.com/penpot/penpot/commit/94b13d08feed752c7ffe912f3888f30dfb07a293) | floscr |
| 2026-11-17 | [:sparkles: Add scale options panel to the right sidebar (#12453)](https://github.com/penpot/penpot/commit/81c240847052b13ecbbe3913c058a4c000adc3e9) | elhombretecla |
| 2026-11-17 | [:bug: Fix clicking a set in the theme editor (#13067)](https://github.com/penpot/penpot/commit/8b8def3b6ecdd134509c3695e0277d19f42dc936) | floscr |
| 2026-11-17 | [:bug: Reap zombie Chromium processes in the exporter container (#12969)](https://github.com/penpot/penpot/commit/445d02e012c10f8f6f6c26281a66687aa014a254) | rayen-khammar |
| 2026-11-17 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/78cfe7fa587b1b2ae90f72488ea55c5e9c9543ee) | niwinz |
| 2026-11-17 | [Merge branch 'staging-2.19.x' into staging](https://github.com/penpot/penpot/commit/94155508e5e2c1b9c553574987ca5ed718823193) | niwinz |
| 2026-11-17 | [Merge remote-tracking branch 'origin/main' into staging-2.19.x](https://github.com/penpot/penpot/commit/1d60ba65b50b78a83f15bd99f257f368f2361428) | niwinz |
| 2026-11-17 | [:bug: Fix duplicate-file crash on nil keys in deleted component objec…](https://github.com/penpot/penpot/commit/ea0ac02900c3997cc746307b3ceb144eabce3a47) | pabloalba |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
