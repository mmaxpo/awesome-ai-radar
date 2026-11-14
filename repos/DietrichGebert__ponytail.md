# DietrichGebert/ponytail

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/DietrichGebert/ponytail)

> Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Rules for coding agents |
| **Added** | 2026-11-14 |

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 190.8k |
| 🍴 **Forks** | 10.7k |
| 🐞 **Open issues + PRs** | [235](https://github.com/DietrichGebert/ponytail/issues) |
| 💻 **Languages** | JavaScript 49% · Python 25% · TypeScript 25% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `ai-agents` `claude` `claude-code` `claude-code-plugin` `cursor-rules` `developer-tools` `llm` `prompt-engineering` `yagni` |
| 🕒 **Last activity** | 2026-10-29 (16d ago) |
| 📅 **Created** | 2026-06-12 |
| 📦 **Latest release** | [v5.3.3](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3) — 2026-10-29 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 12.8 MB |
| 🌐 **Website** | https://ponytail.dev |

## 📦 Recent releases

### [v5.3.3](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3)
<sub>2026-10-29 · 16d ago</sub>

> This one cleans up the band. On Team, Enterprise and managed machines the warning on your first prompt is gone, and the band shows your model and session name again. In VS Code it stays on one line, other plugins' commands no longer print under ponytail's name, and the noisy "duplicate?" hint is gone.
> **What's Changed**
> * fix(band): show the level again after /clear and /resume by @timofeevAV in https://github.com/DietrichGebert/ponytail/pull/1161
> * fix(map): raise the git ls-files buffer so large repos keep tracked files by @HyperionBurn in https://github.com/DietrichGebert/ponytail/pull/1156
> * ci: run agentic benchmark selftest in test workflow by @ml-lubich in https://github.com/DietrichGebert/ponytail/pull/1154
> * docs: clarify Cursor mode state scope by @Boulea7 in https://github.com/DietrichGebert/ponytail/pull/1135
> …

### [v5.3.2](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.2)
<sub>2026-10-16 · 28d ago</sub>

> Ponytail 5.3.2 brings your old sessions to the board. `/ponytail band import` reads your past Claude Code sessions once and adds them with their cost, agent time and tokens, so you can compare them with today's. The board also shows which model each session used.
> **What's Changed**
> * feat(band): past sessions and the model on the board by @DietrichGebert in https://github.com/DietrichGebert/ponytail/pull/1152
> * chore: release v5.3.2 by @DietrichGebert in https://github.com/DietrichGebert/ponytail/pull/1153
> **Full Changelog**: https://github.com/DietrichGebert/ponytail/compare/v5.3.1...v5.3.2

### [v5.3.1](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.1)
<sub>2026-10-16 · 29d ago</sub>

> Ponytail 5.3.1 fixes the band from 5.3. Other mods above the Claude Code prompt now show below the band instead of disappearing, and on Windows the band finds its files without `HOME` and writes the task ledger and board without `mkdir`. Thanks to @AllDmeat and @mohofo7 for the fixes, and to @tomkor and @1410822048 for the reports.
> **What's Changed**
> * fix(band): stack other mods' bands below ours instead of replacing them by @AllDmeat in https://github.com/DietrichGebert/ponytail/pull/1146
> * fix(band): fall back to USERPROFILE when HOME is unset by @mohofo7 in https://github.com/DietrichGebert/ponytail/pull/1144
> * fix(band): write the ledger and board without mkdir by @mohofo7 in https://github.com/DietrichGebert/ponytail/pull/1145
> * chore: release v5.3.1 by @DietrichGebert in https://github.com/DietrichGebert/ponytail/pull/1147
> …

### [v5.3.0](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.0)
<sub>2026-10-16 · 29d ago</sub>

> Ponytail 5.3 puts a band above the Claude Code prompt: what the current task costs, its tokens and agent time, how much existing code it reused, and whether the tests still pass. One click opens the board, a local page with every task across your projects and a card to share. Everything stays on your machine by default, `/ponytail band` hides it, and it needs Claude Code 2.1.290 or later.
> ![The ponytail band in Claude Code](https://raw.githubusercontent.com/DietrichGebert/ponytail/v5.3.0/assets/band/band.png)
> **What's Changed**
> * fix(qoder): keep the ruleset on the /ponytail default turn by @htjworld in https://github.com/DietrichGebert/ponytail/pull/1115
> * fix(hermes): send the off notice after /ponytail off (#1121) by @szsunyuan in https://github.com/DietrichGebert/ponytail/pull/1122
> * fix(skills): remove misleading one-shot revert instructions by @kaya0s in https://github.com/DietrichGebert/ponytail/pull/1125
> …

### [v5.2.0](https://github.com/DietrichGebert/ponytail/releases/tag/v5.2.0)
<sub>2026-10-13 · 1mo ago</sub>

> Mostly fixes for the level you pick. It now survives context compaction instead of falling back to the default, and on macOS the hooks can no longer lose their output, so the ruleset always arrives.
> Also in here: the Cursor installer leaves hooks.json files it doesn't understand alone and no longer removes your own hooks with a similar name, OpenCode doesn't get stuck in review anymore and supports `/ponytail default`, pi completes `/ponytail` arguments, and OMP starts new sessions at the default level. Thanks to everyone who sent fixes!
> **What's Changed**
> * fix(bench): a crashed cell no longer crashes the run summary by @DietrichGebert in https://github.com/DietrichGebert/ponytail/pull/1110
> * docs: manual Hermes install until Hermes fixes its plugin.json check by @DietrichGebert in https://github.com/DietrichGebert/ponytail/pull/1111
> * feat(pi-extension): autocomplete /ponytail arguments by @ruttybob in https://github.com/DietrichGebert/ponytail/pull/1080
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-10-29 | [docs: add PhotoReunion to Already built with Ponytail (#1313)](https://github.com/DietrichGebert/ponytail/commit/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846) | DietrichGebert |
| 2026-10-29 | [chore: release v5.3.3 (#1307)](https://github.com/DietrichGebert/ponytail/commit/7801d061243d7b753bad0e0b3c057cd250b11755) | DietrichGebert |
| 2026-10-29 | [fix(band): drop the duplicate? hint, count only project files, tighte…](https://github.com/DietrichGebert/ponytail/commit/a3edb0ec9d44473f814d9b0e435b80e3cbb138df) | DietrichGebert |
| 2026-10-29 | [fix(band): size the row to bodyColumns only in the terminal (#1302)](https://github.com/DietrichGebert/ponytail/commit/172222eb88b6e7681674431e62a07224e1fc7fcd) | lelmarir |
| 2026-10-29 | [fix(band): watch only /clear, /resume and /branch, so other plugins' …](https://github.com/DietrichGebert/ponytail/commit/134b8e1a3a8078302b8ba77f86626c0802b2a6db) | ph3on1x |
| 2026-10-29 | [fix(band): find the transcript without a classic hook (#1242)](https://github.com/DietrichGebert/ponytail/commit/6309875aa27a788030b8e3f43e29a1342a6370ee) | trhinehart-attentive |
| 2026-10-18 | [fix(bench): wait for the killed todo server before the workdir cleanu…](https://github.com/DietrichGebert/ponytail/commit/09c434ab73ca43761c5d8b0c5d341926c2fba710) | devohmycode |
| 2026-10-18 | [fix(hooks): give the codebase map 3 s so a slow Windows start keeps i…](https://github.com/DietrichGebert/ponytail/commit/5117d0ef09e9fc040093d8d54182d8e28d3201b9) | DietrichGebert |
| 2026-10-18 | [fix(hooks): 15 s hook timeout so a slow node start on Windows keeps i…](https://github.com/DietrichGebert/ponytail/commit/5a5a605fb1292a93095e9b8fcd5a7866f2fcc637) | DietrichGebert |
| 2026-10-18 | [fix(codex): small composer icon instead of the 554 KB logo (#1164)](https://github.com/DietrichGebert/ponytail/commit/629158d41d1f1e2a65c06abe0a3d58bf76ad2745) | DietrichGebert |

[See all commits ↗](https://github.com/DietrichGebert/ponytail/commits)

## ⬇️ Get it

```bash
git clone https://github.com/DietrichGebert/ponytail.git
```
