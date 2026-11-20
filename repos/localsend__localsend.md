# localsend/localsend

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/localsend/localsend)

> An open-source cross-platform alternative to AirDrop

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Open-source AirDrop alternative for every platform |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 99.9k |
| 🍴 **Forks** | 5.7k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 79% · Rust 18% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-19 (yesterday) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.5 MB |
| 🌐 **Website** | https://localsend.org |

## 📦 Recent releases

### [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2)
<sub>2026-08-21 · 3mo ago</sub>

> This release fixes compatibility issues with 1.17.0 and earlier.
> Note: The Windows binaries have been updated to include a signature.
> - feat: drag and drop files into the "Receive via link" browser page
> - feat(desktop): allow customizing the web share pages by placing HTML files in a `web` folder next to the executable
> - feat(cli): add version info to the Windows executable
> - feat(linux): set actual version in the AppImage
> …

### [v1.18.1](https://github.com/localsend/localsend/releases/tag/v1.18.1)
<sub>2026-08-12 · 3mo ago</sub>

> Android+iOS only hotfix update. See [1.18.0](https://github.com/localsend/localsend/releases/tag/v1.18.0) for the full release.
> - fix: revert button icon sizes to 24
> - fix: when sending a message that is accepted immediately, a ghost device list tile appears
> - fix(mobile): when sending a link message, the "Open" button overflows
> - fix(android): add missing ACCESS_LOCAL_NETWORK permission that is required for Android 17+
> - i18n: add Belarusian (@pavel-miniutka), Irish (@aindriu80)

### [v1.18.0](https://github.com/localsend/localsend/releases/tag/v1.18.0)
<sub>2026-08-10 · 3mo ago</sub>

> This release is also the first release of the CLI. It uses the same Rust library as the Flutter app.
> The Rust rewrite of the core networking and file I/O logic is complete. You should notice that in improved transfer speeds.
> Note: The Windows binaries have been updated to include a signature.
> **Summary**
> - feat(cli): initial CLI release
> - feat: receive via link
> …

### [v1.17.0](https://github.com/localsend/localsend/releases/tag/v1.17.0)
<sub>2025-02-20 · 1y ago</sub>

> **Summary**
> A small interim release before WebRTC is stable (https://github.com/localsend/localsend/pull/2204)
> - feat: add advanced setting to filter network interfaces (@Tienisto)
> - feat(mobile): swipe gesture to select multiple media files (@Tienisto)
> - feat(windows): when pasting an image, automatically convert it to PNG (@BrianMwit)
> - feat(android): add option to open gallery when image/video was automatically saved (@Tienisto)
> …

### [v1.16.1](https://github.com/localsend/localsend/releases/tag/v1.16.1)
<sub>2024-11-05 · 2y ago</sub>

> **Summary**
> - feat: show exact error message when using IP address dialog or favorite dialog (@Tienisto)
> - feat(desktop): highlight file when tapping "Show in folder" (@Tienisto)
> - fix(android): properly close app on back gesture (@Tienisto)
> [Full Changelog](https://github.com/localsend/localsend/blob/main/app/assets/CHANGELOG.md)

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [fix: stop a send session that was cancelled while prepare-upload was …](https://github.com/localsend/localsend/commit/e05d12a9c0fd4d8c0245d2ec5c3c177e7e0f759b) | Tienisto |
| 2026-11-18 | [fix: rank link-local IPv6 channels after IPv4 when choosing an addres…](https://github.com/localsend/localsend/commit/a6ee93b55340d7ef5d2519842503c7887f0e7479) | Tienisto |
| 2026-11-18 | [fix: limit connection setup for pinned HTTP clients to 5 seconds (#3726)](https://github.com/localsend/localsend/commit/541689d1a4e8fd552772109b82ae75ecd7722afd) | Tienisto |
| 2026-11-18 | [fix: let cancellation interrupt reading prepare-upload and upload res…](https://github.com/localsend/localsend/commit/84b17d4b6027dda4a6c98b0f7c2011dec034e48d) | Tienisto |
| 2026-11-18 | [fix: strip request URLs from HTTP client errors so the PIN is not exp…](https://github.com/localsend/localsend/commit/025f950e67057dd4330cc22500ec90451df9bb1e) | Tienisto |
| 2026-11-18 | [feat: make sending checksums opt-in (#3723)](https://github.com/localsend/localsend/commit/65496bdb021cd78d26657a34fba1fa5557dcb899) | Tienisto |
| 2026-11-18 | [Expose channel direction reachability and probe peer on /register (#3…](https://github.com/localsend/localsend/commit/ef2578911a0ad34771d9090f66d3f5a80ddb95c7) | Tienisto |
| 2026-11-17 | [chore: add marionette integration for debug builds (#3721)](https://github.com/localsend/localsend/commit/281b491e9c0d0e692fc7ff1caaea28c897a64fd0) | Tienisto |
| 2026-11-17 | [Revert "deps: bump flutter to 3.47.9 (#3692)" (#3717)](https://github.com/localsend/localsend/commit/d1e6198f401939a9b76854f406f7dbb27d67a808) | Tienisto |
| 2026-11-11 | [fix(linux): resolve the tray icon to an absolute path on Snap (#3354)](https://github.com/localsend/localsend/commit/2e7ef1972b0b4e210608ec77ef5fad334f798f7e) | vicajilau |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
