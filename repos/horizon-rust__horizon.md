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
| ⭐ **Stars** | 9.6k |
| 🍴 **Forks** | 1.6k |
| 🐞 **Open issues + PRs** | [1.1k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 82% · Python 13% · Java 5% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.64](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.64) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 500.7 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.64](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.64) — Horizon launcher 0.2.64
<sub>2026-11-14 · today</sub>

> **Fixed**
> - Launcher: a native mod's generated main uses the staged revision's allocator (#15807, fixes #15764)
> **Contributors**
> Thanks to @LilleboHaugen.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-13 · 9f42064 _(pre-release)_
<sub>2026-11-13 · yesterday</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-13 · 9f42064: main (9f42064), built from `nightly/build-2026-11-13-1` (9f42064c11efe7ef3e5ed2baad7ddc2a3b36eea0).
> Source: commit 9f42064c11efe7ef3e5ed2baad7ddc2a3b36eea0, kept for good as the tag `nightly-source/2026-11-13-9f42064`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Native mods: create block entities from the actual state (#11098, fixes #11093)
> …

### [launcher@0.2.63](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.63) — Horizon launcher 0.2.63
<sub>2026-11-13 · yesterday</sub>

> **Fixed**
> - Launcher: no Windows device names or disguising marks in downloaded file names (#15514)
> **Contributors**
> Thanks to @yahya-nusseibeh.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.62](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.62) — Horizon launcher 0.2.62
<sub>2026-11-12 · 2d ago</sub>

> **New**
> - The performance capture platform: /profiler, .hzperf captures and horizon-perf (#15361)
> **Fixed**
> - Launcher: bound the sign-in services' interval and lifetimes (#15419)
> - launcher: fall back to IPv4 when IPv6 to Microsoft sign-in is dead (#15021, fixes #15013)
> - Launcher: a folder with 26.3's version file but not its game says to play 26.3 once (#14771, fixes #14286)
> …

### [launcher@0.2.61](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.61) — Horizon launcher 0.2.61
<sub>2026-11-12 · 2d ago</sub>

> **Fixed**
> - Launcher: uninstall deletes the data of a moved data location (#14567, fixes #14565)
> - Launcher: review and complete Thai translations (th.json) (#14361)
> - Launcher: follow links above the data folder when moving it (#15420)
> - Friends: try every endpoint that answers before giving up on a direct join (#15231)
> - Port-pack: licence text stays one comment line, and families match whole words (#15248)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [Merge pull request #16504 from kacpherek/tooling/merge-test-binaries](https://github.com/horizon-rust/horizon/commit/ec85e818d88dd530aa9a4f4b4a84e92ff163be64) | kacpherek |
| 2026-11-14 | [Merge pull request #16501 from kacpherek/tooling/ci-build-only-changes](https://github.com/horizon-rust/horizon/commit/1adfa1477852ae0481bb10091ceac89c5eb96d7c) | kacpherek |
| 2026-11-14 | [tooling(tests): link each crate's integration tests into one binary](https://github.com/horizon-rust/horizon/commit/d34ed427ed6d60e4919faafe67f4a626bae414b9) | kacpherek |
| 2026-11-14 | [tooling(ci): skip the second verify of a commit the merge queue alrea…](https://github.com/horizon-rust/horizon/commit/08507f1e10a0da5d13ff770c541fc4f14f6dec43) | kacpherek |
| 2026-11-14 | [tooling(ci): skip the launcher job when a merge-queue or main range l…](https://github.com/horizon-rust/horizon/commit/809bc7e54f517a9b6fe758be905f0d9561bddc02) | kacpherek |
| 2026-11-14 | [tooling(ci): reuse compiled workspace crates in the lint job on pull …](https://github.com/horizon-rust/horizon/commit/96ee1dc5882569a8e99ff4c0a1d431a09445a0fc) | kacpherek |
| 2026-11-14 | [tooling(ci): link verify's Rust tests with mold](https://github.com/horizon-rust/horizon/commit/7ffaa0d9180a2402a87f9baec11270066a2afd8b) | kacpherek |
| 2026-11-14 | [tooling(ci): keep built workspace crates between runs so a pull reque…](https://github.com/horizon-rust/horizon/commit/3e93adb19bc2af2c5e37a77d29eeac70bc6ca781) | kacpherek |
| 2026-11-14 | [tooling(ci): share verify's sccache through GitHub's cache from main](https://github.com/horizon-rust/horizon/commit/d83d93b68358b6c9ea8164de099b62f16a306900) | kacpherek |
| 2026-11-14 | [Merge pull request #16483 from kacpherek/tooling/ci-sccache-tests](https://github.com/horizon-rust/horizon/commit/a51b2d41054b13bee18834b5fb0af37eff32eeed) | kacpherek |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
