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
| ⭐ **Stars** | 15.4k |
| 🍴 **Forks** | 1.8k |
| 🐞 **Open issues + PRs** | [15](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 87% · PowerShell 7% · Shell 6% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-21 (today) |
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
| 2026-11-21 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/8258d29726804f5b954a09c625caedc183f7130d) | github-actions[bot] |
| 2026-11-20 | [fix(cbh): report draft leaks OS login; steps heading + platform alias…](https://github.com/elementalsouls/Claude-BugHunter/commit/c5d5c38123bf01f1223da3225bd3d28a930d028f) | elementalsouls |
| 2026-11-20 | [fix(windows): make PowerShell scripts ASCII-only (PS 5.1 parse crash)…](https://github.com/elementalsouls/Claude-BugHunter/commit/9ff08590cb75ca59adf3a2e319e9908cd8ff2f53) | elementalsouls |
| 2026-11-20 | [fix(engine): utf-8 encoding for all file/console I/O (Windows cp1252 …](https://github.com/elementalsouls/Claude-BugHunter/commit/dbb9a590e558b9524e51c07c65d9460530d741e2) | elementalsouls |
| 2026-11-20 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/de07e0138176888e8ac8ba57cf6153a791b3b85f) | github-actions[bot] |
| 2026-11-20 | [feat(mcp): add get_report tool for live disclosed-report bodies (#187)](https://github.com/elementalsouls/Claude-BugHunter/commit/5b7e76eb8e2b2a2793686c74ad53b7b57bdee6c2) | elementalsouls |
| 2026-11-19 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/0e70a021e59d6875004e7a563f8511aca2ba3bc1) | github-actions[bot] |
| 2026-11-18 | [docs(readme): note that the HackerOne account is optional (#176)](https://github.com/elementalsouls/Claude-BugHunter/commit/9bdb0a81658bc25f09c0b52d31fcde923d126e4f) | sm18lr88 |
| 2026-11-18 | [docs(plugin): say what the HackerOne prompts are for and that they ca…](https://github.com/elementalsouls/Claude-BugHunter/commit/ce528f6d446b0b8e45539b2c7cd06003128c6c62) | sm18lr88 |
| 2026-11-18 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369) | github-actions[bot] |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
