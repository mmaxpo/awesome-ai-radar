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
| ⭐ **Stars** | 8.2k |
| 🍴 **Forks** | 815 |
| 🐞 **Open issues + PRs** | [275](https://github.com/vastsa/PI-Desktop/issues) |
| 💻 **Languages** | TypeScript 53% · JavaScript 28% · Rust 15% · CSS 3% |
| 📜 **License** | LGPL-3.0 |
| 🏷 **Topics** | `pi-desktop` `ai-agent` `coding-agent` `desktop-app` `electron` `global` `i18n` `local-first` `mcp` `pi-agent` `plugins` `react` `rust` `typescript` `pi` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-03-22 |
| 📦 **Latest release** | [v0.23.0](https://github.com/vastsa/PI-Desktop/releases/tag/v0.23.0) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 226.2 MB |
| 🌐 **Website** | https://www.aiuo.net |

## 📦 Recent releases

### [v0.24.0-beta.5](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.5) _(pre-release)_
<sub>2026-11-25 · today</sub>

> **What's Changed**
> * fix(transcript): fold finished groups as the turn moves on by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2585
> * feat(chat): align subagent tabs with the conversation display by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2587
> * chore(release): integrate beta.3 into main by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2590
> * chore(release): prepare v0.24.0-beta.4 by @Tioit-Wang in https://github.com/vastsa/PI-Desktop/pull/2591
> * fix(composer): keep an empty last line without a phantom character by @G1oow in https://github.com/vastsa/PI-Desktop/pull/2589
> …

### [v0.24.0-beta.3](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.3) _(pre-release)_
<sub>2026-11-25 · today</sub>

> **What's Changed**
> * fix(desktop): keep image generation model row visible without candidates by @skyler-developer in https://github.com/vastsa/PI-Desktop/pull/2568
> **Full Changelog**: https://github.com/vastsa/PI-Desktop/compare/v0.24.0-beta.2...v0.24.0-beta.3

### [v0.24.0-beta.2](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.2) _(pre-release)_
<sub>2026-11-25 · today</sub>

> **What's Changed**
> * fix(composer): show full background task commands on expansion by @Linuxdazhao in https://github.com/vastsa/PI-Desktop/pull/2497
> * fix(desktop): 工作面板启动器可再打开一个浏览器页签 by @zszz3 in https://github.com/vastsa/PI-Desktop/pull/2490
> * fix(agent-runtime): accept job plus multi-id TaskWait selectors by @koeria in https://github.com/vastsa/PI-Desktop/pull/2489
> * fix(windows): 应用内更新时沿用已注册的安装范围 by @ZedingZhang in https://github.com/vastsa/PI-Desktop/pull/2486
> * fix(agent-runtime): 修复开启电脑操作后 Agent 拿不到 Computer 工具 by @zszz3 in https://github.com/vastsa/PI-Desktop/pull/2483
> …

### [v0.24.0-beta.1](https://github.com/vastsa/PI-Desktop/releases/tag/v0.24.0-beta.1) _(pre-release)_
<sub>2026-11-20 · 5d ago</sub>

> **What's Changed**
> * fix(config-sync): merge entities absent from one side as implicit deletes by @vastsa in https://github.com/vastsa/PI-Desktop/pull/2457
> * fix(chat): fork visible historical replies outside the live window by @koeria in https://github.com/vastsa/PI-Desktop/pull/2430
> * fix(runtime): explicitly disable Responses strict mode when unsupported by @jeffry88 in https://github.com/vastsa/PI-Desktop/pull/2454
> * fix(chrome): keep conversation actions clear of the work-panel toggle by @Linuxdazhao in https://github.com/vastsa/PI-Desktop/pull/2424
> * fix(composer): refresh context usage after compacting a failed turn by @Seraph-x in https://github.com/vastsa/PI-Desktop/pull/2412
> …

### [v0.23.0](https://github.com/vastsa/PI-Desktop/releases/tag/v0.23.0)
<sub>2026-11-19 · 6d ago</sub>

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
| 2026-11-25 | [Merge pull request #2593 from vastsa/release/beta5-composer](https://github.com/vastsa/PI-Desktop/commit/720bbe15de8d69aa4c921388cfae12e376151caf) | Tioit-Wang |
| 2026-11-25 | [chore(release): refresh beta.5 against the merged composer fix](https://github.com/vastsa/PI-Desktop/commit/04d5108f3ce62504df376a68de3f16a6e8a753fe) | Tioit-Wang |
| 2026-11-25 | [Merge pull request #2589 from G1oow/fix/composer-tail-placeholder](https://github.com/vastsa/PI-Desktop/commit/f837ea906e19bb04a77ef4f8c20495eae12066f9) | Tioit-Wang |
| 2026-11-25 | [test(composer): align the native paragraph guard contract](https://github.com/vastsa/PI-Desktop/commit/3083e6a78fbb249bd883e3560d2e8418d64058a2) | Tioit-Wang |
| 2026-11-25 | [chore(release): prepare v0.24.0-beta.5](https://github.com/vastsa/PI-Desktop/commit/a5d39de9f9e3d8a3ddfae5d7a0c9cb76fd7a9093) | Tioit-Wang |
| 2026-11-25 | [feat(composer): integrate skill chips with native multiline editing](https://github.com/vastsa/PI-Desktop/commit/ff5749bcec2e78e84d222270205952c7651a9844) | Tioit-Wang |
| 2026-11-25 | [fix(composer): preserve the native undo anchor for tail deletion](https://github.com/vastsa/PI-Desktop/commit/ff01d91ee729244b2ad27f43aea322a392f4c616) | Tioit-Wang |
| 2026-11-25 | [feat(composer): render selected skills as inline nodes](https://github.com/vastsa/PI-Desktop/commit/70c91e0ef6f19b2179fbb2407c0a930fb203b206) | Tioit-Wang |
| 2026-11-25 | [Merge remote-tracking branch 'upstream/main' into fix/composer-tail-p…](https://github.com/vastsa/PI-Desktop/commit/b116666fd2dc41ae76ab3dda456d25638c8002cf) | G1oow |
| 2026-11-25 | [fix(composer): keep the end-of-draft break in the native undo stack](https://github.com/vastsa/PI-Desktop/commit/3bffe922a98f9e0ac8f127d8b7fec504711f5ad3) | G1oow |

[See all commits ↗](https://github.com/vastsa/PI-Desktop/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vastsa/PI-Desktop.git
```
