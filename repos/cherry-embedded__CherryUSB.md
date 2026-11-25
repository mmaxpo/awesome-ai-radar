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
| 🍴 **Forks** | 465 |
| 🐞 **Open issues + PRs** | [9](https://github.com/cherry-embedded/CherryUSB/issues) |
| 💻 **Languages** | C 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `usb-host` `usb-device` `usb` `cdc` `hid` `uvc` `uac` `dfu` `ehci` `hub` `rndis` `musb` `dwc2` `xhci` `cherryusb` `cdns2` `cdns3` `ohci` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2021-07-10 |
| 📦 **Latest release** | [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — 2026-04-27 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 100.4 MB |
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
| 2026-11-25 | [docs: update md & rst](https://github.com/cherry-embedded/CherryUSB/commit/fd76ba101d829fff80272a2038c5caa89de9b42d) | sakumisu |
| 2026-11-25 | [fix(class/serial): synchronize serial close and disconnect cleanup](https://github.com/cherry-embedded/CherryUSB/commit/4095de02001536a84f39a2f334b3f5cf93d9dc6a) | sakumisu |
| 2026-11-25 | [fix(class/msc/usbd_msc): send fail not abort if some scsi cmds do not…](https://github.com/cherry-embedded/CherryUSB/commit/aa27120c4cc291a9d2a8c937b6199e88ce4ea527) | sakumisu |
| 2026-11-25 | [fix(port): fix host port submission, kill and isr completion handling…](https://github.com/cherry-embedded/CherryUSB/commit/87b1b599d821061e660cb760418351d55fff350c) | sakumisu |
| 2026-11-25 | [chore(tool): add wch speed test tool](https://github.com/cherry-embedded/CherryUSB/commit/6b28357d6b140e9dde1feb22e2522a9663c63550) | sakumisu |
| 2026-11-25 | [docs: update rst](https://github.com/cherry-embedded/CherryUSB/commit/537dbd69cbe2dc0887eb7803266c2d510ae9fa52) | sakumisu |
| 2026-11-25 | [update: set enum thread to the lower prio than app prio](https://github.com/cherry-embedded/CherryUSB/commit/87276ca5efd6538c87cc70d01a484379e4ea6ad2) | sakumisu |
| 2026-11-24 | [update(class/msc/usbh_msc): export usbh_msc_modeswitch](https://github.com/cherry-embedded/CherryUSB/commit/5a38fd508ba43d2e406c00cd658858bb80909c30) | sakumisu |
| 2026-11-23 | [add(class/wch): add ch372 vendor class and ch372 template demo](https://github.com/cherry-embedded/CherryUSB/commit/117a079d06f4c904498b30879de06b05c728399b) | Links0617 |
| 2026-11-23 | [fix(port/wch): fix wch usbhs device controller port burst transfer bug](https://github.com/cherry-embedded/CherryUSB/commit/8a9c2100517a8f85b19ffa9d83806ae0f6397165) | Links0617 |

[See all commits ↗](https://github.com/cherry-embedded/CherryUSB/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cherry-embedded/CherryUSB.git
```
