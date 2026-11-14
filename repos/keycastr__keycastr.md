# keycastr/keycastr

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/keycastr/keycastr)

> KeyCastr, an open-source keystroke visualizer

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Shows your keystrokes on screen for demos and recordings |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 15.2k |
| 🍴 **Forks** | 584 |
| 🐞 **Open issues + PRs** | [94](https://github.com/keycastr/keycastr/issues) |
| 💻 **Languages** | Objective-C 100% |
| 📜 **License** | BSD-3-Clause |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-09-07 (2mo ago) |
| 📅 **Created** | 2009-02-19 |
| 📦 **Latest release** | [v0.11.1](https://github.com/keycastr/keycastr/releases/tag/v0.11.1) — 2026-09-07 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 60.1 MB |

## 📦 Recent releases

### [v0.11.1](https://github.com/keycastr/keycastr/releases/tag/v0.11.1) — Minimal visualizer settings refinement
<sub>2026-09-07 · 2mo ago</sub>

> * Adjust Minimal visualizer keystroke filtering options by @colinta in https://github.com/keycastr/keycastr/pull/354

### [v0.11.0](https://github.com/keycastr/keycastr/releases/tag/v0.11.0) — New "Minimal" Visualizer
<sub>2026-08-27 · 2mo ago</sub>

> Introduces a new visualizer, Minimal. Thanks to @colinta for the original idea, and to @SoCuul for some code contributions along the way. This visualizer can also be filtered to display standalone modifier keys, a popular request.

### [v0.10.5](https://github.com/keycastr/keycastr/releases/tag/v0.10.5) — Improved handling of different input sources
<sub>2025-11-24 · 11mo ago</sub>

> Includes a fix for #314 , where a change in input source could be delayed.

### [v0.10.4](https://github.com/keycastr/keycastr/releases/tag/v0.10.4) — Minor quality of life improvements
<sub>2025-08-24 · 1y ago</sub>

> - Fix to display KeyCastr as inactive if it fails to install an event tap during startup
> - Fixed a long-standing issue with the ShortcutRecorder integration which would result in resetting the global shortcut if the user escaped the text entry box without entering a new shortcut (#328)
> - Fixed capitalization of option keystrokes (#329) and menu entry (#322)

### [v0.10.3](https://github.com/keycastr/keycastr/releases/tag/v0.10.3) — Fixes for backwards compatibility
<sub>2025-03-27 · 1y ago</sub>

> This release contains a couple fixes to help preserve compatibility as far back as macOS 10.13 - a project configuration fix to avoid crashing on startup and an adjustment to the NSArchiver/NSSecureArchiver migration to avoid running on 10.13.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-09-07 | [v0.11.1](https://github.com/keycastr/keycastr/commit/1e552a150afdf8f73fa4a12ba3cca1bbf09eb6ab) | akitchen |
| 2026-09-07 | [Fix Minimal visualizer settings layout warnings and add migration](https://github.com/keycastr/keycastr/commit/65f2a3680bea2eb33102dfb5bc84448eae0d00a8) | akitchen |
| 2026-09-07 | [Refactor preferences, to be a simple show/hide list that determines t…](https://github.com/keycastr/keycastr/commit/535a7ad01db7ec2ddf9c13f56698e2b2fd91fe54) | colinta |
| 2026-08-27 | [v0.11.0](https://github.com/keycastr/keycastr/commit/8a64843c536f19571786773d3e4241b79447b0fb) | akitchen |
| 2026-08-26 | [Set SKIP_INSTALL to YES for all internal bundles, all configurations](https://github.com/keycastr/keycastr/commit/f0f686eeb2b79b7ab2ddf3a808dd7cc53b3536e5) | akitchen |
| 2026-08-26 | [Update copyright year in About View](https://github.com/keycastr/keycastr/commit/82ec65ca2094eac5d9a1188f42aa87b71a5ac50d) | akitchen |
| 2026-08-26 | [Update Sparkle to v2.9.6](https://github.com/keycastr/keycastr/commit/95ee676d9c3d0c0282c769ec1a66a07e206f456e) | akitchen |
| 2026-08-25 | [Guard optional noteKeyUpEvent: with respondsToSelector:](https://github.com/keycastr/keycastr/commit/26deae8d293c44a61b586e84fd0125fa6ae24c68) | akitchen |
| 2026-08-25 | [Size Minimal visualizer key label to its text](https://github.com/keycastr/keycastr/commit/015a6fb4873c577384add6dd7da7515f57b6d26f) | akitchen |
| 2026-08-25 | [Drop trailing spaces from special key labels](https://github.com/keycastr/keycastr/commit/77788e605756ee067b917b2c602dabe9dafc6dcf) | akitchen |

[See all commits ↗](https://github.com/keycastr/keycastr/commits)

## ⬇️ Get it

```bash
git clone https://github.com/keycastr/keycastr.git
```
