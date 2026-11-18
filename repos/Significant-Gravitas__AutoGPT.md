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
| 🍴 **Forks** | 45.9k |
| 🐞 **Open issues + PRs** | [695](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 30% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3) — 2026-11-15 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 649.6 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@78e073749c81 (migration head: 20261112120000_account_deletion_confirmation_skipped). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3)
<sub>2026-11-15 · 3d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.3`**
> **Date:** November 15, 2026
> ---
> **🔒 Security**
> This release fixes several privately reported security issues. We'll publish the advisories once the fixes are live in production.
> ---
> …

### [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2)
<sub>2026-11-11 · 6d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.2`**
> **Date:** January 2025
> ---
> **🔥 What's New?**
> **New Features**
> - **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
> …

### [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 🚀 AutoGPT Platform v0.11.1
<sub>2026-11-06 · 12d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16416** - Self-hosted installs: `.env.default` no longer ships a Web Push (VAPID) key pair, and the backend no longer sends push notifications with the old shipped pair. Run `make init-env` to generate a pair for your install; the single-container image generates its own on first boot. Replacing the pair invalidates existing push subscriptions. `NEXT_PUBLIC_VAPID_PUBLIC_KEY` can stay blank, and the frontend then uses the backend's key (by @ntindle)
> **New Features**
> - **#11220** - Support input nodes alongside trigger nodes (by @Pwuts)
> - **#14991** - Run skills as /commands with arguments in the copilot chat (by @ntindle)
> …

### [autogpt-platform-beta-v0.11.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.0) — 🚀 AutoGPT Platform v0.11.0
<sub>2026-11-04 · 14d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16459** - Payment enforcement is now the backend setting `ENABLE_PLATFORM_PAYMENT` (default off) instead of the `enable-platform-payment` feature flag. A self-hosted install that charges must set it; `FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` and `NEXT_PUBLIC_FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` no longer do anything (by @Pwuts)
> - **#16474** - The platform API answers `413` to a request body over `MAX_REQUEST_BODY_MB` (default 10 MiB) on any route that is not an upload route or webhook ingress. Raise it, or configure media storage, if you pass larger files inline (by @Pwuts)
> - **#16522** - Behind a proxy chain whose `X-Forwarded-For` carries more than one address, list your proxies in the new `TRUSTED_PROXIES` setting (IP addresses or CIDR ranges). Left unset, per-visitor limits get no client IP instead of the header's leftmost entry. An entry that is not an IP address or CIDR range stops the frontend from starting (by @Pwuts)
> - **#15853** - LaunchDarkly support is removed and every feature flag is read from PostHog. `LAUNCH_DARKLY_SDK_KEY`, `FEATURE_FLAG_BACKEND`, `NEXT_PUBLIC_LAUNCHDARKLY_ENABLED`, `NEXT_PUBLIC_LAUNCHDARKLY_CLIENT_ID` and `NEXT_PUBLIC_FEATURE_FLAG_BACKEND` are ignored; without PostHog every flag is its default (by @kcze)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-15 | [fix(backend): stub the new role check in the webhook-preset route tes…](https://github.com/Significant-Gravitas/AutoGPT/commit/657153887ea25aca92014ee713f9ceb344378e74) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/b05a6296a82c42cfb524f1b022c3d6559f22035b) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/36b8a54561e720658c09509c25bc42318632ecd3) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/f2cc414a1d785998872ce7993c45574a212db219) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/7c75f6640c653289ccb5938771c20d8534045e00) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/1d641f6e5df2c5e4ae24969b8a565646ec338834) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/f83734a4318567ce8a01052bacc29fd9d9ca0da9) | ntindle |
| 2026-11-15 | [Merge commit from fork](https://github.com/Significant-Gravitas/AutoGPT/commit/43017c38b2d3ed2f736d6307e49e6f386b42d8f6) | ntindle |
| 2026-11-15 | [chore(libs/deps): bump the production-dependencies group across 1 dir…](https://github.com/Significant-Gravitas/AutoGPT/commit/80e02a5e7697b29330159393a31ce5678b76e4cb) | dependabot[bot] |
| 2026-11-14 | [fix(backend/scheduler): stop skipping runs of agent schedules stored …](https://github.com/Significant-Gravitas/AutoGPT/commit/93d5ab1abbcd5dcdf11432ca9c5af48fa2eb9f32) | Pwuts |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
