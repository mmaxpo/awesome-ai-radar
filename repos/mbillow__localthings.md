# mbillow/localthings

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/mbillow/localthings)

> Control your Samsung appliances from Home Assistant over your home network, with no cloud account.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | Local Samsung SmartThings control for Home Assistant |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 1.4k |
| 🍴 **Forks** | 154 |
| 🐞 **Open issues + PRs** | [105](https://github.com/mbillow/localthings/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `custom-component` `hacs` `hacs-integration` `home-assistant` `home-automation` `samsung` `smartthings` `coap-protocol` `coap-server` `dtls` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-06-30 |
| 📦 **Latest release** | [v0.40.0](https://github.com/mbillow/localthings/releases/tag/v0.40.0) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 5.9 MB |

## 📦 Recent releases

### [v0.40.0](https://github.com/mbillow/localthings/releases/tag/v0.40.0)
<sub>2026-11-26 · today</sub>

> **🚀 Highlights**
> - **Powered-off appliances stay off after a restart.** A washer that drops off Wi-Fi once it turns itself off now shows off, not unavailable. Thanks to @vshijiav! (#845)
> - **TV Wake-on-LAN with a single network adapter.** The magic packet now also goes to the subnet broadcast. Confirmed on a The Frame QN75LS03B. Thanks to @eduardobittencourt! (#872)
> - **Devices on different subnets with the same last IP octet** (`10.0.0.99`, `10.0.1.99`) no longer break each other's connections. (#925, fixes #918)
> - **Cooking permissions.** `start_cooking` checks that a non-admin user may control that oven cavity. Thanks to @leejaew! (#778)
> **✨ Added**
> …

### [v0.39.0](https://github.com/mbillow/localthings/releases/tag/v0.39.0)
<sub>2026-11-15 · 10d ago</sub>

> **🚀 Highlights**
> - **Samsung TVs.** Media player (power, volume, input, sound mode, channel and now-showing), picture mode, Wake-on-LAN, remote, notifications, apps and casting. Not yet run on hardware as merged. Thanks to @benjaml4 and @vmonkey! (#755, #856, part of #388)
> - **Bespoke Jet Bot Combo.** State, battery, cleaning method, water level, auto empty, station status and more. Writes not yet confirmed on hardware. (#861, fixes #838)
> - **Samsung FlexDry over 8888.** Both dryers get cycle, Start, Pause and Stop. The lower one also gets dry level, dry time and temperature. Thanks to @NadinMerali! (#866, from #673, fixes #649)
> - **Range hoods.** Smart ventilate, Do Not Disturb and air quality sensors. Thanks to @sabaatworld! (#828, from #794)
> - **No more reload loops.** An appliance that answers with only part of its data no longer reloads every 30 s, and new entities appear without a reload. (#850, fixes #807)
> …

### [v0.38.0](https://github.com/mbillow/localthings/releases/tag/v0.38.0)
<sub>2026-11-11 · 15d ago</sub>

> **⭐️🌟⭐️ One Thousand Stars ⭐️🌟⭐️**
> **LocalThings now has over 1,000 stars on GitHub!**
> Thank you to everyone who has contributed code, ideas, translations, device diagnostics, helped troubleshoot, verified changes, and reported bugs!
> **🚀 Highlights**
> - **Accurate finish time.** `finish_time` is now timed from when each remaining-time reading arrives. It shows seconds on boards that report them, and rounds to the nearest minute on the others. The deadband scales with the time left. Thanks to @WegnerDan! (#812, from #772, fixes #771)
> - **EHS heat pump data.** Cycle-log sensors (flow and return temperature, flow rate, pump speed, compressor frequency, outdoor temperature) and the installer's field settings (water-law curve, DHW limits, priorities, backup heater, zone control), plus each zone's water-law offset. Settings and diagnostics are disabled by default. Thanks to @pookey! (#678, #813, from #795, part of #697)
> …

### [v0.37.0](https://github.com/mbillow/localthings/releases/tag/v0.37.0)
<sub>2026-11-08 · 18d ago</sub>

> **🚀 Highlights**
> - **Soundbar media player.** Power, volume, mute, source, sound mode, playback, seek, shuffle and track info. Confirmed on the HW-Q950T. Thanks to @vmonkey and @benjaml4! (#775, part of #388)
> - **First robot vacuum.** The POWERbot R7040 gets state, start, pause, return home, spot clean, fan speed, battery and more. Writes not yet confirmed on hardware. (#735, for #659)
> - **Two new languages.** Russian and Serbian (Cyrillic and Latin). Thanks to @maxios777 and @cpmarexel2f! (#773)
> - **More appliances over 8888.** The RF28K9380SR fridge, the DV45K6500EW dryer and WF45K6500AW washer, and the AX80M7580WFD air purifier now set up. Thanks to @jsmith432! (#758, #774, #746, fixes #608, fixes #761, fixes #762)
> **✨ Added**
> …

### [v0.36.0](https://github.com/mbillow/localthings/releases/tag/v0.36.0)
<sub>2026-11-02 · 24d ago</sub>

> **🚀 Highlights**
> - **Soundbars.** Boards without `/device/0` now set up, starting with the HW-S61B (sensors, selects, switches, numbers, buttons). Media player and TV come later. Thanks to @vmonkey! (#606, part of #388)
> - **Faster startup.** Known appliances load from their snapshot and poll in the background, so one that's switched off no longer delays startup or logs an error. Thanks to @jjprz! (#711)
> - **Home Assistant 2026.11.** No more temperature deprecation warnings, and older versions still work. Thanks to @hmmbob! (#720, fixes #705)
> - **DONGLE_0281 fridge over 8888.** Temperature, door, setpoint, Rapid fridge and Vacation mode. Controls not yet confirmed on hardware. (#724, for #698)
> **✨ Added**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Bump version to 0.40.0](https://github.com/mbillow/localthings/commit/d2d8339ed67e0d42e1e7f94a63dbdc5cc34ab1c5) | mbillow |
| 2026-11-26 | [Quick fixes for #902, #906, #911 and #918 (#925)](https://github.com/mbillow/localthings/commit/e28e5366234ec5a5cacae4fdd165cfe43c20387e) | mbillow |
| 2026-11-26 | [Restructure credential acquisition as testing notes, with a risk warn…](https://github.com/mbillow/localthings/commit/2787bf289bae529395eb62be1484f0c12b3beca6) | mbillow |
| 2026-11-26 | [Name an NV7000BS's lower cavity from its Lower modes (#915)](https://github.com/mbillow/localthings/commit/4bb0af61c5f7f16181c78c1b6857eb7161cd41ae) | space192 |
| 2026-11-26 | [Lock Table_02 dials the app greys out; Spanish name for course 23 (#910)](https://github.com/mbillow/localthings/commit/9a0e5b745a3d26eccfe2f0ba8857c7b61731a3cd) | jasimancas |
| 2026-11-26 | [Document the no-root Morphe patch (smortthings) credential route (#899)](https://github.com/mbillow/localthings/commit/464fe71371f8946046ad09e22a92b9e6d83ef4dd) | neoKushan |
| 2026-11-26 | [Read remaining time as 0 once laundry is idle (#894)](https://github.com/mbillow/localthings/commit/49c3d44cd3cdda97b0f6542eed9ee73f44a942b8) | kkevindev |
| 2026-11-26 | [Carry a powered-off appliance through a restart as off (#845)](https://github.com/mbillow/localthings/commit/b76c8c21b7c635ff2b5f043a091c1ce909f26c21) | vshijiav |
| 2026-11-21 | [UN55DU7200 coverage, and redact a TV's location and addresses (#895) …](https://github.com/mbillow/localthings/commit/f86a819c4371be1db3d21e1e06c44b4620dbce33) | mbillow |
| 2026-11-21 | [Fixes for issues #867–#891 (#893)](https://github.com/mbillow/localthings/commit/6f3433131e6377336d5c261ed0f62a8a0ac11080) | mbillow |

[See all commits ↗](https://github.com/mbillow/localthings/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mbillow/localthings.git
```
