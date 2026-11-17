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
| ⭐ **Stars** | 11.0k |
| 🍴 **Forks** | 1.8k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `differential-testing` `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.70](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.70) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 772.9 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.70](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.70) — Horizon launcher 0.2.70
<sub>2026-11-17 · today</sub>

> **New**
> - The mod API: #16941 merged with main (#17145)
> **Fixed**
> - Registry shader packs made for a retired shader API are refused, not installed (#17327)
> - Skip the game-lease cleanup test in optimized builds so the launcher can release (#17418)
> - Shader packs are offered by what the installed game runs, not the launcher's own build (#17567, fixes #17527)
> …

### [launcher@0.2.69](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.69) — Horizon launcher 0.2.69
<sub>2026-11-16 · yesterday</sub>

> **Fixed**
> - Port ledger: fix 1 stale citation in horizon-port-pack (#16881)
> - Change Horizon's licence from MIT to LGPL-3.0-or-later (#17111)
> **Contributors**
> Thanks to @MSedgeMC, @kacpherek.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

### [launcher@0.2.68](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.68) — Horizon launcher 0.2.68
<sub>2026-11-15 · yesterday</sub>

> **New**
> - Arrows show and scroll the top bar's hidden tabs (#16580, fixes #16577)
> **Fixed**
> - Release notes draw only the rows in view (#16558, fixes #16557)
> - fix traduction launcher (#16847)
> - Name --prism-dir in the missing-files hint (#16895, fixes #16891)
> …

### [launcher@0.2.67](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.67) — Horizon launcher 0.2.67
<sub>2026-11-15 · yesterday</sub>

> **Fixed**
> - Retire shader API 0.1; the game serves only 0.2 (#15886)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.66](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.66) — Horizon launcher 0.2.66
<sub>2026-11-15 · 2d ago</sub>

> **Fixed**
> - Run four more slow tests in 17 s instead of 40 s (#16484)
> - Skip parsing game files that cannot hold an impl Game (#16505)
> **Contributors**
> Thanks to @kacpherek.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [tooling(ci): ludodesktop runs no Horizon CI any more (#17883)](https://github.com/horizon-rust/horizon/commit/3a6bea51bd0032b90438fba10c07c32e4bc1288b) | ludovic111 |
| 2026-11-17 | [Silk-touched hives keep their bees and honey on the client (#15872)](https://github.com/horizon-rust/horizon/commit/fd3142737b678255e6ff6337e3b475256b840876) | Sergo007 |
| 2026-11-17 | [docs(governance): NikitaMGrimm on the council list and in the Team's …](https://github.com/horizon-rust/horizon/commit/5fc24d1edd3a85cca85f19596677cc5cbc939374) | NikitaMGrimm |
| 2026-11-17 | [tooling(ci): every pull request gets a size label (#17628)](https://github.com/horizon-rust/horizon/commit/43226feaf33f66cda4aa71e3510ec713004b2b0d) | NikitaMGrimm |
| 2026-11-17 | [docs(template): the pull request template asks for the agent line at …](https://github.com/horizon-rust/horizon/commit/22192f835a39109016848efb8c37bbf0868c20b0) | NikitaMGrimm |
| 2026-11-17 | [tooling(ci): mojang republish checks out its script sparsely, as the …](https://github.com/horizon-rust/horizon/commit/101a3157c1731a1d5f3d028334b315a5212b8191) | NikitaMGrimm |
| 2026-11-17 | [tooling(ci): the lint cache keeps cargo and always records its commit…](https://github.com/horizon-rust/horizon/commit/6186887a62b77d929f8a0a7272dcf4a6a63f4a1e) | NikitaMGrimm |
| 2026-11-17 | [tooling(langs): do not count blank entries as coverage (#17639)](https://github.com/horizon-rust/horizon/commit/5c9c56be8c14e42b8a32ac52aac53ce26e159ecc) | angel2rider |
| 2026-11-17 | [tooling(commands): a fixture pack runs every registered slot-source r…](https://github.com/horizon-rust/horizon/commit/b663e7e80fe4ed9763f792670730bad5ea603634) | TheMrZZ |
| 2026-11-17 | [docs: run the game from horizon-game, where its executable moved (#17…](https://github.com/horizon-rust/horizon/commit/85facc07f20dca066aab2cb2de1fc8d04b63ec5c) | Bl4ckspell7 |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
