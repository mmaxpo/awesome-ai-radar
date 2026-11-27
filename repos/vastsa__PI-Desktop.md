# vastsa/PI-Desktop

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/vastsa/PI-Desktop)

> Local-first AI coding agent desktop: Electron + Rust host core + pi Agent Harness + user-installable plugins

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Chat-first desktop coding agent |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 8.3k |
| 🍴 **Forks** | 827 |
| 🐞 **Open issues + PRs** | [303](https://github.com/vastsa/PI-Desktop/issues) |
| 💻 **Languages** | TypeScript 53% · JavaScript 28% · Rust 15% · CSS 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `pi-desktop` `ai-agent` `coding-agent` `desktop-app` `electron` `global` `i18n` `local-first` `mcp` `pi-agent` `plugins` `react` `rust` `typescript` `pi` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-03-22 |
| 📦 **Latest release** | [v0.23.0](https://github.com/vastsa/PI-Desktop/releases/tag/v0.23.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 220.4 MB |
| 🌐 **Website** | https://www.aiuo.net |

## 📦 Recent releases

### [v0.24.0-beta.5](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.5) _(pre-release)_
<sub>2026-11-25 · 2d ago</sub>

> **What's Changed**
> * fix(transcript): fold finished groups as the turn moves on by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2585
> * feat(chat): align subagent tabs with the conversation display by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2587
> * chore(release): integrate beta.3 into main by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2590
> * chore(release): prepare v0.24.0-beta.4 by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2591
> * fix(composer): keep an empty last line without a phantom character by @G1oow in https://github.com/vastsa/PI-Desktop/pull/2589
> …

### [v0.24.0-beta.3](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.3) _(pre-release)_
<sub>2026-11-25 · 2d ago</sub>

> **What's Changed**
> * fix(desktop): keep image generation model row visible without candidates by @skyler-developer in https://github.com/vastsa/PI-Desktop/pull/2568
> **Full Changelog**: https://github.com/vastsa/PI-Desktop/compare/v0.24.0-beta.2...v0.24.0-beta.3

### [v0.24.0-beta.2](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.2) _(pre-release)_
<sub>2026-11-25 · 2d ago</sub>

> **What's Changed**
> * fix(composer): show full background task commands on expansion by @Linuxdazhao in https://github.com/vastsa/PI-Desktop/pull/2497
> * fix(desktop): 工作面板启动器可再打开一个浏览器页签 by @zszz3 in https://github.com/vastsa/PI-Desktop/pull/2490
> * fix(agent-runtime): accept job plus multi-id TaskWait selectors by @koeria in https://github.com/vastsa/PI-Desktop/pull/2489
> * fix(windows): 应用内更新时沿用已注册的安装范围 by @ZedingZhang in https://github.com/vastsa/PI-Desktop/pull/2486
> * fix(agent-runtime): 修复开启电脑操作后 Agent 拿不到 Computer 工具 by @zszz3 in https://github.com/vastsa/PI-Desktop/pull/2483
> …

### [v0.24.0-beta.1](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.1) _(pre-release)_
<sub>2026-11-20 · 7d ago</sub>

> **What's Changed**
> * fix(config-sync): merge entities absent from one side as implicit deletes by @vastsa in https://github.com/vastsa/PI-Desktop/pull/2457
> * fix(chat): fork visible historical replies outside the live window by @koeria in https://github.com/vastsa/PI-Desktop/pull/2430
> * fix(runtime): explicitly disable Responses strict mode when unsupported by @jeffry88 in https://github.com/vastsa/PI-Desktop/pull/2454
> * fix(chrome): keep conversation actions clear of the work-panel toggle by @Linuxdazhao in https://github.com/vastsa/PI-Desktop/pull/2424
> * fix(composer): refresh context usage after compacting a failed turn by @Seraph-x in https://github.com/vastsa/PI-Desktop/pull/2412
> …

### [v0.23.0](https://github.com/vastsa/PI-Desktop/releases/tag/v0.23.0)
<sub>2026-11-19 · 7d ago</sub>

> **What's Changed**
> * fix(agent-runtime): do not treat connection abort wording as user Stop by @xpeng5278-web in https://github.com/vastsa/PI-Desktop/pull/1865
> * fix(file-manager): theme editor search controls by @AuhNijGnahz in https://github.com/vastsa/PI-Desktop/pull/1861
> * perf(sessions): cache file-derived session summaries by file identity by @CJLY-0915 in https://github.com/vastsa/PI-Desktop/pull/1796
> * fix(ci): keep Electron user-path test out of unit suite by @vastsa in https://github.com/vastsa/PI-Desktop/pull/1872
> * fix(composer): scale the mode chip reservation with the appearance font by @SeanLiu326 in https://github.com/vastsa/PI-Desktop/pull/1879
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [fix(webui): keep late history pages out of the next chat (#2628)](https://github.com/vastsa/PI-Desktop/commit/da30a57b80cf5d22e4929eff934ca8addf865cdc) | ZedingZhang |
| 2026-11-27 | [docs(readme): introduce the LAN WebUI companion](https://github.com/vastsa/PI-Desktop/commit/374317cb99aab6ab4234c97c1e74010443a5cee3) | vastsa |
| 2026-11-27 | [feat(lan-webui): redesign the phone companion around native reading a…](https://github.com/vastsa/PI-Desktop/commit/bfbe8f16666539df04dc76d907a1cc78a6ab986e) | vastsa |
| 2026-11-27 | [feat(lan-webui): fit the companion page to tablet and desktop browsers](https://github.com/vastsa/PI-Desktop/commit/16bf9db86184c081bc8216ff88eae043574b02f6) | vastsa |
| 2026-11-27 | [fix(lan-webui): drop the hard outline around the focused composer](https://github.com/vastsa/PI-Desktop/commit/7abc1c606f90096f30cd35d2ab9f514d956dd591) | vastsa |
| 2026-11-27 | [feat(lan-webui): give every phone page native-grade motion and feedback](https://github.com/vastsa/PI-Desktop/commit/e32fafac3363685b299b64279feb2db0df52bce9) | vastsa |
| 2026-11-27 | [feat(lan-webui): polish the phone conversation and composer](https://github.com/vastsa/PI-Desktop/commit/a99141442623f62c254600567f03dbae5cb0cd36) | vastsa |
| 2026-11-27 | [Merge pull request #2623 from vastsa/feat/lan-webui-model-picker](https://github.com/vastsa/PI-Desktop/commit/bd57246a4bbb33df77dc21babff5433476df0859) | vastsa |
| 2026-11-27 | [test(agent-runtime): synchronize parallel Codemode reads](https://github.com/vastsa/PI-Desktop/commit/f83cf4afcf8b20f74476b3663ba2f3007171718b) | vastsa |
| 2026-11-27 | [fix(ci): run LAN browser journeys on the Electron runner](https://github.com/vastsa/PI-Desktop/commit/eb3d2cfd787bf41fd01f3c2fa3c92ba175eb449c) | vastsa |

[See all commits ↗](https://github.com/vastsa/PI-Desktop/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vastsa/PI-Desktop.git
```
