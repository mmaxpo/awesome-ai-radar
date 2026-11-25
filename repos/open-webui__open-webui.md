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
| ⭐ **Stars** | 159.5k |
| 🍴 **Forks** | 23.1k |
| 🐞 **Open issues + PRs** | [214](https://github.com/open-webui/open-webui/issues) |
| 💻 **Languages** | Svelte 39% · Python 37% · JavaScript 16% · TypeScript 7% · CSS 2% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ollama` `ollama-webui` `llm` `webui` `self-hosted` `llm-ui` `llm-webui` `llms` `rag` `ai` `open-webui` `ui` `openai` `mcp` `openapi` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2023-10-06 |
| 📦 **Latest release** | [v0.13.5](https://github.com/open-webui/open-webui/releases/tag/v0.13.5) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 681.7 MB |
| 🌐 **Website** | https://openwebui.com |

## 📦 Recent releases

### [v0.13.5](https://github.com/open-webui/open-webui/releases/tag/v0.13.5)
<sub>2026-11-25 · today</sub>

> **Added**
> - **Folder workspaces.** Run your project’s tests in a terminal and try the app in a browser while your chat stays open beside them. Choose the computer and project directory once for the folder. Even in a shared folder, everyone can return to their own tabs and layout. If you used the standalone Open WebUI Computer (cptr) app, that workflow is now built into Open WebUI. [#34804](https://github.com/open-webui/open-webui/pull/34804), [#34805](https://github.com/open-webui/open-webui/pull/34805), [#34800](https://github.com/open-webui/open-webui/issues/34800), [#34803](https://github.com/open-webui/open-webui/issues/34803)
> - **Project instructions and skills.** Tell the assistant how your project works once in an `AGENTS.md` or `CLAUDE.md` file. Every new chat in that project folder reads those instructions. Connect the project machine with Open Terminal 0.18.0 or later and the assistant can also follow reusable project instructions called skills, run checks in your terminal and inspect the result in your browser tab.
> - **Long chat performance.** Sending a message was 34× faster in our 130 MB PostgreSQL test chat. The server accepted it in 0.32 seconds, down from 10.9, because it now saves just the messages that changed. Database writes fell from 533 MB to 2 KB per message. [#34689](https://github.com/open-webui/open-webui/pull/34689), [#34671](https://github.com/open-webui/open-webui/pull/34671), [#34688](https://github.com/open-webui/open-webui/issues/34688), [#34672](https://github.com/open-webui/open-webui/issues/34672), [#34674](https://github.com/open-webui/open-webui/issues/34674), [#34670](https://github.com/open-webui/open-webui/issues/34670), [#34646](https://github.com/open-webui/open-webui/issues/34646)
> - **Automatic model selection.** Put one router in the chat’s model picker and it can send coding questions to one model and writing requests to another. Admins choose text patterns or describe the kind of question each model should handle. If nothing matches, the router uses the first model on its list or picks one at random. [#34900](https://github.com/open-webui/open-webui/pull/34900), [#34895](https://github.com/open-webui/open-webui/pull/34895), [#34791](https://github.com/open-webui/open-webui/pull/34791), [#34796](https://github.com/open-webui/open-webui/pull/34796), [#34908](https://github.com/open-webui/open-webui/pull/34908), [#34662](https://github.com/open-webui/open-webui/pull/34662), [#34956](https://github.com/open-webui/open-webui/pull/34956), [#34957](https://github.com/open-webui/open-webui/pull/34957), [#34887](https://github.com/open-webui/open-webui/issues/34887), [#34786](https://github.com/open-webui/open-webui/issues/34786), [#34793](https://github.com/open-webui/open-webui/issues/34793), [#34897](https://github.com/open-webui/open-webui/issues/34897), [#34898](https://github.com/open-webui/open-webui/issues/34898), [#34466](https://github.com/open-webui/open-webui/discussions/34466), [#15996](https://github.com/open-webui/open-webui/discussions/15996)
> - **Citations beside the chat.** Hover over a source number for a quick excerpt, or click it to read the evidence beside the answer. You can compare passages from the same document, see how closely they match your question and jump to the cited PDF page when page information is available. [#34923](https://github.com/open-webui/open-webui/pull/34923), [#34836](https://github.com/open-webui/open-webui/pull/34836), [#34921](https://github.com/open-webui/open-webui/issues/34921), [#34828](https://github.com/open-webui/open-webui/issues/34828), [#34831](https://github.com/open-webui/open-webui/issues/34831), [#34832](https://github.com/open-webui/open-webui/issues/34832), [#34833](https://github.com/open-webui/open-webui/issues/34833), [#34913](https://github.com/open-webui/open-webui/issues/34913), [#34834](https://github.com/open-webui/open-webui/issues/34834), [#34829](https://github.com/open-webui/open-webui/issues/34829), [#20829](https://github.com/open-webui/open-webui/discussions/20829)
> …

### [v0.13.4](https://github.com/open-webui/open-webui/releases/tag/v0.13.4)
<sub>2026-11-17 · 8d ago</sub>

> **Added**
> - **Bring your own computer with Tether.** Tether turns your own computer into part of Open WebUI: models from Ollama, LM Studio or any OpenAI-compatible server, OpenAPI and MCP tool servers and Open Terminal servers that you add in the Tether app now show up just for you in the model selector, the Tools list of the + menu and the terminal menu of any Open WebUI you connect, from whatever device you open it on, and Open WebUI reaches them through Tether, so their addresses, commands and keys never leave your computer. This needs Tether 0.1.14 or later, or 0.1.16 for MCP servers, tool servers and terminals need "ENABLE_TOOL_SERVERS" turned on, and a Tether model whose ID matches a model already in Open WebUI stays hidden. Tether replaces Direct Connections. [#34397](https://github.com/open-webui/open-webui/issues/34397)
> - **Sandboxed agents on your own computer.** Tether 0.1.13 or later can lock the terminal on your computer into a sandbox, so models and coding agents work in your real files without reaching the rest of your machine: on macOS and supported Windows devices, Open Terminal and everything it launches, coding agents included, can only touch the one folder you pick, run offline unless you turn on Network access and accept no incoming connections, with no Docker, virtual machine or administrator setup needed. If the sandbox cannot be enforced, the terminal stays stopped instead of quietly running without it, and browser and desktop control stay off while it is on. Turn it on in Tether under Settings > Open Terminal > Sandbox.
> - **Local MCP servers through Tether.** Open WebUI can now use MCP servers that run as a local command over stdio, the way many MCP servers are distributed, by launching them on your computer through Tether 0.1.16 or later, with no proxy such as mcpo and no port to open. Add one in Tether under Settings > Integrations > Tools with its command, or connect an MCP server by its web address, and pick it from the Tools list of the + menu. Local commands run with your own account's access, outside Tether's workspace sandbox.
> - **A computer for every user.** With Terminals 0.4.0 or later connected, Open WebUI now hands out sandboxed computers on demand: anyone with Write access to the connection can create a terminal right from the terminal menu of the message input, pick whether everyone shares one machine or each user, chat or model gets its own, and set its image, CPU, memory, storage, network profile, environment variables, start directory and a setup script that, for example, clones a repository and installs its dependencies, without an administrator setting up each one. Terminals can be shared with users and groups and their instances started, stopped, restarted or deleted, a View files option opens any terminal's files without selecting it for the chat, System info shows how the setup script went, and those who manage a terminal can open the files and system info of other people's running instances. Start and Stop need Terminals 0.4.1 or later, the start directory and setup script need Open Terminal 0.17.7 or later in the terminal's image, and network profiles are the ones an administrator defined with "TERMINALS_NETWORK_PROFILES".
> - **Coding agents as chat models.** Coding agents now work much like any other model in the chat. Hermes, Antigravity, GitHub Copilot, Goose and Qwen Code join Codex, Claude Code, Cursor, Grok, OpenCode, Cline, Gemini CLI and Pi, and any other ACP agent added to Open Terminal with "OPEN_TERMINAL_ACP_AGENTS" works as well, once it is installed and signed in on the terminal. Auto for tool permissions now lets Codex, Claude Code and Grok approve routine actions themselves and pass on only what they escalate, and the reasoning effort in the advanced parameters now also applies to Claude Code, Pi and ACP agents that offer effort levels, such as OpenCode, which stop with an error when the chosen level is not offered for the model. Replies can now be regenerated and earlier messages edited, and a forked or cloned agent chat picks up where the original left off: Codex continues its own conversation from that point, other agents start over from the chat so far, and file changes the agent already made stay. Claude Code continues its own conversation too with the next Open Terminal release after 0.17.20 and until then asks you to update Open Terminal instead. The new agents and Auto for Claude Code and Grok need Open Terminal 0.17.19 or later, and effort for Claude Code, Pi and ACP agents needs 0.17.9 or later. [#34167](https://github.com/open-webui/open-webui/issues/34167)
> …

### [v0.13.3](https://github.com/open-webui/open-webui/releases/tag/v0.13.3)
<sub>2026-11-08 · 16d ago</sub>

> **Added**
> - 🦾 **Agents in automations.** The automation editor now lets you choose a terminal and working folder, then select a coding agent available there. Scheduled runs use that saved terminal and folder, and check that the terminal and agent are still available before starting. Agent automations send their results to a chat; channel destinations remain available for ordinary models. [Commit](https://github.com/open-webui/open-webui/commit/21fc016141c73a0e11b428c61bde20527bbc228a)
> - 📂 **Change terminal and folder during a chat.** You can now choose a different terminal or working folder after sending messages, including in temporary chats. Both controls remain disabled while a reply is being generated. [Commit](https://github.com/open-webui/open-webui/commit/a518ff1630b74ed6edd62538c5da4bb26cc6dd20)
> - 🇧🇷 **Brazilian Portuguese translations.** Added missing translations for terminal and folder controls, Git actions, spreadsheet editing, voice notes, tab shortcuts, notification sounds and tool settings. Updated the explanations for document retrieval, tool permissions and voice settings. [#33945](https://github.com/open-webui/open-webui/pull/33945)
> **Fixed**
> - 📂 **Files tabs follow terminal changes.** Switching a chat to another terminal now updates its open Files tabs to show that terminal's files, instead of leaving the previous terminal's folders on screen. With a terminal set to "Per chat", the Files tab also switches to the chat's own files after the first message. [#33954](https://github.com/open-webui/open-webui/pull/33954)
> …

### [v0.13.2](https://github.com/open-webui/open-webui/releases/tag/v0.13.2)
<sub>2026-11-08 · 17d ago</sub>

> **Fixed**
> - 🔓 **Chat over plain HTTP.** Opening Open WebUI over plain HTTP at a LAN or Docker address now loads new and existing chats instead of staying on a spinner with "crypto.randomUUID is not a function". [#33919](https://github.com/open-webui/open-webui/issues/33919)
> - 📝 **Comments and Markdown editing over plain HTTP.** Creating, replying to and editing comments, and editing Markdown files containing rendered blocks such as Mermaid diagrams or callouts, no longer fail with the same UUID error. [Commit](https://github.com/open-webui/open-webui/commit/3c400952cbb30e8eb72652d83b2af2f75a3b9341)
> - 🎛️ **Side Chat permission switch.** The Allow Side Chat switch is now visible even when Temporary Chat is off, so administrators can configure the two permissions independently. [#33920](https://github.com/open-webui/open-webui/pull/33920)

### [v0.13.1](https://github.com/open-webui/open-webui/releases/tag/v0.13.1)
<sub>2026-11-08 · 17d ago</sub>

> **Added**
> - 🦾 **Coding agents as models.** On an Open Terminal that offers agents, coding agents such as Claude Code, Codex and Pi now appear in the model picker. You can chat with them or call them by voice, choose their reasoning effort and service tier, and approve their tool requests in the chat. Each conversation uses one agent, and agent chats cannot be regenerated, continued or edited and resent. If an agent's terminal goes away, its chats and new chats fall back to the default model and earlier replies keep the agent's name. Autocompletion in agent chats uses the task model, or is skipped when there is none. [#33843](https://github.com/open-webui/open-webui/pull/33843), [#33860](https://github.com/open-webui/open-webui/pull/33860), [#33880](https://github.com/open-webui/open-webui/pull/33880), [#33857](https://github.com/open-webui/open-webui/pull/33857)
> - 🪢 **Introducing Tether.** [Tether](https://github.com/open-webui/tether) is the new desktop companion app for macOS, Windows and Linux that ties your own computer to Open WebUI. Sign in once and your computer shows up under Your devices in the terminal menu, so models, coding agents and automations can work in your real files, repositories and tools, and you can reach them from any browser, including your phone. Tether connects out to Open WebUI, so there are no ports to open, its terminal output resumes after a dropped connection, and it delivers notifications to your desktop even when no Open WebUI page is open. It signs in with a renewable session that expires after 90 days without use by default, set with "SESSION_EXPIRES_IN".
> - 💸 **Much cheaper tool chats.** Chats that use tools now cost much less. Citation instructions, memory recall, the skills list and attached knowledge are no longer rewritten into the system prompt or your message on every tool round, so the start of the conversation stays the same between requests and providers can serve it from their prompt cache. Custom pipes see a different message layout as a result; see Context as hidden tool results under Changed. [#33852](https://github.com/open-webui/open-webui/issues/33852)
> - 🚦 **Auto tool permissions.** Administrators can now turn on Auto, a third tool permission mode next to Full access and Ask for approval (off by default). A review model checks each tool call and runs it right away only when it judges that no confirmation is needed. The review sends the tool, its arguments and your last few messages to the configured scoring API, and any call it cannot review, because of an error, a timeout or too much context, asks for approval.
> - 📚 **Full text for small files.** Files whose extracted text is shorter than a new threshold (50,000 characters by default, set with "RAG_FULL_TEXT_CHAR_THRESHOLD" or in the admin Documents settings) are now included in full instead of through retrieval. This applies both when Preload files adds the content to the conversation and when the model reads an attached file with its file search tool, and the file viewer shows when it happens.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [Merge pull request #34613 from open-webui/dev](https://github.com/open-webui/open-webui/commit/926f826eaef6179c092a936eede6c7363e425975) | tjbck |
| 2026-11-25 | [fix: attaching a file without pandoc sometimes shows a raw error inst…](https://github.com/open-webui/open-webui/commit/7e5634d2086be4e87e3c7921b1421933ee489a9a) | Classic298 |
| 2026-11-25 | [chore: format](https://github.com/open-webui/open-webui/commit/bb51c01700757e04fb383e0fd5d35c7b5525e2a0) | tjbck |
| 2026-11-25 | [refac](https://github.com/open-webui/open-webui/commit/efcbd9c6d72ed3f643b8c8dc80e7b55b1a201755) | tjbck |
| 2026-11-25 | [refac](https://github.com/open-webui/open-webui/commit/1c2c3e794e36e33a5560797829e1b8d9eb5c9ea7) | tjbck |
| 2026-11-25 | [fix: deleting a note leaves its chat counted in admin analytics (#35059)](https://github.com/open-webui/open-webui/commit/18b9b449c77f61244dd027b7ce73ef2741bbaa1d) | Classic298 |
| 2026-11-25 | [fix: deleting a folder or all chats leaves their replies and sub-agen…](https://github.com/open-webui/open-webui/commit/cdf38c4a7205336cf3a2f1b701f09a68c8ae900a) | Classic298 |
| 2026-11-25 | [fix: deleting a folder with its chats leaves their sub-agent and time…](https://github.com/open-webui/open-webui/commit/1fcfc8a5cd78151166ef777de47b94e8b04e3205) | Classic298 |
| 2026-11-25 | [refac](https://github.com/open-webui/open-webui/commit/b0d5c67f76a47b2ca0ab969e29d8147a04248215) | tjbck |
| 2026-11-25 | [refac](https://github.com/open-webui/open-webui/commit/ee591b44b3c1d3d1a3d3e166547b9a5214038dab) | tjbck |

[See all commits ↗](https://github.com/open-webui/open-webui/commits)

## ⬇️ Get it

```bash
git clone https://github.com/open-webui/open-webui.git
```
