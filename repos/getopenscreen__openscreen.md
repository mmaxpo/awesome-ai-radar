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
| ⭐ **Stars** | 7.9k |
| 🍴 **Forks** | 528 |
| 🐞 **Open issues + PRs** | [63](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 49% · Rust 20% · HTML 13% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 284.2 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0)
<sub>2026-11-17 · 6d ago</sub>

> <p align="center">
>   <img src="https://raw.githubusercontent.com/getopenscreen/openscreen/v2.3.0/public/openscreen.png" alt="OpenScreen" width="64" />
> </p>
> **OpenScreen 2.3 gives you more control while recording and a clearer view of every AI edit.** Keep a floating camera preview nearby, pause your narration without ending the take, and follow the agent's work step by step. This release also adds per-clip rotation, Dutch and Polish, and native X11 recording.
> **[Download for Windows, macOS and Linux](https://getopenscreen.com/download/)** · [Full changelog](https://github.com/getopenscreen/openscreen/compare/v2.2.2...v2.3.0)
> Free and open source. MIT licensed. No features behind a paywall.
> …

### [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) _(pre-release)_
<sub>2026-11-17 · 6d ago</sub>

> **Changes since v2.3.0-rc.6**
> - fix(preview): keep scrubs playing while a new source loads
> - fix(preview): wait for metadata before resuming queued seeks
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.6...v2.3.0-rc.7

### [v2.3.0-rc.6](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.6) _(pre-release)_
<sub>2026-11-17 · 6d ago</sub>

> **Changes since v2.3.0-rc.5**
> - fix(recording): drop a saved display whose stable id is gone
> - fix(stt): keep whisper decoding from starving the machine
> - fix(voiceover): reject empty takes and failed saves
> - fix(preview): keep playback across a manual source seek
> - fix(updater): close idle macOS MCP sessions before installing
> …

### [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) _(pre-release)_
<sub>2026-11-16 · 7d ago</sub>

> **Changes since v2.3.0-rc.4**
> - fix(export): keep the permissions of the file an MP4 or GIF export replaces
> - fix(export): set a replaced export's mode through the staged file's handle
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.4...v2.3.0-rc.5

### [v2.3.0-rc.4](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.4) _(pre-release)_
<sub>2026-11-15 · 7d ago</sub>

> **Changes since v2.3.0-rc.3**
> - fix(export): keep the existing file when an export write fails
> - fix(export): stage an export write under a short name
> - fix(export): keep the permissions of the file an export replaces
> - fix(recording): a dismissed picker cancels the start and never leaves the webcam recording
> - fix(recording): keep a portal cancel that arrives with ready, before the wait
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(linux): prevent Wayland HUD clipping at larger text scales](https://github.com/getopenscreen/openscreen/commit/20abd8c8542e8ed1bd655012e607f9a27b082737) | IdrisGit |
| 2026-11-23 | [fix(cli): write a whole chunk before acknowledging it](https://github.com/getopenscreen/openscreen/commit/e10f02bdf01b7a766e971e9dbefa21a6fa3db150) | EtienneLescot |
| 2026-11-23 | [fix(cli): give each export its own partial file, and remove it when t…](https://github.com/getopenscreen/openscreen/commit/706317dee1ab518eeb10a1f27a1a714937da3216) | EtienneLescot |
| 2026-11-23 | [fix(cli): stream the audio export and the voiceover mix in chunks](https://github.com/getopenscreen/openscreen/commit/c41b94ae3eb483bfbc20327d6510182cb219c510) | EtienneLescot |
| 2026-11-23 | [fix(hud): open no camera preview window at launch while the camera is…](https://github.com/getopenscreen/openscreen/commit/26df66b975f39ab2d80e1bcb84a3b54e927f73c9) | EtienneLescot |
| 2026-11-23 | [fix(recording): record the only X11 display when Electron's display_i…](https://github.com/getopenscreen/openscreen/commit/5952eba463fa484df40c6cfef6735bb2a75a9d8b) | EtienneLescot |
| 2026-11-23 | [fix(capture): close an open pause before a Linux take's stopped snapshot](https://github.com/getopenscreen/openscreen/commit/5cdf47c049aca68dc1a1e49838d8862d2a895012) | EtienneLescot |
| 2026-11-23 | [fix(stt): give up on a Whisper model download that stops receiving data](https://github.com/getopenscreen/openscreen/commit/73058deb2c8f6e4b2666fff0b99935463332e147) | EtienneLescot |
| 2026-11-23 | [docs(effects): say how to go on when an effect's image cannot be read…](https://github.com/getopenscreen/openscreen/commit/254e8585092ffec33148ee70aae1e15b73e24007) | EtienneLescot |
| 2026-11-23 | [fix(media): size an image by a decoded frame only, never by its heade…](https://github.com/getopenscreen/openscreen/commit/647a2b4d429e6415d166d037483f378cd8adc3c3) | EtienneLescot |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
