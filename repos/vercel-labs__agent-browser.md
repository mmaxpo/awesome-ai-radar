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
| ⭐ **Stars** | 53.3k |
| 🍴 **Forks** | 3.7k |
| 🐞 **Open issues + PRs** | [576](https://github.com/vercel-labs/agent-browser/issues) |
| 💻 **Languages** | Rust 92% · TypeScript 6% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-01-11 |
| 📦 **Latest release** | [v0.43.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.43.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 36.3 MB |
| 🌐 **Website** | https://agent-browser.dev |

## 📦 Recent releases

### [v0.43.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.43.0)
<sub>2026-11-12 · 9d ago</sub>

> **New Features**
> - Added **snapshot hints** for controls whose accessible name is empty or shared with another ref in the same snapshot. The hint follows the ref and lists the control's icon, image file, `data-testid`, `name` or `id`, and the text of the nearest row or list item (#2578)
> - Added a **Modern Web Guidance skill** that retrieves Chrome's guidance for a task and checks the built page in agent-browser (#2577)
> **Bug Fixes**
> - Fixed **commands on closed tabs** waiting for the timeout. A command whose tab closes before Chrome answers now fails with `Target closed: CDP session <id> detached` (#2576)
> - Fixed **recordings with an emulated device scale**, which now capture at full density by switching to screenshots when a screencast frame is below the page's scale (#2572)
> …

### [v0.42.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.42.0)
<sub>2026-11-10 · 12d ago</sub>

> **New Features**
> - Added **saved flows** (experimental): record a browser task once, then replay its requests. A run tries direct HTTP first, then the same request from the page, then a replay of the recorded commands, and saves the tier that worked. Runs send requests only to public addresses, and saving waits for in-flight requests and follows redirects to the end (#2236, #2397, #2432, #2433, #2444)
> - **MCP tools** now list only the shared arguments each tool uses (#2311)
> **Bug Fixes**
> - Fixed **session reuse and relaunch**, now decided in one place in the daemon. A connection target is kept only after an attach succeeds, and security settings persist across daemon restarts (#2396, #2418, #2429)
> - Fixed **Safari and iOS WebDriver sessions** being dropped (#2385)
> …

### [v0.41.2](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.2)
<sub>2026-11-03 · 18d ago</sub>

> **New Features**
> - Added **targeted skill references** with `skills get <name> --ref <ref>` and the MCP `agent_browser_skills_get` tool's `refs` argument, so agents can load one reference or template at a time (#2310)
> - Added **Chrome security warnings** when newer stable releases list CVE fixes, without blocking commands. Set `AGENT_BROWSER_NO_VERSION_CHECK=1` to skip the check (#2309)
> **Bug Fixes**
> - Fixed **session restarts** when commands omit or change timeout settings, preserving open pages and reusing the running daemon's default timeout for waits (#2288)
> - Fixed **bare `open`** dropping configured profiles and browser arguments and relaunching Chrome with a temporary profile (#2287)
> …

### [v0.41.1](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.1)
<sub>2026-11-01 · 20d ago</sub>

> **Bug Fixes**
> - Fixed **cookie attributes** so `cookies set` honors `--http-only` and `--same-site`, preserves the existing aliases, and rejects unknown arguments (#2256)
> - Fixed **page error clearing** so `errors --clear` removes captured errors (#2253)
> - Fixed **MCP selector waits** so bare integer selectors return an error instead of becoming timed waits (#2254)
> - Fixed **plugin error redaction** so sensitive operations omit unsupported protocol values (#2255)
> - Fixed **invalid limit handling** so overflowing idle timeouts and invalid output limits produce warnings instead of overflowing or being silently ignored (#2250, #2258)
> …

### [v0.41.0](https://github.com/vercel-labs/agent-browser/releases/tag/v0.41.0)
<sub>2026-10-29 · 24d ago</sub>

> **Breaking Changes**
> - **`@agent-browser/eve` tools now come from the MCP tool catalog.** The extension exposes the CLI's MCP tools instead of 21 hand-written ones, so tool names and inputs change: `navigate` is `open`, `evaluate` is `eval`, `press_key` is `press`, `select_option` is `select`, `set_checked` is `check` and `uncheck`, `get` is `get_text`, `get_url` and the other `get_*` tools, `tabs` is the `tab_*` tools, and `wait_for` is the `wait_*` tools. The same names apply to `@agent-browser/eve/tools` overrides. The sandbox needs agent-browser 0.41, which the extension installs by default (#2241)
> **New Features**
> - Added **`agent-browser mcp call <tool> '<json>'`** to run one MCP tool without a stdio session and print its result as JSON with the agent-browser version, for runtimes that cannot keep a process open between tool calls (#2238)
> - Added **`@agent-browser/sandbox/mcp-tools.json`**, every MCP tool with its title, description, input schema, annotations and profiles, generated from the CLI and checked by a test (#2240)
> **Improvements**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(ci): enable WebMCP on Chrome 157+, unblock paused iframes under -…](https://github.com/vercel-labs/agent-browser/commit/d2dfc782ccdd79d25a9b4f0acced9321789cecb8) | Railly |
| 2026-11-21 | [feat(webmcp): announce page tools so agents use them (#2606)](https://github.com/vercel-labs/agent-browser/commit/1fde6b90e8f17474b2f122d4b4ce43a7fa0a6aa0) | Railly |
| 2026-11-21 | [fix(cli): reject unmet preconditions in upload, har stop, diff snapsh…](https://github.com/vercel-labs/agent-browser/commit/bb034f384c838a1754fbcfb2095766cbcabb2c09) | Railly |
| 2026-11-21 | [test(native): serialize encryption-key and HOME mutation behind one e…](https://github.com/vercel-labs/agent-browser/commit/5aad200e67ee7c4ca170c97907d7a2ab4d199eb4) | Railly |
| 2026-11-21 | [fix(mcp): keep tool argument values from being read as CLI flags (#2681)](https://github.com/vercel-labs/agent-browser/commit/45d8c11ddc1289dc0644da483f3d3825e5bd3f15) | Railly |
| 2026-11-21 | [test: fix Windows CI failures in session settings and pin-tab tests (…](https://github.com/vercel-labs/agent-browser/commit/a7e41ff16a2be5daca4eccef71f3a97a34352bc1) | Railly |
| 2026-11-21 | [fix(daemon): carry action warnings out of band instead of in response…](https://github.com/vercel-labs/agent-browser/commit/07883ddbc0fd7649e5ea545ed76a04e020ab5393) | Railly |
| 2026-11-20 | [fix(snapshot): ref native controls with non-interactive roles, pierce…](https://github.com/vercel-labs/agent-browser/commit/343602553a26a44a9eb9393f99f1dd009d39ae8f) | Railly |
| 2026-11-20 | [fix(session): keep the session setup across relaunch and new tabs, wi…](https://github.com/vercel-labs/agent-browser/commit/b72a381d0e30fc750c004587d6744182b65f95f9) | Railly |
| 2026-11-20 | [fix(refs): reject refs issued for a replaced document (#2685)](https://github.com/vercel-labs/agent-browser/commit/4605d82cfc20dbd051f57a631b5b7130e32141a5) | Railly |

[See all commits ↗](https://github.com/vercel-labs/agent-browser/commits)

## ⬇️ Get it

```bash
git clone https://github.com/vercel-labs/agent-browser.git
```
