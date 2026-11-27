# browser-use/browser-use

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/browser-use/browser-use)

> Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | Python library for AI browser agents |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 122.2k |
| 🍴 **Forks** | 13.7k |
| 🐞 **Open issues + PRs** | [587](https://github.com/browser-use/browser-use/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llm` `ai-agents` `ai-tools` `browser-automation` `python` `browser-use` `playwright` `browser-agent` `cdp` `cloud-browser` `computer-use` `headless-browser` `mcp` `remote-browser` `stealth-browser` `web-automation` `web-scraping` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2024-10-31 |
| 📦 **Latest release** | [1.0.9](https://github.com/browser-use/browser-use/releases/tag/1.0.9) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 42.4 MB |
| 🌐 **Website** | https://browser-use.com |

## 📦 Recent releases

### [1.0.9](https://github.com/browser-use/browser-use/releases/tag/1.0.9) — browser-use 1.0.9
<sub>2026-11-26 · today</sub>

> `pip install 'browser-use==1.0.9'`
> - `rotate_proxy(country=None)`: the same Browser Use cloud browser gets a new exit IP, and its tabs, cookies and logins stay. It works over the browser's own connection with no API key; the API is only a fallback. The agent is pointed to it only when a page is a block for its IP, at most once per site. For a site that serves one country (.ru, .de, .co.uk, .kr), it's told to use an exit in that country. On 11 sites that block cloud browsers, the pass rate went from 48% to 62% (#6537, #6540).
> - `rotate_proxy()` now fails clearly when the cloud reports no new exit IP. A `Browser(cdp_url=...)` on any browser-use.com host counts as a cloud browser (#6540).
> - Claude prompt caching now works on every route: `openrouter:anthropic/...`, `bedrock:` Claude models, and `ChatOpenAI(..., base_url='https://openrouter.ai/api/v1')`. Before this, every step re-billed the whole prompt there (cache_read was always 0). Bedrock is covered by unit tests only and wasn't tested live (#6546, fixes #6543).
> PRs: https://github.com/browser-use/browser-use/pull/6540, https://github.com/browser-use/browser-use/pull/6546

### [1.0.8](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — browser-use 1.0.8
<sub>2026-11-22 · 5d ago</sub>

> `pip install 'browser-use==1.0.8'`
> - The judge asks as one more turn of the run, so the provider reads the run from its cache instead of billing the trace again. It returns the same verdict fields, gotchas included (#6457).
> - No API key over SSH or on a headless machine: the run prints a link and a code to approve on any device, then continues (#6427).
> - DeepSeek and Qwen in thinking mode: when the model refuses the forced final call at the step limit, the agent asks again without forcing, so the run returns its answer (#6453).
> - `bu.type` never prints a password field's value (#6455).
> - `Browser(cdp_url=...)` attaches the one page already open instead of a new blank tab (#6456).
> …

### [1.0.8rc1](https://github.com/browser-use/browser-use/releases/tag/1.0.8rc1) — 1.0.8rc1: release candidate for 1.0.8 _(pre-release)_
<sub>2026-11-20 · 6d ago</sub>

> `pip install 'browser-use==1.0.8rc1'`
> - The judge asks as one more turn of the run, so the provider reads the run from its cache instead of billing the trace again. It returns the same verdict fields, gotchas included (#6457).
> - No API key over SSH or on a headless machine: the run prints a link and a code to approve on any device, then continues (#6427).
> - DeepSeek and Qwen in thinking mode: when the model refuses the forced final call at the step limit, the agent asks again without forcing, so the run returns its answer (#6453).
> - `bu.type` never prints a password field's value (#6455).
> - `Browser(cdp_url=...)` attaches the one page already open instead of a new blank tab (#6456).
> …

### [1.0.7](https://github.com/browser-use/browser-use/releases/tag/1.0.7) — browser-use 1.0.7
<sub>2026-11-20 · 6d ago</sub>

> `pip install 'browser-use==1.0.7'`
> - **MCP calls no longer time out at 60 s.** A long `browser_exec` now replies within 50 s with the output so far, so Cursor and other clients with a 60 s limit get a result instead of `Request timed out`. The cell keeps running, and calling `browser_exec` again with empty code returns the rest. Calls under 50 s reply exactly as before (#6477).
> - README: Browser Use for enterprises, and the Cloud API key link is back in the Python quickstart (#6442, #6422).
> - Skills, README, CLI and MCP ask coding agents for integration feedback (#6454).

### [1.0.6](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — browser-use 1.0.6
<sub>2026-11-16 · 11d ago</sub>

> `pip install 'browser-use==1.0.6'`
> - **BU 4.0 is the default model.** `Agent(task)` and `ChatBrowserUse()` now run `bu-4.0` on the Browser Use gateway instead of `bu-fast`. Pass `llm='bu-4.0-mini'` for simple tasks at the lowest cost, or `llm='bu-4.0-pro'` for the hardest tasks (#6430).
> - **This costs more if you pass no `llm`.** BU 4.0 tokens cost 15 times as much as `bu-fast` ($1.80 / $9.00 per 1M input / output tokens, against $0.12 / $0.60), and it runs at high instead of medium reasoning in the default mode. A short test task cost $0.022 instead of $0.0014. To keep the previous model and price, pass `llm='bu-fast'`. Prices: https://docs.browser-use.com/open-source/models
> - The first run without a key opens Browser Use login and continues after approval; cloud browsers print their live-view link (#6425).
> - Judge gotchas stay grounded in what the run observed (#6418).
> PRs: https://github.com/browser-use/browser-use/pull/6430, https://github.com/browser-use/browser-use/pull/6425, https://github.com/browser-use/browser-use/pull/6418, https://github.com/browser-use/browser-use/pull/6431

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-27 | [ci: run pytest on every core with pytest-xdist (#6493)](https://github.com/browser-use/browser-use/commit/456ff150afb8fd09fc32db1a0d4d64bd85c505cd) | gregpr07 |
| 2026-11-27 | [Merge origin/main into ci/parallel-pytest](https://github.com/browser-use/browser-use/commit/ceaec9df65a603648691d4791f1d4027b4143282) | gregpr07 |
| 2026-11-26 | [Cache Claude on OpenRouter, Bedrock and ChatOpenAI(base_url=OpenRoute…](https://github.com/browser-use/browser-use/commit/717694f63b61319cb20fe0359378e07aaa2baa2d) | gregpr07 |
| 2026-11-26 | [OpenRouter key goes through _env_key (stripped, blank falls back); th…](https://github.com/browser-use/browser-use/commit/b2e997152f9c69208f029a257a92e7b675fca6a7) | gregpr07 |
| 2026-11-26 | [Merge remote-tracking branch 'origin/main' into fix/claude-cache-all-…](https://github.com/browser-use/browser-use/commit/a460b286ec6b2251eb5c95fff3d8907d07b8693f) | gregpr07 |
| 2026-11-26 | [1.0.9: rotate_proxy() with a country hint for blocked sites (#6540)](https://github.com/browser-use/browser-use/commit/9e07ff09f0b059049e5160230aea80352390caf5) | gregpr07 |
| 2026-11-26 | [rotate_proxy: the API fallback says it needs the <id>.cdp.browser-use…](https://github.com/browser-use/browser-use/commit/8bd02c60773390dc012ecff5ee0eecd7b1eacea1) | gregpr07 |
| 2026-11-26 | [cloud cdp_url: a browser-use.com host is a cloud browser (no uuid reg…](https://github.com/browser-use/browser-use/commit/3dab6969d069b920c18bf5a9093de7df8bd6655e) | gregpr07 |
| 2026-11-26 | [Cache Claude on OpenRouter, Bedrock and ChatOpenAI(base_url=OpenRoute…](https://github.com/browser-use/browser-use/commit/dc4cf238743f4bdfe27fe57eae1174245178a5dd) | gregpr07 |
| 2026-11-26 | [rotate_proxy docstring: keep 'never in the middle of a login or check…](https://github.com/browser-use/browser-use/commit/c582b1c563a99ae2046ce5356ad53bfe00e8ad7e) | gregpr07 |

[See all commits ↗](https://github.com/browser-use/browser-use/commits)

## ⬇️ Get it

```bash
git clone https://github.com/browser-use/browser-use.git
```
