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
| ⭐ **Stars** | 5.3k |
| 🍴 **Forks** | 748 |
| 🐞 **Open issues + PRs** | [15](https://github.com/onehumanbeing/esp32-iphone-agent/issues) |
| 💻 **Languages** | Swift 67% · C 17% · Go 6% · C++ 5% · Python 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `airplay` `computer-use` `esp32` `esp32-s3` `iphone` `llm` `usb-hid` `claude-code` `ios` `ios-automation` `mcp` `mcp-server` `mobile-agent` `phone-agent` `screen-mirroring` `xiao-esp32s3` `manina-ai` `seeed-xiao` `iphone-automation` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-10-11 |
| 📦 **Latest release** | [v1.0.10.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.10.1) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 20.0 MB |
| 🌐 **Website** | https://manina.ai?ref=github |

## 📦 Recent releases

### [v1.0.10.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.10.1) — Manina AI 1.0.10.1 (TestFlight)
<sub>2026-11-23 · 2d ago</sub>

> - Chinese input is much faster: pinyin goes in one go and is read back once; a right text is no longer deleted and typed again (a long text that shows only its end, the same message already in the chat, an OCR slip). Only English letters or the keyboard's other candidate (西安 for 西岸) are typed again.
> - Agent: a `type` that repeats part of the text just typed is not typed again; `tap 发送` without quotes is understood (no second model call).
> - Runs end faster: the keyboard check after a run is read on the phone (0.2 s instead of 8-30 s), the planner's done check is off, no wait for a late on-device tree on slower phones, no 2.5 s stall at the start.
> - Intents: a finished run keeps its plan; replayed steps carry this run's result; a done right after the app's own open is held once.
> - Nothing goes on the clipboard at a run's start.
> - Hermes Agent plugin (`integrations/hermes`, a portable Agent Plugins v1 package): the esp32agent MCP server (esp32agent 0.1.5) plus the manina skill. `hermes plugins install onehumanbeing/esp32-iphone-agent/integrations/hermes --enable`.

### [v1.0.10](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.10) — Manina AI 1.0.10 (TestFlight)
<sub>2026-11-22 · 3d ago</sub>

> - Agent: `collect WHAT max N` that stops on its count saves the result (README) and says where, as a list read to its end does.
> - Agent: when the progress count is reached and the result written but the run goes on with another gesture, the planner looks once.
> - Agent: a tap on a send button (发送 / Send / 发布 / Post / 回复 / Reply) is held once like Enter after a `type` that stopped part way, or when the same text was already sent; the same tap again goes through.
> - Runs: a run that a guard gave up on ("stuck:") ends as `stall`, not `model_fail`; run_end also says which link the mouse and keyboard used (`transport`: usb / ble) and the longest run of gestures that changed nothing (`unchanged_max`).

### [v1.0.9](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.9) — Manina AI 1.0.9 (TestFlight)
<sub>2026-11-21 · 3d ago</sub>

> - iOS 16.4 minimum: iPhone 8 and iPhone X can run the app. On iPhones before iOS 17 the agent leaves an app through the AssistiveTouch menu (its button found on the screen) instead of the Home bar.
> - Experimental M5Stack StopWatch board (Bluetooth): it shows the run (character, steps, time, the step's text), the yellow key pauses and resumes, two quick presses stop, help and confirms buzz until answered, a done task's answer shows on the screen, quick intents (the newest 5) start from the watch, hold yellow to talk. Updates from its own firmware channel; the app sends it the phone's time and what needs fixing (mirroring lost, iPhone locked).
> - Agent: `collect WHAT max N` stops once the goal's N items are read.
> - Agent: a screen back for the third time with no progress goes to the planner. Tab bar guard: a tab bar is a row of three or more short labels.
> - Start: an app opened by its link (Fiverr added) waits for the screen only when iOS asked "Open in …?" first; a replay skips opening the app the link already opened, and looks for a step's label for at most 2.5 s.
> - Learning: a tap's label is the text nearest it by its box (a search bar no longer learns the logo above it); the plan judge knows the app was opened before the plan.
> …

### [v1.0.7](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.7) — Manina AI 1.0.7 (TestFlight)
<sub>2026-11-18 · 6d ago</sub>

> **App 1.0.7 · firmware 0.2.6 (TestFlight)**
> - Agent: model replies are read off the main thread (board replies no longer wait behind them), and the app logs what the main thread runs when it stalls.
> - Agent: a list whose cards already show every fact the goal asks for is read with `collect` from the top and never opened item by item; a collect stops once older items than the goal's dates show and nothing new does, and the run writes its result at once. One item with several facts (time, amount, start, end) stays one line. The first scroll back up after that is refused with the reason; a second goes through.
> - Agent: higher ceilings: model output 8000 tokens (a reply still cut at its ceiling is asked once more with 16000), each up to 300 items, notes up to 1000 characters and 5000 items, 12 write-up rounds after the hand back.
> - Agent: a done after only writing (snap, note, file, progress) ends the run, unless that file or snap failed.
> - App: a free-line lease request that never reached the server is asked again (five times) and says the connection failed instead of "busy".
> …

### [v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17) — Handsy 1.0.6 build 17 (TestFlight)
<sub>2026-11-15 · 9d ago</sub>

> - App: a start whose Home gestures did nothing while the board's USB is up, but with no mouse on this iPhone,
>   says to plug the board straight into this iPhone and tap Allow for the accessory, and goes on by itself once
>   the mouse shows up (30 s); a board whose USB is asleep asks to unlock the iPhone. It used to say "plug it into
>   USB-C" to users whose board was plugged in.
> - App: when no fresh screen image arrives at startup, the app reopens the board's stream once before asking to
>   restart Screen Mirroring.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [README: first screen says what it does, which board to buy, and one-c…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9b1d512ec319bf79ce572ebe65ee0d686f31a6bd) | onehumanbeing |
| 2026-11-24 | [README: link the setup guides for AI iPhone control, MCP and Claude C…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9ac751618ee644e947646a72b8e0fa6a340fb3fb) | onehumanbeing |
| 2026-11-23 | [Changelog: 1.0.10.1, significantly faster Chinese input (#185)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/90f450ea7c2741901a2b4102c8d209c930961912) | onehumanbeing |
| 2026-11-23 | [App 1.0.10.1: much faster Chinese input (#184)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8e51f56b3ec3e2577226c8bfdc7ca6f2eaae8e30) | onehumanbeing |
| 2026-11-23 | [Hermes Agent plugin: esp32agent MCP server and manina skill (#183)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/6af87ec7a5ad2f19e2d98d39222e19ca4fd1958b) | onehumanbeing |
| 2026-11-22 | [Merge pull request #182 from onehumanbeing/fix/1.0.10](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d1cca3301a5f061a50f42886898d43da67ee74d9) | onehumanbeing |
| 2026-11-22 | [App 1.0.10: collect max saves the result, a reached count goes to the…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8eb875b6a72b86208a23b9ed5980d00b9aa83cda) | onehumanbeing |
| 2026-11-22 | [Merge pull request #180 from huisinro/feat/no-airplay-audio](https://github.com/onehumanbeing/esp32-iphone-agent/commit/97f116a343762ea12739ce21cd040230d6ebf8d1) | onehumanbeing |
| 2026-11-22 | [Merge pull request #181 from onehumanbeing/fw-0.2.8-readme](https://github.com/onehumanbeing/esp32-iphone-agent/commit/1fc4eb377a0a204fc4318a9c9a8a829211a2fdb5) | onehumanbeing |
| 2026-11-22 | [README: iOS 16.4+ with the TestFlight app (iPhone 8 / X), M5Stack Sto…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/f58fb82b581f014393ca1a8d84553fa9aec35274) | onehumanbeing |

[See all commits ↗](https://github.com/onehumanbeing/esp32-iphone-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/onehumanbeing/esp32-iphone-agent.git
```
