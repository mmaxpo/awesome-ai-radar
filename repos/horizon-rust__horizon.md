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
| ⭐ **Stars** | 11.7k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.5k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.103](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.103) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 850.3 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.103](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.103) — Horizon launcher 0.2.103
<sub>2026-11-22 · today</sub>

> **Fixed**
> - Prebuilt_game's archives store no group or other write bits, whatever the umask (#18501, fixes #18500)
> **Contributors**
> Thanks to @maaz7409.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.102](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.102) — Horizon launcher 0.2.102
<sub>2026-11-22 · today</sub>

> **New**
> - Restore Modrinth for Resource, Shader, and Data Packs with per-kind filtering (#19628, fixes #19618)
> - Expose raw text and let player commands validate their arguments (#18661, fixes #17985)
> **Fixed**
> - Refuse [[inject]] manifests and remove its consumers (#19625)
> - Check a bundled pack's replaced package before a reload mounts it (#19314, fixes #18653)
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-22 · 2b77287 _(pre-release)_
<sub>2026-11-22 · today</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-22 · 2b77287: main (2b77287), built from `nightly/build-2026-11-22-1` (2b77287de099c9316278ba7ac4d83590fdb7ef30).
> Source: commit 2b77287de099c9316278ba7ac4d83590fdb7ef30, kept for good as the tag `nightly-source/2026-11-22-2b77287`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - A forward replay seek plays on instead of rebuilding the world (#19395) (#19452)
> …

### [sdk-2b77287de099c9316278ba7ac4d83590fdb7ef30](https://github.com/horizon-rust/horizon/releases/tag/sdk-2b77287de099c9316278ba7ac4d83590fdb7ef30) — Mod SDK 2b77287de0 _(pre-release)_
<sub>2026-11-22 · today</sub>

> Exact-build SDK for 2b77287de099c9316278ba7ac4d83590fdb7ef30; sdk.json inventories every asset and SHA256SUMS is signed for sdk-2b77287de099c9316278ba7ac4d83590fdb7ef30.

### [launcher@0.2.101](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.101) — Horizon launcher 0.2.101
<sub>2026-11-22 · today</sub>

> **Fixed**
> - A retry of Move Data works in the same folder, and never touches a staging folder it didn't create (#19613)
> - RuntimeLevels::reset_vanilla regenerates the vanilla dimensions from a new seed (#18369) (#18379, fixes #18369)
> - Move Data shows its steps in a window of its own (#19619, fixes #19607)
> **Contributors**
> Thanks to @NikitaMGrimm, @ZiQu-dev.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [feature(mods): video export mod API (#19310 PR C) (#19750)](https://github.com/horizon-rust/horizon/commit/c814ab2ab6f0432b79f18a70b8af7b5cea82dc9d) | NikitaMGrimm |
| 2026-11-22 | [tooling(tests): mod-vocab's wire depth tests give their thread a Wind…](https://github.com/horizon-rust/horizon/commit/b2a84d21e83fc0d497902e664a6fdf07da7c1794) | Ragbie |
| 2026-11-22 | [tooling: wire_layout_tests.rs is rustfmt-clean, so format_scan passes…](https://github.com/horizon-rust/horizon/commit/3ec9e732d92674782491c372c04fb25706ca3ef6) | HamasakiBrain |
| 2026-11-22 | [bug(items): a stack's own glider component reaches the client (#19755)](https://github.com/horizon-rust/horizon/commit/7eda8519e4d5b17dbc17e9e2a195e436cf060a52) | HamasakiBrain |
| 2026-11-22 | [docs(benchmark): the A/B example passes horizon-perf summary the newe…](https://github.com/horizon-rust/horizon/commit/3a0c68c1c9d5ce67d63f032f0b148b09d7197aad) | maaz7409 |
| 2026-11-22 | [Shader packs: a storage image binds a float texture its qualifier onl…](https://github.com/horizon-rust/horizon/commit/322774f158d5e395d5cd8fc61085b15f75f005a4) | maaz7409 |
| 2026-11-22 | [bug(render): resource pack core shaders are used again, negative heig…](https://github.com/horizon-rust/horizon/commit/b357c5c4b2d40aa0ec38841841c6b6360954d7a0) | DomiIRL |
| 2026-11-22 | [perf(render): GPU compute meshlet culling and Visbuffer mesh shader s…](https://github.com/horizon-rust/horizon/commit/45eeccded1f65397833686818f589d81b579ecbc) | liqttt |
| 2026-11-22 | [docs(benchmark): the A/B section reads its result with horizon-perf s…](https://github.com/horizon-rust/horizon/commit/3465b5f7ac98ae1b6cd0d1acb52e57478e7bf1c4) | maaz7409 |
| 2026-11-22 | [perf(rendering): worker-thread meshlets, occlusion culling, indirect …](https://github.com/horizon-rust/horizon/commit/a27fee23ca32b659220f5d27e8b7ba50ab420582) | liqttt |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
