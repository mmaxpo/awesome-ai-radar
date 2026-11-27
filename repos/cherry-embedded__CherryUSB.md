# cherry-embedded/CherryUSB

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/cherry-embedded/CherryUSB)

> CherryUSB is a tiny and beautiful, high performance and portable USB host and device stack for embedded system with USB IP

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧰 Open-source utilities |
| **Project** | — |
| **Why it's worth a look** | USB host/device stack for microcontrollers |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 2.1k |
| 🍴 **Forks** | 466 |
| 🐞 **Open issues + PRs** | [9](https://github.com/cherry-embedded/CherryUSB/issues) |
| 💻 **Languages** | C 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `usb-host` `usb-device` `usb` `cdc` `hid` `uvc` `uac` `dfu` `ehci` `hub` `rndis` `musb` `dwc2` `xhci` `cherryusb` `cdns2` `cdns3` `ohci` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2021-07-10 |
| 📦 **Latest release** | [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — 2026-04-27 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 100.5 MB |
| 🌐 **Website** | https://cherryusb.readthedocs.io |

## 📦 Recent releases

### [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — CherryUSB v1.6.1
<sub>2026-04-27 · 7mo ago</sub>

> **Hi, there, this version is a freeze version, the next release time we planned is 2026-12-31, thank you for supporting cherryusb!**
> **Common**
> - update(xbox): Xbox USB host driver support into build(#407)
> - refactor: move cherryrb and cherrymp into common dir, rename with usb_ringbuffer and usb_mempool
> - update(demo): format mouse report comment
> - update(demo): change string index max to sizeof(string_descriptors) / sizeof(char *))
> …

### [v1.6.0](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.0) — CherryUSB v1.6.0
<sub>2026-01-27 · 10mo ago</sub>

> **Common**
> - update(demo): remove all old desc api
> **Device**
> - feat(class/gamepad): add gamepad device #392
> **Host**
> - feat:  host add event callback mechanism similar to device @Egahp
> …

### [v1.5.3.99](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.5.3.99) — CherryUSB v1.5.3.99
<sub>2026-01-22 · 10mo ago</sub>

> This is the last version for release/v1.5.
> **Common**
> - refactor(osal): replace NuttX internal APIs with POSIX APIs @SunJun8
> - fix(demo): fix cdc ecm string check
> **Device**
> **Host**
> …

### [v1.5.3](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.5.3) — CherryUSB v1.5.3
<sub>2025-12-12 · 11mo ago</sub>

> **Common**
> - feat(demo): add mongoose rndis demo
> - update(demo/cdc_acm_rttchardev): add finsh & console switch with usb
> - update: remove old bl616 wifi driver, add new api
> - update(demo): format uac demos with macros
> - update(demo): add more descriptor init macros
> …

### [v1.5.2](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.5.2) — CherryUSB v1.5.2
<sub>2025-08-07 · 1y ago</sub>

> **Common**
> - update(common/usb_hc): change interval u8 to u32 for us
> - update(usb_config): change CONFIG_USBHOST_MAX_INTF_ALTSETTINGS to 2 as default for less memory usage
> - update(osal/idf): change freertos timer to esp_timer, change xtaskcreate to xTaskCreatePinnedToCore
> - fix(common/usb_util): fix missing __ICCARM_V8 define
> - style: remove some logs, fix log typo, format log
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [docs: update rst](https://github.com/cherry-embedded/CherryUSB/commit/1e8817b70adda37c03837d7460083156c1a1b471) | sakumisu |
| 2026-11-27 | [fix(port): fix setup->bmRequestType with USB_REQUEST_RECIPIENT_MASK](https://github.com/cherry-embedded/CherryUSB/commit/eee13087480c84c43b5c443d6112aa72e79b7f13) | sakumisu |
| 2026-11-27 | [fix(port): fix host port timeout and complete completion handling](https://github.com/cherry-embedded/CherryUSB/commit/954345ec88d188ad53bc9c5c9952b873392a899c) | sakumisu |
| 2026-11-27 | [refactor(class): refactor host net class, add link monitor and fix so…](https://github.com/cherry-embedded/CherryUSB/commit/1bf816b921093a2c7266a694f360960407ef0363) | sakumisu |
| 2026-11-26 | [docs: update md & rst](https://github.com/cherry-embedded/CherryUSB/commit/e98a9a2a572ccc5da62cac87e324a0f7bc9a3231) | sakumisu |
| 2026-11-26 | [fix(class/serial): synchronize serial close and disconnect cleanup](https://github.com/cherry-embedded/CherryUSB/commit/554723213c077eae0055d0802328035e65c05fc9) | sakumisu |
| 2026-11-25 | [fix(class/msc/usbd_msc): send fail not abort if some scsi cmds do not…](https://github.com/cherry-embedded/CherryUSB/commit/aa27120c4cc291a9d2a8c937b6199e88ce4ea527) | sakumisu |
| 2026-11-25 | [fix(port): fix host port submission, kill and isr completion handling…](https://github.com/cherry-embedded/CherryUSB/commit/87b1b599d821061e660cb760418351d55fff350c) | sakumisu |
| 2026-11-25 | [chore(tool): add wch speed test tool](https://github.com/cherry-embedded/CherryUSB/commit/6b28357d6b140e9dde1feb22e2522a9663c63550) | sakumisu |
| 2026-11-25 | [docs: update rst](https://github.com/cherry-embedded/CherryUSB/commit/537dbd69cbe2dc0887eb7803266c2d510ae9fa52) | sakumisu |

[See all commits ↗](https://github.com/cherry-embedded/CherryUSB/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cherry-embedded/CherryUSB.git
```
