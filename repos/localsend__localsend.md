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
| ⭐ **Stars** | 100.1k |
| 🍴 **Forks** | 5.7k |
| 🐞 **Open issues + PRs** | [1.0k](https://github.com/localsend/localsend/issues) |
| 💻 **Languages** | Dart 78% · Rust 18% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `flutter` `file-sharing` `dart` `flutter-apps` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2022-12-16 |
| 📦 **Latest release** | [v1.18.2](https://github.com/localsend/localsend/releases/tag/v1.18.2) — 2026-08-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.3 MB |
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
| 2026-11-21 | [fix(linux): require only Ayatana appindicator in the deb and name its…](https://github.com/localsend/localsend/commit/26cc8f997aa3f7ad789c12500a8b7206cfbb3ddc) | Tienisto |
| 2026-11-21 | [fix(linux): name rpm desktop file after the application id so KWin sh…](https://github.com/localsend/localsend/commit/296bcf7490091bc6874f0d3c0ef043d927dc5d9d) | Tienisto |
| 2026-11-21 | [fix(android): preserve gallery file modification times (#3715)](https://github.com/localsend/localsend/commit/2fe29dce145491db12228136ee8b0d2e662f9cc3) | ShlomoCode |
| 2026-11-21 | [fix: bound inline text previews to prevent large-message freezes (#3737)](https://github.com/localsend/localsend/commit/1f36be759864c24e8cfada70d225547483c05906) | kneeyard126 |
| 2026-11-20 | [fix(linux): install rpm icon without setuid, set StartupWMClass and r…](https://github.com/localsend/localsend/commit/12ec31310382d0e7a6f54697ebc9c7c64f833ccd) | Tienisto |
| 2026-11-20 | [fix: avoid division by zero on the progress page when a file fails in…](https://github.com/localsend/localsend/commit/8e999736643547a3b375e1d442d160fa852db6ef) | Tienisto |
| 2026-11-20 | [feat(linux): add software rendering toggle with automatic fallback af…](https://github.com/localsend/localsend/commit/b1b9abc7201b8afaa3ba7027575a2673fb6e78ee) | Tienisto |
| 2026-11-19 | [fix: stop a send session that was cancelled while prepare-upload was …](https://github.com/localsend/localsend/commit/e05d12a9c0fd4d8c0245d2ec5c3c177e7e0f759b) | Tienisto |
| 2026-11-18 | [fix: rank link-local IPv6 channels after IPv4 when choosing an addres…](https://github.com/localsend/localsend/commit/a6ee93b55340d7ef5d2519842503c7887f0e7479) | Tienisto |
| 2026-11-18 | [fix: limit connection setup for pinned HTTP clients to 5 seconds (#3726)](https://github.com/localsend/localsend/commit/541689d1a4e8fd552772109b82ae75ecd7722afd) | Tienisto |

[See all commits ↗](https://github.com/localsend/localsend/commits)

## ⬇️ Get it

```bash
git clone https://github.com/localsend/localsend.git
```
