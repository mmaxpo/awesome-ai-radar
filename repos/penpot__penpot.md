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
| 🐞 **Open issues + PRs** | [938](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5) — 2026-11-24 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 436.3 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5)
<sub>2026-11-24 · 2d ago</sub>

> **:bug: Bugs fixed**
> - Revert [#13165](https://github.com/penpot/penpot/issues/13165), because it causes more regression, the issue is already correctly fixed on the upcoming 2.20.0

### [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4)
<sub>2026-11-23 · 3d ago</sub>

> **:bug: Bugs fixed**
> - Fix importing large `.penpot` files in Chrome [#13165](https://github.com/penpot/penpot/issues/13165) (PR: [#13183](https://github.com/penpot/penpot/pull/13183))

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 8d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 10d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 15d ago</sub>

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
| 2026-11-26 | [:bug: Use ControlOrMeta for primary modifier in Playwright specs](https://github.com/penpot/penpot/commit/f3fa38ecf690a5d57b0af3ccbcdad452e7516601) | belen-albeza |
| 2026-11-26 | [:bug: Fix render-wasm Playwright specs on macOS](https://github.com/penpot/penpot/commit/08365f6e1f521d9ddfc35dbd7dba4b49b83794e5) | lukel97 |
| 2026-11-26 | [:sparkles: Leave the opacity shortcuts without a default key (#13309)](https://github.com/penpot/penpot/commit/b80456b607a77a0c3006afcfb243c25fd3f1f962) | EvaMarco |
| 2026-11-26 | [:bug: Preserve effective center alignment on existing strokes (#11692)](https://github.com/penpot/penpot/commit/58d35aae984fa9b61e4c184dfe145cecc4b6a26c) | makesomethingshit |
| 2026-11-26 | [:bug: Show MCP URL copied toast only after a successful copy (#13360)](https://github.com/penpot/penpot/commit/4d0486e811b6907433419b289ac9bede8a6a00fa) | gabrielribeiro3105 |
| 2026-11-26 | [:bug: Review pull requests whose diff exceeds GitHub's limit (#13355)](https://github.com/penpot/penpot/commit/7c1de34c6c5ebd4c561c692a531cd4d9fe4aec6e) | Alotor |
| 2026-11-26 | [:recycle: Use a DS secondary button in the request access dialog (#13…](https://github.com/penpot/penpot/commit/f65009a2546d4820e83b3a0da6cd567c48e94529) | EvaMarco |
| 2026-11-26 | [:recycle: Use DS icon buttons for the Measures toggles (#13278)](https://github.com/penpot/penpot/commit/6aedbc330e85f36294f8118ce09e2407deeac837) | EvaMarco |
| 2026-11-26 | [:recycle: Use the DS button in the Design tab export menu (#13275)](https://github.com/penpot/penpot/commit/9977a4fbc6d4512f4794a68fb15cc16bdbe22053) | EvaMarco |
| 2026-11-26 | [:sparkles: Focus a new page when it is added from the Pages list (#13…](https://github.com/penpot/penpot/commit/284ffbc39109e6b0cb28de6fe7053e44997ea2a8) | EvaMarco |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
