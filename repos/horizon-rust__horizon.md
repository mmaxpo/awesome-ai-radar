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
| ⭐ **Stars** | 10.1k |
| 🍴 **Forks** | 1.7k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 82% · Python 13% · Java 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.66](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.66) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 508.8 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.66](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.66) — Horizon launcher 0.2.66
<sub>2026-11-15 · today</sub>

> **Fixed**
> - Run four more slow tests in 17 s instead of 40 s (#16484)
> - Skip parsing game files that cannot hold an impl Game (#16505)
> **Contributors**
> Thanks to @kacpherek.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.65](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.65) — Horizon launcher 0.2.65
<sub>2026-11-14 · today</sub>

> **Fixed**
> - Handle non-finite auxiliary frame samples (#15728, fixes #15704)
> - Recognize public IPv6 hosting routes (#15735, fixes #15717)
> - Add bounded streaming download engine (#16274)
> - Disable cmd AutoRun when creating Windows junctions (#15829, fixes #15722)
> **Contributors**
> …

### [launcher@0.2.64](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.64) — Horizon launcher 0.2.64
<sub>2026-11-14 · yesterday</sub>

> **Fixed**
> - Launcher: a native mod's generated main uses the staged revision's allocator (#15807, fixes #15764)
> **Contributors**
> Thanks to @LilleboHaugen.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-13 · 9f42064 _(pre-release)_
<sub>2026-11-13 · 2d ago</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-13 · 9f42064: main (9f42064), built from `nightly/build-2026-11-13-1` (9f42064c11efe7ef3e5ed2baad7ddc2a3b36eea0).
> Source: commit 9f42064c11efe7ef3e5ed2baad7ddc2a3b36eea0, kept for good as the tag `nightly-source/2026-11-13-9f42064`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Native mods: create block entities from the actual state (#11098, fixes #11093)
> …

### [launcher@0.2.63](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.63) — Horizon launcher 0.2.63
<sub>2026-11-13 · 2d ago</sub>

> **Fixed**
> - Launcher: no Windows device names or disguising marks in downloaded file names (#15514)
> **Contributors**
> Thanks to @yahya-nusseibeh.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [execute if stopwatch tests the stopwatch against its range (#16661)](https://github.com/horizon-rust/horizon/commit/a9a30a3b6e3c246747748572e7b10c5fc6b9dc5e) | ilguerro |
| 2026-11-15 | [parity(player): a clip that starts inside an outline keeps the face i…](https://github.com/horizon-rust/horizon/commit/2fb3c979bae5d058f2d711deb5ec2eb9949ba2a0) | denkattt |
| 2026-11-15 | [Trail sprint dust for sprinting mobs, and none for a flying player (#…](https://github.com/horizon-rust/horizon/commit/a7f4daf8dcc2f4f2048e9d5d6b266f14661c0ab9) | ilguerro |
| 2026-11-15 | [Keep the spyglass's look sensitivity to first person and outline far …](https://github.com/horizon-rust/horizon/commit/786f24c7aacfcb188246182e96b7b9815d67a1a8) | ilguerro |
| 2026-11-15 | [Deflate the powder snow box by vanilla's float epsilon (#16627)](https://github.com/horizon-rust/horizon/commit/d1284717c20acfa52f5c1fd16d02cda1df731708) | ilguerro |
| 2026-11-15 | [Read a vibration particle's block destination without its namespace (…](https://github.com/horizon-rust/horizon/commit/d0ec46b5a3d8d97fce55434638d276a8932b26ba) | ilguerro |
| 2026-11-15 | [ci(runners): the whole merge queue runs on the checks runners (#16770)](https://github.com/horizon-rust/horizon/commit/c8aae4660e9d028a013db92d5d65b64768a74c83) | kacpherek |
| 2026-11-15 | [Credit no one for an explosion whose cause is explicitly none (#16617)](https://github.com/horizon-rust/horizon/commit/0b753a27e4528c59ae6a9499da41c405ceacdf84) | ilguerro |
| 2026-11-15 | [Let mobs, items, boats and minecarts tilt a big dripleaf (#16592)](https://github.com/horizon-rust/horizon/commit/0a983a88ed094f50cd20d36666e38a5ff7b9a886) | ilguerro |
| 2026-11-15 | [Let mobs see through powder snow and not through a snow layer's top (…](https://github.com/horizon-rust/horizon/commit/2748619ed89943b75ef6f1e9eed38471c5ffb750) | ilguerro |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
