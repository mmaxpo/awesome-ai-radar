# sandbox-quantum/switch

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/sandbox-quantum/switch)

> Open-source AI teammates in Slack, Teams, Discord, Telegram and Mattermost. Self-host it, with any agent harness and any model.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Self-hosted coding agents inside Slack, Teams or Discord |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 4.5k |
| 🍴 **Forks** | 354 |
| 🐞 **Open issues + PRs** | [694](https://github.com/sandbox-quantum/switch/issues) |
| 💻 **Languages** | Python 55% · TypeScript 44% |
| 📜 **License** | Other |
| 🏷 **Topics** | `agent-orchestration` `ai-agents` `discord` `mcp` `microsoft-teams` `multi-agent` `slack` `ai` `chatops` `langchain` `open-source` `openai` `self-hosted` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-07-16 |
| 📦 **Latest release** | [switch-console-v0.41.1](https://github.com/sandbox-quantum/switch/releases/tag/switch-console-v0.41.1) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 93.4 MB |
| 🌐 **Website** | https://www.switchagents.ai |

## 📦 Recent releases

### [switch-agent-controller-v0.32.2-dev.628.g9704ba1](https://github.com/sandbox-quantum/switch/releases/tag/switch-agent-controller-v0.32.2-dev.628.g9704ba1) — switch-agent-controller 0.32.2-dev.628.g9704ba1 (dev build of main) _(pre-release)_
<sub>2026-11-18 · today</sub>

> The Switch agent controller built from main at 9704ba133acf462824f302c7815ef68b90d9d4b6, for the dev environment, whose controllers update to it on their own. Not for installing by hand; switch-dev-cleanup prunes it.
>   SHA-256: `1f0c2202ee2ff5e7c024b56718f73e95ad1397e1ec871d835f7ec798943cbd62`

### [switch-console-v0.41.1](https://github.com/sandbox-quantum/switch/releases/tag/switch-console-v0.41.1) — Switch Console 0.41.1
<sub>2026-11-18 · today</sub>

> **What's Changed**
> - **The workspace switcher now shows on every build, not only one that can reach Switch Cloud** — second workspaces, Create organization, New workspace and pending invitations are reachable from the sidebar on stable too
> - **Install failures show the whole error** (and log it in full) instead of a truncated message
> - **Sidebar reads a workspace's agents' rooms in one request** rather than one per agent each refresh
> - **Fixed:** Cursor launches with a supported permission mode
> - **switch-buddy's opening messages slide in** from onboarding/Home
> …

### [switch-v0.32.1](https://github.com/sandbox-quantum/switch/releases/tag/switch-v0.32.1) — switch-core 0.32.1
<sub>2026-11-18 · today</sub>

> **What's Changed**
> - **A re-enrolled computer keeps its device and agents** — a controller enrolling again from a machine/account/data-folder it already has a device for takes that device over (same id, name, agents) instead of creating a duplicate
> - **`GET /gateway/agents/rooms`** — list up to 100 agents' rooms in one request
> - **Fixed:** reading an agent no longer loads every room in the workspace (Console sidebar refresh no longer hogs the DB pool)
> - **Preview (behind a flag, off by default):** auto-route ↔ assigned-agent mutual exclusion, single-agent untagged delivery, and a Gemini decision backend
> **Contributors:** @agent-runner353 · @amaudruz · @abeldantas · @christian-mcdermott · @raullopez-sandbox
> …

### [switch-agent-controller-v0.32.1](https://github.com/sandbox-quantum/switch/releases/tag/switch-agent-controller-v0.32.1) — switch-agent-controller 0.32.1
<sub>2026-11-18 · today</sub>

> The Switch agent controller 0.32.1, released with Switch 0.32.1, for running managed agents on your own Linux or macOS machines.
> SHA-256: `c2a2bbc9eda9b8b1c71c792074ca7e830dee47efe32cc52344e7d3260bfab625`
> Install (Node 22.13 or later) with `install.sh`, which checks the package's signature (`switch-agent-controller-0.32.1.tgz.sig`) before installing it. Then enroll with a code from the Devices page and run `switch-agent-controller install-service`. A controller connected to Switch 0.32.1 updates to this release on its own once it is idle.

### [switch-agent-controller-v0.32.1-dev.626.g7a0009e](https://github.com/sandbox-quantum/switch/releases/tag/switch-agent-controller-v0.32.1-dev.626.g7a0009e) — switch-agent-controller 0.32.1-dev.626.g7a0009e (dev build of main) _(pre-release)_
<sub>2026-11-18 · today</sub>

> The Switch agent controller built from main at 7a0009ef6143150ce56641da52db805d0efb14fc, for the dev environment, whose controllers update to it on their own. Not for installing by hand; switch-dev-cleanup prunes it.
>   SHA-256: `ab7cadff2f4e58860a70f3d17208225772491f800038d8c9988f3e70f76e7884`

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [chore(release): Switch Console 0.41.1 (#2132)](https://github.com/sandbox-quantum/switch/commit/9704ba133acf462824f302c7815ef68b90d9d4b6) | amaudruz |
| 2026-11-18 | [chore(release): switch-core 0.32.1 (#2131)](https://github.com/sandbox-quantum/switch/commit/7a0009ef6143150ce56641da52db805d0efb14fc) | amaudruz |
| 2026-11-18 | [Merge pull request #2126 from sandbox-quantum/feat/decision-gemini-ba…](https://github.com/sandbox-quantum/switch/commit/5b9bbfe2883cd7c9e02c5d36e1ef685078660eec) | agent-runner353 |
| 2026-11-18 | [Keep a computer's device and agents when it enrolls again (device ide…](https://github.com/sandbox-quantum/switch/commit/7088f20d8512d1702eafd44576e7fe2b6470f60b) | christian-mcdermott |
| 2026-11-18 | [decision: spell out the colleague-reply exception for Gemini and Haiku](https://github.com/sandbox-quantum/switch/commit/775683d28a4292f94d726ebb7a484e1af541b3ba) | agent-runner353 |
| 2026-11-18 | [decision: add a gemini_decision backend (Google's Decisions API)](https://github.com/sandbox-quantum/switch/commit/246e81e30935876dd670facf470d27248903753c) | agent-runner353 |
| 2026-11-18 | [fix(console): show the whole install error and log failed installs in…](https://github.com/sandbox-quantum/switch/commit/483d32234da0555fdede794bccd4ff42f51031b4) | amaudruz |
| 2026-11-18 | [Console: slide in switch-buddy's first messages on the way from onboa…](https://github.com/sandbox-quantum/switch/commit/b027564f0f1065f2957bd36e594bc86d0eb09827) | amaudruz |
| 2026-11-18 | [Merge pull request #2026 from sandbox-quantum/feat/one-to-one-rooms-a…](https://github.com/sandbox-quantum/switch/commit/782a18c39e615dfca06ee8973e2b55466c105f36) | agent-runner353 |
| 2026-11-18 | [Merge pull request #2117 from sandbox-quantum/fix/cursor-permission-m…](https://github.com/sandbox-quantum/switch/commit/4d06fe2d080cee50a2c746e19136b888ce1eb3ca) | raullopez-sandbox |

[See all commits ↗](https://github.com/sandbox-quantum/switch/commits)

## ⬇️ Get it

```bash
git clone https://github.com/sandbox-quantum/switch.git
```
