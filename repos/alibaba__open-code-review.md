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
| ⭐ **Stars** | 52.7k |
| 🍴 **Forks** | 4.2k |
| 🐞 **Open issues + PRs** | [335](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 12% · TypeScript 10% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-16 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10) — 2026-11-15 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 53.4 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)
<sub>2026-11-15 · yesterday</sub>

> **🚀 Features**
> - feat(review): default --to to HEAD when only --from is given (#1936)
> - feat(cli): render Markdown summaries and style progress output (#1927)
> - feat(review): support --resume for workspace mode (#1922)
> - feat(workspace): support comparison-side code access (#1915)
> **Full Changelog**: https://github.com/alibaba/open-code-review/compare/v1.13.9...v1.13.10

### [v1.13.9](https://github.com/alibaba/open-code-review/releases/tag/v1.13.9)
<sub>2026-11-13 · 3d ago</sub>

> **🚀 Features**
> - feat(manifest): record excluded files in run coverage (#1901)
> **🐛 Bug Fixes**
> - fix(action): show warnings in zero-finding PR summaries (#1766)
> - fix(deps): update compatible vulnerable dependencies (#1919)
> - fix(session): emit [] instead of null from session list --json (#1742)
> …

### [v1.13.8](https://github.com/alibaba/open-code-review/releases/tag/v1.13.8)
<sub>2026-11-12 · 4d ago</sub>

> **🚀 Features**
> - feat(tools): support reading both comparison sides (#1903)
> - feat: add GitHub Copilot CLI integration (plugin manifest + guide) (#1890)
> - feat(llm): prefer MiniMax M3.1 Flash in model suggestions (#1784)
> **🐛 Bug Fixes**
> - fix(acp): register stub signals before readiness (#1905)
> …

### [v1.13.7](https://github.com/alibaba/open-code-review/releases/tag/v1.13.7)
<sub>2026-11-10 · 6d ago</sub>

> **🚀 Features**
> - feat(scan): gate PLAN_TASK on file size (#1252)
> - feat(session): inspect saved sessions by ID from any directory (#1884)
> - feat(rules): add Clojure and ClojureScript review rules (#965)
> **🐛 Bug Fixes**
> - fix: prevent postinstall 404 crash for unreleased v0.0.0 (#1820)
> …

### [v1.13.6](https://github.com/alibaba/open-code-review/releases/tag/v1.13.6)
<sub>2026-11-05 · 11d ago</sub>

> **🚀 Features**
> - feat(pages): showcase supported model providers (#1862)
> - feat(lang): review Starlark files (#1851)
> - feat(rules): add C# review rules (#1840)
> **🐛 Bug Fixes**
> - fix(llm): preserve explicit false stream override (#1531)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-16 | [fix(session): compare sessions recorded under different path spelling…](https://github.com/alibaba/open-code-review/commit/dd1a7e12a3565f5f7396acb394d83ab18102e6ce) | castorhrio |
| 2026-11-16 | [fix(viewer): truncate multibyte file paths on rune boundaries (#1854)](https://github.com/alibaba/open-code-review/commit/783fa679736ea6b1bb4d2fb57e50d1f65590d6cd) | LuckVd |
| 2026-11-16 | [fix(config): address dotted MCP server names in config set (#1826)](https://github.com/alibaba/open-code-review/commit/e4c80117321c99b86e9d9da8e1254cc81beb01b6) | LuckVd |
| 2026-11-16 | [fix(scan): cut summary comments on a rune boundary (#1852)](https://github.com/alibaba/open-code-review/commit/13e5e9571ff1d80f6b37f675b8ec54512ea61e93) | kevin9327 |
| 2026-11-16 | [feat(session): filter listed sessions by branch (#1702)](https://github.com/alibaba/open-code-review/commit/b71e455d0ec3a00b828ec785e52ccbf425178e72) | OUAO-FRANK |
| 2026-11-16 | [fix(vscode): show partial and failed reviews as failed, not "No issue…](https://github.com/alibaba/open-code-review/commit/35642d05e526353f12a66808a7c9fae601d800c6) | divya0795 |
| 2026-11-16 | [fix(viewer): inset in-table focus rings and let long meta values wrap…](https://github.com/alibaba/open-code-review/commit/9b3e6a56d33dab8b6b17458d310286b472eefc63) | misslead |
| 2026-11-16 | [feat(rules): add Move review rules (#959)](https://github.com/alibaba/open-code-review/commit/8441fa76114f30443d2ae575c7a517716fde5b9c) | chethanuk |
| 2026-11-16 | [fix(acp): state input limits in their error messages (#1917)](https://github.com/alibaba/open-code-review/commit/59e55d5efb7b8411705cf0f25d89e82a63972c6d) | sisantaChhatoi |
| 2026-11-15 | [feat(review): default --to to HEAD when only --from is given (#1936)](https://github.com/alibaba/open-code-review/commit/7e5ce06c88de5ce81df5dc4f24e2e485b517fae8) | Walternater |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
