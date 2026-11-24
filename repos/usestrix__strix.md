# usestrix/strix

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/usestrix/strix)

> Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛡 Security & OSINT |
| **Project** | — |
| **Why it's worth a look** | AI penetration testing to find and fix app vulnerabilities |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 77.4k |
| 🍴 **Forks** | 8.8k |
| 🐞 **Open issues + PRs** | [626](https://github.com/usestrix/strix/issues) |
| 💻 **Languages** | Python 79% · Go 11% · TypeScript 8% · Jinja 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agents` `artificial-intelligence` `cybersecurity` `penetration-testing` `ai-penetration-testing` `ai-pentesting` `ai-security` `bug-bounty` `ctf-tools` `cybersecurity-tools` `ethical-hacking` `llm-security` `offensive-security` `pentesting-tools` `red-teaming` `security-automation` `security` `code-quality` `ai-hacking` `hacking` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2025-08-05 |
| 📦 **Latest release** | [v1.7.1](https://github.com/usestrix/strix/releases/tag/v1.7.1) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 18.1 MB |
| 🌐 **Website** | https://strix.ai |

## 📦 Recent releases

### [v1.7.1](https://github.com/usestrix/strix/releases/tag/v1.7.1)
<sub>2026-11-10 · 13d ago</sub>

> **What's Changed**
> * Stop the run after finish_pr_review by @ian-at-strix in https://github.com/usestrix/strix/pull/1451
> * Stop false "ended without calling finish_scan" error on PR reviews by @ian-at-strix in https://github.com/usestrix/strix/pull/1449
> * feat(cli): add -r and a title column to the resume picker by @ian-at-strix in https://github.com/usestrix/strix/pull/1450
> * feat(tui): set the terminal title to the scan target by @ian-at-strix in https://github.com/usestrix/strix/pull/1479
> * fix(logging): suppress Agents SDK PTY warning that interferes with TUI by @ian-at-strix in https://github.com/usestrix/strix/pull/1392
> …

### [v1.7.0](https://github.com/usestrix/strix/releases/tag/v1.7.0)
<sub>2026-10-05 · 1mo ago</sub>

> **What's Changed**
> * fix(models): frontier model check matches the model name only, never the provider route by @0xallam in https://github.com/usestrix/strix/pull/1280
> * feat(reporting): link HTTP exchange evidence by @bearsyankees in https://github.com/usestrix/strix/pull/1281
> * feat(prompts): require http_exchange_ids for proxy-validated findings by @0xallam in https://github.com/usestrix/strix/pull/1292
> * docs: add Vercel AI Gateway provider guide by @erulkey in https://github.com/usestrix/strix/pull/1254
> * fix(web_search): send only the agent's query to Exa search by @0xallam in https://github.com/usestrix/strix/pull/1306
> …

### [v1.6.2](https://github.com/usestrix/strix/releases/tag/v1.6.2)
<sub>2026-09-05 · 2mo ago</sub>

> **What's Changed**
> * fix(agents): stop parents waiting on finished non-interactive children by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1241
> * fix(cloud): print top-up instructions on 402 and guide oversize or ar… by @bearsyankees in https://github.com/usestrix/strix/pull/1242
> * fix(viewer): show stopped run status by @kusonooyasumi in https://github.com/usestrix/strix/pull/1249
> * feat(web_search): add Exa as a web search provider alongside Perplexity by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1270
> * fix(cli): join the import warm-up before the engine imports, drop the orphan purge by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1273
> …

### [v1.6.1](https://github.com/usestrix/strix/releases/tag/v1.6.1)
<sub>2026-09-02 · 2mo ago</sub>

> **What's Changed**
> * skills: reference new cloud cli by @bearsyankees in https://github.com/usestrix/strix/pull/1227
> * MCP call errors no longer quarantine the connection by @yoni-at-strix in https://github.com/usestrix/strix/pull/1228
> * fix(tui): run environment and model checks on the no-target start screen by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1232
> * fix(ci): make the pre-commit mypy hook and the test suite pass on a fresh checkout by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1234
> * fix(config): merge env into cli-config.json and invalidate the linked LLM connection on change by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1236
> …

### [v1.6.0](https://github.com/usestrix/strix/releases/tag/v1.6.0)
<sub>2026-09-01 · 2mo ago</sub>

> **What's Changed**
> * Fix LiteLLM cost model resolution by @bearsyankees in https://github.com/usestrix/strix/pull/1069
> * feat: place caller-provided files into the sandbox workspace (`extra_files`, `--workspace-file`) by @yoni-at-strix in https://github.com/usestrix/strix/pull/1085
> * feat(reporting): contextual CVSS breakdown on dependency reports by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1091
> * feat(reporting): require contextual CVSS and usage evidence on dependency reports by @devin-ai-integration[bot] in https://github.com/usestrix/strix/pull/1092
> * handle resume tokens gracefully by @bearsyankees in https://github.com/usestrix/strix/pull/1097
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [Judge input typed into a shell on what is typed](https://github.com/usestrix/strix/commit/935f82350782cdf15d70cbcb3e6d7e48f49071c2) | yoni-at-strix |
| 2026-11-24 | [Save each test object's details and the agent that made it in the export](https://github.com/usestrix/strix/commit/30cceb56a58aef122a054892759a68de16c47113) | yoni-at-strix |
| 2026-11-24 | [Keep only the opening command for each shell session](https://github.com/usestrix/strix/commit/7006745a02b3c7a125bc7ebed75cdc2270174898) | yoni-at-strix |
| 2026-11-24 | [Append one row to test_objects.csv per registered object](https://github.com/usestrix/strix/commit/ccef1bb83476a4329a3a226c1c4bde137139424d) | yoni-at-strix |
| 2026-11-24 | [Write the test-object registry as test_objects.csv beside the report](https://github.com/usestrix/strix/commit/c2fd0d7f9ca80f5a78bf7d4727a3f41fdfd32e4a) | yoni-at-strix |
| 2026-11-24 | [Keep a refusal after the deadline, never clear a request body that wa…](https://github.com/usestrix/strix/commit/6ed21629b0b3c291f5c865a5a8e280ff74392cc9) | yoni-at-strix |
| 2026-11-24 | [Check shell input against the engine's own session record, find the i…](https://github.com/usestrix/strix/commit/b24fddc7aca95f53b60443d2746e5700b909cc36) | yoni-at-strix |
| 2026-11-24 | [Tell the terminal prompt when its copy of an action was cut](https://github.com/usestrix/strix/commit/6b79bbedeef9a350af733d2c40c6cde8f250f39b) | yoni-at-strix |
| 2026-11-24 | [Show the whole action in the terminal approval prompt and keep approv…](https://github.com/usestrix/strix/commit/cee348bb167b913bef6b21a21ab6c32e553405bd) | yoni-at-strix |
| 2026-11-24 | [Offer the action check every file a command names, bind shell session…](https://github.com/usestrix/strix/commit/70e638a34a284868c2e8f03732e79bf6212f434a) | yoni-at-strix |

[See all commits ↗](https://github.com/usestrix/strix/commits)

## ⬇️ Get it

```bash
git clone https://github.com/usestrix/strix.git
```
