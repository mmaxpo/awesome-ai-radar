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
| ⭐ **Stars** | 13.2k |
| 🍴 **Forks** | 1.3k |
| 🐞 **Open issues + PRs** | [54](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 11% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 200.4 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135)
<sub>2026-11-13 · today</sub>

> **Patch Changes**
> - Updated dependencies [[`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da)]:
>   - setup-agent@0.2.0

### [setup-agent@0.2.0](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.0)
<sub>2026-11-13 · today</sub>

> **Minor Changes**
> - [#10566](https://github.com/assistant-ui/assistant-ui/pull/10566) [`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da) - Fetch the agent's instructions from the setup server. Commands that print guidance get the briefing, the stream's messages, the next-command hints and the relayed questions from `<setup-url>/guide`. A wording fix now ships with a server deploy instead of waiting for people to upgrade. Setup is online-only: without the guide a command fails with `Setup needs internet access to <url>`. The guide is data. The CLI strips control characters, fills placeholders itself, refuses redirects and guides over 256 KB, and runs only the `print`, `print-status` and `announce-agent` steps. ([@Yonom](https://github.com/Yonom))
>   Removed `agentInstructions`, `INSTRUCTIONS` and `AgentInstructionsOptions` from `setup-agent/cli`, since the text now lives on the server. `diffEvents` and `followSetup` take the guide.

### [create-assistant-ui@0.0.98](https://github.com/assistant-ui/assistant-ui/releases/tag/create-assistant-ui%400.0.98)
<sub>2026-11-13 · today</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - assistant-ui@0.0.135

### [setup-agent@0.1.2](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.1.2)
<sub>2026-11-13 · today</sub>

> **Patch Changes**
> - [#10561](https://github.com/assistant-ui/assistant-ui/pull/10561) [`c9cc1b7`](https://github.com/assistant-ui/assistant-ui/commit/c9cc1b7d292eda5c2131de9e7c5b0d74a402426f) - Keep the coding agent working until the setup is done. The briefing and the stream's `browser.opened` and `input.needed` messages now tell the agent that nothing wakes it once it ends its turn, so it blocks on answers with `wait` instead of stopping to wait for the browser. `wait <input-id>`, `wait plan` and `--wait` return after 100 seconds with `{"ok":false,"status":"waiting","next":"<command>"}` so an agent shell's own time limit does not kill them; `--timeout <seconds>` sets another limit and `0` waits as long as it takes. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/x-buildutils@0.0.33](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/x-buildutils%400.0.33)
<sub>2026-11-13 · today</sub>

> **Patch Changes**
> - [#10544](https://github.com/assistant-ui/assistant-ui/pull/10544) [`7854908`](https://github.com/assistant-ui/assistant-ui/commit/7854908de003619397e9e30c578eb926246d2068) - Emit the declarations of ESM packages with the native TypeScript 7 compiler. In local measurements this about halved a cold build of every package in the repository. The emitted types are equivalent, though some unions, members and inferred types print differently. ([@Kinfe123](https://github.com/Kinfe123))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-13 | [chore: update versions (#10570)](https://github.com/assistant-ui/assistant-ui/commit/7d7427653f6ba47b0b954510eed9c594d64e74d5) | github-actions[bot] |
| 2026-11-13 | [feat(setup-agent)!: the agent's wording now comes from the setup serv…](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da) | Yonom |
| 2026-11-13 | [chore: update versions (#10564)](https://github.com/assistant-ui/assistant-ui/commit/27fa54dba55178d717a53252c4be5c95b319affa) | github-actions[bot] |
| 2026-11-13 | [feat(checkout-worker): new /<link>/guide route serves the CLI's texts…](https://github.com/assistant-ui/assistant-ui/commit/4aac7f8fa56bc13ce8fe7dbee74dd92bdbc76db6) | Yonom |
| 2026-11-13 | [chore(docs): setup leftovers removed (#10567)](https://github.com/assistant-ui/assistant-ui/commit/5074ccd621a11bfd557319615aea2c7758235fca) | Yonom |
| 2026-11-13 | [fix(setup-agent): the agent runs setup to the end; waits hand back ne…](https://github.com/assistant-ui/assistant-ui/commit/c9cc1b7d292eda5c2131de9e7c5b0d74a402426f) | Yonom |
| 2026-11-13 | [chore: update versions (#10518)](https://github.com/assistant-ui/assistant-ui/commit/0ee899e03d03056f82ab3e958e42b26c7dcf6d60) | github-actions[bot] |
| 2026-11-13 | [fix(react-ag-ui): resumeRun follows the run in flight; pair Assistant…](https://github.com/assistant-ui/assistant-ui/commit/b2311ec7a8a15533a20e3ff206653dd0f020ef8e) | Yonom |
| 2026-11-13 | [chore(python): assistant-stream 0.0.38 (#10563)](https://github.com/assistant-ui/assistant-ui/commit/48b5c8e244d4d7d335e5ac769ed1db2db0c946d4) | Yonom |
| 2026-11-13 | [feat(python): adapter factory, per-run context, SSE keepalive and cro…](https://github.com/assistant-ui/assistant-ui/commit/e22c12db36d2331158443e80489feab775f976de) | Yonom |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
