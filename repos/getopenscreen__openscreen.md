# getopenscreen/openscreen

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/getopenscreen/openscreen)

> Record your screen, ship a demo. Free and open-source, GPU-accelerated, no watermarks, no subscriptions. Windows, macOS, Linux. Actively maintained.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Screen recorder that turns recordings into demo videos |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 7.4k |
| 🍴 **Forks** | 490 |
| 🐞 **Open issues + PRs** | [47](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) — 2026-11-16 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 280.3 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) _(pre-release)_
<sub>2026-11-16 · today</sub>

> **Changes since v2.3.0-rc.4**
> - fix(export): keep the permissions of the file an MP4 or GIF export replaces
> - fix(export): set a replaced export's mode through the staged file's handle
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.4...v2.3.0-rc.5

### [v2.3.0-rc.4](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.4) _(pre-release)_
<sub>2026-11-15 · today</sub>

> **Changes since v2.3.0-rc.3**
> - fix(export): keep the existing file when an export write fails
> - fix(export): stage an export write under a short name
> - fix(export): keep the permissions of the file an export replaces
> - fix(recording): a dismissed picker cancels the start and never leaves the webcam recording
> - fix(recording): keep a portal cancel that arrives with ready, before the wait
> …

### [v2.3.0-rc.3](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.3) _(pre-release)_
<sub>2026-11-15 · today</sub>

> **Changes since v2.3.0-rc.2**
> - fix(linux): keep the capture helper's diagnostics out of the editor's toast
> - fix(export): keep the last frame when the encoder returns it without a duration
> - fix(export): copy the render's AAC into an .m4a instead of re-encoding it
> - fix(linux): keep the Wayland camera preview across the editor and Notes off the bar
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.2...v2.3.0-rc.3

### [v2.3.0-rc.2](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.2) _(pre-release)_
<sub>2026-11-15 · today</sub>

> **Changes since v2.3.0-rc.1**
> - fix(update): keep a per-user Windows install per user when an all-users one exists
> - fix(notes): restore a minimized Notes window from the HUD's Notes button
> - fix(mcp): record the user's camera for startRecording camera: true
> - fix(editor): reach Save Diagnostics from the wordmark menu
> - fix(mcp): take the restore baseline right before a take's prefs apply
> …

### [v2.3.0-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.1) _(pre-release)_
<sub>2026-11-14 · yesterday</sub>

> **Changes since v2.2.2**
> - chore(release): release v2.2.1 into main
> - docs(website): add a terms of use page, linked from the footer
> - feat(usage): send the install week with the daily count, for cohort retention
> - fix(usage): no mtime fallback for the install week, validate the stored week
> - fix(usage): treat an unrepresentable birthtime as an unknown install week
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(stt): keep whisper decoding from starving the machine](https://github.com/getopenscreen/openscreen/commit/d36aa7d82ff7716dd9017ce77f6fcf153c8374d4) | EtienneLescot |
| 2026-11-16 | [fix(export): set a replaced export's mode through the staged file's h…](https://github.com/getopenscreen/openscreen/commit/40eb6484ac947324d3b44c62a81cbeed50b1ad52) | EtienneLescot |
| 2026-11-16 | [fix(export): keep the permissions of the file an MP4 or GIF export re…](https://github.com/getopenscreen/openscreen/commit/ce93ed2ad7e11411bf83c416e4d8712adb6d44d4) | EtienneLescot |
| 2026-11-16 | [docs(testing): mark the targeted rc.2 and rc.3 rows Partial, as the c…](https://github.com/getopenscreen/openscreen/commit/f8536ede0db2211f5cffe2ba3a5c0883affbda15) | EtienneLescot |
| 2026-11-16 | [docs(testing): log the v2.3.0-rc.2 and rc.3 e2e passes on Windows, ma…](https://github.com/getopenscreen/openscreen/commit/34aac0137721278f79d75b1e07a43c44027061bc) | EtienneLescot |
| 2026-11-16 | [fix(recording): drop a saved display whose stable id is gone](https://github.com/getopenscreen/openscreen/commit/4e3ce0f60637e0e3d45c53358a7b65364352152f) | EtienneLescot |
| 2026-11-15 | [fix(linux): read the Wayland Notes size when it shrinks, minimum incl…](https://github.com/getopenscreen/openscreen/commit/3c2a4770c2ede9f1b37638fd4ebfc868bcde7972) | EtienneLescot |
| 2026-11-15 | [fix(linux): size Wayland Notes from the HUD's reported bar top](https://github.com/getopenscreen/openscreen/commit/d2d77a3f48294f95c8589e86a41f52613b63e6a1) | EtienneLescot |
| 2026-11-15 | [fix(linux): open Notes at the top edge on Wayland, clear of the HUD bar](https://github.com/getopenscreen/openscreen/commit/d76cfebc3621fe8a9c06cedf11ea75e01f1227c9) | EtienneLescot |
| 2026-11-15 | [fix(recording): keep a portal cancel that arrives with ready, before …](https://github.com/getopenscreen/openscreen/commit/8f00b8f8d7c531aa8812a2df884df4ded274826e) | EtienneLescot |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
