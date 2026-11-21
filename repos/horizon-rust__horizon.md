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
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.96](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.96) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 841.3 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

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

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-21 · 8f83e5c _(pre-release)_
<sub>2026-11-21 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-21 · 8f83e5c: main (8f83e5c), built from `nightly/build-2026-11-21-1` (8f83e5c85ae3b9a117f742e8d91170c5c9080a06).
> Source: commit 8f83e5c85ae3b9a117f742e8d91170c5c9080a06, kept for good as the tag `nightly-source/2026-11-21-8f83e5c`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - A global dispenser_acts hook (#17989, fixes #17979)
> …

### [sdk-8f83e5c85ae3b9a117f742e8d91170c5c9080a06](https://github.com/horizon-rust/horizon/releases/tag/sdk-8f83e5c85ae3b9a117f742e8d91170c5c9080a06) — Mod SDK 8f83e5c85a _(pre-release)_
<sub>2026-11-21 · today</sub>

> Exact-build SDK for 8f83e5c85ae3b9a117f742e8d91170c5c9080a06; sdk.json inventories every asset and SHA256SUMS is signed for sdk-8f83e5c85ae3b9a117f742e8d91170c5c9080a06.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [bug(launcher): Move Data makes relative links inside the data again o…](https://github.com/horizon-rust/horizon/commit/d291d972b894bd0a16c3b216c4aeada257c33324) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data leaves out the links to other launchers' Min…](https://github.com/horizon-rust/horizon/commit/39491415fa05e87e538d3217371760027b437687) | NikitaMGrimm |
| 2026-11-21 | [bug(rendering): a full video memory no longer ends the game when a fr…](https://github.com/horizon-rust/horizon/commit/14e2417643246551de7f54f0c5683c9e3099e966) | NikitaMGrimm |
| 2026-11-21 | [bug(launcher): Move Data leaves out the game's cache instead of stopp…](https://github.com/horizon-rust/horizon/commit/f037744a79f9982c47876f49c5a3067279f88706) | NikitaMGrimm |
| 2026-11-21 | [tooling(ci): a pull request's prebuild gives the compile turn back to…](https://github.com/horizon-rust/horizon/commit/1b2146314f197dbf137dd3efe693cb00f4e417d7) | NikitaMGrimm |
| 2026-11-21 | [tooling(ci): environment_render, lan_auth and source_silence leave kn…](https://github.com/horizon-rust/horizon/commit/f6628e77f1e16b6350addd4448ff61d305551675) | NikitaMGrimm |
| 2026-11-21 | [bug(prepare): an exporter JVM that stops early says how (#19388)](https://github.com/horizon-rust/horizon/commit/0d6185beb986bc27062e9ac1d2ed2dd287f28b0d) | NikitaMGrimm |
| 2026-11-21 | [feature(mods): a mod drives replay playback (open, pause, seek, speed…](https://github.com/horizon-rust/horizon/commit/25b4d89fb13a0a1fc6f0cd366bb6cd9dd47bee5a) | NikitaMGrimm |
| 2026-11-21 | [bug(fonts): a huge TrueType glyph or space advance in a pack font is …](https://github.com/horizon-rust/horizon/commit/9387019b6aac65639f73ce4f90f5505381cd16ce) | sushanth-dev |
| 2026-11-21 | [tests(launcher): the cleanup test unlocks the update lock before clos…](https://github.com/horizon-rust/horizon/commit/09a272db1959ec570ef2c79f2c3c6836a3840ad5) | NikitaMGrimm |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
