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
| 🐞 **Open issues + PRs** | [59](https://github.com/assistant-ui/assistant-ui/issues) |
| 💻 **Languages** | TypeScript 84% · MDX 10% · JavaScript 3% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `conversational-ai` `radix-ui` `shadcn` `ui-components` `copilot` `chatbot` `vercel-ai-sdk` `ai-chatbot` `react-chatbot` `base-ui` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2023-11-22 |
| 📦 **Latest release** | [@assistant-ui/core@0.3.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/core%400.3.37) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 205.7 MB |
| 🌐 **Website** | https://www.assistant-ui.com |

## 📦 Recent releases

### [@assistant-ui/core@0.3.37](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/core%400.3.37)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - [#10593](https://github.com/assistant-ui/assistant-ui/pull/10593) [`528bfe9`](https://github.com/assistant-ui/assistant-ui/commit/528bfe964f1306f7070fd4efe034873b5f1cfe45) - `MessageRepository.import` now leaves the repository unchanged when it throws, for example when a message's parent or the head is missing. Thread `import` and `reset`, and loading history in the local runtime, check the data before clearing the current messages, so a history that cannot be placed no longer empties the thread. ([@Yonom](https://github.com/Yonom))
> - [#10597](https://github.com/assistant-ui/assistant-ui/pull/10597) [`f1a812d`](https://github.com/assistant-ui/assistant-ui/commit/f1a812d2d1a6c824ea397d798a9b158f750b7804) - never run a frontend tool's `execute` for a tool call the backend owns. Tool-call parts gain `providerExecuted`: the tool invocation tracker, `ToolExecutionStream` and `unstable_runPendingTools` skip a call that carries it, even when the run ends before the backend's result arrives. UI message streams set it for provider-executed calls, the data stream format carries it from `addToolCallPart({ providerExecuted: true })` to the client, and `@assistant-ui/ai-sdk` sets it from the AI SDK part's `providerExecuted`. A dynamic tool call is marked only when its part carries `providerExecuted: true`, so otherwise it stays client-runnable as it is in the AI SDK. `@assistant-ui/react-langchain` holds a call while the graph is paused on an interrupt, and `@assistant-ui/eve` never hands a call to a frontend tool. ([@Yonom](https://github.com/Yonom))
> - [#10641](https://github.com/assistant-ui/assistant-ui/pull/10641) [`8f30cfc`](https://github.com/assistant-ui/assistant-ui/commit/8f30cfc76b6e1483cc390a293eafc4d8fffb2bcd) - Keep Cloud message ID mappings available when a thread history moves from its live item to the listed item, so edits to loaded messages reach Cloud. ([@rupic-app](https://github.com/apps/rupic-app))
> - [#10601](https://github.com/assistant-ui/assistant-ui/pull/10601) [`11afc02`](https://github.com/assistant-ui/assistant-ui/commit/11afc0276e87cc0834342d6fdeeaaf0595fccdbe) - fix(cloud): loading a thread follows `has_more` from the message list, so a page that ends before its limit no longer ends the thread early ([@Yonom](https://github.com/Yonom))
> - [#10666](https://github.com/assistant-ui/assistant-ui/pull/10666) [`d9a7f68`](https://github.com/assistant-ui/assistant-ui/commit/d9a7f68b5a38fcc3f68b5acf127f71dd5b8a6837) - keep how a dictation session ended. Composer state gains `lastDictationEnd` (`{ reason, error?: AssistantError }`), set when a session ends and cleared before the next adapter listen attempt, so a UI can explain a failed dictation after `dictation` returns to `undefined`. The ended `DictationAdapter.Status` gains `error?: unknown`, which the composer normalizes to `AssistantError`, and `WebSpeechDictationAdapter` fills it with the browser's `{ code, message }` (for example `not-allowed` for a blocked microphone). `DictationEnd` is exported. ([@vidiyala99](https://github.com/vidiyala99))
> …

### [@assistant-ui/x-generative-compiler@0.0.22](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/x-generative-compiler%400.0.22)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - [#10709](https://github.com/assistant-ui/assistant-ui/pull/10709) [`08aa6f1`](https://github.com/assistant-ui/assistant-ui/commit/08aa6f1e19dc5228546cbc6878d6de510f0cd19e) - fix: drop module bindings that only a stripped region used, whatever their initializer, so calls and constructors such as `createDb(...)` or `new PrismaClient(...)` that only a backend `execute` needed no longer stay in the client build. A file whose `"use generative"` directive is not its first statement now fails the build instead of shipping uncompiled, and `withAui` runs the loader on every JS/TS extension, including `.mts` and `.cts`. ([@Yonom](https://github.com/Yonom))

### [@assistant-ui/vue@0.0.8](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/vue%400.0.8)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - [#10656](https://github.com/assistant-ui/assistant-ui/pull/10656) [`cba4061`](https://github.com/assistant-ui/assistant-ui/commit/cba406112b09de49e99764b51a9d90a8ca952cc7) - keep the viewport footer inset accurate as content grows and its top margin changes. ([@okisdev](https://github.com/okisdev))
> - [#10655](https://github.com/assistant-ui/assistant-ui/pull/10655) [`d694a8b`](https://github.com/assistant-ui/assistant-ui/commit/d694a8b638fe1ba59466a25b19aebcbfcaf5325f) - `useScrollLock` holds its position on containers with `scroll-behavior: smooth` and when the page itself is the scroller. ([@okisdev](https://github.com/okisdev))
> - [#10649](https://github.com/assistant-ui/assistant-ui/pull/10649) [`8b606de`](https://github.com/assistant-ui/assistant-ui/commit/8b606de5b53572fb3da8be799f7324031b885524) - share composition, attachment key, and message id helpers across bindings without changing their behavior. ([@okisdev](https://github.com/okisdev))
> - [#10654](https://github.com/assistant-ui/assistant-ui/pull/10654) [`415db3a`](https://github.com/assistant-ui/assistant-ui/commit/415db3acc68cb9413205d8b26f9232ea472aef07) - destroy vue and svelte provider clients on unmount so scopes and active streams stop immediately. ([@okisdev](https://github.com/okisdev))
> - [#10668](https://github.com/assistant-ui/assistant-ui/pull/10668) [`f88a093`](https://github.com/assistant-ui/assistant-ui/commit/f88a093ec9b79a2137092e6d22ec51d7feb02f64) - Escape now stops speech only in the Vue thread it is pressed in, and an Escape that ends an IME composition no longer stops speech. ([@okisdev](https://github.com/okisdev))
> …

### [@assistant-ui/vite@0.0.22](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/vite%400.0.22)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - Updated dependencies [[`08aa6f1`](https://github.com/assistant-ui/assistant-ui/commit/08aa6f1e19dc5228546cbc6878d6de510f0cd19e)]:
>   - @assistant-ui/x-generative-compiler@0.0.22

### [@assistant-ui/variants@0.0.5](https://github.com/assistant-ui/assistant-ui/releases/tag/%40assistant-ui/variants%400.0.5)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - [#10604](https://github.com/assistant-ui/assistant-ui/pull/10604) [`9c7de04`](https://github.com/assistant-ui/assistant-ui/commit/9c7de0413212819811d38af4a30944e9611859d1) - fix: the Next.js route handlers now check the client address like the Vite plugin, and refuse requests whose address is unknown unless `allowRemoteClients` is set. ([@Yonom](https://github.com/Yonom))

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(adapters): forward core's store and tap peers (#10704)](https://github.com/assistant-ui/assistant-ui/commit/03c06506107f55a7bc11bed616a2fed06af8a8ba) | okisdev |
| 2026-11-18 | [fix(core): runtime extras expose useExtras so the React Compiler sees…](https://github.com/assistant-ui/assistant-ui/commit/ac873e5d3aded57180cbb8f2ec17fa109db6e4cd) | okisdev |
| 2026-11-18 | [fix(ui): media, attachment swatches and source favicons load remote u…](https://github.com/assistant-ui/assistant-ui/commit/152efcfe7601325ab9b7fa1dec41e5c6c768d1b3) | Yonom |
| 2026-11-18 | [perf(assistant-stream): many-part streams decode with less merge over…](https://github.com/assistant-ui/assistant-ui/commit/709a0cc74b14b6196b9e9466ecac58b502ae70e5) | Yonom |
| 2026-11-18 | [fix(react-langchain): preserve prior tool outputs on edit (#10688)](https://github.com/assistant-ui/assistant-ui/commit/bf541446c512dde599b7f36151c9b35e0453fadf) | rupic-app[bot] |
| 2026-11-18 | [fix(examples): guard remaining model routes from cross-site requests …](https://github.com/assistant-ui/assistant-ui/commit/18e5b35458d87956c4859a235eb0cdce5f1e8c6b) | rupic-app[bot] |
| 2026-11-18 | [fix(remote-components): limit dev CORS and closed-policy image/media …](https://github.com/assistant-ui/assistant-ui/commit/5cdc7a3266708e4718071551590f642a7a77846c) | Yonom |
| 2026-11-18 | [ci(python): python CI runs PostgreSQL thread-store cases (#10648)](https://github.com/assistant-ui/assistant-ui/commit/af4f279dc6fa04c581c80cf99ae41fd47476c62d) | egg119 |
| 2026-11-18 | [fix: disabled frontend tools no longer run, and set_form_field only s…](https://github.com/assistant-ui/assistant-ui/commit/9906ce658c309e57b138c5232f2fb1b09cdb55f8) | Yonom |
| 2026-11-18 | [fix(release): waits up to 15 minutes for npm versions before tagging …](https://github.com/assistant-ui/assistant-ui/commit/11afc90119d4ebe2d569e8ae6ddce2e81bc4401b) | Kinfe123 |

[See all commits ↗](https://github.com/assistant-ui/assistant-ui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/assistant-ui/assistant-ui.git
```
