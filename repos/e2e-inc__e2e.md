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
| ⭐ **Stars** | 14.3k |
| 🍴 **Forks** | 799 |
| 🐞 **Open issues + PRs** | [101](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 133.9 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1)
<sub>2026-11-19 · 6d ago</sub>

> **Patch Changes**
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - Add `@e2e-dev/revyl`: `revyl({ app, device, osVersion })` runs mobile targets on Revyl's hosted iOS simulators and Android emulators, one device per worker slot, through agent-device's `@agent-device/revyl` plugin. Set `REVYL_API_KEY` in the run environment; Revyl installs the build from the `https` `app` URL. Needs `@e2e-dev/mobile` 0.12.8 or later.

### [@e2e-dev/notte@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/notte%400.0.1)
<sub>2026-11-19 · 6d ago</sub>

> **Patch Changes**
> - [#1726](https://github.com/e2e-inc/e2e/pull/1726) [`9602daa`](https://github.com/e2e-inc/e2e/commit/9602daa9602444673b99ef6aaa33c67a81cb2f0b) Thanks [@andreakiro](https://github.com/andreakiro)! - New package: `notte()`, a browser provider that runs each test attempt in its own [Notte](https://notte.cc) cloud browser session, stops it when the attempt ends, reads `browser.waitForDownload` files back from the session's storage, and stops the sessions of workers that died when the run ends. [Notte browsers](https://e2e.com/docs/integrations/notte)

### [@e2e-dev/moli@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/moli%400.0.1)
<sub>2026-11-19 · 6d ago</sub>

> **Patch Changes**
> - [#1843](https://github.com/e2e-inc/e2e/pull/1843) [`29a0261`](https://github.com/e2e-inc/e2e/commit/29a0261775fc362aa26e7ea0fe53e671c864dbc1) Thanks [@ldm0](https://github.com/ldm0)! - Add `moli()` for `web({ browser: moli() })`. Each worker gets a local Moli CDP server with layout and resources enabled, automatic port selection, startup cancellation, and process cleanup when its lease ends.

### [@e2e-dev/testmu@0.0.6](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.6)
<sub>2026-11-19 · 6d ago</sub>

> **Patch Changes**
> - [#1859](https://github.com/e2e-inc/e2e/pull/1859) [`e65091b`](https://github.com/e2e-inc/e2e/commit/e65091bbe10b00860ec6240336b57933a7ce65f7) Thanks [@kdy1](https://github.com/kdy1)! - Update agent-device to 0.21.38. Opening an app now waits for the app's first screen before the first capture, and on Android a relaunch accepts a package that Android restarts at once. On iOS, `device.back()` presses the navigation bar's back button when there is one, keyboard dismiss and enter have a bounded idle wait, and agent-device establishes the screen origin of a full-screen private accessibility root.
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - `@e2e-dev/mobile/lease` adds `agentDevicePlugin(entry)`, which checks a provider plugin's version against the engine's agent-device and registers it in a lease daemon's home; `@e2e-dev/testmu` now uses it and needs `@e2e-dev/mobile` 0.12.8 or later. A lease's `device` selector is used to allocate it and no longer goes on the worker's client, since the lease scope already picks the device.

### [@e2e-dev/smol@0.1.4](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.4)
<sub>2026-11-19 · 6d ago</sub>

> **Patch Changes**
> - [#1785](https://github.com/e2e-inc/e2e/pull/1785) [`ceaea64`](https://github.com/e2e-inc/e2e/commit/ceaea64ceead09d0a0f8cb5b384ef0d9ffac23a1) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.1 and `@ai-sdk/provider` to 4.0.38. Smol sandboxes use the Playwright 1.65.1 image.
> - [#1965](https://github.com/e2e-inc/e2e/pull/1965) [`60d29cf`](https://github.com/e2e-inc/e2e/commit/60d29cfe4c9d88b00659e0d0e00b8973d61e7391) Thanks [@szymonrybczak](https://github.com/szymonrybczak)! - List the maintainers' `@e2e.com` addresses in `contributors`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [feat(web): filter browser.cookies() by URL (ENG-1502) (#2250)](https://github.com/e2e-inc/e2e/commit/a47a95604b6bb49c5c3c1e839b15d0c64295f9d8) | okwasniewski |
| 2026-11-25 | [feat(test): add test.describe.only and the only option on describe (E…](https://github.com/e2e-inc/e2e/commit/769a20051358aeb08188e2ea50306611d27d1d3b) | KrzysztofMoch |
| 2026-11-25 | [fix(report): escape & in markdown text, so entity text shows as writt…](https://github.com/e2e-inc/e2e/commit/c371f78c3a56f8d1b5a72acb4ed0f98b19765886) | abhinavapasok |
| 2026-11-25 | [docs(pt): catch up mobile and web with permissions: 'all' (#2247)](https://github.com/e2e-inc/e2e/commit/679519f13128f6c3f6e621f217583cafee3d2c96) | eriveltonelias |
| 2026-11-25 | [feat(web): add browser.setNetwork to take the browser offline (ENG-10…](https://github.com/e2e-inc/e2e/commit/860f9e5c18f73fd54dc44ad25ed3ee2370bb3fba) | okwasniewski |
| 2026-11-25 | [fix(core): a caught launch() or newSession() rejection no longer fail…](https://github.com/e2e-inc/e2e/commit/511a01acc474c27521dc9f892ee0020e26aa153d) | kdy1 |
| 2026-11-25 | [fix(run): cancel engine calls of a body abandoned at its timeout (ENG…](https://github.com/e2e-inc/e2e/commit/42207c79ec7a927077d0995653aab1a18bf61ab5) | okwasniewski |
| 2026-11-25 | [ci: post microbench results to the pull request as one comment (#2235)](https://github.com/e2e-inc/e2e/commit/5d4e9799629a2222296cad7ee468e06e9945f88f) | kdy1 |
| 2026-11-25 | [test(mobile-benchmark): seed the Photo Picker photo with a fixed capt…](https://github.com/e2e-inc/e2e/commit/c3f2bf37bb29be6397e49afeac7666025f161c07) | karolkulesza |
| 2026-11-25 | [fix(core): read a locator with more than 2048 matches as a set (ENG-1…](https://github.com/e2e-inc/e2e/commit/956f74174148c74acd6380fd8af1e4ab755d9476) | kdy1 |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
