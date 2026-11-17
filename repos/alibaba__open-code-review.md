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
| ⭐ **Stars** | 53.5k |
| 🍴 **Forks** | 4.4k |
| 🐞 **Open issues + PRs** | [353](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 12% · TypeScript 10% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.13.11](https://github.com/alibaba/open-code-review/releases/tag/v1.13.11) — 2026-11-17 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 54.2 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.13.11](https://github.com/alibaba/open-code-review/releases/tag/v1.13.11)
<sub>2026-11-17 · today</sub>

> **🚀 Features**
> - feat(session): filter listed sessions by branch (#1702)
> - feat(rules): add Move review rules (#959)
> **🐛 Bug Fixes**
> - fix(session): compare sessions recorded under different path spellings (#1750)
> - fix(viewer): truncate multibyte file paths on rune boundaries (#1854)
> …

### [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)
<sub>2026-11-15 · 2d ago</sub>

> **🚀 Features**
> - feat(review): default --to to HEAD when only --from is given (#1936)
> - feat(cli): render Markdown summaries and style progress output (#1927)
> - feat(review): support --resume for workspace mode (#1922)
> - feat(workspace): support comparison-side code access (#1915)
> **Full Changelog**: https://github.com/alibaba/open-code-review/compare/v1.13.9...v1.13.10

### [v1.13.9](https://github.com/alibaba/open-code-review/releases/tag/v1.13.9)
<sub>2026-11-13 · 4d ago</sub>

> **🚀 Features**
> - feat(manifest): record excluded files in run coverage (#1901)
> **🐛 Bug Fixes**
> - fix(action): show warnings in zero-finding PR summaries (#1766)
> - fix(deps): update compatible vulnerable dependencies (#1919)
> - fix(session): emit [] instead of null from session list --json (#1742)
> …

### [v1.13.8](https://github.com/alibaba/open-code-review/releases/tag/v1.13.8)
<sub>2026-11-12 · 5d ago</sub>

> **🚀 Features**
> - feat(tools): support reading both comparison sides (#1903)
> - feat: add GitHub Copilot CLI integration (plugin manifest + guide) (#1890)
> - feat(llm): prefer MiniMax M3.1 Flash in model suggestions (#1784)
> **🐛 Bug Fixes**
> - fix(acp): register stub signals before readiness (#1905)
> …

### [v1.13.7](https://github.com/alibaba/open-code-review/releases/tag/v1.13.7)
<sub>2026-11-10 · 7d ago</sub>

> **🚀 Features**
> - feat(scan): gate PLAN_TASK on file size (#1252)
> - feat(session): inspect saved sessions by ID from any directory (#1884)
> - feat(rules): add Clojure and ClojureScript review rules (#965)
> **🐛 Bug Fixes**
> - fix: prevent postinstall 404 crash for unreleased v0.0.0 (#1820)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-17 | [fix(session): keep finding identity fields separate (#1955)](https://github.com/alibaba/open-code-review/commit/d30f93864e9c682d27c7fb2d03ae112dca966c32) | Afloat16 |
| 2026-11-17 | [fix(telemetry): serialize lazy metric initialization (#1883)](https://github.com/alibaba/open-code-review/commit/9430c9c61a7d35556cb0cebfc9408cbeab7edb96) | divya0795 |
| 2026-11-17 | [gitcmd: bound Wait after cancellation with WaitDelay (#1909)](https://github.com/alibaba/open-code-review/commit/178543d92fecb7fcfe2da55ffcdc4486997fa75b) | Batianxieshen1 |
| 2026-11-17 | [feat(pages): add contact link to website footer (#1975)](https://github.com/alibaba/open-code-review/commit/ed658157c6e15f8a086a289768c759cb9a63107a) | lizhengfeng101 |
| 2026-11-17 | [fix(tool): bound file_read result bytes, not just line count (#1878)](https://github.com/alibaba/open-code-review/commit/4192238f9cb97abf9be134edc272659fcecb0a6b) | RerankerGuo |
| 2026-11-17 | [fix(cmd): return non-zero for partial operational failures (#1030)](https://github.com/alibaba/open-code-review/commit/b5e81a11e926a7557b0cc0c50b98058e0c85b39e) | Qiyuanqiii |
| 2026-11-17 | [docs: improve agent onboarding and refresh localized screenshots (#1957)](https://github.com/alibaba/open-code-review/commit/0f5a28495aeb9d27388db74c240c56c5c5f5868f) | lizhengfeng101 |
| 2026-11-16 | [fix(session): compare sessions recorded under different path spelling…](https://github.com/alibaba/open-code-review/commit/dd1a7e12a3565f5f7396acb394d83ab18102e6ce) | castorhrio |
| 2026-11-16 | [fix(viewer): truncate multibyte file paths on rune boundaries (#1854)](https://github.com/alibaba/open-code-review/commit/783fa679736ea6b1bb4d2fb57e50d1f65590d6cd) | LuckVd |
| 2026-11-16 | [fix(config): address dotted MCP server names in config set (#1826)](https://github.com/alibaba/open-code-review/commit/e4c80117321c99b86e9d9da8e1254cc81beb01b6) | LuckVd |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
