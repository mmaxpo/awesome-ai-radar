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
| ⭐ **Stars** | 1.2k |
| 🍴 **Forks** | 124 |
| 🐞 **Open issues + PRs** | [17](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 81% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.5 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.30.0-beta.3](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.3) — Haven 4.30.0-beta.3 _(pre-release)_
<sub>2026-11-20 · 3d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.2:
> **Added**
> - More profile customization (thanks Bo0sted, #5900): pick a banner color in Edit Profile or let it follow your avatar, upload and crop a banner picture (with its own size limit in Uploads & Limits), and give your profile card a two-color theme it fades between.
> - Call settings everywhere (thanks Roolk, #5903): Settings has a new Voice & video page with every call setting, usable without joining a call, plus Test microphone (with Hear myself) and Test camera. The fullscreen call popup shows the same full set of settings instead of three dropdowns.
> - The quick reaction row leads with your favorites, then the reactions you use most, then the usual defaults (thanks Amnibro, #5902). A row you customized still wins, and its editor has a Reset to automatic button.
> …

### [v4.30.0-beta.2](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.2) — Haven 4.30.0-beta.2 _(pre-release)_
<sub>2026-11-16 · 7d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.1:
> **Added**
> - Manage members replaces Add members in a channel's right-click menu. Everyone is listed with the people in the channel ticked: tick someone to add them, untick to remove them, by person, by role, or with All users, which adds everyone when ticked and removes everyone when unticked. Nothing changes until you press the button, and removing asks first. Whoever may add people to a channel may take them out again, and so may anyone with Kick there; only the admin removes an admin or a guest, and others only remove people ranked below them (a private channel's creator may remove anyone else in it). A role hidden on profile cards no longer shows in this list.
> - Emote names keep their capitals (asked for by gitty323, #5895): upload `HOLY` and `holy` as two different emotes, as Twitch and 7TV do. `:holy:` still finds `HOLY` when there is no exact match, so older messages keep working. A new switch, Settings > Chat & media > Turn emote names into emotes when I send, is off by default. When it is on, a word you type that is exactly a custom emote's name, capitals included, is sent as that emote, with no colons or picker. Code, links, mentions and slash commands are left alone. An admin can make the switch part of Defaults for New Members, so it starts on for everyone on their server (thanks Amnibro).
> - Sort your DMs: the new sort button in the Direct Messages header picks Latest message, Alphabetical or Manual order. The pick and the order you arranged by hand follow your account to every device, and pinned DMs stay on top whatever you choose (thanks Amnibro).
> …

### [v4.30.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.1) — Haven 4.30.0-beta.1 _(pre-release)_
<sub>2026-11-15 · 8d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> It has everything in 4.29.0, plus these, which are not in a stable yet:
> **Added**
> - Mass-select in forums: a Select button on the forum toolbar and a Select entry in a topic's right-click menu pick topics for moving or deleting several at once, with Select all. Phone-width screens had no way into selection mode in a forum. Moving offers forums only and takes the topics' replies along. Thanks Amnibro (#5892).
> - A bell in the reply bar chooses whether your reply sends a push notification to the person you reply to (on by default, remembered on this device). With it on, a reply reaches them like an @mention would, including through a server muted with "except @mentions", and replies inside a thread now notify their author too. Thanks Bo0sted (#5891).
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. The channel merged into keeps its name, settings, permissions and members; every message of the other moves into it in time order, threads and all, and the other is deleted. A Discord message that is in both (imported in one, relayed by Ferry in the other) is kept once, with its replies, reactions and pin. Messages that look re-posted by hand from Discord (the same text, posted later in Haven) are listed with both copies, and only the ticked ones go, leaving the Discord copy with its real author and time. Ferry links, webhooks, scheduled messages and role menus come along, a later history import lands in the merged channel, and people who were caught up stay caught up. Protected messages always stay.
> …

### [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — Haven 4.29.0
<sub>2026-11-15 · 8d ago</sub>

> **Added**
> - Call controls in fullscreen (thanks Roolk, #5849): mute, deafen, camera, screen share, call settings and leave stay on screen over a fullscreen camera or screen share, and a picker switches which stream is shown without leaving fullscreen.
> - Video players in chat have Theater (as wide as the chat) and Fullscreen buttons: YouTube cards, uploaded videos and videos in link previews.
> - Platform emoji built into Haven: Windows, Mac, iPhone, Android and Linux, under Platforms in the emoji picker. They work in messages, reactions and role menus.
> - Role menus: each role's emoji is picked from a searchable list of every emoji, the server's custom ones and Haven's own included. A role named after a platform starts with its icon.
> - Add members to a channel that already exists: right-click it and pick people one by one, a whole role at a time, or All users. People already in it are shown, and banned people are left out. It works for the admin and anyone who can invite people, and on a private channel for whoever may invite to it (its creator or a moderator there).
> …

### [v4.29.0-beta.5](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.5) — Haven 4.29.0-beta.5 _(pre-release)_
<sub>2026-11-13 · 9d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.28.0 until the next stable.
> Changes since 4.29.0-beta.4:
> **Added**
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. Every message moves over in time order, threads and all; a Discord message that is in both is kept once, and messages that look re-posted by hand are listed and only removed when ticked. Thanks Dawnforger (#5890).
> - Bots can edit their own messages through the webhook API (`PATCH /api/webhooks/<token>/messages/<id>`). A bot only ever edits its own messages, and protected messages stay as they are.
> - A timeout now shows how long it lasts in a bar above the message box, and a forum post written during a timeout is kept instead of lost. Thanks Amnibro (#5887).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [Put a name typed in full first in the @mention list (#5932)](https://github.com/ancsemi/Haven/commit/ad9ae09a9820ea228cd0ca4a8a8d1cc735405f82) | Amnibro |
| 2026-11-22 | [Show how many people picked each role on its role menu button](https://github.com/ancsemi/Haven/commit/1f10a78a072eb5a6c49369864635b48a0eb99f29) | ancsemi |
| 2026-11-22 | [Add the local network block to the coturn setup in the guide](https://github.com/ancsemi/Haven/commit/6017195bad24ecf76e321d6454d11c41628eb6e0) | ancsemi |
| 2026-11-22 | [Put test webhook makers in their webhook's channel](https://github.com/ancsemi/Haven/commit/c33ea4381605a7c851d18c808814762cc7728c62) | ancsemi |
| 2026-11-22 | [Keep the example TURN relay from reaching the local network](https://github.com/ancsemi/Haven/commit/6505b10c6f840474301a301825f3d453d93ebd76) | ancsemi |
| 2026-11-22 | [Read long messages in pieces in the AI link sweep](https://github.com/ancsemi/Haven/commit/6e343a0fa6d5f1b18c8c145e74aee218279d5d9b) | ancsemi |
| 2026-11-22 | [Auto-cleanup removes only real attachments nothing else uses](https://github.com/ancsemi/Haven/commit/5f28bba1d0b037c10e124ff7999163c41e0916c2) | ancsemi |
| 2026-11-22 | [Limit wrong passwords per account on admin recovery](https://github.com/ancsemi/Haven/commit/bec809f16d46acbe519932656c4920f139727ce8) | ancsemi |
| 2026-11-22 | [Stop a webhook token when its maker can no longer open the channel](https://github.com/ancsemi/Haven/commit/567e918560b444494aa97a4cc5d0ea546e26480a) | ancsemi |
| 2026-11-22 | [Let only the installer's own page drive the installer](https://github.com/ancsemi/Haven/commit/3ba93ba37f5814b84f92d10495234b0b91887a06) | ancsemi |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
