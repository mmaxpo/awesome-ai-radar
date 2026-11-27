# onehumanbeing/esp32-iphone-agent

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/onehumanbeing/esp32-iphone-agent)

> Manina AI: let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | AI controls a real iPhone via a $7 ESP32 |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 5.4k |
| 🍴 **Forks** | 756 |
| 🐞 **Open issues + PRs** | [17](https://github.com/onehumanbeing/esp32-iphone-agent/issues) |
| 💻 **Languages** | Swift 68% · C 16% · Go 6% · C++ 5% · Python 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `airplay` `computer-use` `esp32` `esp32-s3` `iphone` `llm` `usb-hid` `claude-code` `ios` `ios-automation` `mcp` `mcp-server` `mobile-agent` `phone-agent` `screen-mirroring` `xiao-esp32s3` `manina-ai` `seeed-xiao` `iphone-automation` |
| 🕒 **Last activity** | 2026-11-26 (yesterday) |
| 📅 **Created** | 2026-10-11 |
| 📦 **Latest release** | [v1.0.11.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.11.1) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 20.5 MB |
| 🌐 **Website** | https://manina.ai?ref=github |

## 📦 Recent releases

### [v1.0.11.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.11.1) — Handsy 1.0.11.1 (TestFlight)
<sub>2026-11-26 · yesterday</sub>

> **Built and tested with an automated harness: the changes below were found, fixed and checked on a real iPhone by the harness itself.**
> - Long press: the agent can press and hold (`tap X Y hold`), for a chat message's menu (Forward, Copy), an icon's quick actions or selecting a word.
> - Opening apps no longer hangs on iOS's "Open in …?" prompt, and an English iPhone searches a known app by its English name (Maps, rednote) instead of pinyin.
> - Faster Chinese typing: the pinyin for a text is worked out once, with no stall on the first character.
> - Faster pointer search: each screen is decoded once.
> - Harness (`harness/`): files to and from the app over pymobiledevice3 (about 1.5 s instead of 40 s), `tapcv.py` taps and restarts Screen Mirroring with no one at the phone, `collect.py` walks an app's screens and records screen, text and action, `timing.py` shows where a run's time went.

### [v1.0.11](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.11) — Manina AI 1.0.11 (TestFlight)
<sub>2026-11-25 · yesterday</sub>

> - App: Settings › Model › Sign in with ChatGPT: runs use your own ChatGPT Plus or Pro plan (the same usage limits Codex uses), with no API key.
> - App: the Settings note on Look ahead says it is on by default (it has been since 2026-11-25).
> - App: the "Let Me Use the Pointer" setup page lists the AssistiveTouch steps one by one, ticks each as it is done, says what it is waiting for (AssistiveTouch, the board's mouse, Screen Mirroring) and, after 20 s on one of them, the likely cause and fix. It looked frozen before.
> - App: a landscape app learns its own pointer landings (a separate table from portrait), so a steady miss there is corrected after a few taps.
> - App: a landscape app (a game) goes to the model at 540 px on its short side (about 1170x540), as many pixels as portrait; it went at 540x250 and small targets were unreadable.
> - App: faster on screens that never stand still: one such step caps every later wait at 0.8 s, a screen seen moving in the last 2 minutes waits at most 1 s, the longest wait for a still screen is 3 s (was 4), and the pointer check waits 0.2 s instead of 0.6 s there.
> …

### [v1.0.10.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.10.1) — Manina AI 1.0.10.1 (TestFlight)
<sub>2026-11-23 · 4d ago</sub>

> - Chinese input is much faster: pinyin goes in one go and is read back once; a right text is no longer deleted and typed again (a long text that shows only its end, the same message already in the chat, an OCR slip). Only English letters or the keyboard's other candidate (西安 for 西岸) are typed again.
> - Agent: a `type` that repeats part of the text just typed is not typed again; `tap 发送` without quotes is understood (no second model call).
> - Runs end faster: the keyboard check after a run is read on the phone (0.2 s instead of 8-30 s), the planner's done check is off, no wait for a late on-device tree on slower phones, no 2.5 s stall at the start.
> - Intents: a finished run keeps its plan; replayed steps carry this run's result; a done right after the app's own open is held once.
> - Nothing goes on the clipboard at a run's start.
> - Hermes Agent plugin (`integrations/hermes`, a portable Agent Plugins v1 package): the esp32agent MCP server (esp32agent 0.1.5) plus the manina skill. `hermes plugins install onehumanbeing/esp32-iphone-agent/integrations/hermes --enable`.

### [v1.0.10](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.10) — Manina AI 1.0.10 (TestFlight)
<sub>2026-11-22 · 5d ago</sub>

> - Agent: `collect WHAT max N` that stops on its count saves the result (README) and says where, as a list read to its end does.
> - Agent: when the progress count is reached and the result written but the run goes on with another gesture, the planner looks once.
> - Agent: a tap on a send button (发送 / Send / 发布 / Post / 回复 / Reply) is held once like Enter after a `type` that stopped part way, or when the same text was already sent; the same tap again goes through.
> - Runs: a run that a guard gave up on ("stuck:") ends as `stall`, not `model_fail`; run_end also says which link the mouse and keyboard used (`transport`: usb / ble) and the longest run of gestures that changed nothing (`unchanged_max`).

### [v1.0.9](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.9) — Manina AI 1.0.9 (TestFlight)
<sub>2026-11-21 · 5d ago</sub>

> - iOS 16.4 minimum: iPhone 8 and iPhone X can run the app. On iPhones before iOS 17 the agent leaves an app through the AssistiveTouch menu (its button found on the screen) instead of the Home bar.
> - Experimental M5Stack StopWatch board (Bluetooth): it shows the run (character, steps, time, the step's text), the yellow key pauses and resumes, two quick presses stop, help and confirms buzz until answered, a done task's answer shows on the screen, quick intents (the newest 5) start from the watch, hold yellow to talk. Updates from its own firmware channel; the app sends it the phone's time and what needs fixing (mirroring lost, iPhone locked).
> - Agent: `collect WHAT max N` stops once the goal's N items are read.
> - Agent: a screen back for the third time with no progress goes to the planner. Tab bar guard: a tab bar is a row of three or more short labels.
> - Start: an app opened by its link (Fiverr added) waits for the screen only when iOS asked "Open in …?" first; a replay skips opening the app the link already opened, and looks for a step's label for at most 2.5 s.
> - Learning: a tap's label is the text nearest it by its box (a search bar no longer learns the logo above it); the plan judge knows the app was opened before the plan.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [README: add ten language translations and a language switcher (#193)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/dd32c21d3cf59da6214d2c28135a00da93fd748a) | onehumanbeing |
| 2026-11-26 | [App 1.0.11.1 (harness): long press, faster opening and typing, harnes…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8451f3e6f038a548cfa49b0dddfa455e3565326b) | onehumanbeing |
| 2026-11-25 | [App 1.0.11 (#190)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9331b8704e29acc51aefe2694e77f141b71d26a6) | onehumanbeing |
| 2026-11-24 | [README: first screen says what it does, which board to buy, and one-c…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9b1d512ec319bf79ce572ebe65ee0d686f31a6bd) | onehumanbeing |
| 2026-11-24 | [README: link the setup guides for AI iPhone control, MCP and Claude C…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9ac751618ee644e947646a72b8e0fa6a340fb3fb) | onehumanbeing |
| 2026-11-23 | [Changelog: 1.0.10.1, significantly faster Chinese input (#185)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/90f450ea7c2741901a2b4102c8d209c930961912) | onehumanbeing |
| 2026-11-23 | [App 1.0.10.1: much faster Chinese input (#184)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8e51f56b3ec3e2577226c8bfdc7ca6f2eaae8e30) | onehumanbeing |
| 2026-11-23 | [Hermes Agent plugin: esp32agent MCP server and manina skill (#183)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/6af87ec7a5ad2f19e2d98d39222e19ca4fd1958b) | onehumanbeing |
| 2026-11-22 | [Merge pull request #182 from onehumanbeing/fix/1.0.10](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d1cca3301a5f061a50f42886898d43da67ee74d9) | onehumanbeing |
| 2026-11-22 | [App 1.0.10: collect max saves the result, a reached count goes to the…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8eb875b6a72b86208a23b9ed5980d00b9aa83cda) | onehumanbeing |

[See all commits ↗](https://github.com/onehumanbeing/esp32-iphone-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/onehumanbeing/esp32-iphone-agent.git
```
