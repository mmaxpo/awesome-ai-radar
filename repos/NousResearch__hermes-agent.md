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
| 2026-11-21 | [test(dashboard): the foreign-address probe test never names an addres…](https://github.com/NousResearch/hermes-agent/commit/b25cf0a408d20bbc658cac26deca35d084980466) | unsupportedpastels |
| 2026-11-21 | [fix(dashboard): --status probes its own address only where this machi…](https://github.com/NousResearch/hermes-agent/commit/686baf81b86a7e884be5e0ddd656d6b2c6af52f2) | unsupportedpastels |
| 2026-11-21 | [test(dashboard): the exec-launcher --status test runs the launcher th…](https://github.com/NousResearch/hermes-agent/commit/d61e25fffecd9b5bcb607a844e936ed4b22a9cb9) | unsupportedpastels |
| 2026-11-21 | [fix(dashboard): --status probes the address it names, so an exec laun…](https://github.com/NousResearch/hermes-agent/commit/6141972d9c1ded69f0315a82623ca53ed93ed574) | BearHuddleston |
| 2026-11-21 | [fix(dashboard): --status checks listener address overlap before omitt…](https://github.com/NousResearch/hermes-agent/commit/891a8250005accb26c5a1bfec9e23c0284ba1e19) | BearHuddleston |
| 2026-11-21 | [fix(dashboard): --status attributes a held port by the peer its probe…](https://github.com/NousResearch/hermes-agent/commit/572e4ab424b82842aef2437beade93d950b94ce0) | unsupportedpastels |
| 2026-11-21 | [test(dashboard): the listener-hint test no longer races the gateway's…](https://github.com/NousResearch/hermes-agent/commit/8c72699488e04d7749ae7420058bdd27d70ecd73) | unsupportedpastels |
| 2026-11-21 | [fix(dashboard): the gateway hints name its live listener and read no …](https://github.com/NousResearch/hermes-agent/commit/05677872dfd4e4cd806bfbf828a580c54f7f8085) | unsupportedpastels |
| 2026-11-21 | [fix(dashboard): a gateway draining or in its restart wait keeps exit 75](https://github.com/NousResearch/hermes-agent/commit/f14e36c2403fef09721ea1b3c4e67e264aee485a) | unsupportedpastels |
| 2026-11-21 | [fix(dashboard): --status leaves its own launcher out and names a gate…](https://github.com/NousResearch/hermes-agent/commit/273dae2080d74d63014ebb1abfd93501368385c5) | unsupportedpastels |

[See all commits ↗](https://github.com/NousResearch/hermes-agent/commits)

## ⬇️ Get it

```bash
git clone https://github.com/NousResearch/hermes-agent.git
```
