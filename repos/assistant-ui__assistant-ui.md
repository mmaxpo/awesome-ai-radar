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
| 🐞 **Open issues + PRs** | [35](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [@assistant-ui/core@0.3.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/core%400.3.37) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 208.4 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [@assistant-ui/core@0.3.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/core%400.3.37)
<sub>2026-11-18 · 4d ago</sub>

> **Patch Changes**
> - [#10593](https://github.com/assistant-ui/assistant-ui/pull/10593) [`528bfe9`](https://github.com/assistant-ui/assistant-ui/commit/528bfe964f1306f7070fd4efe034873b5f1cfe45) - `MessageRepository.import` now leaves the repository unchanged when it throws, for example when a message's parent or the head is missing. Thread `import` and `reset`, and loading history in the local runtime, check the data before clearing the current messages, so a history that cannot be placed no longer empties the thread. ([@Yonom](https://github.com/Yonom))
> - [#10597](https://github.com/assistant-ui/assistant-ui/pull/10597) [`f1a812d`](https://github.com/assistant-ui/assistant-ui/commit/f1a812d2d1a6c824ea397d798a9b158f750b7804) - never run a frontend tool's `execute` for a tool call the backend owns. Tool-call parts gain `providerExecuted`: the tool invocation tracker, `ToolExecutionStream` and `unstable_runPendingTools` skip a call that carries it, even when the run ends before the backend's result arrives. UI message streams set it for provider-executed calls, the data stream format carries it from `addToolCallPart({ providerExecuted: true })` to the client, and `@assistant-ui/ai-sdk` sets it from the AI SDK part's `providerExecuted`. A dynamic tool call is marked only when its part carries `providerExecuted: true`, so otherwise it stays client-runnable as it is in the AI SDK. `@assistant-ui/react-langchain` holds a call while the graph is paused on an interrupt, and `@assistant-ui/eve` never hands a call to a frontend tool. ([@Yonom](https://github.com/Yonom))
> - [#10641](https://github.com/assistant-ui/assistant-ui/pull/10641) [`8f30cfc`](https://github.com/assistant-ui/assistant-ui/commit/8f30cfc76b6e1483cc390a293eafc4d8fffb2bcd) - Keep Cloud message ID mappings available when a thread history moves from its live item to the listed item, so edits to loaded messages reach Cloud. ([@rupic-app](https://github.com/apps/rupic-app))
> - [#10601](https://github.com/assistant-ui/assistant-ui/pull/10601) [`11afc02`](https://github.com/assistant-ui/assistant-ui/commit/11afc0276e87cc0834342d6fdeeaaf0595fccdbe) - fix(cloud): loading a thread follows `has_more` from the message list, so a page that ends before its limit no longer ends the thread early ([@Yonom](https://github.com/Yonom))
> - [#10666](https://github.com/assistant-ui/assistant-ui/pull/10666) [`d9a7f68`](https://github.com/assistant-ui/assistant-ui/commit/d9a7f68b5a38fcc3f68b5acf127f71dd5b8a6837) - keep how a dictation session ended. Composer state gains `lastDictationEnd` (`{ reason, error?: AssistantError }`), set when a session ends and cleared before the next adapter listen attempt, so a UI can explain a failed dictation after `dictation` returns to `undefined`. The ended `DictationAdapter.Status` gains `error?: unknown`, which the composer normalizes to `AssistantError`, and `WebSpeechDictationAdapter` fills it with the browser's `{ code, message }` (for example `not-allowed` for a blocked microphone). `DictationEnd` is exported. ([@vidiyala99](https://github.com/vidiyala99))
> …

### [@assistant-ui/x-generative-compiler@0.0.22](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/x-generative-compiler%400.0.22)
<sub>2026-11-18 · 4d ago</sub>

> **Patch Changes**
> - [#10709](https://github.com/assistant-ui/assistant-ui/pull/10709) [`08aa6f1`](https://github.com/assistant-ui/assistant-ui/commit/08aa6f1e19dc5228546cbc6878d6de510f0cd19e) - fix: drop module bindings that only a stripped region used, whatever their initializer, so calls and constructors such as `createDb(...)` or `new PrismaClient(...)` that only a backend `execute` needed no longer stay in the client build. A file whose `"use generative"` directive is not its first statement now fails the build instead of shipping uncompiled, and `withAui` runs the loader on every JS/TS extension, including `.mts` and `.cts`. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/vue@0.0.8](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/vue%400.0.8)
<sub>2026-11-18 · 4d ago</sub>

> **Patch Changes**
> - [#10656](https://github.com/assistant-ui/assistant-ui/pull/10656) [`cba4061`](https://github.com/assistant-ui/assistant-ui/commit/cba406112b09de49e99764b51a9d90a8ca952cc7) - keep the viewport footer inset accurate as content grows and its top margin changes. ([@okisdev](https://github.com/okisdev))
> - [#10655](https://github.com/assistant-ui/assistant-ui/pull/10655) [`d694a8b`](https://github.com/assistant-ui/assistant-ui/commit/d694a8b638fe1ba59466a25b19aebcbfcaf5325f) - `useScrollLock` holds its position on containers with `scroll-behavior: smooth` and when the page itself is the scroller. ([@okisdev](https://github.com/okisdev))
> - [#10649](https://github.com/assistant-ui/assistant-ui/pull/10649) [`8b606de`](https://github.com/assistant-ui/assistant-ui/commit/8b606de5b53572fb3da8be799f7324031b885524) - share composition, attachment key, and message id helpers across bindings without changing their behavior. ([@okisdev](https://github.com/okisdev))
> - [#10654](https://github.com/assistant-ui/assistant-ui/pull/10654) [`415db3a`](https://github.com/assistant-ui/assistant-ui/commit/415db3acc68cb9413205d8b26f9232ea472aef07) - destroy vue and svelte provider clients on unmount so scopes and active streams stop immediately. ([@okisdev](https://github.com/okisdev))
> - [#10668](https://github.com/assistant-ui/assistant-ui/pull/10668) [`f88a093`](https://github.com/assistant-ui/assistant-ui/commit/f88a093ec9b79a2137092e6d22ec51d7feb02f64) - Escape now stops speech only in the Vue thread it is pressed in, and an Escape that ends an IME composition no longer stops speech. ([@okisdev](https://github.com/okisdev))
> …

### [@assistant-ui/vite@0.0.22](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/vite%400.0.22)
<sub>2026-11-18 · 4d ago</sub>

> **Patch Changes**
> - Updated dependencies [[`08aa6f1`](https://github.com/assistant-ui/assistant-ui/commit/08aa6f1e19dc5228546cbc6878d6de510f0cd19e)]:
>   - @assistant-ui/x-generative-compiler@0.0.22

### [@assistant-ui/variants@0.0.5](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/variants%400.0.5)
<sub>2026-11-18 · 4d ago</sub>

> **Patch Changes**
> - [#10604](https://github.com/assistant-ui/assistant-ui/pull/10604) [`9c7de04`](https://github.com/assistant-ui/assistant-ui/commit/9c7de0413212819811d38af4a30944e9611859d1) - fix: the Next.js route handlers now check the client address like the Vite plugin, and refuse requests whose address is unknown unless `allowRemoteClients` is set. ([@Yonom](https://github.com/Yonom))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [fix(docs-theme): supports Farming Labs 0.2.x peers from 0.2.141 (#10720)](https://github.com/assistant-ui/assistant-ui/commit/810fa6256ed52d31b7fc11e2fe55301e66bbc00b) | Kinfe123 |
| 2026-11-22 | [fix(deps): update vite to 8.3.8 (#10786)](https://github.com/assistant-ui/assistant-ui/commit/09540e57cab69ad754c4341c48fe1b85ea199dfe) | Kinfe123 |
| 2026-11-22 | [fix(docs): make design tokens follow the design guide (#10783)](https://github.com/assistant-ui/assistant-ui/commit/75283e18d212b886ba4b490b02ba3bab87b5499c) | Kinfe123 |
| 2026-11-21 | [fix(deps): update @hono/node-server to 2.1.11 (#10779)](https://github.com/assistant-ui/assistant-ui/commit/93b04aa47612a448044b9feb725031467fe6fd08) | aui-sec[bot] |
| 2026-11-21 | [fix(deps): update react-router and zod (#10765)](https://github.com/assistant-ui/assistant-ui/commit/3b848877bd631bea0f652971a7a0300ed595218c) | aui-sec[bot] |
| 2026-11-20 | [feat(store): warn in development on the deprecated useAui({ ... }) ov…](https://github.com/assistant-ui/assistant-ui/commit/e1efac0c22e9799f3d0e0422dc6abdbe8c1c5c09) | Yonom |
| 2026-11-20 | [docs(pricing): divider rules have square ends (#10774)](https://github.com/assistant-ui/assistant-ui/commit/f3b24f5a6782a22f2fea8897e7ce87c76fe4facf) | Kinfe123 |
| 2026-11-20 | [docs(mcp): send server instructions and describe preview config roots…](https://github.com/assistant-ui/assistant-ui/commit/3314276279f6515ae6ec4bbf6cf241fb2eaeb5bc) | Yonom |
| 2026-11-20 | [ci: review tier gives an archive outside every area T3 (#10771)](https://github.com/assistant-ui/assistant-ui/commit/67ca14d9106a09f48dfa54eae0b0999fa899ac99) | okisdev |
| 2026-11-20 | [fix(core): hosted runtime hooks pick up edits on fast refresh (#10769)](https://github.com/assistant-ui/assistant-ui/commit/3c1497d5ed2b4821a8f2007cc0aa8361e58b24d6) | okisdev |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
