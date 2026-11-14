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
| ⭐ **Stars** | 99.0k |
| 🍴 **Forks** | 5.7k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 80% · Rust 17% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-11 (3d ago) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.5 MB |
| 🌐 **Website** | https://localsend.org |

## 📦 Recent releases

### [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2)
<sub>2026-08-21 · 2mo ago</sub>

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
| 2026-11-11 | [fix(linux): resolve the tray icon to an absolute path on Snap (#3354)](https://github.com/localsend/localsend/commit/2e7ef1972b0b4e210608ec77ef5fad334f798f7e) | vicajilau |
| 2026-11-08 | [fix(linux): do not fail the build on the appindicator deprecation (#3…](https://github.com/localsend/localsend/commit/8476c091c5a107e4507b6b3ec0cb15a069e857b5) | vicajilau |
| 2026-11-08 | [fix(linux): respect `XDG_CONFIG_HOME`, safely remove the desktop entr…](https://github.com/localsend/localsend/commit/c95e254813968d5bb41e31eaed5dfd497c03693c) | vicajilau |
| 2026-11-08 | [fix(linux): set StartupWMClass in the deb desktop entry (#3355)](https://github.com/localsend/localsend/commit/c9ecfac3df63cf3f02e6a2cdc297ccebf08e8824) | vicajilau |
| 2026-11-08 | [fix: allow scrolling in the edit favorites dialog (#3192)](https://github.com/localsend/localsend/commit/c833d501dd3a6ff70b9889c97772f316b8abd3d3) | samdelong |
| 2026-11-08 | [fix: Flatpak drag-and-drop for files outside Downloads (#3373)](https://github.com/localsend/localsend/commit/9f8f356a9c9c38892f803b7006279db71f940987) | loucass |
| 2026-11-08 | [fix: show "LocalSend" as title in the Linux system tray (#3374)](https://github.com/localsend/localsend/commit/8b0899323a5fce50ebf9b3ca09e60046c8c75d00) | Josephur |
| 2026-11-08 | [deps: bump flutter to 3.47.9 (#3692)](https://github.com/localsend/localsend/commit/ef8ba6526b1fceb7bac58b410f231a23bec8e655) | Tienisto |
| 2026-11-07 | [fix: release wakelock when a transfer fails (#3603)](https://github.com/localsend/localsend/commit/0ddf2536d4f5937724dbb8ea6a301bd48f26eca2) | bunnysayzz |
| 2026-11-07 | [feat: add x86_64 rpm package to release workflow (#3038)](https://github.com/localsend/localsend/commit/39f215e4f6f112d614d094c1d623847e4bd6faf1) | basil |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
