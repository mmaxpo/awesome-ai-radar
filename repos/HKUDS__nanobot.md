# HKUDS/nanobot

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/HKUDS/nanobot)

> Your lightweight open-source personal agent.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Lightweight open-source personal agent |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 50.3k |
| 🍴 **Forks** | 8.8k |
| 🐞 **Open issues + PRs** | [862](https://github.com/HKUDS/nanobot/issues) |
| 💻 **Languages** | Python 61% · TypeScript 38% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-agent` `ai-agents` `openclaw` `agent-framework` `chatbot` `chatops` `discord-bot` `llm-agents` `llms` `local-llm` `mcp` `model-context-protocol` `multi-agent` `openai-compatible` `personal-ai-assistant` `python` `self-hosted` `telegram-bot-ai-assistant` `webui` `workflow-automation` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-02-01 |
| 📦 **Latest release** | [v0.4.2](https://github.com/HKUDS/nanobot/releases/tag/v0.4.2) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 88.6 MB |
| 🌐 **Website** | https://nanobot.wiki |

## 📦 Recent releases

### [v0.4.2](https://github.com/HKUDS/nanobot/releases/tag/v0.4.2)
<sub>2026-11-21 · 2d ago</sub>

> **Changes**
> - Connect over SSH to gateways that also advertise a public WebSocket URL. **Use existing SSH settings** now supports Windows hosts where Python 3 is available as `python`. The quick-pairing command remains Linux-only; gateway-native TLS and `trustedProxyAuth` are still unsupported over SSH. [#6682](https://github.com/HKUDS/nanobot/pull/6682)
> - See the latest activity when a turn is collapsed, and see which follow-up messages are still waiting for the agent. Reconnecting also preserves the state of running turns more reliably. [#6664](https://github.com/HKUDS/nanobot/pull/6664), [#6719](https://github.com/HKUDS/nanobot/pull/6719), [#6726](https://github.com/HKUDS/nanobot/pull/6726), [#6715](https://github.com/HKUDS/nanobot/pull/6715)
> - Find Tools, Skills, and Chat Platforms in one **Apps** catalog. Choose the reasoning effort for your next message from the composer, without changing the shared preset. [#6700](https://github.com/HKUDS/nanobot/pull/6700), [#6441](https://github.com/HKUDS/nanobot/pull/6441)
> - Long messages you send can collapse to keep the conversation easier to scan. Expand them with **Show more**, or copy the full text without expanding. [#6739](https://github.com/HKUDS/nanobot/pull/6739)
> - Align the footer controls in the settings sidebar, and keep the model picker open when you reopen it quickly after switching presets. [Settings sidebar fix](https://github.com/HKUDS/nanobot/commit/bc690f0394a00703d6f25a48c63ecb0170b2e091), [#6743](https://github.com/HKUDS/nanobot/pull/6743)
> …

### [v0.4.1](https://github.com/HKUDS/nanobot/releases/tag/v0.4.1)
<sub>2026-11-06 · 17d ago</sub>

> **Changes**
> - Fix TLS certificate verification, sandboxed shell execution and workspace permissions for queued inputs.
> - Keep idle maintenance from blocking active work or incorrectly refusing an update. Improve retry, reconnection and recovery behavior, and preserve native provider state through compaction.
> - Add a file-context graph with file previews, local Markdown links and recent context snapshots. Switching topics keeps each conversation's context separate.
> - Share syntax highlighting across code, source previews and read-only diffs, with complete source copying and plain-text fallbacks.
> - Reduce unnecessary memory copies in file reads, session history and provider requests. Improve navigation, context-usage display, history loading and skill-source identification.
> …

### [v0.4.0](https://github.com/HKUDS/nanobot/releases/tag/v0.4.0)
<sub>2026-10-28 · 26d ago</sub>

> 🐈 **nanobot `v0.4.0`** makes everyday work easier to continue — with durable conversation history, a more capable workbench, and a clearer path to the next update.
> **Keep moving.** The gateway now stores model history and browser transcripts in SQLite, imports existing conversations, and coordinates updates around saved state. Stable and opt-in Preview releases share one update flow, with explicit confirmation before installation and restart.
> The browser workbench is easier to navigate and connect: complete prompt-history navigation, remote instances, clearer delegated-task details, richer attachments, and more consistent mobile controls. The terminal gains Mermaid diagram viewing and target-specific native bundles. Both clients continue to use the same Python gateway.
> This release also makes installation ownership explicit. Supported managed installations can update and recover the program through the app; other installations receive instructions for their original package manager or deployment. Recovery does not mean restoring an old copy of your chats. Please read the upgrade notes before replacing an existing installation.
> **Highlights**
> - **One update flow, with your confirmation** — Check releases in Settings → About, choose whether to receive Preview updates, review the exact version, and confirm installation and restart. Supported official-installer and POSIX uv environments can use the in-app flow once the public release has verified approval proof.
> …

### [v0.3.5](https://github.com/HKUDS/nanobot/releases/tag/v0.3.5)
<sub>2026-09-15 · 2mo ago</sub>

> 🐈 **nanobot `v0.3.5`** brings the workbench to the terminal — and makes conversations easier to continue across the browser, terminal, and chat apps.
> The headline is **one agent, more places to work**. Run `nanobot` for the native terminal client or `nanobot webui` for the browser. Both use the same gateway and saved WebSocket conversations. Terminal sessions can be resumed, forked, inspected, and detached without building a separate agent runtime.
> The browser workbench has grown around real multitasking: grouped conversation panes, temporary chats, persistent sidebar ordering, session mentions, a skills marketplace, portable Agent Plugins, and browser OAuth for remote MCP servers. Automations now have task and calendar views, clearer scheduling controls, and per-run replies. Mobile composition, settings, context charts, app logos, and branded mentions received another round of focused polish.
> The other story is **continuity you can inspect**. Context usage and compaction are visible, interrupted work has clearer recovery controls, and session history is more durable across pagination, reconnects, and upgrades. This release also tightens attachment, process, workspace, and email-authentication boundaries. Please read the upgrade notes before replacing an existing installation.
> **Highlights**
> - **A native terminal workbench** — Start with `nanobot`, switch sessions, paste supported clipboard images, complete app and skill references, inspect context and file diffs, queue follow-ups, and use `/detach` to leave the gateway running.
> …

### [v0.3.0](https://github.com/HKUDS/nanobot/releases/tag/v0.3.0)
<sub>2026-07-25 · 4mo ago</sub>

> 🐈 **nanobot `v0.3.0`** is here: **260 PRs merged and 38 new contributors**. The agent gained agency.
> The fastest way to experience the release is one command:
> ```bash
> nanobot webui
> ```
> It prepares the local WebUI, starts the gateway, and opens the browser workbench. On a fresh install, guided setup helps you choose a provider and configure access without beginning in a JSON file. The published package already includes the WebUI, so there is no separate frontend build.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [fix(commands): deliver deferred receipts in order to the original ses…](https://github.com/HKUDS/nanobot/commit/37c2af8ffc86c5adf0a9e42732e26722d8a4260b) | chengyongru |
| 2026-11-23 | [feat(channels): localize native Telegram, Discord and Feishu command …](https://github.com/HKUDS/nanobot/commit/db93433950fbd6c56d5adbf7800535e7177945e6) | chengyongru |
| 2026-11-23 | [test: consolidate overlapping coverage across runtime and clients (#6…](https://github.com/HKUDS/nanobot/commit/a078bffdf9a7728d17ecbda62f59c60348dc9d03) | chengyongru |
| 2026-11-23 | [fix(webui): honor the /model result before displaying or using a pres…](https://github.com/HKUDS/nanobot/commit/9fc36e1b72769575ddac9078c5595b97188a7a13) | chengyongru |
| 2026-11-23 | [fix(webui): adapt message actions to the chat pane width (#6762)](https://github.com/HKUDS/nanobot/commit/6ab2d8ffb5359b9a0bf89d1e3e830ce1e75a00a8) | chengyongru |
| 2026-11-23 | [feat(clients): localize slash menus and preserve command reply text (…](https://github.com/HKUDS/nanobot/commit/44fcf6439817c7dc921c22fb9bc222134ee3ab01) | chengyongru |
| 2026-11-23 | [feat(commands): route localized command results through channel prese…](https://github.com/HKUDS/nanobot/commit/d38aac78989ec601d2fa0f6ede174654f28a3fa6) | chengyongru |
| 2026-11-23 | [fix(types): describe the regex search contract for JSON schema (#6755)](https://github.com/HKUDS/nanobot/commit/026191c9badb8efcb58c2f3aae6c4aee64ec78bb) | chengyongru |
| 2026-11-23 | [fix(webui): align activity status icons with reply text (#6754)](https://github.com/HKUDS/nanobot/commit/ee65a5945507d5c4a9368f88a19a3b77cb160e7e) | chengyongru |
| 2026-11-23 | [feat(webui): fold the diff toggle into the file edit row (#6753)](https://github.com/HKUDS/nanobot/commit/e8ddac5283fe5cea5475d2c0cb0342cbc7ece1a3) | chengyongru |

[See all commits ↗](https://github.com/HKUDS/nanobot/commits)

## ⬇️ Get it

```bash
git clone https://github.com/HKUDS/nanobot.git
```
