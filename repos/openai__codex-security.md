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
| ⭐ **Stars** | 14.2k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [195](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 77% · Python 19% · JavaScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-20 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 95.7 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — Codex Security GitHub Action 0.10.1
<sub>2026-11-18 · yesterday</sub>

> GitHub Action for [Codex Security 0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1).
> Installs `@openai/codex-security@0.10.1`.
> ```yaml
> uses: openai/codex-security@bf650710f36c16936324efe250a49cdd9f2da037 # action-v0.10.1
> ```

### [npm-v0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1) — Codex Security 0.10.1
<sub>2026-11-18 · yesterday</sub>

> **Highlights**
> - **Exclude paths from scans.** Run `cs scan . --exclude-path examples/` to exclude a directory from review in Standard, Deep, or diff scans. Repeat the flag for more paths, or set `scan.exclude_paths` in your project configuration. Paths are literal and relative to the repository. The scanner can still read excluded files for context and filters out findings whose locations all fall under excluded paths.
> - **Import scanner findings.** Use `cs import continuum` to collect AWS Continuum code issues with their supporting evidence. Attack-path analysis can use observations from the tested target when assessing reachability and severity. You can also import saved CrowdStrike Falcon Cloud Security IaC reports into your local workbench.
> - **Deep Scan.** When Codex blocks a worker request because of a misalignment policy violation, Deep Scan now stops and reports the refusal without retrying the request.
> - **Threat modeling.** When a route appears in a test or on a deleted line, the threat-modeling instructions now ask the scanner to verify that the application still serves it.
> **Upgrade notes**
> …

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 8d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 8d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 10d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-20 | [fix(cli): honor configured caller scope in captured stack investigati…](https://github.com/openai/codex-security/commit/9b7b90c94c94b7eaec65018b0265b868f8b37e28) | utsav-oai |
| 2026-11-20 | [fix(sdk): accept indexed stack misses (#2761)](https://github.com/openai/codex-security/commit/f9114413c92bd92d6b5f8aa72aea733062dd5ad0) | utsav-oai |
| 2026-11-20 | [feat(cli)!: support incremental exploitability investigations (#2745)](https://github.com/openai/codex-security/commit/a69515510f8525e7909f770e61f5c8be450e3e29) | utsav-oai |
| 2026-11-20 | [fix(workbench): split legacy roots from linked global finding groups …](https://github.com/openai/codex-security/commit/8c485db1432fbe0734cabf0249def5204a473d95) | hyeonsang010716 |
| 2026-11-20 | [fix(config): keep cached scan skills disabled across path aliases (#2…](https://github.com/openai/codex-security/commit/e426284c595fb4616b9909826e142e1b84a3ae59) | adityajai119 |
| 2026-11-20 | [fix(cli): assess captured stacks against public advisory conditions (…](https://github.com/openai/codex-security/commit/bcf39188a399d023331065766118c4f8996ea850) | utsav-oai |
| 2026-11-20 | [feat(cli): render exploitability reports in Markdown and interactive …](https://github.com/openai/codex-security/commit/ff1123120b151dd92cbf423eb845be1abc3303ff) | utsav-oai |
| 2026-11-20 | [fix(history): use singular nouns for one-item match-all counts (#2751)](https://github.com/openai/codex-security/commit/72f4502902766bd01bd21aea138edb777098e1b9) | i098 |
| 2026-11-20 | [docs(cli): clarify static verification is instruction-based (#2744)](https://github.com/openai/codex-security/commit/c5f9a9100c3b97212b571219096e6343bf1dd41b) | TheOutlandsDev |
| 2026-11-19 | [chore(deps): bump promptfoo from 0.124.1 to 0.125.1 in /evals/triage-…](https://github.com/openai/codex-security/commit/bd09ff8254667cedd355cd1f2e354e5a8002facf) | dependabot[bot] |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
