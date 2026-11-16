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
| ⭐ **Stars** | 62.4k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [943](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 75% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2) — 2026-11-16 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 429.2 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · today</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 5d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

### [2.19.0](https://github.com/penpot/penpot/releases/tag/2.19.0)
<sub>2026-11-09 · 6d ago</sub>

> **:boom: Breaking changes & Deprecations**
> **Migrate legacy file payloads to file_data and delete orphan revisions**
> File payloads now live in one place: every file state and snapshot is kept in `file_data`, and the orphan `file_change` rows that kept old payloads alive forever are removed. No read path reached those rows and nothing ever collected them, so the upgrade also reclaims the database and TOAST space they held. There is no API or UI change.
> On small and medium instances this happens automatically on boot and there is nothing to do. On large instances (millions of snapshots, hundreds of GB in TOAST) the work does not fit in the startup transaction: run it by hand **before upgrading to 2.19.0** following the [large-instance runbook](https://github.com/penpot/penpot/blob/staging/operations/2.19.0-migrate-legacy-file-data.md). The runbook tells you whether your instance needs it, keeps the instance online while the data moves, and verifies the result before you deploy.
> [#12784](https://github.com/penpot/penpot/issues/12784) (PR: [#12785](https://github.com/penpot/penpot/pull/12785))
> **Enable the Admin Console by default**
> …

### [2.18.7](https://github.com/penpot/penpot/releases/tag/2.18.7)
<sub>2026-11-09 · 7d ago</sub>

> **:bug: Bugs fixed**
> - Fix binfile import accepting library relations outside the package and self-relations [#12895](https://github.com/penpot/penpot/issues/12895) (PR: [#12862](https://github.com/penpot/penpot/pull/12862))

### [2.18.6](https://github.com/penpot/penpot/releases/tag/2.18.6)
<sub>2026-11-04 · 11d ago</sub>

> **:bug: Bugs fixed**
> - Fix upload endpoints storing server files when the path points outside the temp dir [#12771](https://github.com/penpot/penpot/issues/12771) (PR: [#12772](https://github.com/penpot/penpot/pull/12772))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [:zap: Memoize boards with grids in frame-grid* (#13075)](https://github.com/penpot/penpot/commit/a224608a0ed58aa130c5781f1671067a1df488bb) | lukel97 |
| 2026-11-16 | [:books: Name a worker count when running the Playwright suite (#12799)](https://github.com/penpot/penpot/commit/bd4af28d78f14fb800b9f808be4522259597bd4c) | alvorithm |
| 2026-11-16 | [:bug: Send the team's custom fonts to the worker (#13044)](https://github.com/penpot/penpot/commit/bbaebfb146673044468d37d8ff48f411584bd52e) | lukel97 |
| 2026-11-16 | [:zap: Move WASM component thumbnail rendering to the worker (#13046)](https://github.com/penpot/penpot/commit/1ccb9e9cb9c88e4c707c3852fe8e3b3397cd82a9) | lukel97 |
| 2026-11-16 | [:bug: Fix blurry file thumbnails rendered with render-wasm (#13026)](https://github.com/penpot/penpot/commit/b0dbbe828597f92d9b36a11173466e9f7ac57b6d) | belen-albeza |
| 2026-11-16 | [:arrow_up: Update dependency pnpm to v12.21.0 (#13063)](https://github.com/penpot/penpot/commit/99497d3b7c75468db113db8400cd69f2d48a4fe2) | penpot-renovate[bot] |
| 2026-11-16 | [:arrow_up: Update DHI base images (#13062)](https://github.com/penpot/penpot/commit/4d91d8f098e149c175c7031e087bdddf60cdd12a) | penpot-renovate[bot] |
| 2026-11-16 | [:bug: Retry the publish of the websocket delivery assertions](https://github.com/penpot/penpot/commit/e95007a93bc660700706b4b6ceb6748c01682c4e) | niwinz |
| 2026-11-16 | [:books: Add the 2.21.0 changelog section](https://github.com/penpot/penpot/commit/239291539b74a4a3db6af3d92ef1b66847b075b2) | niwinz |
| 2026-11-16 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/18a827d65aeaab3b9a70329798cd0fc4d2e72c48) | niwinz |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
