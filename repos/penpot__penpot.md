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
| ⭐ **Stars** | 62.3k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [934](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 75% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1) — 2026-11-11 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 429.8 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 3d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 5d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 5d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

### [2.18.6](https://github.com/penpot/penpot/releases/tag/2.18.6)
<sub>2026-11-04 · 10d ago</sub>

> **:bug: Bugs fixed**
> - Fix upload endpoints storing server files when the path points outside the temp dir [#12771](https://github.com/penpot/penpot/issues/12771) (PR: [#12772](https://github.com/penpot/penpot/pull/12772))

### [2.18.5](https://github.com/penpot/penpot/releases/tag/2.18.5)
<sub>2026-10-26 · 19d ago</sub>

> No changes for 2.18.5 according to CHANGES.md

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [:bug: Fix database pool min-size falling back to max-size (#13052)](https://github.com/penpot/penpot/commit/dc340f74af935e6aaa9a1d730a5b0f5d624bf647) | UsamaSadiq |
| 2026-11-14 | [:arrow_up: Update DHI base images (#13050)](https://github.com/penpot/penpot/commit/a19fbbc826e4504ede440feb755b1bd41d355f86) | penpot-renovate[bot] |
| 2026-11-14 | [:books: Fix typo in export presets docs](https://github.com/penpot/penpot/commit/3ba5a0cb1527c5af483756e4dbaf1dc4a248b5b2) | ajschmidt8 |
| 2026-11-13 | [:bug: Revoke websocket subscriptions when access is revoked (#12189)](https://github.com/penpot/penpot/commit/9c5260314a359ec17fbadb33a59dada7052f5fb1) | niwinz |
| 2026-11-13 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/8715450f535d3cb0da43f8d61ce0d76f1ae081bb) | niwinz |
| 2026-11-13 | [Merge remote-tracking branch 'origin/staging-2.19.x' into staging](https://github.com/penpot/penpot/commit/976f0164817c89f57024a1846417e8dc739cf2a9) | Alotor |
| 2026-11-13 | [:bug: Restore the WASM stack pointer after a failed call (#12978)](https://github.com/penpot/penpot/commit/a7b6ef0d4183a0516ebf7185275d537e1eea9d9f) | belen-albeza |
| 2026-11-13 | [:recycle: Wait on signals instead of event-loop turns on frontend tes…](https://github.com/penpot/penpot/commit/69c33c4877493387a5782d8c4d81652c5d661072) | niwinz |
| 2026-11-13 | [:bug: Keep file_change kind nullable so rollback keeps writing](https://github.com/penpot/penpot/commit/679e70e48ce93d02538ced2c52a7faa339572131) | niwinz |
| 2026-11-13 | [:bug: Limit token propagation to the new instance on swap and instanc…](https://github.com/penpot/penpot/commit/3e48ab96e44101b94484cf6bcb4d3f02e1f3d444) | Alotor |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
