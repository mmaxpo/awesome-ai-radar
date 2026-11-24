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
| ⭐ **Stars** | 11.9k |
| 🍴 **Forks** | 2.1k |
| 🐞 **Open issues + PRs** | [1.4k](https://github.com/horizon-rust/horizon/issues) |
| 💻 **Languages** | Rust 85% · Python 11% · Java 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `game-engine` `linux` `minecraft` `reimplementation` `rust` `vulkan` `wgpu` `gamedev` `minecraft-java` `voxel` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-10-03 |
| 📦 **Latest release** | [launcher@0.2.108](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.108) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 878.2 MB |
| 🌐 **Website** | https://playhorizon.dev |

## 📦 Recent releases

### [launcher@0.2.108](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.108) — Horizon launcher 0.2.108
<sub>2026-11-24 · today</sub>

> **New**
> - Entity-context shapes for vanilla blocks (#19085, fixes #18622)
> - Dragon_change_phase hook, Paper's EnderDragonChangePhaseEvent (#18760)
> - Let client mods replace the closing save screen (#20272, fixes #18650)
> - Follow the machine's power state instead of reading it once at startup (#18485, fixes #18240)
> - Draw textured camera-relative celestial geometry (#20303)
> …

### [launcher@0.2.107](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.107) — Horizon launcher 0.2.107
<sub>2026-11-22 · yesterday</sub>

> **Fixed**
> - Don't parse a Java instance's game command as Horizon arguments (#19911, fixes #19719)
> **Contributors**
> Thanks to @Juanpalai.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [launcher@0.2.106](https://github.com/horizon-rust/horizon/releases/tag/launcher%400.2.106) — Horizon launcher 0.2.106
<sub>2026-11-22 · yesterday</sub>

> **Fixed**
> - A mod made for a newer game says to update the instance (#19818)
> **Contributors**
> Thanks to @NikitaMGrimm.
> Your launcher updates itself. New here? On Linux take the .AppImage below, make it executable and run it; on Windows and macOS download the archive, extract it and run `horizon-launcher` (Horizon.app on macOS). Website: https://playhorizon.dev
> ---
> …

### [nightly](https://github.com/horizon-rust/horizon/releases/tag/nightly) — Nightly 2026-11-22 · f1bb66f _(pre-release)_
<sub>2026-11-22 · yesterday</sub>

> <h1>Want to play? Download the <a href="https://playhorizon.dev">Horizon launcher</a>.</h1><h1>Do NOT run the files below. They will not work on their own.</h1><p>The launcher installs this version and keeps it up to date. You need your own copy of Minecraft: Java Edition. The files below are what the launcher installs, and the dedicated server for people who host one.</p>
> Nightly 2026-11-22 · f1bb66f: main (f1bb66f), built from `nightly/build-2026-11-22-2` (f1bb66f353cf67f2aa4665293fc75c8d91186fc7).
> Source: commit f1bb66f353cf67f2aa4665293fc75c8d91186fc7, kept for good as the tag `nightly-source/2026-11-22-f1bb66f`; horizon-source.tar.gz is its tree. Native mods built for this Nightly pin that commit.
> The launcher installs it by itself; your worlds stay as they are. A Nightly can include pull requests the Team picked before they are merged (below). Report bugs with the version the game shows ("Nightly <date> · <commit>").
> **New**
> - Let native mods record named profiling scopes (#18678, fixes #18672)
> …

### [sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7](https://github.com/horizon-rust/horizon/releases/tag/sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7) — Mod SDK f1bb66f353 _(pre-release)_
<sub>2026-11-22 · yesterday</sub>

> Exact-build SDK for f1bb66f353cf67f2aa4665293fc75c8d91186fc7; sdk.json inventories every asset and SHA256SUMS is signed for sdk-f1bb66f353cf67f2aa4665293fc75c8d91186fc7.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [server: report world-upgrade management notifications (#17411)](https://github.com/horizon-rust/horizon/commit/2b5d6ec91c3fa0e20263102aea11aea9bb80196b) | TiggerTakkyTTT |
| 2026-11-24 | [feature(modding): crafting_recipe_choice lets a mod pick among matchi…](https://github.com/horizon-rust/horizon/commit/b78709a7731245f945f59fab45d9c2107090675f) | Echo-0-Code |
| 2026-11-24 | [bug(mods): support custom growing-plant survival families (#19746)](https://github.com/horizon-rust/horizon/commit/b1b1a28d42e294569854f0f5cfa5286f02906e89) | TiggerTakkyTTT |
| 2026-11-24 | [A join that fails before the login finishes is titled "Failed to conn…](https://github.com/horizon-rust/horizon/commit/4cc33af3530963070de19dd7ba0efbc42b17f0bb) | rdbtCVS |
| 2026-11-24 | [mod-api: support per-entity entity_tick_pre/post via Registrar::entit…](https://github.com/horizon-rust/horizon/commit/4f8cb82844308705bf8310f26cdd66abbf859acf) | levzzz5154 |
| 2026-11-24 | [Input source: InputSource and InputHost in the engine, no implementer…](https://github.com/horizon-rust/horizon/commit/734075e77ba495c27c99c5f1bf2fad71db6e4e1d) | martipops |
| 2026-11-24 | [Let End gateways outside the End take travellers, and catch fast fall…](https://github.com/horizon-rust/horizon/commit/a9949e62791b517b67a1aa2cbf9f52cf8682ec37) | ilguerro |
| 2026-11-24 | [parity(end): a dragon respawn's crystals are saved as vanilla's respa…](https://github.com/horizon-rust/horizon/commit/d65323c263913de539273378b5181c57fbc5baaf) | rdbtCVS |
| 2026-11-24 | [A mob's equipment enchantments make it immune to damage, as LivingEnt…](https://github.com/horizon-rust/horizon/commit/732cc2fb697be92feb07c9afba04ff522b906ba9) | rdbtCVS |
| 2026-11-24 | [World Options buttons show vanilla's tooltips and why a greyed-out on…](https://github.com/horizon-rust/horizon/commit/245c32639ce5a8e5c65ae4a762fa20e6214f2ef6) | rdbtCVS |

[See all commits ↗](https://github.com/horizon-rust/horizon/commits)

## ⬇️ Get it

```bash
git clone https://github.com/horizon-rust/horizon.git
```
