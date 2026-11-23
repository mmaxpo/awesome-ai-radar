# open-webui/open-webui

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/open-webui/open-webui)

> User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🧩 Low-code builders & chat UIs |
| **Project** | — |
| **Why it's worth a look** | Self-hosted chat UI for Ollama and OpenAI-compatible APIs |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 159.3k |
| 🍴 **Forks** | 23.1k |
| 🐞 **Open issues + PRs** | [288](https://github.com/open-webui/open-webui/issues) |
| 💻 **Languages** | Svelte 39% · Python 37% · JavaScript 16% · TypeScript 7% · CSS 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ollama` `ollama-webui` `llm` `webui` `self-hosted` `llm-ui` `llm-webui` `llms` `rag` `ai` `open-webui` `ui` `openai` `mcp` `openapi` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2023-10-06 |
| 📦 **Latest release** | [v0.13.4](https://github.com/open-webui/open-webui/releases/tag/v0.13.4) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 667.2 MB |
| 🌐 **Website** | https://openwebui.com |

## 📦 Recent releases

### [v0.13.4](https://github.com/open-webui/open-webui/releases/tag/v0.13.4)
<sub>2026-11-17 · 6d ago</sub>

> **Added**
> - **Bring your own computer with Tether.** Tether turns your own computer into part of Open WebUI: models from Ollama, LM Studio or any OpenAI-compatible server, OpenAPI and MCP tool servers and Open Terminal servers that you add in the Tether app now show up just for you in the model selector, the Tools list of the + menu and the terminal menu of any Open WebUI you connect, from whatever device you open it on, and Open WebUI reaches them through Tether, so their addresses, commands and keys never leave your computer. This needs Tether 0.1.14 or later, or 0.1.16 for MCP servers, tool servers and terminals need "ENABLE_TOOL_SERVERS" turned on, and a Tether model whose ID matches a model already in Open WebUI stays hidden. Tether replaces Direct Connections. [#34397](https://github.com/open-webui/open-webui/issues/34397)
> - **Sandboxed agents on your own computer.** Tether 0.1.13 or later can lock the terminal on your computer into a sandbox, so models and coding agents work in your real files without reaching the rest of your machine: on macOS and supported Windows devices, Open Terminal and everything it launches, coding agents included, can only touch the one folder you pick, run offline unless you turn on Network access and accept no incoming connections, with no Docker, virtual machine or administrator setup needed. If the sandbox cannot be enforced, the terminal stays stopped instead of quietly running without it, and browser and desktop control stay off while it is on. Turn it on in Tether under Settings > Open Terminal > Sandbox.
> - **Local MCP servers through Tether.** Open WebUI can now use MCP servers that run as a local command over stdio, the way many MCP servers are distributed, by launching them on your computer through Tether 0.1.16 or later, with no proxy such as mcpo and no port to open. Add one in Tether under Settings > Integrations > Tools with its command, or connect an MCP server by its web address, and pick it from the Tools list of the + menu. Local commands run with your own account's access, outside Tether's workspace sandbox.
> - **A computer for every user.** With Terminals 0.4.0 or later connected, Open WebUI now hands out sandboxed computers on demand: anyone with Write access to the connection can create a terminal right from the terminal menu of the message input, pick whether everyone shares one machine or each user, chat or model gets its own, and set its image, CPU, memory, storage, network profile, environment variables, start directory and a setup script that, for example, clones a repository and installs its dependencies, without an administrator setting up each one. Terminals can be shared with users and groups and their instances started, stopped, restarted or deleted, a View files option opens any terminal's files without selecting it for the chat, System info shows how the setup script went, and those who manage a terminal can open the files and system info of other people's running instances. Start and Stop need Terminals 0.4.1 or later, the start directory and setup script need Open Terminal 0.17.7 or later in the terminal's image, and network profiles are the ones an administrator defined with "TERMINALS_NETWORK_PROFILES".
> - **Coding agents as chat models.** Coding agents now work much like any other model in the chat. Hermes, Antigravity, GitHub Copilot, Goose and Qwen Code join Codex, Claude Code, Cursor, Grok, OpenCode, Cline, Gemini CLI and Pi, and any other ACP agent added to Open Terminal with "OPEN_TERMINAL_ACP_AGENTS" works as well, once it is installed and signed in on the terminal. Auto for tool permissions now lets Codex, Claude Code and Grok approve routine actions themselves and pass on only what they escalate, and the reasoning effort in the advanced parameters now also applies to Claude Code, Pi and ACP agents that offer effort levels, such as OpenCode, which stop with an error when the chosen level is not offered for the model. Replies can now be regenerated and earlier messages edited, and a forked or cloned agent chat picks up where the original left off: Codex continues its own conversation from that point, other agents start over from the chat so far, and file changes the agent already made stay. Claude Code continues its own conversation too with the next Open Terminal release after 0.17.20 and until then asks you to update Open Terminal instead. The new agents and Auto for Claude Code and Grok need Open Terminal 0.17.19 or later, and effort for Claude Code, Pi and ACP agents needs 0.17.9 or later. [#34167](https://github.com/open-webui/open-webui/issues/34167)
> …

### [v0.13.3](https://github.com/open-webui/open-webui/releases/tag/v0.13.3)
<sub>2026-11-08 · 14d ago</sub>

> **Added**
> - 🦾 **Agents in automations.** The automation editor now lets you choose a terminal and working folder, then select a coding agent available there. Scheduled runs use that saved terminal and folder, and check that the terminal and agent are still available before starting. Agent automations send their results to a chat; channel destinations remain available for ordinary models. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
> - 📂 **Change terminal and folder during a chat.** You can now choose a different terminal or working folder after sending messages, including in temporary chats. Both controls remain disabled while a reply is being generated. [Commit](https://github.com/open-webui/open-webui/commit/a518ff1630b74ed6edd62538c5da4bb26cc6dd20)
> - 🇧🇷 **Brazilian Portuguese translations.** Added missing translations for terminal and folder controls, Git actions, spreadsheet editing, voice notes, tab shortcuts, notification sounds and tool settings. Updated the explanations for document retrieval, tool permissions and voice settings. [#33945](https://github.com/open-webui/open-webui/pull/33945)
> **Fixed**
> - 📂 **Files tabs follow terminal changes.** Switching a chat to another terminal now updates its open Files tabs to show that terminal's files, instead of leaving the previous terminal's folders on screen. With a terminal set to "Per chat", the Files tab also switches to the chat's own files after the first message. [#33954](https://github.com/open-webui/open-webui/pull/33954)
> …

### [v0.13.2](https://github.com/open-webui/open-webui/releases/tag/v0.13.2)
<sub>2026-11-08 · 15d ago</sub>

> **Fixed**
> - 🔓 **Chat over plain HTTP.** Opening Open WebUI over plain HTTP at a LAN or Docker address now loads new and existing chats instead of staying on a spinner with "crypto.randomUUID is not a function". [#33919](https://github.com/open-webui/open-webui/issues/33919)
> - 📝 **Comments and Markdown editing over plain HTTP.** Creating, replying to and editing comments, and editing Markdown files containing rendered blocks such as Mermaid diagrams or callouts, no longer fail with the same UUID error. [Commit](https://github.com/open-webui/open-webui/commit/3c400952cbb30e8eb72652d83b2af2f75a3b9341)
> - 🎛️ **Side Chat permission switch.** The Allow Side Chat switch is now visible even when Temporary Chat is off, so administrators can configure the two permissions independently. [#33920](https://github.com/open-webui/open-webui/pull/33920)

### [v0.13.1](https://github.com/open-webui/open-webui/releases/tag/v0.13.1)
<sub>2026-11-08 · 15d ago</sub>

> **Added**
> - 🦾 **Coding agents as models.** On an Open Terminal that offers agents, coding agents such as Claude Code, Codex and Pi now appear in the model picker. You can chat with them or call them by voice, choose their reasoning effort and service tier, and approve their tool requests in the chat. Each conversation uses one agent, and agent chats cannot be regenerated, continued or edited and resent. If an agent's terminal goes away, its chats and new chats fall back to the default model and earlier replies keep the agent's name. Autocompletion in agent chats uses the task model, or is skipped when there is none. [#33843](https://github.com/open-webui/open-webui/pull/33843), [#33860](https://github.com/open-webui/open-webui/pull/33860), [#33880](https://github.com/open-webui/open-webui/pull/33880), [#33857](https://github.com/open-webui/open-webui/pull/33857)
> - 🪢 **Introducing Tether.** [Tether](https://github.com/open-webui/tether) is the new desktop companion app for macOS, Windows and Linux that ties your own computer to Open WebUI. Sign in once and your computer shows up under Your devices in the terminal menu, so models, coding agents and automations can work in your real files, repositories and tools, and you can reach them from any browser, including your phone. Tether connects out to Open WebUI, so there are no ports to open, its terminal output resumes after a dropped connection, and it delivers notifications to your desktop even when no Open WebUI page is open. It signs in with a renewable session that expires after 90 days without use by default, set with "SESSION_EXPIRES_IN".
> - 💸 **Much cheaper tool chats.** Chats that use tools now cost much less. Citation instructions, memory recall, the skills list and attached knowledge are no longer rewritten into the system prompt or your message on every tool round, so the start of the conversation stays the same between requests and providers can serve it from their prompt cache. Custom pipes see a different message layout as a result; see Context as hidden tool results under Changed. [#33852](https://github.com/open-webui/open-webui/issues/33852)
> - 🚦 **Auto tool permissions.** Administrators can now turn on Auto, a third tool permission mode next to Full access and Ask for approval (off by default). A review model checks each tool call and runs it right away only when it judges that no confirmation is needed. The review sends the tool, its arguments and your last few messages to the configured scoring API, and any call it cannot review, because of an error, a timeout or too much context, asks for approval.
> - 📚 **Full text for small files.** Files whose extracted text is shorter than a new threshold (50,000 characters by default, set with "RAG_FULL_TEXT_CHAR_THRESHOLD" or in the admin Documents settings) are now included in full instead of through retrieval. This applies both when Preload files adds the content to the conversation and when the model reads an attached file with its file search tool, and the file viewer shows when it happens.
> …

### [v0.13.0](https://github.com/open-webui/open-webui/releases/tag/v0.13.0)
<sub>2026-11-03 · 20d ago</sub>

> **Added**
> - 📑 **Tabbed workspace.** The Tabs button at the top of a chat now opens a workspace for files, multiple terminal sessions, artifacts, previews, voice calls and comments. Add tabs from the + menu, drag to reorder them, and create and save new files directly into the selected terminal. Keep the conversation and its working files together while coding, analyzing data or reviewing generated documents. [Commit](https://github.com/open-webui/open-webui/commit/2d7cf5ec99c3fa5c7ee48b91823fb8021b846cf3), [Commit](https://github.com/open-webui/open-webui/commit/5b58b1ebc03024fca1efd498aeabe4d9880dc3aa), [Commit](https://github.com/open-webui/open-webui/commit/a06aa230f75cc2d3512d1bca197a98f3c35da96f), [Commit](https://github.com/open-webui/open-webui/commit/cdc6feecd3769aac41844d81bd775dfb69b44912)
> - 🖥️ **Open Terminal Desktop tab for computer use.** Open the Desktop tab from the + menu to view and control the desktop provided by your connected Open Terminal, with mouse, keyboard, clipboard and audio support where available. With a model that can call its desktop tools, you can follow computer-use workflows in the same desktop and step in yourself: operate graphical apps, inspect generated documents or handle a step that needs manual input. Requires an Open Terminal connection with desktop support enabled. [Commit](https://github.com/open-webui/open-webui/commit/b51e68fbb3e641e7f9027f5164fcf6b0e111cf27), [Commit](https://github.com/open-webui/open-webui/commit/3bd0cdd0f3cc075420540462f2bf246c73236495), [Commit](https://github.com/open-webui/open-webui/commit/03401a6e331d25425533933da85d3e5496deca3f), [Commit](https://github.com/open-webui/open-webui/commit/6dd3cc216f63085d2a1105117c65064c3e0ca3b6)
> - 🌐 **Browser tab for browser use and web app testing.** Open websites and local development servers beside your chat, with navigation controls, multiple tabs and a mobile viewport. On a compatible Open Terminal connection, Chrome mode gives you and the model a shared browser session for browser automation: navigate sites, interact with forms and test the web apps the model builds. You can watch the work and interact with the page yourself; Proxy mode remains available for previews. Requires browser support on the selected terminal, and Chrome availability for browser-use tools. [Commit](https://github.com/open-webui/open-webui/commit/fbe69b01fd58a374211d348a28eb5988b11d41de), [Commit](https://github.com/open-webui/open-webui/commit/3bd0cdd0f3cc075420540462f2bf246c73236495), [Commit](https://github.com/open-webui/open-webui/commit/9260e312fb4238b504652eff0d8ca45445ca0821)
> - ↔️ **Full-width tabs.** On larger screens, expand the tabbed workspace to fill the chat area, with the main conversation kept as its own tab. Switch between the chat, code, browser and desktop with more room to work, or return to the side-by-side layout; your layout choice is remembered. [Commit](https://github.com/open-webui/open-webui/commit/09030d5dd2def4324d98c25f92cf54b1ec1844f1), [Commit](https://github.com/open-webui/open-webui/commit/1ce8616ab9587ca717015d5af9cb26ee4296311f)
> - 💻 **Open WebUI Desktop 0.1.x.** The separately installed app for macOS, Windows and Linux now focuses on setting up and running Open WebUI on your own computer, with optional llama.cpp local models. The 0.1.0–0.1.4 updates bring a slimmer interface, searchable settings, startup logs, optional automatic Desktop updates, start-to-tray controls and image copying and saving. They also improve screen sharing, knowledge folder uploads, Linux graphics and shortcuts, and NVIDIA/AMD local-model setup and updates. Use it for a managed local installation and local AI workflows. [Desktop changelog](https://github.com/open-webui/desktop/blob/v0.1.4/CHANGELOG.md), [Download v0.1.4](https://github.com/open-webui/desktop/releases/tag/v0.1.4)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [Merge pull request #33965 from open-webui/dev](https://github.com/open-webui/open-webui/commit/0666e59d26a4d056e0bacee41742486badd71cf8) | tjbck |
| 2026-11-17 | [fix: Temporary in the / menu does nothing on a new chat (#34609)](https://github.com/open-webui/open-webui/commit/dcde707f0f227900380ff37489ed3490368c33d1) | Classic298 |
| 2026-11-17 | [refac](https://github.com/open-webui/open-webui/commit/10be890bceab3584108fec9a121ec169b028c56d) | tjbck |
| 2026-11-17 | [refac](https://github.com/open-webui/open-webui/commit/a59b4099c63e41853503d2a1c7f52a69943632e1) | tjbck |
| 2026-11-17 | [doc: changelog](https://github.com/open-webui/open-webui/commit/c3dfec2b0dd9d4e5e5907e93ab312ebcf293309d) | tjbck |
| 2026-11-17 | [refac](https://github.com/open-webui/open-webui/commit/359b549c47f1f089d97877613131ce2d3522edab) | tjbck |
| 2026-11-17 | [doc: changelog](https://github.com/open-webui/open-webui/commit/02c39e9a0aa4621634ddefd3d3955fa96eccd568) | tjbck |
| 2026-11-17 | [doc: changelog](https://github.com/open-webui/open-webui/commit/34a32f0dbbe33360679f8e7f9bd4832df1542c5d) | tjbck |
| 2026-11-17 | [docs: update 0.13.4 changelog (#34603)](https://github.com/open-webui/open-webui/commit/bd0fa6d191af53f20abf605635368248fef9158b) | Classic298 |
| 2026-11-17 | [perf: PDF preview opens large files in seconds (#34602)](https://github.com/open-webui/open-webui/commit/bd5445a791bc3873bed0f5199d097b85c3aa6376) | Classic298 |

[See all commits ↗](https://github.com/open-webui/open-webui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/open-webui/open-webui.git
```
