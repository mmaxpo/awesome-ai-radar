# ethanplusai/sellbird

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/ethanplusai/sellbird)

> Sellbird (formerly Harvey): the open-source outreach platform that runs on your Claude or ChatGPT plan. Finds companies and decision makers, verifies emails, writes personal cold email, sends it and handles the replies.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛠 Apps & other |
| **Project** | — |
| **Why it's worth a look** | Open-source AI sales outreach (finds leads, sends emails) |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 6.9k |
| 🍴 **Forks** | 1.4k |
| 🐞 **Open issues + PRs** | [77](https://github.com/ethanplusai/sellbird/issues) |
| 💻 **Languages** | Python 92% · JavaScript 5% · CSS 2% · HTML 1% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai-agent` `autonomous-agent` `claude` `cold-email` `prospecting` `python` `sales-automation` `claude-code` `codex` `email-verification` `harvey` `lead-generation` `outreach` `sellbird` `sales-agent` `grok` `grok-bot` |
| 🕒 **Last activity** | 2026-11-18 (3d ago) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [v0.4.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.4.0) — 2026-11-06 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 18.4 MB |
| 🌐 **Website** | https://sellbird.ai |

## 📦 Recent releases

### [v0.4.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.4.0) — 0.4.0: Harvey is now Sellbird
<sub>2026-11-06 · 14d ago</sub>

> > **Follow [@sellbirdagent](https://x.com/sellbirdagent) on X** for new releases, features and the roadmap.
> Harvey has a new name: **Sellbird**. Same project, same history, same maintainers. Your stars, forks and issues are all here, and every old `github.com/ethanplusai/harvey` link redirects.
> **Why the new name?** The name Harvey belongs to another AI company, so this open-source project needed a name of its own. Nothing about how it works has changed. More at [sellbird.ai/harvey](https://sellbird.ai/harvey/).
> Sellbird finds companies that need what you sell, finds the person who decides, checks their email address, writes each one a personal cold email, sends it and handles the replies. It runs on your own machine, on the Claude or ChatGPT plan you already have. If you'd rather not run it yourself, [sellbird.ai](https://sellbird.ai) is the hosted version, now in early access.
> **Upgrading**
> **Not a terminal person?** Open your Harvey folder in Claude Code (or Codex) and say: *"Update Harvey to the latest version."* It runs the steps below for you.
> …

### [v0.3.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.3.0) — 0.3.0 — Claude or Codex subscriptions
<sub>2026-10-13 · 1mo ago</sub>

> Harvey now runs on your **Claude Code or Codex subscription**. Claude remains the default; Codex is opt-in, with no automatic provider or API-key fallback.
> - **Codex support:** macOS/Linux, Codex CLI **0.159.3 exactly**, explicit **gpt-5.5**, and a file-based ChatGPT login. Choose Codex in `harvey setup` or use `harvey train <url> --provider codex --model gpt-5.5`.
> - **Safer recovery and sending:** provider failures pause work without losing replies; reply handling finishes before queued mail sends. Usage and health displays follow the selected provider.
> - **Windows dashboard fix:** UTF-8 assets now load correctly. Codex itself remains unsupported on Windows.
> **Limits:** keyring login storage and Codex in the shipped Docker image are unsupported. Harvey never refreshes your login; renew it through Codex or `codex login` when needed (roughly every eight days). An expired login pauses Harvey safely.
> **Upgrade:** from your existing checkout, activate its virtual environment, run `git pull --ff-only`, then `python -m pip install -e .`, and restart Harvey. Existing Claude users need no provider configuration changes. See the [Codex setup instructions](https://github.com/ethanplusai/harvey#using-a-chatgpt-plan-instead-codex) before switching.
> …

### [v0.2.1](https://github.com/ethanplusai/sellbird/releases/tag/v0.2.1) — 0.2.1 — security release
<sub>2026-10-13 · 1mo ago</sub>

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
| 2026-11-18 | [Merge pull request #269 from ethanplusai/feat/x-in-cli](https://github.com/ethanplusai/sellbird/commit/b212385259da92246a56311d790d936e75dd70dd) | ethanplusai |
| 2026-11-18 | [Link @sellbirdagent from setup's summary, and open release notes with it](https://github.com/ethanplusai/sellbird/commit/edbfea80e79ba1b913ddc3b3bcf46597131a1c96) | ethanplusai |
| 2026-11-18 | [Merge pull request #267 from ethanplusai/feat/follow-on-x](https://github.com/ethanplusai/sellbird/commit/d315300838999f5fd62c37ecdac2d763a84cdc8a) | ethanplusai |
| 2026-11-18 | [Point people at @sellbirdagent on X from the README and the dashboard](https://github.com/ethanplusai/sellbird/commit/724dcf96e2aa63189e60e096d0d132801100242a) | ethanplusai |
| 2026-11-18 | [Merge pull request #265 from ethanplusai/docs/trendshift-badge](https://github.com/ethanplusai/sellbird/commit/964a3a73ba51eef22a621715b0aabfea8d788db7) | ethanplusai |
| 2026-11-18 | [Add the Trendshift badge to the README](https://github.com/ethanplusai/sellbird/commit/5ae5b191651c297ceffb1be18d618fc781f1506f) | ethanplusai |
| 2026-11-11 | [Merge pull request #238 from ethanplusai/fix/no-tip-status](https://github.com/ethanplusai/sellbird/commit/25ec83978b21d16ae20779d09bfea113f37f0ef8) | ethanplusai |
| 2026-11-11 | [Test: read app.js as UTF-8, so the label check passes on Windows](https://github.com/ethanplusai/sellbird/commit/d7297c4f9a64c33e6dda5bd264e363d81c210447) | ethanplusai |
| 2026-11-11 | [no_tip: a dashboard label, a count in sellbird status, and a way back](https://github.com/ethanplusai/sellbird/commit/58275518c3facceb11cffc5c01ac6ecf54f3772f) | ethanplusai |
| 2026-11-11 | [Merge pull request #233 from mattia33011/feat/writer-site-facts](https://github.com/ethanplusai/sellbird/commit/1fe9c48ae2158d638ca73ec96e8a6108c7e57a6f) | ethanplusai |

[See all commits ↗](https://github.com/ethanplusai/sellbird/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ethanplusai/sellbird.git
```
