# elementalsouls/Claude-BugHunter

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/elementalsouls/Claude-BugHunter)

> A Claude Code skill bundle for bug hunting and external red-team work - 84 skills, 15 slash commands, 681 disclosed-report patterns curated across 24 core vulnerability classes, plus enterprise identity + infrastructure attack matrices.

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
| ⭐ **Stars** | 22.5k |
| 🍴 **Forks** | 2.3k |
| 🐞 **Open issues + PRs** | [19](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 90% · PowerShell 5% · Shell 4% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-05-05 |
| 📦 **Latest release** | [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — 2026-06-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 3.8 MB |
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
| 2026-11-25 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/6a2153d9932adf41fa4d7f5dee626047c5005a83) | github-actions[bot] |
| 2026-11-24 | [feat(docs): bespoke terminal-HUD landing page for GitHub Pages (#232)](https://github.com/elementalsouls/Claude-BugHunter/commit/9796beeeded3b9e6df50b9f5f89e79dc43bc6915) | elementalsouls |
| 2026-11-24 | [chore(assets): refresh star history chart](https://github.com/elementalsouls/Claude-BugHunter/commit/6b710c27c586100511f81acc2d6403aa2e616204) | github-actions[bot] |
| 2026-11-24 | [feat(engine): default data isolation + leak-proof attack metrics (#230)](https://github.com/elementalsouls/Claude-BugHunter/commit/d5f7d0d001bc6f6ba4ac38cf730b1871b9d8840c) | elementalsouls |
| 2026-11-24 | [feat(skill): add exploit-completion + sync skill count 83 → 84 everyw…](https://github.com/elementalsouls/Claude-BugHunter/commit/b33313ba0e507dcbf2ed117b86155c6afb25e99e) | elementalsouls |
| 2026-11-24 | [feat(engine): deterministic, LLM-free evidence capture + corroboratio…](https://github.com/elementalsouls/Claude-BugHunter/commit/1ba6fd74de74b29b6b9606766dd881eb26a978fc) | elementalsouls |
| 2026-11-23 | [feat(cbh): `cbh scope import` fills scope.md from a program's publish…](https://github.com/elementalsouls/Claude-BugHunter/commit/5843d2765d1e354de72b64016de964e6d7718f24) | udarshmarthala |
| 2026-11-23 | [fix(scope): harden the scope gate against three fail-open paths (#182…](https://github.com/elementalsouls/Claude-BugHunter/commit/a7e73914e6e7eba98f39721df53d76629b9bed23) | elementalsouls |
| 2026-11-23 | [fix: five tooling/engine correctness bugs — classify, extract_json, s…](https://github.com/elementalsouls/Claude-BugHunter/commit/6a530fb3149c8c34d3ba0eb31b4eb431e91da648) | elementalsouls |
| 2026-11-23 | [chore(readme): dedicated wordmark-only sponsor badge + spacing](https://github.com/elementalsouls/Claude-BugHunter/commit/f645b4cf80d1e4d65eef9513246f347befa3997e) | elementalsouls |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
