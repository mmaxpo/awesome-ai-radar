# ethanplusai/sellbird

[← Back to radar](../README.md) · [Open on GitHub ↗](https://github.com/ethanplusai/sellbird)

> Sellbird (formerly Harvey): the open-source outreach platform that runs on your Claude or ChatGPT plan. Finds companies and decision makers, verifies emails, writes personal cold email, sends it and handles the replies.

## 📝 My notes

| | |
|---|---|
| **Status** | study |
| **Project** | — |
| **Why I saved it** | — |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 5.1k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [32](https://github.com/ethanplusai/sellbird/issues) |
| 💻 **Languages** | Python 92% · JavaScript 5% · CSS 2% · HTML 1% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai-agent` `autonomous-agent` `claude` `claude-code` `codex` `cold-email` `email-verification` `harvey` `lead-generation` `outreach` `prospecting` `python` `sales-automation` `sellbird` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [v0.4.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.4.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 18.4 MB |
| 🌐 **Website** | https://sellbird.ai |

## 📦 Recent releases

### [v0.4.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.4.0) — 0.4.0: Harvey is now Sellbird
<sub>2026-11-06 · 4d ago</sub>

> Harvey has a new name: **Sellbird**. Same project, same history, same maintainers. Your stars, forks and issues are all here, and every old `github.com/ethanplusai/harvey` link redirects.
> **Why the new name?** The name Harvey belongs to another AI company, so this open-source project needed a name of its own. Nothing about how it works has changed. More at [sellbird.ai/harvey](https://sellbird.ai/harvey/).
> Sellbird finds companies that need what you sell, finds the person who decides, checks their email address, writes each one a personal cold email, sends it and handles the replies. It runs on your own machine, on the Claude or ChatGPT plan you already have. If you'd rather not run it yourself, [sellbird.ai](https://sellbird.ai) is the hosted version, now in early access.
> **Upgrading**
> **Not a terminal person?** Open your Harvey folder in Claude Code (or Codex) and say: *"Update Harvey to the latest version."* It runs the steps below for you.
> Or in a terminal:
> …

### [v0.3.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.3.0) — 0.3.0 — Claude or Codex subscriptions
<sub>2026-10-13 · 28d ago</sub>

> Harvey now runs on your **Claude Code or Codex subscription**. Claude remains the default; Codex is opt-in, with no automatic provider or API-key fallback.
> - **Codex support:** macOS/Linux, Codex CLI **0.159.3 exactly**, explicit **gpt-5.5**, and a file-based ChatGPT login. Choose Codex in `harvey setup` or use `harvey train <url> --provider codex --model gpt-5.5`.
> - **Safer recovery and sending:** provider failures pause work without losing replies; reply handling finishes before queued mail sends. Usage and health displays follow the selected provider.
> - **Windows dashboard fix:** UTF-8 assets now load correctly. Codex itself remains unsupported on Windows.
> **Limits:** keyring login storage and Codex in the shipped Docker image are unsupported. Harvey never refreshes your login; renew it through Codex or `codex login` when needed (roughly every eight days). An expired login pauses Harvey safely.
> **Upgrade:** from your existing checkout, activate its virtual environment, run `git pull --ff-only`, then `python -m pip install -e .`, and restart Harvey. Existing Claude users need no provider configuration changes. See the [Codex setup instructions](https://github.com/ethanplusai/harvey#using-a-chatgpt-plan-instead-codex) before switching.
> …

### [v0.2.1](https://github.com/ethanplusai/sellbird/releases/tag/v0.2.1) — 0.2.1 — security release
<sub>2026-10-13 · 28d ago</sub>

> A security release. Update if you run Harvey.
> **Security**
> - **Claude now runs with no tools.** Every Claude call used to run with
>   `--dangerously-skip-permissions`, and prompts include text Harvey doesn't
>   control: prospect email replies and scraped web pages. Instructions hidden
>   in that text could make Claude run commands, read or write files, or use
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [Merge pull request #238 from ethanplusai/fix/no-tip-status](https://github.com/ethanplusai/sellbird/commit/25ec83978b21d16ae20779d09bfea113f37f0ef8) | ethanplusai |
| 2026-11-11 | [Test: read app.js as UTF-8, so the label check passes on Windows](https://github.com/ethanplusai/sellbird/commit/d7297c4f9a64c33e6dda5bd264e363d81c210447) | ethanplusai |
| 2026-11-11 | [no_tip: a dashboard label, a count in sellbird status, and a way back](https://github.com/ethanplusai/sellbird/commit/58275518c3facceb11cffc5c01ac6ecf54f3772f) | ethanplusai |
| 2026-11-11 | [Merge pull request #233 from mattia33011/feat/writer-site-facts](https://github.com/ethanplusai/sellbird/commit/1fe9c48ae2158d638ca73ec96e8a6108c7e57a6f) | ethanplusai |
| 2026-11-11 | [Merge main (CHANGELOG: keep both entries)](https://github.com/ethanplusai/sellbird/commit/0c264407c140e7bb5284bef2442d32ee500773f4) | ethanplusai |
| 2026-11-11 | [Merge pull request #236 from HookTXT/hooktxt/french-owner-titles](https://github.com/ethanplusai/sellbird/commit/74ce4c16f12600abc5ad1f0b2ad90da2d6877761) | ethanplusai |
| 2026-11-11 | [Merge pull request #231 from mattia33011/feat/italian-opt-out](https://github.com/ethanplusai/sellbird/commit/f20d487013c0a77ca9715000d333dc32b7011615) | ethanplusai |
| 2026-11-11 | [Merge main into hooktxt/french-owner-titles](https://github.com/ethanplusai/sellbird/commit/c38ec9e6f702dcb255c963b1f8ea571ed80b5864) | HookTXT |
| 2026-11-11 | [Merge main: accept Italian and French opt-out lines side by side](https://github.com/ethanplusai/sellbird/commit/75a1e8c69186b15dca0a80d7bf271f0fa518a0dc) | ethanplusai |
| 2026-11-11 | [Merge main (CHANGELOG: keep both entries)](https://github.com/ethanplusai/sellbird/commit/0ad9f5b6686f3115d671249f19404b02e8aea39c) | ethanplusai |

[See all commits ↗](https://github.com/ethanplusai/sellbird/commits)

## 👥 Top contributors

[ethanplusai](https://github.com/ethanplusai) (404) · [gabrielaoimevbore-beep](https://github.com/gabrielaoimevbore-beep) (61) · [thekasyap](https://github.com/thekasyap) (12) · [xiaoheiai4719-collab](https://github.com/xiaoheiai4719-collab) (6) · [MBScoin](https://github.com/MBScoin) (5)

## ⬇️ Get it

```bash
git clone https://github.com/ethanplusai/sellbird.git
```
