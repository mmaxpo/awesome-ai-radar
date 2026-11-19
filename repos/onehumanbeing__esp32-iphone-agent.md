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
| 🍴 **Forks** | 701 |
| 🐞 **Open issues + PRs** | [25](https://github.com/onehumanbeing/esp32-iphone-agent/issues) |
| 💻 **Languages** | Swift 68% · C 17% · Go 7% · C++ 3% · Python 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `airplay` `computer-use` `esp32` `esp32-s3` `iphone` `llm` `usb-hid` `dsh-plugin` `claude-code` `ios` `ios-automation` `mcp` `mcp-server` `mobile-agent` `phone-agent` `screen-mirroring` `xiao-esp32s3` `manina-ai` `seeed-xiao` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-10-11 |
| 📦 **Latest release** | [v1.0.7](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.7) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 19.0 MB |
| 🌐 **Website** | https://manina.ai?ref=github |

## 📦 Recent releases

### [v1.0.7](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.7) — Manina AI 1.0.7 (TestFlight)
<sub>2026-11-18 · today</sub>

> **App 1.0.7 · firmware 0.2.6 (TestFlight)**
> - Agent: model replies are read off the main thread (board replies no longer wait behind them), and the app logs what the main thread runs when it stalls.
> - Agent: a list whose cards already show every fact the goal asks for is read with `collect` from the top and never opened item by item; a collect stops once older items than the goal's dates show and nothing new does, and the run writes its result at once. One item with several facts (time, amount, start, end) stays one line. The first scroll back up after that is refused with the reason; a second goes through.
> - Agent: higher ceilings: model output 8000 tokens (a reply still cut at its ceiling is asked once more with 16000), each up to 300 items, notes up to 1000 characters and 5000 items, 12 write-up rounds after the hand back.
> - Agent: a done after only writing (snap, note, file, progress) ends the run, unless that file or snap failed.
> - App: a free-line lease request that never reached the server is asked again (five times) and says the connection failed instead of "busy".
> …

### [v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17) — Handsy 1.0.6 build 17 (TestFlight)
<sub>2026-11-15 · 3d ago</sub>

> - App: a start whose Home gestures did nothing while the board's USB is up, but with no mouse on this iPhone,
>   says to plug the board straight into this iPhone and tap Allow for the accessory, and goes on by itself once
>   the mouse shows up (30 s); a board whose USB is asleep asks to unlock the iPhone. It used to say "plug it into
>   USB-C" to users whose board was plugged in.
> - App: when no fresh screen image arrives at startup, the app reopens the board's stream once before asking to
>   restart Screen Mirroring.
> …

### [v1.0.5](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.5) — Handsy 1.0.5 (TestFlight)
<sub>2026-11-13 · 5d ago</sub>

> **Highlights**
> **Phone calls and texts (Beta).** The agent dials, speaks through iOS Live Speech and hears the other side through Live Captions. Here it books a haircut:
> ![Handsy makes a phone call](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-phone-call.gif)
> **Intents improve themselves.** Show a task once; the app works out the steps. When a saved step misses, the run's review finds why and the intent is fixed for the next run:
> ![Record once, then the intent learns](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-record-learns.gif)
> Also new: web search when a task needs it (Tools, Beta), apps opened by name through Spotlight and checked, and reliable typing of Chinese and other scripts.
> …

### [v1.0.4](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.4) — Handsy 1.0.4 (TestFlight)
<sub>2026-11-13 · 5d ago</sub>

> **Highlights**
> - DeepSeek models no longer wait on high-effort thinking for each step (#118).
> - An outdated board gets the update sheet when it connects.
> - Opening the model list no longer crashes on iOS 27.3, and a calibration that misses is not kept.
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> …

### [v1.0.3](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.3) — Handsy 1.0.3 (TestFlight)
<sub>2026-11-13 · 5d ago</sub>

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
| 2026-11-18 | [Tests: on-device tree test waits longer than a phone's look (#174)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/9877aa0900f3e7883a7fe950e810e5d34b0bb839) | onehumanbeing |
| 2026-11-18 | [App 1.0.7: faster list runs, Files search, iPad, LAN mode, firmware 0…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d4d34c0e7ec714cf58d11f97792465575d696ae3) | onehumanbeing |
| 2026-11-18 | [Rebrand Handsy to Manina AI (manina.ai) (#167)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/7947101a615a90de0e9cf7b3ea7e1f6b975a41e5) | onehumanbeing |
| 2026-11-16 | [README: point to the Handsy plug-in device waitlist (#162)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/936d9e12c57f15253b35f4ce704ebebd945a1591) | onehumanbeing |
| 2026-11-15 | [Hotfix: stats no longer crash the app after a board restart (App 1.0.…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d39d6a8414298dc58900713baa19a9f49f277dd1) | onehumanbeing |
| 2026-11-14 | [test(ios): open the yellow step before looking for Unsure (#159)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d9b6febe104f8aa8919eb514805f4736a1b76602) | onehumanbeing |
| 2026-11-14 | [fix(ios): keep demo data out from under the firmware sheet (#158)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/77b6f5a9cbe21e1c7249440265e6ff9e7df77c8a) | onehumanbeing |
| 2026-11-14 | [Startup: say why the board isn't this iPhone's input, retry the strea…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/ce49d0c9311b5b3741c7a14293d804b7ed233235) | onehumanbeing |
| 2026-11-14 | [fix(cli): update tinygo bluetooth to v0.17.0 so the Windows scan find…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/5d4061ee75adfbcc54bca136f9a50af04b5df700) | HenriqueBueno |
| 2026-11-14 | [README: lead the first screen with the result and a star ask (#154)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/cc566b9d946bac7980177d83fc92e398553d919d) | onehumanbeing |

[See all commits ↗](https://github.com/onehumanbeing/esp32-iphone-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/onehumanbeing/esp32-iphone-agent.git
```
