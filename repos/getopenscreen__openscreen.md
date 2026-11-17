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
| ⭐ **Stars** | 7.5k |
| 🍴 **Forks** | 493 |
| 🐞 **Open issues + PRs** | [48](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 281.1 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) _(pre-release)_
<sub>2026-11-17 · today</sub>

> **Changes since v2.3.0-rc.6**
> - fix(preview): keep scrubs playing while a new source loads
> - fix(preview): wait for metadata before resuming queued seeks
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.6...v2.3.0-rc.7

### [v2.3.0-rc.6](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.6) _(pre-release)_
<sub>2026-11-17 · today</sub>

> **Changes since v2.3.0-rc.5**
> - fix(recording): drop a saved display whose stable id is gone
> - fix(stt): keep whisper decoding from starving the machine
> - fix(voiceover): reject empty takes and failed saves
> - fix(preview): keep playback across a manual source seek
> - fix(updater): close idle macOS MCP sessions before installing
> …

### [v2.3.0-rc.5](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.5) _(pre-release)_
<sub>2026-11-16 · yesterday</sub>

> **Changes since v2.3.0-rc.4**
> - fix(export): keep the permissions of the file an MP4 or GIF export replaces
> - fix(export): set a replaced export's mode through the staged file's handle
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.4...v2.3.0-rc.5

### [v2.3.0-rc.4](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.4) _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> **Changes since v2.3.0-rc.3**
> - fix(export): keep the existing file when an export write fails
> - fix(export): stage an export write under a short name
> - fix(export): keep the permissions of the file an export replaces
> - fix(recording): a dismissed picker cancels the start and never leaves the webcam recording
> - fix(recording): keep a portal cancel that arrives with ready, before the wait
> …

### [v2.3.0-rc.3](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.3) _(pre-release)_
<sub>2026-11-15 · yesterday</sub>

> **Changes since v2.3.0-rc.2**
> - fix(linux): keep the capture helper's diagnostics out of the editor's toast
> - fix(export): keep the last frame when the encoder returns it without a duration
> - fix(export): copy the render's AAC into an .m4a instead of re-encoding it
> - fix(linux): keep the Wayland camera preview across the editor and Notes off the bar
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.2...v2.3.0-rc.3

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [chore(release): release v2.3.0 into main](https://github.com/getopenscreen/openscreen/commit/42a776ef9e322bd3a7757b428264e1eb4d12951d) | github-actions[bot] |
| 2026-11-17 | [docs(testing): record signed rc7 seek qualification](https://github.com/getopenscreen/openscreen/commit/307970bc97077de91b8e86e55e8ccdda14001c7f) | EtienneLescot |
| 2026-11-17 | [docs(testing): qualify rc6 and its scrub follow-up](https://github.com/getopenscreen/openscreen/commit/9a820fde10507c58ac9f3d409039430c7d294cd6) | EtienneLescot |
| 2026-11-17 | [docs(testing): record v2.3.0 desktop regression evidence](https://github.com/getopenscreen/openscreen/commit/c0b4173d4e080cace7a4cc006da81f26b859c4ac) | EtienneLescot |
| 2026-11-17 | [fix(preview): wait for metadata before resuming queued seeks](https://github.com/getopenscreen/openscreen/commit/ce55b76c91c69b26a95c55e33202f42b581ee00a) | EtienneLescot |
| 2026-11-17 | [fix(preview): keep scrubs playing while a new source loads](https://github.com/getopenscreen/openscreen/commit/efe23737441e4d0e7f45469fe417288eebb09595) | EtienneLescot |
| 2026-11-17 | [fix(audio): preserve removed tail fragments and preview playback](https://github.com/getopenscreen/openscreen/commit/fccdcdf9ea9c05d4ca6d884eaa6a72ba928ce8f1) | EtienneLescot |
| 2026-11-17 | [fix(audio): retain music fades beyond the programme end](https://github.com/getopenscreen/openscreen/commit/3e325342b5e3bcd99dac3a5cad8f0f4fd8c36b9d) | EtienneLescot |
| 2026-11-17 | [fix(ai): ignore superseded provider snapshots](https://github.com/getopenscreen/openscreen/commit/1a94c5d1ed15852bcab984482000c2862bc71d22) | EtienneLescot |
| 2026-11-17 | [fix(ai): wait for provider setup before Smart cuts](https://github.com/getopenscreen/openscreen/commit/70de53ceae559a7be6c9a4d4506a781532faa692) | EtienneLescot |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
