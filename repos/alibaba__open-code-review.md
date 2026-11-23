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
| ⭐ **Stars** | 55.6k |
| 🍴 **Forks** | 4.6k |
| 🐞 **Open issues + PRs** | [356](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 11% · TypeScript 10% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.14.2](https://github.com/alibaba/open-code-review/releases/tag/v1.14.2) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 56.8 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.14.2](https://github.com/alibaba/open-code-review/releases/tag/v1.14.2)
<sub>2026-11-23 · today</sub>

> **🚀 Features**
> - feat(i18n): add Turkish README, site docs and VS Code localization (#1986)
> **🐛 Bug Fixes**
> - fix(rules): recognize BOM-prefixed Objective-C source (#1964)
> **🔧 Refactoring**
> - refactor: adopt modern Go stdlib helpers (#1566)
> …

### [v1.14.1](https://github.com/alibaba/open-code-review/releases/tag/v1.14.1)
<sub>2026-11-22 · yesterday</sub>

> **🚀 Features**
> - feat(skills): include behavior and impact in native and delegated reviews (#2029)
> **🐛 Bug Fixes**
> - fix(tool): reject workspace named pipes before opening (#1979)
> - fix(examples): fail GitFlic and Gerrit jobs when ocr review fails (#2032)
> - fix(cli): show token usage in analysis reports (#2030)
> …

### [v1.14.0](https://github.com/alibaba/open-code-review/releases/tag/v1.14.0)
<sub>2026-11-21 · 2d ago</sub>

> **🚀 Features**
> - feat(rules,allowlist): exclude Cargo test/benchmark paths and refine Rust rules (#1971)
> - feat(review): add optional behavior and impact analysis (#1937)
> - feat(cli): order review and scan findings by severity (#2003)
> - feat(rules): add SQL review rules (#1941)
> - feat(rules): add Dhall review rules (#963)
> …

### [v1.13.13](https://github.com/alibaba/open-code-review/releases/tag/v1.13.13)
<sub>2026-11-19 · 4d ago</sub>

> **🚀 Features**
> - feat(pages): link the leaderboard to AACR-Bench (#1995)
> **🐛 Bug Fixes**
> - fix(llmloop): reserve complete compression context budget (#1993)
> - fix(chatgptauth): drain OAuth callback responses before closing (#1996)
> **📖 Documentation**
> …

### [v1.13.12](https://github.com/alibaba/open-code-review/releases/tag/v1.13.12)
<sub>2026-11-18 · 5d ago</sub>

> **🚀 Features**
> - feat(pages): add contact link to website footer (#1975)
> **🐛 Bug Fixes**
> - fix(session): keep finding identity fields separate (#1955)
> - fix(telemetry): serialize lazy metric initialization (#1883)
> - fix(tool): bound file_read result bytes, not just line count (#1878)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [feat(i18n): add Turkish README, site docs and VS Code localization (#…](https://github.com/alibaba/open-code-review/commit/e74f2c6bd4422bd1e12d257d1725bcce1d6b9ddd) | alkank |
| 2026-11-22 | [fix(rules): recognize BOM-prefixed Objective-C source (#1964)](https://github.com/alibaba/open-code-review/commit/9285d1b8958ec709ac7db751b73e6d2153ef1a4c) | Afloat16 |
| 2026-11-22 | [refactor: adopt modern Go stdlib helpers (#1566)](https://github.com/alibaba/open-code-review/commit/d0744d31b19d9fe97ffeff78dd8fb04e0be69312) | sisantaChhatoi |
| 2026-11-22 | [docs(skill): respect review-only intent for mispositioned findings (#…](https://github.com/alibaba/open-code-review/commit/284ff013f0705ae6cac4c8dfbffa2f2551886d56) | prascli |
| 2026-11-22 | [fix(tool): reject workspace named pipes before opening (#1979)](https://github.com/alibaba/open-code-review/commit/fa315a0ee2012483ea72b7fd49f937812de9c761) | Afloat16 |
| 2026-11-22 | [fix(examples): fail GitFlic and Gerrit jobs when ocr review fails (#2…](https://github.com/alibaba/open-code-review/commit/78c2e0e26f62ea150044cb0be2357b93f80f5b86) | thejesh23 |
| 2026-11-22 | [feat(skills): include behavior and impact in native and delegated rev…](https://github.com/alibaba/open-code-review/commit/398f4349cfa8be58c25c0a988ad5db1def5bd528) | lizhengfeng101 |
| 2026-11-21 | [docs(runtime): remove the phase-one design note (#2031)](https://github.com/alibaba/open-code-review/commit/39515dca6161fb7fd176d87704b2b10e5f7a0c36) | lizhengfeng101 |
| 2026-11-21 | [fix(cli): show token usage in analysis reports (#2030)](https://github.com/alibaba/open-code-review/commit/5f4d905f2d5e209aaa9e2f6e5495cc1cb82c0150) | lizhengfeng101 |
| 2026-11-21 | [fix(viewer): keep the report header stable across tabs (#2022)](https://github.com/alibaba/open-code-review/commit/d29ca2044a42ea297a7fa93692d0f5ac8f38d84e) | lizhengfeng101 |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
