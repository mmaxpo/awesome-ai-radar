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
| ⭐ **Stars** | 7.8k |
| 🍴 **Forks** | 519 |
| 🐞 **Open issues + PRs** | [68](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 282.7 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0)
<sub>2026-11-17 · 4d ago</sub>

> <p align="center">
>   <img src="https://raw.githubusercontent.com/getopenscreen/openscreen/v2.3.0/public/openscreen.png" alt="OpenScreen" width="64" />
> </p>
> **OpenScreen 2.3 gives you more control while recording and a clearer view of every AI edit.** Keep a floating camera preview nearby, pause your narration without ending the take, and follow the agent's work step by step. This release also adds per-clip rotation, Dutch and Polish, and native X11 recording.
> **[Download for Windows, macOS and Linux](https://getopenscreen.com/download/)** · [Full changelog](https://github.com/getopenscreen/openscreen/compare/v2.2.2...v2.3.0)
> Free and open source. MIT licensed. No features behind a paywall.
> …

### [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) _(pre-release)_
<sub>2026-11-17 · 5d ago</sub>

> **Changes since v2.3.0-rc.6**
> - fix(preview): keep scrubs playing while a new source loads
> - fix(preview): wait for metadata before resuming queued seeks
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.6...v2.3.0-rc.7

### [v2.3.0-rc.6](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.6) _(pre-release)_
<sub>2026-11-17 · 5d ago</sub>

> **Changes since v2.3.0-rc.5**
> - fix(recording): drop a saved display whose stable id is gone
> - fix(stt): keep whisper decoding from starving the machine
> - fix(voiceover): reject empty takes and failed saves
> - fix(preview): keep playback across a manual source seek
> - fix(updater): close idle macOS MCP sessions before installing
> …

### [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) _(pre-release)_
<sub>2026-11-16 · 6d ago</sub>

> **Changes since v2.3.0-rc.4**
> - fix(export): keep the permissions of the file an MP4 or GIF export replaces
> - fix(export): set a replaced export's mode through the staged file's handle
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.4...v2.3.0-rc.5

### [v2.3.0-rc.4](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.4) _(pre-release)_
<sub>2026-11-15 · 6d ago</sub>

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
| 2026-11-21 | [fix(stt): force --cpu only for an explicit CPU backend, not for auto](https://github.com/getopenscreen/openscreen/commit/128ab63727967b11601686b92e447be87260e864) | EtienneLescot |
| 2026-11-21 | [fix(stt): launch the CPU-labelled whisper helper with --cpu](https://github.com/getopenscreen/openscreen/commit/28f691806768a4cd3e18701d4ac9693feee23e04) | EtienneLescot |
| 2026-11-21 | [test(mcp): pin that a failed start's reason reaches the client](https://github.com/getopenscreen/openscreen/commit/00a0d96e880e7d453ef20fc36659e1196dc7fbfb) | IdrisGit |
| 2026-11-21 | [fix(mcp): report a failed start's reason instead of a 30s timeout](https://github.com/getopenscreen/openscreen/commit/b4e6a59a926c54970470b8bfb6dd3f3a5d143f55) | IdrisGit |
| 2026-11-21 | [fix(recording): give the immediate start a machine-readable outcome](https://github.com/getopenscreen/openscreen/commit/328c6d41faafa665a4f7c21f751168ec9b8b560a) | IdrisGit |
| 2026-11-21 | [fix(website): drop a stale pending webcam target when no seek is in f…](https://github.com/getopenscreen/openscreen/commit/c1a2c97dfd2c21fdd93db2533c625a6d58ddfac2) | EtienneLescot |
| 2026-11-21 | [fix(website): keep the webcam bubble tracking the scroll after a re-a…](https://github.com/getopenscreen/openscreen/commit/f789607aed5a73a24889bc7e2b7b84fb319bfea0) | EtienneLescot |
| 2026-11-19 | [fix(editor): bound the dimension backfill save so a hung save cannot …](https://github.com/getopenscreen/openscreen/commit/01914391ad244d1152856ea9f0a249fb3dc4f713) | EtienneLescot |
| 2026-11-19 | [fix(editor): retry the dimension backfill after a failed save](https://github.com/getopenscreen/openscreen/commit/f5d1813183ba9e68678106486f2b811ebfbf3ac6) | EtienneLescot |
| 2026-11-19 | [fix(editor): keep the backfill save inside useTimeline for the write …](https://github.com/getopenscreen/openscreen/commit/5933740d5c39bf802954ea5fe95051b97b9bbaf5) | EtienneLescot |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
