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
| ⭐ **Stars** | 100.4k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 79% · Rust 18% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.9 MB |
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
| 2026-11-23 | [fix: preserve extension case and leading dot in FilePathStringExt.wit…](https://github.com/localsend/localsend/commit/89881acb32c9edf6a4bdffc4e21214bf0321708e) | lingyicute |
| 2026-11-23 | [feat: group the changelog by release and show what's new after an upd…](https://github.com/localsend/localsend/commit/1be89369573775e9bc573ce236a9d59fc510767a) | ShlomoCode |
| 2026-11-23 | [docs: update changelog](https://github.com/localsend/localsend/commit/d8702511dfb074d795452a9204ba3c9473f4f01f) | Tienisto |
| 2026-11-23 | [fix: anonymous sender fingerprint (#3754)](https://github.com/localsend/localsend/commit/0d9060eeebc2b422522958ade46067d19982d3c0) | Tienisto |
| 2026-11-23 | [chore: bump rustls to 0.23.46 (#3753)](https://github.com/localsend/localsend/commit/ebd0473c79b7e84eb8b79ba767a4b3ac39d7ee3c) | Tienisto |
| 2026-11-23 | [docs: update release date](https://github.com/localsend/localsend/commit/11af648e2ad29222cac7bca967d094750f339cdd) | Tienisto |
| 2026-11-22 | [feat: Add support for Alpine Linux CLI (#3752)](https://github.com/localsend/localsend/commit/12d127724828e194566d9b9848dc97d438b52be0) | julianxhokaxhiu |
| 2026-11-22 | [fix(windows): close running app and remove autostart, Send to shortcu…](https://github.com/localsend/localsend/commit/9dddabf8e95298f90e9c1e76bd96e4c4e44c9681) | Tienisto |
| 2026-11-22 | [fix(windows): render LocalSend icon in the Share Sheet & "Share with"…](https://github.com/localsend/localsend/commit/eb61b5f10119c47161cbd20d4a1e4edd4e308489) | ShlomoCode |
| 2026-11-21 | [ci: locate makeappx in Windows SDK bin instead of App Certification K…](https://github.com/localsend/localsend/commit/19c02034291ae9ef24dc1a6611aa126115a86ad1) | Tienisto |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
