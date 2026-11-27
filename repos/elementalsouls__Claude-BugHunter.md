# elementalsouls/Claude-BugHunter

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/elementalsouls/Claude-BugHunter)

> A Claude Code skill bundle for bug hunting and external red-team work - 85 skills, 16 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.

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
| ⭐ **Stars** | 25.6k |
| 🍴 **Forks** | 2.6k |
| 🐞 **Open issues + PRs** | [16](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 91% · PowerShell 5% · Shell 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-27 (today) |
| 📅 **Created** | 2026-05-05 |
| 📦 **Latest release** | [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — 2026-06-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 5.0 MB |
| 🌐 **Website** | https://elementalsouls.github.io/Claude-BugHunter/ |

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
<sub>2026-05-25 · 6mo ago</sub>

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
| 2026-11-27 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/9b7fc8dcf599a48f5f986971fdc62146a7f5a431) | github-actions[bot] |
| 2026-11-27 | [ci(install-smoke): fix PowerShell hunt-reject step exit code + widen …](https://github.com/elementalsouls/Claude-BugHunter/commit/49cfc2aa8d87adf8fa3d540d2eea7aca02e9e3b4) | elementalsouls |
| 2026-11-27 | [fix: close 4 audit gaps + a live stale banner count (in-house)](https://github.com/elementalsouls/Claude-BugHunter/commit/b2140b84b9c025dcb5ce4feac6b5d294cb61caa9) | elementalsouls |
| 2026-11-27 | [docs: lead cbh install with the released PyPI package (#211)](https://github.com/elementalsouls/Claude-BugHunter/commit/166dd9bb737a396ae7a32f4497108c0b5a98599a) | elementalsouls |
| 2026-11-27 | [docs: scrub local account name from an SSTI PoC `id` output](https://github.com/elementalsouls/Claude-BugHunter/commit/c73e5b3b57556206f82be349ee990249bfab6918) | elementalsouls |
| 2026-11-27 | [ci(release): add PyPI Trusted-Publishing workflow for the cbh CLI (#211)](https://github.com/elementalsouls/Claude-BugHunter/commit/49ab711ccfecd9ebdcbc4048c6efcad72595467b) | elementalsouls |
| 2026-11-27 | [fix(skills): replace upstream install block with the bundle's own ins…](https://github.com/elementalsouls/Claude-BugHunter/commit/76ef5886fb654eaa812f50a27f19035d4e060035) | elementalsouls |
| 2026-11-27 | [fix: in-house batch — scope CIDR-comment fail-open, hunt path escape,…](https://github.com/elementalsouls/Claude-BugHunter/commit/0a88d485f234a9191f9d1038efe62cd78899d311) | elementalsouls |
| 2026-11-27 | [fix(security): close 5 fail-open scope / off-scope-request holes (rep…](https://github.com/elementalsouls/Claude-BugHunter/commit/063874d1c44637a76be978d207de6c98becf7421) | elementalsouls |
| 2026-11-26 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/c5ff11779ee00beda2cbe05d5093fcd4ecba8f04) | github-actions[bot] |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
