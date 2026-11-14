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
| ⭐ **Stars** | 4.5k |
| 🍴 **Forks** | 441 |
| 🐞 **Open issues + PRs** | [264](https://github.com/crmne/zapfast/issues) |
| 💻 **Languages** | Rust 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `chat` `desktop-app` `egui` `linux` `macos` `messaging` `rust` `whatsapp` `whatsapp-client` `windows` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-08-29 |
| 📦 **Latest release** | [v0.21.2](https://github.com/crmne/zapfast/releases/tag/v0.21.2) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 52.7 MB |
| 🌐 **Website** | https://zapfast.rocks/ |

## 📦 Recent releases

### [v0.21.2](https://github.com/crmne/zapfast/releases/tag/v0.21.2) — ZapFast v0.21.2
<sub>2026-11-14 · today</sub>

> ZapFast 0.21.2 lists the groups you share with someone, speaks Dutch, finds people by the start of any word in their name, and gives the macOS traffic lights room of their own when the chat list is hidden.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-v0.21.2-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast_0.21.2_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.2/zapfast-0.21.2-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`. On Fedora, `sudo dnf copr enable paolino/zapfast` and then `sudo dnf install zapfast`, which keeps ZapFast updated with the rest of your system.
> **New**
> - **A person's details list the groups you share with them.** Under the media in their info panel, each group you are both in, by name; click one to open it. Locked groups stay in the locked folder. By @Goodly58. (#786)
> - **ZapFast speaks Dutch.** The whole interface, following your system's language. By @TheDutchSmoke. (#770)
> …

### [v0.21.1](https://github.com/crmne/zapfast/releases/tag/v0.21.1) — ZapFast v0.21.1
<sub>2026-11-03 · 10d ago</sub>

> ZapFast 0.21.1 fixes the disappearing messages menu, which 0.21.0 added but never opened, lines up the info panel's header with the chat beside it, and plays videos that some encoders lay out differently.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-v0.21.1-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast_0.21.1_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.1/zapfast-0.21.1-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> **Fixed**
> - **The disappearing messages timer opens its choices.** In 0.21.0 the timer in a chat's info panel showed the current setting, but a click or Enter on it did nothing. By @crmne. (#531)
> - **The info panel's header lines up with the chat header beside it.** Its edge sat a few points lower, and on the Messages theme, where the chat header has no edge, it drew a line of its own. By @crmne; thanks @ArthurWillers, who reported it. (#639)
> …

### [v0.21.0](https://github.com/crmne/zapfast/releases/tag/v0.21.0) — ZapFast v0.21.0
<sub>2026-11-01 · 12d ago</sub>

> ZapFast 0.21.0 adds chat export, link previews on the messages you send, contact blocking, disappearing-message controls, progress and cancel for attachments, and full-size review before sending. Screen readers and the keyboard can move through messages, voice messages you have not heard are marked, downloads sort into folders, and the Linux packages install on Debian 12 again. It also fixes a crash when sound plays on some Linux systems, a link that stayed down until a restart, an update that could stop ZapFast from starting, videos that never arrived, edits and stars that went missing, and stickers that stayed blank.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-v0.21.0-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast_0.21.0_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> ![A chat with a link preview card above the message field and on a sent message](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-link-preview.png)
> ![A staged picture shown large in the chat pane, with a caption field and a strip of tiles](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-review-attachments.png)
> ![The Export chat dialog with an option to include attachments](https://github.com/crmne/zapfast/releases/download/v0.21.0/zapfast-0.21.0-export-chat.png)
> …

### [v0.20.1](https://github.com/crmne/zapfast/releases/tag/v0.20.1) — ZapFast v0.20.1
<sub>2026-10-24 · 21d ago</sub>

> ZapFast 0.20.1 fixes custom themes with see-through colours on Linux, which 0.20.0 broke, and brings the first round of contributions since: send a photo as view once, group status mentions no longer show as unsupported messages, HD copies of photos stay out of the chat, and about 140 more of the interface's words can be translated.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-v0.20.1-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast_0.20.1_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.20.1/zapfast-0.20.1-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> **New**
> - **Send a photo as view once.** By @ArthurWillers. (#597)
> - **ZapFast leaves notifications to your phone while your displays are off,** so they don't wait unseen on a sleeping computer. By @victorblino. (#596)
> …

### [v0.20.0](https://github.com/crmne/zapfast/releases/tag/v0.20.0) — ZapFast v0.20.0
<sub>2026-10-23 · 22d ago</sub>

> ZapFast 0.20.0 makes and answers WhatsApp calls: voice and video, one-to-one and, as an experiment, in groups. It rings for an incoming call, and a new Calls page lists every call. Calls are new and video calls are in alpha, so please try them, and if something breaks, point your agents at it: pull requests are very welcome. A rail beside the chat list now holds Chats, Calls, Starred and Settings. Sound and recording run on a new audio layer that talks to PipeWire directly on Linux. This release also brings group invite links and group management, starred and pinned messages, a full-window photo and video viewer, chat info in a side panel, sound in WhatsApp's videos, deletions that sync with your phone, and dozens of fixes from more than forty contributors. The prebuilt Linux packages need Ubuntu 24.04, Debian 13 or newer: Ubuntu 22.04 and Debian 12 are not supported.
> **Download ZapFast:** [Mac](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-macos-universal.dmg) · [Windows](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-x86_64-pc-windows-msvc.msi) · [Windows ARM](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-aarch64-pc-windows-msvc.msi) · [Linux](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-x86_64-unknown-linux-gnu.tar.gz) · [Linux ARM](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-aarch64-unknown-linux-gnu.tar.gz) · [AppImage](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-0.20.0-x86_64.AppImage) · [AppImage ARM](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-0.20.0-aarch64.AppImage) · [Flatpak](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-v0.20.0-x86_64.flatpak) · [Debian/Ubuntu](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast_0.20.0_amd64.deb) · [Fedora](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-0.20.0-1.x86_64.rpm)
> On a Mac, `brew install --cask crmne/tap/zapfast`. On Arch, `yay -S zapfast-bin`.
> On Windows, pick the `.msi`. The setup program (`-setup.exe`) is still attached so that installs from 0.19.0 and earlier can update through it.
> ![The Calls page in the rail beside the chat list, with recent and missed calls, the All and Missed chips, and a call-back button on each row](https://github.com/crmne/zapfast/releases/download/v0.20.0/zapfast-0.20.0-calls.png)
> *The screenshot uses ZapFast's built-in demo content.*
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [Release 0.21.2](https://github.com/crmne/zapfast/commit/a5108caae57b624f3cfc51b095fe307794107f53) | crmne |
| 2026-11-13 | [Add a WhatsApp on Linux page and a Portuguese page for Brazil](https://github.com/crmne/zapfast/commit/fe577a21bf9eca2a664860634010ea41e64116a7) | crmne |
| 2026-11-13 | [Set the site's version in the release commit itself](https://github.com/crmne/zapfast/commit/77a1e9aa24d721f6cf8132d97c575588134d1755) | crmne |
| 2026-11-13 | [Give the homepage's film its size before it loads](https://github.com/crmne/zapfast/commit/47aee939a77542a1543ccbd0d746863779f5400b) | crmne |
| 2026-11-13 | [Give the site's main pages search titles that say what ZapFast is](https://github.com/crmne/zapfast/commit/b9d50531e32d361028d2f04b81c91ad3d4ea716e) | crmne |
| 2026-11-13 | [Point the site at 0.21.1](https://github.com/crmne/zapfast/commit/527fedd5375230613963ffb183c7811a97f8e1ae) | crmne |
| 2026-11-09 | [Update fastframe to v0.16.1 (#929)](https://github.com/crmne/zapfast/commit/4497f08cee368235dedb4848990916bb40bfc88e) | renovate[bot] |
| 2026-11-08 | [Show the groups in common on a person's details (#786)](https://github.com/crmne/zapfast/commit/421d194fb45530ad0811e2b5d81be8f805c47748) | Goodly58 |
| 2026-11-08 | [Size the New chat list to its matches and open the first match with E…](https://github.com/crmne/zapfast/commit/63f09e264fc7ac17e7d3749cc4b6baa2608fc27f) | Mayank-Bhatasana |
| 2026-11-08 | [Keep a closed ZapFast running in the macOS Dock without a menu-bar it…](https://github.com/crmne/zapfast/commit/2bab073d81c95a4c33a385dcc652fd9062ff2adb) | felipefdl |

[See all commits ↗](https://github.com/crmne/zapfast/commits)

## ⬇️ Get it

```bash
git clone https://github.com/crmne/zapfast.git
```
