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
| ⭐ **Stars** | 14.4k |
| 🍴 **Forks** | 801 |
| 🐞 **Open issues + PRs** | [108](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/testmu@0.0.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.7) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 130.9 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/testmu@0.0.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.7)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.

### [@e2e-dev/revyl@0.0.2](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.2)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.
> - [#1947](https://github.com/e2e-inc/e2e/pull/1947) [`8255089`](https://github.com/e2e-inc/e2e/commit/82550897f47469272d464fa92c3580033442af02) Thanks [@KayaanT](https://github.com/KayaanT)! - Tests a local build on Revyl: with `app` left out of `revyl()`, each device starts with no app and the target's `app.appPath` is uploaded to it and installed there.

### [@e2e-dev/limrun@0.2.7](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/limrun%400.2.7)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - [#1975](https://github.com/e2e-inc/e2e/pull/1975) [`1676981`](https://github.com/e2e-inc/e2e/commit/1676981ab76fd7a8b7262057a74b320545b0e3bb) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.42. On iOS, `device.dismissKeyboard()` no longer presses the keyboard's Hide Keyboard or Done key: an iPad keyboard now goes away by the same short drag as an iPhone one. Pressing Enter sends one Return to the focused input, a fill reaches only the input a tap at that point reaches, and a command on a session whose simulator was deleted fails at once instead of waiting about 20 seconds. A fill on iOS is also a little faster.

### [@e2e-dev/kernel@0.2.4](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/kernel%400.2.4)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - [#2122](https://github.com/e2e-inc/e2e/pull/2122) [`13b5450`](https://github.com/e2e-inc/e2e/commit/13b5450384eb7aad4c44f9d2f95dc1821a47ec2e) Thanks [@DeryFerd](https://github.com/DeryFerd)! - The Kernel provider no longer prints the browser's live view URL into the run log; it logs `browser <id>` alone. The view URL carries tokens that act on the session, and a run's log is often public CI output. The browser keeps its `e2e_run`, `e2e_target`, and `e2e_slot` tags, so Kernel's dashboard still finds it.

### [@e2e-dev/eas@0.3.6](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/eas%400.3.6)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - [#2184](https://github.com/e2e-inc/e2e/pull/2184) [`a560224`](https://github.com/e2e-inc/e2e/commit/a5602240c9e37ecf60310b68fb508a0225676524) Thanks [@DeryFerd](https://github.com/DeryFerd)! - The install command now lists `e2e` and `@e2e-dev/mobile`. Installing `@e2e-dev/eas` alone left them out of `package.json`, and with pnpm `e2e.config.ts` could not import them.
> - [#2224](https://github.com/e2e-inc/e2e/pull/2224) [`06aa108`](https://github.com/e2e-inc/e2e/commit/06aa108bb858e9acacd06099a38fe7633cee2060) Thanks [@okwasniewski](https://github.com/okwasniewski)! - `expoSimulators()` installs a local build itself: with no `buildId` or `applicationArchiveUrl`, the target's `app.appPath` is uploaded to each simulator and installed there, before the first test. Remove a fixture that calls `device.installApp()` for that build, since it now uploads the build a second time. A session whose build does not install is stopped. Needs `@e2e-dev/mobile` 0.12.9 or later.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(mobile): release leased device session before stopping daemon (#1…](https://github.com/e2e-inc/e2e/commit/c801a12f8afea963775652ba73a7dbeaea894fa2) | GaspardIV |
| 2026-11-26 | [fix(core): keep unreadable artifacts marked as incomplete (#2311)](https://github.com/e2e-inc/e2e/commit/d32dc7cfbbdfbdee13e306b48ffd73a024d9b164) | michal-e2e |
| 2026-11-26 | [docs: make guides easier to read and cut robotic phrasing (#2310)](https://github.com/e2e-inc/e2e/commit/c3109278ee064d3cfe5c7468ab873631ab63fdac) | okwasniewski |
| 2026-11-26 | [fix(types): reject annotated config types in test.extend (ENG-1530) (…](https://github.com/e2e-inc/e2e/commit/1ed0f183ae821a71c06473c7013824a1b2f3c540) | satya164 |
| 2026-11-26 | [feat(cli): leave pnpm's skill links alone in init and upgrade, and dr…](https://github.com/e2e-inc/e2e/commit/a423238bad96007b31399f0af510e3633c5cd07a) | michal-e2e |
| 2026-11-26 | [fix(core): retire a host whose failed launch could not end its attemp…](https://github.com/e2e-inc/e2e/commit/935e3f8bb23554a210dab2d177c5a2e13a9eae5a) | okwasniewski |
| 2026-11-26 | [feat(web): add browser.name and browser.version (ENG-1242) (#2251)](https://github.com/e2e-inc/e2e/commit/a118c36ea51e8942510eb2f1927b0a77cdf0f34c) | okwasniewski |
| 2026-11-26 | [docs(skill): cut the e2e skill in half and point to the docs for full…](https://github.com/e2e-inc/e2e/commit/976482432ccb566dcc792393620b65a7e084a201) | michal-e2e |
| 2026-11-26 | [fix(run): stop dispatching to a worker that reported a fatal error (#…](https://github.com/e2e-inc/e2e/commit/74e2abea83a4b70120d8e36fb33d25af15edb0dd) | okwasniewski |
| 2026-11-26 | [feat(skill): prefer agent.act when configured, tighten test structure…](https://github.com/e2e-inc/e2e/commit/d31e76719c884b50edbf7556afd22f43c1394e1d) | michal-e2e |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
