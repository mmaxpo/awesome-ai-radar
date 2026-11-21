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
| ⭐ **Stars** | 265.1k |
| 🍴 **Forks** | 59.9k |
| 🐞 **Open issues + PRs** | [54.2k](https://github.com/NousResearch/hermes-agent/issues) |
| 💻 **Languages** | Python 73% · TypeScript 24% · JavaScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agent` `ai-agents` `llm` `anthropic` `chatgpt` `claude` `claude-code` `codex` `hermes` `hermes-agent` `nous-research` `openai` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2025-07-22 |
| 📦 **Latest release** | [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1512.9 MB |
| 🌐 **Website** | https://hermes-agent.nousresearch.com |

## 📦 Recent releases

### [v0.23.3+canary.20261120T064609Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3%2Bcanary.20261120T064609Z) — Hermes Agent canary v0.23.3+canary.20261120T064609Z _(pre-release)_
<sub>2026-11-20 · yesterday</sub>

> **Hermes Agent v0.23.3+canary.20261120T064609Z (v0.23.3+canary.20261120T064609Z)**
> **Release Date:** November 20, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) — Hermes Agent v0.23.3
<sub>2026-11-20 · yesterday</sub>

> **Hermes Agent v0.23.3**
> **Release Date:** November 19, 2026
> > Patch release. This tag rolls up the ~370 PRs merged since v0.23.2 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.
> **About this release**
> Measured at commit `caafe5389ae`, the window since v0.23.2 contains **1,657 non-merge commits** across **3,948 changed files** (+222,379 / −96,154), **370 merged PRs** and **60 closed issues**.
> Also in the window, undocumented here on purpose: one prompt-cache lifecycle controller (warming through long tool runs, compaction of idle chats before the 1h cache expires, Nous Portal on the full 1h lifecycle, `prompt_caching.cache_ttl` defaulting to `auto`), compaction that archives the tool results it drops, the proactive tool-result prune on by default, a one-question first-run CLI setup with the free tier included, GPT-6.2 Astra and Sol (+ Pro) on OpenRouter and Nous Portal, a "Waiting on teammates" strip above Bot Chat composers, the Linux AppImage agent payload run from a stable per-build copy, the storage layer split behind a persistence interface with its SQLite backend, dependency security bumps (oauthlib, opentelemetry, tornado), and a large batch of new plugin-catalog entries.
> …

### [v0.23.2+canary.20261119T064637Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261119T064637Z) — Hermes Agent canary v0.23.2+canary.20261119T064637Z _(pre-release)_
<sub>2026-11-19 · 2d ago</sub>

> **Hermes Agent v0.23.2+canary.20261119T064637Z (v0.23.2+canary.20261119T064637Z)**
> **Release Date:** November 19, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.2+canary.20261118T064620Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261118T064620Z) — Hermes Agent canary v0.23.2+canary.20261118T064620Z _(pre-release)_
<sub>2026-11-18 · 3d ago</sub>

> **Hermes Agent v0.23.2+canary.20261118T064620Z (v0.23.2+canary.20261118T064620Z)**
> **Release Date:** November 18, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.2+canary.20261117T064624Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261117T064624Z) — Hermes Agent canary v0.23.2+canary.20261117T064624Z _(pre-release)_
<sub>2026-11-17 · 4d ago</sub>

> **Hermes Agent v0.23.2+canary.20261117T064624Z (v0.23.2+canary.20261117T064624Z)**
> **Release Date:** November 17, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [fix(gateway): never copy a launcher key the home's .env already sets](https://github.com/NousResearch/hermes-agent/commit/38fde82474b5d370590e314358cc05076dc9ae70) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): name running turns in the no-service-manager recipe too](https://github.com/NousResearch/hermes-agent/commit/c8a8bfb2f7af7d673b43a4de46fff3098ba1d4e1) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): probe a by-hand backend's health only in the planner's …](https://github.com/NousResearch/hermes-agent/commit/49607d4ce546dfa3f39ab442f74f48c07f658a3c) | unsupportedpastels |
| 2026-11-21 | [test(gateway): run the status-wording cases on the host they describe](https://github.com/NousResearch/hermes-agent/commit/989b03e10f1c318633c2c5bc25e1c4b21fc6f68d) | unsupportedpastels |
| 2026-11-21 | [test(gateway): check the plan's hermes commands by their output, not …](https://github.com/NousResearch/hermes-agent/commit/78b654f287db5a2e75f6e866da1e44eedcf45a8d) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): block a by-hand plan on a refused old public URL](https://github.com/NousResearch/hermes-agent/commit/0137734cf8f8cd761e28a2279c1d8ea687fb5fde) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): say how the unknown-activity blocker clears and name it…](https://github.com/NousResearch/hermes-agent/commit/18cfd6e05556bd8da0b34b7599b0825468ea7589) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): name known running turns in every forced by-hand plan](https://github.com/NousResearch/hermes-agent/commit/ad067d40f27ab03baba9533d085e08c005e31c09) | BearHuddleston |
| 2026-11-21 | [fix(gateway): treat a by-hand backend without /api/health as unknown …](https://github.com/NousResearch/hermes-agent/commit/dbd7ace40a6bc9fbd2a8a770793c44b2e4fa6a44) | unsupportedpastels |
| 2026-11-21 | [fix(gateway): redact inline source after pythonw short -c clusters too](https://github.com/NousResearch/hermes-agent/commit/f12fc78ca1d048de0091d30e124f6acc3a8d0ad1) | unsupportedpastels |

[See all commits ↗](https://github.com/NousResearch/hermes-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NousResearch/hermes-agent.git
```
