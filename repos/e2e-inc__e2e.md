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
| 🍴 **Forks** | 789 |
| 🐞 **Open issues + PRs** | [132](https://github.com/e2e-inc/e2e/issues) |
| 💻 **Languages** | TypeScript 99% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `e2e` `e2e-testing` `end-to-end-testing` `mobile` `mobile-testing` `playwright` `web` `ai-testing` `automation-testing` `qa` `test-automation` `testing` `testing-framework` `testing-tools` `ui-testing` `agentic-testing` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-07-22 |
| 📦 **Latest release** | [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 124.1 MB |
| 🌐 **Website** | https://e2e.com |

## 📦 Recent releases

### [@e2e-dev/revyl@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/revyl%400.0.1)
<sub>2026-11-19 · 4d ago</sub>

> **Patch Changes**
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - Add `@e2e-dev/revyl`: `revyl({ app, device, osVersion })` runs mobile targets on Revyl's hosted iOS simulators and Android emulators, one device per worker slot, through agent-device's `@agent-device/revyl` plugin. Set `REVYL_API_KEY` in the run environment; Revyl installs the build from the `https` `app` URL. Needs `@e2e-dev/mobile` 0.12.8 or later.

### [@e2e-dev/notte@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/notte%400.0.1)
<sub>2026-11-19 · 4d ago</sub>

> **Patch Changes**
> - [#1726](https://github.com/e2e-inc/e2e/pull/1726) [`9602daa`](https://github.com/e2e-inc/e2e/commit/9602daa9602444673b99ef6aaa33c67a81cb2f0b) Thanks [@andreakiro](https://github.com/andreakiro)! - New package: `notte()`, a browser provider that runs each test attempt in its own [Notte](https://notte.cc) cloud browser session, stops it when the attempt ends, reads `browser.waitForDownload` files back from the session's storage, and stops the sessions of workers that died when the run ends. [Notte browsers](https://e2e.com/docs/integrations/notte)

### [@e2e-dev/moli@0.0.1](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/moli%400.0.1)
<sub>2026-11-19 · 4d ago</sub>

> **Patch Changes**
> - [#1843](https://github.com/e2e-inc/e2e/pull/1843) [`29a0261`](https://github.com/e2e-inc/e2e/commit/29a0261775fc362aa26e7ea0fe53e671c864dbc1) Thanks [@ldm0](https://github.com/ldm0)! - Add `moli()` for `web({ browser: moli() })`. Each worker gets a local Moli CDP server with layout and resources enabled, automatic port selection, startup cancellation, and process cleanup when its lease ends.

### [@e2e-dev/testmu@0.0.6](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/testmu%400.0.6)
<sub>2026-11-19 · 4d ago</sub>

> **Patch Changes**
> - [#1859](https://github.com/e2e-inc/e2e/pull/1859) [`e65091b`](https://github.com/e2e-inc/e2e/commit/e65091bbe10b00860ec6240336b57933a7ce65f7) Thanks [@kdy1](https://github.com/kdy1)! - Update agent-device to 0.21.38. Opening an app now waits for the app's first screen before the first capture, and on Android a relaunch accepts a package that Android restarts at once. On iOS, `device.back()` presses the navigation bar's back button when there is one, keyboard dismiss and enter have a bounded idle wait, and agent-device establishes the screen origin of a full-screen private accessibility root.
> - [#1958](https://github.com/e2e-inc/e2e/pull/1958) [`ad641be`](https://github.com/e2e-inc/e2e/commit/ad641beeaca6ee56a251bdc0abde8053b0b0ee7c) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Update agent-device to 0.21.39. Android taps and key presses no longer wait for global animations, and screenshots on Android and single-panel iOS simulators read rotation without an extra round trip.
> - [#1708](https://github.com/e2e-inc/e2e/pull/1708) [`f659d64`](https://github.com/e2e-inc/e2e/commit/f659d64d80cbb484f539681a6bf72f5047854a99) Thanks [@KayaanT](https://github.com/KayaanT)! - `@e2e-dev/mobile/lease` adds `agentDevicePlugin(entry)`, which checks a provider plugin's version against the engine's agent-device and registers it in a lease daemon's home; `@e2e-dev/testmu` now uses it and needs `@e2e-dev/mobile` 0.12.8 or later. A lease's `device` selector is used to allocate it and no longer goes on the worker's client, since the lease scope already picks the device.

### [@e2e-dev/smol@0.1.4](https://github.com/e2e-inc/e2e/releases/tag/%40e2e-dev/smol%400.1.4)
<sub>2026-11-19 · 4d ago</sub>

> **Patch Changes**
> - [#1785](https://github.com/e2e-inc/e2e/pull/1785) [`ceaea64`](https://github.com/e2e-inc/e2e/commit/ceaea64ceead09d0a0f8cb5b384ef0d9ffac23a1) Thanks [@okwasniewski](https://github.com/okwasniewski)! - Bump playwright-core to 1.65.1 and `@ai-sdk/provider` to 4.0.38. Smol sandboxes use the Playwright 1.65.1 image.
> - [#1965](https://github.com/e2e-inc/e2e/pull/1965) [`60d29cf`](https://github.com/e2e-inc/e2e/commit/60d29cfe4c9d88b00659e0d0e00b8973d61e7391) Thanks [@szymonrybczak](https://github.com/szymonrybczak)! - List the maintainers' `@e2e.com` addresses in `contributors`.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [feat(mcp): run JavaScript in run_code (#1998)](https://github.com/e2e-inc/e2e/commit/7afe2ea34aba17153c9b968b9fe5ad5b7cf9097b) | okwasniewski |
| 2026-11-23 | [fix(html-reporter): show names as written instead of lowercasing them…](https://github.com/e2e-inc/e2e/commit/74904fcbfdefc27be8db0fffa73a3af8a92fb6d0) | okwasniewski |
| 2026-11-23 | [chore(dev): PR description as source of truth, pnpm record:terminal (…](https://github.com/e2e-inc/e2e/commit/f6172e7654c483d77250e79c004abdc484046dde) | okwasniewski |
| 2026-11-23 | [docs(examples): list 14 more open source projects testing with e2e (#…](https://github.com/e2e-inc/e2e/commit/1f9321694fe35a664a3de17e124c32227cef02cf) | okwasniewski |
| 2026-11-23 | [feat(init): pick an example from a list with a bare --example (#2104)](https://github.com/e2e-inc/e2e/commit/02cf99bea4808571b04009ebb87bb8cc9a9886ea) | okwasniewski |
| 2026-11-23 | [perf(core): paint screenshot masks up to 20x faster, compare identica…](https://github.com/e2e-inc/e2e/commit/58f3d45a6d5b280ae4d169a471accb424e7c20e3) | KrzysztofMoch |
| 2026-11-23 | [feat(reporters)!: one live hook, interactive flag, and pause events (…](https://github.com/e2e-inc/e2e/commit/cd811a4254c137ffeb50043f6402e4b78ce0505c) | okwasniewski |
| 2026-11-23 | [fix(acp): sign Codex in with an API key and redact provider keys (#2062)](https://github.com/e2e-inc/e2e/commit/1ece4df43b2fb48ccb04240fc64eeb6189ba72ca) | michal-e2e |
| 2026-11-23 | [fix(desktop): fix reads, ids, input, and screenshots found in a secon…](https://github.com/e2e-inc/e2e/commit/202f1216673f16a194f42b10e1d6ff85671d1288) | kdy1 |
| 2026-11-23 | [ci: install Chromium's cached apt packages without apt-get update (#2…](https://github.com/e2e-inc/e2e/commit/970b74ed4cb385ef30aa5c0444a91ed16cb4374c) | kdy1 |

[See all commits ↗](https://github.com/e2e-inc/e2e/commits)

## ⬇️ Get it

```bash
git clone https://github.com/e2e-inc/e2e.git
```
