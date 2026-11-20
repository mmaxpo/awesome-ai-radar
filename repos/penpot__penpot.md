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
| 🐞 **Open issues + PRs** | [934](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3) — 2026-11-18 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 433.1 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 2d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 4d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 9d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 11d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 11d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [:zap: Resolve tokens incrementally with tokenscript (#12437)](https://github.com/penpot/penpot/commit/3c4ae62db53b3e844a5ea4cb54aaee8efe2f7d14) | floscr |
| 2026-11-20 | [:zap: Fuse the reg-objects of a change batch per container (#12310)](https://github.com/penpot/penpot/commit/b6a08ea4cb79bcc46c9bb4843ec8061df8e92bbe) | niwinz |
| 2026-11-20 | [:sparkles: Cover subscription rules with unit tests and trim e2e spec…](https://github.com/penpot/penpot/commit/d6e816daa045146f5e8c919ceed0aa0ec375662f) | niwinz |
| 2026-11-20 | [:wrench: Fix pr validations](https://github.com/penpot/penpot/commit/ea11c4d71d519556c4b068cc25a819532a9be7fb) | yamila-moreno |
| 2026-11-20 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/15a099f1188c427beae4c75d680ad7d246cff074) | niwinz |
| 2026-11-20 | [:arrow_up: Update dependencies (#13191)](https://github.com/penpot/penpot/commit/1debed7f3c244d4698544839b0bbab0cfce21bd2) | niwinz |
| 2026-11-20 | [:sparkles: Explain why a library cannot be disconnected in its modal …](https://github.com/penpot/penpot/commit/c40287254cce63b69732e0b6814bedf9b67c1fd8) | filipsajdak |
| 2026-11-20 | [:sparkles: Copy stable deep link to selected boards from context menu…](https://github.com/penpot/penpot/commit/454e461c1eda2f164bcf87df13bb65d7093b7d06) | filipsajdak |
| 2026-11-19 | [:bug: Undo a main text edit and its follow-up sync in one step](https://github.com/penpot/penpot/commit/6d0be9f47f18e7ca4a3716d7a483351533b2822f) | pabloalba |
| 2026-11-19 | [:bug: Skip WebGL auto-grow heals for texts with a failed font](https://github.com/penpot/penpot/commit/8a9e87e33eb7262a0156ac1ea0cdd205d35e570e) | pabloalba |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
