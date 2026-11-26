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
| ⭐ **Stars** | 14.4k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [220](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 77% · Python 19% · JavaScript 3% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.11.0](https://github.com/openai/codex-security/releases/tag/action-v0.11.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 91.5 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.11.0](https://github.com/openai/codex-security/releases/tag/action-v0.11.0) — Codex Security GitHub Action 0.11.0
<sub>2026-11-24 · yesterday</sub>

> GitHub Action for [Codex Security 0.11.0](https://github.com/openai/codex-security/releases/tag/npm-v0.11.0).
> Installs `@openai/codex-security@0.11.0`.
> ```yaml
> uses: openai/codex-security@02c70601a70dde2d1c9c9867d4ead298370890d1 # action-v0.11.0
> ```

### [npm-v0.11.0](https://github.com/openai/codex-security/releases/tag/npm-v0.11.0) — Codex Security 0.11.0
<sub>2026-11-24 · yesterday</sub>

> **Highlights**
> Codex Security 0.11.0 adds two opt-in ways to investigate a finding. You can check whether a dependency advisory applies to your code or ask AWS Continuum to assess a code finding in a deployed environment.
> - **Dependency investigations.** Set `CODEX_SECURITY_ENABLE_DEPENDENCY_EXPLOITABILITY=1` and run `cs exploitability check "$CVE_ID" --format html` from your checkout. You can also supply captured call stacks. The check asks an independent reviewer to verify the evidence. The report shows which advisory conditions are met and where the evidence is incomplete. [Experimental CLI guide](https://github.com/openai/codex-security/blob/npm-v0.11.0/sdk/typescript/docs/cli.md#experimental-dependency-investigations)
> - **AWS Continuum validation.** Select a trusted project file that configures Continuum. The CLI sends findings to AWS when you request validation. The packaged plugin submits them automatically after a Standard, Deep, or diff scan with that file. Check the destination first. Finding details can contain sensitive information. Local validation notes stay on the host by default. Codex severity and `--fail-on-severity` stay unchanged. [Choose what to send and resume a check](https://github.com/openai/codex-security/blob/npm-v0.11.0/docs/validation-providers.md)
> - **Patch and verify.** On the original host, `cs patch` and `cs verify-fix` can reuse current Continuum evidence. They distinguish issue-wide results from findings assessed individually and evaluate the fix independently. If a finding moves to another issue, rerun `cs validate --scan` with the original options to refresh it. Disputed verdicts and scores require newer evidence.
> - **Deep Scan on Windows.** Deep Scan retries a heartbeat or receipt update when another process briefly holds the file open. If the write fails, the previous file stays intact.
> …

### [action-v0.10.1](https://github.com/openai/codex-security/releases/tag/action-v0.10.1) — Codex Security GitHub Action 0.10.1
<sub>2026-11-18 · 7d ago</sub>

> GitHub Action for [Codex Security 0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1).
> Installs `@openai/codex-security@0.10.1`.
> ```yaml
> uses: openai/codex-security@bf650710f36c16936324efe250a49cdd9f2da037 # action-v0.10.1
> ```

### [npm-v0.10.1](https://github.com/openai/codex-security/releases/tag/npm-v0.10.1) — Codex Security 0.10.1
<sub>2026-11-18 · 7d ago</sub>

> **Highlights**
> - **Exclude paths from scans.** Run `cs scan . --exclude-path examples/` to exclude a directory from review in Standard, Deep, or diff scans. Repeat the flag for more paths, or set `scan.exclude_paths` in your project configuration. Paths are literal and relative to the repository. The scanner can still read excluded files for context and filters out findings whose locations all fall under excluded paths.
> - **Import scanner findings.** Use `cs import continuum` to collect AWS Continuum code issues with their supporting evidence. Attack-path analysis can use observations from the tested target when assessing reachability and severity. You can also import saved CrowdStrike Falcon Cloud Security IaC reports into your local workbench.
> - **Deep Scan.** When Codex blocks a worker request because of a misalignment policy violation, Deep Scan now stops and reports the refusal without retrying the request.
> - **Threat modeling.** When a route appears in a test or on a deleted line, the threat-modeling instructions now ask the scanner to verify that the application still serves it.
> **Upgrade notes**
> …

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 14d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [feat(skills): select workflow instructions at runtime (#2296)](https://github.com/openai/codex-security/commit/256cddf5eb503a8e34b991c86265ec85776a9b07) | mldangelo-oai |
| 2026-11-25 | [fix(cli): honor scan automation options and output contracts (#1186)](https://github.com/openai/codex-security/commit/9e4594e5e50c284e26e207366cedecb96e28cd29) | mldangelo-oai |
| 2026-11-24 | [feat: default scans to GPT-6.1 Sol with high reasoning effort (#2358)](https://github.com/openai/codex-security/commit/4d4b4fedf1920e728ca1f775115491752a6002d7) | mldangelo-oai |
| 2026-11-24 | [refactor: simplify sealed finding projections and SARIF line hashes (…](https://github.com/openai/codex-security/commit/3d5faa06d5bfd7e3b2a46148ef5391eb70a49016) | mldangelo-oai |
| 2026-11-24 | [refactor: simplify dependency discovery, worklist queries, and trace …](https://github.com/openai/codex-security/commit/035d95b28264469a6ce8ccf05c46d38b0f67a5bb) | mldangelo-oai |
| 2026-11-24 | [test: share workbench, checkpoint, and Deep Scan fixtures (#2828)](https://github.com/openai/codex-security/commit/96a80780d9fe95fdb2c04dea0c8278374273f6a9) | mldangelo-oai |
| 2026-11-24 | [refactor: simplify workbench requests and finding history projections…](https://github.com/openai/codex-security/commit/16102d6a02c1222bf37055695f07d735a9febdfc) | mldangelo-oai |
| 2026-11-24 | [test(sdk): simplify client cleanup and distinguish usage counters (#2…](https://github.com/openai/codex-security/commit/33590f4b16712b53d73940b073329a4b27ba2879) | mldangelo-oai |
| 2026-11-24 | [refactor(cli): define opt-in flags with a shared schema factory (#2830)](https://github.com/openai/codex-security/commit/eead4a80aa3fa2d4e43f9e8950465ae99b311801) | mldangelo-oai |
| 2026-11-24 | [test: simplify release and grading fixtures (#2825)](https://github.com/openai/codex-security/commit/93299f6d7d59fc1eb5332e4f9a341c661389cbc5) | mldangelo-oai |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
