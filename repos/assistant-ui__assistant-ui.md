# assistant-ui/assistant-ui

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/assistant-ui/assistant-ui)

> Typescript/React Library for AI Chat 💬🚀

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | React chat UI for AI agents |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 13.5k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [53](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 233.7 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3)
<sub>2026-11-24 · 3d ago</sub>

> **Patch Changes**
> - [#10801](https://github.com/assistant-ui/assistant-ui/pull/10801) [`4a0d2a5`](https://github.com/assistant-ui/assistant-ui/commit/4a0d2a5b9f04c8fb7ff9cd224827a958096b52dc) - A setup whose coding agent's stream has been gone for an hour while its setup page stayed awake (the agent stopped it, or its machine or sandbox went away) now ends as cancelled, with a note to run setup again, instead of staying half-finished. A sleep that silences both the page and the agent does not end it. ([@Yonom](https://github.com/Yonom))
> - [#10798](https://github.com/assistant-ui/assistant-ui/pull/10798) [`f91eb36`](https://github.com/assistant-ui/assistant-ui/commit/f91eb36ee688059c9eed90cc85b223f7bb035c11) - The guide a setup reads now has a `stream.unattended` text, and `loadGuide` sends `unattended=1` when its caller passes `unattended: true`. ([@Yonom](https://github.com/Yonom))
> - [#10797](https://github.com/assistant-ui/assistant-ui/pull/10797) [`a926a19`](https://github.com/assistant-ui/assistant-ui/commit/a926a19a80d1220925b36628f1a62614a7c767f9) - `setup` run by a coding agent now opens with what it is, which way to go (give the user the setup page link, or rerun with `--unattended` when nobody will answer), and how to stop it (`setup <url> cancel`). `--unattended` has the agent decide each choice and finish on its own. Over SSH without a forwarded display, in CI, or on a Linux or BSD machine with no display, setup opens no browser unless `BROWSER` or `SETUP_AGENT_BROWSER` names one. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-opencode@0.2.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-opencode%400.2.37)
<sub>2026-11-24 · 3d ago</sub>

> **Patch Changes**
> - [#10781](https://github.com/assistant-ui/assistant-ui/pull/10781) [`361e21c`](https://github.com/assistant-ui/assistant-ui/commit/361e21c652878437291df8d0665620a8aeeb36f7) - An assistant message the user stops now ends as cancelled instead of failing with an "Aborted" error, so stopping a run no longer shows an error message. ([@micheal0034](https://github.com/micheal0034))

### [@assistant-ui/react-ink-markdown@0.0.57](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink-markdown%400.0.57)
<sub>2026-11-24 · 3d ago</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))
> - Updated dependencies [[`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5)]:
>   - @assistant-ui/react-ink@0.0.56

### [@assistant-ui/react-ink@0.0.56](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink%400.0.56)
<sub>2026-11-24 · 3d ago</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-generative-ui@0.1.12](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-generative-ui%400.1.12)
<sub>2026-11-24 · 3d ago</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - @assistant-ui/generative-ui@0.0.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [fix(docs): preserve paths and variants on markdown misses (#10955)](https://github.com/assistant-ui/assistant-ui/commit/98c2aa0873e5c03a2ea6936f71a882785f0f9b07) | okisdev |
| 2026-11-27 | [fix(core): keeps prepended history from settling in-transit sends (#1…](https://github.com/assistant-ui/assistant-ui/commit/b691d368a01c7874ff869a3e5e6d58557f3e88b6) | pratik340 |
| 2026-11-27 | [fix(core): external-store messages appear before paint (#10881)](https://github.com/assistant-ui/assistant-ui/commit/289119ed2019a0f83f698be867280c9ffd69d3ff) | Yonom |
| 2026-11-27 | [fix(docs): serves homepage and missing pages as markdown (#10870)](https://github.com/assistant-ui/assistant-ui/commit/6e3c1f12527816bfbf946ac8af8e3dcfa4f2f309) | Kinfe123 |
| 2026-11-27 | [ci: shared helper tests have one owner per event (#10871)](https://github.com/assistant-ui/assistant-ui/commit/f8ef927f38a50d82c987b8c5460491d774d824ce) | Kinfe123 |
| 2026-11-27 | [fix(ci): lazy imports count toward template footprints (#10930)](https://github.com/assistant-ui/assistant-ui/commit/5a25ad49ceeb465e62746bb4b375ce2c24342414) | Kinfe123 |
| 2026-11-27 | [ci(examples): skip durable tests for README-only edits (#10868)](https://github.com/assistant-ui/assistant-ui/commit/1af16a5f2e3083124c3463e62b4993d9c4b3217d) | Kinfe123 |
| 2026-11-27 | [perf(docs): reuses cached article appOS bundle (#10936)](https://github.com/assistant-ui/assistant-ui/commit/0574265e68cfdd425a05cce4ff14135054bae9c5) | Kinfe123 |
| 2026-11-27 | [fix(docs-theme): accepts compatible Farming Labs 0.2.x peers (#10793)](https://github.com/assistant-ui/assistant-ui/commit/390f5d40c10e1d17c6a8ea2bab453b466bf231ad) | Kinfe123 |
| 2026-11-27 | [ci(docs): preserve test caches when the root README changes (#10948)](https://github.com/assistant-ui/assistant-ui/commit/b4d2049008c625bbfa85ef4343e78f62b0db6065) | henrivalle |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
