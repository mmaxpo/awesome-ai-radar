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
| ⭐ **Stars** | 62.8k |
| 🍴 **Forks** | 4.5k |
| 🐞 **Open issues + PRs** | [928](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5) — 2026-11-24 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 436.4 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5)
<sub>2026-11-24 · 3d ago</sub>

> **:bug: Bugs fixed**
> - Revert [#13165](https://github.com/penpot/penpot/issues/13165), because it causes more regression, the issue is already correctly fixed on the upcoming 2.20.0

### [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4)
<sub>2026-11-23 · 4d ago</sub>

> **:bug: Bugs fixed**
> - Fix importing large `.penpot` files in Chrome [#13165](https://github.com/penpot/penpot/issues/13165) (PR: [#13183](https://github.com/penpot/penpot/pull/13183))

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 9d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 11d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 16d ago</sub>

> **:lock: Security fixes**
> - Fix editor-role team members retrieving the signed invitation token of any pending invitation (https://github.com/penpot/penpot/security/advisories/GHSA-4mmc-j8rh-74pf) (PR: [#12892](https://github.com/penpot/penpot/pull/12892))
> - Fix share-link page-scope escape in `get-profiles-for-file-comments` leaking the identity of comment authors outside the link's scope (https://github.com/penpot/penpot/security/advisories/GHSA-89cq-3wv7-987r) (PR: [#12888](https://github.com/penpot/penpot/pull/12888))
> - Fix missing authorization and unbounded array in mark-all-threads-as-read that let any authenticated user write the status of inaccessible threads (https://github.com/penpot/penpot/security/advisories/GHSA-j4vc-cmf6-jhr7) (PR: [#12894](https://github.com/penpot/penpot/pull/12894))
> - Fix incomplete SVG sanitizer escaping that let a "sanitized" SVG carry live script (CVE-2026-105694) (https://github.com/penpot/penpot/security/advisories/GHSA-qwhj-rchj-58mg) (PR: [#12887](https://github.com/penpot/penpot/pull/12887))
> **:bug: Bugs fixed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [:zap: Build gap overlay bounds from the flex board's shapes only (#13…](https://github.com/penpot/penpot/commit/1cbb532eff328cd96f581f5373c98e91b5f5edbf) | lukel97 |
| 2026-11-27 | [:bug: Resolve the registry in each job instead of passing it along](https://github.com/penpot/penpot/commit/04e3b73c2d95554e5f13cf5c1d42ddac9c0b2db4) | bameda |
| 2026-11-27 | [:bug: Allow apostrophes in custom font family names (#13122)](https://github.com/penpot/penpot/commit/9bcb8a5b038d780b5440be2146ac70215e6b0b2a) | EvaMarco |
| 2026-11-27 | [:recycle: Use the DS select for the shadow type (#13305)](https://github.com/penpot/penpot/commit/814eef62f99a58628903be2b4a3c748137191a23) | EvaMarco |
| 2026-11-27 | [:sparkles: Build preview image sets into their own registry](https://github.com/penpot/penpot/commit/151b40887743a6772435dedb696f8d1fd41c45c8) | bameda |
| 2026-11-27 | [:recycle: Use DS controls in the dashboard progress notification (#13…](https://github.com/penpot/penpot/commit/c3ce46ed9ae152f419de553e995a64b64ecebbca) | EvaMarco |
| 2026-11-27 | [:recycle: Use the DS select for the constraints selects (#13308)](https://github.com/penpot/penpot/commit/f29187aaec06e8aa717ed98522f00641a1981e8a) | EvaMarco |
| 2026-11-27 | [:bug: Add the safe.directory entry only when missing (#12667)](https://github.com/penpot/penpot/commit/a767474773e038ce7c1929e56e8ed89e9e6ed6f2) | alvorithm |
| 2026-11-27 | [:bug: Keep the component shapes the variant repairs write on develop …](https://github.com/penpot/penpot/commit/ab9ea2140de0bbd0fb3b77d6390b46c5ba3cc36d) | EvaMarco |
| 2026-11-27 | [:recycle: Use the DS select for the font variant (#13311)](https://github.com/penpot/penpot/commit/f39b8c9efa1d1dffa1182ec0654746af4cbc939b) | EvaMarco |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
