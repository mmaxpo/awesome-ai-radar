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
| ⭐ **Stars** | 122.0k |
| 🍴 **Forks** | 13.6k |
| 🐞 **Open issues + PRs** | [586](https://github.com/browser-use/browser-use/issues) |
| 💻 **Languages** | Python 99% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `llm` `ai-agents` `ai-tools` `browser-automation` `python` `browser-use` `playwright` `browser-agent` `cdp` `cloud-browser` `computer-use` `headless-browser` `mcp` `remote-browser` `stealth-browser` `web-automation` `web-scraping` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2024-10-31 |
| 📦 **Latest release** | [1.0.8](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — 2026-11-22 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 42.3 MB |
| 🌐 **Website** | https://browser-use.com |

## 📦 Recent releases

### [1.0.8](https://github.com/browser-use/browser-use/releases/tag/1.0.8) — browser-use 1.0.8
<sub>2026-11-22 · 3d ago</sub>

> `pip install 'browser-use==1.0.8'`
> - The judge asks as one more turn of the run, so the provider reads the run from its cache instead of billing the trace again. It returns the same verdict fields, gotchas included (#6457).
> - No API key over SSH or on a headless machine: the run prints a link and a code to approve on any device, then continues (#6427).
> - DeepSeek and Qwen in thinking mode: when the model refuses the forced final call at the step limit, the agent asks again without forcing, so the run returns its answer (#6453).
> - `bu.type` never prints a password field's value (#6455).
> - `Browser(cdp_url=...)` attaches the one page already open instead of a new blank tab (#6456).
> …

### [1.0.8rc1](https://github.com/browser-use/browser-use/releases/tag/1.0.8rc1) — 1.0.8rc1: release candidate for 1.0.8 _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

> `pip install 'browser-use==1.0.8rc1'`
> - The judge asks as one more turn of the run, so the provider reads the run from its cache instead of billing the trace again. It returns the same verdict fields, gotchas included (#6457).
> - No API key over SSH or on a headless machine: the run prints a link and a code to approve on any device, then continues (#6427).
> - DeepSeek and Qwen in thinking mode: when the model refuses the forced final call at the step limit, the agent asks again without forcing, so the run returns its answer (#6453).
> - `bu.type` never prints a password field's value (#6455).
> - `Browser(cdp_url=...)` attaches the one page already open instead of a new blank tab (#6456).
> …

### [1.0.7](https://github.com/browser-use/browser-use/releases/tag/1.0.7) — browser-use 1.0.7
<sub>2026-11-20 · 4d ago</sub>

> `pip install 'browser-use==1.0.7'`
> - **MCP calls no longer time out at 60 s.** A long `browser_exec` now replies within 50 s with the output so far, so Cursor and other clients with a 60 s limit get a result instead of `Request timed out`. The cell keeps running, and calling `browser_exec` again with empty code returns the rest. Calls under 50 s reply exactly as before (#6477).
> - README: Browser Use for enterprises, and the Cloud API key link is back in the Python quickstart (#6442, #6422).
> - Skills, README, CLI and MCP ask coding agents for integration feedback (#6454).

### [1.0.6](https://github.com/browser-use/browser-use/releases/tag/1.0.6) — browser-use 1.0.6
<sub>2026-11-16 · 9d ago</sub>

> `pip install 'browser-use==1.0.6'`
> - **BU 4.0 is the default model.** `Agent(task)` and `ChatBrowserUse()` now run `bu-4.0` on the Browser Use gateway instead of `bu-fast`. Pass `llm='bu-4.0-mini'` for simple tasks at the lowest cost, or `llm='bu-4.0-pro'` for the hardest tasks (#6430).
> - **This costs more if you pass no `llm`.** BU 4.0 tokens cost 15 times as much as `bu-fast` ($1.80 / $9.00 per 1M input / output tokens, against $0.12 / $0.60), and it runs at high instead of medium reasoning in the default mode. A short test task cost $0.022 instead of $0.0014. To keep the previous model and price, pass `llm='bu-fast'`. Prices: https://docs.browser-use.com/open-source/models
> - The first run without a key opens Browser Use login and continues after approval; cloud browsers print their live-view link (#6425).
> - Judge gotchas stay grounded in what the run observed (#6418).
> PRs: https://github.com/browser-use/browser-use/pull/6430, https://github.com/browser-use/browser-use/pull/6425, https://github.com/browser-use/browser-use/pull/6418, https://github.com/browser-use/browser-use/pull/6431

### [1.0.5](https://github.com/browser-use/browser-use/releases/tag/1.0.5) — browser-use 1.0.5
<sub>2026-11-14 · 11d ago</sub>

> `pip install 'browser-use==1.0.5'`
> - Every run is judged by your own model: one more low-effort request checks the run against the task and fills `result.judgement` with `success`, `failure_reason`, `description`, `prompt_injection_detected`, `bot_block_or_captcha_detected` and `gotchas`. `judge_context=` gives it your criteria; `judge=False` turns it off; the 0.x `use_judge` / `ground_truth` work again (#6398).
> - The judge sees the trace, the run's last screenshots and the final page (unless `use_vision=False`). It writes gotchas whenever the site rejected input, errored, blocked or rate-limited the agent, also on a successful run, e.g. "The form requires phone numbers in (###) ###-#### format" (#6403).
> 13 real runs, each judged 3 times: gotchas on 15/15 verdicts where the site pushed back (6/15 before), 2/24 on clean runs, success verdicts unchanged.
> PRs: https://github.com/browser-use/browser-use/pull/6398, https://github.com/browser-use/browser-use/pull/6403, https://github.com/browser-use/browser-use/pull/6404

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [cli, cli-mcp: switch to the user's Chrome once its remote debugging i…](https://github.com/browser-use/browser-use/commit/94784c1f7ecb6b0a5f565b7f9fba59e395b7e048) | gregpr07 |
| 2026-11-24 | [cli, cli-mcp: leave the own Chromium once the user's Chrome has remot…](https://github.com/browser-use/browser-use/commit/65820e9b3f292b731581bdc1b1489787b264bc07) | gregpr07 |
| 2026-11-22 | [1.0.8: release the 1.0.8rc1 code (#6504)](https://github.com/browser-use/browser-use/commit/753d629d76eb2b670f4cf467f3355bbe750f6845) | gregpr07 |
| 2026-11-22 | [1.0.8](https://github.com/browser-use/browser-use/commit/d567193f6e06c8b6f570dd3482babb027eb9dfaf) | gregpr07 |
| 2026-11-20 | [1.0.8rc1: cached judge, SSH sign-in, step-limit answers and 3 fixes (…](https://github.com/browser-use/browser-use/commit/e682e0dc02d77a307a5b2aedf17142c2cd69af5b) | gregpr07 |
| 2026-11-20 | [review: cached judge gets the run's status and result; default-model …](https://github.com/browser-use/browser-use/commit/8e6ac139e3067db036cbb94ded3c4c266dd7f85e) | gregpr07 |
| 2026-11-20 | [1.0.8rc1](https://github.com/browser-use/browser-use/commit/a642b849c8c874da07ab71f33cad9b2ec36c80c6) | gregpr07 |
| 2026-11-20 | [Merge branch 'pr6427new' into release-1.0.8b](https://github.com/browser-use/browser-use/commit/6566e3aad70fc3462b815fc997895c452c30ebca) | gregpr07 |
| 2026-11-20 | [Merge branch 'pr6457' into release-1.0.8b](https://github.com/browser-use/browser-use/commit/39e72d1d64f487ca9a88951a40e83d2fb4f1221c) | gregpr07 |
| 2026-11-20 | [Merge branch 'pr6453' into release-1.0.8b](https://github.com/browser-use/browser-use/commit/f30d5f8f06e326340d7e551fd023d5b5d2df1a97) | gregpr07 |

[See all commits ↗](https://github.com/browser-use/browser-use/commits)

## ⬇️ Get it

```bash
git clone https://github.com/browser-use/browser-use.git
```
