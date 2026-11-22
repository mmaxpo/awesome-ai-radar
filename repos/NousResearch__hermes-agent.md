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
| ⭐ **Stars** | 265.3k |
| 🍴 **Forks** | 60.0k |
| 🐞 **Open issues + PRs** | [54.2k](https://github.com/NousResearch/hermes-agent/issues) |
| 💻 **Languages** | Python 73% · TypeScript 24% · JavaScript 2% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai` `ai-agent` `ai-agents` `llm` `anthropic` `chatgpt` `claude` `claude-code` `codex` `hermes` `hermes-agent` `nous-research` `openai` |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2025-07-22 |
| 📦 **Latest release** | [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1512.5 MB |
| 🌐 **Website** | https://hermes-agent.nousresearch.com |

## 📦 Recent releases

### [v0.23.3+canary.20261120T064609Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3%2Bcanary.20261120T064609Z) — Hermes Agent canary v0.23.3+canary.20261120T064609Z _(pre-release)_
<sub>2026-11-20 · 2d ago</sub>

> **Hermes Agent v0.23.3+canary.20261120T064609Z (v0.23.3+canary.20261120T064609Z)**
> **Release Date:** November 20, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.3](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.3) — Hermes Agent v0.23.3
<sub>2026-11-20 · 2d ago</sub>

> **Hermes Agent v0.23.3**
> **Release Date:** November 19, 2026
> > Patch release. This tag rolls up the ~370 PRs merged since v0.23.2 into a stable release for the GitHub release (CLI and installers), the Microsoft Store app, Docker and Hermes Cloud. Full curated notes for this window ship with v0.24.0.
> **About this release**
> Measured at commit `caafe5389ae`, the window since v0.23.2 contains **1,657 non-merge commits** across **3,948 changed files** (+222,379 / −96,154), **370 merged PRs** and **60 closed issues**.
> Also in the window, undocumented here on purpose: one prompt-cache lifecycle controller (warming through long tool runs, compaction of idle chats before the 1h cache expires, Nous Portal on the full 1h lifecycle, `prompt_caching.cache_ttl` defaulting to `auto`), compaction that archives the tool results it drops, the proactive tool-result prune on by default, a one-question first-run CLI setup with the free tier included, GPT-6.2 Astra and Sol (+ Pro) on OpenRouter and Nous Portal, a "Waiting on teammates" strip above Bot Chat composers, the Linux AppImage agent payload run from a stable per-build copy, the storage layer split behind a persistence interface with its SQLite backend, dependency security bumps (oauthlib, opentelemetry, tornado), and a large batch of new plugin-catalog entries.
> …

### [v0.23.2+canary.20261119T064637Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261119T064637Z) — Hermes Agent canary v0.23.2+canary.20261119T064637Z _(pre-release)_
<sub>2026-11-19 · 3d ago</sub>

> **Hermes Agent v0.23.2+canary.20261119T064637Z (v0.23.2+canary.20261119T064637Z)**
> **Release Date:** November 19, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.2+canary.20261118T064620Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261118T064620Z) — Hermes Agent canary v0.23.2+canary.20261118T064620Z _(pre-release)_
<sub>2026-11-18 · 4d ago</sub>

> **Hermes Agent v0.23.2+canary.20261118T064620Z (v0.23.2+canary.20261118T064620Z)**
> **Release Date:** November 18, 2026
> **Downloads**
> **Hermes Desktop**
> | OS | Architecture | Download |
> |---|---|---|
> …

### [v0.23.2+canary.20261117T064624Z](https://github.com/NousResearch/hermes-agent/releases/tag/v0.23.2%2Bcanary.20261117T064624Z) — Hermes Agent canary v0.23.2+canary.20261117T064624Z _(pre-release)_
<sub>2026-11-17 · 5d ago</sub>

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
| 2026-11-22 | [test(desktop): disband rewrite leaves out another room's tombstone](https://github.com/NousResearch/hermes-agent/commit/0f602c5f6f18615632535251d62a2db74ce93b69) | teknium1 |
| 2026-11-22 | [fix(desktop): every group chat storage writer keeps the whole room re…](https://github.com/NousResearch/hermes-agent/commit/49a2bdcab97bfb2e617fb3ed331f6c0a1fa3b24e) | kshitijk4poor |
| 2026-11-22 | [test(profiles): pin the review-surfaced branches of the profile lifec…](https://github.com/NousResearch/hermes-agent/commit/da8e7d71abe4ac165760cd813c0c18c53e697b90) | kshitijk4poor |
| 2026-11-22 | [fix(profiles): a failed import stages in a hidden mkdtemp, so Windows…](https://github.com/NousResearch/hermes-agent/commit/cbfc05acd8c4af391bb0029a71a4522948d020ad) | kshitijk4poor |
| 2026-11-22 | [test(profiles): the staging-mode test is POSIX-only; the lock wait is…](https://github.com/NousResearch/hermes-agent/commit/9b70b9b33136e2f2cde00865cc05a92cf83507fd) | kshitijk4poor |
| 2026-11-22 | [fix(profiles): import and rename publish a name like create, so a rac…](https://github.com/NousResearch/hermes-agent/commit/427b87092cf8eb008ad964a4cee05501ebe9541d) | kshitijk4poor |
| 2026-11-22 | [fix(desktop): the share-keys hint scopes the launch profile to a fres…](https://github.com/NousResearch/hermes-agent/commit/ad6d519aceef17d502814f9b8034cd5d63b51456) | kshitijk4poor |
| 2026-11-22 | [fix(desktop): the share-keys hint says a cloned bot's logins are copied](https://github.com/NousResearch/hermes-agent/commit/5e2124dc825f8631b82653b615304058135e98d8) | kshitijk4poor |
| 2026-11-22 | [fix(kanban): the model preflight judges a card by the provider and UR…](https://github.com/NousResearch/hermes-agent/commit/fbd2c432354a0410f660310c369c864cd0082359) | kshitijk4poor |
| 2026-11-22 | [test(ci): check that notarytool's stdout stays out of the preflight l…](https://github.com/NousResearch/hermes-agent/commit/8650b2aea8899cc494acf87b117d1f9c75dacbc4) | BearHuddleston |

[See all commits ↗](https://github.com/NousResearch/hermes-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NousResearch/hermes-agent.git
```
