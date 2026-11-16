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
| ⭐ **Stars** | 10.5k |
| 🍴 **Forks** | 1.8k |
| 🐞 **Open issues + PRs** | [1.3k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.69](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.69) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 825.2 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.69](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.69) — Horizon launcher 0.2.69
<sub>2026-11-16 · today</sub>

> **Fixed**
> - Port ledger: fix 1 stale citation in horizon-port-pack (#16881)
> - Change Horizon's licence from MIT to LGPL-3.0-or-later (#17111)
> **Contributors**
> Thanks to @MSedgeMC, @kacpherek.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.68](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.68) — Horizon launcher 0.2.68
<sub>2026-11-15 · today</sub>

> **New**
> - Arrows show and scroll the top bar's hidden tabs (#16580, fixes #16577)
> **Fixed**
> - Release notes draw only the rows in view (#16558, fixes #16557)
> - fix traduction launcher (#16847)
> - Name --prism-dir in the missing-files hint (#16895, fixes #16891)
> …

### [launcher@0.2.67](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.67) — Horizon launcher 0.2.67
<sub>2026-11-15 · today</sub>

> **Fixed**
> - Retire shader API 0.1; the game serves only 0.2 (#15886)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.66](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.66) — Horizon launcher 0.2.66
<sub>2026-11-15 · yesterday</sub>

> **Fixed**
> - Run four more slow tests in 17 s instead of 40 s (#16484)
> - Skip parsing game files that cannot hold an impl Game (#16505)
> **Contributors**
> Thanks to @kacpherek.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.65](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.65) — Horizon launcher 0.2.65
<sub>2026-11-14 · yesterday</sub>

> **Fixed**
> - Handle non-finite auxiliary frame samples (#15728, fixes #15704)
> - Recognize public IPv6 hosting routes (#15735, fixes #15717)
> - Add bounded streaming download engine (#16274)
> - Disable cmd AutoRun when creating Windows junctions (#15829, fixes #15722)
> **Contributors**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [bug(launcher): registry shader packs made for a retired shader API ar…](https://github.com/horizon-rust/horizon/commit/69ab572dbd1bf2f2924a424f791014e09d9d0b50) | NikitaMGrimm |
| 2026-11-16 | [tooling(mods): api-gen's two cfg_attr module path tests no longer sha…](https://github.com/horizon-rust/horizon/commit/54717b296579414add1ff4d18f7ca3ca35130bd2) | yassinsolim |
| 2026-11-16 | [tooling(mods): TerrainColumn in an export list of its own, so check_l…](https://github.com/horizon-rust/horizon/commit/333fe839e6c80699f4ea913434a809170bc4e4eb) | yassinsolim |
| 2026-11-16 | [Merge pull request #17145 from kacpherek/mod-api-merge](https://github.com/horizon-rust/horizon/commit/85b5bcca7c79bb470b90bdb5914b413aa66fe7ae) | levzzz5154 |
| 2026-11-16 | [Keep upstream and fork release test fixtures distinct](https://github.com/horizon-rust/horizon/commit/4a0c49aaa7b0d949558fb92e1d16a35c2626ea89) | levzzz5154 |
| 2026-11-16 | [Make Mods search fixture independent of product registration](https://github.com/horizon-rust/horizon/commit/9a3f8deb5712b0a59f6596b2490138b09a1076b9) | levzzz5154 |
| 2026-11-16 | [Reconcile imported tooling contracts with Horizon CI](https://github.com/horizon-rust/horizon/commit/5d3191373d50af28c02eb3b5ddff78de12162a8f) | levzzz5154 |
| 2026-11-15 | [Finish mod API merge gates and preserve policy boundaries](https://github.com/horizon-rust/horizon/commit/280e2edee5caf057d461dd53384c3b21c1b9e9bc) | levzzz5154 |
| 2026-11-15 | [Merge current main into mod API completion](https://github.com/horizon-rust/horizon/commit/4e3d4b0e8490483550145191fb715d89ad2725d8) | levzzz5154 |
| 2026-11-15 | [Use supported UTF-16 and resident-order APIs in transfer regressions](https://github.com/horizon-rust/horizon/commit/5015cff59e6260285a5ae5b326ea4c20eefea165) | levzzz5154 |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
