# alibaba/open-code-review

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/alibaba/open-code-review)

> Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precise line-level comments, built-in multi-language ruleset (NPE, thread-safety, XSS, SQL injection), OpenAI & Anthropic compatible.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 💻 Coding agents & dev tools |
| **Project** | — |
| **Why it's worth a look** | Alibaba's AI code-review CLI: LLM agent + deterministic checks, line-level comments, CI-ready |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 54.3k |
| 🍴 **Forks** | 4.5k |
| 🐞 **Open issues + PRs** | [338](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 12% · TypeScript 10% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.13.13](https://github.com/alibaba/open-code-review/releases/tag/v1.13.13) — 2026-11-19 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.6 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.13.13](https://github.com/alibaba/open-code-review/releases/tag/v1.13.13)
<sub>2026-11-19 · today</sub>

> **🚀 Features**
> - feat(pages): link the leaderboard to AACR-Bench (#1995)
> **🐛 Bug Fixes**
> - fix(llmloop): reserve complete compression context budget (#1993)
> - fix(chatgptauth): drain OAuth callback responses before closing (#1996)
> **📖 Documentation**
> …

### [v1.13.12](https://github.com/alibaba/open-code-review/releases/tag/v1.13.12)
<sub>2026-11-18 · yesterday</sub>

> **🚀 Features**
> - feat(pages): add contact link to website footer (#1975)
> **🐛 Bug Fixes**
> - fix(session): keep finding identity fields separate (#1955)
> - fix(telemetry): serialize lazy metric initialization (#1883)
> - fix(tool): bound file_read result bytes, not just line count (#1878)
> …

### [v1.13.11](https://github.com/alibaba/open-code-review/releases/tag/v1.13.11)
<sub>2026-11-17 · 2d ago</sub>

> **🚀 Features**
> - feat(session): filter listed sessions by branch (#1702)
> - feat(rules): add Move review rules (#959)
> **🐛 Bug Fixes**
> - fix(session): compare sessions recorded under different path spellings (#1750)
> - fix(viewer): truncate multibyte file paths on rune boundaries (#1854)
> …

### [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)
<sub>2026-11-15 · 4d ago</sub>

> **🚀 Features**
> - feat(review): default --to to HEAD when only --from is given (#1936)
> - feat(cli): render Markdown summaries and style progress output (#1927)
> - feat(review): support --resume for workspace mode (#1922)
> - feat(workspace): support comparison-side code access (#1915)
> **Full Changelog**: https://github.com/alibaba/open-code-review/compare/v1.13.9...v1.13.10

### [v1.13.9](https://github.com/alibaba/open-code-review/releases/tag/v1.13.9)
<sub>2026-11-13 · 6d ago</sub>

> **🚀 Features**
> - feat(manifest): record excluded files in run coverage (#1901)
> **🐛 Bug Fixes**
> - fix(action): show warnings in zero-finding PR summaries (#1766)
> - fix(deps): update compatible vulnerable dependencies (#1919)
> - fix(session): emit [] instead of null from session list --json (#1742)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [perf(viewer): avoid copying owned JSONL records (#1967)](https://github.com/alibaba/open-code-review/commit/a74bcbbd4975eb3a92493d5eb537cf276d79b322) | Afloat16 |
| 2026-11-19 | [fix(gitlab_ci): stop posting a check-mark LGTM on a failed review (#1…](https://github.com/alibaba/open-code-review/commit/37ff30759815613ac29d76a68d8932f2781ba113) | gengwg |
| 2026-11-19 | [feat(rules): add SQL review rules (#1941)](https://github.com/alibaba/open-code-review/commit/55b4b311d6b7dacf9798fa63a4780386db1e5bf3) | mvanhorn |
| 2026-11-19 | [feat(rules): add Dhall review rules (#963)](https://github.com/alibaba/open-code-review/commit/b87ca79fbfb1b9efdd86c79dcf4977ebf91bedea) | chethanuk |
| 2026-11-19 | [feat(rules): add Ruby review rules (#1940)](https://github.com/alibaba/open-code-review/commit/817ed02d7b1917ec6a36630d926af34661af9b97) | mvanhorn |
| 2026-11-19 | [feat(allowlist): add CUDA (.cu/.cuh) and HIP (.hip) review support (#…](https://github.com/alibaba/open-code-review/commit/1363b96552c0a9bda86bcd0ba5b61a2d668c51dd) | SU-AN-coder |
| 2026-11-19 | [fix(llmloop): reserve complete compression context budget (#1993)](https://github.com/alibaba/open-code-review/commit/445ad9dea3057346986197385858a1a281253cc9) | lizhengfeng101 |
| 2026-11-18 | [fix(chatgptauth): drain OAuth callback responses before closing (#1996)](https://github.com/alibaba/open-code-review/commit/5d6552adafb6cbedfb54793214b777cd134dc97b) | lizhengfeng101 |
| 2026-11-18 | [feat(pages): link the leaderboard to AACR-Bench (#1995)](https://github.com/alibaba/open-code-review/commit/d56d7a4cf6cc3f0869a75b07bcf85cd82c9c83ef) | lizhengfeng101 |
| 2026-11-18 | [perf(pages): lazy-load documentation content by language (#1992)](https://github.com/alibaba/open-code-review/commit/8f9ce54026cf2d08feb989a40d5f8de1ba89e6e4) | wzxsdf |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
