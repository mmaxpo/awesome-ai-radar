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
| ⭐ **Stars** | 53.9k |
| 🍴 **Forks** | 3.8k |
| 🐞 **Open issues + PRs** | [495](https://github.com/vercel-labs/agent-browser/issues) |
| 💻 **Languages** | Rust 94% · TypeScript 4% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-01-11 |
| 📦 **Latest release** | [v0.44.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.44.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 39.7 MB |
| 🌐 **Website** | https://agent-browser.dev |

## 📦 Recent releases

### [v0.44.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.44.0)
<sub>2026-11-23 · yesterday</sub>

> **New Features**
> - Added a **Ladybird provider**: `-p ladybird` drives Ladybird over WebDriver, headless by default or with `--headed`. Safari and Ladybird share one local driver launcher, and the WebDriver client now honors `Content-Length`, so it no longer hangs on drivers that keep the connection open. Snapshots and refs stay Chrome-only, as with Safari (#2721)
> - Added **background tab controls**: `tab keep live [tab]` keeps a background tab running at full speed instead of throttled, `tab keep throttled` returns it to the default, and `tab keep frozen <tab>` pauses it until the agent switches back. The daemon unfreezes a tab before any command runs on it and when the session closes (#2624, #2627)
> - Added **right-click, middle-click, and modifier keys** to `click` and `dblclick` with `--button` and `--modifiers`. A double click now sends two full clicks (#2594)
> - **WebMCP announcements** now tell agents what the page's tools are and when to use them, list each tool as `[origin] name [frame]: description` with full descriptions for small catalogs, mark tools from other origins as cross-origin, and include a ready-to-run `webmcp invoke` command for the page's own tools. `webmcp invoke` also accepts the JSON input right after the tool name (#2606, #2591, #2720)
> - Added **feature flag overrides** to the `vercel` skill, renamed from `protected-vercel-deployments`. Agents set the Flags SDK override cookie so only their own browser sees a variant, instead of changing the flag for everyone on the environment (#2441)
> …

### [v0.43.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.43.0)
<sub>2026-11-12 · 12d ago</sub>

> **New Features**
> - Added **snapshot hints** for controls whose accessible name is empty or shared with another ref in the same snapshot. The hint follows the ref and lists the control's icon, image file, `data-testid`, `name` or `id`, and the text of the nearest row or list item (#2578)
> - Added a **Modern Web Guidance skill** that retrieves Chrome's guidance for a task and checks the built page in agent-browser (#2577)
> **Bug Fixes**
> - Fixed **commands on closed tabs** waiting for the timeout. A command whose tab closes before Chrome answers now fails with `Target closed: CDP session <id> detached` (#2576)
> - Fixed **recordings with an emulated device scale**, which now capture at full density by switching to screenshots when a screencast frame is below the page's scale (#2572)
> …

### [v0.42.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.42.0)
<sub>2026-11-10 · 15d ago</sub>

> **New Features**
> - Added **saved flows** (experimental): record a browser task once, then replay its requests. A run tries direct HTTP first, then the same request from the page, then a replay of the recorded commands, and saves the tier that worked. Runs send requests only to public addresses, and saving waits for in-flight requests and follows redirects to the end (#2236, #2397, #2432, #2433, #2444)
> - **MCP tools** now list only the shared arguments each tool uses (#2311)
> **Bug Fixes**
> - Fixed **session reuse and relaunch**, now decided in one place in the daemon. A connection target is kept only after an attach succeeds, and security settings persist across daemon restarts (#2396, #2418, #2429)
> - Fixed **Safari and iOS WebDriver sessions** being dropped (#2385)
> …

### [v0.41.2](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.2)
<sub>2026-11-03 · 21d ago</sub>

> **New Features**
> - Added **targeted skill references** with `skills get <name> --ref <ref>` and the MCP `agent_browser_skills_get` tool's `refs` argument, so agents can load one reference or template at a time (#2310)
> - Added **Chrome security warnings** when newer stable releases list CVE fixes, without blocking commands. Set `AGENT_BROWSER_NO_VERSION_CHECK=1` to skip the check (#2309)
> **Bug Fixes**
> - Fixed **session restarts** when commands omit or change timeout settings, preserving open pages and reusing the running daemon's default timeout for waits (#2288)
> - Fixed **bare `open`** dropping configured profiles and browser arguments and relaunching Chrome with a temporary profile (#2287)
> …

### [v0.41.1](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.1)
<sub>2026-11-01 · 24d ago</sub>

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
| 2026-11-25 | [Prepare v0.45.0 (#2748)](https://github.com/vercel-labs/agent-browser/commit/f0a98351ec920bd826b22c98dacf8414f04b9832) | lahfir |
| 2026-11-25 | [fix(iframe): resolve frames by selector and ref, and scope selectors,…](https://github.com/vercel-labs/agent-browser/commit/e20a97bde0eb187f6f572b529710705d3b9a490d) | Railly |
| 2026-11-25 | [fix(dashboard): forward editing shortcuts and bridge copy, cut and pa…](https://github.com/vercel-labs/agent-browser/commit/7b20c4939a1cb9b7383ea118b0ae9b07f18c6743) | Railly |
| 2026-11-25 | [fix(iframe): run eval in the selected frame and capture cross-origin …](https://github.com/vercel-labs/agent-browser/commit/58d313edb6a305e3235b8a9f38960f0ae6b9c779) | Railly |
| 2026-11-25 | [fix(iframe): label iframes by name in snapshots and align iframe anno…](https://github.com/vercel-labs/agent-browser/commit/8a78afb37728ccc2963a060ca6080e85334d91d0) | Railly |
| 2026-11-25 | [fix(state): collect storage without stalling, leaking focus, or hitti…](https://github.com/vercel-labs/agent-browser/commit/0536ca2a1b23e7a0ce16c81cfb623fc24122664e) | Railly |
| 2026-11-25 | [fix(state): show state list dates and state show counts, and keep spe…](https://github.com/vercel-labs/agent-browser/commit/20d0eff8a50d62e6bd4efa3b133873422cbf6dc7) | Railly |
| 2026-11-25 | [fix(dashboard): map live view pointer to the real frame, forward held…](https://github.com/vercel-labs/agent-browser/commit/7d6ff1bf3362c64dc6e34ac10aea81f3b32a35a7) | Railly |
| 2026-11-24 | [fix(firefox): double-click, POST reload, cdp-url, and Windows test he…](https://github.com/vercel-labs/agent-browser/commit/5759f6bb2cdf3d8cf0670b0996a8793972a4628e) | lahfir |
| 2026-11-24 | [feat(firefox): click with another button or held modifier keys (#2595)](https://github.com/vercel-labs/agent-browser/commit/06ea6d6a5299a0d815cb71e594590359d1ef0d59) | lahfir |

[See all commits ↗](https://github.com/vercel-labs/agent-browser/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/agent-browser.git
```
