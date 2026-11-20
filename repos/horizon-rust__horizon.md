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
| ⭐ **Stars** | 11.5k |
| 🍴 **Forks** | 2.0k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.88](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.88) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 844.1 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.88](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.88) — Horizon launcher 0.2.88
<sub>2026-11-20 · today</sub>

> **Fixed**
> - An OpenGL driver crash at start moves Windows players to DirectX 12 or WARP (#18824, fixes #18291)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-20 · 0a875da _(pre-release)_
<sub>2026-11-20 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-20 · 0a875da: main (0a875da), built from `nightly/build-2026-11-20-1` (0a875da91dbb0fdcb7ba8c42c11341aa229af51a).
> Source: commit 0a875da91dbb0fdcb7ba8c42c11341aa229af51a, kept for good as the tag `nightly-source/2026-11-20-0a875da`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - TAA upscaling under a shader pack without a post chain (#18665, fixes #18642)
> …

### [sdk-0a875da91dbb0fdcb7ba8c42c11341aa229af51a](https://github.com/horizon-rust/horizon/releases/tag/sdk-0a875da91dbb0fdcb7ba8c42c11341aa229af51a) — Mod SDK 0a875da91d _(pre-release)_
<sub>2026-11-20 · today</sub>

> Exact-build SDK for 0a875da91dbb0fdcb7ba8c42c11341aa229af51a; sdk.json inventories every asset and SHA256SUMS is signed for sdk-0a875da91dbb0fdcb7ba8c42c11341aa229af51a.

### [launcher@0.2.87](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.87) — Horizon launcher 0.2.87
<sub>2026-11-20 · today</sub>

> **New**
> - Let client mods request a graceful quit (#18561, fixes #18389)
> **Fixed**
> - The window gets a native build's result before the old-build cleanup runs (#18681, fixes #18669)
> **Contributors**
> Thanks to @NikitaMGrimm, @RLC248.
> …

### [launcher@0.2.86](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.86) — Horizon launcher 0.2.86
<sub>2026-11-20 · today</sub>

> **Fixed**
> - A native build prepares its base version instead of asking for a terminal command (#18664, fixes #18659)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [feature(mods): a client mod reads the far terrain's surface past its …](https://github.com/horizon-rust/horizon/commit/ca157af21f79ddbbada7cf44b970913bb4608960) | Teiwazik |
| 2026-11-20 | [feature(mods): player_handshake, read, rewrite and refuse a client's …](https://github.com/horizon-rust/horizon/commit/475677b7ff152a0fbdad9442be98cedd2e594cb9) | Detimes |
| 2026-11-20 | [docs(mods): repin a native mod when its SDK pin stops building (#18955)](https://github.com/horizon-rust/horizon/commit/c84fd8d0884e1d83d9190d2753ba667fe113c389) | UnQuis |
| 2026-11-20 | [Native mod API: name the wearer in GetEnchantmentLevelEvent (#19002)](https://github.com/horizon-rust/horizon/commit/b60f40bdd3e34b0feb0661c8720a7f8402ffd5ba) | UnQuis |
| 2026-11-20 | [Native mod API: an equip sound ItemPart hook with the slot name (#18861)](https://github.com/horizon-rust/horizon/commit/c692a12cfc5f9fbe63f0caecfc2f11f21f3086b4) | UnQuis |
| 2026-11-20 | [fix(mods): a lower crate's mirror keeps the root re-exports its kept …](https://github.com/horizon-rust/horizon/commit/04b92a5b4bc9c56352c9bd9de202f09ab748074e) | ZiQu-dev |
| 2026-11-20 | [feature(mods): the block entities in a box (LevelRef::block_entities)…](https://github.com/horizon-rust/horizon/commit/cf5fc1c2007cf6f9d88449d5b3cc73812e6f6219) | DrDth |
| 2026-11-20 | [feature(mods): command literal words take uppercase letters, as Briga…](https://github.com/horizon-rust/horizon/commit/cae4dd072c376d701aea1b2c92f72c18d43d73e8) | DrDth |
| 2026-11-20 | [feat(mods): a global dispenser_acts hook (#17989)](https://github.com/horizon-rust/horizon/commit/bff7165c73e1b1852e359451cfdd05d7d377f44c) | rdbtCVS |
| 2026-11-20 | [tooling(parity): the prebuild says where its time went (#19025)](https://github.com/horizon-rust/horizon/commit/a6116911fd3e715b58d8aa19196c4b4e27711b8d) | NikitaMGrimm |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
