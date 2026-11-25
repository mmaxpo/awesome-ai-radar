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
| ⭐ **Stars** | 56.3k |
| 🍴 **Forks** | 4.6k |
| 🐞 **Open issues + PRs** | [346](https://github.com/alibaba/open-code-review/issues) |
| 💻 **Languages** | Go 70% · JavaScript 11% · TypeScript 11% · Kotlin 5% · CSS 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agent` `code-review` `code-review-assistant` `harness` `repository-level-context` `agent-skills` |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-05-18 |
| 📦 **Latest release** | [v1.14.3](https://github.com/alibaba/open-code-review/releases/tag/v1.14.3) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 57.1 MB |
| 🌐 **Website** | https://open-codereview.ai |

## 📦 Recent releases

### [v1.14.3](https://github.com/alibaba/open-code-review/releases/tag/v1.14.3)
<sub>2026-11-24 · yesterday</sub>

> **🐛 Bug Fixes**
> - fix(tool): return a model-facing error for invalid code_search regex (#1811)
> - fix(deps): update OpenTelemetry to v1.47.0 (#2067)
> **📖 Documentation**
> - docs(actions): explain how to allow pull_request_target (#2068)
> - docs(review-rules): note that include also overrides the extension allowlist (#1913)
> …

### [v1.14.2](https://github.com/alibaba/open-code-review/releases/tag/v1.14.2)
<sub>2026-11-23 · 2d ago</sub>

> **🚀 Features**
> - feat(i18n): add Turkish README, site docs and VS Code localization (#1986)
> **🐛 Bug Fixes**
> - fix(rules): recognize BOM-prefixed Objective-C source (#1964)
> **🔧 Refactoring**
> - refactor: adopt modern Go stdlib helpers (#1566)
> …

### [v1.14.1](https://github.com/alibaba/open-code-review/releases/tag/v1.14.1)
<sub>2026-11-22 · 3d ago</sub>

> **🚀 Features**
> - feat(skills): include behavior and impact in native and delegated reviews (#2029)
> **🐛 Bug Fixes**
> - fix(tool): reject workspace named pipes before opening (#1979)
> - fix(examples): fail GitFlic and Gerrit jobs when ocr review fails (#2032)
> - fix(cli): show token usage in analysis reports (#2030)
> …

### [v1.14.0](https://github.com/alibaba/open-code-review/releases/tag/v1.14.0)
<sub>2026-11-21 · 4d ago</sub>

> **🚀 Features**
> - feat(rules,allowlist): exclude Cargo test/benchmark paths and refine Rust rules (#1971)
> - feat(review): add optional behavior and impact analysis (#1937)
> - feat(cli): order review and scan findings by severity (#2003)
> - feat(rules): add SQL review rules (#1941)
> - feat(rules): add Dhall review rules (#963)
> …

### [v1.13.13](https://github.com/alibaba/open-code-review/releases/tag/v1.13.13)
<sub>2026-11-19 · 6d ago</sub>

> **🚀 Features**
> - feat(pages): link the leaderboard to AACR-Bench (#1995)
> **🐛 Bug Fixes**
> - fix(llmloop): reserve complete compression context budget (#1993)
> - fix(chatgptauth): drain OAuth callback responses before closing (#1996)
> **📖 Documentation**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [fix(tool): preserve binary matches in code_search (#2046)](https://github.com/alibaba/open-code-review/commit/d4f568f71d3a9d5c5ec972791b1509e40cd31ad1) | Bbbtt04 |
| 2026-11-25 | [feat(allowlist): exclude C and C++ test and benchmark paths (#2081)](https://github.com/alibaba/open-code-review/commit/64e2075fb2b588e3c490c7c6166f9edab2820c6a) | alex09x |
| 2026-11-25 | [docs(filter): document the secret-path gate in the architecture and F…](https://github.com/alibaba/open-code-review/commit/7ea9c5280655deeaba43f2a298df70dbf17c070b) | SU-AN-coder |
| 2026-11-24 | [docs(cli): complete command help (#2055)](https://github.com/alibaba/open-code-review/commit/9007ae84e0de7b84d72f9833f6b12a2a731d5cbd) | chaojixinren |
| 2026-11-24 | [feat(i18n): add Vietnamese (vi-VN) translation (#2035)](https://github.com/alibaba/open-code-review/commit/6a7e92c293ddd781cd2445214699a877cd45c36a) | dung997tb |
| 2026-11-24 | [fix(config): validate and trim llm.url wherever it is written (#2039)](https://github.com/alibaba/open-code-review/commit/6e63a26ba6b2c0b928e6772807e86d40f6b80825) | REI-330 |
| 2026-11-24 | [feat(skills): review GitHub PRs from pinned snapshots (#2038)](https://github.com/alibaba/open-code-review/commit/959f8f5bb6fca717d4af05996103ad960a77cc99) | lizhengfeng101 |
| 2026-11-24 | [feat(session): persist retry reports in session end (#1083)](https://github.com/alibaba/open-code-review/commit/404b058f4cef477ab061e1ae4250fea37701769f) | Gongyl01 |
| 2026-11-24 | [fix(tool): return a model-facing error for invalid code_search regex …](https://github.com/alibaba/open-code-review/commit/f6379f71edba1e59dbc056e8f455df1f84396498) | OUAO-FRANK |
| 2026-11-24 | [docs(actions): explain how to allow pull_request_target (#2068)](https://github.com/alibaba/open-code-review/commit/4e284aa9b304dc62f43f919398129a0af44a705e) | Qiyuanqiii |

[See all commits ↗](https://github.com/alibaba/open-code-review/commits)

## ⬇️ Get it

```bash
git clone https://github.com/alibaba/open-code-review.git
```
