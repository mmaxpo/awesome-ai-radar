# onehumanbeing/esp32-iphone-agent

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/onehumanbeing/esp32-iphone-agent)

> Let an AI model use a real iPhone with a $7 ESP32: AirPlay eyes, USB HID hands, any OpenAI-compatible vision model. No Mac, no developer account, no jailbreak.

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
| ⭐ **Stars** | 4.9k |
| 🍴 **Forks** | 676 |
| 🐞 **Open issues + PRs** | [16](https://github.com/onehumanbeing/esp32-iphone-agent/issues) |
| 💻 **Languages** | Swift 61% · C 21% · Go 9% · C++ 4% · Python 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `airplay` `automation` `computer-use` `esp32` `esp32-s3` `iphone` `llm` `usb-hid` `dsh-plugin` `claude-code` `ios` `ios-automation` `mcp` `mcp-server` `mobile-agent` `phone-agent` `screen-mirroring` `seeed-xiao` `xiao-esp32s3` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-10-11 |
| 📦 **Latest release** | [v1.0.5](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.5) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 18.6 MB |
| 🌐 **Website** | https://handsy.tech?ref=github |

## 📦 Recent releases

### [v1.0.5](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.5) — Handsy 1.0.5 (TestFlight)
<sub>2026-11-13 · today</sub>

> **Highlights**
> **Phone calls and texts (Beta).** The agent dials, speaks through iOS Live Speech and hears the other side through Live Captions. Here it books a haircut:
> ![Handsy makes a phone call](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-phone-call.gif)
> **Intents improve themselves.** Show a task once; the app works out the steps. When a saved step misses, the run's review finds why and the intent is fixed for the next run:
> ![Record once, then the intent learns](https://github.com/onehumanbeing/esp32-iphone-agent/releases/download/v1.0.5/handsy-1.0.5-record-learns.gif)
> Also new: web search when a task needs it (Tools, Beta), apps opened by name through Spotlight and checked, and reliable typing of Chinese and other scripts.
> …

### [v1.0.4](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.4) — Handsy 1.0.4 (TestFlight)
<sub>2026-11-13 · today</sub>

> **Highlights**
> - DeepSeek models no longer wait on high-effort thinking for each step (#118).
> - An outdated board gets the update sheet when it connects.
> - Opening the model list no longer crashes on iOS 27.3, and a calibration that misses is not kept.
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> …

### [v1.0.3](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.3) — Handsy 1.0.3 (TestFlight)
<sub>2026-11-13 · today</sub>

> **Highlights**
> A fix release: typing Chinese no longer crashes the app (#111), the app builds with Xcode 26.3 and 27 (#112), and a round of several gestures goes to the model so a plan isn't redone.
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> TestFlight build 11. Tagged on the main commit that carries this version.
> - Free line: requests carry the iPhone's model (e.g. `iPhone18,2`, `X-Device-Model`) to adapt to its screen;
> …

### [v1.0.1](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.1) — Handsy 1.0.1 (TestFlight)
<sub>2026-11-13 · today</sub>

> **Highlights**
> The first iPhone app. No computer in the middle: the ESP32 board is the AirPlay receiver and the iPhone's USB mouse and keyboard, and the app on the iPhone is the agent. It plans, looks at the mirrored screen and acts, with a Live Activity, Siri and Shortcuts, and recovers by itself when the board, hotspot or mirroring drops.
> ![Handsy on a real iPhone](https://github.com/onehumanbeing/esp32-iphone-agent/raw/main/docs/images/demo.gif)
> Join the TestFlight beta: https://testflight.apple.com/join/1xQHgJcA · Firmware and setup: https://handsy.tech/install
> ---
> TestFlight build 9. Tagged on the main commit that carries this version.
> …

### [v1.0.6](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6) — Handsy 1.0.6 (TestFlight)
<sub>2026-11-13 · today</sub>

> **Highlights**
> - **Standby in Dynamic Island**: between runs the island offers your most used intents and New Task, so a task starts from whatever app you are in.
> - **Add to a running task**: words typed while it runs join its next step.
> - **Tasks over many items**: the agent lists what matches, asks once with how many, then runs up to 1000 steps; repeated taps are done without a model call each time.
> - **One memory** for the app and the CLI (`esp32agent memory`, MCP `memory_recall` / `memory_add`).
> - Optional absolute-mouse firmware (`hardware/flash.sh --abs`): no pointer calibration.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [App 1.0.6: record learning, steer, standby island, long tasks, absolu…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/39aa23e17de957bc01529fbd8f22f4deef0e08ca) | onehumanbeing |
| 2026-11-12 | [fastlane: export with App Store Connect API key cloud signing (no Xco…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/87ddf6cf082c58a078c47f2b805c240205d0d516) | onehumanbeing |
| 2026-11-12 | [Changelog 1.0.5: intents improve themselves (#151)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/788d9f16afd3b9b71772ec8bdd3e01fb834bb5d2) | onehumanbeing |
| 2026-11-12 | [Agent fixes: open apps by code, Chinese/accented typing, tap verdict,…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/1e16a02fdefcc8a358badf26d95ee56f49718561) | onehumanbeing |
| 2026-11-12 | [Firmware 0.2.5: lost video packets reported, press_for, result, net w…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/119801dd98757a3133d9d78b788e6a527fd6653b) | onehumanbeing |
| 2026-11-10 | [test(ios): inject the Keychain so the key tests also run in CI (#143)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/5a4fddfbb1f2ce25fee9de816f93259ec5e3b9fa) | djs-91 |
| 2026-11-09 | [fix(ios): remove the saved key when the user clears the API key (#137)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/92b472fe0d46e0e8802c67915d20b236d145ab0e) | djs-91 |
| 2026-11-09 | [Docs: wait_idr after boot means an IDR too big for the buffer (follow…](https://github.com/onehumanbeing/esp32-iphone-agent/commit/0cb40beff4b92b0ccdec5266ee4e12a61658f116) | onehumanbeing |
| 2026-11-09 | [fix(video): snap returns err waiting for keyframe while wait_idr (#132)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/4b175ea45121802de30360fef0b373826b853dcd) | shinjiyu |
| 2026-11-08 | [test(daemon): fail instead of hang when onStatus holds c.mu (#126)](https://github.com/onehumanbeing/esp32-iphone-agent/commit/8574ef7e03db708f9c7c0ffc9407936850ff3eeb) | onehumanbeing |

[See all commits ↗](https://github.com/onehumanbeing/esp32-iphone-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/onehumanbeing/esp32-iphone-agent.git
```
