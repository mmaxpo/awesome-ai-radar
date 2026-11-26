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
| 🍴 **Forks** | 718 |
| 🐞 **Open issues + PRs** | [233](https://github.com/BuilderIO/agent-native/issues) |
| 💻 **Languages** | TypeScript 87% · MDX 10% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agents` `ai` `react` `agent-native` `typescript` `agent-framework` `agentic-ai` `ai-agents` `framework` `generative-ui` `mcp` `open-source` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [@agent-native/core@0.234.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.234.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 626.1 MB |
| 🌐 **Website** | https://www.agent-native.com |

## 📦 Recent releases

### [@agent-native/core@0.234.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core%400.234.0)
<sub>2026-11-25 · today</sub>

> **Minor Changes**
> - bf2d0b4: Generalize the MCP Skills extension (`io.modelcontextprotocol/skills`, SEP-2640) so any app can opt in via `mcp.skills` to serve reviewed, exported skills and optional `references/...` files alongside `ui://` MCP App resources with unified caller identity, org, OAuth scope, and revocation checks.
> - f7de4d5: Actions can live in subfolders of `actions/`; the name is the relative path joined with `-` (`billing/create-invoice.ts` is `billing-create-invoice`), and two files resolving to one name fail boot. `tool-search` returns exactly the tools named when a query is only known action names, and its description no longer pushes `includeSchemas`. Saved automations now apply the app's `resolveActionSurface`, so excluded tools are neither discoverable nor callable from them (`details.automation` is set and `details.event` is undefined for those runs).
> **Patch Changes**
> - 4a34f01: The `an` skill now describes when a live app view helps, carries the user's selection into follow-ups, updates the same view after a change and reads back what was saved. Dispatch's MCP server serves the skill through the MCP Skills extension, so hosts that support Skills over MCP get it with the connector.
> - 33e0e8c: Persist a run's terminal reason atomically with its terminal status so a successor lease cannot leave the completed run without a reason.
> …

### [@agent-native/creative-context@0.8.78](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/creative-context%400.8.78)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

### [@agent-native/agentkit@0.234.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/agentkit%400.234.0)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - e466d90: Keep a chat alive when it reconnects after its run moved on: the client and event stream now skip events from a run other than the subscribed one, and reconnecting from a sequence the server already pruned resumes from the earliest retained event instead of failing with `run_stream_failed`.
> - Release all public npm packages with a patch version bump.

### [@agent-native/recap-cli@0.5.109](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/recap-cli%400.5.109)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

### [@agent-native/core-corpus@0.234.0](https://github.com/BuilderIO/agent-native/releases/tag/%40agent-native/core-corpus%400.234.0)
<sub>2026-11-25 · today</sub>

> **Patch Changes**
> - Release all public npm packages with a patch version bump.

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Let the an skill pick the right Agent-Native app from a plain request…](https://github.com/BuilderIO/agent-native/commit/a3032a654da9600eb2184f45ea35e1a2f90ffc2f) | 3mdistal |
| 2026-11-26 | [Stop Create file and uploads from duplicating or overwriting a file o…](https://github.com/BuilderIO/agent-native/commit/415f03e467c7450d0a3f3e844b2905a2d51860c5) | 3mdistal |
| 2026-11-26 | [Keep the page still when a check mark is ticked on a phone or tablet …](https://github.com/BuilderIO/agent-native/commit/6409765ac8e274b4b466f861eab30dcfa2a99458) | 3mdistal |
| 2026-11-26 | [Stop Mail's repeated Gmail cooldowns from 50-part batches and non-Gma…](https://github.com/BuilderIO/agent-native/commit/20691507dcb79810f2074857a08ad9088ca8c846) | 3mdistal |
| 2026-11-26 | [Start J and K from the email you're on in Mail, and mark it once (#9730)](https://github.com/BuilderIO/agent-native/commit/02936993d6260e5270a5fb31f90858c79d395719) | 3mdistal |
| 2026-11-26 | [Design: stop showing a failure when an image edit succeeded (#9919)](https://github.com/BuilderIO/agent-native/commit/b4b454a4984792982fe55ad39df4952ab207ec34) | steve8708 |
| 2026-11-26 | [Report Typecheck success for verified changelog-only changes (#9912)](https://github.com/BuilderIO/agent-native/commit/aa224c4090cdb23d96a8ca63b05fe622b1a0b26a) | steve8708 |
| 2026-11-26 | [fix(design): list components in the layers panel and show typed expor…](https://github.com/BuilderIO/agent-native/commit/6cacb9d95254ffc5ecf83ec27deb3746aff2e594) | steve8708 |
| 2026-11-26 | [toolkit: let an app reveal its tree while the session loads (#9918)](https://github.com/BuilderIO/agent-native/commit/a37f93540ef31a3383c5adb93022a70919e3bedb) | steve8708 |
| 2026-11-26 | [design: Arrange options reorder layers in unfocused overview screens …](https://github.com/BuilderIO/agent-native/commit/37bab500262faafb7d06c0be6ba260a05a7cf46e) | steve8708 |

[See all commits ↗](https://github.com/BuilderIO/agent-native/commits)

## ⬇️ Get it

```bash
git clone https://github.com/BuilderIO/agent-native.git
```
