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
| ⭐ **Stars** | 11.4k |
| 🍴 **Forks** | 1.9k |
| 🐞 **Open issues + PRs** | [1.2k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.81](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.81) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.1 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.81](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.81) — Horizon launcher 0.2.81
<sub>2026-11-19 · today</sub>

> **New**
> - A mouse wheel's notch glides instead of jumping (#16541, fixes #16531)
> **Fixed**
> - Match vanilla server address IDN handling (#17430, fixes #16928)
> - Allow spaces and Unicode when moving data (#17863, fixes #17757)
> - Wasm mods keep loading when the mod API only grows (#18357, fixes #18253)
> …

### [launcher@0.2.80](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.80) — Horizon launcher 0.2.80
<sub>2026-11-19 · today</sub>

> **Fixed**
> - Carry mods' own biome modifier types as NeoForge's where their fields say enough (#18292, fixes #18285)
> **Contributors**
> Thanks to @DrDth.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.79](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.79) — Horizon launcher 0.2.79
<sub>2026-11-18 · today</sub>

> **Fixed**
> - Make the download sign-in diagnostic self-contained (#17829, fixes #17746)
> - Prepare uses the Microsoft Store launcher's Java (#16853, fixes #16849)
> - Carry predicate files in 26.3's shape (#18195, fixes #18194)
> - Format the generated points, so clippy stops scanning 8 MB lines (#18202)
> - Play says which step it's on before the game starts (#18252)
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-18 · dd67b76 _(pre-release)_
<sub>2026-11-19 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-18 · dd67b76: main (dd67b76), built from `nightly/build-2026-11-18-5` (dd67b76ff23e28c6d8e21859df600d31572f81a0).
> Source: commit dd67b76ff23e28c6d8e21859df600d31572f81a0, kept for good as the tag `nightly-source/2026-11-18-dd67b76`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Set a player's name in the Tab list only (#17884, fixes #17843)
> …

### [sdk-dd67b76ff23e28c6d8e21859df600d31572f81a0](https://github.com/horizon-rust/horizon/releases/tag/sdk-dd67b76ff23e28c6d8e21859df600d31572f81a0) — Mod SDK dd67b76ff2 _(pre-release)_
<sub>2026-11-19 · today</sub>

> Exact-build SDK for dd67b76ff23e28c6d8e21859df600d31572f81a0; sdk.json inventories every asset and SHA256SUMS is signed for sdk-dd67b76ff23e28c6d8e21859df600d31572f81a0.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [parity(rendering,items): normalize minecraft:component select matchin…](https://github.com/horizon-rust/horizon/commit/a38f2f8b600cb899db5f0fee6a60f66ad6632d06) | FitchWorks |
| 2026-11-19 | [perf(mobs): search a target among the slots of its species, not every…](https://github.com/horizon-rust/horizon/commit/a82b6173e5ee0552b48ae6538a2adb2497a6256f) | RsMan-Dev |
| 2026-11-19 | [perf(creative): index stack deduplication during tab rebuilds (#18459)](https://github.com/horizon-rust/horizon/commit/35182ca4655b1526cad86868c5cb22bdd0a7283d) | nekotxs |
| 2026-11-19 | [Make a guardian stroll when its beam ends and an allay wander ten blo…](https://github.com/horizon-rust/horizon/commit/0dbee9533023c39f9a09f7ede9341cf32a31f1b5) | ilguerro |
| 2026-11-19 | [perf(datafix): index wide JSON objects while parsing (#18443)](https://github.com/horizon-rust/horizon/commit/bc6bc483a80e9b78d3d0ce86fde3ae8021d25e93) | nekotxs |
| 2026-11-19 | [tooling(cargo): horizon-bench, horizon-prepare and horizon-theme inhe…](https://github.com/horizon-rust/horizon/commit/89d2817ac41a30bb442a834edd90691432396541) | Bl4ckspell7 |
| 2026-11-19 | [bug(launcher): a Java instance no longer shows Horizon's Update butto…](https://github.com/horizon-rust/horizon/commit/ee695b4f47d71e1b0b845471f0f2b34a82d535c6) | plantrungnampl |
| 2026-11-19 | [tooling(mods): a malformed internals entry's error names its index an…](https://github.com/horizon-rust/horizon/commit/716961b24de29a71ed6ecb99412cbe3a28ff3552) | NikitaMGrimm |
| 2026-11-19 | [docs(mods): cargo horizon-mod update moves a wasm mod's pin too (#18481)](https://github.com/horizon-rust/horizon/commit/16e7495cb2ea65a0f4c029dae09c39f348b203ee) | NikitaMGrimm |
| 2026-11-19 | [parity(blocks): run block events and random ticks inside handlingTick…](https://github.com/horizon-rust/horizon/commit/d10c93f45a84d42b9742d2cd5d6fb2017fc00c65) | Keel0n |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
