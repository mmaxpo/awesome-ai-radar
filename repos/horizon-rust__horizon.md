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
| ⭐ **Stars** | 11.2k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.78](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.78) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 828.5 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.78](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.78) — Horizon launcher 0.2.78
<sub>2026-11-18 · today</sub>

> **Fixed**
> - The storage report no longer fails on the links the game makes in its cache (#18144, fixes #17911)
> **Contributors**
> Thanks to @abuzar310.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.77](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.77) — Horizon launcher 0.2.77
<sub>2026-11-18 · today</sub>

> **Fixed**
> - The window never waits for the game to say its shader API (#18155)
> - List imported modpacks without reading their mods on the window thread (#18161)
> - The migration lock is released before its file closes (#18143, fixes #18138)
> **Contributors**
> Thanks to @NikitaMGrimm, @abuzar310.
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-18 · 0b14f8a _(pre-release)_
<sub>2026-11-18 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-18 · 0b14f8a: main (0b14f8a), built from `nightly/build-2026-11-18-1` (0b14f8acfd97fa2c750e42795249dcc981178ca4).
> Source: commit 0b14f8acfd97fa2c750e42795249dcc981178ca4, kept for good as the tag `nightly-source/2026-11-18-0b14f8a`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Graphics: a Full Performance preset, and every preset a fixed table (#15700)
> …

### [sdk-0b14f8acfd97fa2c750e42795249dcc981178ca4](https://github.com/horizon-rust/horizon/releases/tag/sdk-0b14f8acfd97fa2c750e42795249dcc981178ca4) — Mod SDK 0b14f8acfd _(pre-release)_
<sub>2026-11-18 · today</sub>

> Exact-build SDK for 0b14f8acfd97fa2c750e42795249dcc981178ca4; sdk.json inventories every asset and SHA256SUMS is signed for sdk-0b14f8acfd97fa2c750e42795249dcc981178ca4.

### [launcher@0.2.76](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.76) — Horizon launcher 0.2.76
<sub>2026-11-18 · today</sub>

> **Fixed**
> - Keep content the game refuses out of the carry (#18067, fixes #18063)
> - Remove stale patch-applied dir before running horizon-mixins (#17959, fixes #17931)
> **Contributors**
> Thanks to @DrDth, @Rocklarper.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [refactor(gameplay): Wave 3, ExecutionRole and Dim move to horizon-gam…](https://github.com/horizon-rust/horizon/commit/44afc8241d9a531de15a57a70e064fe9b079692b) | kacpherek |
| 2026-11-18 | [refactor(gameplay): Wave 3, villager logic runs on a VillagerLevel tr…](https://github.com/horizon-rust/horizon/commit/1d2c106e3b62efb41307ee67ee56e109fbfd7c9e) | kacpherek |
| 2026-11-18 | [feature(mods): set a server player's velocity (#17907)](https://github.com/horizon-rust/horizon/commit/ef956993e1fe8900b56a18f86a870c4905fdd6f2) | Detimes |
| 2026-11-18 | [feature(mods): PlayerRef::connect_address gives the host and port the…](https://github.com/horizon-rust/horizon/commit/90a3dec839ef77edfcc6a25eb47cf5e5e532190f) | RsMan-Dev |
| 2026-11-18 | [feature(mods): mob_reset_goals gives a loaded mob the goals of a new …](https://github.com/horizon-rust/horizon/commit/e0bacd674621f85c4ed102806da85c29a3de3a59) | RsMan-Dev |
| 2026-11-18 | [bug(launcher): Play says which step it's on before the game starts (#…](https://github.com/horizon-rust/horizon/commit/7df554e918c73fd9a804b62839b870f65aaa1352) | NikitaMGrimm |
| 2026-11-18 | [refactor(gameplay): /time, /weather, /gamerule and /help run on comma…](https://github.com/horizon-rust/horizon/commit/bf6e27f92433d5a5e130b98da0a62ebf360cae04) | kacpherek |
| 2026-11-18 | [tooling(state-digest): an extended scene, and a LAN host digest that …](https://github.com/horizon-rust/horizon/commit/a96db09075a0f7f9a97c666044bdf75c88f34e0c) | kacpherek |
| 2026-11-18 | [tooling(game): list what a function uses on Game (#18188)](https://github.com/horizon-rust/horizon/commit/a0f94090bbe9a4a431b8da4b8b4d384e0ac858e8) | kacpherek |
| 2026-11-18 | [refactor(gameplay): Wave 3, minecart state and rules move to horizon-…](https://github.com/horizon-rust/horizon/commit/066250ec573ed516dc10dcd3f3b44071bba5062b) | kacpherek |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
