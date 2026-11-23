# horizon-rust/horizon

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/horizon-rust/horizon)

> Minecraft 26.3 rewritten in Rust.

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
| ⭐ **Stars** | 11.8k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.6k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.107](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.107) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 861.3 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.107](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.107) — Horizon launcher 0.2.107
<sub>2026-11-22 · today</sub>

> **Fixed**
> - Don't parse a Java instance's game command as Horizon arguments (#19911, fixes #19719)
> **Contributors**
> Thanks to @Juanpalai.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.106](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.106) — Horizon launcher 0.2.106
<sub>2026-11-22 · today</sub>

> **Fixed**
> - A mod made for a newer game says to update the instance (#19818)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-22 · f1bb66f _(pre-release)_
<sub>2026-11-22 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-22 · f1bb66f: main (f1bb66f), built from `nightly/build-2026-11-22-2` (f1bb66f353cf67f2aa4665293fc75c8d91186fc7).
> Source: commit f1bb66f353cf67f2aa4665293fc75c8d91186fc7, kept for good as the tag `nightly-source/2026-11-22-f1bb66f`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Let native mods record named profiling scopes (#18678, fixes #18672)
> …

### [sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7](https://github.com/horizon-rust/horizon/releases/tag/sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7) — Mod SDK f1bb66f353 _(pre-release)_
<sub>2026-11-22 · today</sub>

> Exact-build SDK for f1bb66f353cf67f2aa4665293fc75c8d91186fc7; sdk.json inventories every asset and SHA256SUMS is signed for sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7.

### [launcher@0.2.105](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.105) — Horizon launcher 0.2.105
<sub>2026-11-22 · yesterday</sub>

> **New**
> - Native mod API: pre and committed hooks for a mod's own equipment slots (#19012, fixes #19011)
> **Fixed**
> - Stage marked trait methods in lower crates (#19700, fixes #19423)
> - A_replaced_binary_is_replaced_again_at_its_path sets its swapped-in file to 0644 (#19739, fixes #19730)
> - Align Mods and Packs filter drawer with Modrinth and instance rules (#19793)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [bug(client): the crash report scrubber knows the player's name (#20219)](https://github.com/horizon-rust/horizon/commit/ac51b9859d87a34c35fb1a6ccf15f27f49a2c52c) | DUzzL |
| 2026-11-23 | [perf(render): +22.6% to +37.7% stress BE FPS (+2.9% village) via sing…](https://github.com/horizon-rust/horizon/commit/432d764acb1694686bce1863cda0dbae83d9acb4) | sl4ppleware |
| 2026-11-23 | [perf(commands): each function tag is expanded once, without recursion…](https://github.com/horizon-rust/horizon/commit/8af680316d266a8b87fc4893f5c6754002a715e5) | DUzzL |
| 2026-11-23 | [bug(launcher): size the pictures of packs, worlds and listed servers …](https://github.com/horizon-rust/horizon/commit/5b143935f0f1bd0a39799391666aeab249f0e5c4) | DUzzL |
| 2026-11-23 | [bug(rendering): a font named again and again through references is re…](https://github.com/horizon-rust/horizon/commit/1695538566da106c7d961b1fc44d776668b25a78) | DUzzL |
| 2026-11-23 | [tooling(saves): reproducible save/load and pure-Rust codec benchmark,…](https://github.com/horizon-rust/horizon/commit/492ec76efee5af6ff25b17d273697a52e64acfc9) | jvz-devx |
| 2026-11-23 | [perf(worldgen): bounded per-worker CompiledSurfaceRule variant cache …](https://github.com/horizon-rust/horizon/commit/211e07fc54d8aa5bdf3deb879b2f3ac460186c8d) | sl4ppleware |
| 2026-11-23 | [bug(mods): a biome region in another namespace its mod owns is refuse…](https://github.com/horizon-rust/horizon/commit/4e0ae69f8fb37868c041082550dde435969fe3a0) | abuzar310 |
| 2026-11-23 | [tooling(worlds): anvil_dump.py and world_compare.py read a chunk stor…](https://github.com/horizon-rust/horizon/commit/a0553e5795bc6100204c34d5f71ccc965bda4fd9) | abuzar310 |
| 2026-11-23 | [bug(options): an escaped surrogate pair in options.txt is read as one…](https://github.com/horizon-rust/horizon/commit/23d2949b2514805cb1bd61fff1f2fabae50291af) | abuzar310 |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
