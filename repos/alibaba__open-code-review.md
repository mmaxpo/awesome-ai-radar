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
| ⭐ **Stars** | 55.0k |
| 🍴 **Forks** | 4.5k |
| 🐞 **Open issues + PRs** | [340](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 71% · JavaScript 11% · TypeScript 10% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.14.0](https://github.com/alibaba/open-code-review/releases/tag/v1.14.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 56.5 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.14.0](https://github.com/alibaba/open-code-review/releases/tag/v1.14.0)
<sub>2026-11-21 · today</sub>

> **🚀 Features**
> - feat(rules,allowlist): exclude Cargo test/benchmark paths and refine Rust rules (#1971)
> - feat(review): add optional behavior and impact analysis (#1937)
> - feat(cli): order review and scan findings by severity (#2003)
> - feat(rules): add SQL review rules (#1941)
> - feat(rules): add Dhall review rules (#963)
> …

### [v1.13.13](https://github.com/alibaba/open-code-review/releases/tag/v1.13.13)
<sub>2026-11-19 · 2d ago</sub>

> **🚀 Features**
> - feat(pages): link the leaderboard to AACR-Bench (#1995)
> **🐛 Bug Fixes**
> - fix(llmloop): reserve complete compression context budget (#1993)
> - fix(chatgptauth): drain OAuth callback responses before closing (#1996)
> **📖 Documentation**
> …

### [v1.13.12](https://github.com/alibaba/open-code-review/releases/tag/v1.13.12)
<sub>2026-11-18 · 3d ago</sub>

> **🚀 Features**
> - feat(pages): add contact link to website footer (#1975)
> **🐛 Bug Fixes**
> - fix(session): keep finding identity fields separate (#1955)
> - fix(telemetry): serialize lazy metric initialization (#1883)
> - fix(tool): bound file_read result bytes, not just line count (#1878)
> …

### [v1.13.11](https://github.com/alibaba/open-code-review/releases/tag/v1.13.11)
<sub>2026-11-17 · 4d ago</sub>

> **🚀 Features**
> - feat(session): filter listed sessions by branch (#1702)
> - feat(rules): add Move review rules (#959)
> **🐛 Bug Fixes**
> - fix(session): compare sessions recorded under different path spellings (#1750)
> - fix(viewer): truncate multibyte file paths on rune boundaries (#1854)
> …

### [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)
<sub>2026-11-15 · 6d ago</sub>

> **🚀 Features**
> - feat(review): default --to to HEAD when only --from is given (#1936)
> - feat(cli): render Markdown summaries and style progress output (#1927)
> - feat(review): support --resume for workspace mode (#1922)
> - feat(workspace): support comparison-side code access (#1915)
> **Full Changelog**: https://github.com/alibaba/open-code-review/compare/v1.13.9...v1.13.10

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [docs(runtime): remove the phase-one design note (#2031)](https://github.com/alibaba/open-code-review/commit/39515dca6161fb7fd176d87704b2b10e5f7a0c36) | lizhengfeng101 |
| 2026-11-21 | [fix(cli): show token usage in analysis reports (#2030)](https://github.com/alibaba/open-code-review/commit/5f4d905f2d5e209aaa9e2f6e5495cc1cb82c0150) | lizhengfeng101 |
| 2026-11-21 | [fix(viewer): keep the report header stable across tabs (#2022)](https://github.com/alibaba/open-code-review/commit/d29ca2044a42ea297a7fa93692d0f5ac8f38d84e) | lizhengfeng101 |
| 2026-11-21 | [feat(rules,allowlist): exclude Cargo test/benchmark paths and refine …](https://github.com/alibaba/open-code-review/commit/7e4ecad163fd584630815c1a3abf4b3708a893a0) | alex09x |
| 2026-11-21 | [fix(review): include TypeScript module extensions (#1962)](https://github.com/alibaba/open-code-review/commit/561787693595bbb2e12658557d63a661873c5aff) | Afloat16 |
| 2026-11-21 | [docs(configuration): explain remote Chat Completions providers (#2005)](https://github.com/alibaba/open-code-review/commit/99ab679d7e327d13c6b69e71651ec30bbb2152f9) | wzxsdf |
| 2026-11-21 | [fix(mcp): match tool definitions to their registered server (#1972)](https://github.com/alibaba/open-code-review/commit/2de8b4d9d5eb2939116cda628112e938d8a225a9) | Afloat16 |
| 2026-11-21 | [feat(review): add optional behavior and impact analysis (#1937)](https://github.com/alibaba/open-code-review/commit/3adfc5a3fe59523620cfca94a06fbeb32021fc8b) | lizhengfeng101 |
| 2026-11-20 | [fix(pages): recover partial-locale fallback and fragment navigation (…](https://github.com/alibaba/open-code-review/commit/5a6f77ccd1540ed4e80c06490a696543e507d3e4) | wzxsdf |
| 2026-11-20 | [docs(review-rules): explain specification-aware reviews (#2006)](https://github.com/alibaba/open-code-review/commit/5a8c1cb8efd6576f5341a198093ef83dfb837e6c) | wzxsdf |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
