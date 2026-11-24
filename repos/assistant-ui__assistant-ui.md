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
| 🐞 **Open issues + PRs** | [37](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 213.6 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3)
<sub>2026-11-24 · today</sub>

> **Patch Changes**
> - [#10801](https://github.com/assistant-ui/assistant-ui/pull/10801) [`4a0d2a5`](https://github.com/assistant-ui/assistant-ui/commit/4a0d2a5b9f04c8fb7ff9cd224827a958096b52dc) - A setup whose coding agent's stream has been gone for an hour while its setup page stayed awake (the agent stopped it, or its machine or sandbox went away) now ends as cancelled, with a note to run setup again, instead of staying half-finished. A sleep that silences both the page and the agent does not end it. ([@Yonom](https://github.com/Yonom))
> - [#10798](https://github.com/assistant-ui/assistant-ui/pull/10798) [`f91eb36`](https://github.com/assistant-ui/assistant-ui/commit/f91eb36ee688059c9eed90cc85b223f7bb035c11) - The guide a setup reads now has a `stream.unattended` text, and `loadGuide` sends `unattended=1` when its caller passes `unattended: true`. ([@Yonom](https://github.com/Yonom))
> - [#10797](https://github.com/assistant-ui/assistant-ui/pull/10797) [`a926a19`](https://github.com/assistant-ui/assistant-ui/commit/a926a19a80d1220925b36628f1a62614a7c767f9) - `setup` run by a coding agent now opens with what it is, which way to go (give the user the setup page link, or rerun with `--unattended` when nobody will answer), and how to stop it (`setup <url> cancel`). `--unattended` has the agent decide each choice and finish on its own. Over SSH without a forwarded display, in CI, or on a Linux or BSD machine with no display, setup opens no browser unless `BROWSER` or `SETUP_AGENT_BROWSER` names one. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-opencode@0.2.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-opencode%400.2.37)
<sub>2026-11-24 · today</sub>

> **Patch Changes**
> - [#10781](https://github.com/assistant-ui/assistant-ui/pull/10781) [`361e21c`](https://github.com/assistant-ui/assistant-ui/commit/361e21c652878437291df8d0665620a8aeeb36f7) - An assistant message the user stops now ends as cancelled instead of failing with an "Aborted" error, so stopping a run no longer shows an error message. ([@micheal0034](https://github.com/micheal0034))

### [@assistant-ui/react-ink-markdown@0.0.57](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink-markdown%400.0.57)
<sub>2026-11-24 · today</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))
> - Updated dependencies [[`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5)]:
>   - @assistant-ui/react-ink@0.0.56

### [@assistant-ui/react-ink@0.0.56](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink%400.0.56)
<sub>2026-11-24 · today</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-generative-ui@0.1.12](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-generative-ui%400.1.12)
<sub>2026-11-24 · today</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - @assistant-ui/generative-ui@0.0.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore(docs): install the appOS host from npm as @assistant-ui/appos (…](https://github.com/assistant-ui/assistant-ui/commit/49e98e1a0bc57c3ea521a6a6558c405f2bfa9253) | Yonom |
| 2026-11-24 | [fix(setup-agent): trust only real setup hosts and safe agent binaries…](https://github.com/assistant-ui/assistant-ui/commit/022d8f8972233d676ad1dd18a780b5a9c512b42b) | Yonom |
| 2026-11-24 | [ci: fix the with-expo deploy install (#10825)](https://github.com/assistant-ui/assistant-ui/commit/5cefd82e897cdecc2ed3e8f408e80a72db46cae3) | Yonom |
| 2026-11-24 | [fix(setup): ask before a key or sign-in goes to an agent (#10819)](https://github.com/assistant-ui/assistant-ui/commit/6fc894760dfff81b1c3ea49b95609f809b11a141) | Yonom |
| 2026-11-24 | [fix(setup-agent): a setup link holds one setup (#10817)](https://github.com/assistant-ui/assistant-ui/commit/1503639fd82dcdf12a1aa49134201e725e1c2557) | Yonom |
| 2026-11-24 | [ci: fix Vercel and Expo deploy installs after the appOS dependency (#…](https://github.com/assistant-ui/assistant-ui/commit/c90fbaca737e42e5ef996ef2c461a4caebc0670b) | Yonom |
| 2026-11-24 | [docs(examples): embeds article assistant on the examples page (#10777)](https://github.com/assistant-ui/assistant-ui/commit/c9f4998631ff71e41e9d8716eff07cc2303eda9f) | Yonom |
| 2026-11-24 | [ci(review): privileged PR reviews use validated relays (#10753)](https://github.com/assistant-ui/assistant-ui/commit/29b9a04e8fd0da64000fd1d2828f2f3ab8e28146) | Yonom |
| 2026-11-24 | [chore: update versions (#10794)](https://github.com/assistant-ui/assistant-ui/commit/8903f15e160cabaaf8c50348cb36edee7da25bee) | github-actions[bot] |
| 2026-11-24 | [ci: jobs use scoped secrets and verified build inputs (#10598)](https://github.com/assistant-ui/assistant-ui/commit/a748ba51d387aff4ad0acaf301ad7635b9732769) | Yonom |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
