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
| 🐞 **Open issues + PRs** | [203](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 77% · Python 20% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-19 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 87.6 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — Codex Security GitHub Action 0.10.1
<sub>2026-11-18 · today</sub>

> GitHub Action for [Codex Security 0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1).
> Installs `@openai/codex-security@0.10.1`.
> ```yaml
> uses: openai/codex-security@bf650710f36c16936324efe250a49cdd9f2da037 # action-v0.10.1
> ```

### [npm-v0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1) — Codex Security 0.10.1
<sub>2026-11-18 · today</sub>

> **Highlights**
> - **Exclude paths from scans.** Run `cs scan . --exclude-path examples/` to exclude a directory from review in Standard, Deep, or diff scans. Repeat the flag for more paths, or set `scan.exclude_paths` in your project configuration. Paths are literal and relative to the repository. The scanner can still read excluded files for context and filters out findings whose locations all fall under excluded paths.
> - **Import scanner findings.** Use `cs import continuum` to collect AWS Continuum code issues with their supporting evidence. Attack-path analysis can use observations from the tested target when assessing reachability and severity. You can also import saved CrowdStrike Falcon Cloud Security IaC reports into your local workbench.
> - **Deep Scan.** When Codex blocks a worker request because of a misalignment policy violation, Deep Scan now stops and reports the refusal without retrying the request.
> - **Threat modeling.** When a route appears in a test or on a deleted line, the threat-modeling instructions now ask the scanner to verify that the application still serves it.
> **Upgrade notes**
> …

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 7d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 7d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 9d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-19 | [feat: add JSON error details for scan validation failures (#2730)](https://github.com/openai/codex-security/commit/8b114ad59518ba8529e9ea9e7d66004f6b4bc26e) | ianw-oai |
| 2026-11-18 | [feat(cli): add independently reviewed dependency checks (#2715)](https://github.com/openai/codex-security/commit/5313e2e8579de78dea582bfed0d96cec493f5594) | utsav-oai |
| 2026-11-18 | [test(cli): honor the CI timeout for integration commands (#2725)](https://github.com/openai/codex-security/commit/067c9b30616916c66f2da7a6fc8919ce9fab5447) | mldangelo-oai |
| 2026-11-18 | [chore(deps): bump the codex group across 3 directories with 2 updates…](https://github.com/openai/codex-security/commit/a1e56b73a55638dd500b12d5dd62d3e9d7453582) | dependabot[bot] |
| 2026-11-18 | [chore(deps): update napi-derive to 3.7.1 in the native plugin (#2721)](https://github.com/openai/codex-security/commit/fd5bf1a093e720e1bb3416a9eef43dc764ccaa90) | dependabot[bot] |
| 2026-11-18 | [chore(deps): bump fast-xml-parser from 5.11.1 to 5.12.0 in /github-ac…](https://github.com/openai/codex-security/commit/fe1c651640c845d72721daeb5e31270113d72fde) | dependabot[bot] |
| 2026-11-18 | [chore(deps): bump ruff from 0.17.3 to 0.17.4 in /plugins/codex-securi…](https://github.com/openai/codex-security/commit/2101ecb33b0bcb15099e77425de571ced395a836) | dependabot[bot] |
| 2026-11-18 | [chore(deps): bump tokenx from 1.6.0 to 2.2.0 in /sdk/typescript (#2627)](https://github.com/openai/codex-security/commit/171e785e24d9a2f549c3594472bb460f1dbd02c3) | dependabot[bot] |
| 2026-11-18 | [chore(deps): bump napi from 3.16.1 to 3.16.2 in /plugins/codex-securi…](https://github.com/openai/codex-security/commit/96fb3de45ac7cc0513a12cf292373c00e4c6ee33) | dependabot[bot] |
| 2026-11-18 | [ci: bump docker/login-action from 4.7.0 to 4.8.0 (#2642)](https://github.com/openai/codex-security/commit/29b002fe8b7973ea7a6212f93b11fad7b619b700) | dependabot[bot] |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
