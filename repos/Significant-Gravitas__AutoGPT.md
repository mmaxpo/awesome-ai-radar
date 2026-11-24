# Significant-Gravitas/AutoGPT

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/Significant-Gravitas/AutoGPT)

> AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🤖 Agent frameworks & multi-agent |
| **Project** | — |
| **Why it's worth a look** | The original autonomous-agent project, now an agent-building platform |
| **Added** | 2026-11-11 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 188.2k |
| 🍴 **Forks** | 45.8k |
| 🐞 **Open issues + PRs** | [838](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 31% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) — 2026-11-19 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 668.8 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@79d86bb48b6b (migration head: 20261120120000_add_onboarding_wizard_writer). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) — 🚀 AutoGPT Platform v0.12.0
<sub>2026-11-19 · 4d ago</sub>

> **⚠️ Breaking change**
> **The frontend no longer reads `TRUST_X_FORWARDED_FOR`** (#16530, @Pwuts). A self-hosted frontend that set it by hand gets no client IP from `X-Forwarded-For` for the sign-in IP log, IP blocks and per-visitor store search until `TRUSTED_PROXIES` lists the proxy in front of it. The single-container image and Vercel need nothing.
> **What to do:** if your frontend sets `TRUST_X_FORWARDED_FOR`, remove it and set `TRUSTED_PROXIES` to a comma-separated list of the addresses or CIDR ranges of the proxies in front of it. Until you do, the frontend logs a warning at start that the old setting is ignored. The same `TRUSTED_PROXIES` setting now also names the proxies for the backend and the External API's per-address limits, replacing `FORWARDED_ALLOW_IPS` and `TRUSTED_PROXY_COUNT`, which keep working but are deprecated; behind your own reverse proxy, the single-container image takes it too. See [Client IP Addresses](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/client-ip.md).
> ---
> **✨ Highlights**
> - **Get started faster.** Signing up takes fewer steps (no more typing your password twice), the sign-up and login pages show up right away, and setup no longer gets stuck on "Loading your setup…". Sign up with Google and you can connect Gmail, Drive and Calendar in the same step. (#16829, #16831, #16968, #16845, #16877)
> …

### [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3)
<sub>2026-11-15 · 9d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.3`**
> **Date:** November 15, 2026
> ---
> **🔒 Security**
> This release fixes several privately reported security issues. We'll publish the advisories once the fixes are live in production.
> ---
> …

### [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2)
<sub>2026-11-11 · 12d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.2`**
> **Date:** January 2025
> ---
> **🔥 What's New?**
> **New Features**
> - **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
> …

### [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 🚀 AutoGPT Platform v0.11.1
<sub>2026-11-06 · 18d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16416** - Self-hosted installs: `.env.default` no longer ships a Web Push (VAPID) key pair, and the backend no longer sends push notifications with the old shipped pair. Run `make init-env` to generate a pair for your install; the single-container image generates its own on first boot. Replacing the pair invalidates existing push subscriptions. `NEXT_PUBLIC_VAPID_PUBLIC_KEY` can stay blank, and the frontend then uses the backend's key (by @ntindle)
> **New Features**
> - **#11220** - Support input nodes alongside trigger nodes (by @Pwuts)
> - **#14991** - Run skills as /commands with arguments in the copilot chat (by @ntindle)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(frontend/copilot): take the send intent from the app, not the URL](https://github.com/Significant-Gravitas/AutoGPT/commit/dd0b5f73266ea5f3dfab37ebccd93049af58e106) | Pwuts |
| 2026-11-20 | [fix(platform): require an http(s) sign-in URL in the MCP OAuth flow](https://github.com/Significant-Gravitas/AutoGPT/commit/51e0547fcdb9c8307dd103f8063a3998f952e356) | Pwuts |
| 2026-11-20 | [fix(backend/executor): sub-graph runs use only the input masks of the…](https://github.com/Significant-Gravitas/AutoGPT/commit/41035ea2a14c71468f32d7ff7bc724be8703fb25) | Pwuts |
| 2026-11-20 | [fix(backend/executor): end a stopped Orchestrator's tool loop, and ru…](https://github.com/Significant-Gravitas/AutoGPT/commit/ef10f1acdf0d3b3e3435ec7eee394acac26858fc) | Pwuts |
| 2026-11-20 | [fix(blocks): route the Orchestrator CLI's model calls through a loopb…](https://github.com/Significant-Gravitas/AutoGPT/commit/1c5aec63c2ad404bb34f8ef60e9c5c54c2b3e486) | Pwuts |
| 2026-11-20 | [fix(backend/copilot): open the URL the browser host check returned](https://github.com/Significant-Gravitas/AutoGPT/commit/56b80deb4cd1341bad7db779bc513f6d14bb2d6c) | Pwuts |
| 2026-11-20 | [fix(frontend/auth): send every password reset link back to the reset …](https://github.com/Significant-Gravitas/AutoGPT/commit/74ff1298896fdb190737f1010c70651c804a9489) | Pwuts |
| 2026-11-19 | [feat(frontend): measure send-to-answer timing in chat (#15541)](https://github.com/Significant-Gravitas/AutoGPT/commit/eda70873cde1d9cb0b720bdcac8983d62f0f8d25) | ntindle |
| 2026-11-19 | [ci(platform): harden release jobs, attest images and review new depen…](https://github.com/Significant-Gravitas/AutoGPT/commit/6a42315fec58ad499f3670e3aee349a61fb3d194) | ntindle |
| 2026-11-19 | [feat(platform): connect services from the mobile app chat (#16923)](https://github.com/Significant-Gravitas/AutoGPT/commit/b217f800f13f27bb0fd73d7e5683c997ac4f2939) | 0ubbe |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
