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
| 🐞 **Open issues + PRs** | [715](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 31% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-11 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 2026-11-06 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 626.7 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@2dbf60b8eca5 (migration head: 20261109120000_add_feedback_prompt). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.11.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.1) — 🚀 AutoGPT Platform v0.11.1
<sub>2026-11-06 · 5d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16416** - Self-hosted installs: `.env.default` no longer ships a Web Push (VAPID) key pair, and the backend no longer sends push notifications with the old shipped pair. Run `make init-env` to generate a pair for your install; the single-container image generates its own on first boot. Replacing the pair invalidates existing push subscriptions. `NEXT_PUBLIC_VAPID_PUBLIC_KEY` can stay blank, and the frontend then uses the backend's key (by @ntindle)
> **New Features**
> - **#11220** - Support input nodes alongside trigger nodes (by @Pwuts)
> - **#14991** - Run skills as /commands with arguments in the copilot chat (by @ntindle)
> …

### [autogpt-platform-beta-v0.11.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.0) — 🚀 AutoGPT Platform v0.11.0
<sub>2026-11-04 · 7d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#16459** - Payment enforcement is now the backend setting `ENABLE_PLATFORM_PAYMENT` (default off) instead of the `enable-platform-payment` feature flag. A self-hosted install that charges must set it; `FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` and `NEXT_PUBLIC_FORCE_FLAG_ENABLE_PLATFORM_PAYMENT` no longer do anything (by @Pwuts)
> - **#16474** - The platform API answers `413` to a request body over `MAX_REQUEST_BODY_MB` (default 10 MiB) on any route that is not an upload route or webhook ingress. Raise it, or configure media storage, if you pass larger files inline (by @Pwuts)
> - **#16522** - Behind a proxy chain whose `X-Forwarded-For` carries more than one address, list your proxies in the new `TRUSTED_PROXIES` setting (IP addresses or CIDR ranges). Left unset, per-visitor limits get no client IP instead of the header's leftmost entry. An entry that is not an IP address or CIDR range stops the frontend from starting (by @Pwuts)
> - **#15853** - LaunchDarkly support is removed and every feature flag is read from PostHog. `LAUNCH_DARKLY_SDK_KEY`, `FEATURE_FLAG_BACKEND`, `NEXT_PUBLIC_LAUNCHDARKLY_ENABLED`, `NEXT_PUBLIC_LAUNCHDARKLY_CLIENT_ID` and `NEXT_PUBLIC_FEATURE_FLAG_BACKEND` are ignored; without PostHog every flag is its default (by @kcze)
> …

### [autogpt-platform-beta-v0.10.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.10.0) — 🚀 AutoGPT Platform v0.10.0
<sub>2026-10-27 · 14d ago</sub>

> **🔥 What's New?**
> **⚠️ Breaking Changes**
> - **#15970** - Self-hosted Docker Compose generates its own service passwords per install and won't start without them: run `make init-env` (or the installer) before `docker compose up`. PostgreSQL, RabbitMQ, Redis, FalkorDB and ClamAV now listen on `127.0.0.1` only. Existing installs: see [Upgrading: service passwords are generated per install](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/getting-started.md#upgrading-service-passwords-are-generated-per-install) (by @ntindle)
> - **#12206** - External API v1 is deprecated in favour of the new v2, and keeps working until 2027-01-31 (by @Pwuts)
> **New Features**
> - **#15990** - Record when each API key was last used (by @ntindle)
> …

### [autogpt-platform-beta-v0.9.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.9.0) — 🚀 Release `autogpt-platform-beta-v0.9.0`
<sub>2026-10-23 · 19d ago</sub>

> **🔥 What's New?**
> **New Features**
> - **#15824** - Add measures and admin tools against multi-account abuse (by @Pwuts)
> - **#14553** - Self-host from the Docker Hub image, with a Windows installer (by @ntindle)
> - **#14981** - Every block declares its effect; Auto judges cheap outward actions and asks first on costly ones (by @Pwuts)
> - **#15675** - Add admin users page to look up, ban and impersonate a user, with rate limits folded in (by @Pwuts)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-05 | [docs(platform): Changelog v0.11.0 (#16651)](https://github.com/Significant-Gravitas/AutoGPT/commit/9cb76f9026d388c9bf2e098af2beae1cc864f055) | itsababseh |
| 2026-11-05 | [feat(blocks): add Treg blocks for people, company and web data (#16393)](https://github.com/Significant-Gravitas/AutoGPT/commit/30a2ba122119518259d0c30696cc5e86942136f1) | Torantulino |
| 2026-11-05 | [fix(backend/copilot): admit a chat turn in one statement after its lo…](https://github.com/Significant-Gravitas/AutoGPT/commit/5396938150abd99ff5fb01f8922b9a864c4e4496) | ntindle |
| 2026-11-05 | [docs(platform): Changelog v0.10.0 (#16315)](https://github.com/Significant-Gravitas/AutoGPT/commit/0865d245d265a46824094afa3f248e128a9a5d0f) | itsababseh |
| 2026-11-05 | [fix(backend/copilot): reuse expert checks within a turn (#15534)](https://github.com/Significant-Gravitas/AutoGPT/commit/afb5149fb82c875fb83823bbecd15dd5f1acceb5) | ntindle |
| 2026-11-05 | [fix(backend): hide bash tool without a supported sandbox (#16455)](https://github.com/Significant-Gravitas/AutoGPT/commit/ba17311fd83b292210e918f8ad8d90f07b5e38ad) | ntindle |
| 2026-11-05 | [fix(backend): validate the configured Claude CLI before subscription …](https://github.com/Significant-Gravitas/AutoGPT/commit/b2e895bcd4408ebcd93212db06636bdd94dd9143) | ntindle |
| 2026-11-05 | [fix(frontend): separate graph memory availability from skill learning…](https://github.com/Significant-Gravitas/AutoGPT/commit/b03a0cfa7d956d63864a338f67ea9fa9658b96fe) | ntindle |
| 2026-11-05 | [fix(platform): support atomic runtime config writes on Windows (#16450)](https://github.com/Significant-Gravitas/AutoGPT/commit/7695bf3a3387a919d7ad4b9632d056732f4a98f5) | ntindle |
| 2026-11-05 | [fix(backend): normalize configurable copilot workspace prefixes (#16454)](https://github.com/Significant-Gravitas/AutoGPT/commit/b5409778fbaa5be2c51b841694dbbfe4b3892ce6) | ntindle |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
