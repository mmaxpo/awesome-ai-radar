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
| 🍴 **Forks** | 115 |
| 🐞 **Open issues + PRs** | [14](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 80% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-15 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 21.3 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.30.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.1) — Haven 4.30.0-beta.1 _(pre-release)_
<sub>2026-11-15 · today</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> It has everything in 4.29.0, plus these, which are not in a stable yet:
> **Added**
> - Mass-select in forums: a Select button on the forum toolbar and a Select entry in a topic's right-click menu pick topics for moving or deleting several at once, with Select all. Phone-width screens had no way into selection mode in a forum. Moving offers forums only and takes the topics' replies along. Thanks Amnibro (#5892).
> - A bell in the reply bar chooses whether your reply sends a push notification to the person you reply to (on by default, remembered on this device). With it on, a reply reaches them like an @mention would, including through a server muted with "except @mentions", and replies inside a thread now notify their author too. Thanks Bo0sted (#5891).
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. The channel merged into keeps its name, settings, permissions and members; every message of the other moves into it in time order, threads and all, and the other is deleted. A Discord message that is in both (imported in one, relayed by Ferry in the other) is kept once, with its replies, reactions and pin. Messages that look re-posted by hand from Discord (the same text, posted later in Haven) are listed with both copies, and only the ticked ones go, leaving the Discord copy with its real author and time. Ferry links, webhooks, scheduled messages and role menus come along, a later history import lands in the merged channel, and people who were caught up stay caught up. Protected messages always stay.
> …

### [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — Haven 4.29.0
<sub>2026-11-15 · today</sub>

> **Added**
> - Call controls in fullscreen (thanks Roolk, #5849): mute, deafen, camera, screen share, call settings and leave stay on screen over a fullscreen camera or screen share, and a picker switches which stream is shown without leaving fullscreen.
> - Video players in chat have Theater (as wide as the chat) and Fullscreen buttons: YouTube cards, uploaded videos and videos in link previews.
> - Platform emoji built into Haven: Windows, Mac, iPhone, Android and Linux, under Platforms in the emoji picker. They work in messages, reactions and role menus.
> - Role menus: each role's emoji is picked from a searchable list of every emoji, the server's custom ones and Haven's own included. A role named after a platform starts with its icon.
> - Add members to a channel that already exists: right-click it and pick people one by one, a whole role at a time, or All users. People already in it are shown, and banned people are left out. It works for the admin and anyone who can invite people, and on a private channel for whoever may invite to it (its creator or a moderator there).
> …

### [v4.29.0-beta.5](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.5) — Haven 4.29.0-beta.5 _(pre-release)_
<sub>2026-11-13 · yesterday</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.28.0 until the next stable.
> Changes since 4.29.0-beta.4:
> **Added**
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. Every message moves over in time order, threads and all; a Discord message that is in both is kept once, and messages that look re-posted by hand are listed and only removed when ticked. Thanks Dawnforger (#5890).
> - Bots can edit their own messages through the webhook API (`PATCH /api/webhooks/<token>/messages/<id>`). A bot only ever edits its own messages, and protected messages stay as they are.
> - A timeout now shows how long it lasts in a bar above the message box, and a forum post written during a timeout is kept instead of lost. Thanks Amnibro (#5887).
> …

### [v4.29.0-beta.4](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.4) — Haven 4.29.0-beta.4 _(pre-release)_
<sub>2026-11-11 · 3d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Back and forward on the mouse's side buttons, like a browser: back closes the thread or pop-out DM you opened, leaves a forum topic for the forum's list, or returns to the channel you came from. A side button set as a shortcut in Haven Desktop keeps doing only that.
> - The @ button also counts mentions and replies sent while you were away, and pulses while there are some (thanks Amnibro, asked for by broilpromptu).
> - Click an @mention of a person to open their profile card (#5878, asked for by birdcrazy).
> - Favorites in the emoji pickers, saved on your account (#5874, thanks Amnibro).
> …

### [v4.29.0-beta.3](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.3) — Haven 4.29.0-beta.3 _(pre-release)_
<sub>2026-11-08 · 6d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Mentions and replies: the @ button next to your name lists every message that @mentions you or replies to you, newest first, and clicking one jumps to it. A small count shows how many you have not seen yet (thanks broilpromptu). `mentions:me` in search does the same.
> - Add members to a channel from its right-click menu: pick people one by one, a whole role at a time, or All users. On a private channel it works for whoever may invite to it.
> - Blocked names (Settings > Admin > Who can sign up): words no username or display name may contain. Capitals, spaces, symbols, accents and look-alike numbers are ignored, so "B4d_W0rd" counts as "badword". Members who already have one are listed for the admin.
> - Emoji search knows far more words: Unicode's keywords plus everyday chat words, so "this" finds 👆, "dead" finds 💀 and "sus" finds 🤨. Best matches come first.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [Release 4.30.0-beta.1](https://github.com/ancsemi/Haven/commit/875d8176e8a93c114d6cf30e7fd176a63e545315) | ancsemi |
| 2026-11-15 | [Website and changelog: Haven 4.29.0 and Desktop 1.8.4 are out](https://github.com/ancsemi/Haven/commit/494eef9fa98ce57582144c0c69cc24f047a57dd0) | ancsemi |
| 2026-11-15 | [Bump cache tags on client files changed since 4.28.0](https://github.com/ancsemi/Haven/commit/21555e48536f2ca360c47e3180877ef5e02ddc9f) | ancsemi |
| 2026-11-15 | [Open the link preview size menu above threads and pop-out DMs](https://github.com/ancsemi/Haven/commit/1bdaef7d43e463d9a98f7090cd1225db321d932d) | ancsemi |
| 2026-11-15 | [Refuse Add all members on hidden-code channels and under private pare…](https://github.com/ancsemi/Haven/commit/a1dfabfb9207883d0bcb3ddf74f8530bfcd92d8b) | ancsemi |
| 2026-11-14 | [Use the accent text colour on forum selection marks, bump cache tags,…](https://github.com/ancsemi/Haven/commit/6c176a764ccfc2dd15619cb26dcff59c5d604486) | ancsemi |
| 2026-11-14 | [Mass-select forum topics to move or delete several at once (#5892)](https://github.com/ancsemi/Haven/commit/1e06adfa5036eed2f94ab7f3385757ac27156e4c) | Amnibro |
| 2026-11-14 | [Let the sender choose whether a reply pushes its author (#5891)](https://github.com/ancsemi/Haven/commit/9c2f038f3544359994048b8b0db352091bf776e3) | Bo0sted |
| 2026-11-13 | [Release 4.29.0-beta.5](https://github.com/ancsemi/Haven/commit/875ad21c31b0e7ec05bbb2e311c35c26821793b5) | ancsemi |
| 2026-11-13 | [Let the admin merge a channel into another, for Ferry import duplicat…](https://github.com/ancsemi/Haven/commit/7d07fd3ce5cfd8dc8c1af4773259feaac5028486) | Dawnforger |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
