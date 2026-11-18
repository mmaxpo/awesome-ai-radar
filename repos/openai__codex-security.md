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
| ⭐ **Stars** | 14.0k |
| 🍴 **Forks** | 1.1k |
| 🐞 **Open issues + PRs** | [187](https://github.com/openai/codex-security/issues) |
| 💻 **Languages** | TypeScript 76% · Python 21% · JavaScript 2% |
| 📜 **License** | Apache-2.0 |
| 🏷 **Topics** | `ai-security` `application-security` `cli` `code-scanning` `codex` `codex-security` `cybersecurity` `devsecops` `nodejs` `npm` `openai` `sdk` `security` `typescript` `vulnerability-scanning` |
| 🕒 **Last activity** | 2026-11-18 (today) |
| 📅 **Created** | 2026-07-13 |
| 📦 **Latest release** | [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — 2026-11-12 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 88.3 MB |
| 🌐 **Website** | https://developers.openai.com/codex/security |

## 📦 Recent releases

### [action-v0.10.0](https://github.com/openai/codex-security/releases/tag/action-v0.10.0) — Codex Security GitHub Action 0.10.0
<sub>2026-11-12 · 6d ago</sub>

> GitHub Action for [Codex Security 0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0).
> Installs `@openai/codex-security@0.10.0`.
> ```yaml
> uses: openai/codex-security@3bde66eda1a5c6b0c4cd245f51c16424c9374afb # action-v0.10.0
> ```

### [npm-v0.10.0](https://github.com/openai/codex-security/releases/tag/npm-v0.10.0) — Codex Security 0.10.0
<sub>2026-11-12 · 6d ago</sub>

> **Highlights**
> Codex Security 0.10.0 gives clearer guidance when a patch is blocked, lets interrupted Standard scans resume, and adds a budget for batch scans.
> - **Blocked patch results.** The patch prompt asks whether any files changed, what stopped the fix, and what to do next. When a fix depends on work outside the checkout, the result explains why the external change is needed and where it belongs when known. [#2609](https://github.com/openai/codex-security/pull/2609)
> - **Standard scan setup.** Standard scans start with the vulnerability audit and load host-specific instructions when needed. Focused investigators receive their own briefs, and scan history records the file count from the scan's inventory. [#2046](https://github.com/openai/codex-security/pull/2046)
> - **Resume interrupted Standard scans.** Run `codex-security scans resume SCAN_ID` to continue from a saved checkpoint in the original Codex session. The resumed scan retains its usage and budget. [#2610](https://github.com/openai/codex-security/pull/2610)
> - **Batch scan budgets.** Set `--max-total-cost` on bulk or component scans to share one estimated budget across repositories or components, including retries and recoveries. In-flight work can exceed the estimate. [#2592](https://github.com/openai/codex-security/pull/2592)
> …

### [action-v0.9.1](https://github.com/openai/codex-security/releases/tag/action-v0.9.1) — Codex Security GitHub Action 0.9.1
<sub>2026-11-10 · 8d ago</sub>

> GitHub Action for [Codex Security 0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1).
> Installs `@openai/codex-security@0.9.1`.
> ```yaml
> uses: openai/codex-security@a98b35d7eef9f85c298c86229445bb64ac427aaf # action-v0.9.1
> ```

### [npm-v0.9.1](https://github.com/openai/codex-security/releases/tag/npm-v0.9.1) — Codex Security 0.9.1
<sub>2026-11-10 · 8d ago</sub>

> **Highlights**
> - The npm package includes Developer ID-signed native addons for Apple Silicon and Intel Macs. This lets Codex Desktop load the addon when preparing review items.
> - Deep Scan runs independent Standard reviews in batches. Workers can share leads and verify each other's evidence. The final report groups observations that have the same fix and retains the source locations from each review. [Deep Scan guide](https://github.com/openai/codex-security/blob/main/sdk/typescript/docs/cli.md#configure-deep-scans)
> - External scanner imports are enabled by default in the CLI, SDK, and plugin. You can preview supported reports, save findings locally, and publish supported findings to Cloud. The scanner guides list the accepted formats and which inputs are local-only. [Scanner import guides](https://github.com/openai/codex-security/blob/main/docs/scanner-imports/README.md)
> - `scans logs` finds sessions faster in large compressed histories. The GitHub Action also includes scan scope limitations in its job summary, including when a scan returns zero findings.
> **Upgrade notes**
> …

### [npm-v0.9.0](https://github.com/openai/codex-security/releases/tag/npm-v0.9.0) — Codex Security 0.9.0 (source only)
<sub>2026-11-10 · 8d ago</sub>

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
| 2026-11-18 | [test(dedupe): cover retries for overloaded and internal Codex errors …](https://github.com/openai/codex-security/commit/ffee55ab54ca4ecebb1c088146177164c1228d91) | Shizoqua |
| 2026-11-18 | [docs: add security workflow sample to examples index (#2666)](https://github.com/openai/codex-security/commit/aa4f286743a79337d6e5080e2a77ece474304b95) | adwaitm1301 |
| 2026-11-18 | [feat(cli): investigate supplied dependency stacks (#2713)](https://github.com/openai/codex-security/commit/c1482dc808b7b3c9cdc02cba6822f68a5f4a4b14) | utsav-oai |
| 2026-11-17 | [feat(cli): add an opt-in foundation for dependency investigations (#2…](https://github.com/openai/codex-security/commit/78418ad7c907c67a5bf5d0f2620e8b6afda3710a) | utsav-oai |
| 2026-11-17 | [chore(release): 0.10.1](https://github.com/openai/codex-security/commit/9293f253bb979fd470d91e7ba1117362c0b304a3) | github-actions[bot] |
| 2026-11-17 | [feat(scanner-imports): retain validation evidence for individual Cont…](https://github.com/openai/codex-security/commit/775231e9bf5f6bcda0bef5ff0b82860b5551f923) | mldangelo-oai |
| 2026-11-17 | [feat(classify-severity): emit structured diagnostics on hosted record…](https://github.com/openai/codex-security/commit/acced5b84cb5e0565c95f90709b08014d85ffd7e) | kmbroai |
| 2026-11-17 | [fix(findings): use saved comparison evidence across linked worktrees …](https://github.com/openai/codex-security/commit/034d9762878a52f0458ae25c92eb0679de97d38f) | mldangelo-oai |
| 2026-11-17 | [chore(deps): update the Python and Node devcontainer features (#2560)](https://github.com/openai/codex-security/commit/887ef11a25063b3ed2eb4ec9282e136d7eff0906) | dependabot[bot] |
| 2026-11-17 | [fix(history): avoid repeating findings in bulk scan matching (#149)](https://github.com/openai/codex-security/commit/95e0c8891c887f2a7c18df4fdbc0c57cc3c9111c) | GautamSharma99 |

[See all commits ↗](https://github.com/openai/codex-security/commits)

## ⬇️ Get it

```bash
git clone https://github.com/openai/codex-security.git
```
