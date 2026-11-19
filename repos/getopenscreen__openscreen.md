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
| ⭐ **Stars** | 7.6k |
| 🍴 **Forks** | 499 |
| 🐞 **Open issues + PRs** | [50](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 280.8 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0)
<sub>2026-11-17 · yesterday</sub>

> <p align="center">
>   <img src="https://raw.githubusercontent.com/getopenscreen/openscreen/v2.3.0/public/openscreen.png" alt="OpenScreen" width="64" />
> </p>
> **OpenScreen 2.3 gives you more control while recording and a clearer view of every AI edit.** Keep a floating camera preview nearby, pause your narration without ending the take, and follow the agent's work step by step. This release also adds per-clip rotation, Dutch and Polish, and native X11 recording.
> **[Download for Windows, macOS and Linux](https://getopenscreen.com/download/)** · [Full changelog](https://github.com/getopenscreen/openscreen/compare/v2.2.2...v2.3.0)
> Free and open source. MIT licensed. No features behind a paywall.
> …

### [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

> **Changes since v2.3.0-rc.6**
> - fix(preview): keep scrubs playing while a new source loads
> - fix(preview): wait for metadata before resuming queued seeks
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.6...v2.3.0-rc.7

### [v2.3.0-rc.6](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.6) _(pre-release)_
<sub>2026-11-17 · 2d ago</sub>

> **Changes since v2.3.0-rc.5**
> - fix(recording): drop a saved display whose stable id is gone
> - fix(stt): keep whisper decoding from starving the machine
> - fix(voiceover): reject empty takes and failed saves
> - fix(preview): keep playback across a manual source seek
> - fix(updater): close idle macOS MCP sessions before installing
> …

### [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) _(pre-release)_
<sub>2026-11-16 · 3d ago</sub>

> **Changes since v2.3.0-rc.4**
> - fix(export): keep the permissions of the file an MP4 or GIF export replaces
> - fix(export): set a replaced export's mode through the staged file's handle
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.4...v2.3.0-rc.5

### [v2.3.0-rc.4](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.4) _(pre-release)_
<sub>2026-11-15 · 3d ago</sub>

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
| 2026-11-19 | [test(compositor): skip the dmabuf round-trip on buffer capability, no…](https://github.com/getopenscreen/openscreen/commit/44579df5bdd157aac78a17bb74619d37853ab226) | EtienneLescot |
| 2026-11-19 | [test(compositor): only skip the dmabuf round-trip when the device lac…](https://github.com/getopenscreen/openscreen/commit/95705aafd5d0930dffba8996868414d706ad2a02) | DariusDev16 |
| 2026-11-19 | [fix(compositor): return None from create_exportable_staging without d…](https://github.com/getopenscreen/openscreen/commit/0c8a43ca22bda303d72732561f00d2b55d4c785e) | DariusDev16 |
| 2026-11-18 | [docs(build): name unzip as a Linux prerequisite for ONNX Runtime](https://github.com/getopenscreen/openscreen/commit/14b4c2f2460f1f1eaa6186b66da8d049d09dd8d5) | EtienneLescot |
| 2026-11-18 | [fix(build): name the extractor and clean up when extraction fails](https://github.com/getopenscreen/openscreen/commit/cf568881b02b690360d1496529644707ff5254ba) | EtienneLescot |
| 2026-11-18 | [fix(build): fetch ONNX Runtime from Microsoft's NuGet package](https://github.com/getopenscreen/openscreen/commit/185e469c3eddf2afc514272ef095a124b5111944) | EtienneLescot |
| 2026-11-18 | [fix(linux): offer only the EGL modifiers all four formats import](https://github.com/getopenscreen/openscreen/commit/d55d0d5fb36b8701dd4ad8b19cb9342908a013d7) | EtienneLescot |
| 2026-11-18 | [fix(linux): accept any surface type in the surfaceless EGL config](https://github.com/getopenscreen/openscreen/commit/db22c1ea9696f8c086f873f0cad09fba42668c93) | EtienneLescot |
| 2026-11-18 | [feat(linux): import DMA-BUF frames through EGL when VA-API cannot](https://github.com/getopenscreen/openscreen/commit/37e1b38c30ad82cd1a1ada5db0d368aff64c821d) | EtienneLescot |
| 2026-11-17 | [chore(release): release v2.3.0 into main](https://github.com/getopenscreen/openscreen/commit/42a776ef9e322bd3a7757b428264e1eb4d12951d) | github-actions[bot] |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
