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
| ⭐ **Stars** | 188.1k |
| 🍴 **Forks** | 45.8k |
| 🐞 **Open issues + PRs** | [777](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 31% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) — 2026-11-19 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 665.6 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@9c2d9e1a523b (migration head: 20261112120000_account_deletion_confirmation_skipped). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) — 🚀 AutoGPT Platform v0.12.0
<sub>2026-11-19 · today</sub>

> **⚠️ Breaking change**
> **The frontend no longer reads `TRUST_X_FORWARDED_FOR`** (#16530, @Pwuts). A self-hosted frontend that set it by hand gets no client IP from `X-Forwarded-For` for the sign-in IP log, IP blocks and per-visitor store search until `TRUSTED_PROXIES` lists the proxy in front of it. The single-container image and Vercel need nothing.
> **What to do:** if your frontend sets `TRUST_X_FORWARDED_FOR`, remove it and set `TRUSTED_PROXIES` to a comma-separated list of the addresses or CIDR ranges of the proxies in front of it. Until you do, the frontend logs a warning at start that the old setting is ignored. The same `TRUSTED_PROXIES` setting now also names the proxies for the backend and the External API's per-address limits, replacing `FORWARDED_ALLOW_IPS` and `TRUSTED_PROXY_COUNT`, which keep working but are deprecated; behind your own reverse proxy, the single-container image takes it too. See [Client IP Addresses](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/client-ip.md).
> ---
> **✨ Highlights**
> - **Get started faster.** Signing up takes fewer steps (no more typing your password twice), the sign-up and login pages show up right away, and setup no longer gets stuck on "Loading your setup…". Sign up with Google and you can connect Gmail, Drive and Calendar in the same step. (#16829, #16831, #16968, #16845, #16877)
> …

### [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3)
<sub>2026-11-15 · 5d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.3`**
> **Date:** November 15, 2026
> ---
> **🔒 Security**
> This release fixes several privately reported security issues. We'll publish the advisories once the fixes are live in production.
> ---
> …

### [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2)
<sub>2026-11-11 · 8d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.2`**
> **Date:** January 2025
> ---
> **🔥 What's New?**
> **New Features**
> - **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
> …

### [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 🚀 AutoGPT Platform v0.11.1
<sub>2026-11-06 · 14d ago</sub>

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
| 2026-11-19 | [feat(frontend): measure send-to-answer timing in chat (#15541)](https://github.com/Significant-Gravitas/AutoGPT/commit/eda70873cde1d9cb0b720bdcac8983d62f0f8d25) | ntindle |
| 2026-11-19 | [ci(platform): harden release jobs, attest images and review new depen…](https://github.com/Significant-Gravitas/AutoGPT/commit/6a42315fec58ad499f3670e3aee349a61fb3d194) | ntindle |
| 2026-11-19 | [feat(platform): connect services from the mobile app chat (#16923)](https://github.com/Significant-Gravitas/AutoGPT/commit/b217f800f13f27bb0fd73d7e5683c997ac4f2939) | 0ubbe |
| 2026-11-19 | [feat(backend): measure first answer timing separately from model acti…](https://github.com/Significant-Gravitas/AutoGPT/commit/2adcd0b5a9ccc8850548ce5abbd6d05eaa867771) | ntindle |
| 2026-11-19 | [feat(frontend/copilot): send again a message the chat couldn't confir…](https://github.com/Significant-Gravitas/AutoGPT/commit/58d903c2bb584d9f936acab68057f55e783a17ba) | ntindle |
| 2026-11-19 | [feat(platform): turn the mobile chat input's mic into a recording orb…](https://github.com/Significant-Gravitas/AutoGPT/commit/c9f593da688c70b24f3a23f0cdb23cdfee829f8d) | 0ubbe |
| 2026-11-19 | [fix(frontend): prevent translation extensions from breaking suggested…](https://github.com/Significant-Gravitas/AutoGPT/commit/bd04f550aab1e89cb556e6e240f675a974d8d492) | sentry[bot] |
| 2026-11-19 | [fix(frontend): save the builder graph from one loaded snapshot after …](https://github.com/Significant-Gravitas/AutoGPT/commit/c055303d9681a14db2974cb7ec45f264e8fe683f) | ntindle |
| 2026-11-19 | [feat(platform): a provider joins an existing account only for its own…](https://github.com/Significant-Gravitas/AutoGPT/commit/36474d67a4e248a4c6379042184fd89b4fce76ed) | ntindle |
| 2026-11-19 | [fix(backend/copilot): tell Otto a refused tool call did not happen (#…](https://github.com/Significant-Gravitas/AutoGPT/commit/8d9dc278063c0820646d333c79e30d82387cb3f1) | kcze |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
