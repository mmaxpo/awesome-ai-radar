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
| ⭐ **Stars** | 229.1k |
| 🍴 **Forks** | 31.2k |
| 🐞 **Open issues + PRs** | [4.2k](https://github.com/anomalyco/opencode/issues) |
| 💻 **Languages** | TypeScript 74% · Rust 14% · MDX 9% · CSS 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2025-04-30 |
| 📦 **Latest release** | [v2.4.1](https://github.com/anomalyco/opencode/releases/tag/v2.4.1) — 2026-11-23 |
| 🌿 **Default branch** | `dev` |
| 💾 **Size** | 746.1 MB |
| 🌐 **Website** | https://opencode.ai |

## 📦 Recent releases

### [v2.4.1](https://github.com/anomalyco/opencode/releases/tag/v2.4.1)
<sub>2026-11-23 · yesterday</sub>

> **Highlights**
> - **macOS 12 Session Fix**: OpenCode can save assistant messages again on the older SQLite version included with macOS 12. ([#65771](https://github.com/anomalyco/opencode/pull/65771))
> - **Config-Only Providers Show Their Models**: Providers you set up only in your config, such as Ollama, now show their models in `/models` without a `/connect` login. ([#65793](https://github.com/anomalyco/opencode/pull/65793))
> - **Unread `/btw` Answers**: When a side question finishes behind another side-panel tab, its tab shows an unread dot until you open it. ([#65821](https://github.com/anomalyco/opencode/pull/65821))
> **Core**
> **Improvements**
> …

### [v2.4.0](https://github.com/anomalyco/opencode/releases/tag/v2.4.0)
<sub>2026-11-23 · 2d ago</sub>

> **Highlights**
> - **Built-In Desktop Browser**: Import your sign-ins and browsing history from Chrome, Edge, Firefox or Safari, and add extensions from Chromium browsers or the Chrome and Edge stores. Everything stays in one persistent desktop profile: chat links open signed in, your tabs survive restarts and the agent can read and drive the same pages without you switching apps. ([#63002](https://github.com/anomalyco/opencode/pull/63002), [#65073](https://github.com/anomalyco/opencode/pull/65073))
> - **Automations**: Ask the agent to run a prompt, a script or a shell command on a timer, on a cron schedule or when an MCP server sends an event, and manage them with `/automation`. Set `"automations": false` in your config if you don't want them. ([#65296](https://github.com/anomalyco/opencode/pull/65296), [#65186](https://github.com/anomalyco/opencode/pull/65186))
> - **Generate Videos**: When a connected provider has a video model, the agent can make videos with `generate_video`. It keeps working while the video renders and saves the files into your workspace when they're ready. ([#63666](https://github.com/anomalyco/opencode/pull/63666), [#65664](https://github.com/anomalyco/opencode/pull/65664))
> - **New TUI Look**: The TUI's new designs are on by default, and the `opencode` theme is the new one. Pick `opencode-classic` in **Theme** to keep the previous colors. ([#64988](https://github.com/anomalyco/opencode/pull/64988))
> - **Windows Taskbar Status**: On Windows, the taskbar button shows session progress, counts sessions that need you and flashes when a permission or question is waiting. ([#65317](https://github.com/anomalyco/opencode/pull/65317), [#65318](https://github.com/anomalyco/opencode/pull/65318), [#65319](https://github.com/anomalyco/opencode/pull/65319))
> …

### [v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2)
<sub>2026-11-18 · 7d ago</sub>

> **Highlights**
> - **GPT-6.2 Prompt Caching**: GPT-6.2 models don't cache a system prompt sent in the Responses `instructions` field, so every step re-billed it as uncached input. OpenCode now sends it as a leading developer message on every Responses route, including OpenAI (API key and ChatGPT sign-in), GitHub Copilot, Zen, Azure and OpenRouter, so it is cached from the second step on. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> **Core**
> **Bug fixes**
> - Fixed GPT-6.2 models re-billing the system prompt as uncached input on every step. On GitHub Copilot `gpt-6.2-sol`, uncached input per step dropped from about 14,000 tokens to 3. Compaction through `/responses/compact` now reads the same cached prefix. ([#64542](https://github.com/anomalyco/opencode/pull/64542), [#64544](https://github.com/anomalyco/opencode/pull/64544))
> - `webfetch` structured output no longer repeats the `url` and `format` it was called with. ([#64534](https://github.com/anomalyco/opencode/pull/64534))

### [v2.3.1](https://github.com/anomalyco/opencode/releases/tag/v2.3.1)
<sub>2026-11-18 · 7d ago</sub>

> **Highlights**
> - **Timed-Out Shell Commands Keep Running**: A shell command still running when its timeout expires now moves to the background instead of being killed, so long builds and test runs finish and report back. A foreground `timeout: 0` now means the default 120 seconds. ([#63699](https://github.com/anomalyco/opencode/pull/63699))
> - **Compaction Without the Wait**: As a session nears automatic compaction, the summary is now written in the background, so your next prompt doesn't pause for it. Set `compaction.background: false` to turn it off; a background summary that ends up unused still costs tokens. ([#64290](https://github.com/anomalyco/opencode/pull/64290))
> - **GPT 6.2 with ChatGPT Sign-In**: GPT 6.2 Sol and GPT 6.2 Astra, plus their fast variants, now show up in the model picker when you sign in with ChatGPT. ([#64508](https://github.com/anomalyco/opencode/pull/64508))
> - **Update Plugins from Settings**: Open **Settings › Extensions**, click **Check for updates**, then **Update** on any plugin with a new version. ([#64511](https://github.com/anomalyco/opencode/pull/64511))
> - **Comment on Selected Code**: Selecting code in diff and file viewers now just selects it, so you can copy it, and an **Add comment** toolbar appears beside the selection. ([#64410](https://github.com/anomalyco/opencode/pull/64410))
> …

### [v1.19.6](https://github.com/anomalyco/opencode/releases/tag/v1.19.6)
<sub>2026-11-17 · 8d ago</sub>

> **Desktop**
> **Improvements**
> - OpenCode 1 now offers the upgrade to OpenCode 2.0. OpenCode 2 downloads in the background and installs only when you choose: Restart to upgrade, Upgrade on quit, or Later. Your sessions, projects, and settings are kept. Plugins made for OpenCode 1 need an update.
> **Core**
> **Bugfixes**
> - Sessions with many images no longer send oversized requests. When the images in a session's history pass 25 MiB, the oldest are replaced with a placeholder.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [test(core): drop redundant core tests (#66387)](https://github.com/anomalyco/opencode/commit/1b297d1a4958db26b5b4082ff13eef01d20eaaef) | neriousy |
| 2026-11-25 | [fix(site): point the legal history's Nov 25 entries at dev's commit (…](https://github.com/anomalyco/opencode/commit/ad4ed1d41df1d131754af98de783d74426481e0c) | adamdotdevin |
| 2026-11-25 | [docs(site): publish the updated Terms of Use and the Refund Policy (#…](https://github.com/anomalyco/opencode/commit/2cd57b2f8bceeae79c4dabdce4a5ee111ce516c9) | adamdotdevin |
| 2026-11-25 | [fix(core): expand ~\ in session move destinations on Windows (#66269)](https://github.com/anomalyco/opencode/commit/7b8a065e29ad493ff5125356c1136b472b482805) | shaojunying |
| 2026-11-25 | [fix(core): keep published MCP OAuth resource over configured query (#…](https://github.com/anomalyco/opencode/commit/6d2cb07f17e6acd17cd7560adc189281f186a237) | neriousy |
| 2026-11-25 | [fix(util): keep a final empty + line in an added file (#66378)](https://github.com/anomalyco/opencode/commit/68c244f40beed99554738278c3c6a71b97999e4c) | neriousy |
| 2026-11-25 | [feat(app): show archived sessions dimmed in Search sessions (#66356)](https://github.com/anomalyco/opencode/commit/45277af6cf203c9d9b30ad5dd8f10d8cc1d6bb5e) | opencode-agent[bot] |
| 2026-11-25 | [fix(session-ui): open file tree position menu with Shift+F10 (#66372)](https://github.com/anomalyco/opencode/commit/fd3c9c454f757b56c8ecec17b1df83d92be36027) | usrnk1 |
| 2026-11-25 | [fix(tui): keep the model picker responsive with large catalogs (#66370)](https://github.com/anomalyco/opencode/commit/ea8aa5b05ef49af86d6c78dad0a19e2877e034e0) | neriousy |
| 2026-11-25 | [fix(tui): list every provider of a just-connected integration (#66363)](https://github.com/anomalyco/opencode/commit/d06f869560b894e23400d88d1afa765cb04381d6) | vimtor |

[See all commits ↗](https://github.com/anomalyco/opencode/commits)

## ⬇️ Get it

```bash
git clone https://github.com/anomalyco/opencode.git
```
