# anomalyco/opencode

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/anomalyco/opencode)

> The open source coding agent.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Open-source AI coding agent |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 227.7k |
| 🍴 **Forks** | 30.9k |
| 🐞 **Open issues + PRs** | [4.1k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 85% · MDX 11% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) — 2026-11-18 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 732.0 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · today</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · today</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · yesterday</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

### [process-daemon-v0.6.0](https://github.com/anomalyco/opencode/releases/tag/process-daemon-v0.6.0) — process-daemon v0.6.0
<sub>2026-11-16 · yesterday</sub>

> opencode-pty 0.6.0 (protocol 9) from packages/process-daemon, published to npm as @opencode/pty@0.6.0.

### [v2.3.0](https://github.com/anomalyco/opencode/releases/tag/v2.3.0)
<sub>2026-11-13 · 5d ago</sub>

> **Highlights**
> - **Background Subagents by Default**: Subagents now return immediately, continue in the background, and report back whenever they become idle. You can keep working in the parent session while multiple subagents run concurrently. ([#63382](https://github.com/anomalyco/opencode/pull/63382))
> - **Quieter Transcripts by Default**: The TUI now summarizes each run of tool calls and thoughts into one collapsible activity row, so the answer is easier to follow. To see every step again, set **Verbosity** to `medium` or `high` in settings, or set `session.verbosity` in your TUI config; an existing setting is kept. ([#63207](https://github.com/anomalyco/opencode/pull/63207))
> - **Jump to an Earlier Prompt**: In the desktop app, open **Jump to message** from the command palette or press `Cmd+Alt+G` (`Ctrl+Alt+G` on Windows and Linux) to search prompts across the current session and jump directly to one. ([#63585](https://github.com/anomalyco/opencode/pull/63585))
> **Core**
> **Improvements**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [fix(app): keep Home's date headers visible while scrolling (#64665)](https://github.com/anomalyco/opencode/commit/bb01d3eeccbca4db324d5997db1507ca919a274c) | arvsrn |
| 2026-11-18 | [fix(session-ui): keep the latest response copy visible at rest (#64640)](https://github.com/anomalyco/opencode/commit/0220248dc102d6d7cf89fcf5f970ca22d4624b29) | usrnk1 |
| 2026-11-18 | [fix(core): match file permission rules without case on macOS (#64626)](https://github.com/anomalyco/opencode/commit/79bd2c6f11fd5ad011dbe5a1c31343c46e1e5294) | knp-sap |
| 2026-11-18 | [feat(app): redesign the goal pill (#60001)](https://github.com/anomalyco/opencode/commit/d412042beb9821ed61c73466406f7dbfdadc04e0) | arvsrn |
| 2026-11-18 | [feat(plugin): let GUI plugins declare their own icons (#64577)](https://github.com/anomalyco/opencode/commit/22377659a8ed223f3eebc86660dd1a5bc2b33ca5) | Hona |
| 2026-11-18 | [docs(go): note GLM-5.3 limited-time limits (#64611)](https://github.com/anomalyco/opencode/commit/521ceac004e59fbbfca0929596107cd8430f2b26) | opencode-agent[bot] |
| 2026-11-18 | [docs: deprecate GLM-5.3-Flash Free (#64600)](https://github.com/anomalyco/opencode/commit/1862f2ce5c4ac5ec9b47b4aea85a5412f8e23a19) | opencode-agent[bot] |
| 2026-11-18 | [refactor(core): replace watch_mcp_event with list_mcp_events (#64586)](https://github.com/anomalyco/opencode/commit/a0fdbf9b91ed2cf8bfd778ccec340285403eddc2) | rekram1-node |
| 2026-11-18 | [feat(core): tell models about Bun's file APIs in Code Mode with full_…](https://github.com/anomalyco/opencode/commit/7667ec40206230a76c9e285ee594a04c2173523d) | rekram1-node |
| 2026-11-18 | [fix(codemode): say why an import can't be resolved (#64587)](https://github.com/anomalyco/opencode/commit/db8730ebcd192fe72e044c2286859d892cce2225) | rekram1-node |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
