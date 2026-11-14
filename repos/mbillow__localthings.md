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
| ⭐ **Stars** | 1.3k |
| 🍴 **Forks** | 134 |
| 🐞 **Open issues + PRs** | [98](https://github.com/mbillow/localthings/issues) |
| 💻 **Languages** | Python 100% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `custom-component` `hacs` `hacs-integration` `home-assistant` `home-automation` `samsung` `smartthings` `coap-protocol` `coap-server` `dtls` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-06-30 |
| 📦 **Latest release** | [v0.38.0](https://github.com/mbillow/localthings/releases/tag/v0.38.0) — 2026-11-11 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 5.7 MB |

## 📦 Recent releases

### [v0.38.0](https://github.com/mbillow/localthings/releases/tag/v0.38.0)
<sub>2026-11-11 · 3d ago</sub>

> **⭐️🌟⭐️ One Thousand Stars ⭐️🌟⭐️**
> **LocalThings now has over 1,000 stars on GitHub!**
> Thank you to everyone who has contributed code, ideas, translations, device diagnostics, helped troubleshoot, verified changes, and reported bugs!
> **🚀 Highlights**
> - **Accurate finish time.** `finish_time` is now timed from when each remaining-time reading arrives. It shows seconds on boards that report them, and rounds to the nearest minute on the others. The deadband scales with the time left. Thanks to @WegnerDan! (#812, from #772, fixes #771)
> - **EHS heat pump data.** Cycle-log sensors (flow and return temperature, flow rate, pump speed, compressor frequency, outdoor temperature) and the installer's field settings (water-law curve, DHW limits, priorities, backup heater, zone control), plus each zone's water-law offset. Settings and diagnostics are disabled by default. Thanks to @pookey! (#678, #813, from #795, part of #697)
> …

### [v0.37.0](https://github.com/mbillow/localthings/releases/tag/v0.37.0)
<sub>2026-11-08 · 6d ago</sub>

> **🚀 Highlights**
> - **Soundbar media player.** Power, volume, mute, source, sound mode, playback, seek, shuffle and track info. Confirmed on the HW-Q950T. Thanks to @vmonkey and @benjaml4! (#775, part of #388)
> - **First robot vacuum.** The POWERbot R7040 gets state, start, pause, return home, spot clean, fan speed, battery and more. Writes not yet confirmed on hardware. (#735, for #659)
> - **Two new languages.** Russian and Serbian (Cyrillic and Latin). Thanks to @maxios777 and @cpmarexel2f! (#773)
> - **More appliances over 8888.** The RF28K9380SR fridge, the DV45K6500EW dryer and WF45K6500AW washer, and the AX80M7580WFD air purifier now set up. Thanks to @jsmith432! (#758, #774, #746, fixes #608, fixes #761, fixes #762)
> **✨ Added**
> …

### [v0.36.0](https://github.com/mbillow/localthings/releases/tag/v0.36.0)
<sub>2026-11-02 · 12d ago</sub>

> **🚀 Highlights**
> - **Soundbars.** Boards without `/device/0` now set up, starting with the HW-S61B (sensors, selects, switches, numbers, buttons). Media player and TV come later. Thanks to @vmonkey! (#606, part of #388)
> - **Faster startup.** Known appliances load from their snapshot and poll in the background, so one that's switched off no longer delays startup or logs an error. Thanks to @jjprz! (#711)
> - **Home Assistant 2026.11.** No more temperature deprecation warnings, and older versions still work. Thanks to @hmmbob! (#720, fixes #705)
> - **DONGLE_0281 fridge over 8888.** Temperature, door, setpoint, Rapid fridge and Vacation mode. Controls not yet confirmed on hardware. (#724, for #698)
> **✨ Added**
> …

### [v0.35.0](https://github.com/mbillow/localthings/releases/tag/v0.35.0)
<sub>2026-10-28 · 17d ago</sub>

> **🚀 Highlights**
> - **Two new languages.** French and Brazilian Portuguese join the existing eight. The four actions (Start cooking and the three resource actions) can now be translated, and every language has them. Thanks to @3615nulsi and @eduardobittencourt! (#617, #694, from #686)
> - **More appliances over TCP 8888.** The DV80M8214AW dryer, the NZ36K7570R cooktop, the NQ70M6650DS microwave/oven combo and the NW9300MD's oven cavities now set up. LocalThings now recognizes an 8888 appliance by the type it reports for itself, so a model nobody has mapped yet still reads in full. Thanks to @roweboat123, @antiremy and @korbijn! (#619, #675, #687, #690, #693, closes #636, closes #646)
> - **Paired range hood.** The NZ30K7570RS's Bluetooth hood gets its fan, light and shutoff timer, all confirmed on hardware. Thanks to @antiremy! (#677, for #676)
> - **Switch off subdevices.** Configure → Subdevices lets you untick a slot that isn't real hardware, like a blank cavity on some ovens and ranges. (#685)
> **✨ Added**
> …

### [v0.34.0](https://github.com/mbillow/localthings/releases/tag/v0.34.0)
<sub>2026-10-11 · 1mo ago</sub>

> **🚀 Highlights**
> - **New `observe_resource` action.** Subscribe to a resource for up to two minutes and see everything it pushes, next to a plain read. It lists any field that only arrived in a notification. This is for finding data a device sends only when something is subscribed. (#612, for #607)
> - **Oven lamp, sound and energy saving work with Remote Control off**, as in the SmartThings app. Everything that heats or starts a cook still needs Remote Control. Thanks to @BrawnyBravo! (#610, from #183 and #500)
> **✨ Added**
> - Fridges: start and end times for "Don't make ice at night". (#614, closes #599)
> **🐛 Fixed**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [Attach an integration zip to each release for HACS download counts (#…](https://github.com/mbillow/localthings/commit/cda240997d9996f9610ca0e542a97d1c52295bc4) | mbillow |
| 2026-11-13 | [Add a manual workflow to backfill release zips (#848)](https://github.com/mbillow/localthings/commit/fac361000a6b4ee5b556127b635051beda81a90b) | mbillow |
| 2026-11-12 | [docs: record AF18DX936WFN owner PSK recovery (#791)](https://github.com/mbillow/localthings/commit/663e4b39732bffb29cea4ed13d71b60a4d52d08d) | blupine |
| 2026-11-12 | [Quick fixes from issue triage: dishwasher buzzer (#821), Family Hub s…](https://github.com/mbillow/localthings/commit/2043f2a555fe43b4039527851828c57b9e0eeea7) | mbillow |
| 2026-11-12 | [Keep a Collection board's missed hrefs through first discovery (#833)…](https://github.com/mbillow/localthings/commit/c42bf975309d2b8385ef9939c1c62d4999e537ac) | mbillow |
| 2026-11-12 | [Skip Family Hub alarm placeholders with state 'none' (#826) (#831)](https://github.com/mbillow/localthings/commit/195fcfc7aa94a1d1273540ace8fa607c6ac01f5b) | mbillow |
| 2026-11-12 | [Samsung TV: picture-mode support and full QN90A fixture (#755)](https://github.com/mbillow/localthings/commit/723fcaa671a332bb6e95f65901e62c835fe99568) | benjaml4 |
| 2026-11-11 | [Let the microwave lamp and vent fan write with Remote Control off (#818)](https://github.com/mbillow/localthings/commit/2f39151e2cb71463e01393e33d5859c7470ad4b8) | Camwise1 |
| 2026-11-11 | [Add laundry drum-light controls and On/Off buzzer switches (#793) (#830)](https://github.com/mbillow/localthings/commit/1ec499896797b1b12405cd1db056630b127fa9fb) | mbillow |
| 2026-11-11 | [Register the alarm sensor on metadata-only clear responses (#792) (#829)](https://github.com/mbillow/localthings/commit/e3dfacc86527b4b932378f4b7979708fd492feb8) | mbillow |

[See all commits ↗](https://github.com/mbillow/localthings/commits)

## ⬇️ Get it

```bash
git clone https://github.com/mbillow/localthings.git
```
