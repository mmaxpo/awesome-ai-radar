# elementalsouls/Claude-BugHunter

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/elementalsouls/Claude-BugHunter)

> A Claude Code skill bundle for bug hunting and external red-team work - 82 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛡 Security & OSINT |
| **Project** | — |
| **Why it's worth a look** | Claude Code skill bundle for bug hunting and red teaming |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 8.4k |
| 🍴 **Forks** | 1.3k |
| 🐞 **Open issues + PRs** | [8](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 86% · PowerShell 8% · Shell 6% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-05-05 |
| 📦 **Latest release** | [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — 2026-06-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3.6 MB |
| 🌐 **Website** | https://elementalsouls.github.io/Claude-BugHunter |

## 📦 Recent releases

### [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — v2.1 — community skills · CI gate · security fixes
<sub>2026-06-05 · 5mo ago</sub>

> Second major bundle release. **51 → 71 skills**, a CI quality/safety gate, a docs site, and security fixes to the toolkit's own code.
> **✨ Added**
> - **20 new `hunt-*` skills** (community v3 expansion — thanks @muhsiindeniiz): `hunt-lfi`, `hunt-nosqli`, `hunt-deserialization`, `hunt-cors`, `hunt-host-header`, `hunt-open-redirect`, `hunt-brute-force`, `hunt-session`, `hunt-ldap`, `hunt-nextjs`, `hunt-nodejs`, `hunt-dom`, `hunt-websocket`, `hunt-grpc`, `hunt-laravel`, `hunt-springboot`, `hunt-k8s`, `hunt-cicd`, `hunt-source-leak`, `hunt-tls-network`. (28 → 48 hunt modules.)
> - **CI skill-linter** — validates every `SKILL.md` and blocks leaked secrets + client/engagement identifiers (SHA-256 denylist; plaintext names never enter the repo).
> - **Docs site** — GitHub Pages under `docs/` with a searchable, auto-generated [skill catalog](https://github.com/elementalsouls/Claude-BugHunter/blob/main/docs/skills.md).
> - **Community infrastructure** — issue/PR templates, `CODEOWNERS`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `FUNDING.yml`.
> …

### [v2.0](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.0) — v2.0 — report-curation + 5 missing surfaces + chains + engagements
<sub>2026-05-25 · 5mo ago</sub>

> Workstream A — Report-curation backfill across 11 hunt-* skills.
>   hunt-graphql 3 -> 12 | hunt-race-condition 3 -> 12 | hunt-xxe 4 -> 10
>   hunt-cache-poison 4 -> 10 | hunt-auth-bypass 4 -> 12 | hunt-business-logic 7 -> 12
>   hunt-sqli 8 -> 12 | hunt-ssrf 9 -> 15 | hunt-csrf 10 -> 15
>   hunt-oauth 10 -> 19 | hunt-subdomain 11 -> 15.
>   Citations are primary-source URLs (HackerOne reports, GitHub Security
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/5d91c812ee25efc0c1d5191377632e3aed7e8d2d) | github-actions[bot] |
| 2026-11-16 | [fix(engine): close coverage only after every endpoint work item has a…](https://github.com/elementalsouls/Claude-BugHunter/commit/64410edb7f445e1837665e2fd713d47958a51094) | rudycelekli |
| 2026-11-16 | [fix(engine): resume validation without rechecking rejected candidates…](https://github.com/elementalsouls/Claude-BugHunter/commit/a261142827a1d9c31d24824a6a99d7410ea82053) | rudycelekli |
| 2026-11-16 | [fix(engine): isolate mock reports and checkpoints from live engagemen…](https://github.com/elementalsouls/Claude-BugHunter/commit/d82e9b7a99f04a74b22567fdd2c7acedbd4dbba8) | rudycelekli |
| 2026-11-16 | [fix(engine): guarantee the default OpenAPI sweep skips write methods …](https://github.com/elementalsouls/Claude-BugHunter/commit/ffae460b4713d80510845c629fbf56f5eae53f6a) | rudycelekli |
| 2026-11-16 | [fix(report): preserve heading-like evidence inside Markdown fences (#…](https://github.com/elementalsouls/Claude-BugHunter/commit/c95dee6c24071a9e483bd5c40a2566cf05a5d27b) | rudycelekli |
| 2026-11-16 | [fix(recon): record redirects without following their destinations (#149)](https://github.com/elementalsouls/Claude-BugHunter/commit/8c902b0bbcb033e3e70280aa587184885e954c5a) | rudycelekli |
| 2026-11-16 | [fix(recon): constrain passive candidates to the requested domain (#148)](https://github.com/elementalsouls/Claude-BugHunter/commit/66e0114eb385bf5fde9e7e2363989846a002cdb7) | rudycelekli |
| 2026-11-16 | [fix(mcp): preserve malformed JSON configs and continue wiring other h…](https://github.com/elementalsouls/Claude-BugHunter/commit/c516518129d1e64f8ed5901834050b85e9d6d02e) | rudycelekli |
| 2026-11-16 | [fix(scaffold): keep Bash engagement creation usable with malformed re…](https://github.com/elementalsouls/Claude-BugHunter/commit/cb12a50b4fec680be9b2b81cf9b568243db40764) | rudycelekli |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
