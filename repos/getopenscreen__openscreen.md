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
| 🍴 **Forks** | 485 |
| 🐞 **Open issues + PRs** | [60](https://github.com/getopenscreen/openscreen/issues) |
| 💻 **Languages** | TypeScript 48% · Rust 20% · HTML 14% · MDX 6% · JavaScript 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `electron` `open-source` `screen-capture` `screen-recorder` `cross-platform` `ffmpeg` `product-demo` `rust` `screen-recording` `screen-studio` `screencast` `speech-to-text` `typescript` `video-editing` `video-editor` `wayland` `wgpu` `whisper` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-03-14 |
| 📦 **Latest release** | [v2.2.2](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2) — 2026-11-04 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 279.5 MB |
| 🌐 **Website** | https://getopenscreen.com/ |

## 📦 Recent releases

### [v2.3.0-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.3.0-rc.1) _(pre-release)_
<sub>2026-11-14 · today</sub>

> **Changes since v2.2.2**
> - chore(release): release v2.2.1 into main
> - docs(website): add a terms of use page, linked from the footer
> - feat(usage): send the install week with the daily count, for cohort retention
> - fix(usage): no mtime fallback for the install week, validate the stored week
> - fix(usage): treat an unrepresentable birthtime as an unknown install week
> …

### [v2.2.2](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2)
<sub>2026-11-04 · 10d ago</sub>

> If OpenScreen saves you time, a star on the repo helps others find it.
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.2.1...v2.2.2

### [v2.2.2-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.2-rc.1) _(pre-release)_
<sub>2026-11-04 · 10d ago</sub>

> **Changes since v2.2.1**
> - fix(export): recover nearby frames before sparse clip starts
> **Full Changelog**: https://github.com/getopenscreen/openscreen/compare/v2.2.1...v2.2.2-rc.1

### [v2.2.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.1)
<sub>2026-11-03 · 12d ago</sub>

> If OpenScreen saves you time, a star on the repo helps others find it.
> **What's Changed**
> * ci: retry validating the stapled macOS DMG when Apple drops the connection by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1433
> * fix: pick the YCbCr matrix per frame on macOS by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1421
> * docs: e2e results on main before the next prerelease by @EtienneLescot in https://github.com/getopenscreen/openscreen/pull/1434
> * fix(export): bound a clip by the container duration, not a one-frame video stream by @dropafterfree in https://github.com/getopenscreen/openscreen/pull/1418
> …

### [v2.2.1-rc.1](https://github.com/getopenscreen/openscreen/releases/tag/v2.2.1-rc.1) _(pre-release)_
<sub>2026-11-02 · 12d ago</sub>

> **Changes since v2.2.0**
> - ci: retry validating the stapled macOS DMG when Apple drops the connection
> - fix(compositor): pick the YCbCr matrix per frame on macOS
> - fix(compositor): leave BT.2020 CL on the default path, convert 10-bit samples with 10-bit bounds
> - docs(testing): log the prerelease passes on main and the signed CI DMG
> - docs(testing): add the x64 DMG signature check
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [docs(testing): expect Check for Updates in the tray, Help and wordmar…](https://github.com/getopenscreen/openscreen/commit/16f317ffb07d785467f175b556f3d932a095c3d6) | EtienneLescot |
| 2026-11-15 | [docs(testing): fix the update feed recipe and the Windows Help menu c…](https://github.com/getopenscreen/openscreen/commit/0b6f8deffd446e080e4272687bb5b2cf4e12452e) | EtienneLescot |
| 2026-11-15 | [fix(update): keep a per-user Windows install per user when an all-use…](https://github.com/getopenscreen/openscreen/commit/dff7d5b6cabc3239ca87bdbb5f078573b105bd05) | EtienneLescot |
| 2026-11-15 | [docs(testing): name the bump commit and run attempt behind the macOS …](https://github.com/getopenscreen/openscreen/commit/a050b6493bb0b42ac08cdd3c0b329097c62f6f9e) | EtienneLescot |
| 2026-11-15 | [docs(testing): log the v2.3.0-rc.1 e2e passes on Windows, macOS and L…](https://github.com/getopenscreen/openscreen/commit/400d28acb7549a985153f5ed4ee4715bcbd9d5c9) | EtienneLescot |
| 2026-11-14 | [fix(i18n): add the Polish strings for the crop pixel fields](https://github.com/getopenscreen/openscreen/commit/07a2d01eecd8667627925f89f05e802444cce893) | EtienneLescot |
| 2026-11-14 | [fix(editor): derive the crop size minimum from the locked ratio](https://github.com/getopenscreen/openscreen/commit/264380359a2664ae59e1e618cc6f7788f4f871b6) | EtienneLescot |
| 2026-11-14 | [fix(editor): keep the crop ratio and commit pixel fields on blur](https://github.com/getopenscreen/openscreen/commit/563001018f3b872c385a652acac563e7047cd002) | EtienneLescot |
| 2026-11-14 | [fix(editor): put crop pixel labels inline so the fields fit above the…](https://github.com/getopenscreen/openscreen/commit/90962bc4491644ba0bbe1bc8e4d70702100fdb85) | 0xmyst3ry |
| 2026-11-14 | [feat(editor): add pixel X / Y / Width / Height fields to the crop](https://github.com/getopenscreen/openscreen/commit/5cbc691ebbabd7629ac6768330a527e08d93d0b8) | 0xmyst3ry |

[See all commits ↗](https://github.com/getopenscreen/openscreen/commits)

## ⬇️ Get it

```bash
git clone https://github.com/getopenscreen/openscreen.git
```
