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
| ⭐ **Stars** | 13.3k |
| 🍴 **Forks** | 1.3k |
| 🐞 **Open issues + PRs** | [66](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 204.1 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135)
<sub>2026-11-13 · 2d ago</sub>

> **Patch Changes**
> - Updated dependencies [[`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da)]:
>   - setup-agent@0.2.0

### [setup-agent@0.2.0](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.0)
<sub>2026-11-13 · 2d ago</sub>

> **Minor Changes**
> - [#10566](https://github.com/assistant-ui/assistant-ui/pull/10566) [`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da) - Fetch the agent's instructions from the setup server. Commands that print guidance get the briefing, the stream's messages, the next-command hints and the relayed questions from `<setup-url>/guide`. A wording fix now ships with a server deploy instead of waiting for people to upgrade. Setup is online-only: without the guide a command fails with `Setup needs internet access to <url>`. The guide is data. The CLI strips control characters, fills placeholders itself, refuses redirects and guides over 256 KB, and runs only the `print`, `print-status` and `announce-agent` steps. ([@Yonom](https://github.com/Yonom))
>   Removed `agentInstructions`, `INSTRUCTIONS` and `AgentInstructionsOptions` from `setup-agent/cli`, since the text now lives on the server. `diffEvents` and `followSetup` take the guide.

### [create-assistant-ui@0.0.98](https://github.com/assistant-ui/assistant-ui/releases/tag/create-assistant-ui%400.0.98)
<sub>2026-11-13 · 2d ago</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - assistant-ui@0.0.135

### [setup-agent@0.1.2](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.1.2)
<sub>2026-11-13 · 2d ago</sub>

> **Patch Changes**
> - [#10561](https://github.com/assistant-ui/assistant-ui/pull/10561) [`c9cc1b7`](https://github.com/assistant-ui/assistant-ui/commit/c9cc1b7d292eda5c2131de9e7c5b0d74a402426f) - Keep the coding agent working until the setup is done. The briefing and the stream's `browser.opened` and `input.needed` messages now tell the agent that nothing wakes it once it ends its turn, so it blocks on answers with `wait` instead of stopping to wait for the browser. `wait <input-id>`, `wait plan` and `--wait` return after 100 seconds with `{"ok":false,"status":"waiting","next":"<command>"}` so an agent shell's own time limit does not kill them; `--timeout <seconds>` sets another limit and `0` waits as long as it takes. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/x-buildutils@0.0.33](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/x-buildutils%400.0.33)
<sub>2026-11-13 · 2d ago</sub>

> **Patch Changes**
> - [#10544](https://github.com/assistant-ui/assistant-ui/pull/10544) [`7854908`](https://github.com/assistant-ui/assistant-ui/commit/7854908de003619397e9e30c578eb926246d2068) - Emit the declarations of ESM packages with the native TypeScript 7 compiler. In local measurements this about halved a cold build of every package in the repository. The emitted types are equivalent, though some unions, members and inferred types print differently. ([@Kinfe123](https://github.com/Kinfe123))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(core): keep in-flight thread list mutations across same-store ada…](https://github.com/assistant-ui/assistant-ui/commit/b43be2420a395ec193a01a8e85bf818c76a7cc90) | gentil93 |
| 2026-11-16 | [fix(assistant-stream): forward a data part's wire id to onData (#10574)](https://github.com/assistant-ui/assistant-ui/commit/7250300f918ab54bf53d92ef07de3e56ae81ac2e) | egg119 |
| 2026-11-16 | [fix(python): finalize producers cancelled before startup (#10557)](https://github.com/assistant-ui/assistant-ui/commit/c3de6c55a900b5c91b63d8a16685b4719a30d64b) | tarun5004 |
| 2026-11-16 | [fix(react,react-lexical): omit aria-expanded from trigger popover ARI…](https://github.com/assistant-ui/assistant-ui/commit/d156e7987ddf4aca65feb89df8d23f29d8b1bc63) | chuganzy |
| 2026-11-16 | [fix(core): tool calls a provider executes never run frontend execute …](https://github.com/assistant-ui/assistant-ui/commit/f1a812d2d1a6c824ea397d798a9b158f750b7804) | Yonom |
| 2026-11-16 | [fix(cloud): loading a thread follows has_more from the message list (…](https://github.com/assistant-ui/assistant-ui/commit/11afc0276e87cc0834342d6fdeeaaf0595fccdbe) | Yonom |
| 2026-11-16 | [fix(core): file and source parts with fields of the wrong type render…](https://github.com/assistant-ui/assistant-ui/commit/8c67589ca1b3ffac888c19e9a2759ee7c052ce4b) | Yonom |
| 2026-11-16 | [fix(python): each owner gets its own run stream (#10608)](https://github.com/assistant-ui/assistant-ui/commit/2ad1f7212f14cc5e33a9dd49a4e3f03a3619480d) | Yonom |
| 2026-11-16 | [fix(react-mcp): colliding MCP tool names register no tool (#10606)](https://github.com/assistant-ui/assistant-ui/commit/2e381de8ea8d3db63c672a42cc60706fde914bbf) | Yonom |
| 2026-11-16 | [fix(react-ag-ui): a tool call an interrupt names never runs its front…](https://github.com/assistant-ui/assistant-ui/commit/4e3eecb04602a735f629b58c1bc6d639ab5a3676) | Yonom |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
