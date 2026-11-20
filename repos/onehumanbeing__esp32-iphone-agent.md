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
| ⭐ **Stars** | 5.1k |
| 🍴 **Forks** | 708 |
| 🐞 **Open issues + PRs** | [25](https://github.com/onehumanbeing/esp32-iphone-agent/issues) |
| 💻 **Languages** | Swift 68% · C 16% · Go 7% · C++ 4% · Python 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `airplay` `computer-use` `esp32` `esp32-s3` `iphone` `llm` `usb-hid` `dsh-plugin` `claude-code` `ios` `ios-automation` `mcp` `mcp-server` `mobile-agent` `phone-agent` `screen-mirroring` `xiao-esp32s3` `manina-ai` `seeed-xiao` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-10-11 |
| 📦 **Latest release** | [v1.0.7](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.7) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 19.6 MB |
| 🌐 **Website** | https://manina.ai?ref=github |

## 📦 Recent releases

### [v1.0.7](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.7) — Manina AI 1.0.7 (TestFlight)
<sub>2026-11-18 · yesterday</sub>

> **App 1.0.7 · firmware 0.2.6 (TestFlight)**
> - Agent: model replies are read off the main thread (board replies no longer wait behind them), and the app logs what the main thread runs when it stalls.
> - Agent: a list whose cards already show every fact the goal asks for is read with `collect` from the top and never opened item by item; a collect stops once older items than the goal's dates show and nothing new does, and the run writes its result at once. One item with several facts (time, amount, start, end) stays one line. The first scroll back up after that is refused with the reason; a second goes through.
> - Agent: higher ceilings: model output 8000 tokens (a reply still cut at its ceiling is asked once more with 16000), each up to 300 items, notes up to 1000 characters and 5000 items, 12 write-up rounds after the hand back.
> - Agent: a done after only writing (snap, note, file, progress) ends the run, unless that file or snap failed.
> - App: a free-line lease request that never reached the server is asked again (five times) and says the connection failed instead of "busy".
> …

### [v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17) — Handsy 1.0.6 build 17 (TestFlight)
<sub>2026-11-15 · 4d ago</sub>

> - App: a start whose Home gestures did nothing while the board's USB is up, but with no mouse on this iPhone,
>   says to plug the board straight into this iPhone and tap Allow for the accessory, and goes on by itself once
>   the mouse shows up (30 s); a board whose USB is asleep asks to unlock the iPhone. It used to say "plug it into
>   USB-C" to users whose board was plugged in.
> - App: when no fresh screen image arrives at startup, the app reopens the board's stream once before asking to
>   restart Screen Mirroring.
> …

### [v1.0.5](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.5) — Handsy 1.0.5 (TestFlight)
<sub>2026-11-13 · 6d ago</sub>

> **Highlights**
> **Phone calls and texts (Beta).** The agent dials, speaks through iOS Live Speech and hears the other side through Live Captions. Here it books a haircut:
> ![Handsy makes a phone call](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-phone-call.gif)
> **Intents improve themselves.** Show a task once; the app works out the steps. When a saved step misses, the run's review finds why and the intent is fixed for the next run:
> ![Record once, then the intent learns](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-record-learns.gif)
> Also new: web search when a task needs it (Tools, Beta), apps opened by name through Spotlight and checked, and reliable typing of Chinese and other scripts.
> …

### [v1.0.4](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.4) — Handsy 1.0.4 (TestFlight)
<sub>2026-11-13 · 6d ago</sub>

> **Highlights**
> - DeepSeek models no longer wait on high-effort thinking for each step (#118).
> - An outdated board gets the update sheet when it connects.
> - Opening the model list no longer crashes on iOS 27.3, and a calibration that misses is not kept.
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> …

### [v1.0.3](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.3) — Handsy 1.0.3 (TestFlight)
<sub>2026-11-13 · 6d ago</sub>

> **Highlights**
> A fix release: typing Chinese no longer crashes the app (#111), the app builds with Xcode 26.3 and 27 (#112), and a round of several gestures goes to the model so a plan isn't redone.
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> TestFlight build 11. Tagged on the main commit that carries this version.
> - Free line: requests carry the iPhone's model (e.g. `iPhone18,2`, `X-Device-Model`) to adapt to its screen;
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [App 1.0.8 · firmware v0.2.7: Bluetooth mode, faster Chinese typing, s…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/e387137d873a32fb7a5c3d7e07b7ab4489b7e11d) | onehumanbeing |
| 2026-11-20 | [Free line: the leftover lease kept in memory too, where the keychain …](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d0e45d53d616b543f4a7fe694f4a358e52c92cc1) | onehumanbeing |
| 2026-11-20 | [Merge remote-tracking branch 'origin/main' into test/108-ble](https://github.com/onehumanbeing/esp32-iphone-agent/commit/33fafc72d7eae196f3da018051778653ce8bcd09) | onehumanbeing |
| 2026-11-20 | [README: Bluetooth mode (1.0.8, firmware v0.2.7), with thanks to @cy41…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/52f222e7a5fd8a436cd1af059bd7212041c522a0) | onehumanbeing |
| 2026-11-20 | [Runs: a review set in the background no longer blocks opening runs](https://github.com/onehumanbeing/esp32-iphone-agent/commit/1bc446bf0e9c0e474643da9b808bcbc087afff53) | onehumanbeing |
| 2026-11-20 | [Tests: a typing nothing on screen shows stops and deletes nothing](https://github.com/onehumanbeing/esp32-iphone-agent/commit/6ecad936825e4f1a81e7f3ba9cc4abf94b059796) | onehumanbeing |
| 2026-11-20 | [Merge branch 'ui/runs-delete-all' into test/108-ble](https://github.com/onehumanbeing/esp32-iphone-agent/commit/34715f4b9613fe35e2f7be85130fea08dd12a1d2) | onehumanbeing |
| 2026-11-20 | [Merge branch 'fix/open-spotlight-tap' into test/108-ble](https://github.com/onehumanbeing/esp32-iphone-agent/commit/22838535ff6155fbd9c5084793b92913c90e7f27) | onehumanbeing |
| 2026-11-20 | [Typing: stop when nothing reached the field instead of taking unread …](https://github.com/onehumanbeing/esp32-iphone-agent/commit/2868b093d1aef606b0a1a81cbd0cb3a1dde8d27b) | onehumanbeing |
| 2026-11-20 | [Runs: Delete All Runs / Delete Failed Runs in the toolbar menu](https://github.com/onehumanbeing/esp32-iphone-agent/commit/e6425235d3abd212c6204a2aabe63bf04ae2550f) | onehumanbeing |

[See all commits ↗](https://github.com/onehumanbeing/esp32-iphone-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/onehumanbeing/esp32-iphone-agent.git
```
