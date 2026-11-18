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
| ⭐ **Stars** | 7.7k |
| 🍴 **Forks** | 710 |
| 🐞 **Open issues + PRs** | [276](https://github.com/BuilderIO/agent-native/issues) |
| 💻 **Languages** | TypeScript 87% · MDX 10% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `react` `agent-native` `typescript` `agent-framework` `agentic-ai` `ai-agents` `framework` `generative-ui` `mcp` `open-source` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [@agent-native/core@0.231.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.231.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 598.1 MB |
| 🌐 **Website** | https://www.agent-native.com |

## 📦 Recent releases

### [@agent-native/core@0.231.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.231.0)
<sub>2026-11-18 · today</sub>

> **Minor Changes**
> - 2755d62: Add `billing.commercialSurfaces` to `agent-native.json` (env `AGENT_NATIVE_CONFIG_BILLING_COMMERCIAL_SURFACES`). It defaults to `"show"`, which changes nothing. `"hide"` removes credit units and amounts, plan upgrades, free-credit offers and referral rewards: usage reads as dollars and tokens (a run reports its provider cost and no credits), existing credit alerts can't be listed, changed or delivered and new ones can't be created, stored credit-alert notices drop out of the inbox, the credit notice, credit-limit email and run-details credits row are left out, a credits-limit error offers only Retry in the card and the transcript, the referral action returns nothing, and the Builder connect popover, model picker and first-run setup drop the free-credit pitch. A composer host sets the Builder choice's caption with the `builder.creditsOffered` adapter. `commercialSurfacesHidden()` (from `@agent-native/core/client/app-config`) and `deploymentUsageBilling()` let an app follow the same setting, and `AgentKitRoot` takes `showRunCredits`. With `notifications.usageLimitNotices: false`, usage-limit alerts are no longer evaluated or sent on any channel.
> - 3d92e2e: Settings › Labs has a "Show all Labs features" switch that turns on every Lab the person hasn't chosen for. `set-labs-show-all` lets the agent flip it, the on/off state of each Lab is mirrored into the `labs` application state, and `assertLabEnabled` lets an action used only by a Lab refuse callers who haven't turned it on.
> **Patch Changes**
> - 9f49abc: Apps in a workspace with no domain can now delegate to each other. When both apps share `A2A_SECRET`, the caller sends the person's own signed identity with no workspace claim, and the peer runs the call in that person's personal scope instead of rejecting an unsigned request. When a peer pauses the delegated task for approval, the chat shows a card that opens the peer's approval page, then continues the same task once the person approves it there. The card stays in the chat after a reload and closes once that task finishes.
> - d863c6a: `setAgentChatContextItemAndPersist()` and `removeAgentChatContextItemAndPersist()` hold their change when a synchronous `setAgentChatContextItem()` publishes while their write is in flight. Before, the newer synchronous state hid the persisted change, so a composer prefill staged as the agent panel opened could vanish, and a removed one could stay. The change is now applied to that newer state, saved before the next queued write starts, and shown once saved, unless the synchronous change set the same key, or removed it or cleared the context. `setAgentChatContextItem()` and the other synchronous changes now save through the ordered app-state writer, so an earlier save can't reach the server after a later one and replace it.
> …

### [@agent-native/toolkit@0.231.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/toolkit%400.231.0)
<sub>2026-11-18 · today</sub>

> **Minor Changes**
> - 2755d62: Add `billing.commercialSurfaces` to `agent-native.json` (env `AGENT_NATIVE_CONFIG_BILLING_COMMERCIAL_SURFACES`). It defaults to `"show"`, which changes nothing. `"hide"` removes credit units and amounts, plan upgrades, free-credit offers and referral rewards: usage reads as dollars and tokens (a run reports its provider cost and no credits), existing credit alerts can't be listed, changed or delivered and new ones can't be created, stored credit-alert notices drop out of the inbox, the credit notice, credit-limit email and run-details credits row are left out, a credits-limit error offers only Retry in the card and the transcript, the referral action returns nothing, and the Builder connect popover, model picker and first-run setup drop the free-credit pitch. A composer host sets the Builder choice's caption with the `builder.creditsOffered` adapter. `commercialSurfacesHidden()` (from `@agent-native/core/client/app-config`) and `deploymentUsageBilling()` let an app follow the same setting, and `AgentKitRoot` takes `showRunCredits`. With `notifications.usageLimitNotices: false`, usage-limit alerts are no longer evaluated or sent on any channel.
> - 3d92e2e: Settings › Labs has a "Show all Labs features" switch that turns on every Lab the person hasn't chosen for. `set-labs-show-all` lets the agent flip it, the on/off state of each Lab is mirrored into the `labs` application state, and `assertLabEnabled` lets an action used only by a Lab refuse callers who haven't turned it on.
> **Patch Changes**
> - 9f49abc: Apps in a workspace with no domain can now delegate to each other. When both apps share `A2A_SECRET`, the caller sends the person's own signed identity with no workspace claim, and the peer runs the call in that person's personal scope instead of rejecting an unsigned request. When a peer pauses the delegated task for approval, the chat shows a card that opens the peer's approval page, then continues the same task once the person approves it there. The card stays in the chat after a reload and closes once that task finishes.
> - d863c6a: The editor drag handle's app menu request has `insertAbove()`, which adds an empty paragraph above the block with the caret in it. A menu in a dialog, such as a phone's bottom sheet, now stays open when the on-screen keyboard resizes the page, as a menu with `role="menu"` already did.
> …

### [@agent-native/pinpoint@0.1.118](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/pinpoint%400.1.118)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

### [@agent-native/dispatch@0.42.10](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/dispatch%400.42.10)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - 2755d62: Add `billing.commercialSurfaces` to `agent-native.json` (env `AGENT_NATIVE_CONFIG_BILLING_COMMERCIAL_SURFACES`). It defaults to `"show"`, which changes nothing. `"hide"` removes credit units and amounts, plan upgrades, free-credit offers and referral rewards: usage reads as dollars and tokens (a run reports its provider cost and no credits), existing credit alerts can't be listed, changed or delivered and new ones can't be created, stored credit-alert notices drop out of the inbox, the credit notice, credit-limit email and run-details credits row are left out, a credits-limit error offers only Retry in the card and the transcript, the referral action returns nothing, and the Builder connect popover, model picker and first-run setup drop the free-credit pitch. A composer host sets the Builder choice's caption with the `builder.creditsOffered` adapter. `commercialSurfacesHidden()` (from `@agent-native/core/client/app-config`) and `deploymentUsageBilling()` let an app follow the same setting, and `AgentKitRoot` takes `showRunCredits`. With `notifications.usageLimitNotices: false`, usage-limit alerts are no longer evaluated or sent on any channel.
> - 50f7168: Dispatch can now run a granted workspace app's actions directly. Set `dispatch.directAppActions` (env `DISPATCH_DIRECT_APP_ACTIONS=true`) to add `list_app_actions`, `call_app_action`, and `read_view` to Dispatch's agent and MCP tools; they call the target app as the signed-in user, only for apps that user has granted, and return in about a second instead of running the app's agent through `ask_app`. The setting is off by default, and with it off Dispatch's tools and `ask_app` are unchanged.
>   Dispatch app discovery now honors the workspace's `deployment.workspace.appsDirectory` and `appInclude` settings, and shows the `icon` set for an app in the deployment manifest or in `.agent-native/workspace-apps.json`. Apps listed without a description no longer break MCP task discovery.
>   `setDispatchAppActionHeaderProvider` (from `@agent-native/dispatch/server`) lets a deployment add headers to each direct app action connection, such as a per-turn grant the target app's MCP turn grant admitter recognizes. It can't replace `Authorization`.
>   A full MCP catalog (`catalog_scope: "full"`) now honors `externalAgents.writes: "ask_app_only"`: only reads and the compact builtins stay directly callable, and writes still go through `ask_app`. `mcpToolCallWasNotSent` (from `@agent-native/core/mcp-client`) tells a refusal `callTool` raised before sending apart from a failure after the call may have run.
> …

### [@agent-native/creative-context@0.8.75](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/creative-context%400.8.75)
<sub>2026-11-18 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [Add desktop host extension points for per-app onboarding (#9360)](https://github.com/BuilderIO/agent-native/commit/b608a9ee4613631d2caf0c76db62a83449cd30d6) | steve8708 |
| 2026-11-18 | [Add extension points for provider gates, A2A call hooks, MCP turn gra…](https://github.com/BuilderIO/agent-native/commit/41c2b0edd73bab20a0bffb5017b360aaa2ef4d04) | steve8708 |
| 2026-11-18 | [Add opt-in share focus, member invite and credential draft options (#…](https://github.com/BuilderIO/agent-native/commit/66de1ad4216f0b9d6eb6aa6e34ca7e1dd9014f0f) | steve8708 |
| 2026-11-18 | [Allow members to open new workspace apps before an admin visits (#9366)](https://github.com/BuilderIO/agent-native/commit/0cc6bb387b7555e3257b374cce591d6361590b3d) | steve8708 |
| 2026-11-18 | [chore: release packages (patch) [stable-release] [skip netlify] (#9365)](https://github.com/BuilderIO/agent-native/commit/c9e37cbd5a1053b4216460f4c8529466eff89b5e) | builder-io-integration[bot] |
| 2026-11-18 | [chore: release packages (patch) [stable-release] [skip netlify] (#9334)](https://github.com/BuilderIO/agent-native/commit/91038304706e399adcc7340f3d36ef02d8e62356) | builder-io-integration[bot] |
| 2026-11-18 | [design: hide templates when designs contain files (#9355)](https://github.com/BuilderIO/agent-native/commit/57947d99b9825138d0fd563697953bb994a34ed9) | builder-factory |
| 2026-11-18 | [Add opt-in direct app actions and workspace app icons to Dispatch (#9…](https://github.com/BuilderIO/agent-native/commit/50f71688775fa43e2c21aebdf9c26b8695664617) | steve8708 |
| 2026-11-18 | [Clips: bump Chrome extension to 0.1.24 (#9333)](https://github.com/BuilderIO/agent-native/commit/2db59c8ce13d7a361b54c008566b1aef79ff1d6d) | shomix |
| 2026-11-18 | [Add billing.commercialSurfaces to hide credits, plans and promos (#9357)](https://github.com/BuilderIO/agent-native/commit/2755d62a0c1ba19b6d858ede1b6abd91114128cc) | steve8708 |

[See all commits ↗](https://github.com/BuilderIO/agent-native/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BuilderIO/agent-native.git
```
