# vercel-labs/agent-browser

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/vercel-labs/agent-browser)

> Browser automation CLI for AI agents

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Browser automation CLI built for AI agents |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 53.7k |
| 🍴 **Forks** | 3.8k |
| 🐞 **Open issues + PRs** | [556](https://github.com/vercel-labs/agent-browser/issues) |
| 💻 **Languages** | Rust 92% · TypeScript 5% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-01-11 |
| 📦 **Latest release** | [v0.44.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.44.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 36.9 MB |
| 🌐 **Website** | https://agent-browser.dev |

## 📦 Recent releases

### [v0.44.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.44.0)
<sub>2026-11-23 · today</sub>

> **New Features**
> - Added a **Ladybird provider**: `-p ladybird` drives Ladybird over WebDriver, headless by default or with `--headed`. Safari and Ladybird share one local driver launcher, and the WebDriver client now honors `Content-Length`, so it no longer hangs on drivers that keep the connection open. Snapshots and refs stay Chrome-only, as with Safari (#2721)
> - Added **background tab controls**: `tab keep live [tab]` keeps a background tab running at full speed instead of throttled, `tab keep throttled` returns it to the default, and `tab keep frozen <tab>` pauses it until the agent switches back. The daemon unfreezes a tab before any command runs on it and when the session closes (#2624, #2627)
> - Added **right-click, middle-click, and modifier keys** to `click` and `dblclick` with `--button` and `--modifiers`. A double click now sends two full clicks (#2594)
> - **WebMCP announcements** now tell agents what the page's tools are and when to use them, list each tool as `[origin] name [frame]: description` with full descriptions for small catalogs, mark tools from other origins as cross-origin, and include a ready-to-run `webmcp invoke` command for the page's own tools. `webmcp invoke` also accepts the JSON input right after the tool name (#2606, #2591, #2720)
> - Added **feature flag overrides** to the `vercel` skill, renamed from `protected-vercel-deployments`. Agents set the Flags SDK override cookie so only their own browser sees a variant, instead of changing the flag for everyone on the environment (#2441)
> …

### [v0.43.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.43.0)
<sub>2026-11-12 · 11d ago</sub>

> **New Features**
> - Added **snapshot hints** for controls whose accessible name is empty or shared with another ref in the same snapshot. The hint follows the ref and lists the control's icon, image file, `data-testid`, `name` or `id`, and the text of the nearest row or list item (#2578)
> - Added a **Modern Web Guidance skill** that retrieves Chrome's guidance for a task and checks the built page in agent-browser (#2577)
> **Bug Fixes**
> - Fixed **commands on closed tabs** waiting for the timeout. A command whose tab closes before Chrome answers now fails with `Target closed: CDP session <id> detached` (#2576)
> - Fixed **recordings with an emulated device scale**, which now capture at full density by switching to screenshots when a screencast frame is below the page's scale (#2572)
> …

### [v0.42.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.42.0)
<sub>2026-11-10 · 14d ago</sub>

> **New Features**
> - Added **saved flows** (experimental): record a browser task once, then replay its requests. A run tries direct HTTP first, then the same request from the page, then a replay of the recorded commands, and saves the tier that worked. Runs send requests only to public addresses, and saving waits for in-flight requests and follows redirects to the end (#2236, #2397, #2432, #2433, #2444)
> - **MCP tools** now list only the shared arguments each tool uses (#2311)
> **Bug Fixes**
> - Fixed **session reuse and relaunch**, now decided in one place in the daemon. A connection target is kept only after an attach succeeds, and security settings persist across daemon restarts (#2396, #2418, #2429)
> - Fixed **Safari and iOS WebDriver sessions** being dropped (#2385)
> …

### [v0.41.2](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.2)
<sub>2026-11-03 · 20d ago</sub>

> **New Features**
> - Added **targeted skill references** with `skills get <name> --ref <ref>` and the MCP `agent_browser_skills_get` tool's `refs` argument, so agents can load one reference or template at a time (#2310)
> - Added **Chrome security warnings** when newer stable releases list CVE fixes, without blocking commands. Set `AGENT_BROWSER_NO_VERSION_CHECK=1` to skip the check (#2309)
> **Bug Fixes**
> - Fixed **session restarts** when commands omit or change timeout settings, preserving open pages and reusing the running daemon's default timeout for waits (#2288)
> - Fixed **bare `open`** dropping configured profiles and browser arguments and relaunching Chrome with a temporary profile (#2287)
> …

### [v0.41.1](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.1)
<sub>2026-11-01 · 23d ago</sub>

> **Bug Fixes**
> - Fixed **cookie attributes** so `cookies set` honors `--http-only` and `--same-site`, preserves the existing aliases, and rejects unknown arguments (#2256)
> - Fixed **page error clearing** so `errors --clear` removes captured errors (#2253)
> - Fixed **MCP selector waits** so bare integer selectors return an error instead of becoming timed waits (#2254)
> - Fixed **plugin error redaction** so sensitive operations omit unsupported protocol values (#2255)
> - Fixed **invalid limit handling** so overflowing idle timeouts and invalid output limits produce warnings instead of overflowing or being silently ignored (#2250, #2258)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [Prepare v0.44.0 (#2722)](https://github.com/vercel-labs/agent-browser/commit/0a923358ea989d7602f0d06507ad3447c62ffe9b) | lahfir |
| 2026-11-23 | [fix(webmcp): show each tool's origin in announcements (#2720)](https://github.com/vercel-labs/agent-browser/commit/bf03eb13832d5817593df769203ed6c8b6f46b77) | Railly |
| 2026-11-23 | [refactor(settings): carry the restore key, save policy and checks onl…](https://github.com/vercel-labs/agent-browser/commit/1ee56cd2b7ce17629b1cf6cd119847a3364493a0) | Railly |
| 2026-11-23 | [feat(webdriver): add Ladybird provider (#2721)](https://github.com/vercel-labs/agent-browser/commit/dc987e0831b41417169647d0152101c7c363c328) | lahfir |
| 2026-11-23 | [fix(interaction): refuse fill, type, check, uncheck and select on pre…](https://github.com/vercel-labs/agent-browser/commit/3a83e3cfb25ab0b93ab546aedb755e0d70b5c3a3) | Railly |
| 2026-11-23 | [Version the OG image URL by card content (#2719)](https://github.com/vercel-labs/agent-browser/commit/e0d56f21bb81a7e72c6ea8550de00e091d2668ac) | ctate |
| 2026-11-23 | [Use the Vercel Labs lockup in the docs header (#2717)](https://github.com/vercel-labs/agent-browser/commit/c091f702a731499070f32f2f3136c5bcb8b0e60f) | ctate |
| 2026-11-23 | [Use the Vercel Labs OG card generator (#2718)](https://github.com/vercel-labs/agent-browser/commit/1af7c73eb04f33633e353d31b10eb29b53b84247) | ctate |
| 2026-11-21 | [fix(ci): enable WebMCP on Chrome 157+, unblock paused iframes under -…](https://github.com/vercel-labs/agent-browser/commit/d2dfc782ccdd79d25a9b4f0acced9321789cecb8) | Railly |
| 2026-11-21 | [feat(webmcp): announce page tools so agents use them (#2606)](https://github.com/vercel-labs/agent-browser/commit/1fde6b90e8f17474b2f122d4b4ce43a7fa0a6aa0) | Railly |

[See all commits ↗](https://github.com/vercel-labs/agent-browser/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/agent-browser.git
```
