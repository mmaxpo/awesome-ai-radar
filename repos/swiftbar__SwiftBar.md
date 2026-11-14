# swiftbar/SwiftBar

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/swiftbar/SwiftBar)

> Powerful macOS menu bar customization tool

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Put any script's output in the Mac menu bar |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.8k |
| 🍴 **Forks** | 146 |
| 🐞 **Open issues + PRs** | [11](https://github.com/swiftbar/SwiftBar/issues) |
| 💻 **Languages** | Swift 97% · Shell 1% · Just 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `productivity` `macos` `scripting` |
| 🕒 **Last activity** | 2026-11-08 (5d ago) |
| 📅 **Created** | 2020-10-25 |
| 📦 **Latest release** | [v2.1.2-beta-5](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-5) — 2026-09-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.5 MB |
| 🌐 **Website** | https://swiftbar.app |

## 📦 Recent releases

### [v2.1.2-beta-5](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-5) — 2.1.2 BETA 5 _(pre-release)_
<sub>2026-09-29 · 1mo ago</sub>

> **SwiftBar 2.1.2 beta 5**
> This beta replaces beta 4, whose binary was archived with an Xcode beta toolchain — the source of the image-size regression reported against it — and adds four fixes.
> **Fixed by rebuilding**
> * `image=`/`templateImage=` render at intrinsic size again without explicit `width`/`height`. Beta 4's artifact triggered a per-process downscale inside AppKit; the code was never at fault. [#572](https://github.com/swiftbar/SwiftBar/issues/572) [#513](https://github.com/swiftbar/SwiftBar/issues/513)
> * The Login Items entry now actually shows "SwiftBar" — the beta 4 artifact shipped without this stamp. [#553](https://github.com/swiftbar/SwiftBar/issues/553)
> **Fixes**
> …

### [v2.1.2-beta-4](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-4) — 2.1.2 BETA 4 _(pre-release)_
<sub>2026-09-27 · 1mo ago</sub>

> **SwiftBar 2.1.2 beta 4**
> This beta collects eleven fixes and one new plugin option since beta 3, focused on macOS 26/27 menu behavior and wake-from-sleep false alarms.
> **Fixes**
> * Custom `color=` is preserved through hover on macOS 26 — colored titles are left alone during menu tracking, which also resolves inline-image loss on hover. [#541](https://github.com/swiftbar/SwiftBar/issues/541) [#530](https://github.com/swiftbar/SwiftBar/issues/530) [#558](https://github.com/swiftbar/SwiftBar/pull/558)
> * Calendar and Reminders access works again for plugins on macOS 14+ — the EventKit full-access usage keys were missing. [#411](https://github.com/swiftbar/SwiftBar/issues/411) [#549](https://github.com/swiftbar/SwiftBar/pull/549)
> * The stale-update ⚠️ no longer fires after wake from sleep — sleep time is excluded from staleness checks. [#540](https://github.com/swiftbar/SwiftBar/issues/540) [#551](https://github.com/swiftbar/SwiftBar/issues/551) [#561](https://github.com/swiftbar/SwiftBar/pull/561)
> …

### [v2.1.2-beta-3](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-3) — 2.1.2 BETA 3 _(pre-release)_
<sub>2026-08-15 · 3mo ago</sub>

> **SwiftBar 2.1.2 beta 3**
> This beta adds two macOS 26 menu-rendering fixes since beta 2.
> **Fixes**
> * Preserved explicit SF Symbol palette, hierarchical, and multicolor rendering instead of applying template tint over configured colors. [#532](https://github.com/swiftbar/SwiftBar/issues/532) [#537](https://github.com/swiftbar/SwiftBar/pull/537)
> * Corrected multiline title alignment after inline Base64 images and redrew tracked menu colors without replacing attributed titles. [#533](https://github.com/swiftbar/SwiftBar/issues/533) [#538](https://github.com/swiftbar/SwiftBar/pull/538)
> Please test SF Symbols with `sfconfig`, multiline menu rows with Base64 images, and hover colors on macOS 26 before the stable release.
> …

### [v2.1.2-beta-2](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-2) — 2.1.2 BETA 2 _(pre-release)_
<sub>2026-08-14 · 3mo ago</sub>

> **SwiftBar 2.1.2 beta 2**
> This beta adds three compatibility fixes since beta 1 and is intended for validation before the stable 2.1.2 release.
> **Fixes**
> * Restored legacy plugin data and cache directory compatibility after upgrading from SwiftBar 2.0.1, including safe recovery of data written by affected 2.1.x builds. [#522](https://github.com/swiftbar/SwiftBar/issues/522) [#524](https://github.com/swiftbar/SwiftBar/pull/524)
> * Restored `swiftbar://refreshplugin` lookup by complete plugin filename while preserving absolute plugin identities. [#527](https://github.com/swiftbar/SwiftBar/issues/527) [#528](https://github.com/swiftbar/SwiftBar/pull/528)
> * Fixed menu rows and inline Base64 images disappearing during hover on macOS 26. [#519](https://github.com/swiftbar/SwiftBar/issues/519) [#529](https://github.com/swiftbar/SwiftBar/pull/529)
> …

### [v2.1.2-beta-1](https://github.com/swiftbar/SwiftBar/releases/tag/v2.1.2-beta-1) — 2.1.2 BETA 1 _(pre-release)_
<sub>2026-08-12 · 3mo ago</sub>

> **SwiftBar 2.1.2 beta 1**
> This beta fixes two menu regressions and is intended for validation before the stable 2.1.2 release.
> **Fixes**
> * Restored the intrinsic size of Base64 and template images in dropdown menu items on macOS 26 and later. [#513](https://github.com/swiftbar/SwiftBar/issues/513) [#516](https://github.com/swiftbar/SwiftBar/pull/516)
> * Fixed submenu parents becoming disabled after incremental child or title changes. [#512](https://github.com/swiftbar/SwiftBar/issues/512) [#514](https://github.com/swiftbar/SwiftBar/issues/514) [#515](https://github.com/swiftbar/SwiftBar/issues/515) [#518](https://github.com/swiftbar/SwiftBar/pull/518)
> Please test the affected image and submenu-refresh scenarios and report any remaining regressions before the stable release.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-08 | [chore(release): prepare unsigned build 627 handoff](https://github.com/swiftbar/SwiftBar/commit/97f4f87dc90e668c7829f1ee4a6fb7988c47bc73) | melonamin |
| 2026-11-08 | [fix: bound stream shutdown and preserve multiline image bounds](https://github.com/swiftbar/SwiftBar/commit/c5bd3c0b69e7187bd185650836f0f8567bffe634) | melonamin |
| 2026-11-08 | [fix(release): handle missing captures and record issue verification](https://github.com/swiftbar/SwiftBar/commit/270705363d807a027abdb97f2981760d9b9730f3) | melonamin |
| 2026-11-08 | [fix(terminal): open a window when tab creation is unavailable](https://github.com/swiftbar/SwiftBar/commit/1ef8d2160a86593f1461003c00ccafbccbef8c8b) | melonamin |
| 2026-11-08 | [docs(release): hand off unsigned build 625 and final test evidence](https://github.com/swiftbar/SwiftBar/commit/35538716ce2b8c09ebcdea70382b31939a3935c2) | melonamin |
| 2026-11-08 | [fix(menu): keep multiline images visible on macOS 26 and later](https://github.com/swiftbar/SwiftBar/commit/a1a5150447c2c12453d2ed0fd644117ad76214f9) | melonamin |
| 2026-11-08 | [docs(release): record merged source and issue disposition](https://github.com/swiftbar/SwiftBar/commit/8bb9f30768c7955e2009496c9dc1668abdd26088) | melonamin |
| 2026-11-08 | [docs(release): hand off beta signing and retain evidence](https://github.com/swiftbar/SwiftBar/commit/23a5c4116e174f1106a0937c7c6a3a41a4c34a47) | melonamin |
| 2026-11-08 | [docs(release): record stabilization proof and remaining gates](https://github.com/swiftbar/SwiftBar/commit/cc9420b6b5806e04defbdf5e8a0247655a5b511d) | melonamin |
| 2026-11-08 | [fix(plugin): snapshot requests and reject obsolete run state](https://github.com/swiftbar/SwiftBar/commit/681ac78208f3e87fa568dd540583b9db331ef281) | melonamin |

[See all commits ↗](https://github.com/swiftbar/SwiftBar/commits)

## ⬇️ Get it

```bash
git clone https://github.com/swiftbar/SwiftBar.git
```
