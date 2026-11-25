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
| 🐞 **Open issues + PRs** | [950](https://github.com/penpot/penpot/issues) |
| 💻 **Languages** | Clojure 76% · JavaScript 6% · Rust 6% · TypeScript 5% · SCSS 3% |
| 📜 **License** | MPL-2.0 |
| 🏷 **Topics** | `ux-design` `ux-experience` `prototyping` `clojure` `clojurescript` `ui` `design` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2015-12-29 |
| 📦 **Latest release** | [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5) — 2026-11-24 |
| 🌿 **Default branch** | `develop` |
| 💾 **Size** | 436.7 MB |
| 🌐 **Website** | https://penpot.app |

## 📦 Recent releases

### [2.19.5](https://github.com/penpot/penpot/releases/tag/2.19.5)
<sub>2026-11-24 · yesterday</sub>

> **:bug: Bugs fixed**
> - Revert [#13165](https://github.com/penpot/penpot/issues/13165), because it causes more regression, the issue is already correctly fixed on the upcoming 2.20.0

### [2.19.4](https://github.com/penpot/penpot/releases/tag/2.19.4)
<sub>2026-11-23 · 2d ago</sub>

> **:bug: Bugs fixed**
> - Fix importing large `.penpot` files in Chrome [#13165](https://github.com/penpot/penpot/issues/13165) (PR: [#13183](https://github.com/penpot/penpot/pull/13183))

### [2.19.3](https://github.com/penpot/penpot/releases/tag/2.19.3)
<sub>2026-11-18 · 7d ago</sub>

> No changes for 2.19.3 according to CHANGES.md

### [2.19.2](https://github.com/penpot/penpot/releases/tag/2.19.2)
<sub>2026-11-16 · 9d ago</sub>

> **:bug: Bugs fixed**
> - Fix referential integrity error when copying component variants with nested components across libraries and teams [#10704](https://github.com/penpot/penpot/issues/10704) (PR: [#12928](https://github.com/penpot/penpot/pull/12928))
> - Fix migration 0033 inserting nil shape entries for dangling child references that blocked file opening [#12936](https://github.com/penpot/penpot/issues/12936) (PR: [#12979](https://github.com/penpot/penpot/pull/12979))
> - Fix switching a variant and adding a component instance taking over 10 seconds in files with many token-styled shapes [#13019](https://github.com/penpot/penpot/issues/13019) (PR: [#13021](https://github.com/penpot/penpot/pull/13021))
> - Fix autosave failing after uploading an SVG as a component in the assets panel, and on other mains named unlike their component [#12773](https://github.com/penpot/penpot/issues/12773) (PR: [#12794](https://github.com/penpot/penpot/pull/12794))
> - Fix `enable-oidc-registration` not working when password login is disabled [#12964](https://github.com/penpot/penpot/issues/12964) (PR: [#12974](https://github.com/penpot/penpot/pull/12974))
> …

### [2.19.1](https://github.com/penpot/penpot/releases/tag/2.19.1)
<sub>2026-11-11 · 14d ago</sub>

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
| 2026-11-25 | [Merge remote-tracking branch 'origin/staging' into develop](https://github.com/penpot/penpot/commit/a0bbafaf12c60804fde2c03a510ed62049e0942a) | superalex |
| 2026-11-25 | [:bug: Honor text and emoji presentation in WebGL text (#13295)](https://github.com/penpot/penpot/commit/f9f5a4cdd0049d62c151c592be39807896382459) | superalex |
| 2026-11-25 | [:sparkles: Add on-demand pull request reviews (#13272)](https://github.com/penpot/penpot/commit/aab5a4752f4fbfaf5aeabb6234c81d5c36be61eb) | MischaPanch |
| 2026-11-25 | [:books: Fix shortcut labels and ruler guide keys in the user guide (#…](https://github.com/penpot/penpot/commit/89717787c78e4f71fe56680fe40576eb937c8c7b) | myfunnyandy |
| 2026-11-25 | [:bug: Normalize legacy svg attrs of pasted shapes (#13334)](https://github.com/penpot/penpot/commit/edd487cddd2dc52d4b135f969147ca3ee1922d43) | EvaMarco |
| 2026-11-25 | [:sparkles: Count the trips of a throttled update loop before reportin…](https://github.com/penpot/penpot/commit/efe420e3e471869d58d0ab425e52dac67f63db0b) | EvaMarco |
| 2026-11-25 | [:bug: Keep variant property order and remove the right property past …](https://github.com/penpot/penpot/commit/1438be5b2614095a1076c784e14e370e0a315e07) | elenatorro |
| 2026-11-25 | [:bug: Ignore default constraints when syncing library components](https://github.com/penpot/penpot/commit/7f53bf76b699dbf69207ff1c496c78b7e52b657b) | pabloalba |
| 2026-11-25 | [:bug: Keep the image when Selected colors changes a text color (#13313)](https://github.com/penpot/penpot/commit/6337810676134b7632dc241a2f33d7383e2fbb15) | EvaMarco |
| 2026-11-25 | [:bug: Validate and repair variant properties as a set](https://github.com/penpot/penpot/commit/571ee80a4b35e340743b703ca8e5cde46e2cfe04) | pabloalba |

[See all commits ↗](https://github.com/penpot/penpot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/penpot/penpot.git
```
