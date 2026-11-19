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
| 🐞 **Open issues + PRs** | [264](https://github.com/BuilderIO/agent-native/issues) |
| 💻 **Languages** | TypeScript 87% · MDX 11% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `react` `agent-native` `typescript` `agent-framework` `agentic-ai` `ai-agents` `framework` `generative-ui` `mcp` `open-source` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [@agent-native/core@0.231.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.231.0) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 601.9 MB |
| 🌐 **Website** | https://www.agent-native.com |

## 📦 Recent releases

### [v0.1.150-nightly.450](https://github.com/BuilderIO/agent-native/releases/tag/v0.1.150-nightly.450) — Agent-Native Nightly v0.1.150-nightly.450 _(pre-release)_
<sub>2026-11-19 · today</sub>

> Auto-updating Nightly build of the Agent-Native desktop app.

### [clips-nightly-v0.1.528-0](https://github.com/BuilderIO/agent-native/releases/tag/clips-nightly-v0.1.528-0) — Clips Nightly v0.1.528-0 _(pre-release)_
<sub>2026-11-18 · today</sub>

> Auto-updating nightly build of the Clips menu-bar app.
> The in-app updater fetches its manifest from the `clips-nightly-latest`
> release — this versioned release is the immutable source of the
> signed bundles it downloads.

### [v0.1.150-nightly.449](https://github.com/BuilderIO/agent-native/releases/tag/v0.1.150-nightly.449) — Agent-Native Nightly v0.1.150-nightly.449 _(pre-release)_
<sub>2026-11-18 · today</sub>

> Auto-updating Nightly build of the Agent-Native desktop app.

### [v0.1.150-nightly.448](https://github.com/BuilderIO/agent-native/releases/tag/v0.1.150-nightly.448) — Agent-Native Nightly v0.1.150-nightly.448 _(pre-release)_
<sub>2026-11-18 · yesterday</sub>

> Auto-updating Nightly build of the Agent-Native desktop app.

### [@agent-native/core@0.231.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.231.0)
<sub>2026-11-18 · yesterday</sub>

> **Minor Changes**
> - 2755d62: Add `billing.commercialSurfaces` to `agent-native.json` (env `AGENT_NATIVE_CONFIG_BILLING_COMMERCIAL_SURFACES`). It defaults to `"show"`, which changes nothing. `"hide"` removes credit units and amounts, plan upgrades, free-credit offers and referral rewards: usage reads as dollars and tokens (a run reports its provider cost and no credits), existing credit alerts can't be listed, changed or delivered and new ones can't be created, stored credit-alert notices drop out of the inbox, the credit notice, credit-limit email and run-details credits row are left out, a credits-limit error offers only Retry in the card and the transcript, the referral action returns nothing, and the Builder connect popover, model picker and first-run setup drop the free-credit pitch. A composer host sets the Builder choice's caption with the `builder.creditsOffered` adapter. `commercialSurfacesHidden()` (from `@agent-native/core/client/app-config`) and `deploymentUsageBilling()` let an app follow the same setting, and `AgentKitRoot` takes `showRunCredits`. With `notifications.usageLimitNotices: false`, usage-limit alerts are no longer evaluated or sent on any channel.
> - 3d92e2e: Settings › Labs has a "Show all Labs features" switch that turns on every Lab the person hasn't chosen for. `set-labs-show-all` lets the agent flip it, the on/off state of each Lab is mirrored into the `labs` application state, and `assertLabEnabled` lets an action used only by a Lab refuse callers who haven't turned it on.
> **Patch Changes**
> - 9f49abc: Apps in a workspace with no domain can now delegate to each other. When both apps share `A2A_SECRET`, the caller sends the person's own signed identity with no workspace claim, and the peer runs the call in that person's personal scope instead of rejecting an unsigned request. When a peer pauses the delegated task for approval, the chat shows a card that opens the peer's approval page, then continues the same task once the person approves it there. The card stays in the chat after a reload and closes once that task finishes.
> - d863c6a: `setAgentChatContextItemAndPersist()` and `removeAgentChatContextItemAndPersist()` hold their change when a synchronous `setAgentChatContextItem()` publishes while their write is in flight. Before, the newer synchronous state hid the persisted change, so a composer prefill staged as the agent panel opened could vanish, and a removed one could stay. The change is now applied to that newer state, saved before the next queued write starts, and shown once saved, unless the synchronous change set the same key, or removed it or cleared the context. `setAgentChatContextItem()` and the other synchronous changes now save through the ordered app-state writer, so an earlier save can't reach the server after a later one and replace it.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [Design: handle failed plan submissions (#9205)](https://github.com/BuilderIO/agent-native/commit/0eeea8c3807240daaa3cd936f4734431f1f62598) | builder-factory |
| 2026-11-19 | [Keep redacted Brain knowledge retrievable with write-time provenance …](https://github.com/BuilderIO/agent-native/commit/a7165c23af6da77885630ccdb97c9e5054801626) | steve8708 |
| 2026-11-19 | [Keep poll feeds moving past unreadable events (#9452)](https://github.com/BuilderIO/agent-native/commit/658a9f505f533a83061acd03914e22ca1931d6fa) | steve8708 |
| 2026-11-19 | [fix(toolkit): hold Enter in the composer while the model list loads (…](https://github.com/BuilderIO/agent-native/commit/234a3bac3b8963f0e9434f5b86d427171c439259) | steve8708 |
| 2026-11-19 | [Keep share access controls reachable (#9447)](https://github.com/BuilderIO/agent-native/commit/caec4be74df0111c0209ee89e7223e9c3f189f5d) | steve8708 |
| 2026-11-19 | [Design: don't throw on cross-origin iframe scroll reads (#8687)](https://github.com/BuilderIO/agent-native/commit/ad0d44a3e5d68881410135f531a553d2a2eeb693) | builder-factory |
| 2026-11-19 | [Report definite distillation delivery failures accurately (#9444)](https://github.com/BuilderIO/agent-native/commit/5402d2313b4afd7ce6b204a828e6545aa37484da) | steve8708 |
| 2026-11-19 | [Leave Brain's schema to its migrations at boot (#9443)](https://github.com/BuilderIO/agent-native/commit/6bba7708ef94b2a3b6d7bf7e50189b0f985cfeff) | steve8708 |
| 2026-11-19 | [Give Content's Agent tab one head, one loading placeholder and wrappe…](https://github.com/BuilderIO/agent-native/commit/1090567dd6b8bc97c45c33964655b90055fc8daf) | 3mdistal |
| 2026-11-19 | [Fix Share Escape swallowed by exiting suggestion list (#9440)](https://github.com/BuilderIO/agent-native/commit/6938e7c3f92ed074cba339b87d7350dd6e3ea041) | builder-factory |

[See all commits ↗](https://github.com/BuilderIO/agent-native/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BuilderIO/agent-native.git
```
