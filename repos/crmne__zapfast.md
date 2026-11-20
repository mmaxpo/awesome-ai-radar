# crmne/zapfast

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/crmne/zapfast)

> ZapFast: a fast, native WhatsApp client in Rust and egui

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Native WhatsApp desktop client written in Rust |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.8k |
| 🍴 **Forks** | 487 |
| 🐞 **Open issues + PRs** | [295](https://github.com/crmne/zapfast/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `chat` `desktop-app` `egui` `linux` `macos` `messaging` `rust` `whatsapp` `whatsapp-client` `windows` |
| 🕒 **Last activity** | 2026-11-17 (2d ago) |
| 📅 **Created** | 2026-08-29 |
| 📦 **Latest release** | [v0.21.3](https://github.com/crmne/zapfast/releases/tag/v0.21.3) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 62.3 MB |
| 🌐 **Website** | https://zapfast.rocks/ |

## 📦 Recent releases

### [v0.21.3](https://github.com/crmne/zapfast/releases/tag/v0.21.3) — ZapFast v0.21.3
<sub>2026-11-17 · 3d ago</sub>

> ZapFast 0.21.3 is a batch of fixes: messages that stayed on "Waiting for this message", the window flickering on Windows, a first sync that wrote gigabytes to disk, the macOS accent picker typing two letters, the newest emoji, and calls that dropped when Accept was clicked twice.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-0.21.3-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-0.21.3-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-v0.21.3-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast_0.21.3_amd64.deb) · [Fedora/openSUSE](https://github.com/crmne/zapfast/releases/download/v0.21.3/zapfast-0.21.3-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`. On Fedora, `sudo dnf copr enable paolino/zapfast` and then `sudo dnf install zapfast`, which keeps ZapFast updated with the rest of your system.
> **Fixed**
> - **Messages no longer stay on "Waiting for this message".** Messages from some contacts' linked devices could never be read, on ZapFast or on the phone, since 0.21.2. ZapFast now uses whatsapp-rust's fixes for checking those devices' identities, and asks again instead of giving up. By @crmne; thanks @XylotoGhost, who reported it. (#1052)
> - **The window no longer flickers on Windows with NVIDIA graphics.** A frame of plain background colour flashed now and then, while typing or not. Fixed upstream in egui by @sknowledge1, who found the cause, and carried in ZapFast until egui releases it; thanks @neorai for the report and @arachnoise, @Mesazane and @sknowledge1 for narrowing it down. (#945)
> …

### [v0.21.2](https://github.com/crmne/zapfast/releases/tag/v0.21.2) — ZapFast v0.21.2
<sub>2026-11-14 · 5d ago</sub>

> ZapFast 0.21.2 lists the groups you share with someone, speaks Dutch, finds people by the start of any word in their name, and gives the macOS traffic lights room of their own when the chat list is hidden.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast_0.21.2_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`. On Fedora, `sudo dnf copr enable paolino/zapfast` and then `sudo dnf install zapfast`, which keeps ZapFast updated with the rest of your system.
> **New**
> - **A person's details list the groups you share with them.** Under the media in their info panel, each group you are both in, by name; click one to open it. Locked groups stay in the locked folder. By @Goodly58. (#786)
> - **ZapFast speaks Dutch.** The whole interface, following your system's language. By @TheDutchSmoke. (#770)
> …

### [v0.21.1](https://github.com/crmne/zapfast/releases/tag/v0.21.1) — ZapFast v0.21.1
<sub>2026-11-03 · 16d ago</sub>

> ZapFast 0.21.1 fixes the disappearing messages menu, which 0.21.0 added but never opened, lines up the info panel's header with the chat beside it, and plays videos that some encoders lay out differently.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast_0.21.1_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> **Fixed**
> - **The disappearing messages timer opens its choices.** In 0.21.0 the timer in a chat's info panel showed the current setting, but a click or Enter on it did nothing. By @crmne. (#531)
> - **The info panel's header lines up with the chat header beside it.** Its edge sat a few points lower, and on the Messages theme, where the chat header has no edge, it drew a line of its own. By @crmne; thanks @ArthurWillers, who reported it. (#639)
> …

### [v0.21.0](https://github.com/crmne/zapfast/releases/tag/v0.21.0) — ZapFast v0.21.0
<sub>2026-11-01 · 18d ago</sub>

> ZapFast 0.21.0 adds chat export, link previews on the messages you send, contact blocking, disappearing-message controls, progress and cancel for attachments, and full-size review before sending. Screen readers and the keyboard can move through messages, voice messages you have not heard are marked, downloads sort into folders, and the Linux packages install on Debian 12 again. It also fixes a crash when sound plays on some Linux systems, a link that stayed down until a restart, an update that could stop ZapFast from starting, videos that never arrived, edits and stars that went missing, and stickers that stayed blank.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast_0.21.0_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> ![A chat with a link preview card above the message field and on a sent message](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-link-preview.png)
> ![A staged picture shown large in the chat pane, with a caption field and a strip of tiles](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-review-attachments.png)
> ![The Export chat dialog with an option to include attachments](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-export-chat.png)
> …

### [v0.20.1](https://github.com/crmne/zapfast/releases/tag/v0.20.1) — ZapFast v0.20.1
<sub>2026-10-24 · 27d ago</sub>

> ZapFast 0.20.1 fixes custom themes with see-through colours on Linux, which 0.20.0 broke, and brings the first round of contributions since: send a photo as view once, group status mentions no longer show as unsupported messages, HD copies of photos stay out of the chat, and about 140 more of the interface's words can be translated.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast_0.20.1_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> **New**
> - **Send a photo as view once.** By @ArthurWillers. (#597)
> - **ZapFast leaves notifications to your phone while your displays are off,** so they don't wait unseen on a sleeping computer. By @victorblino. (#596)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Release 0.21.3](https://github.com/crmne/zapfast/commit/a6f0f624a4a82dbdc5b0b08e721794fbe943348a) | crmne |
| 2026-11-17 | [Stop quitting from waiting on a busy account for good](https://github.com/crmne/zapfast/commit/dbab1b05cbd79fdc040ecedc76165ae0abf40b29) | crmne |
| 2026-11-17 | [Commit each history chunk and each run of queued events once](https://github.com/crmne/zapfast/commit/1b4e2d5307cc38eb47b22fec58ceedfd70ae8635) | crmne |
| 2026-11-17 | [Type only the chosen accent with the macOS press-and-hold picker](https://github.com/crmne/zapfast/commit/964cdbcb457e4f4ffe214bcb018315ae13accd3a) | crmne |
| 2026-11-17 | [Stop the window flickering on Windows with NVIDIA](https://github.com/crmne/zapfast/commit/afe62d0005cd87d2a83756792b588058f7f908c0) | crmne |
| 2026-11-17 | [Show the unread count on the macOS Dock with fastframe 0.17.1](https://github.com/crmne/zapfast/commit/0c450859e02bc8558a51266320201198b4c7d090) | crmne |
| 2026-11-17 | [Move whatsapp-rust to upstream main for companion identity recovery](https://github.com/crmne/zapfast/commit/2884938da9c669673fe40ca70d261237c31d0704) | crmne |
| 2026-11-17 | [Write out the names a forwarded message mentions](https://github.com/crmne/zapfast/commit/71b7962e990042d9b8d9ad808fb82e7b25002b0b) | crmne |
| 2026-11-17 | [Download album photos and videos by themselves as they come into view](https://github.com/crmne/zapfast/commit/c934d1131537e58b779f8b3dc4ac6b2b7e871c37) | crmne |
| 2026-11-17 | [Draw Emoji 18.0 and offer only emoji the bundled font draws](https://github.com/crmne/zapfast/commit/ef88a0a7ad85e2fdf29f37b554459bf620a14b9f) | crmne |

[See all commits ↗](https://github.com/crmne/zapfast/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crmne/zapfast.git
```
