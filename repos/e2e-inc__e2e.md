# e2e-inc/e2e

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/e2e-inc/e2e)

> Next generation e2e testing framework for web and mobile apps.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | End-to-end testing for agent-written code |
| **Added** | 2026-11-14 |

↪️ **Moved** — was `tester-army/e2e` · 🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 14.5k |
| 🍴 **Forks** | 808 |
| 🐞 **Open issues + PRs** | [141](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 97% · Rust 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.7) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 133.9 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.7)
<sub>2026-11-25 · yesterday</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.

### [@e2e-dev/revyl@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.2)
<sub>2026-11-25 · yesterday</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.
> - [#1947](https://github.com/e2e-inc/e2e/pull/1947) [`8255089`](https://github.com/e2e-inc/e2e/commit/82550897f47469272d464fa92c3580033442af02) Thanks [@KayaanT](https://github.com/KayaanT)! - Tests a local build on Revyl: with `app` left out of `revyl()`, each device starts with no app and the target's `app.appPath` is uploaded to it and installed there.

### [@e2e-dev/limrun@0.2.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.7)
<sub>2026-11-25 · yesterday</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.

### [@e2e-dev/kernel@0.2.4](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.4)
<sub>2026-11-25 · yesterday</sub>

> **Patch Changes**
> - [#2122](https://github.com/e2e-inc/e2e/pull/2122) [`13b5450`](https://github.com/e2e-inc/e2e/commit/13b5450384eb7aad4c44f9d2f95dc1821a47ec2e) Thanks [@DeryFerd](https://github.com/DeryFerd)! - The Kernel provider no longer prints the browser's live view URL into the run log; it logs `browser <id>` alone. The view URL carries tokens that act on the session, and a run's log is often public CI output. The browser keeps its `e2e_run`, `e2e_target`, and `e2e_slot` tags, so Kernel's dashboard still finds it.

### [@e2e-dev/eas@0.3.6](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/eas%400.3.6)
<sub>2026-11-25 · yesterday</sub>

> **Patch Changes**
> - [#2184](https://github.com/e2e-inc/e2e/pull/2184) [`a560224`](https://github.com/e2e-inc/e2e/commit/a5602240c9e37ecf60310b68fb508a0225676524) Thanks [@DeryFerd](https://github.com/DeryFerd)! - The install command now lists `e2e` and `@e2e-dev/mobile`. Installing `@e2e-dev/eas` alone left them out of `package.json`, and with pnpm `e2e.config.ts` could not import them.
> - [#2224](https://github.com/e2e-inc/e2e/pull/2224) [`06aa108`](https://github.com/e2e-inc/e2e/commit/06aa108bb858e9acacd06099a38fe7633cee2060) Thanks [@okwasniewski](https://github.com/okwasniewski)! - `expoSimulators()` installs a local build itself: with no `buildId` or `applicationArchiveUrl`, the target's `app.appPath` is uploaded to each simulator and installed there, before the first test. Remove a fixture that calls `device.installApp()` for that build, since it now uploads the build a second time. A session whose build does not install is stopped. Needs `@e2e-dev/mobile` 0.12.9 or later.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [docs(id): translate the getting-started and platform pages (#2193)](https://github.com/e2e-inc/e2e/commit/1535215b2e2ced13b36ba2e4e0bcbe093afeab63) | ardi-zanki |
| 2026-11-27 | [docs(examples): add the web scraper example (ENG-1559) (#2376)](https://github.com/e2e-inc/e2e/commit/ad5d186ff3d345cabf3a09fcae4f487ed39540ff) | kacperkapusciak |
| 2026-11-27 | [fix(acp): disable CODEX_FEATURES_OFF when listing Codex MCP servers (…](https://github.com/e2e-inc/e2e/commit/27fd3763f9f2207c07c7c6a1ce4b719359e686cd) | aloneangel45 |
| 2026-11-27 | [fix(desktop): count a SwiftUI alert button's press as landed (#2347)](https://github.com/e2e-inc/e2e/commit/75a950897c74a098ff99b13161f245b75620f0e1) | okwasniewski |
| 2026-11-27 | [docs(core): give the real default of app.identity (#2360)](https://github.com/e2e-inc/e2e/commit/6c87952d886baee0143d2a8556ca6d9011b62ed4) | leninworld |
| 2026-11-27 | [docs: move @e2e-dev/core out of Platforms and Test API (GTM-1176) (#2…](https://github.com/e2e-inc/e2e/commit/731045fae137962dbece4759f11b76c3d010a23d) | kacperkapusciak |
| 2026-11-27 | [feat(agents): add per-agent maxContextBytes (#2350)](https://github.com/e2e-inc/e2e/commit/7e733376ecdbe1f7aee7f17c2aef05bb9a1bdf49) | okwasniewski |
| 2026-11-27 | [Point NOTICE files at e2e.com (#2349)](https://github.com/e2e-inc/e2e/commit/3015db6acefb4ed1ecbe3fe84e672a8f6370f4d1) | okwasniewski |
| 2026-11-27 | [fix(config): accept undefined entries in config records (ENG-1538) (#…](https://github.com/e2e-inc/e2e/commit/026d8570d7c64784760c29253ce727f0ce72eba6) | satya164 |
| 2026-11-27 | [docs(expect): say poll and toPass default to the configured timeouts …](https://github.com/e2e-inc/e2e/commit/2b6ef91d7a707ed39b9b5569bf471815b8bdfb18) | leninworld |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
