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
| ⭐ **Stars** | 229.3k |
| 🍴 **Forks** | 31.2k |
| 🐞 **Open issues + PRs** | [4.2k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 74% · Rust 14% · MDX 9% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.4.2](https://github.com/anomalyco/opencode/releases/tag/v2.4.2) — 2026-11-26 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 748.8 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.4.2](https://github.com/anomalyco/opencode/releases/tag/v2.4.2)
<sub>2026-11-26 · today</sub>

> **Highlights**
> - **GPT-6.2 System Prompt**: GPT-6.2 Sol and Astra, and the `gpt-latest` aliases, use a system prompt written for GPT-6.2. ([#66297](https://github.com/anomalyco/opencode/pull/66297))
> - **OpenCode Go Onboarding Fix**: After you connect OpenCode, the model picker lists OpenCode Go first. ([#66363](https://github.com/anomalyco/opencode/pull/66363))
> - **Esc Takes Back Your Last Message**: If the composer is empty, stopping a response with Esc before the model has written anything or called a tool removes your message and puts it back in the composer, images included, so you can edit it and send again. ([#65505](https://github.com/anomalyco/opencode/pull/65505))
> **Upgrade notes**
> - **"Always allow" for a web fetch allows that site only.** It used to allow every URL. Approvals saved by earlier versions stay as they were. ([#66000](https://github.com/anomalyco/opencode/pull/66000))
> …

### [v2.4.1](https://github.com/anomalyco/opencode/releases/tag/v2.4.1)
<sub>2026-11-23 · 2d ago</sub>

> **Highlights**
> - **macOS 12 Session Fix**: OpenCode can save assistant messages again on the older SQLite version included with macOS 12. ([#65771](https://github.com/anomalyco/opencode/pull/65771))
> - **Config-Only Providers Show Their Models**: Providers you set up only in your config, such as Ollama, now show their models in `/models` without a `/connect` login. ([#65793](https://github.com/anomalyco/opencode/pull/65793))
> - **Unread `/btw` Answers**: When a side question finishes behind another side-panel tab, its tab shows an unread dot until you open it. ([#65821](https://github.com/anomalyco/opencode/pull/65821))
> **Core**
> **Improvements**
> …

### [v2.4.0](https://github.com/anomalyco/opencode/releases/tag/v2.4.0)
<sub>2026-11-23 · 3d ago</sub>

> **Highlights**
> - **Built-In Desktop Browser**: Import your sign-ins and browsing history from Chrome, Edge, Firefox or Safari, and add extensions from Chromium browsers or the Chrome and Edge stores. Everything stays in one persistent desktop profile: chat links open signed in, your tabs survive restarts and the agent can read and drive the same pages without you switching apps. ([#63002](https://github.com/anomalyco/opencode/pull/63002), [#65073](https://github.com/anomalyco/opencode/pull/65073))
> - **Automations**: Ask the agent to run a prompt, a script or a shell command on a timer, on a cron schedule or when an MCP server sends an event, and manage them with `/automation`. Set `"automations": false` in your config if you don't want them. ([#65296](https://github.com/anomalyco/opencode/pull/65296), [#65186](https://github.com/anomalyco/opencode/pull/65186))
> - **Generate Videos**: When a connected provider has a video model, the agent can make videos with `generate_video`. It keeps working while the video renders and saves the files into your workspace when they're ready. ([#63666](https://github.com/anomalyco/opencode/pull/63666), [#65664](https://github.com/anomalyco/opencode/pull/65664))
> - **New TUI Look**: The TUI's new designs are on by default, and the `opencode` theme is the new one. Pick `opencode-classic` in **Theme** to keep the previous colors. ([#64988](https://github.com/anomalyco/opencode/pull/64988))
> - **Windows Taskbar Status**: On Windows, the taskbar button shows session progress, counts sessions that need you and flashes when a permission or question is waiting. ([#65317](https://github.com/anomalyco/opencode/pull/65317), [#65318](https://github.com/anomalyco/opencode/pull/65318), [#65319](https://github.com/anomalyco/opencode/pull/65319))
> …

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · 8d ago</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · 8d ago</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [feat(app): show where automations run and which session they wake (#6…](https://github.com/anomalyco/opencode/commit/782125f72a60220a4896490be628d16be56ac1da) | neriousy |
| 2026-11-26 | [feat(desktop): add smooth scrolling setting on linux (#66622)](https://github.com/anomalyco/opencode/commit/c39ad3b75c8f8b0571305415f74172c2d7b6ba1f) | neriousy |
| 2026-11-26 | [fix(core): pass a plugin id in the session.update test (#66620)](https://github.com/anomalyco/opencode/commit/44159132a50051514e282053eb4b4654ae587213) | neriousy |
| 2026-11-26 | [fix(plugin): session.update silently ignores archived (#61036)](https://github.com/anomalyco/opencode/commit/3c019e91991a473ceb7bd8424660f2f405fc3170) | LuckUVeryX |
| 2026-11-26 | [fix(tui): draw text selections in theme colours (#65776)](https://github.com/anomalyco/opencode/commit/586fa9038aeb4bf442b3b16a55e8ece8248700fc) | neriousy |
| 2026-11-26 | [fix(app): ask before opening a folder from an opencode:// link (#65803)](https://github.com/anomalyco/opencode/commit/924b56024020f20fd1839e38bac8d87f4ac01dfb) | neriousy |
| 2026-11-26 | [fix(core): keep nested permission metadata JSON-encodable (#66391)](https://github.com/anomalyco/opencode/commit/b5ae67aecbcf982952147868356eb38093053142) | neriousy |
| 2026-11-26 | [fix(session-ui): show images tool calls return in the timeline (#66430)](https://github.com/anomalyco/opencode/commit/f91949daee3ee0b622cfae73ac72d15b9499351f) | neriousy |
| 2026-11-26 | [feat(app): add Copy submenu to session menus (#66576)](https://github.com/anomalyco/opencode/commit/6e0eda631780532d7f7111ff59bc41b4d970787b) | opencode-agent[bot] |
| 2026-11-26 | [fix(core): fall back to legacy when the MCP probe gets an HTTP 5xx (#…](https://github.com/anomalyco/opencode/commit/70e8a0f6f30bbe4077847a0ce0936c4b56458227) | neriousy |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
