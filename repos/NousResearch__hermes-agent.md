# NousResearch/hermes-agent

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/NousResearch/hermes-agent)

> The agent that grows with you

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | TCOS |
| **Why it's worth a look** | Self-improving agent that grows with you — huge community |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 265.8k |
| 🍴 **Forks** | 60.2k |
| 🐞 **Open issues + PRs** | [54.2k](https://github.com/NousResearch/hermes-agent/issues) |
| 💻 **Languages** | Python 73% · TypeScript 24% · JavaScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agent` `ai-agents` `llm` `anthropic` `chatgpt` `claude` `claude-code` `codex` `hermes` `hermes-agent` `nous-research` `openai` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-07-22 |
| 📦 **Latest release** | [v0.23.4](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.4) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1516.7 MB |
| 🌐 **Website** | https://hermes-agent.nousresearch.com |

## 📦 Recent releases

### [v0.23.4](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.4) — Hermes Agent v0.23.4
<sub>2026-11-24 · today</sub>

> **Hermes Agent v0.23.4**
> **Release Date:** November 23, 2026
> > Patch release. This tag rolls up the ~229 PRs merged since v0.23.3 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.
> **About this release**
> Measured at commit `8fc03744473`, the window since v0.23.3 contains **1,122 non-merge commits** across **1,316 changed files** (+96,873 / −6,703), **229 merged PRs** and **281 closed issues**.
> Also in the window, undocumented here on purpose: Gemini 4 Hydrogen, Neon and Carbon on Nous Portal, OpenRouter and Vertex, `hermes gateway migrate --backends` to move an old serve/dashboard backend onto the gateway (with a System page card in the dashboard), `hermes plugins config` to edit a plugin's settings from the terminal, approval cards in Desktop for a sandbox's folder and site requests, gateway clients announcing who they are so plugins can see which client sent a turn, a long run of Desktop streaming and transcript performance work, a retryable indicator for slow profile switches, `hermes dashboard password` without a TTY prompt, configurable skill index description length (`skills.index_desc_limit`), managed-scope config honored by security and URL-safety reads, and a large batch of new plugin-catalog entries.
> …

### [canary.20261124T064706Z-v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/canary.20261124T064706Z-v0.23.3) — Hermes Agent canary canary.20261124T064706Z-v0.23.3 _(pre-release)_
<sub>2026-11-24 · today</sub>

> **Hermes Agent v0.23.3+canary.20261124T064706Z (canary.20261124T064706Z-v0.23.3)**
> **Release Date:** November 24, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [canary.20261123T065600Z-v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/canary.20261123T065600Z-v0.23.3) — Hermes Agent canary canary.20261123T065600Z-v0.23.3 _(pre-release)_
<sub>2026-11-23 · yesterday</sub>

> **Hermes Agent v0.23.3+canary.20261123T065600Z (canary.20261123T065600Z-v0.23.3)**
> **Release Date:** November 23, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.3+canary.20261120T064609Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3%2Bcanary.20261120T064609Z) — Hermes Agent canary v0.23.3+canary.20261120T064609Z _(pre-release)_
<sub>2026-11-20 · 4d ago</sub>

> **Hermes Agent v0.23.3+canary.20261120T064609Z (v0.23.3+canary.20261120T064609Z)**
> **Release Date:** November 20, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) — Hermes Agent v0.23.3
<sub>2026-11-20 · 4d ago</sub>

> **Hermes Agent v0.23.3**
> **Release Date:** November 19, 2026
> > Patch release. This tag rolls up the ~370 PRs merged since v0.23.2 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.
> **About this release**
> Measured at commit `caafe5389ae`, the window since v0.23.2 contains **1,657 non-merge commits** across **3,948 changed files** (+222,379 / −96,154), **370 merged PRs** and **60 closed issues**.
> Also in the window, undocumented here on purpose: one prompt-cache lifecycle controller (warming through long tool runs, compaction of idle chats before the 1h cache expires, Nous Portal on the full 1h lifecycle, `prompt_caching.cache_ttl` defaulting to `auto`), compaction that archives the tool results it drops, the proactive tool-result prune on by default, a one-question first-run CLI setup with the free tier included, GPT-6.2 Astra and Sol (+ Pro) on OpenRouter and Nous Portal, a "Waiting on teammates" strip above Bot Chat composers, the Linux AppImage agent payload run from a stable per-build copy, the storage layer split behind a persistence interface with its SQLite backend, dependency security bumps (oauthlib, opentelemetry, tornado), and a large batch of new plugin-catalog entries.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [fix(dashboard): refuse a non-UTF-8 .env with a quoted override before…](https://github.com/NousResearch/hermes-agent/commit/4c84e78629cf1cdfcb79bea3b39aa4a49003c829) | unsupportedpastels |
| 2026-11-24 | [fix(dashboard): judge a username template against the same .env names…](https://github.com/NousResearch/hermes-agent/commit/32019114f25789d96bba7c31465dd48f8614aeb8) | unsupportedpastels |
| 2026-11-24 | [fix(dashboard): remove a .env override assigned under a quoted name](https://github.com/NousResearch/hermes-agent/commit/f44f7bf41b35aa3641ae283a2a6a2d828a208aa1) | unsupportedpastels |
| 2026-11-24 | [fix(gateway): catch only the errors the gateway service generators raise](https://github.com/NousResearch/hermes-agent/commit/e015ff7274e4a226e1df849ddea33a2a7ecd09bd) | unsupportedpastels |
| 2026-11-24 | [refactor(config): remove whole .env assignments in remove_env_value, …](https://github.com/NousResearch/hermes-agent/commit/e49fff4540fe3e6b83184a03ff073bc202e0227f) | unsupportedpastels |
| 2026-11-24 | [fix(gateway): count a NAME= token after a quoted env value as set](https://github.com/NousResearch/hermes-agent/commit/ae61e5292c0d3aec308f4e40ecdbb0f9dda83d34) | unsupportedpastels |
| 2026-11-24 | [fix(gateway): apply a unit's UnsetEnvironment= when reading the envir…](https://github.com/NousResearch/hermes-agent/commit/d95b398a588e8f5e0cbdf937a980f97d9ae7061d) | unsupportedpastels |
| 2026-11-24 | [fix(gateway): judge a first move's .env template against the gateway …](https://github.com/NousResearch/hermes-agent/commit/7cf1c52f588480bb65e6c5ea7dcb3b5478388ff7) | unsupportedpastels |
| 2026-11-24 | [fix(dashboard): remove whole .env assignments around multi-line value…](https://github.com/NousResearch/hermes-agent/commit/783d58e564cef4ede748a1473dab6089b3079e46) | unsupportedpastels |
| 2026-11-24 | [fix(gateway): refuse a stopped unit whose env launcher may set its home](https://github.com/NousResearch/hermes-agent/commit/23efc4e1dbad916db62be55c6c570d515b0670eb) | unsupportedpastels |

[See all commits ↗](https://github.com/NousResearch/hermes-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NousResearch/hermes-agent.git
```
