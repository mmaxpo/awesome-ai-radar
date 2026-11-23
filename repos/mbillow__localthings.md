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
| 🍴 **Forks** | 149 |
| 🐞 **Open issues + PRs** | [97](https://github.com/mbillow/localthings/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `custom-component` `hacs` `hacs-integration` `home-assistant` `home-automation` `samsung` `smartthings` `coap-protocol` `coap-server` `dtls` |
| 🕒 **Last activity** | 2026-11-21 (2d ago) |
| 📅 **Created** | 2026-06-30 |
| 📦 **Latest release** | [v0.39.0](https://github.com/mbillow/localthings/releases/tag/v0.39.0) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 6.7 MB |

## 📦 Recent releases

### [v0.39.0](https://github.com/mbillow/localthings/releases/tag/v0.39.0)
<sub>2026-11-15 · 7d ago</sub>

> **🚀 Highlights**
> - **Samsung TVs.** Media player (power, volume, input, sound mode, channel and now-showing), picture mode, Wake-on-LAN, remote, notifications, apps and casting. Not yet run on hardware as merged. Thanks to @benjaml4 and @vmonkey! (#755, #856, part of #388)
> - **Bespoke Jet Bot Combo.** State, battery, cleaning method, water level, auto empty, station status and more. Writes not yet confirmed on hardware. (#861, fixes #838)
> - **Samsung FlexDry over 8888.** Both dryers get cycle, Start, Pause and Stop. The lower one also gets dry level, dry time and temperature. Thanks to @NadinMerali! (#866, from #673, fixes #649)
> - **Range hoods.** Smart ventilate, Do Not Disturb and air quality sensors. Thanks to @sabaatworld! (#828, from #794)
> - **No more reload loops.** An appliance that answers with only part of its data no longer reloads every 30 s, and new entities appear without a reload. (#850, fixes #807)
> …

### [v0.38.0](https://github.com/mbillow/localthings/releases/tag/v0.38.0)
<sub>2026-11-11 · 12d ago</sub>

> **⭐️🌟⭐️ One Thousand Stars ⭐️🌟⭐️**
> **LocalThings now has over 1,000 stars on GitHub!**
> Thank you to everyone who has contributed code, ideas, translations, device diagnostics, helped troubleshoot, verified changes, and reported bugs!
> **🚀 Highlights**
> - **Accurate finish time.** `finish_time` is now timed from when each remaining-time reading arrives. It shows seconds on boards that report them, and rounds to the nearest minute on the others. The deadband scales with the time left. Thanks to @WegnerDan! (#812, from #772, fixes #771)
> - **EHS heat pump data.** Cycle-log sensors (flow and return temperature, flow rate, pump speed, compressor frequency, outdoor temperature) and the installer's field settings (water-law curve, DHW limits, priorities, backup heater, zone control), plus each zone's water-law offset. Settings and diagnostics are disabled by default. Thanks to @pookey! (#678, #813, from #795, part of #697)
> …

### [v0.37.0](https://github.com/mbillow/localthings/releases/tag/v0.37.0)
<sub>2026-11-08 · 15d ago</sub>

> **🚀 Highlights**
> - **Soundbar media player.** Power, volume, mute, source, sound mode, playback, seek, shuffle and track info. Confirmed on the HW-Q950T. Thanks to @vmonkey and @benjaml4! (#775, part of #388)
> - **First robot vacuum.** The POWERbot R7040 gets state, start, pause, return home, spot clean, fan speed, battery and more. Writes not yet confirmed on hardware. (#735, for #659)
> - **Two new languages.** Russian and Serbian (Cyrillic and Latin). Thanks to @maxios777 and @cpmarexel2f! (#773)
> - **More appliances over 8888.** The RF28K9380SR fridge, the DV45K6500EW dryer and WF45K6500AW washer, and the AX80M7580WFD air purifier now set up. Thanks to @jsmith432! (#758, #774, #746, fixes #608, fixes #761, fixes #762)
> **✨ Added**
> …

### [v0.36.0](https://github.com/mbillow/localthings/releases/tag/v0.36.0)
<sub>2026-11-02 · 21d ago</sub>

> **🚀 Highlights**
> - **Soundbars.** Boards without `/device/0` now set up, starting with the HW-S61B (sensors, selects, switches, numbers, buttons). Media player and TV come later. Thanks to @vmonkey! (#606, part of #388)
> - **Faster startup.** Known appliances load from their snapshot and poll in the background, so one that's switched off no longer delays startup or logs an error. Thanks to @jjprz! (#711)
> - **Home Assistant 2026.11.** No more temperature deprecation warnings, and older versions still work. Thanks to @hmmbob! (#720, fixes #705)
> - **DONGLE_0281 fridge over 8888.** Temperature, door, setpoint, Rapid fridge and Vacation mode. Controls not yet confirmed on hardware. (#724, for #698)
> **✨ Added**
> …

### [v0.35.0](https://github.com/mbillow/localthings/releases/tag/v0.35.0)
<sub>2026-10-28 · 25d ago</sub>

> **🚀 Highlights**
> - **Two new languages.** French and Brazilian Portuguese join the existing eight. The four actions (Start cooking and the three resource actions) can now be translated, and every language has them. Thanks to @3615nulsi and @eduardobittencourt! (#617, #694, from #686)
> - **More appliances over TCP 8888.** The DV80M8214AW dryer, the NZ36K7570R cooktop, the NQ70M6650DS microwave/oven combo and the NW9300MD's oven cavities now set up. LocalThings now recognizes an 8888 appliance by the type it reports for itself, so a model nobody has mapped yet still reads in full. Thanks to @roweboat123, @antiremy and @korbijn! (#619, #675, #687, #690, #693, closes #636, closes #646)
> - **Paired range hood.** The NZ30K7570RS's Bluetooth hood gets its fan, light and shutoff timer, all confirmed on hardware. Thanks to @antiremy! (#677, for #676)
> - **Switch off subdevices.** Configure → Subdevices lets you untick a slot that isn't real hardware, like a blank cavity on some ovens and ranges. (#685)
> **✨ Added**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [UN55DU7200 coverage, and redact a TV's location and addresses (#895) …](https://github.com/mbillow/localthings/commit/f86a819c4371be1db3d21e1e06c44b4620dbce33) | mbillow |
| 2026-11-21 | [Fixes for issues #867–#891 (#893)](https://github.com/mbillow/localthings/commit/6f3433131e6377336d5c261ed0f62a8a0ac11080) | mbillow |
| 2026-11-20 | [Enforce target control permission for cooking actions (#778)](https://github.com/mbillow/localthings/commit/5b0e8b64727871f2d0d5242cf971781488aa92f3) | leejaew |
| 2026-11-20 | [Fix TV Wake-on-LAN on default-only network adapters (#872)](https://github.com/mbillow/localthings/commit/a711b609966ee8457d4796b5440c087ab7bd87c3) | eduardobittencourt |
| 2026-11-20 | [Keep a known sibling whose seed answered when its probe times out (#885)](https://github.com/mbillow/localthings/commit/58c5dd83e6c177c2bcf5edf5594ea3f2d5df563b) | antiremy |
| 2026-11-20 | [Read a no-reading EHS cycle temperature byte as unknown (#880)](https://github.com/mbillow/localthings/commit/125b32056411aef8bb822b5f669e23b1291027d0) | pookey |
| 2026-11-19 | [Give entities of one capability distinct names in every language (#873)](https://github.com/mbillow/localthings/commit/4224f5fa73786a4ce77eb9386dced852c7df9a92) | wit3 |
| 2026-11-19 | [Say in the README that diagnostics keep the OCF device ID (#874) (#892)](https://github.com/mbillow/localthings/commit/5815224dce7fb4395716cc842c333e65e52d38e8) | wit3 |
| 2026-11-15 | [Bump version to 0.39.0](https://github.com/mbillow/localthings/commit/11a23140c5d2493ecb616fdffff8128faa0bc953) | mbillow |
| 2026-11-15 | [Decode the NY9100DW burner entities when no Fuel_ token is reported (…](https://github.com/mbillow/localthings/commit/6cfeb7bee52a5301c7573b797f66ade42b0178d4) | Varshavia |

[See all commits ↗](https://github.com/mbillow/localthings/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mbillow/localthings.git
```
