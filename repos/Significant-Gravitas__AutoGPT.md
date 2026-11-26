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
| 🐞 **Open issues + PRs** | [805](https://github.com/Significant-Gravitas/AutoGPT/issues) |
| 💻 **Languages** | Python 68% · TypeScript 31% |
| 📜 **License** | Other |
| 🏷 **Topics** | `ai` `openai` `python` `artificial-intelligence` `autonomous-agents` `llama-api` `agentic-ai` `agents` `llm` `claude` `gpt` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2023-03-16 |
| 📦 **Latest release** | [autogpt-platform-beta-v0.12.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.1) — 2026-11-26 |
| 🌿 **Default branch** | `master` |
| 💾 **Size** | 673.2 MB |
| 🌐 **Website** | https://agpt.co |

## 📦 Recent releases

### [preview-seed-fixture](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/preview-seed-fixture) — Preview seed fixture (rolling) _(pre-release)_
<sub>2026-08-06 · 3mo ago</sub>

> Rolling, fully SYNTHETIC preview-database seed fixture baked from dev@39cc96026f5a (migration head: 20261120120000_add_onboarding_wizard_writer). Preview environments restore fixture.dump.gz (custom-format, gzipped, platform schema only, including _prisma_migrations) BEFORE running a PR's own migrations, so schema changes run against populated tables. RESTORE: apply restore-preamble.sql to the target database first (it creates the platform schema and installs the vector + pg_trgm extensions into it, which pg_dump --schema=platform omits), then run 'gunzip -c fixture.dump.gz | pg_restore -d <db> --no-owner' WITHOUT --exit-on-error (the dump's own CREATE SCHEMA collides benignly with the preamble's). SECURITY INVARIANT: this bake holds no cloud credentials and has no read path to any real database — it runs entirely against a throwaway Postgres container and contains only synthetic rows (Faker-generated, plus the hand-written preview marketplace) and the already-public marketplace agent exports checked into autogpt_platform/backend/agents/. This asset is regenerated on every eligible dev push and weekly; treat it as disposable.

### [autogpt-platform-beta-v0.12.1](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.1) — 🚀 AutoGPT Platform v0.12.1
<sub>2026-11-26 · today</sub>

> **✨ Highlights**
> - **Connected from the moment you sign in.** Continue with Google or Continue with Microsoft now connects your email, files and calendar on the same screen, so Otto can use them from your first chat with no extra setup step. (#16882)
> - **More services for Otto.** Otto can now connect to Attio and Neon. Skills show each service under its own name and logo, and recognise a service you've already connected instead of asking you to connect it again. (#16950, #17265, #17340, #17333, #17347)
> - **Chats that keep up with you.** If your connection drops as you hit Send, Otto now offers Send again instead of losing your message. A message you send while Otto is still finishing its answer gets a reply of its own, in a chat with Otto, in the builder and in Memory. A chat open in another tab shows new replies without a reload, and after you press Stop, your next message goes straight through. (#17369, #17249, #17251, #16504, #17365, #17292)
> ---
> **🔒 Security**
> …

### [autogpt-platform-beta-v0.12.0](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.12.0) — 🚀 AutoGPT Platform v0.12.0
<sub>2026-11-19 · 6d ago</sub>

> **⚠️ Breaking change**
> **The frontend no longer reads `TRUST_X_FORWARDED_FOR`** (#16530, @Pwuts). A self-hosted frontend that set it by hand gets no client IP from `X-Forwarded-For` for the sign-in IP log, IP blocks and per-visitor store search until `TRUSTED_PROXIES` lists the proxy in front of it. The single-container image and Vercel need nothing.
> **What to do:** if your frontend sets `TRUST_X_FORWARDED_FOR`, remove it and set `TRUSTED_PROXIES` to a comma-separated list of the addresses or CIDR ranges of the proxies in front of it. Until you do, the frontend logs a warning at start that the old setting is ignored. The same `TRUSTED_PROXIES` setting now also names the proxies for the backend and the External API's per-address limits, replacing `FORWARDED_ALLOW_IPS` and `TRUSTED_PROXY_COUNT`, which keep working but are deprecated; behind your own reverse proxy, the single-container image takes it too. See [Client IP Addresses](https://github.com/Significant-Gravitas/AutoGPT/blob/master/docs/platform/client-ip.md).
> ---
> **✨ Highlights**
> - **Get started faster.** Signing up takes fewer steps (no more typing your password twice), the sign-up and login pages show up right away, and setup no longer gets stuck on "Loading your setup…". Sign up with Google and you can connect Gmail, Drive and Calendar in the same step. (#16829, #16831, #16968, #16845, #16877)
> …

### [autogpt-platform-beta-v0.11.3](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.3)
<sub>2026-11-15 · 11d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.3`**
> **Date:** November 15, 2026
> ---
> **🔒 Security**
> This release fixes several privately reported security issues. We'll publish the advisories once the fixes are live in production.
> ---
> …

### [autogpt-platform-beta-v0.11.2](https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.11.2)
<sub>2026-11-11 · 14d ago</sub>

> **🚀 Release `autogpt-platform-beta-v0.11.2`**
> **Date:** January 2025
> ---
> **🔥 What's New?**
> **New Features**
> - **#16308** - Plan-first trial: starter tasks and experts on the paywall, hire step removed, team hired on trial start, Home starts with ranked tasks owned by experts (by @itsababseh)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [fix(backend): re-check a scheduled copilot turn's organization when i…](https://github.com/Significant-Gravitas/AutoGPT/commit/0a0e0111fa9bca0bce3f932dfdde7c77338c96be) | Pwuts |
| 2026-11-26 | [fix(backend): act in the personal organization for v1 credentials wit…](https://github.com/Significant-Gravitas/AutoGPT/commit/373267241d0457b343ab2350ee59afbf63ce4713) | Pwuts |
| 2026-11-26 | [test(backend): fix two remainder-shard tests red on dev (#17439)](https://github.com/Significant-Gravitas/AutoGPT/commit/4eb7f6794e638f3e3969e8624e943707c07a424b) | Pwuts |
| 2026-11-26 | [fix(blocks): route the Claude Code block's model calls through a plat…](https://github.com/Significant-Gravitas/AutoGPT/commit/e93a33806f59b979b1b3dbdd6d347e08e43f230f) | Pwuts |
| 2026-11-26 | [fix(backend/copilot): count desktops opened from the Computer tab aga…](https://github.com/Significant-Gravitas/AutoGPT/commit/0230bbd364da02065f1404d261819bafd6417849) | Pwuts |
| 2026-11-26 | [fix(backend/executor): hold a usage-priced block's cost before it runs](https://github.com/Significant-Gravitas/AutoGPT/commit/80259593f9b8dcec652b39d2214910b45661466a) | Pwuts |
| 2026-11-26 | [fix(backend/copilot): share a ledger's balance among the AutoPilot bl…](https://github.com/Significant-Gravitas/AutoGPT/commit/bd9091ce045cef7fc9107b646dd23fee98487eef) | Pwuts |
| 2026-11-26 | [fix(backend/executor): price a block on its input coerced to the bloc…](https://github.com/Significant-Gravitas/AutoGPT/commit/dca249a9a2bef19039f3f593ae343602bce0a439) | Pwuts |
| 2026-11-26 | [fix(backend/executor): bill model requests cut off by a run's known f…](https://github.com/Significant-Gravitas/AutoGPT/commit/6be0e1c447b2fc6406d0468013a312c6f061132a) | Pwuts |
| 2026-11-26 | [fix(backend): apply org roles to private submission media reads (#17414)](https://github.com/Significant-Gravitas/AutoGPT/commit/5144d56c99506665021f4e5608cec906fabd3680) | Pwuts |

[See all commits ↗](https://github.com/Significant-Gravitas/AutoGPT/commits)

## ⬇️ Get it

```bash
git clone https://github.com/Significant-Gravitas/AutoGPT.git
```
