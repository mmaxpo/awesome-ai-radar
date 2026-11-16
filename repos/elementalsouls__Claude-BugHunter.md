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
| ⭐ **Stars** | 7.1k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [3](https://github.com/elementalsouls/Claude-BugHunter/issues) |
| 💻 **Languages** | Python 85% · PowerShell 8% · Shell 6% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `ai-security` `anthropic` `application-security` `bug-bounty` `bugbounty` `bugcrowd` `claude` `claude-code` `claude-skills` `ethical-hacking` `hackerone` `offensive-security` `pentesting` `red-team` `security-tools` `web-security` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-05-05 |
| 📦 **Latest release** | [v2.1](https://github.com/elementalsouls/Claude-BugHunter/releases/tag/v2.1) — 2026-06-05 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 4.1 MB |
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
| 2026-11-16 | [fix(eval): report false-positive rates alongside grading coverage (#131)](https://github.com/elementalsouls/Claude-BugHunter/commit/2f9a226d38d35d28d06f1ed63753799d498a2b3d) | rudycelekli |
| 2026-11-16 | [fix(scope): preserve metacharacters in host regex rules (#122)](https://github.com/elementalsouls/Claude-BugHunter/commit/228f976a6535ae2bd6d8b4e5736f5e1ca1c7ec10) | rudycelekli |
| 2026-11-16 | [fix(eval): preserve ungraded PortSwigger outcomes (#117)](https://github.com/elementalsouls/Claude-BugHunter/commit/a5d1710562ab5bd79b7c8fa8021a4c8cf686a797) | rudycelekli |
| 2026-11-16 | [fix(hooks): scan staged content before allowing a commit (#112)](https://github.com/elementalsouls/Claude-BugHunter/commit/028776f14ba61e45f00fa0d30b739d42cf48c24b) | rudycelekli |
| 2026-11-16 | [fix(packaging): keep the standalone skill and report index current (#…](https://github.com/elementalsouls/Claude-BugHunter/commit/c4fb2c104d98dead9c9603926de3d43ff35add80) | rudycelekli |
| 2026-11-16 | [fix(skills): fit three descriptions within the Agent Skills limit (#92)](https://github.com/elementalsouls/Claude-BugHunter/commit/56cb92bf09a2f70f5474edaf8f3f53615b7b797d) | xunguangzlj-cloud |
| 2026-11-16 | [fix(cli): make triage signal matching case-insensitive (#90)](https://github.com/elementalsouls/Claude-BugHunter/commit/b81ab02c524f29c05676fedfae935165065d3694) | neonhomesick |
| 2026-11-16 | [fix(engine): select the last JSON verdict fence in message order (#114)](https://github.com/elementalsouls/Claude-BugHunter/commit/5201c23bfcf143cbea109e1b28ff583462ed3bdd) | rudycelekli |
| 2026-11-16 | [fix(mcp): preserve arguments and environment keys in Codex TOML (#109)](https://github.com/elementalsouls/Claude-BugHunter/commit/86abbf2e4a1656c7705d0c123a27a6ab6df50c47) | rudycelekli |
| 2026-11-16 | [fix(cli): preserve nested Markdown in drafted reports (#106)](https://github.com/elementalsouls/Claude-BugHunter/commit/672b734d784ac33b01eca713316d4e75b654060b) | rudycelekli |

[See all commits ↗](https://github.com/elementalsouls/Claude-BugHunter/commits)

## ⬇️ Get it

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
```
