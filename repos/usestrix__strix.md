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
| ⭐ **Stars** | 76.9k |
| 🍴 **Forks** | 8.8k |
| 🐞 **Open issues + PRs** | [618](https://github.com/usestrix/strix/issues) |
| 💻 **Languages** | Python 78% · Go 11% · TypeScript 8% · Jinja 1% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `agents` `artificial-intelligence` `cybersecurity` `penetration-testing` `ai-penetration-testing` `ai-pentesting` `ai-security` `bug-bounty` `ctf-tools` `cybersecurity-tools` `ethical-hacking` `llm-security` `offensive-security` `pentesting-tools` `red-teaming` `security-automation` `security` `code-quality` `ai-hacking` `hacking` |
| 🕒 **Last activity** | 2026-11-19 (yesterday) |
| 📅 **Created** | 2025-08-05 |
| 📦 **Latest release** | [v1.7.1](https://github.com/usestrix/strix/releases/tag/v1.7.1) — 2026-11-10 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 18.0 MB |
| 🌐 **Website** | https://strix.ai |

## 📦 Recent releases

### [v1.7.1](https://github.com/usestrix/strix/releases/tag/v1.7.1)
<sub>2026-11-10 · 10d ago</sub>

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
| 2026-11-19 | [refactor(prompts): delegate patch work by task, not agent type](https://github.com/usestrix/strix/commit/a1ccf777d80e812edf23fc8b82bdc17def6143ac) | 0xallam |
| 2026-11-19 | [fix(skills): preserve workflow outcomes and review the delivered patch](https://github.com/usestrix/strix/commit/cce68922784af5def973cdd0d17e92239df89779) | 0xallam |
| 2026-11-19 | [feat(skills): the finding is filed first and the fix agent attaches t…](https://github.com/usestrix/strix/commit/b1dfe05974936f5b4868c392f1bbad52d9de6608) | 0xallam |
| 2026-11-19 | [docs(skills): keep the withholding conditions in one list](https://github.com/usestrix/strix/commit/d560ec418d22955df7a46b75cd6bc619d864bde9) | 0xallam |
| 2026-11-19 | [docs(skills): keep the withholding conditions in one list](https://github.com/usestrix/strix/commit/d843c23c48ed7b8913b82419bbeae7a99e0c3db4) | 0xallam |
| 2026-11-19 | [fix(skills): the fix agent hands the reviewer the text it intends to …](https://github.com/usestrix/strix/commit/23558cd6b446c6ae4dc1b80daefa80c3c67497d1) | devin-ai-integration[bot] |
| 2026-11-19 | [fix(skills): the reviewer accepts a disclosed partial fix when the op…](https://github.com/usestrix/strix/commit/b68ab5dbeda69a79f983e19f8638cdee67490fec) | devin-ai-integration[bot] |
| 2026-11-19 | [fix(prompts): the white-box delegation rules name the fix agent as th…](https://github.com/usestrix/strix/commit/bc68109b71c193308f485fe6912ef1eebd34d2ec) | devin-ai-integration[bot] |
| 2026-11-19 | [feat(skills): a dedicated fix agent and an independent reviewer decid…](https://github.com/usestrix/strix/commit/582b1c934ed5c49654f66fa2cb2153be297a3a07) | 0xallam |
| 2026-11-19 | [Remove --methodology; a reusable methodology goes in --instruction-fi…](https://github.com/usestrix/strix/commit/85e569b2217a9be15e792674761f9a03fe3a77eb) | bearsyankees |

[See all commits ↗](https://github.com/usestrix/strix/commits)

## ⬇️ Get it

```bash
git clone https://github.com/usestrix/strix.git
```
