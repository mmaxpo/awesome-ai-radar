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
| ⭐ **Stars** | 51.0k |
| 🍴 **Forks** | 3.8k |
| 🐞 **Open issues + PRs** | [341](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 12% · TypeScript 10% · Kotlin 6% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.13.9](https://github.com/alibaba/open-code-review/releases/tag/v1.13.9) — 2026-11-13 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.4 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.13.9](https://github.com/alibaba/open-code-review/releases/tag/v1.13.9)
<sub>2026-11-13 · yesterday</sub>

> **🚀 Features**
> - feat(manifest): record excluded files in run coverage (#1901)
> **🐛 Bug Fixes**
> - fix(action): show warnings in zero-finding PR summaries (#1766)
> - fix(deps): update compatible vulnerable dependencies (#1919)
> - fix(session): emit [] instead of null from session list --json (#1742)
> …

### [v1.13.8](https://github.com/alibaba/open-code-review/releases/tag/v1.13.8)
<sub>2026-11-12 · 2d ago</sub>

> **🚀 Features**
> - feat(tools): support reading both comparison sides (#1903)
> - feat: add GitHub Copilot CLI integration (plugin manifest + guide) (#1890)
> - feat(llm): prefer MiniMax M3.1 Flash in model suggestions (#1784)
> **🐛 Bug Fixes**
> - fix(acp): register stub signals before readiness (#1905)
> …

### [v1.13.7](https://github.com/alibaba/open-code-review/releases/tag/v1.13.7)
<sub>2026-11-10 · 4d ago</sub>

> **🚀 Features**
> - feat(scan): gate PLAN_TASK on file size (#1252)
> - feat(session): inspect saved sessions by ID from any directory (#1884)
> - feat(rules): add Clojure and ClojureScript review rules (#965)
> **🐛 Bug Fixes**
> - fix: prevent postinstall 404 crash for unreleased v0.0.0 (#1820)
> …

### [v1.13.6](https://github.com/alibaba/open-code-review/releases/tag/v1.13.6)
<sub>2026-11-05 · 8d ago</sub>

> **🚀 Features**
> - feat(pages): showcase supported model providers (#1862)
> - feat(lang): review Starlark files (#1851)
> - feat(rules): add C# review rules (#1840)
> **🐛 Bug Fixes**
> - fix(llm): preserve explicit false stream override (#1531)
> …

### [v1.13.5](https://github.com/alibaba/open-code-review/releases/tag/v1.13.5)
<sub>2026-11-03 · 10d ago</sub>

> **🚀 Features**
> - feat(allowlist): add HAML, Slim and ERB template support (#1552)
> - feat(allowlist): review .jsonc files (#1801)
> - feat(allowlist): add EJS, Liquid and Nunjucks template support (#1553)
> - feat(rules): add Scala-specific review rules (#1095)
> **🐛 Bug Fixes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [feat(workspace): support comparison-side code access (#1915)](https://github.com/alibaba/open-code-review/commit/abd6416e6faec64e00af170a74633e34d56ab467) | lizhengfeng101 |
| 2026-11-13 | [fix(action): show warnings in zero-finding PR summaries (#1766)](https://github.com/alibaba/open-code-review/commit/0e9060da66af36a96a15516e76a001953095318b) | Frank-zhu2000 |
| 2026-11-13 | [feat(manifest): record excluded files in run coverage (#1901)](https://github.com/alibaba/open-code-review/commit/65b12d71c80dd2dd25834bb3063baf1c224be86a) | NicolasRocchia |
| 2026-11-13 | [fix(deps): update compatible vulnerable dependencies (#1919)](https://github.com/alibaba/open-code-review/commit/e24b6c75eab71761ec3417dbc983c73578d54c72) | lizhengfeng101 |
| 2026-11-12 | [fix(session): emit [] instead of null from session list --json (#1742)](https://github.com/alibaba/open-code-review/commit/6386895e7cfac419bd7a9cf4795e8b824a6e3ced) | castorhrio |
| 2026-11-12 | [fix(tools): enforce per-request tool declarations (#1841)](https://github.com/alibaba/open-code-review/commit/43638b5c503233910639d8c24d646cfb76d2cc25) | chaojixinren |
| 2026-11-12 | [docs(rules): put the rule table back in matching order, and hold it t…](https://github.com/alibaba/open-code-review/commit/1d7cc448200eebe3fb710834c0e7b8d04b63f77b) | abhisheksharma2411 |
| 2026-11-12 | [feat(tools): support reading both comparison sides (#1903)](https://github.com/alibaba/open-code-review/commit/4236c871fe8130aa840a2a1c0922f469e87e0416) | lizhengfeng101 |
| 2026-11-11 | [fix(acp): register stub signals before readiness (#1905)](https://github.com/alibaba/open-code-review/commit/db5db6bec62ee45c02171a12e043b8239223aa07) | lizhengfeng101 |
| 2026-11-11 | [fix(ci): upgrade Go toolchains to 1.26.11 (#1904)](https://github.com/alibaba/open-code-review/commit/a6b57ecaa002c01f1f0b361866de89b318dc4a7a) | lizhengfeng101 |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
