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
| 🍴 **Forks** | 118 |
| 🐞 **Open issues + PRs** | [15](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 80% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 24.7 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.30.0-beta.2](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.2) — Haven 4.30.0-beta.2 _(pre-release)_
<sub>2026-11-16 · yesterday</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.1:
> **Added**
> - Manage members replaces Add members in a channel's right-click menu. Everyone is listed with the people in the channel ticked: tick someone to add them, untick to remove them, by person, by role, or with All users, which adds everyone when ticked and removes everyone when unticked. Nothing changes until you press the button, and removing asks first. Whoever may add people to a channel may take them out again, and so may anyone with Kick there; only the admin removes an admin or a guest, and others only remove people ranked below them (a private channel's creator may remove anyone else in it). A role hidden on profile cards no longer shows in this list.
> - Emote names keep their capitals (asked for by gitty323, #5895): upload `HOLY` and `holy` as two different emotes, as Twitch and 7TV do. `:holy:` still finds `HOLY` when there is no exact match, so older messages keep working. A new switch, Settings > Chat & media > Turn emote names into emotes when I send, is off by default. When it is on, a word you type that is exactly a custom emote's name, capitals included, is sent as that emote, with no colons or picker. Code, links, mentions and slash commands are left alone. An admin can make the switch part of Defaults for New Members, so it starts on for everyone on their server (thanks Amnibro).
> - Sort your DMs: the new sort button in the Direct Messages header picks Latest message, Alphabetical or Manual order. The pick and the order you arranged by hand follow your account to every device, and pinned DMs stay on top whatever you choose (thanks Amnibro).
> …

### [v4.30.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.1) — Haven 4.30.0-beta.1 _(pre-release)_
<sub>2026-11-15 · 3d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> It has everything in 4.29.0, plus these, which are not in a stable yet:
> **Added**
> - Mass-select in forums: a Select button on the forum toolbar and a Select entry in a topic's right-click menu pick topics for moving or deleting several at once, with Select all. Phone-width screens had no way into selection mode in a forum. Moving offers forums only and takes the topics' replies along. Thanks Amnibro (#5892).
> - A bell in the reply bar chooses whether your reply sends a push notification to the person you reply to (on by default, remembered on this device). With it on, a reply reaches them like an @mention would, including through a server muted with "except @mentions", and replies inside a thread now notify their author too. Thanks Bo0sted (#5891).
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. The channel merged into keeps its name, settings, permissions and members; every message of the other moves into it in time order, threads and all, and the other is deleted. A Discord message that is in both (imported in one, relayed by Ferry in the other) is kept once, with its replies, reactions and pin. Messages that look re-posted by hand from Discord (the same text, posted later in Haven) are listed with both copies, and only the ticked ones go, leaving the Discord copy with its real author and time. Ferry links, webhooks, scheduled messages and role menus come along, a later history import lands in the merged channel, and people who were caught up stay caught up. Protected messages always stay.
> …

### [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — Haven 4.29.0
<sub>2026-11-15 · 3d ago</sub>

> **Added**
> - Call controls in fullscreen (thanks Roolk, #5849): mute, deafen, camera, screen share, call settings and leave stay on screen over a fullscreen camera or screen share, and a picker switches which stream is shown without leaving fullscreen.
> - Video players in chat have Theater (as wide as the chat) and Fullscreen buttons: YouTube cards, uploaded videos and videos in link previews.
> - Platform emoji built into Haven: Windows, Mac, iPhone, Android and Linux, under Platforms in the emoji picker. They work in messages, reactions and role menus.
> - Role menus: each role's emoji is picked from a searchable list of every emoji, the server's custom ones and Haven's own included. A role named after a platform starts with its icon.
> - Add members to a channel that already exists: right-click it and pick people one by one, a whole role at a time, or All users. People already in it are shown, and banned people are left out. It works for the admin and anyone who can invite people, and on a private channel for whoever may invite to it (its creator or a moderator there).
> …

### [v4.29.0-beta.5](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.5) — Haven 4.29.0-beta.5 _(pre-release)_
<sub>2026-11-13 · 4d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.28.0 until the next stable.
> Changes since 4.29.0-beta.4:
> **Added**
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. Every message moves over in time order, threads and all; a Discord message that is in both is kept once, and messages that look re-posted by hand are listed and only removed when ticked. Thanks Dawnforger (#5890).
> - Bots can edit their own messages through the webhook API (`PATCH /api/webhooks/<token>/messages/<id>`). A bot only ever edits its own messages, and protected messages stay as they are.
> - A timeout now shows how long it lasts in a bar above the message box, and a forum post written during a timeout is kept instead of lost. Thanks Amnibro (#5887).
> …

### [v4.29.0-beta.4](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.4) — Haven 4.29.0-beta.4 _(pre-release)_
<sub>2026-11-11 · 6d ago</sub>

> Early access release. It goes to servers that turned on Settings > Admin > "Early access updates" and to the `:beta` Docker image. Everyone else stays on the stable version.
> **New**
> - Back and forward on the mouse's side buttons, like a browser: back closes the thread or pop-out DM you opened, leaves a forum topic for the forum's list, or returns to the channel you came from. A side button set as a shortcut in Haven Desktop keeps doing only that.
> - The @ button also counts mentions and replies sent while you were away, and pulses while there are some (thanks Amnibro, asked for by broilpromptu).
> - Click an @mention of a person to open their profile card (#5878, asked for by birdcrazy).
> - Favorites in the emoji pickers, saved on your account (#5874, thanks Amnibro).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Explain the catches in the merged PRs and bump the emoji picker cache…](https://github.com/ancsemi/Haven/commit/244e86c8698c13c38201691420685fd3db5abd55) | ancsemi |
| 2026-11-18 | [Show picture borders in threads and on your own avatar at the bottom …](https://github.com/ancsemi/Haven/commit/e598077254dcae77ce91a1e70f7aec97e3339ac3) | ancsemi |
| 2026-11-18 | [Give back a message or forum post that auto-mod refused](https://github.com/ancsemi/Haven/commit/640ea7ac35005fccb68af42e30cbbc4f72cc4852) | ancsemi |
| 2026-11-18 | [Retry relayed tracks that fail to connect and check for missing ones …](https://github.com/ancsemi/Haven/commit/d6907a5d4e3d1361a2299d532e1ef69aef8899cf) | ancsemi |
| 2026-11-18 | [Keep the channel list usable in the Compact layout when Join and Crea…](https://github.com/ancsemi/Haven/commit/49e17c729676ac32b84f476bff44680acf4496b4) | Amnibro |
| 2026-11-18 | [Keep a "Missed call" line in the chat when a DM call goes unanswered …](https://github.com/ancsemi/Haven/commit/1addb8395a0a64162526296da7f2a3fab422e21e) | Amnibro |
| 2026-11-18 | [Encrypt mobile push payloads to the device (#5871) (#5873)](https://github.com/ancsemi/Haven/commit/c0bf393b8c59e310e1342ebcb75732ee5fd06f00) | Amnibro |
| 2026-11-18 | [Feat/shared call settings (#5903)](https://github.com/ancsemi/Haven/commit/4bc9bb540ad3bbcc5ea022fd36cbe7112878e118) | Roolk |
| 2026-11-18 | [Lead the quick reaction row with your favorites, then your most-used …](https://github.com/ancsemi/Haven/commit/ca7934c38e93496116fbfc49814a76ee2b978747) | Amnibro |
| 2026-11-18 | [[feat] More profile customization (#5900)](https://github.com/ancsemi/Haven/commit/e9ead9eb5791155ce3a62c99d10528207558724a) | Bo0sted |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
