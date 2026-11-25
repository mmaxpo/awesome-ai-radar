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
| ⭐ **Stars** | 100.8k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 79% · Rust 18% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-24 (yesterday) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.19.0](https://github.com/localsend/localsend/releases/tag/v1.19.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.8 MB |
| 🌐 **Website** | https://localsend.org |

## 📦 Recent releases

### [v1.19.0](https://github.com/localsend/localsend/releases/tag/v1.19.0)
<sub>2026-11-24 · yesterday</sub>

> This release also added the rpm package for the first time (e.g. for Fedora users).
> Please note a breaking change in the CLI when sending files.
> - feat: make sending checksums opt-in (@Tienisto)
> - feat: format timestamps using system date and time settings (@ShlomoCode)
> - feat: add keyboard shortcuts to accept or decline incoming transfers (@Tienisto)
> - feat: restore hashtag codes for connecting to devices (@Tienisto)
> …

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

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [ci: build android with JDK 21 to match F-Droid (#3758)](https://github.com/localsend/localsend/commit/44f48f18a5503c43873570ff489d27ff1983e198) | Tienisto |
| 2026-11-23 | [docs: update changelog](https://github.com/localsend/localsend/commit/b3b5f647d73e734636014c1cf2b44a7cbafd1fb6) | Tienisto |
| 2026-11-23 | [fix: drop i18n from changelog content (#3757)](https://github.com/localsend/localsend/commit/6f7f49820371f72a292194dc5cdb0f50ba4d07f9) | Tienisto |
| 2026-11-23 | [Fix message input dialog overflow with large text (#3749)](https://github.com/localsend/localsend/commit/58e742179572a53a45e557e87231d15d888470a7) | ArtemChikolaev |
| 2026-11-23 | [fix: preserve extension case and leading dot in FilePathStringExt.wit…](https://github.com/localsend/localsend/commit/89881acb32c9edf6a4bdffc4e21214bf0321708e) | lingyicute |
| 2026-11-23 | [feat: group the changelog by release and show what's new after an upd…](https://github.com/localsend/localsend/commit/1be89369573775e9bc573ce236a9d59fc510767a) | ShlomoCode |
| 2026-11-23 | [docs: update changelog](https://github.com/localsend/localsend/commit/d8702511dfb074d795452a9204ba3c9473f4f01f) | Tienisto |
| 2026-11-23 | [fix: anonymous sender fingerprint (#3754)](https://github.com/localsend/localsend/commit/0d9060eeebc2b422522958ade46067d19982d3c0) | Tienisto |
| 2026-11-23 | [chore: bump rustls to 0.23.46 (#3753)](https://github.com/localsend/localsend/commit/ebd0473c79b7e84eb8b79ba767a4b3ac39d7ee3c) | Tienisto |
| 2026-11-23 | [docs: update release date](https://github.com/localsend/localsend/commit/11af648e2ad29222cac7bca967d094750f339cdd) | Tienisto |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
