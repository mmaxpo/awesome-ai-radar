# BuilderIO/agent-native

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/BuilderIO/agent-native)

> A framework for building agentic apps

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Apps that mix agent chat with traditional UI |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 7.8k |
| 🍴 **Forks** | 714 |
| 🐞 **Open issues + PRs** | [276](https://github.com/BuilderIO/agent-native/issues) |
| 💻 **Languages** | TypeScript 87% · MDX 10% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `react` `agent-native` `typescript` `agent-framework` `agentic-ai` `ai-agents` `framework` `generative-ui` `mcp` `open-source` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [@agent-native/core@0.232.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.232.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 620.1 MB |
| 🌐 **Website** | https://www.agent-native.com |

## 📦 Recent releases

### [clips-nightly-v0.1.534-0](https://github.com/BuilderIO/agent-native/releases/tag/clips-nightly-v0.1.534-0) — Clips Nightly v0.1.534-0 _(pre-release)_
<sub>2026-11-24 · today</sub>

> Auto-updating nightly build of the Clips menu-bar app.
> The in-app updater fetches its manifest from the `clips-nightly-latest`
> release — this versioned release is the immutable source of the
> signed bundles it downloads.

### [v0.1.150-nightly.461](https://github.com/BuilderIO/agent-native/releases/tag/v0.1.150-nightly.461) — Agent-Native Nightly v0.1.150-nightly.461 _(pre-release)_
<sub>2026-11-23 · today</sub>

> Auto-updating Nightly build of the Agent-Native desktop app.

### [@agent-native/core@0.232.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.232.0)
<sub>2026-11-23 · today</sub>

> **Minor Changes**
> - bf07e40: The agent's resource writes can now refuse to write over a newer save. An agent's resource read starts with a `[revision …, scope …]` line, and the `resources` write action, `write-resource` and `pnpm action resource-write --expected-revision` take that revision back: when someone saved the file after the read, nothing is written and the write fails with `save_conflict` and the revision there now. Writes report the new revision, and a write without one still replaces what's there. `POST /_agent-native/resources` returns the `revision` too, and with `ifNotExists` it now creates only where no file is, so of two creates at once the second gets the first one's file instead of writing over it, and a shared create in an organization gets the organization's file from before organizations instead of hiding it behind a new copy. `useCreateResource` accepts `ifNotExists`, and `resourcePutIfSnapshot` takes `visibility`, `threadId`, `runId` and `expiresAt`. Toolkit's personalization settings save their instructions over the version each edit started from, merging onto a newer save and asking which version to keep when both changed the text.
> - 089091b: Publish app capability manifests and standardize tab-scoped navigation. Enable realtime sync by default, acknowledge settled screens, and let embedded app frames handle view tools.
> - 41c2b0e: Add extension points a deployment can register its own policy through, with no change until something registers:
>   - `fetchWithProviderCallGate` (from `@agent-native/core/provider-api` and `@agent-native/core/provider-api/call-gates`) sends a request made with a package's own client through the registered provider call gates, so a gate refuses, debits or rate-limits it exactly as it would a provider-api request. `precheckProviderCall` takes the request URL when known, so a gate that claims requests by URL is prechecked too, and a caller that must precheck before its own work (such as a token refresh) calls `precheckGatedProviderCall`, which bounds the precheck by the same admission deadline (`ProviderCallGateAdmissionTimeoutError`), and passes the receipt as `prechecked` so it runs once. The scheduling Google Calendar provider sends every request through it as provider `google_calendar`, takes an optional `getAccountIdentity(credentialId)` that gates receive as the request's `accountId` (a lookup that misses the admission deadline arrives as `ProviderAccountLookupTimeoutError` in `accountIdError`), and an optional `appId` (default `"scheduling"`) that gates receive as the consuming app.
>   - `registerA2AActionCallHook` (from `@agent-native/core/a2a`) lets a hook add JSON-RPC params to outgoing `actions/invoke` calls and, on the receiving app, refuse an incoming call or admit it as foreground work (`isA2AForegroundCall()`), optionally in a verified organization. A refusal reaches the caller as `A2ACallRefusedError`.
> …

### [@agent-native/pinpoint@0.1.119](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/pinpoint%400.1.119)
<sub>2026-11-23 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

### [@agent-native/agentkit@0.232.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/agentkit%400.232.0)
<sub>2026-11-23 · today</sub>

> **Patch Changes**
> - 6facea0: Keep the Thinking indicator visible after a chat message appears while its run is starting, including when a queued message starts immediately.
> - 4163448: Define typed action suggestions and receipts so hosts can execute the specific action a user selects.
> - Release all public npm packages with a patch version bump.
> - 88dad0f: Keep a stopped chat reply's text the same live and after reload: Stop tells the server the last part of the reply the browser showed, the server saves the reply only up to there, and a run whose Stop reached another server still saves its reply.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [factory-run: no oncall ping on reporter questions; bare form submissi…](https://github.com/BuilderIO/agent-native/commit/8b4875096cc6aa40117772ea36a5ce6ed0c9b5db) | samijaber |
| 2026-11-24 | [Let Content's code-mode pilot run as scripts for allowlisted organiza…](https://github.com/BuilderIO/agent-native/commit/6e1e604563873b141cc95f002201e24053bcbf1b) | 3mdistal |
| 2026-11-24 | [content: show all available move destinations (#9754)](https://github.com/BuilderIO/agent-native/commit/f926f0b84382e512feeabdbaef4514289cfd9e40) | builder-factory |
| 2026-11-24 | [Design: local canvas performance benchmark (#9699)](https://github.com/BuilderIO/agent-native/commit/a5b8d285214540d94e19aa9e1eb172cd1060dac9) | shomix |
| 2026-11-24 | [Design: keep inspector controls within narrow panels (#9775)](https://github.com/BuilderIO/agent-native/commit/9d72686fb58a4b367af4da22caedacda567af589) | builder-factory |
| 2026-11-24 | [Record how big each MCP tool result is in tool-call analytics (#9687)](https://github.com/BuilderIO/agent-native/commit/acad739808b2f6ec7c8a0e14fdcd3232a717a36b) | 3mdistal |
| 2026-11-24 | [Show a data program's scheduled refresh in Analytics' MCP tools (#9697)](https://github.com/BuilderIO/agent-native/commit/c862f5821b0b949ec10c122421932da43f6a035c) | 3mdistal |
| 2026-11-24 | [Re-read a data program panel until the run its Refresh queued lands (…](https://github.com/BuilderIO/agent-native/commit/a20bef88d0b4f9435a7bf0d4a6dbc287a68a7d66) | 3mdistal |
| 2026-11-24 | [Bind durable attachment references to canonical submissions (#9736)](https://github.com/BuilderIO/agent-native/commit/b9ad2ba8576f822f8a968d9859e9a68332e494a6) | an-fleet-bot[bot] |
| 2026-11-24 | [Say why Content's Suggesting mode refused an edit (#9672)](https://github.com/BuilderIO/agent-native/commit/7d214dc1158d7f54c7f38c4736f56b799e7e77e5) | 3mdistal |

[See all commits ↗](https://github.com/BuilderIO/agent-native/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BuilderIO/agent-native.git
```
