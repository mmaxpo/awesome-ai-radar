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
| ⭐ **Stars** | 24.0k |
| 🍴 **Forks** | 2.4k |
| 🐞 **Open issues + PRs** | [30](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 91% · PowerShell 5% · Shell 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-05-05 |
| 📦 **Latest release** | [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — 2026-06-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.9 MB |
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
| 2026-11-26 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/c5ff11779ee00beda2cbe05d5093fcd4ecba8f04) | github-actions[bot] |
| 2026-11-25 | [feat(engine): diff-based regression hunting via cbh diff + /diff (#239)](https://github.com/elementalsouls/Claude-BugHunter/commit/08965e258195f49ce0166ddf38b3d48d82ae3f18) | Huzaifa60 |
| 2026-11-25 | [docs(changelog): credit @speto2 for the scope-bypass disclosure (#249)](https://github.com/elementalsouls/Claude-BugHunter/commit/a091b520c32d1df87113f3341b6d351166d9ccc0) | elementalsouls |
| 2026-11-25 | [fix(security): scope bypass via backslash in URL authority + redactio…](https://github.com/elementalsouls/Claude-BugHunter/commit/3e68bed839635edeeb7b27335ba9a4cec8c2d839) | elementalsouls |
| 2026-11-25 | [docs: PCAP hygiene + Bugcrowd VRT mappings + safer CRLF recovery (in-…](https://github.com/elementalsouls/Claude-BugHunter/commit/4c9966e4cafea11e24309d9e71d1c89602319c57) | elementalsouls |
| 2026-11-25 | [fix: harness-MCP UTF-8 at import + wapt dispatch coverage (in-house, …](https://github.com/elementalsouls/Claude-BugHunter/commit/f38645334451f517daadccc8a4f902d8555310cb) | elementalsouls |
| 2026-11-25 | [fix: landing-page no-JS robustness + scope hardening (in-house, credi…](https://github.com/elementalsouls/Claude-BugHunter/commit/464251e55a62d2a397bba20353db0c8a03d5fda7) | elementalsouls |
| 2026-11-25 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/6a2153d9932adf41fa4d7f5dee626047c5005a83) | github-actions[bot] |
| 2026-11-24 | [feat(docs): bespoke terminal-HUD landing page for GitHub Pages (#232)](https://github.com/elementalsouls/Claude-BugHunter/commit/9796beeeded3b9e6df50b9f5f89e79dc43bc6915) | elementalsouls |
| 2026-11-24 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/6b710c27c586100511f81acc2d6403aa2e616204) | github-actions[bot] |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
