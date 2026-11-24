# openai/codex-security

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/openai/codex-security)

> OpenAI's Codex Security CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities. npm: https://www.npmjs.com/package/@openai/codex-security

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🛡 Security & OSINT |
| **Project** | — |
| **Why it's worth a look** | OpenAI's CLI/SDK to find, validate and fix security vulnerabilities |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 14.3k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [222](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 77% · Python 19% · JavaScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 90.1 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — Codex Security GitHub Action 0.10.1
<sub>2026-11-18 · 5d ago</sub>

> GitHub Action for [Codex Security 0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1).
> Installs `@openai/codex-security@0.10.1`.
> ```yaml
> uses: openai/codex-security@bf650710f36c16936324efe250a49cdd9f2da037 # action-v0.10.1
> ```

### [npm-v0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1) — Codex Security 0.10.1
<sub>2026-11-18 · 5d ago</sub>

> **Highlights**
> - **Exclude paths from scans.** Run `cs scan . --exclude-path examples/` to exclude a directory from review in Standard, Deep, or diff scans. Repeat the flag for more paths, or set `scan.exclude_paths` in your project configuration. Paths are literal and relative to the repository. The scanner can still read excluded files for context and filters out findings whose locations all fall under excluded paths.
> - **Import scanner findings.** Use `cs import continuum` to collect AWS Continuum code issues with their supporting evidence. Attack-path analysis can use observations from the tested target when assessing reachability and severity. You can also import saved CrowdStrike Falcon Cloud Security IaC reports into your local workbench.
> - **Deep Scan.** When Codex blocks a worker request because of a misalignment policy violation, Deep Scan now stops and reports the refusal without retrying the request.
> - **Threat modeling.** When a route appears in a test or on a deleted line, the threat-modeling instructions now ask the scanner to verify that the application still serves it.
> **Upgrade notes**
> …

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 12d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 12d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 14d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore(deps): bump Codex CLI and SDK to 0.172.0 (#2823)](https://github.com/openai/codex-security/commit/72d6f26113e511b2f8d6e9cf469bc29d1fb78e7e) | dependabot[bot] |
| 2026-11-24 | [chore(release): 0.11.0](https://github.com/openai/codex-security/commit/353fbf8f5cc0dc5287561809bb4df93319ca4642) | github-actions[bot] |
| 2026-11-24 | [docs(cli): clarify test execution during patch risk assessment (#2763)](https://github.com/openai/codex-security/commit/8c253917991f48fa0da8087056d51150937eb023) | mldangelo-oai |
| 2026-11-24 | [ci: bump actions/create-github-app-token from 3.3.0 to 3.4.0 (#2813)](https://github.com/openai/codex-security/commit/4b431802448ef49ee4b87c82473f2224aba4ca1f) | dependabot[bot] |
| 2026-11-24 | [fix(validation): refresh Continuum evidence after issue moves and dis…](https://github.com/openai/codex-security/commit/21ebff7bf0a117bbc46f720cdbb28c9ee62544b2) | mldangelo-oai |
| 2026-11-24 | [fix(deep-scan): retry Windows JSON artifact replacement and clean up …](https://github.com/openai/codex-security/commit/6077499932d24f989df15506b6dc2751f285081f) | abhiramshaji-cyber |
| 2026-11-24 | [fix(validation): exclude outdated Continuum verdicts from remediation…](https://github.com/openai/codex-security/commit/6f586d8bbc2396f0f991c1756a1364896b9c3c04) | mldangelo-oai |
| 2026-11-24 | [feat(remediation): reuse saved Continuum assessments in patch and ver…](https://github.com/openai/codex-security/commit/73eb1520f6bdfdbaebfe0ba6f2861617cdc27d73) | mldangelo-oai |
| 2026-11-24 | [fix(validation): keep Continuum verdicts while waiting for linked iss…](https://github.com/openai/codex-security/commit/81534c4b689501f7a728209aafe84ae486de6286) | mldangelo-oai |
| 2026-11-24 | [fix(validation): resume pending Continuum checks and preserve inconcl…](https://github.com/openai/codex-security/commit/2324a7b557c49b9f0640ca4833ec56ac796dea9d) | mldangelo-oai |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
