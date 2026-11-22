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
| ⭐ **Stars** | 100.2k |
| 🍴 **Forks** | 5.8k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 79% · Rust 18% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 24.2 MB |
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
| 2026-11-22 | [fix(windows): render LocalSend icon in the Share Sheet & "Share with"…](https://github.com/localsend/localsend/commit/eb61b5f10119c47161cbd20d4a1e4edd4e308489) | ShlomoCode |
| 2026-11-21 | [ci: locate makeappx in Windows SDK bin instead of App Certification K…](https://github.com/localsend/localsend/commit/19c02034291ae9ef24dc1a6611aa126115a86ad1) | Tienisto |
| 2026-11-21 | [release: 1.19.0+65 (#3745)](https://github.com/localsend/localsend/commit/5c70ff3648265858f46634633134ab19b783ba41) | Tienisto |
| 2026-11-21 | [docs: clarify Debian startup changelog entry (#3746)](https://github.com/localsend/localsend/commit/da72a45a5b00eb60793e138bc42ae43b4d9863a7) | ShlomoCode |
| 2026-11-21 | [docs: update changelog for 1.19.0 (#3744)](https://github.com/localsend/localsend/commit/94b09400ef004c1dd1a86c25e5c3a89f2e17604a) | Tienisto |
| 2026-11-21 | [docs: update changelog (#3500)](https://github.com/localsend/localsend/commit/dffc9bedb7d23eaa63ea8b534ce72dc5b418069f) | ShlomoCode |
| 2026-11-21 | [i18n: add missing translations for all locales (#3743)](https://github.com/localsend/localsend/commit/855c4aad968e55b624e6e6173c88043e309042c3) | Tienisto |
| 2026-11-21 | [Update tr.json (#3710)](https://github.com/localsend/localsend/commit/063ae5e22887215c895e6a2ba465ef2d75f72388) | mikropsoft |
| 2026-11-21 | [feat: show HTTPS badge in device list tile when encryption is enabled…](https://github.com/localsend/localsend/commit/e13200e1a9c1b1073bbe9b58bfe6ccb4756ae879) | Tienisto |
| 2026-11-21 | [fix(linux): require only Ayatana appindicator in the deb and name its…](https://github.com/localsend/localsend/commit/26cc8f997aa3f7ad789c12500a8b7206cfbb3ddc) | Tienisto |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
