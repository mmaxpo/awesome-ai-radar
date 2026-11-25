# addyosmani/agent-skills

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Production-grade engineering skills for AI coding agents |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 120.4k |
| 🍴 **Forks** | 12.5k |
| 🐞 **Open issues + PRs** | [115](https://github.com/addyosmani/agent-skills/issues) |
| 💻 **Languages** | JavaScript 77% · Shell 21% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `antigravity` `claude-code` `cursor` `skills` `codex` |
| 🕒 **Last activity** | 2026-11-24 (yesterday) |
| 📅 **Created** | 2026-02-15 |
| 📦 **Latest release** | [0.6.18](https://github.com/addyosmani/agent-skills/releases/tag/0.6.18) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2.1 MB |
| 🌐 **Website** | https://skills.addy.ie |

## 📦 Recent releases

### [0.6.18](https://github.com/addyosmani/agent-skills/releases/tag/0.6.18) — Agent Skills 0.6.18
<sub>2026-11-24 · yesterday</sub>

> Agent Skills 0.6.18 makes every skill carry its own copy of the shared checklists, so installing a single skill no longer leaves its references missing. It also fixes two security references that said more than they did.
> **Skills**
> - **Shared checklists ship with each skill** (#670, @drakulavich, reviewed by @federicobartoli, fixes #597). Skills that use a checklist from the root `references/` now carry a generated copy under `references/shared/`. A per-skill install has everything it links to, and nothing depends on symlinks, so it also works on Windows. CI fails if a copy drifts from its source. **Contributors:** after editing anything in `references/`, run `node scripts/sync-shared-references.js` and commit the copies.
> - **The SSRF example is marked as partial** (#809, @RogueTex, #805). It was labelled GOOD, but `fetch` resolves DNS again after the check. It now says what the precheck doesn't cover and how to close the gap at connection time.
> - **The floor guard no longer prints the lines it flags** (#806, @TanmayShah29, #804). Findings are reported as `file:line`, so a suppressed line holding a secret-like value stays out of terminals and agent logs.
> - **The a11y audit script resolves from the installed skill** (#810, @RogueTex). It works from your own project, not only from this repo's root.
> …

### [0.6.17](https://github.com/addyosmani/agent-skills/releases/tag/0.6.17) — Agent Skills 0.6.17
<sub>2026-11-18 · 6d ago</sub>

> Agent Skills 0.6.17 adds an accessibility-engineering skill for auditing and fixing WCAG 2.2 AA issues, fixes a rollback workflow that could never log in, and lets you regrade eval runs without paying for them again.
> **New skill**
> - **accessibility-engineering** (#261, @Chukwuebuka-2003, reviewed by @nucliweb). Audits an existing interface with pinned axe-core and pa11y, triages the findings, and walks through the manual keyboard and screen reader checks the tools can't do. It ships an `accessibility-auditor` persona, an `/a11y` command, and an audit script that fails a partial run instead of reporting zero violations. Building new UI stays with frontend-ui-engineering. The shared accessibility checklist now targets WCAG 2.2 AA and matches the skill.
> **Fixes**
> - **Rollback can log in** (#799, @divya0795). The ci-cd-and-automation rollback workflow ran `vercel rollback` on a runner with no Vercel login, so it failed exactly when needed. It now passes the token, like the preview step already did.
> - **Review evidence from the right tree** (#795, @TanmayShah29, reported by @Scroller251-cloud in #788). code-review-and-quality checks that the checkout is clean and on the reviewed ref before running tests or probes, since a working copy can hold another session's edits.
> …

### [0.6.16](https://github.com/addyosmani/agent-skills/releases/tag/0.6.16) — Agent Skills 0.6.16
<sub>2026-11-14 · 11d ago</sub>

> Agent Skills 0.6.16 lets specs evolve past V1, teaches the docs skill to spot drift, stops the frontend skill from installing toolchains just to verify, and fixes two quality-gate examples that could never fail.
> **Skills**
> - **Spec evolution** (#383, @ayobamiseun). Specs now carry a version and an Out of Scope (Deferred) list, and a change to a shipped feature gets its own small delta spec (`SPEC-<change>.md`) instead of a rewrite. `/spec` writes one when `SPEC.md` already exists, and `/build auto` picks the delta that isn't `Status: implemented` and refuses to run a plan generated from a different spec.
> - **Documentation drift** (#514, @vyasdx). When a doc may be stale, documentation-and-adrs compares the last commit to the code with the last commit to the doc, and says "can't tell" instead of "current" when the history is unordered. Change logs are appended to, never rewritten.
> - **Verify with what the project has** (#732, @TwelveNights). frontend-ui-engineering no longer installs a test runner or type checker just to check its work, and follows the WAI-ARIA APG patterns for menus, dialogs, tabs, listboxes and comboboxes. Measured +0.10 across 11 models, with package installs down from 24% to 4% of runs.
> - **Review findings checked against the code** (#736, @CybotTM). code-review-and-quality checks each finding against the callers, guards and tests that reach the change, labels defects already in the base separately, and treats zero findings as a valid result.
> …

### [0.6.15](https://github.com/addyosmani/agent-skills/releases/tag/0.6.15) — Agent Skills 0.6.15
<sub>2026-10-31 · 25d ago</sub>

> Agent Skills 0.6.15 stops the security skill's staged-secret check from printing the secret it finds, fixes two simplify-ignore bugs that could corrupt protected code, and makes the constraints skill's security and accessibility gates actually fail CI.
> **Security**
> - **The staged-secret check no longer echoes credentials** (#718, @santhiprakash, reported by @xmxxc in #717). The old `git diff --cached | grep` printed every matching line, so a staged key landed in the terminal and in any agent's transcript. It also read as clean when git failed. The check is now `git diff --cached -i -G'…' --name-only`: it prints only file names, and a git failure exits non-zero by itself. Fixed in all three places it was documented.
> **Hooks**
> - **simplify-ignore restores re-indented placeholders cleanly** (#766, @Quinnod345, #765). If `/code-simplify` un-indented a placeholder or edited its reason, Stop wrote back a broken comment around the block, a syntax error in any `/* */` language. Blocks marked with `-- simplify-ignore-start` (SQL, Lua, Haskell) no longer warn that they were deleted, and a missing lock directory no longer stops Stop before every file is restored.
> **Skills**
> …

### [0.6.14](https://github.com/addyosmani/agent-skills/releases/tag/0.6.14) — Agent Skills 0.6.14
<sub>2026-10-29 · 27d ago</sub>

> Agent Skills 0.6.14 is mostly about code samples. More than twenty snippets across the skills either failed as written or taught the wrong thing, and they're fixed. It also closes two supply-chain and injection risks in the samples, stops Claude Code from starting `/ship` or `/build` on its own, and brings the root manifest in line with Agent Plugins 1.0.0.
> **Security fixes in the samples**
> - **The Lighthouse CI example ran the unscoped `lhci` package** (#721), which isn't Lighthouse CI. It now invokes `@lhci/cli`.
> - **The rollback workflow passed its input straight into `run:`** (#691), a script injection in any repo that copied it. It goes through `env` now.
> - The constraints skill scans the working tree for secrets, not only commits (#729), and the hardening reference returns 404 before an ownership check reads a missing task (#726).
> **Samples that now work as written**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [chore(release): bump plugin manifests to 0.6.18](https://github.com/addyosmani/agent-skills/commit/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74) | r2 |
| 2026-11-24 | [Merge #773: exercise the version-validator CLI against temporary mani…](https://github.com/addyosmani/agent-skills/commit/5695183d6b0aa4b1573498273fe45288b22442e1) | addyosmani |
| 2026-11-24 | [Merge #771: cache large WebFetch responses without argv limits](https://github.com/addyosmani/agent-skills/commit/c8418b72d9a8d43b44502c83d24f1303022ce4f7) | addyosmani |
| 2026-11-24 | [Merge #769: isolate fixture repositories from inherited Git hooks](https://github.com/addyosmani/agent-skills/commit/99820a90559cdc5a5715867b1ad3f21f6523557c) | addyosmani |
| 2026-11-24 | [Merge #806: report floor-guard findings by file and line](https://github.com/addyosmani/agent-skills/commit/ca5d610ccef46574198124f0ed727b5e32499009) | addyosmani |
| 2026-11-24 | [Merge #807: let plan commands defer to the configured task list target](https://github.com/addyosmani/agent-skills/commit/ec9d4ae4959fbff9d03974ecb24325aa026a8e6e) | addyosmani |
| 2026-11-24 | [Merge #809: mark the SSRF precheck example as incomplete](https://github.com/addyosmani/agent-skills/commit/65021295f7e97abf8311bb9e8d3425b290240c29) | addyosmani |
| 2026-11-24 | [Merge #813: pin the example workflows to Node 24 action majors](https://github.com/addyosmani/agent-skills/commit/522482d28c81d593d0f296f66e730748cf69e7b0) | addyosmani |
| 2026-11-24 | [Merge #810: resolve the a11y audit helper from the installed skill](https://github.com/addyosmani/agent-skills/commit/9133aae7af4937900079ba9efb3efbdb418970ab) | addyosmani |
| 2026-11-24 | [Merge #670: ship shared checklists as generated skill-local copies](https://github.com/addyosmani/agent-skills/commit/3ed9f6961c481a681f6533c1f58369a93eb23526) | addyosmani |

[See all commits ↗](https://github.com/addyosmani/agent-skills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/addyosmani/agent-skills.git
```
