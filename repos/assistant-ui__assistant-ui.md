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
| ⭐ **Stars** | 13.4k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [36](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 220.8 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3)
<sub>2026-11-24 · yesterday</sub>

> **Patch Changes**
> - [#10801](https://github.com/assistant-ui/assistant-ui/pull/10801) [`4a0d2a5`](https://github.com/assistant-ui/assistant-ui/commit/4a0d2a5b9f04c8fb7ff9cd224827a958096b52dc) - A setup whose coding agent's stream has been gone for an hour while its setup page stayed awake (the agent stopped it, or its machine or sandbox went away) now ends as cancelled, with a note to run setup again, instead of staying half-finished. A sleep that silences both the page and the agent does not end it. ([@Yonom](https://github.com/Yonom))
> - [#10798](https://github.com/assistant-ui/assistant-ui/pull/10798) [`f91eb36`](https://github.com/assistant-ui/assistant-ui/commit/f91eb36ee688059c9eed90cc85b223f7bb035c11) - The guide a setup reads now has a `stream.unattended` text, and `loadGuide` sends `unattended=1` when its caller passes `unattended: true`. ([@Yonom](https://github.com/Yonom))
> - [#10797](https://github.com/assistant-ui/assistant-ui/pull/10797) [`a926a19`](https://github.com/assistant-ui/assistant-ui/commit/a926a19a80d1220925b36628f1a62614a7c767f9) - `setup` run by a coding agent now opens with what it is, which way to go (give the user the setup page link, or rerun with `--unattended` when nobody will answer), and how to stop it (`setup <url> cancel`). `--unattended` has the agent decide each choice and finish on its own. Over SSH without a forwarded display, in CI, or on a Linux or BSD machine with no display, setup opens no browser unless `BROWSER` or `SETUP_AGENT_BROWSER` names one. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-opencode@0.2.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-opencode%400.2.37)
<sub>2026-11-24 · yesterday</sub>

> **Patch Changes**
> - [#10781](https://github.com/assistant-ui/assistant-ui/pull/10781) [`361e21c`](https://github.com/assistant-ui/assistant-ui/commit/361e21c652878437291df8d0665620a8aeeb36f7) - An assistant message the user stops now ends as cancelled instead of failing with an "Aborted" error, so stopping a run no longer shows an error message. ([@micheal0034](https://github.com/micheal0034))

### [@assistant-ui/react-ink-markdown@0.0.57](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink-markdown%400.0.57)
<sub>2026-11-24 · yesterday</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))
> - Updated dependencies [[`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5)]:
>   - @assistant-ui/react-ink@0.0.56

### [@assistant-ui/react-ink@0.0.56](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink%400.0.56)
<sub>2026-11-24 · yesterday</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-generative-ui@0.1.12](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-generative-ui%400.1.12)
<sub>2026-11-24 · yesterday</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - @assistant-ui/generative-ui@0.0.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [feat(library): add an app that lists every installable with its insta…](https://github.com/assistant-ui/assistant-ui/commit/4797ce5da22845dfa0c0d2cbd115f8e6fe42d2a2) | aiellie |
| 2026-11-25 | [feat(docs): show element badges under a reworked block viewer (#10839)](https://github.com/assistant-ui/assistant-ui/commit/c0d52411c133fca73ceeedc640cdaa41ee86a576) | aiellie |
| 2026-11-25 | [fix(ui): load remote images in markdown, link previews and galleries …](https://github.com/assistant-ui/assistant-ui/commit/52048962324eb74bb27654277123361125e0e6b4) | Yonom |
| 2026-11-25 | [feat(docs): add an Images block to the Blocks pages (#10838)](https://github.com/assistant-ui/assistant-ui/commit/156f2562866303b6bad3218eb32461db96c08dcc) | aiellie |
| 2026-11-25 | [fix(deps): update @vue/shared and unhead (#10857)](https://github.com/assistant-ui/assistant-ui/commit/c4674af60846e1f26d56dfae9852b3b04e4f087e) | aui-sec[bot] |
| 2026-11-25 | [fix(core): keep an open tool group open when reasoning lands ahead of…](https://github.com/assistant-ui/assistant-ui/commit/db46e0b306e19e6af0567fdbcb2364368c0acc75) | samdickson22 |
| 2026-11-25 | [ci(checkout-worker): explain how to recover from a failed deploy (#10…](https://github.com/assistant-ui/assistant-ui/commit/85bb2ae48ae926e0ceb96b2252a3415ee4ab78b7) | Kinfe123 |
| 2026-11-25 | [ci(ag-ui): runs server tests on example changes (#10770)](https://github.com/assistant-ui/assistant-ui/commit/669e01c519a7493bf762a6ea3d6cd26c39f511a7) | lhy-dcf |
| 2026-11-25 | [docs: add PowerShell setup for AG-UI example (#10837)](https://github.com/assistant-ui/assistant-ui/commit/bdb8911526c1cd98375a400bb19e57655096ad96) | terminalchai |
| 2026-11-25 | [ci(release): log the request id and git push reason when GitHub refus…](https://github.com/assistant-ui/assistant-ui/commit/09a1a36bb4d950d6cf5ffb6487fea730cf5fa1ae) | Kinfe123 |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
