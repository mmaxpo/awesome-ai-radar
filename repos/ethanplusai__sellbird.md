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
| ⭐ **Stars** | 7.5k |
| 🍴 **Forks** | 1.6k |
| 🐞 **Open issues + PRs** | [101](https://github.com/ethanplusai/sellbird/issues) |
| 💻 **Languages** | Python 87% · JavaScript 8% · CSS 3% · HTML 2% |
| 📜 **License** | AGPL-3.0 |
| 🏷 **Topics** | `ai-agent` `autonomous-agent` `claude` `cold-email` `prospecting` `python` `sales-automation` `claude-code` `codex` `email-verification` `harvey` `lead-generation` `outreach` `sellbird` `sales-agent` `grok` `grok-bot` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-03-12 |
| 📦 **Latest release** | [v0.5.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.5.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 25.0 MB |
| 🌐 **Website** | https://sellbird.ai |

## 📦 Recent releases

### [v0.5.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.5.0) — 0.5.0: your sales team, inside your agent
<sub>2026-11-25 · 2d ago</sub>

> Sellbird finds the businesses worth talking to, writes the first email and every follow-up, and books the meeting. With 0.5 it lives where you already work: in Claude Code, Claude desktop and Codex.
> - **Connect in one click.** Run `sellbird connect`, or press Connect next to Claude Code, Claude desktop or Codex in the dashboard. No config files to edit, no keys pasted anywhere. Your agent gets its own key with limited reach.
> - **Ask your agent "What needs me?"** It answers with a card in the chat: what Sellbird did overnight, what's waiting for your OK, how each campaign is doing. One click opens the full app right next to the chat, already signed in.
> - **A new app, built around your agent.** A dock with six places: Today, Outbound, Inbound, People, Calendar and Numbers, plus Set up. Pages open with one sentence on where things stand. Today shows what your agent did and what only you can decide. Drafts show why each person was picked.
> - **Everything in one place.** Outbound, inbound leads from your site's forms, texts to people who said yes, brand mentions, social playbooks, people with stages and deals, a real calendar with week and month views, and numbers with charts over time and a found-to-meeting funnel.
> - **You stay in charge.** Your agent can read, draft, plan and explain. Approving, sending, buying and resuming are always your clicks.
> …

### [v0.4.0](https://github.com/ethanplusai/sellbird/releases/tag/v0.4.0) — 0.4.0: Harvey is now Sellbird
<sub>2026-11-06 · 20d ago</sub>

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
| 2026-11-25 | [Merge pull request #309 from ethanplusai/feat/agent-first-ui](https://github.com/ethanplusai/sellbird/commit/8c743f1c475f61f7b2c04e50501cf6938a126ed6) | ethanplusai |
| 2026-11-25 | [README: Sellbird shown inside Claude and Codex, and the app in a wind…](https://github.com/ethanplusai/sellbird/commit/6717494d245d7b8a4c54b2f6a4a932d787cfa392) | ethanplusai |
| 2026-11-25 | [Tests pass on Linux and Windows: the desktop install test uses this c…](https://github.com/ethanplusai/sellbird/commit/6d01e693d95cf7627af9dd77ce08824c85f58255) | ethanplusai |
| 2026-11-25 | [CLA: Florida law. NOTICE: Voyage Studios LLC, doing business as Sellb…](https://github.com/ethanplusai/sellbird/commit/bfe73bff91f89b326922701c1ad3d1db8da41ea4) | ethanplusai |
| 2026-11-25 | [Add the Sellbird Contributor License Agreement and a bot that checks …](https://github.com/ethanplusai/sellbird/commit/a494279e5fb0323a466af6bdc6d561a81690e9aa) | ethanplusai |
| 2026-11-24 | [Sellbird 0.5.0](https://github.com/ethanplusai/sellbird/commit/3d1ce72bc5fac331d22185050b8f041138e15950) | ethanplusai |
| 2026-11-24 | [README and docs for 0.5: Sellbird inside your agent, the new app, upg…](https://github.com/ethanplusai/sellbird/commit/500601a317d33e48533bb8f141c5a291b60e22eb) | ethanplusai |
| 2026-11-24 | [Setup wizard banner lines up again](https://github.com/ethanplusai/sellbird/commit/70e343b663277abeb615907aca6b9e7e34033bdf) | ethanplusai |
| 2026-11-24 | [Fresh-install fixes: plain empty status, no warmup check on the examp…](https://github.com/ethanplusai/sellbird/commit/f6dd87f0ec100b3704139173e6f885be6a1372fd) | ethanplusai |
| 2026-11-24 | [A card posts its click straight to the dashboard when the app won't](https://github.com/ethanplusai/sellbird/commit/28fa60a78d331e43fc5375a8becd8ac82d95503a) | ethanplusai |

[See all commits ↗](https://github.com/ethanplusai/sellbird/commits)

## ⬇️ Get it

```bash
git clone https://github.com/ethanplusai/sellbird.git
```
