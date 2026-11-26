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
| ⭐ **Stars** | 54.1k |
| 🍴 **Forks** | 3.8k |
| 🐞 **Open issues + PRs** | [505](https://github.com/vercel-labs/agent-browser/issues) |
| 💻 **Languages** | Rust 94% · TypeScript 4% · JavaScript 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-01-11 |
| 📦 **Latest release** | [v0.45.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.45.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 40.9 MB |
| 🌐 **Website** | https://agent-browser.dev |

## 📦 Recent releases

### [v0.45.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.45.0)
<sub>2026-11-25 · today</sub>

> **New Features**
> - Added a **Firefox engine** driven over WebDriver BiDi: pass `--engine firefox` (or set `AGENT_BROWSER_ENGINE=firefox`) with Firefox 150 or newer to drive a local Firefox install with snapshots and `@eN` refs across open and closed shadow roots and iframes, `find` locators, shared form preconditions and error codes (`fill`, `type`, `check`, `uncheck`, `select --by`), right-click, middle-click, and modifier keys (`--button`, `--modifiers`), network routes and HAR capture, `--allowed-domains`, downloads, viewport, media, geolocation, header, and offline emulation, isolated windows, `--pin-tab`, screenshots, PDF export, and dashboard live view (#2205, #2206, #2207, #2208, #2595, #2633)
> - Added **Firefox attach mode**: connect to an existing Firefox instance over WebDriver BiDi with `--cdp` or `connect` (including `ws://.../session?devtools=<port>` endpoints), apply live settings in place, and detach on `close` without closing the running browser (#2227)
> **Bug Fixes**
> - Fixed **keyboard `keydown`, `keyup`, and `press` modifier handling**: `keydown` and `keyup` now send `code`, `keyCode`, `location`, and printable text and carry held modifiers across subsequent keyboard, mouse, and flow-recorder commands. `press` applies US-layout Shift mapping, suppresses printable text for Alt, Control, and Meta chords, and dispatches modifier key events for chords not already held (#2734)
> - Fixed **saved flow host rules, write consent, deadlines, and result shaping**: saved host rules now match hostnames regardless of case or a trailing DNS root dot, non-`POST` requests carrying GraphQL queries require write declarations and consent, HTTP preflight cookie and route lookups and in-page fetches stop at the run deadline, empty result lists no longer fail `--fields` or `--where`, and `--limit` shapes only retained rows (#2735)
> …

### [v0.44.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.44.0)
<sub>2026-11-23 · 2d ago</sub>

> **New Features**
> - Added a **Ladybird provider**: `-p ladybird` drives Ladybird over WebDriver, headless by default or with `--headed`. Safari and Ladybird share one local driver launcher, and the WebDriver client now honors `Content-Length`, so it no longer hangs on drivers that keep the connection open. Snapshots and refs stay Chrome-only, as with Safari (#2721)
> - Added **background tab controls**: `tab keep live [tab]` keeps a background tab running at full speed instead of throttled, `tab keep throttled` returns it to the default, and `tab keep frozen <tab>` pauses it until the agent switches back. The daemon unfreezes a tab before any command runs on it and when the session closes (#2624, #2627)
> - Added **right-click, middle-click, and modifier keys** to `click` and `dblclick` with `--button` and `--modifiers`. A double click now sends two full clicks (#2594)
> - **WebMCP announcements** now tell agents what the page's tools are and when to use them, list each tool as `[origin] name [frame]: description` with full descriptions for small catalogs, mark tools from other origins as cross-origin, and include a ready-to-run `webmcp invoke` command for the page's own tools. `webmcp invoke` also accepts the JSON input right after the tool name (#2606, #2591, #2720)
> - Added **feature flag overrides** to the `vercel` skill, renamed from `protected-vercel-deployments`. Agents set the Flags SDK override cookie so only their own browser sees a variant, instead of changing the flag for everyone on the environment (#2441)
> …

### [v0.43.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.43.0)
<sub>2026-11-12 · 13d ago</sub>

> **New Features**
> - Added **snapshot hints** for controls whose accessible name is empty or shared with another ref in the same snapshot. The hint follows the ref and lists the control's icon, image file, `data-testid`, `name` or `id`, and the text of the nearest row or list item (#2578)
> - Added a **Modern Web Guidance skill** that retrieves Chrome's guidance for a task and checks the built page in agent-browser (#2577)
> **Bug Fixes**
> - Fixed **commands on closed tabs** waiting for the timeout. A command whose tab closes before Chrome answers now fails with `Target closed: CDP session <id> detached` (#2576)
> - Fixed **recordings with an emulated device scale**, which now capture at full density by switching to screenshots when a screencast frame is below the page's scale (#2572)
> …

### [v0.42.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.42.0)
<sub>2026-11-10 · 16d ago</sub>

> **New Features**
> - Added **saved flows** (experimental): record a browser task once, then replay its requests. A run tries direct HTTP first, then the same request from the page, then a replay of the recorded commands, and saves the tier that worked. Runs send requests only to public addresses, and saving waits for in-flight requests and follows redirects to the end (#2236, #2397, #2432, #2433, #2444)
> - **MCP tools** now list only the shared arguments each tool uses (#2311)
> **Bug Fixes**
> - Fixed **session reuse and relaunch**, now decided in one place in the daemon. A connection target is kept only after an attach succeeds, and security settings persist across daemon restarts (#2396, #2418, #2429)
> - Fixed **Safari and iOS WebDriver sessions** being dropped (#2385)
> …

### [v0.41.2](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.2)
<sub>2026-11-03 · 22d ago</sub>

> **New Features**
> - Added **targeted skill references** with `skills get <name> --ref <ref>` and the MCP `agent_browser_skills_get` tool's `refs` argument, so agents can load one reference or template at a time (#2310)
> - Added **Chrome security warnings** when newer stable releases list CVE fixes, without blocking commands. Set `AGENT_BROWSER_NO_VERSION_CHECK=1` to skip the check (#2309)
> **Bug Fixes**
> - Fixed **session restarts** when commands omit or change timeout settings, preserving open pages and reusing the running daemon's default timeout for waits (#2288)
> - Fixed **bare `open`** dropping configured profiles and browser arguments and relaunching Chrome with a temporary profile (#2287)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(launch): report relaunchedBrowser when the settings pass closed t…](https://github.com/vercel-labs/agent-browser/commit/a67ba089fec5fbfec07346aebad11666463d9799) | Railly |
| 2026-11-26 | [fix(iframe): fall back to top-level frame selector and report coverin…](https://github.com/vercel-labs/agent-browser/commit/a94b9f4a1e5c20195a06ec951347bfdc546c139f) | Railly |
| 2026-11-26 | [fix(tracing): stop only the recorder a command started (#2763)](https://github.com/vercel-labs/agent-browser/commit/6e857a8a4fcf6f473a04c70ed83fa987e1a8619e) | Railly |
| 2026-11-25 | [Prepare v0.45.0 (#2748)](https://github.com/vercel-labs/agent-browser/commit/f0a98351ec920bd826b22c98dacf8414f04b9832) | lahfir |
| 2026-11-25 | [fix(iframe): resolve frames by selector and ref, and scope selectors,…](https://github.com/vercel-labs/agent-browser/commit/e20a97bde0eb187f6f572b529710705d3b9a490d) | Railly |
| 2026-11-25 | [fix(dashboard): forward editing shortcuts and bridge copy, cut and pa…](https://github.com/vercel-labs/agent-browser/commit/7b20c4939a1cb9b7383ea118b0ae9b07f18c6743) | Railly |
| 2026-11-25 | [fix(iframe): run eval in the selected frame and capture cross-origin …](https://github.com/vercel-labs/agent-browser/commit/58d313edb6a305e3235b8a9f38960f0ae6b9c779) | Railly |
| 2026-11-25 | [fix(iframe): label iframes by name in snapshots and align iframe anno…](https://github.com/vercel-labs/agent-browser/commit/8a78afb37728ccc2963a060ca6080e85334d91d0) | Railly |
| 2026-11-25 | [fix(state): collect storage without stalling, leaking focus, or hitti…](https://github.com/vercel-labs/agent-browser/commit/0536ca2a1b23e7a0ce16c81cfb623fc24122664e) | Railly |
| 2026-11-25 | [fix(state): show state list dates and state show counts, and keep spe…](https://github.com/vercel-labs/agent-browser/commit/20d0eff8a50d62e6bd4efa3b133873422cbf6dc7) | Railly |

[See all commits ↗](https://github.com/vercel-labs/agent-browser/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/agent-browser.git
```
