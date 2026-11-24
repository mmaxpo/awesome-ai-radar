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
| 🍴 **Forks** | 4.5k |
| 🐞 **Open issues + PRs** | [943](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5) — 2026-11-24 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 434.6 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5)
<sub>2026-11-24 · today</sub>

> **:bug: Bugs fixed**
> - Revert [#13165](https://github.com/penpot/penpot/issues/13165), because it causes more regression, the issue is already correctly fixed on the upcoming 2.20.0

### [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4)
<sub>2026-11-23 · yesterday</sub>

> **:bug: Bugs fixed**
> - Fix importing large `.penpot` files in Chrome [#13165](https://github.com/penpot/penpot/issues/13165) (PR: [#13183](https://github.com/penpot/penpot/pull/13183))

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 6d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 8d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 13d ago</sub>

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
| 2026-11-24 | [:bug: Show the full library name in a tooltip when it is cut (#13237)](https://github.com/penpot/penpot/commit/07c3409ad0fbcc9ba1126833865f446ac81847da) | EvaMarco |
| 2026-11-24 | [:bug: Add opt-in MCP JSON replies and deliver pending outcomes on shu…](https://github.com/penpot/penpot/commit/01a7342f4b66fa9177730fc796dcf30f9f885858) | myagizmaktav |
| 2026-11-24 | [:sparkles: Add nitrate methods to bring owned teams into an organizat…](https://github.com/penpot/penpot/commit/dc49d6bed6e898e075dc7ad52d25e16464aab5a5) | juanfran |
| 2026-11-24 | [Merge remote-tracking branch 'origin/develop' into develop](https://github.com/penpot/penpot/commit/495df7ef667bf81a3c3eb617c9ac45871cd53a1e) | niwinz |
| 2026-11-24 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/4427b83ae0430eb5ff1fefece9a1ccc298c93347) | niwinz |
| 2026-11-24 | [:bug: Fix not rendering & computing into layout trailing white spaces…](https://github.com/penpot/penpot/commit/5aac5ab9bafe8f88e4553c23371fcea25e02d0cf) | belen-albeza |
| 2026-11-24 | [Merge remote-tracking branch 'origin/staging-2.19.x' into staging](https://github.com/penpot/penpot/commit/bc3f8dd6ef162d3288b4a0fce9ed65586db48f6b) | niwinz |
| 2026-11-24 | [:bug: Correct UI CSS export and test restore flow](https://github.com/penpot/penpot/commit/5fafca7665cd973707e19a742d7411768a86835f) | niwinz |
| 2026-11-24 | [:tada: Add a command to create pull requests](https://github.com/penpot/penpot/commit/b52fcc7e6d822e6dc5310cb9d200a6593417900f) | niwinz |
| 2026-11-24 | [:bug: Fix render-wasm panic when an auto layout has only absolute chi…](https://github.com/penpot/penpot/commit/407ee58ddd9bd5a744bd988d1c88b5c122eee449) | elenatorro |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
