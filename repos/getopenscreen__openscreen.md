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
| ⭐ **Stars** | 8.2k |
| 🍴 **Forks** | 549 |
| 🐞 **Open issues + PRs** | [81](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 49% · Rust 20% · HTML 13% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.4.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.4.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 283.7 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.4.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.4.0)
<sub>2026-11-23 · 2d ago</sub>

> If OpenScreen saves you time, a star on the repo helps others find it.
> **What's Changed**
> * fix(linux): record through a version 1 ScreenCast portal by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1538
> * feat(timeline): show each speed region's output duration by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1557
> * feat(editor): add pixel X / Y / Width / Height fields to the crop by @0xmyst3ry in https://github.com/getopenscreen/openscreen/pull/1389
> * docs(testing): log the v2.3.0-rc.1 e2e passes on Windows, macOS and Linux by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1565
> …

### [v2.4.0-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.4.0-rc.1) _(pre-release)_
<sub>2026-11-23 · 2d ago</sub>

> **Changes since v2.3.0**
> - fix(linux): record through a version 1 ScreenCast portal
> - fix(linux): take the v1 path on an empty cursor-mode mask
> - feat(timeline): show each speed region's output duration on its pill
> - fix(timeline): show a speed pill's full label on hover when it is cut off
> - feat(editor): add pixel X / Y / Width / Height fields to the crop
> …

### [v2.3.0](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0)
<sub>2026-11-17 · 9d ago</sub>

> <p align="center">
>   <img src="https://raw.githubusercontent.com/getopenscreen/openscreen/v2.3.0/public/openscreen.png" alt="OpenScreen" width="64" />
> </p>
> **OpenScreen 2.3 gives you more control while recording and a clearer view of every AI edit.** Keep a floating camera preview nearby, pause your narration without ending the take, and follow the agent's work step by step. This release also adds per-clip rotation, Dutch and Polish, and native X11 recording.
> **[Download for Windows, macOS and Linux](https://getopenscreen.com/download/)** · [Full changelog](https://github.com/getopenscreen/openscreen/compare/v2.2.2...v2.3.0)
> Free and open source. MIT licensed. No features behind a paywall.
> …

### [v2.3.0-rc.7](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.7) _(pre-release)_
<sub>2026-11-17 · 9d ago</sub>

> **Changes since v2.3.0-rc.6**
> - fix(preview): keep scrubs playing while a new source loads
> - fix(preview): wait for metadata before resuming queued seeks
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.3.0-rc.6...v2.3.0-rc.7

### [v2.3.0-rc.6](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.6) _(pre-release)_
<sub>2026-11-17 · 9d ago</sub>

> **Changes since v2.3.0-rc.5**
> - fix(recording): drop a saved display whose stable id is gone
> - fix(stt): keep whisper decoding from starving the machine
> - fix(voiceover): reject empty takes and failed saves
> - fix(preview): keep playback across a manual source seek
> - fix(updater): close idle macOS MCP sessions before installing
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(plugin): ask about a real window before staging; match across whi…](https://github.com/getopenscreen/openscreen/commit/96e3cd327e572eb13b19e4f040e689db9fdad0b4) | claude |
| 2026-11-26 | [fix(plugin): stop cleanly in the capture skill, ask before a real window](https://github.com/getopenscreen/openscreen/commit/4d2175aea8b15937cab36f0f8c49f8a29e752ff6) | claude |
| 2026-11-26 | [fix(plugin): stop the directory edition from pointing at a local server](https://github.com/getopenscreen/openscreen/commit/ec5ba943b9f6fb7de0971b4c5742ac3e8bf09b46) | claude |
| 2026-11-26 | [plugin: ask the user to quit OpenScreen before installing the update](https://github.com/getopenscreen/openscreen/commit/f4eda9b08274bc50e3bd3875b45d672ec6869cb8) | claude |
| 2026-11-26 | [plugin: ask for a new session after updating, and tell a disconnected…](https://github.com/getopenscreen/openscreen/commit/2f9bc4ade9c85a3ad093ab7f8f18635179839226) | claude |
| 2026-11-26 | [plugin: point the directory edition's update route at the install guide](https://github.com/getopenscreen/openscreen/commit/2ff5fc200f3adc7fd0928feb4be964e391dd20bd) | claude |
| 2026-11-26 | [plugin: give the directory edition a route to update OpenScreen](https://github.com/getopenscreen/openscreen/commit/3cdf96bbd68e63867ec2c5a92f1ad710ae2d94c0) | claude |
| 2026-11-26 | [fix(plugin): keep set-up steps out of the directory edition](https://github.com/getopenscreen/openscreen/commit/9c267b6ffcb9f5e4240024bdcaa3f0c821d07ca4) | claude |
| 2026-11-26 | [fix(plugin): drop the manifest's network field from the directory edi…](https://github.com/getopenscreen/openscreen/commit/1db0135a2e4287f309d93a1dd6a50c3b295efde7) | claude |
| 2026-11-26 | [fix(plugin): qualify the capture skill's headless choice in the direc…](https://github.com/getopenscreen/openscreen/commit/0558e0384e581191ee6b1338a913e6d050844edf) | claude |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
