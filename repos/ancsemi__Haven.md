# ancsemi/Haven

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ancsemi/Haven)

> Self-hosted private chat: no cloud, no telemetry, no Big Tech. Discord alternative that runs on your own machine.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Self-hosted private chat server (Discord alternative) |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.1k |
| 🍴 **Forks** | 114 |
| 🐞 **Open issues + PRs** | [17](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 80% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.28.0](https://github.com/ancsemi/Haven/releases/tag/v4.28.0) — 2026-11-07 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 22.1 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.29.0-beta.5](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.5) — Haven 4.29.0-beta.5 _(pre-release)_
<sub>2026-11-13 · today</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.28.0 until the next stable.
> Changes since 4.29.0-beta.4:
> **Added**
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. Every message moves over in time order, threads and all; a Discord message that is in both is kept once, and messages that look re-posted by hand are listed and only removed when ticked. Thanks Dawnforger (#5890).
> - Bots can edit their own messages through the webhook API (`PATCH /api/webhooks/<token>/messages/<id>`). A bot only ever edits its own messages, and protected messages stay as they are.
> - A timeout now shows how long it lasts in a bar above the message box, and a forum post written during a timeout is kept instead of lost. Thanks Amnibro (#5887).
> …

### [v4.29.0-beta.4](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.4) — Haven 4.29.0-beta.4 _(pre-release)_
<sub>2026-11-11 · 2d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Back and forward on the mouse's side buttons, like a browser: back closes the thread or pop-out DM you opened, leaves a forum topic for the forum's list, or returns to the channel you came from. A side button set as a shortcut in Haven Desktop keeps doing only that.
> - The @ button also counts mentions and replies sent while you were away, and pulses while there are some (thanks Amnibro, asked for by broilpromptu).
> - Click an @mention of a person to open their profile card (#5878, asked for by birdcrazy).
> - Favorites in the emoji pickers, saved on your account (#5874, thanks Amnibro).
> …

### [v4.29.0-beta.3](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.3) — Haven 4.29.0-beta.3 _(pre-release)_
<sub>2026-11-08 · 5d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Mentions and replies: the @ button next to your name lists every message that @mentions you or replies to you, newest first, and clicking one jumps to it. A small count shows how many you have not seen yet (thanks broilpromptu). `mentions:me` in search does the same.
> - Add members to a channel from its right-click menu: pick people one by one, a whole role at a time, or All users. On a private channel it works for whoever may invite to it.
> - Blocked names (Settings > Admin > Who can sign up): words no username or display name may contain. Capitals, spaces, symbols, accents and look-alike numbers are ignored, so "B4d_W0rd" counts as "badword". Members who already have one are listed for the admin.
> - Emoji search knows far more words: Unicode's keywords plus everyday chat words, so "this" finds 👆, "dead" finds 💀 and "sus" finds 🤨. Best matches come first.
> …

### [v4.28.0](https://github.com/ancsemi/Haven/releases/tag/v4.28.0) — Haven 4.28.0
<sub>2026-11-07 · 7d ago</sub>

> **Added**
> - Settings are split into a few pages, so each one is short: Appearance, Chat & media, Notifications and so on for you, and Server, People & roles, Safety, Content, Network & scale and Bots & data for admins. Longer explanations fold behind an ⓘ button (thanks Amnibro, #5838).
> - AutoMod Quarantine, an experimental plugin (thanks Amnibro, #5836): holds links in chat until they are checked, by an AI model on your own server or a cloud AI a moderator picks. Off unless a member turns the plugin on and, for the server parts, an admin turns on Settings > Safety > Auto-Mod > AI link checks. Only the link is ever sent to an AI, never the message. See docs/automod.md.
> - Send later takes files: attach them in the Send later window, and files already waiting in the message box come along.
> - Blocked file types under Settings > Admin > Content > Uploads & Limits (#5833): list types such as exe, bat or dll, and nobody can upload files of those types. Empty by default.
> - Listen Together plays Spotify playlists and albums: sharing one queues its songs in order, found on YouTube like single Spotify songs. It used to play one song named after the playlist.
> …

### [v4.29.0-beta.2](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.2) — Haven 4.29.0-beta.2 _(pre-release)_
<sub>2026-11-06 · 8d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Your profile picture shows in the account bar at the top of the sidebar, in your chosen shape. Clicking it opens Edit Profile, and the server connection light sits on its top-left corner.
> - Your custom status shows under your name in the account bar, or Set status when you have none, and clicking it opens the status picker (thanks reverb256, #5859).
> - Reading a channel on one device clears its unread badge and closes its notification on your other devices too (thanks Roolk).
> - The donors list calls the people who give every month Monthly Supporters.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [Release 4.29.0-beta.5](https://github.com/ancsemi/Haven/commit/875ad21c31b0e7ec05bbb2e311c35c26821793b5) | ancsemi |
| 2026-11-13 | [Let the admin merge a channel into another, for Ferry import duplicat…](https://github.com/ancsemi/Haven/commit/7d07fd3ce5cfd8dc8c1af4773259feaac5028486) | Dawnforger |
| 2026-11-13 | [Serve .aac, .flac and .opus uploads under their standard types](https://github.com/ancsemi/Haven/commit/ebb9ee7710d8a09c672992c5c8587c783173aa41) | ancsemi |
| 2026-11-12 | [Add a switch to turn off back and forward on the mouse side buttons (…](https://github.com/ancsemi/Haven/commit/2193bc9f979d4ffff59afb2a42061c7c71009180) | ancsemi |
| 2026-11-12 | [Fold link previews after the second in a message, add a Start link pr…](https://github.com/ancsemi/Haven/commit/e52c5401cb937923562224433d10e4ce60673304) | Amnibro |
| 2026-11-12 | [Show how long a timeout lasts, and keep a forum post written during o…](https://github.com/ancsemi/Haven/commit/40696c9feff9a917cec01a9c4916b93df513aa7b) | Amnibro |
| 2026-11-11 | [Let bots edit their own messages through the webhook API](https://github.com/ancsemi/Haven/commit/cba1285a6b0c3972b5bcffc9a3f98829f366bbd3) | ancsemi |
| 2026-11-11 | [Keep muted sub-channels inside their own category](https://github.com/ancsemi/Haven/commit/8064279a40ad3dc7b5cbaba5b700d7ac4ec328cb) | ancsemi |
| 2026-11-11 | [Clear a forum's unread topics from the sidebar mark-read actions](https://github.com/ancsemi/Haven/commit/49d4231611a473f3c0ffecf60aea89f2a5dcebc2) | ancsemi |
| 2026-11-11 | [Release 4.29.0-beta.4](https://github.com/ancsemi/Haven/commit/9ecef9c052f8389be8c078267c51fb30770f1a60) | ancsemi |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
