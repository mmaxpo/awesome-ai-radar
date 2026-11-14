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
| 🍴 **Forks** | 464 |
| 🐞 **Open issues + PRs** | [9](https://github.com/cherry-embedded/CherryUSB/issues) |
| 💻 **Languages** | C 98% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `usb-host` `usb-device` `usb` `cdc` `hid` `uvc` `uac` `dfu` `ehci` `hub` `rndis` `musb` `dwc2` `xhci` `cherryusb` `cdns2` `cdns3` `ohci` |
| 🕒 **Last activity** | 2026-11-11 (3d ago) |
| 📅 **Created** | 2021-07-10 |
| 📦 **Latest release** | [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — 2026-04-27 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 94.5 MB |
| 🌐 **Website** | https://cherryusb.readthedocs.io |

## 📦 Recent releases

### [v1.6.1](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.1) — CherryUSB v1.6.1
<sub>2026-04-27 · 6mo ago</sub>

> **Hi, there, this version is a freeze version, the next release time we planned is 2026-12-31, thank you for supporting cherryusb!**
> **Common**
> - update(xbox): Xbox USB host driver support into build(#407)
> - refactor: move cherryrb and cherrymp into common dir, rename with usb_ringbuffer and usb_mempool
> - update(demo): format mouse report comment
> - update(demo): change string index max to sizeof(string_descriptors) / sizeof(char *))
> …

### [v1.6.0](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.6.0) — CherryUSB v1.6.0
<sub>2026-01-27 · 9mo ago</sub>

> **Common**
> - update(demo): remove all old desc api
> **Device**
> - feat(class/gamepad): add gamepad device #392
> **Host**
> - feat:  host add event callback mechanism similar to device @Egahp
> …

### [v1.5.3.99](https://github.com/cherry-embedded/CherryUSB/releases/tag/v1.5.3.99) — CherryUSB v1.5.3.99
<sub>2026-01-22 · 9mo ago</sub>

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
| 2026-11-11 | [fix(port/wch usbhsd): Fix the TOG mismatch issue following a bus rese…](https://github.com/cherry-embedded/CherryUSB/commit/05007a0cdcf480ff5e870ce142bc92c217060fc8) | Links0617 |
| 2026-11-10 | [update(port/aic): sync code from luban lite](https://github.com/cherry-embedded/CherryUSB/commit/a0054795c44037ace8a2b77b6e610adbff2257ea) | sakumisu |
| 2026-11-09 | [update(port/dwc2): adjust register macros order](https://github.com/cherry-embedded/CherryUSB/commit/692e0697c5a60534fb2b8a2edff9a4a4c2f6edba) | sakumisu |
| 2026-11-08 | [fix(ci): fix ci new build](https://github.com/cherry-embedded/CherryUSB/commit/6081dee3f7acdeb2d920b163148909f36acec4a9) | sakumisu |
| 2026-11-08 | [feat(port/dwc2): support dwc2 dev desc dma mode](https://github.com/cherry-embedded/CherryUSB/commit/890a9403754ad069975293fa9e6707e8e1ca8630) | sakumisu |
| 2026-11-08 | [fix(ci): fix iperf last return](https://github.com/cherry-embedded/CherryUSB/commit/cffeac73323c8ca2e1ae9335e5fe35c498cccbb6) | sakumisu |
| 2026-10-30 | [update(port/dwc2/esp): add esp32h4 support](https://github.com/cherry-embedded/CherryUSB/commit/1cf7193676584a0c2bbfa53bf88b13b65a063130) | YanKE01 |
| 2026-10-27 | [fix(port/ehci): fix errors before halt, because halt covers other errors](https://github.com/cherry-embedded/CherryUSB/commit/75ca4bc51fee722eda59ee155ad7025f345e01ab) | sakumisu |
| 2026-10-27 | [fix(security): fix cdc without iad](https://github.com/cherry-embedded/CherryUSB/commit/601ba123afce8562c8cacb939547467d68f6b91c) | sakumisu |
| 2026-10-24 | [fix(security): fix many security vulnerabilities](https://github.com/cherry-embedded/CherryUSB/commit/e5e197bf4f69993de7e81ab2fa94323ff72f5621) | sakumisu |

[See all commits ↗](https://github.com/cherry-embedded/CherryUSB/commits)

## ⬇️ Get it

```bash
git clone https://github.com/cherry-embedded/CherryUSB.git
```
