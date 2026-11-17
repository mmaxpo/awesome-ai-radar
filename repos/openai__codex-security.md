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
| ⭐ **Stars** | 13.9k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [180](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 76% · Python 21% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-17 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 87.4 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 5d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 5d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 7d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

### [npm-v0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1) — Codex Security 0.9.1
<sub>2026-11-10 · 7d ago</sub>

> **Highlights**
> - The npm package includes Developer ID-signed native addons for Apple Silicon and Intel Macs. This lets Codex Desktop load the addon when preparing review items.
> - Deep Scan runs independent Standard reviews in batches. Workers can share leads and verify each other's evidence. The final report groups observations that have the same fix and retains the source locations from each review. [Deep Scan guide](https://github.com/openai/codex-security/blob/main/sdk/typescript/docs/cli.md#configure-deep-scans)
> - External scanner imports are enabled by default in the CLI, SDK, and plugin. You can preview supported reports, save findings locally, and publish supported findings to Cloud. The scanner guides list the accepted formats and which inputs are local-only. [Scanner import guides](https://github.com/openai/codex-security/blob/main/docs/scanner-imports/README.md)
> - `scans logs` finds sessions faster in large compressed histories. The GitHub Action also includes scan scope limitations in its job summary, including when a scan returns zero findings.
> **Upgrade notes**
> …

### [npm-v0.9.0](https://github.com/openai/codex-security/releases/tag/npm-v0.9.0) — Codex Security 0.9.0 (source only)
<sub>2026-11-10 · 7d ago</sub>

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
| 2026-11-17 | [chore(deps): update the Python and Node devcontainer features (#2560)](https://github.com/openai/codex-security/commit/887ef11a25063b3ed2eb4ec9282e136d7eff0906) | dependabot[bot] |
| 2026-11-17 | [fix(history): avoid repeating findings in bulk scan matching (#149)](https://github.com/openai/codex-security/commit/95e0c8891c887f2a7c18df4fdbc0c57cc3c9111c) | GautamSharma99 |
| 2026-11-17 | [fix(deep-scan): stop on Codex misalignment policy refusals (#2410)](https://github.com/openai/codex-security/commit/506e7c569fdb090fe799fe692de56637ffd96ed1) | Shizoqua |
| 2026-11-17 | [fix(bulk-scan): reject receipt IDs missing from the campaign (#2677)](https://github.com/openai/codex-security/commit/6548b9246770ee3e19d99c5044d85e43f85e1c80) | mldangelo-oai |
| 2026-11-17 | [docs(examples): compare vulnerable and repaired invoice ownership che…](https://github.com/openai/codex-security/commit/227bd55457af8beb0cde8cd09f4f092c5daceddf) | neharungta |
| 2026-11-17 | [docs(providers): configure OrcaRouter through a native file profile (…](https://github.com/openai/codex-security/commit/9ebd3711ebee1264d5b89af3ab1e31ccea2d92c8) | martinzudergaming-a11y |
| 2026-11-17 | [docs(providers): document a tested xAI Responses gateway workaround (…](https://github.com/openai/codex-security/commit/3cae0778d6bbf7de1eed7ddcb7426d8ef52784f7) | mldangelo-oai |
| 2026-11-17 | [docs: add a software citation for Codex Security (#2639)](https://github.com/openai/codex-security/commit/b517c49ec423c01b7e23500afa94606dcc2dca5d) | mldangelo-oai |
| 2026-11-17 | [docs(bulk-scan): show how --max-attempts works across two runs (#100)](https://github.com/openai/codex-security/commit/7a07634dcd59897740aaa418a61bdaedfd57084c) | GautamSharma99 |
| 2026-11-17 | [docs(threat-model): check whether the app still serves a route (#200)](https://github.com/openai/codex-security/commit/139e093d810f4c7a928ffe163496a94549894363) | Haiduongcable |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
