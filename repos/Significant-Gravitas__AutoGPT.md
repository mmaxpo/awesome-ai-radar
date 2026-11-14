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
| ⭐ **Stars** | 188.0k |
| 🍴 **Forks** | 45.9k |
| 🐞 **Open issues + PRs** | [681](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 31% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2) — 2026-11-11 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 647.7 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@6ba94560676d (migration head: 20261112120000_account_deletion_confirmation_skipped). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2)
<sub>2026-11-11 · 2d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.2`**
> **Date:** January 2025
> ---
> **🔥 What's New?**
> **New Features**
> - **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
> …

### [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 🚀 AutoGPT Platform v0.11.1
<sub>2026-11-06 · 8d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16416** - Self-hosted installs: `.env.default` no longer ships a Web Push (VAPID) key pair, and the backend no longer sends push notifications with the old shipped pair. Run `make init-env` to generate a pair for your install; the single-container image generates its own on first boot. Replacing the pair invalidates existing push subscriptions. `NEXT_PUBLIC_VAPID_PUBLIC_KEY` can stay blank, and the frontend then uses the backend's key (by @ntindle)
> **New Features**
> - **#11220** - Support input nodes alongside trigger nodes (by @Pwuts)
> - **#14991** - Run skills as /commands with arguments in the copilot chat (by @ntindle)
> …

### [autogpt-platform-beta-v0.11.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.0) — 🚀 AutoGPT Platform v0.11.0
<sub>2026-11-04 · 10d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16459** - Payment enforcement is now the backend setting `ENABLE_PLATFORM_PAYMENT` (default off) instead of the `enable-platform-payment` feature flag. A self-hosted install that charges must set it; `FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` and `NEXT_PUBLIC_FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` no longer do anything (by @Pwuts)
> - **#16474** - The platform API answers `413` to a request body over `MAX_REQUEST_BODY_MB` (default 10 MiB) on any route that is not an upload route or webhook ingress. Raise it, or configure media storage, if you pass larger files inline (by @Pwuts)
> - **#16522** - Behind a proxy chain whose `X-Forwarded-For` carries more than one address, list your proxies in the new `TRUSTED_PROXIES` setting (IP addresses or CIDR ranges). Left unset, per-visitor limits get no client IP instead of the header's leftmost entry. An entry that is not an IP address or CIDR range stops the frontend from starting (by @Pwuts)
> - **#15853** - LaunchDarkly support is removed and every feature flag is read from PostHog. `LAUNCH_DARKLY_SDK_KEY`, `FEATURE_FLAG_BACKEND`, `NEXT_PUBLIC_LAUNCHDARKLY_ENABLED`, `NEXT_PUBLIC_LAUNCHDARKLY_CLIENT_ID` and `NEXT_PUBLIC_FEATURE_FLAG_BACKEND` are ignored; without PostHog every flag is its default (by @kcze)
> …

### [autogpt-platform-beta-v0.10.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.10.0) — 🚀 AutoGPT Platform v0.10.0
<sub>2026-10-27 · 17d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#15970** - Self-hosted Docker Compose generates its own service passwords per install and won't start without them: run `make init-env` (or the installer) before `docker compose up`. PostgreSQL, RabbitMQ, Redis, FalkorDB and ClamAV now listen on `127.0.0.1` only. Existing installs: see [Upgrading: service passwords are generated per install](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/getting-started.md#upgrading-service-passwords-are-generated-per-install) (by @ntindle)
> - **#12206** - External API v1 is deprecated in favour of the new v2, and keeps working until 2027-01-31 (by @Pwuts)
> **New Features**
> - **#15990** - Record when each API key was last used (by @ntindle)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-11 | [fix(frontend): say when a JSON field holds a number too long to keep …](https://github.com/Significant-Gravitas/AutoGPT/commit/ac4e88888d3838fd5790dff2a85845a654d05024) | 0ubbe |
| 2026-11-11 | [fix(backend): let a run leave an input blank when Advanced is on (#16…](https://github.com/Significant-Gravitas/AutoGPT/commit/9789d6d655efabea1bc04b1dd726a1c47f51b884) | 0ubbe |
| 2026-11-11 | [fix(backend): account erasure deletes the account's chats (SECRT-2854…](https://github.com/Significant-Gravitas/AutoGPT/commit/06340e194f3f182b184597dd7dc70a70e49ab015) | kcze |
| 2026-11-11 | [docs(platform): document every rate limit, and how the Platform finds…](https://github.com/Significant-Gravitas/AutoGPT/commit/b6e79fc245779706d53f3afac60d718afe2bd0b3) | Pwuts |
| 2026-11-11 | [fix(platform): treat the platform's SDK keys (Firecrawl, DataForSEO, …](https://github.com/Significant-Gravitas/AutoGPT/commit/e6a91ab7bd149743cd2da7760f6fe57f8b3b4270) | Torantulino |
| 2026-11-11 | [fix(blocks): mark Exa Create Research as an external action (#16707)](https://github.com/Significant-Gravitas/AutoGPT/commit/d4fbbacbeb65f9b94c356a847f3ba29212495c0e) | 0ubbe |
| 2026-11-11 | [feat(platform): erase closed accounts after #15459's 14 days, keeping…](https://github.com/Significant-Gravitas/AutoGPT/commit/2dbf60b8eca52cb4139980d2955872c8260fc4eb) | kcze |
| 2026-11-11 | [ci(platform): read the single-container build cache from the final ba…](https://github.com/Significant-Gravitas/AutoGPT/commit/3b661c618d28b4c9ff0b4ec35cd0859612f2bc1c) | Bentlybro |
| 2026-11-11 | [feat(blocks): let the HubSpot blocks sign in with HubSpot OAuth (#15454)](https://github.com/Significant-Gravitas/AutoGPT/commit/4a0c419cd9725b1b48edb2b3b1068e3c191391cb) | Bentlybro |
| 2026-11-11 | [fix(backend): an expert run with a failed step reports failed, not co…](https://github.com/Significant-Gravitas/AutoGPT/commit/5c9519b8fe39ea1379ea8efc13132c1ea9401231) | Bentlybro |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
