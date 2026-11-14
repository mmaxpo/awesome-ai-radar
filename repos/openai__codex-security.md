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
| ⭐ **Stars** | 13.4k |
| 🍴 **Forks** | 1.0k |
| 🐞 **Open issues + PRs** | [172](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 76% · Python 21% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 83.6 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 2d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 2d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 4d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

### [npm-v0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1) — Codex Security 0.9.1
<sub>2026-11-10 · 4d ago</sub>

> **Highlights**
> - The npm package includes Developer ID-signed native addons for Apple Silicon and Intel Macs. This lets Codex Desktop load the addon when preparing review items.
> - Deep Scan runs independent Standard reviews in batches. Workers can share leads and verify each other's evidence. The final report groups observations that have the same fix and retains the source locations from each review. [Deep Scan guide](https://github.com/openai/codex-security/blob/main/sdk/typescript/docs/cli.md#configure-deep-scans)
> - External scanner imports are enabled by default in the CLI, SDK, and plugin. You can preview supported reports, save findings locally, and publish supported findings to Cloud. The scanner guides list the accepted formats and which inputs are local-only. [Scanner import guides](https://github.com/openai/codex-security/blob/main/docs/scanner-imports/README.md)
> - `scans logs` finds sessions faster in large compressed histories. The GitHub Action also includes scan scope limitations in its job summary, including when a scan returns zero findings.
> **Upgrade notes**
> …

### [npm-v0.9.0](https://github.com/openai/codex-security/releases/tag/npm-v0.9.0) — Codex Security 0.9.0 (source only)
<sub>2026-11-10 · 4d ago</sub>

> **Source-only release.** The source archives below contain the original 0.9.0 release commit. The 0.9.0 build stopped during macOS signing, before npm publication. For the signed CLI and SDK package, use [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> **Highlights**
> - Deep Scan runs independent Standard reviews in batches. Workers can share leads and verify each other's evidence. The final report groups observations that have the same fix and retains the source locations from each review. [Deep Scan guide](https://github.com/openai/codex-security/blob/npm-v0.9.0/sdk/typescript/docs/cli.md#configure-deep-scans)
> - External scanner imports are enabled by default in the CLI, SDK, and plugin. You can preview supported reports, save findings locally, and publish supported findings to Cloud. The scanner guides list the accepted formats and which inputs are local-only. [Scanner import guides](https://github.com/openai/codex-security/blob/npm-v0.9.0/docs/scanner-imports/README.md)
> - `scans logs` finds sessions faster in large compressed histories. The GitHub Action also includes scan scope limitations in its job summary, including when a scan returns zero findings.
> **Upgrade notes**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [fix(plugin): preserve Windows helper exit codes (#2651)](https://github.com/openai/codex-security/commit/173483d7c658be7a512c93d9559bf01a05d5b196) | JoaoMarcos44 |
| 2026-11-13 | [docs: clarify Deep Scan preflight sandbox limits (#2611)](https://github.com/openai/codex-security/commit/f26b669b56a4423abd773c81f6c6c9c2ebadc42a) | dajiaohuang |
| 2026-11-13 | [feat(examples): add synthetic security workflow benchmarks (#2618)](https://github.com/openai/codex-security/commit/462bad3da3089d67c6837f913e5a2f216c9c4ff5) | neharungta |
| 2026-11-12 | [feat(imports): import CrowdStrike FCS IaC findings locally (#2589)](https://github.com/openai/codex-security/commit/4822a9cbc4c4976b6f81ba5afd50787af923ba91) | carlosmmatos-cs |
| 2026-11-12 | [feat(scanner-imports): import AWS Continuum code issues (#2619)](https://github.com/openai/codex-security/commit/2911786f243f08fd61ad854f5c527e7b0c404ccc) | jameshiester-oai |
| 2026-11-12 | [chore(release): 0.10.0](https://github.com/openai/codex-security/commit/f465432bc4c8882a8b667985a9f68045483ed796) | github-actions[bot] |
| 2026-11-12 | [feat(scans): resume interrupted Standard scans (#2610)](https://github.com/openai/codex-security/commit/69038a2f56514f2d4fab43683c97cd313dc5cecb) | ianw-oai |
| 2026-11-12 | [ci: stabilize campaign executable lookup tests (#2621)](https://github.com/openai/codex-security/commit/6b6c5251cf2deb43974beb554f1c1a0899b15871) | mldangelo-oai |
| 2026-11-11 | [feat(import): include AWS-generated patches in Continuum findings (#2…](https://github.com/openai/codex-security/commit/7b5335becab87f87606e5a948518728b6fa1e91a) | mldangelo-oai |
| 2026-11-11 | [fix(action): preserve literal scan paths (#2617)](https://github.com/openai/codex-security/commit/ed649f6337b84f11d5fcf6b13ff90ff8d608a830) | mldangelo-oai |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
