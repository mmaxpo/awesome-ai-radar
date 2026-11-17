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
| 🐞 **Open issues + PRs** | [80](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 204.5 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [assistant-ui@0.0.135](https://github.com/assistant-ui/assistant-ui/releases/tag/assistant-ui%400.0.135)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - Updated dependencies [[`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da)]:
>   - setup-agent@0.2.0

### [setup-agent@0.2.0](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.2.0)
<sub>2026-11-13 · 3d ago</sub>

> **Minor Changes**
> - [#10566](https://github.com/assistant-ui/assistant-ui/pull/10566) [`4254c59`](https://github.com/assistant-ui/assistant-ui/commit/4254c59e520629b51f4278b9e93315fab40a30da) - Fetch the agent's instructions from the setup server. Commands that print guidance get the briefing, the stream's messages, the next-command hints and the relayed questions from `<setup-url>/guide`. A wording fix now ships with a server deploy instead of waiting for people to upgrade. Setup is online-only: without the guide a command fails with `Setup needs internet access to <url>`. The guide is data. The CLI strips control characters, fills placeholders itself, refuses redirects and guides over 256 KB, and runs only the `print`, `print-status` and `announce-agent` steps. ([@Yonom](https://github.com/Yonom))
>   Removed `agentInstructions`, `INSTRUCTIONS` and `AgentInstructionsOptions` from `setup-agent/cli`, since the text now lives on the server. `diffEvents` and `followSetup` take the guide.

### [create-assistant-ui@0.0.98](https://github.com/assistant-ui/assistant-ui/releases/tag/create-assistant-ui%400.0.98)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - Updated dependencies []:
>   - assistant-ui@0.0.135

### [setup-agent@0.1.2](https://github.com/assistant-ui/assistant-ui/releases/tag/setup-agent%400.1.2)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#10561](https://github.com/assistant-ui/assistant-ui/pull/10561) [`c9cc1b7`](https://github.com/assistant-ui/assistant-ui/commit/c9cc1b7d292eda5c2131de9e7c5b0d74a402426f) - Keep the coding agent working until the setup is done. The briefing and the stream's `browser.opened` and `input.needed` messages now tell the agent that nothing wakes it once it ends its turn, so it blocks on answers with `wait` instead of stopping to wait for the browser. `wait <input-id>`, `wait plan` and `--wait` return after 100 seconds with `{"ok":false,"status":"waiting","next":"<command>"}` so an agent shell's own time limit does not kill them; `--timeout <seconds>` sets another limit and `0` waits as long as it takes. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/x-buildutils@0.0.33](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/x-buildutils%400.0.33)
<sub>2026-11-13 · 3d ago</sub>

> **Patch Changes**
> - [#10544](https://github.com/assistant-ui/assistant-ui/pull/10544) [`7854908`](https://github.com/assistant-ui/assistant-ui/commit/7854908de003619397e9e30c578eb926246d2068) - Emit the declarations of ESM packages with the native TypeScript 7 compiler. In local measurements this about halved a cold build of every package in the repository. The emitted types are equivalent, though some unions, members and inferred types print differently. ([@Kinfe123](https://github.com/Kinfe123))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(core): edits to loaded messages are no longer dropped (#10641)](https://github.com/assistant-ui/assistant-ui/commit/8f30cfc76b6e1483cc390a293eafc4d8fffb2bcd) | rupic-app[bot] |
| 2026-11-17 | [docs: read dictation support through useSyncExternalStore (#10684)](https://github.com/assistant-ui/assistant-ui/commit/a4c705b08dbe04159c0a10f1cf9e737928d54c3c) | okisdev |
| 2026-11-17 | [fix(examples): guard the echo runtime's edit and reply timer (#10683)](https://github.com/assistant-ui/assistant-ui/commit/59d5e6d3612e9ccf8a85a51d3c91fa4df1f9ec2d) | okisdev |
| 2026-11-17 | [feat(examples): add with-solid-start (#10681)](https://github.com/assistant-ui/assistant-ui/commit/b3857d98ddb0fe72c1be0ef5955a895b79554517) | okisdev |
| 2026-11-17 | [feat(solid): render initial state on the server without mounting the …](https://github.com/assistant-ui/assistant-ui/commit/e62b16205db600e556db20ec10b6c53f4917dcbc) | okisdev |
| 2026-11-17 | [fix(examples): stop keeps the sent message when a draft exists (#10675)](https://github.com/assistant-ui/assistant-ui/commit/36b8ba970594c6d7bef9a4f1276aa938e720dad0) | okisdev |
| 2026-11-17 | [feat(solid): suggestion primitives (#10669)](https://github.com/assistant-ui/assistant-ui/commit/c6f486829a163b37778de32b5675ae5fa7804f4e) | okisdev |
| 2026-11-17 | [feat(examples): add with-solid (#10667)](https://github.com/assistant-ui/assistant-ui/commit/0d218c788f3f8511263851e45fb442789d21b512) | okisdev |
| 2026-11-17 | [feat(solid): attachment primitives (#10671)](https://github.com/assistant-ui/assistant-ui/commit/f1e0dc1d9a774d825b4cf16838aa08fb15a4ce22) | okisdev |
| 2026-11-17 | [feat(solid): error and chain of thought primitives (#10672)](https://github.com/assistant-ui/assistant-ui/commit/b33fbf124896e5c8343890036775dc8458ae8cb7) | okisdev |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
