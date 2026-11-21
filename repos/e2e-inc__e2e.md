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
| ⭐ **Stars** | 14.1k |
| 🍴 **Forks** | 785 |
| 🐞 **Open issues + PRs** | [141](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 121.9 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1)
<sub>2026-11-19 · yesterday</sub>

> **Patch Changes**
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - Add `@e2e-dev/revyl`: `revyl({ app, device, osVersion })` runs mobile targets on Revyl's hosted iOS simulators and Android emulators, one device per worker slot, through agent-device's `@agent-device/revyl` plugin. Set `REVYL_API_KEY` in the run environment; Revyl installs the build from the `https` `app` URL. Needs `@e2e-dev/mobile` 0.12.8 or later.

### [@e2e-dev/notte@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/notte%400.0.1)
<sub>2026-11-19 · yesterday</sub>

> **Patch Changes**
> - [#1726](https://github.com/e2e-inc/e2e/pull/1726) [`9602daa`](https://github.com/e2e-inc/e2e/commit/9602daa9602444673b99ef6aaa33c67a81cb2f0b) Thanks [@andreakiro](https://github.com/andreakiro)! - New package: `notte()`, a browser provider that runs each test attempt in its own [Notte](https://notte.cc) cloud browser session, stops it when the attempt ends, reads `browser.waitForDownload` files back from the session's storage, and stops the sessions of workers that died when the run ends. [Notte browsers](https://e2e.com/docs/integrations/notte)

### [@e2e-dev/moli@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/moli%400.0.1)
<sub>2026-11-19 · yesterday</sub>

> **Patch Changes**
> - [#1843](https://github.com/e2e-inc/e2e/pull/1843) [`29a0261`](https://github.com/e2e-inc/e2e/commit/29a0261775fc362aa26e7ea0fe53e671c864dbc1) Thanks [@ldm0](https://github.com/ldm0)! - Add `moli()` for `web({ browser: moli() })`. Each worker gets a local Moli CDP server with layout and resources enabled, automatic port selection, startup cancellation, and process cleanup when its lease ends.

### [@e2e-dev/testmu@0.0.6](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.6)
<sub>2026-11-19 · yesterday</sub>

> **Patch Changes**
> - [#1859](https://github.com/e2e-inc/e2e/pull/1859) [`e65091b`](https://github.com/e2e-inc/e2e/commit/e65091bbe10b00860ec6240336b57933a7ce65f7) Thanks [@kdy1](https://github.com/kdy1)! - Update agent-device to 0.21.38. Opening an app now waits for the app's first screen before the first capture, and on Android a relaunch accepts a package that Android restarts at once. On iOS, `device.back()` presses the navigation bar's back button when there is one, keyboard dismiss and enter have a bounded idle wait, and agent-device establishes the screen origin of a full-screen private accessibility root.
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - `@e2e-dev/mobile/lease` adds `agentDevicePlugin(entry)`, which checks a provider plugin's version against the engine's agent-device and registers it in a lease daemon's home; `@e2e-dev/testmu` now uses it and needs `@e2e-dev/mobile` 0.12.8 or later. A lease's `device` selector is used to allocate it and no longer goes on the worker's client, since the lease scope already picks the device.

### [@e2e-dev/smol@0.1.4](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.4)
<sub>2026-11-19 · yesterday</sub>

> **Patch Changes**
> - [#1785](https://github.com/e2e-inc/e2e/pull/1785) [`ceaea64`](https://github.com/e2e-inc/e2e/commit/ceaea64ceead09d0a0f8cb5b384ef0d9ffac23a1) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.1 and `@ai-sdk/provider` to 4.0.38. Smol sandboxes use the Playwright 1.65.1 image.
> - [#1965](https://github.com/e2e-inc/e2e/pull/1965) [`60d29cf`](https://github.com/e2e-inc/e2e/commit/60d29cfe4c9d88b00659e0d0e00b8973d61e7391) Thanks [@szymonrybczak](https://github.com/szymonrybczak)! - List the maintainers' `@e2e.com` addresses in `contributors`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(core): run actions sent in the same turn as complete_step (#1983)](https://github.com/e2e-inc/e2e/commit/225ea85e1a6a36589ca87c432d0293c8ed9ede6b) | kdy1 |
| 2026-11-21 | [feat(cli): show --step keys under the summary and view the screen and…](https://github.com/e2e-inc/e2e/commit/23aa697e2627b9c0ee436ea40128b3ee8f682c1c) | satya164 |
| 2026-11-21 | [feat(mobile): add device.isKeyboardShown() (#1893)](https://github.com/e2e-inc/e2e/commit/1d28ac0feac8808d92b2c4e3bf553937be700cb0) | leszko11 |
| 2026-11-21 | [fix(mobile): fail toHaveScreenshot with POLICY_DENIED when a secure f…](https://github.com/e2e-inc/e2e/commit/7a8e546e26a0c08fb0f52f237798c806dd5a611f) | samanyudas |
| 2026-11-21 | [fix(web): drop row, cell, and listitem roles under a presentational t…](https://github.com/e2e-inc/e2e/commit/24e73a20968375757f5e70e488c286d69bc73b50) | JaynouOliver |
| 2026-11-21 | [docs(security): document pages that hide a password field from e2e (#…](https://github.com/e2e-inc/e2e/commit/34d5d744e7bce2cb018dc50fc220bffc1ebe2b5e) | samanyudas |
| 2026-11-21 | [test(e2e): time the redactFragments cost checks in CPU time (#2018)](https://github.com/e2e-inc/e2e/commit/95aac926982efe2b54f18844c3fb63a5489ca379) | samanyudas |
| 2026-11-21 | [chore(deps): bump workspace deps and agent-device to 0.21.41 (#2043)](https://github.com/e2e-inc/e2e/commit/dbb5efef57c10e8e9cc81ed38d0b4ed8c11787d5) | okwasniewski |
| 2026-11-20 | [fix(cache): read CJK counts followed by a copula as counts (#2005)](https://github.com/e2e-inc/e2e/commit/3e7d19de16ea916ddfd761be3909cc873dd08a73) | Toraastrta |
| 2026-11-20 | [fix(changeset): flag test.fixme report compatibility (#2012)](https://github.com/e2e-inc/e2e/commit/31c8221665503f9013f43ebff586b4382aaf635b) | michal-e2e |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
