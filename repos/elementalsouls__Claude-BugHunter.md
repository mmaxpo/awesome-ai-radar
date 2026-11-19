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
| ⭐ **Stars** | 11.9k |
| 🍴 **Forks** | 1.6k |
| 🐞 **Open issues + PRs** | [5](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 87% · PowerShell 7% · Shell 6% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-19 (today) |
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
| 2026-11-19 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/0e70a021e59d6875004e7a563f8511aca2ba3bc1) | github-actions[bot] |
| 2026-11-18 | [docs(readme): note that the HackerOne account is optional (#176)](https://github.com/elementalsouls/Claude-BugHunter/commit/9bdb0a81658bc25f09c0b52d31fcde923d126e4f) | sm18lr88 |
| 2026-11-18 | [docs(plugin): say what the HackerOne prompts are for and that they ca…](https://github.com/elementalsouls/Claude-BugHunter/commit/ce528f6d446b0b8e45539b2c7cd06003128c6c62) | sm18lr88 |
| 2026-11-18 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369) | github-actions[bot] |
| 2026-11-18 | [feat(mcp): wire the HackerOne MCP into all harnesses like Burp (#165)](https://github.com/elementalsouls/Claude-BugHunter/commit/315c0623c34403f7a2b907eee85398512bb4f72e) | elementalsouls |
| 2026-11-18 | [docs: regenerate skills.md report counts from current main (#164)](https://github.com/elementalsouls/Claude-BugHunter/commit/979f521335f9e33852559b0c880db547ad8167f8) | elementalsouls |
| 2026-11-18 | [fix(mcp): harden HackerOne MCP server (pagination DoS, protocol negot…](https://github.com/elementalsouls/Claude-BugHunter/commit/52d08634d6a503325ac9acd28f35e0ee9fef52c9) | elementalsouls |
| 2026-11-18 | [feat(mcp): add a HackerOne MCP server (closes #151) (#162)](https://github.com/elementalsouls/Claude-BugHunter/commit/cc19ed87f0c0df52c871c9cf372229243ff6d5db) | ItsRenjiii |
| 2026-11-18 | [fix(engine,cli): cross-platform Windows support, utf-8 file writing, …](https://github.com/elementalsouls/Claude-BugHunter/commit/3c43bf8c92c53ad9c2b6ad2b9dca622299d34a34) | parveen0029 |
| 2026-11-18 | [fix(scope): reduce URL bullets in scope.md to their host (#155)](https://github.com/elementalsouls/Claude-BugHunter/commit/bf066585aebaa88a621d0f69095789f06c08824e) | ege-arhan |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
