# addyosmani/agent-skills

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents.

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 📁 Uncategorized |
| **Project** | — |
| **Why it's worth a look** | — |
| **Added** | 2026-11-14 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 117.3k |
| 🍴 **Forks** | 12.3k |
| 🐞 **Open issues + PRs** | [121](https://github.com/addyosmani/agent-skills/issues) |
| 💻 **Languages** | JavaScript 76% · Shell 22% · Python 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | `agent-skills` `antigravity` `claude-code` `cursor` `skills` `codex` |
| 🕒 **Last activity** | 2026-11-14 (today) |
| 📅 **Created** | 2026-02-15 |
| 📦 **Latest release** | [0.6.16](https://github.com/addyosmani/agent-skills/releases/tag/0.6.16) — 2026-11-14 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 1.9 MB |
| 🌐 **Website** | https://skills.addy.ie |

## 📦 Recent releases

### [0.6.16](https://github.com/addyosmani/agent-skills/releases/tag/0.6.16) — Agent Skills 0.6.16
<sub>2026-11-14 · today</sub>

> Agent Skills 0.6.16 lets specs evolve past V1, teaches the docs skill to spot drift, stops the frontend skill from installing toolchains just to verify, and fixes two quality-gate examples that could never fail.
> **Skills**
> - **Spec evolution** (#383, @ayobamiseun). Specs now carry a version and an Out of Scope (Deferred) list, and a change to a shipped feature gets its own small delta spec (`SPEC-<change>.md`) instead of a rewrite. `/spec` writes one when `SPEC.md` already exists, and `/build auto` picks the delta that isn't `Status: implemented` and refuses to run a plan generated from a different spec.
> - **Documentation drift** (#514, @vyasdx). When a doc may be stale, documentation-and-adrs compares the last commit to the code with the last commit to the doc, and says "can't tell" instead of "current" when the history is unordered. Change logs are appended to, never rewritten.
> - **Verify with what the project has** (#732, @TwelveNights). frontend-ui-engineering no longer installs a test runner or type checker just to check its work, and follows the WAI-ARIA APG patterns for menus, dialogs, tabs, listboxes and comboboxes. Measured +0.10 across 11 models, with package installs down from 24% to 4% of runs.
> - **Review findings checked against the code** (#736, @CybotTM). code-review-and-quality checks each finding against the callers, guards and tests that reach the change, labels defects already in the base separately, and treats zero findings as a valid result.
> …

### [0.6.15](https://github.com/addyosmani/agent-skills/releases/tag/0.6.15) — Agent Skills 0.6.15
<sub>2026-10-31 · 14d ago</sub>

> Agent Skills 0.6.15 stops the security skill's staged-secret check from printing the secret it finds, fixes two simplify-ignore bugs that could corrupt protected code, and makes the constraints skill's security and accessibility gates actually fail CI.
> **Security**
> - **The staged-secret check no longer echoes credentials** (#718, @santhiprakash, reported by @xmxxc in #717). The old `git diff --cached | grep` printed every matching line, so a staged key landed in the terminal and in any agent's transcript. It also read as clean when git failed. The check is now `git diff --cached -i -G'…' --name-only`: it prints only file names, and a git failure exits non-zero by itself. Fixed in all three places it was documented.
> **Hooks**
> - **simplify-ignore restores re-indented placeholders cleanly** (#766, @Quinnod345, #765). If `/code-simplify` un-indented a placeholder or edited its reason, Stop wrote back a broken comment around the block, a syntax error in any `/* */` language. Blocks marked with `-- simplify-ignore-start` (SQL, Lua, Haskell) no longer warn that they were deleted, and a missing lock directory no longer stops Stop before every file is restored.
> **Skills**
> …

### [0.6.14](https://github.com/addyosmani/agent-skills/releases/tag/0.6.14) — Agent Skills 0.6.14
<sub>2026-10-29 · 16d ago</sub>

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

### [0.6.12](https://github.com/addyosmani/agent-skills/releases/tag/0.6.12) — Agent Skills 0.6.12
<sub>2026-10-03 · 1mo ago</sub>

> Agent Skills 0.6.12 is mostly about skills saying the right thing. It fixes a spec workflow that ran past its own approval gate, removes a command that does not exist and a code sample that does not parse, and slims performance-optimization the same way 0.6.11 slimmed security-and-hardening.
> **Skill fixes**
> - **spec-driven-development stops after the spec** (#629, @nucliweb, fixes #622). On hosts that load only the skill, some models ran Specify, Plan, Tasks and Implement in one turn, because the explicit "confirm before proceeding" step lived only in the `/spec` command. The skill now ends the turn after saving the spec and waits for approval, the same fix #497 made for interview-me.
> - **No more invented rollback command** (#628, @jsynowiec). The shipping-and-launch checklist told you to run `npx prisma migrate rollback`, which Prisma does not have. It now asks for your project's verified rollback command or runbook, whatever migration tool you use.
> - **The idempotency example parses** (#627, @jsynowiec). A bare `throw;` in api-and-interface-design is a syntax error in JavaScript; it now rethrows the caught error.
> - **performance-optimization is slimmer** (#580, @Syamsuddin, with fixes from @nucliweb's review). Step 3's code patterns moved into a skill-local `references/optimization-patterns.md`, taking SKILL.md from 496 to 267 lines. The condensed summary keeps the guidance that matters without opening the reference: when an index will not help and what to do instead (partial, trigram or expression indexes), that a bad `rows=` estimate means `ANALYZE` rather than a new index, and stating a cache's staleness window.
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-14 | [chore(release): bump plugin manifests to 0.6.16](https://github.com/addyosmani/agent-skills/commit/39b723ceebf81474d0557c1fecd01eddab585563) | r2 |
| 2026-11-14 | [Merge #757: fire debugging on pasted diffs and stack traces](https://github.com/addyosmani/agent-skills/commit/8322e1ce0451481ac9f10cdaf33c2235533ee459) | addyosmani |
| 2026-11-14 | [Merge remote-tracking branch 'origin/main' into pr757](https://github.com/addyosmani/agent-skills/commit/3de865b744d0584c319cc1d6edc73efbc4ccff79) | addyosmani |
| 2026-11-14 | [Merge #763: say the review may look quick from reading the diff](https://github.com/addyosmani/agent-skills/commit/dee5781ef80d5b84cf724f858d2cc20f61e7cfc8) | addyosmani |
| 2026-11-14 | [Merge remote-tracking branch 'origin/main' into pr757](https://github.com/addyosmani/agent-skills/commit/7d90e74db41af477a476ea5c1dc93779e3a2a157) | addyosmani |
| 2026-11-14 | [Merge remote-tracking branch 'origin/main' into pr763](https://github.com/addyosmani/agent-skills/commit/8110c7ad876b8c5f3e9b391efe44f8d50bbf04b3) | addyosmani |
| 2026-11-14 | [Merge #762: re-tune the TDD pasted-code clause for the current router](https://github.com/addyosmani/agent-skills/commit/970d8d3df49279e85ac34fc1ce67b881225717fd) | addyosmani |
| 2026-11-14 | [Merge #383: spec evolution guidance, V1 scoping and delta specs](https://github.com/addyosmani/agent-skills/commit/a8e88e1402ceacd9414d6b4be0f3b3b50f1d51f6) | addyosmani |
| 2026-11-14 | [Merge #744: stage skill resources outside the fixture baseline](https://github.com/addyosmani/agent-skills/commit/a8bb8d46da6a4cf3557b33f95c04344d3885c7f3) | addyosmani |
| 2026-11-14 | [Merge #778: run the hook suites on macOS stock bash](https://github.com/addyosmani/agent-skills/commit/e982f644895e91163ad8545225bb3a821b53784c) | addyosmani |

[See all commits ↗](https://github.com/addyosmani/agent-skills/commits)

## ⬇️ Get it

```bash
git clone https://github.com/addyosmani/agent-skills.git
```
