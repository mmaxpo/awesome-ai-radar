# horizon-rust/horizon

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/horizon-rust/horizon)

> Minecraft: Java Edition 26.3 rewritten from scratch in Rust, checked against vanilla with 281 differential harnesses. Get it with the Horizon launcher.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Minecraft Java Edition server rewritten in Rust |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 11.6k |
| 🍴 **Forks** | 2.0k |
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.98](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.98) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.4 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.98](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.98) — Horizon launcher 0.2.98
<sub>2026-11-21 · today</sub>

> **Fixed**
> - Move Data makes relative links inside the data again on Unix (#19435)
> - Move Data makes the server runtime's links again for the same release (#19438, fixes #19430)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.97](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.97) — Horizon launcher 0.2.97
<sub>2026-11-21 · today</sub>

> **Fixed**
> - Move Data leaves out the game's cache instead of stopping at its links (#19425, fixes #19414)
> - Move Data leaves out the links to other launchers' Minecraft files (#19433)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.96](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.96) — Horizon launcher 0.2.96
<sub>2026-11-21 · today</sub>

> **New**
> - A mod drives replay playback (open, pause, seek, speed, state) (#19247) (#19374, fixes #19247)
> **Fixed**
> - An exporter JVM that stops early says how (#19388)
> **Contributors**
> Thanks to @NikitaMGrimm.
> …

### [launcher@0.2.95](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.95) — Horizon launcher 0.2.95
<sub>2026-11-21 · today</sub>

> **Fixed**
> - tests(launcher): the cleanup test unlocks the update lock before closing it (#19375)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.94](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.94) — Horizon launcher 0.2.94
<sub>2026-11-21 · today</sub>

> **Fixed**
> - Stop cancels native tool/SDK downloads immediately and shows feedback (#19300) (#19313, fixes #19300)
> - Build waits for a busy native cache instead of failing (#19294) (#19303, fixes #19294)
> - A deleted version or an incomplete Minecraft folder no longer stops Prepare (#19328)
> - Exit 78, storage and Intel Mac refusals say what to do (#19334)
> - tests(launcher): the app bundle test runs on hosted Macs (#19355, fixes #19351)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [bug(mods): a game with native mods keeps Play with Friends and Horizo…](https://github.com/horizon-rust/horizon/commit/f618858113f0c3a10679072870951dee22c133ea) | NikitaMGrimm |
| 2026-11-21 | [bug(client): a control screenshot no frame takes fails after 5 s and …](https://github.com/horizon-rust/horizon/commit/f2c19ed9ea5797cb8907a0c24369cce4ad047461) | NikitaMGrimm |
| 2026-11-21 | [feature(mods): a forward replay seek plays on instead of rebuilding t…](https://github.com/horizon-rust/horizon/commit/47fe02b7b3fc20d6994de9e3ab17fde4ebae3404) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data makes the server runtime's links again for t…](https://github.com/horizon-rust/horizon/commit/2e4fe0c5cd47c14dbb02a1afc8dd48b50b07322d) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data makes relative links inside the data again o…](https://github.com/horizon-rust/horizon/commit/d291d972b894bd0a16c3b216c4aeada257c33324) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data leaves out the links to other launchers' Min…](https://github.com/horizon-rust/horizon/commit/39491415fa05e87e538d3217371760027b437687) | NikitaMGrimm |
| 2026-11-21 | [bug(rendering): a full video memory no longer ends the game when a fr…](https://github.com/horizon-rust/horizon/commit/14e2417643246551de7f54f0c5683c9e3099e966) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data leaves out the game's cache instead of stopp…](https://github.com/horizon-rust/horizon/commit/f037744a79f9982c47876f49c5a3067279f88706) | NikitaMGrimm |
| 2026-11-21 | [tooling(ci): a pull request's prebuild gives the compile turn back to…](https://github.com/horizon-rust/horizon/commit/1b2146314f197dbf137dd3efe693cb00f4e417d7) | NikitaMGrimm |
| 2026-11-21 | [tooling(ci): environment_render, lan_auth and source_silence leave kn…](https://github.com/horizon-rust/horizon/commit/f6628e77f1e16b6350addd4448ff61d305551675) | NikitaMGrimm |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
