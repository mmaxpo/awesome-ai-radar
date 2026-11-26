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
| 🐞 **Open issues + PRs** | [61](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 231.8 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [setup-agent@0.2.3](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.3)
<sub>2026-11-24 · 2d ago</sub>

> **Patch Changes**
> - [#10801](https://github.com/assistant-ui/assistant-ui/pull/10801) [`4a0d2a5`](https://github.com/assistant-ui/assistant-ui/commit/4a0d2a5b9f04c8fb7ff9cd224827a958096b52dc) - A setup whose coding agent's stream has been gone for an hour while its setup page stayed awake (the agent stopped it, or its machine or sandbox went away) now ends as cancelled, with a note to run setup again, instead of staying half-finished. A sleep that silences both the page and the agent does not end it. ([@Yonom](https://github.com/Yonom))
> - [#10798](https://github.com/assistant-ui/assistant-ui/pull/10798) [`f91eb36`](https://github.com/assistant-ui/assistant-ui/commit/f91eb36ee688059c9eed90cc85b223f7bb035c11) - The guide a setup reads now has a `stream.unattended` text, and `loadGuide` sends `unattended=1` when its caller passes `unattended: true`. ([@Yonom](https://github.com/Yonom))
> - [#10797](https://github.com/assistant-ui/assistant-ui/pull/10797) [`a926a19`](https://github.com/assistant-ui/assistant-ui/commit/a926a19a80d1220925b36628f1a62614a7c767f9) - `setup` run by a coding agent now opens with what it is, which way to go (give the user the setup page link, or rerun with `--unattended` when nobody will answer), and how to stop it (`setup <url> cancel`). `--unattended` has the agent decide each choice and finish on its own. Over SSH without a forwarded display, in CI, or on a Linux or BSD machine with no display, setup opens no browser unless `BROWSER` or `SETUP_AGENT_BROWSER` names one. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-opencode@0.2.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-opencode%400.2.37)
<sub>2026-11-24 · 2d ago</sub>

> **Patch Changes**
> - [#10781](https://github.com/assistant-ui/assistant-ui/pull/10781) [`361e21c`](https://github.com/assistant-ui/assistant-ui/commit/361e21c652878437291df8d0665620a8aeeb36f7) - An assistant message the user stops now ends as cancelled instead of failing with an "Aborted" error, so stopping a run no longer shows an error message. ([@micheal0034](https://github.com/micheal0034))

### [@assistant-ui/react-ink-markdown@0.0.57](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink-markdown%400.0.57)
<sub>2026-11-24 · 2d ago</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))
> - Updated dependencies [[`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5)]:
>   - @assistant-ui/react-ink@0.0.56

### [@assistant-ui/react-ink@0.0.56](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-ink%400.0.56)
<sub>2026-11-24 · 2d ago</sub>

> **Patch Changes**
> - [#10609](https://github.com/assistant-ui/assistant-ui/pull/10609) [`7a89603`](https://github.com/assistant-ui/assistant-ui/commit/7a89603ccf7ab5e36c0a91fac49bb1818ca5b8d5) - fix: an unterminated OSC, DCS, SOS, PM or APC sequence now ends at its line, so the text on the following lines still shows. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/react-generative-ui@0.1.12](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/react-generative-ui%400.1.12)
<sub>2026-11-24 · 2d ago</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - @assistant-ui/generative-ui@0.0.13

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [docs(search): finds code-only API names in questions (#10920)](https://github.com/assistant-ui/assistant-ui/commit/18575028b385ea20866aa0514aa55f0cf3361eef) | Yonom |
| 2026-11-26 | [fix(docs): agent markdown preserves diagrams, demos and source (#10918)](https://github.com/assistant-ui/assistant-ui/commit/186aa2c877325fbe1b5490caef99ceb22cabd234) | Yonom |
| 2026-11-26 | [fix(docs): serves modern MCP clients and useful markdown pages (#10914)](https://github.com/assistant-ui/assistant-ui/commit/194f736adc45f927c5290f596e1e3179b35156f0) | Yonom |
| 2026-11-26 | [docs(search): finds word forms, code symbols and questions (#10919)](https://github.com/assistant-ui/assistant-ui/commit/8bc7301965691d1c9c97fbac84fb7e742eccfb6f) | Yonom |
| 2026-11-26 | [test(docs): reject new TypeScript sample errors in CI (#10908)](https://github.com/assistant-ui/assistant-ui/commit/2c81ff46ddcb078e24bb3f61de9a2e92f1680a0d) | Yonom |
| 2026-11-26 | [perf(docs): docs pages carry less shared weight (#10910)](https://github.com/assistant-ui/assistant-ui/commit/d61d42011bade7c3de4806ab74aefccfc3114a09) | Yonom |
| 2026-11-26 | [docs(docs-site): concept guides run live demos and track use (#10907)](https://github.com/assistant-ui/assistant-ui/commit/331104d209d493086746a695db2538a551fc9ae9) | Yonom |
| 2026-11-26 | [docs(guides): explains chat styling and themes (#10911)](https://github.com/assistant-ui/assistant-ui/commit/ef0cb8e59351e37ef75b9ebd39c302b47dd59d7f) | Yonom |
| 2026-11-26 | [docs: explain signed approvals and find more pages (#10905)](https://github.com/assistant-ui/assistant-ui/commit/ad93855ea43ec529d8f96585d59af3f6a3f99daf) | Yonom |
| 2026-11-26 | [fix(docs): keeps docs chat scoped and answers every turn (#10909)](https://github.com/assistant-ui/assistant-ui/commit/4d9303a743e403ef4ca392a6feb17f19ccfb5afa) | Yonom |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
