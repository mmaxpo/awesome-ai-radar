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
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2021-07-10 |
| 📦 **Latest release** | [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — 2026-04-27 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 94.7 MB |
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
| 2026-11-23 | [add(class/wch): add ch372 vendor class and ch372 template demo](https://github.com/cherry-embedded/CherryUSB/commit/117a079d06f4c904498b30879de06b05c728399b) | Links0617 |
| 2026-11-23 | [fix(port/wch): fix wch usbhs device controller port burst transfer bug](https://github.com/cherry-embedded/CherryUSB/commit/8a9c2100517a8f85b19ffa9d83806ae0f6397165) | Links0617 |
| 2026-11-23 | [fix(port/wch): fix wch usbss device controller port burst transfer bug](https://github.com/cherry-embedded/CherryUSB/commit/6bbe0b2c47b82e28913061745e7d18e8f1bbeef2) | Links0617 |
| 2026-11-20 | [add(port/wch): add wch usbss device controller port](https://github.com/cherry-embedded/CherryUSB/commit/b518afb1475d9de4b019e2e6c7664a1a4f2d899a) | Links0617 |
| 2026-11-18 | [fix(security): check qh urb valid](https://github.com/cherry-embedded/CherryUSB/commit/7835d108baea5190f84060337bdb110810c1c7c1) | sakumisu |
| 2026-11-18 | [fix(security): fix ep0 setup competition issue](https://github.com/cherry-embedded/CherryUSB/commit/962339a3d3c6619881c9c67379680e7b66dc21c3) | sakumisu |
| 2026-11-18 | [update(class): free class immediately in xxx_connect when return error](https://github.com/cherry-embedded/CherryUSB/commit/62c3ff3c07b79dafbbd3dfaf0a354b9e718e31aa) | sakumisu |
| 2026-11-17 | [fix(class/wireless/usbh_rndis): do not check g_rndis_rx_length with e…](https://github.com/cherry-embedded/CherryUSB/commit/738dedc6ec1968190ef17805fc4e37edbaec4ff3) | sakumisu |
| 2026-11-11 | [fix(port/wch usbhsd): Fix the TOG mismatch issue following a bus rese…](https://github.com/cherry-embedded/CherryUSB/commit/05007a0cdcf480ff5e870ce142bc92c217060fc8) | Links0617 |
| 2026-11-10 | [update(port/aic): sync code from luban lite](https://github.com/cherry-embedded/CherryUSB/commit/a0054795c44037ace8a2b77b6e610adbff2257ea) | sakumisu |

[See all commits ↗](https://github.com/cherry-embedded/CherryUSB/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cherry-embedded/CherryUSB.git
```
