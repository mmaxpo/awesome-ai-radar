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
| ⭐ **Stars** | 7.3k |
| 🍴 **Forks** | 481 |
| 🐞 **Open issues + PRs** | [59](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.2.2](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 279.5 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.2.2](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2)
<sub>2026-11-04 · 9d ago</sub>

> If OpenScreen saves you time, a star on the repo helps others find it.
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.2.1...v2.2.2

### [v2.2.2-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2-rc.1) _(pre-release)_
<sub>2026-11-04 · 9d ago</sub>

> **Changes since v2.2.1**
> - fix(export): recover nearby frames before sparse clip starts
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.2.1...v2.2.2-rc.1

### [v2.2.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.1)
<sub>2026-11-03 · 11d ago</sub>

> If OpenScreen saves you time, a star on the repo helps others find it.
> **What's Changed**
> * ci: retry validating the stapled macOS DMG when Apple drops the connection by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1433
> * fix: pick the YCbCr matrix per frame on macOS by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1421
> * docs: e2e results on main before the next prerelease by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1434
> * fix(export): bound a clip by the container duration, not a one-frame video stream by @dropafterfree in https://github.com/getopenscreen/openscreen/pull/1418
> …

### [v2.2.1-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.1-rc.1) _(pre-release)_
<sub>2026-11-02 · 11d ago</sub>

> **Changes since v2.2.0**
> - ci: retry validating the stapled macOS DMG when Apple drops the connection
> - fix(compositor): pick the YCbCr matrix per frame on macOS
> - fix(compositor): leave BT.2020 CL on the default path, convert 10-bit samples with 10-bit bounds
> - docs(testing): log the prerelease passes on main and the signed CI DMG
> - docs(testing): add the x64 DMG signature check
> …

### [v2.2.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.0)
<sub>2026-11-02 · 11d ago</sub>

> **OpenScreen 2.2 brings layout changes to the timeline, separate tracks for overlapping annotations, and an update button that puts you in control of installation.** This release also improves recording, playback, audio timing and export across Windows, macOS and Linux.
> **✨ Highlights**
> **Change the layout throughout your video**
> The new **Layouts** track lets you switch between **picture-in-picture, side-by-side, top/bottom, camera-only and screen-only** arrangements as your video plays. Place a change at the playhead, move its boundary to adjust the timing, and let the screen and camera transition smoothly into their next positions.
> Layout edits support undo/redo and the AI/MCP tools. Existing Full Camera sections migrate to camera-only layouts while preserving their original easing. [#1404](https://github.com/getopenscreen/openscreen/pull/1404)
> **Keep overlapping annotations easy to edit**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [fix(linux): take the v1 path on an empty cursor-mode mask](https://github.com/getopenscreen/openscreen/commit/5fa2a5570978679870afdfa1038f069dd7bc46af) | EtienneLescot |
| 2026-11-14 | [fix(linux): record through a version 1 ScreenCast portal](https://github.com/getopenscreen/openscreen/commit/1b593155d1c4b9986d6cb5928ebd7d5a62fad675) | EtienneLescot |
| 2026-11-14 | [fix(linux): reopen a paused capture's audio rings before the shared-m…](https://github.com/getopenscreen/openscreen/commit/aa52ab335e6e49574035693ffa72dec7ca215c80) | EtienneLescot |
| 2026-11-14 | [fix(linux): start the shared-memory retry from a clean slate](https://github.com/getopenscreen/openscreen/commit/0d7f3e86190feec168ce2307904c8d9bda87b1ec) | EtienneLescot |
| 2026-11-14 | [fix(linux): keep the shared-memory retry reachable until a frame stages](https://github.com/getopenscreen/openscreen/commit/8967a9a0744aa7addaf59aa868a194efedf03b9e) | EtienneLescot |
| 2026-11-14 | [fix(linux): retry on shared memory when every DMA-BUF frame arrives c…](https://github.com/getopenscreen/openscreen/commit/95357c44d381b6096931115fb4cbc3f89339b9a3) | EtienneLescot |
| 2026-11-14 | [docs: drop camera-preview rows the PR had already removed](https://github.com/getopenscreen/openscreen/commit/7efe10edf305b19150b82f60948cd36a6b8a9ca0) | EtienneLescot |
| 2026-11-14 | [fix(i18n): add the Dutch and Polish camera preview strings](https://github.com/getopenscreen/openscreen/commit/cac16fed2ae8a387a7e4cbb92e10042d8aa650a2) | EtienneLescot |
| 2026-11-14 | [fix(camera-preview): answer review on stale helpers and failed starts](https://github.com/getopenscreen/openscreen/commit/0e1d8e0294ea4aee2bd0a8ba80d0b2fab36541f8) | EtienneLescot |
| 2026-11-14 | [fix(hud): hide the camera preview control while a take cannot exclude it](https://github.com/getopenscreen/openscreen/commit/728f6c05e485a0d8ddf2f19ed88396999bfa87e1) | EtienneLescot |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
