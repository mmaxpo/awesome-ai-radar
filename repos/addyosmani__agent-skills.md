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
| ⭐ **Stars** | 119.7k |
| 🍴 **Forks** | 12.4k |
| 🐞 **Open issues + PRs** | [126](https://github.com/addyosmani/agent-skills/issues) |
| 💻 **Languages** | JavaScript 76% · Shell 22% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `antigravity` `claude-code` `cursor` `skills` `codex` |
| 🕒 **Last activity** | 2026-11-18 (3d ago) |
| 📅 **Created** | 2026-02-15 |
| 📦 **Latest release** | [0.6.17](https://github.com/addyosmani/agent-skills/releases/tag/0.6.17) — 2026-11-18 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 2.0 MB |
| 🌐 **Website** | https://skills.addy.ie |

## 📦 Recent releases

### [0.6.17](https://github.com/addyosmani/agent-skills/releases/tag/0.6.17) — Agent Skills 0.6.17
<sub>2026-11-18 · 3d ago</sub>

> Agent Skills 0.6.17 adds an accessibility-engineering skill for auditing and fixing WCAG 2.2 AA issues, fixes a rollback workflow that could never log in, and lets you regrade eval runs without paying for them again.
> **New skill**
> - **accessibility-engineering** (#261, @Chukwuebuka-2003, reviewed by @nucliweb). Audits an existing interface with pinned axe-core and pa11y, triages the findings, and walks through the manual keyboard and screen reader checks the tools can't do. It ships an `accessibility-auditor` persona, an `/a11y` command, and an audit script that fails a partial run instead of reporting zero violations. Building new UI stays with frontend-ui-engineering. The shared accessibility checklist now targets WCAG 2.2 AA and matches the skill.
> **Fixes**
> - **Rollback can log in** (#799, @divya0795). The ci-cd-and-automation rollback workflow ran `vercel rollback` on a runner with no Vercel login, so it failed exactly when needed. It now passes the token, like the preview step already did.
> - **Review evidence from the right tree** (#795, @TanmayShah29, reported by @Scroller251-cloud in #788). code-review-and-quality checks that the checkout is clean and on the reviewed ref before running tests or probes, since a working copy can hold another session's edits.
> …

### [0.6.16](https://github.com/addyosmani/agent-skills/releases/tag/0.6.16) — Agent Skills 0.6.16
<sub>2026-11-14 · 8d ago</sub>

> Agent Skills 0.6.16 lets specs evolve past V1, teaches the docs skill to spot drift, stops the frontend skill from installing toolchains just to verify, and fixes two quality-gate examples that could never fail.
> **Skills**
> - **Spec evolution** (#383, @ayobamiseun). Specs now carry a version and an Out of Scope (Deferred) list, and a change to a shipped feature gets its own small delta spec (`SPEC-<change>.md`) instead of a rewrite. `/spec` writes one when `SPEC.md` already exists, and `/build auto` picks the delta that isn't `Status: implemented` and refuses to run a plan generated from a different spec.
> - **Documentation drift** (#514, @vyasdx). When a doc may be stale, documentation-and-adrs compares the last commit to the code with the last commit to the doc, and says "can't tell" instead of "current" when the history is unordered. Change logs are appended to, never rewritten.
> - **Verify with what the project has** (#732, @TwelveNights). frontend-ui-engineering no longer installs a test runner or type checker just to check its work, and follows the WAI-ARIA APG patterns for menus, dialogs, tabs, listboxes and comboboxes. Measured +0.10 across 11 models, with package installs down from 24% to 4% of runs.
> - **Review findings checked against the code** (#736, @CybotTM). code-review-and-quality checks each finding against the callers, guards and tests that reach the change, labels defects already in the base separately, and treats zero findings as a valid result.
> …

### [0.6.15](https://github.com/addyosmani/agent-skills/releases/tag/0.6.15) — Agent Skills 0.6.15
<sub>2026-10-31 · 22d ago</sub>

> Agent Skills 0.6.15 stops the security skill's staged-secret check from printing the secret it finds, fixes two simplify-ignore bugs that could corrupt protected code, and makes the constraints skill's security and accessibility gates actually fail CI.
> **Security**
> - **The staged-secret check no longer echoes credentials** (#718, @santhiprakash, reported by @xmxxc in #717). The old `git diff --cached | grep` printed every matching line, so a staged key landed in the terminal and in any agent's transcript. It also read as clean when git failed. The check is now `git diff --cached -i -G'…' --name-only`: it prints only file names, and a git failure exits non-zero by itself. Fixed in all three places it was documented.
> **Hooks**
> - **simplify-ignore restores re-indented placeholders cleanly** (#766, @Quinnod345, #765). If `/code-simplify` un-indented a placeholder or edited its reason, Stop wrote back a broken comment around the block, a syntax error in any `/* */` language. Blocks marked with `-- simplify-ignore-start` (SQL, Lua, Haskell) no longer warn that they were deleted, and a missing lock directory no longer stops Stop before every file is restored.
> **Skills**
> …

### [0.6.14](https://github.com/addyosmani/agent-skills/releases/tag/0.6.14) — Agent Skills 0.6.14
<sub>2026-10-29 · 24d ago</sub>

> Agent Skills 0.6.14 is mostly about code samples. More than twenty snippets across the skills either failed as written or taught the wrong thing, and they're fixed. It also closes two supply-chain and injection risks in the samples, stops Claude Code from starting `/ship` or `/build` on its own, and brings the root manifest in line with Agent Plugins 1.0.0.
> **Security fixes in the samples**
> - **The Lighthouse CI example ran the unscoped `lhci` package** (#721), which isn't Lighthouse CI. It now invokes `@lhci/cli`.
> - **The rollback workflow passed its input straight into `run:`** (#691), a script injection in any repo that copied it. It goes through `env` now.
> - The constraints skill scans the working tree for secrets, not only commits (#729), and the hardening reference returns 404 before an ownership check reads a missing task (#726).
> **Samples that now work as written**
> …

### [0.6.13](https://github.com/addyosmani/agent-skills/releases/tag/0.6.13) — Agent Skills 0.6.13
<sub>2026-10-13 · 1mo ago</sub>

> Agent Skills 0.6.13 fixes code samples in three skills that failed as written, two simplify-ignore bugs that could lose protected code or bring back a reverted change, and gets test-driven-development to fire when the code is already in the prompt. It also sets a written bar for which hosts the README lists.
> **Skill fixes**
> - **Three samples that did not work as written** (@rudycelekli). The error boundary in shipping-and-launch threw on every render and could never show its fallback (#637). The error state in frontend-ui-engineering called a `refetch` that was never defined (#638). The zod title check in the hardening reference accepted a title made only of spaces (#639).
> - **test-driven-development fires on pasted code** (#678, @federicobartoli). "Add unit tests for this function" and a pasted bug with no mention of tests went from 0 of 6 to 6 of 6 runs with one added clause, with no false fires across 24 adjacent prompts. Measured with the model pinned, as proposed in #620.
> - **documentation-and-adrs gains a prose review step** (#661, @manavmishra): mark the details that must survive an edit, and never replace an unsupported claim with an invented example or a stronger guarantee.
> - **`/review` and `/test` are documented as what they are** (#682, reported by @sundeer in #681). They run their skill in the main session; they do not spawn the `code-reviewer` or `test-engineer` personas, whatever the docs said. The review commands now ask for the same severity labels the skill uses (Critical, Required, Optional, Nit).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-18 | [chore(release): bump plugin manifests to 0.6.17](https://github.com/addyosmani/agent-skills/commit/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee) | r2 |
| 2026-11-18 | [Merge #261: add accessibility-engineering skill](https://github.com/addyosmani/agent-skills/commit/222bf920f0d3ac8ce9badf51cd7c60709050c1e0) | addyosmani |
| 2026-11-18 | [Merge #667: record behavioral runs for historical regrading](https://github.com/addyosmani/agent-skills/commit/18336b6e6c24ebed8e26e4959c4cccab8b69042f) | addyosmani |
| 2026-11-18 | [Merge #795: check the checkout is clean and on the reviewed ref](https://github.com/addyosmani/agent-skills/commit/45a9831738039b4cf7da3584aa71be150e089dda) | addyosmani |
| 2026-11-18 | [Merge #797: save capability map and module specs under spec/](https://github.com/addyosmani/agent-skills/commit/d7fd10362675f8829b78e5e031fd57e6e9e9cae7) | addyosmani |
| 2026-11-18 | [Merge #798: make the Gemini subagent example loadable](https://github.com/addyosmani/agent-skills/commit/49d7b464f38c585449f12414008b40904986976f) | addyosmani |
| 2026-11-18 | [Merge #799: give the rollback workflow a Vercel token](https://github.com/addyosmani/agent-skills/commit/9a69de588142a63c726b347d31a918d415a91fce) | addyosmani |
| 2026-11-16 | [fix(a11y): match main's command frontmatter and pack-level persona path](https://github.com/addyosmani/agent-skills/commit/f9e7e19210afb70c621489a9fc80651ce6d7fc8c) | Chukwuebuka-2003 |
| 2026-11-16 | [fix(review): address maintainer accessibility feedback](https://github.com/addyosmani/agent-skills/commit/3b79b0ce438e944fab594b143f20f64b6093562d) | Chukwuebuka-2003 |
| 2026-11-16 | [fix(review): address the second-round review on #261](https://github.com/addyosmani/agent-skills/commit/0094fdbd5ebb15ec9243a94e43e7224edbae52de) | Chukwuebuka-2003 |

[See all commits ↗](https://github.com/addyosmani/agent-skills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/addyosmani/agent-skills.git
```
