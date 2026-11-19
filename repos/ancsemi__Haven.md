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
| 🍴 **Forks** | 120 |
| 🐞 **Open issues + PRs** | [16](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 80% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.6 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.30.0-beta.2](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.2) — Haven 4.30.0-beta.2 _(pre-release)_
<sub>2026-11-16 · 2d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.1:
> **Added**
> - Manage members replaces Add members in a channel's right-click menu. Everyone is listed with the people in the channel ticked: tick someone to add them, untick to remove them, by person, by role, or with All users, which adds everyone when ticked and removes everyone when unticked. Nothing changes until you press the button, and removing asks first. Whoever may add people to a channel may take them out again, and so may anyone with Kick there; only the admin removes an admin or a guest, and others only remove people ranked below them (a private channel's creator may remove anyone else in it). A role hidden on profile cards no longer shows in this list.
> - Emote names keep their capitals (asked for by gitty323, #5895): upload `HOLY` and `holy` as two different emotes, as Twitch and 7TV do. `:holy:` still finds `HOLY` when there is no exact match, so older messages keep working. A new switch, Settings > Chat & media > Turn emote names into emotes when I send, is off by default. When it is on, a word you type that is exactly a custom emote's name, capitals included, is sent as that emote, with no colons or picker. Code, links, mentions and slash commands are left alone. An admin can make the switch part of Defaults for New Members, so it starts on for everyone on their server (thanks Amnibro).
> - Sort your DMs: the new sort button in the Direct Messages header picks Latest message, Alphabetical or Manual order. The pick and the order you arranged by hand follow your account to every device, and pinned DMs stay on top whatever you choose (thanks Amnibro).
> …

### [v4.30.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.1) — Haven 4.30.0-beta.1 _(pre-release)_
<sub>2026-11-15 · 4d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> It has everything in 4.29.0, plus these, which are not in a stable yet:
> **Added**
> - Mass-select in forums: a Select button on the forum toolbar and a Select entry in a topic's right-click menu pick topics for moving or deleting several at once, with Select all. Phone-width screens had no way into selection mode in a forum. Moving offers forums only and takes the topics' replies along. Thanks Amnibro (#5892).
> - A bell in the reply bar chooses whether your reply sends a push notification to the person you reply to (on by default, remembered on this device). With it on, a reply reaches them like an @mention would, including through a server muted with "except @mentions", and replies inside a thread now notify their author too. Thanks Bo0sted (#5891).
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. The channel merged into keeps its name, settings, permissions and members; every message of the other moves into it in time order, threads and all, and the other is deleted. A Discord message that is in both (imported in one, relayed by Ferry in the other) is kept once, with its replies, reactions and pin. Messages that look re-posted by hand from Discord (the same text, posted later in Haven) are listed with both copies, and only the ticked ones go, leaving the Discord copy with its real author and time. Ferry links, webhooks, scheduled messages and role menus come along, a later history import lands in the merged channel, and people who were caught up stay caught up. Protected messages always stay.
> …

### [v4.29.0](https://github.com/ancsemi/Haven/releases/tag/v4.29.0) — Haven 4.29.0
<sub>2026-11-15 · 4d ago</sub>

> **Added**
> - Call controls in fullscreen (thanks Roolk, #5849): mute, deafen, camera, screen share, call settings and leave stay on screen over a fullscreen camera or screen share, and a picker switches which stream is shown without leaving fullscreen.
> - Video players in chat have Theater (as wide as the chat) and Fullscreen buttons: YouTube cards, uploaded videos and videos in link previews.
> - Platform emoji built into Haven: Windows, Mac, iPhone, Android and Linux, under Platforms in the emoji picker. They work in messages, reactions and role menus.
> - Role menus: each role's emoji is picked from a searchable list of every emoji, the server's custom ones and Haven's own included. A role named after a platform starts with its icon.
> - Add members to a channel that already exists: right-click it and pick people one by one, a whole role at a time, or All users. People already in it are shown, and banned people are left out. It works for the admin and anyone who can invite people, and on a private channel for whoever may invite to it (its creator or a moderator there).
> …

### [v4.29.0-beta.5](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.5) — Haven 4.29.0-beta.5 _(pre-release)_
<sub>2026-11-13 · 5d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.28.0 until the next stable.
> Changes since 4.29.0-beta.4:
> **Added**
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. Every message moves over in time order, threads and all; a Discord message that is in both is kept once, and messages that look re-posted by hand are listed and only removed when ticked. Thanks Dawnforger (#5890).
> - Bots can edit their own messages through the webhook API (`PATCH /api/webhooks/<token>/messages/<id>`). A bot only ever edits its own messages, and protected messages stay as they are.
> - A timeout now shows how long it lasts in a bar above the message box, and a forum post written during a timeout is kept instead of lost. Thanks Amnibro (#5887).
> …

### [v4.29.0-beta.4](https://github.com/ancsemi/Haven/releases/tag/v4.29.0-beta.4) — Haven 4.29.0-beta.4 _(pre-release)_
<sub>2026-11-11 · 7d ago</sub>

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
| 2026-11-19 | [Guide: note what a backup's database still holds, fix the Audit Log path](https://github.com/ancsemi/Haven/commit/46104c7185f6b1f5a1b1f90455d38c873b6208d8) | ancsemi |
| 2026-11-19 | [Make Close topic a labeled button on forum cards and the topic header](https://github.com/ancsemi/Haven/commit/ecb7842366f3bc10dd846e299907ffa2e0da8cb8) | ancsemi |
| 2026-11-19 | [Keep the message box in step when text or media is switched on the op…](https://github.com/ancsemi/Haven/commit/95314f9cb2c34a804b9cb4c55ee9b4ab3c96558f) | rajuriprathik-a11y |
| 2026-11-19 | [Start the noise gate closed so steady noise below its level is not se…](https://github.com/ancsemi/Haven/commit/26dafb77d4af49cbecf4e4a23eb813218d5ad98c) | Amnibro |
| 2026-11-19 | [Paste and Ctrl shortcuts follow the key you press on any keyboard lay…](https://github.com/ancsemi/Haven/commit/c4ddeb399984dec79b41d6a2d3e67b332a069d57) | Amnibro |
| 2026-11-19 | [Add an Exporting your data section to the guide (#5910) (#5914)](https://github.com/ancsemi/Haven/commit/4db93fd867c22d5416c1e873a1893943ce6c472c) | Amnibro |
| 2026-11-19 | [Keep Discord pictures and files in Haven through Ferry, opt-in (#5906)](https://github.com/ancsemi/Haven/commit/b0461616b6a9bf0e7121792ed15c3bb07113db95) | Amnibro |
| 2026-11-19 | [Let a long search filter list scroll](https://github.com/ancsemi/Haven/commit/030cbd398bb8daaaea29d14437e3082053ef1c57) | ancsemi |
| 2026-11-19 | [Update the donor list](https://github.com/ancsemi/Haven/commit/92039c73d0e4bd8c7512535ed1774ae499b42cd8) | ancsemi |
| 2026-11-19 | [Keep a muted channel in its place in the channel list](https://github.com/ancsemi/Haven/commit/cfa327bb9f9b413815b2eb1603d33d02c8097e11) | ancsemi |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
