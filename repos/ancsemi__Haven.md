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
| 🍴 **Forks** | 125 |
| 🐞 **Open issues + PRs** | [14](https://github.com/ancsemi/Haven/issues) |
| 💻 **Languages** | JavaScript 81% · HTML 10% · CSS 8% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `chat` `discord` `discord-alternative` `messaging` `privacy` `self-hosted` `selfhosted` `voice-chat` `docker` `homelab` `e2ee` `electron` `end-to-end-encryption` `group-chat` `screen-sharing` `self-hosting` `teamspeak` `video-chat` `webrtc` `discord-clone` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-02-11 |
| 📦 **Latest release** | [v4.30.0](https://github.com/ancsemi/Haven/releases/tag/v4.30.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 23.0 MB |
| 🌐 **Website** | https://haven-app.com |

## 📦 Recent releases

### [v4.31.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.31.0-beta.1) — Haven 4.31.0-beta.1 _(pre-release)_
<sub>2026-11-23 · 3d ago</sub>

> This is an early access build: new work that has not been through a stable release yet. Servers get it only with Settings > Admin > Early access updates switched on (Docker: the `:beta` image). Everything in stable 4.30.0 is included.
> **Added**
> - Bot accounts: Settings > Bots & data now has Webhooks and Bots as separate pages. A bot is a member account a program signs in to with a token, so it can do anything a member can, wherever its roles let it; webhooks are unchanged. Making one needs the new Bot Manager permission. A bot gets the roles and channels a new member gets, and its page has its token (shown once, with Make new token), name, picture, Enable/Disable, a list of Bot Creators who may look after it without any other permission (only the admin and Bot Managers change that list), its channels (added and removed by the Manage members rules) and, for people who can manage roles, Manage this bot's roles. A bot that has never posted can be deleted by a Bot Manager; after that only the admin can, and its messages go with it. Bot accounts carry a BOT tag, can post embeds, buttons and dropdowns, and get clicks straight over their own connection. See "Bot Accounts" in GUIDE.md.
> - Bots can post embeds, buttons and dropdowns, in the same JSON shapes Discord uses, so a Discord bot's payload works as it is. Embeds show a colored card with a title, text, fields, pictures and a footer. Buttons come in the primary, secondary, green, red and link styles. Dropdowns allow one pick or several. A click or a pick is checked and sent to the bot's callback URL, signed, and the bot answers with a private reply, a new message, or an edit that changes the message (a bot's edit can now replace its embeds and buttons). See "Embeds, Buttons and Dropdowns" in GUIDE.md.
> - Two new desktop layouts in Settings > Layout (thanks Amnibro, #5928). Focus puts the conversation that needs you in the middle, with menus in a dock along the bottom, and moves you to the next thing to answer when you send. Focus Classic shows one list at a time (Server, DMs, Activity, You) beside the chat. Both are off unless you pick them. In a call, the channel list also shows a red dot next to anyone sharing their screen; click it to watch.
> - Drag a soundboard sound onto another to put it where you want it (asked for by Raidenphantom). The order is yours alone and follows you to every device; the Soundboard panel, the pop-up and the pop-out all use it, and sounds you have not moved keep their place after the ones you have.
> …

### [v4.30.0](https://github.com/ancsemi/Haven/releases/tag/v4.30.0) — Haven 4.30.0
<sub>2026-11-23 · 3d ago</sub>

> **Before you update**
> - Only if you opted into the PostgreSQL preview: a preview database made with 4.29 is refused by 4.30 at startup. Start the preview on a fresh database. Servers on the normal built-in database are not affected.
> **Added**
> - More profile customization (thanks Bo0sted, #5900): pick a banner color in Edit Profile or let it follow your avatar, upload and crop a banner picture (with its own size limit in Uploads & Limits), and give your profile card a two-color theme it fades between.
> - Call settings everywhere (thanks Roolk, #5903): Settings has a new Voice & video page with every call setting, usable without joining a call, plus Test microphone (with Hear myself) and Test camera. The fullscreen call popup shows the same full set of settings instead of three dropdowns.
> - The quick reaction row leads with your favorites, then the reactions you use most, then the usual defaults (thanks Amnibro, #5902). A row you customized still wins, and its editor has a Reset to automatic button.
> …

### [v4.30.0-beta.3](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.3) — Haven 4.30.0-beta.3 _(pre-release)_
<sub>2026-11-20 · 7d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.2:
> **Added**
> - More profile customization (thanks Bo0sted, #5900): pick a banner color in Edit Profile or let it follow your avatar, upload and crop a banner picture (with its own size limit in Uploads & Limits), and give your profile card a two-color theme it fades between.
> - Call settings everywhere (thanks Roolk, #5903): Settings has a new Voice & video page with every call setting, usable without joining a call, plus Test microphone (with Hear myself) and Test camera. The fullscreen call popup shows the same full set of settings instead of three dropdowns.
> - The quick reaction row leads with your favorites, then the reactions you use most, then the usual defaults (thanks Amnibro, #5902). A row you customized still wins, and its editor has a Reset to automatic button.
> …

### [v4.30.0-beta.2](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.2) — Haven 4.30.0-beta.2 _(pre-release)_
<sub>2026-11-16 · 11d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> New since 4.30.0-beta.1:
> **Added**
> - Manage members replaces Add members in a channel's right-click menu. Everyone is listed with the people in the channel ticked: tick someone to add them, untick to remove them, by person, by role, or with All users, which adds everyone when ticked and removes everyone when unticked. Nothing changes until you press the button, and removing asks first. Whoever may add people to a channel may take them out again, and so may anyone with Kick there; only the admin removes an admin or a guest, and others only remove people ranked below them (a private channel's creator may remove anyone else in it). A role hidden on profile cards no longer shows in this list.
> - Emote names keep their capitals (asked for by gitty323, #5895): upload `HOLY` and `holy` as two different emotes, as Twitch and 7TV do. `:holy:` still finds `HOLY` when there is no exact match, so older messages keep working. A new switch, Settings > Chat & media > Turn emote names into emotes when I send, is off by default. When it is on, a word you type that is exactly a custom emote's name, capitals included, is sent as that emote, with no colons or picker. Code, links, mentions and slash commands are left alone. An admin can make the switch part of Defaults for New Members, so it starts on for everyone on their server (thanks Amnibro).
> - Sort your DMs: the new sort button in the Direct Messages header picks Latest message, Alphabetical or Manual order. The pick and the order you arranged by hand follow your account to every device, and pinned DMs stay on top whatever you choose (thanks Amnibro).
> …

### [v4.30.0-beta.1](https://github.com/ancsemi/Haven/releases/tag/v4.30.0-beta.1) — Haven 4.30.0-beta.1 _(pre-release)_
<sub>2026-11-15 · 12d ago</sub>

> Early access release. Servers on the early access channel (Settings > Admin > "Early access updates") and the Docker `:beta` image get it; everyone else stays on 4.29.0 until the next stable.
> It has everything in 4.29.0, plus these, which are not in a stable yet:
> **Added**
> - Mass-select in forums: a Select button on the forum toolbar and a Select entry in a topic's right-click menu pick topics for moving or deleting several at once, with Select all. Phone-width screens had no way into selection mode in a forum. Moving offers forums only and takes the topics' replies along. Thanks Amnibro (#5892).
> - A bell in the reply bar chooses whether your reply sends a push notification to the person you reply to (on by default, remembered on this device). With it on, a reply reaches them like an @mention would, including through a server muted with "except @mentions", and replies inside a thread now notify their author too. Thanks Bo0sted (#5891).
> - Merge a channel into another (admin, a channel's menu > Merge into…), for the duplicates a Ferry history import leaves next to channels copied by hand. The channel merged into keeps its name, settings, permissions and members; every message of the other moves into it in time order, threads and all, and the other is deleted. A Discord message that is in both (imported in one, relayed by Ferry in the other) is kept once, with its replies, reactions and pin. Messages that look re-posted by hand from Discord (the same text, posted later in Haven) are listed with both copies, and only the ticked ones go, leaving the Discord copy with its real author and time. Ferry links, webhooks, scheduled messages and role menus come along, a later history import lands in the merged channel, and people who were caught up stay caught up. Protected messages always stay.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Name the bot on its form and keep invisible characters out of form te…](https://github.com/ancsemi/Haven/commit/f8c1b13acfdbcdf870520f5ecd72ed792e23d27f) | ancsemi |
| 2026-11-25 | [Let members arrange the Focus Classic rail and add shortcuts such as …](https://github.com/ancsemi/Haven/commit/abd1c65ae0df782cc78a6843175cfc11abe7b6c6) | Amnibro |
| 2026-11-25 | [[feat] Bot text input forms (#5935)](https://github.com/ancsemi/Haven/commit/1087c27e98b15fd39d701b89a1f609f207ad2418) | Bo0sted |
| 2026-11-25 | [Keep room for the current server's ring in the Focus Classic rail; ch…](https://github.com/ancsemi/Haven/commit/3a97fd122d99880a2ee7cad16c7b465539299f2b) | ancsemi |
| 2026-11-25 | [Postgres progress (#5934)](https://github.com/ancsemi/Haven/commit/cbf1305750589d0bd8fbcdc9d847f62be2448c14) | Slyke |
| 2026-11-25 | [Remove the Focus carousel and let an admin's default layout reach mem…](https://github.com/ancsemi/Haven/commit/60cb695ef6c9a74ed1407a5c34d658f849c709eb) | Amnibro |
| 2026-11-25 | [Hold calendar events to the posting rules and refuse merging a calend…](https://github.com/ancsemi/Haven/commit/66184480c9db31adde0fcd2310e60d25fb3d17fe) | ancsemi |
| 2026-11-25 | [Calendar channels: a month of events with RSVPs (#5953)](https://github.com/ancsemi/Haven/commit/5fb128939e1d745cf1dc4b4b4c6653b9dcbbf50e) | Amnibro |
| 2026-11-25 | [Escape the member's name in the devices button tooltip (#5942)](https://github.com/ancsemi/Haven/commit/9184b02703d44769ca33c3b153c375b779a9ad20) | ancsemi |
| 2026-11-25 | [Only the admin sets a channel's default notification level (#5938)](https://github.com/ancsemi/Haven/commit/439143f4e3ab0208fb0da21d77533e986c439743) | ancsemi |

[See all commits ↗](https://github.com/ancsemi/Haven/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ancsemi/Haven.git
```
