# garrytan/gstack

[← Back to the radar](../README.md) · [Open on GitHub ↗](https://github.com/garrytan/gstack)

> Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

## 📝 Notes

| | |
|---|---|
| **Status** | study |
| **Category** | 🪄 Agent skills & guidance |
| **Project** | — |
| **Why it's worth a look** | Garry Tan's Claude Code setup: 23 opinionated role tools |
| **Added** | 2026-11-15 |

🆕 **Active this week**

## 📊 At a glance

| | |
|---|---|
| ⭐ **Stars** | 142.3k |
| 🍴 **Forks** | 21.0k |
| 🐞 **Open issues + PRs** | [49](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-22 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — 2026-11-21 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 271.3 MB |

## 📦 Recent releases

### [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — gstack v1.102.2.0
<sub>2026-11-21 · today</sub>

> gstack 1.102.2.0 fixes two things that broke skills on Codex, stops /plan-tune sending your typed answers to the model without a record, lets large repositories use /ship, makes /office-hours start from ground truth, and moves skill routing out of your CLAUDE.md into the hook that now does that job.
> **Codex**
> - Skills no longer stop on Codex 0.170 when they clean up temporary files: gstack's Codex skills stopped using the `rm -f` form that Codex refuses (67 refusals before, 0 after). (#4612)
> - /review on Codex with OpenAI models no longer fails a review that really ran its security pass. Codex encrypts the message sent to that reviewer, so gstack now recognises the pass from the reviewer it started instead of from the message text. (#4622)
> **Privacy and telemetry**
> - /plan-tune's answer summariser now writes the off-machine send record the README promises before it sends your typed answers to the model, and sends nothing if that record can't be written. A new test fails on any model call that writes no record. Thanks to @robbiesierra for the report. (#4621)
> …

### [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — gstack v1.102.1.0
<sub>2026-11-20 · yesterday</sub>

> gstack 1.102.1.0 closes a gap where a secret written after a slash could be printed unhidden, locks down gstack's usage reporting and makes it more useful for people who opt in, fixes a set of bugs in how gstack picks the right skill for a prompt, and makes a gstack skill's start step run as Claude Code loads the skill, so it can't be skipped.
> **Usage reporting (telemetry, opt-in)**
> - The usage-reporting backend now accepts data only through its own checked endpoint: the public key in the repo can no longer read or write the tables, and a signed-in Supabase user is denied everything. gstack's own test runs never send usage data, test traffic is left out of `gstack-community-dashboard`, and its weekly active count now counts real installs instead of update checks. gstack versions older than v0.11.16.0 (March 2026) stop sending usage data, because they wrote straight to the tables. (#4537)
> - If you opt in, each skill run now also sends nine new fields, each a pick from a fixed list: which coding agent ran it, the model family, whether you, the model or another skill started it, why it ended, whether its own checks passed, whether gstack's routing section and hooks are set up, a random session id, and for upgrades the version you came from and why an upgrade failed. Runs from CI and gstack's own evals label themselves, and a duration gstack couldn't measure is sent empty instead of 0. The opt-in question lists the new fields, and anonymous mode now says it sends "no device ID; a random id per agent session that is never reused". No field carries code, file paths, prompts or repo names; every field is listed in docs/privacy.md. (#4542)
> **Skills and skill suggestions**
> - In Claude Code, each gstack skill's start step now runs while the skill loads, so the model can no longer skip it (in test runs, models had followed a loaded skill's start step in only 45% to 62% of sessions). If loading fails, the skill says so in one line and the model runs the start step itself, as before. Codex and other agents keep the old instructions. (#4509) gstack's paid test that checks this start step now counts one that ran during loading. (#4543)
> …

### [v1.102.0.0](https://github.com/garrytan/gstack/releases/tag/v1.102.0.0) — gstack v1.102.0.0
<sub>2026-11-19 · 2d ago</sub>

> gstack 1.102.0.0 makes Codex a first-class host: it now gets gstack's skill suggestions, the destructive-command check and /review's checklist hold. The destructive-command check was rebuilt to ask far less often while catching far more real damage.
> **Destructive-command check (/careful)**
> - It no longer asks about deleting scratch files (`/tmp`, `mktemp` folders, caches, build output), and it now asks before deletes outside your project, throwing away uncommitted work, history rewrites, remote branch deletes, database resets and cloud deletes. A recursive delete of `/` or your home folder, a force-push to the default branch, and wiping a whole disk are blocked however they're written. On a replay of 254,322 real agent commands, harmless asks fell from 1.40% of commands to 0.33%, and destructive commands caught rose from 443 to 930 of 948. (#4513)
> - It reads commands more carefully: `git push --repo=origin +main`, force-pushes after a `cd` or with `--all`/`--mirror`, quiet `git clean -q`, `find -L … -delete`, and `wipefs -a` in every spelling are caught; `git push -nf` dry runs and greps for SQL text no longer ask. On the same replay this catches no fewer destructive commands, and it adds 141 harmless asks (0.39% of commands in total); a follow-up is working on those. (#4525)
> - Agent SDK programs get a warning instead of an ask, because the SDK refuses an ask nobody answers. Set `GSTACK_SESSION_KIND=interactive` to keep the ask. (#4513)
> **Codex**
> …

### [v1.101.0.0](https://github.com/garrytan/gstack/releases/tag/v1.101.0.0) — gstack v1.101.0.0
<sub>2026-11-18 · 3d ago</sub>

> **gstack v1.101.0.0**
> **What's new**
> - Before you're asked to try an app build, the new `gstack-first-use` command has an agent from another model family play that build on the same kind of device and check the first five things you'll do with it. ([#4465](https://github.com/garrytan/gstack/pull/4465))
> - Before an agent asks its owner a question, `gstack-owner-answers` can check the draft against the owner's earlier answers and suggest dropping only the lines an existing standing yes already covers. ([#4467](https://github.com/garrytan/gstack/pull/4467))
> - GitHub release notes now list every change in plain words, with a link to its pull request. ([#4390](https://github.com/garrytan/gstack/pull/4390))
> - When another agent drives /ship step by step, each phase now runs as one command, the calls are counted, and the run stops itself after 100 minutes. ([#4451](https://github.com/garrytan/gstack/pull/4451))
> …

### [v1.100.0.0](https://github.com/garrytan/gstack/releases/tag/v1.100.0.0) — gstack v1.100.0.0
<sub>2026-11-17 · 4d ago</sub>

> **gstack v1.100.0.0**
> This release fixes five security advisories in a dependency, makes gstack's shell locks safe on Ubuntu 26.04, and changes how /ship writes and reviews pull requests. One optional hook check is removed.
> **Fixes**
> - Security: hono is pinned to 4.13.16, which fixes five advisories (GHSA-3gg2-335m-rxc6, GHSA-46wx-v44x-9hh2, GHSA-4h7h-rv7c-7m2v, GHSA-4m76-xfj5-7975, GHSA-h7mg-cq63-vhpq) found in 4.13.13. hono reaches gstack only through its development and test tools, and gstack's own code never uses it, so none of the five was reachable; contributors get the fix on their next `bun install`. (#4408)
> - gstack's shell locks admit exactly one holder again on Ubuntu 26.04 and GitHub's current `ubuntu-latest`, whose Rust `mkdir` reports success even when another process created the directory first. Before this, two updates could move one checkout at once, or two `gstack-config set` calls could drop each other's keys. (#4262)
> - /ship's documentation check no longer wastes one of its two attempts when the checking model writes text after its result line; it is asked once, for free, to resend the result alone. (#4285)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-22 | [Review exclusions stay in place when the repo's own policy test pins …](https://github.com/garrytan/gstack/commit/44e244d603036a46833ce14e9fd319276ee73e33) | garrytan |
| 2026-11-22 | [Free test shards stop failing when a test's browser exits during the …](https://github.com/garrytan/gstack/commit/3c9cda0a2d678777d6487c545b9cbb8e26618485) | garrytan |
| 2026-11-22 | [A fix closes its review finding only after a finished full review, an…](https://github.com/garrytan/gstack/commit/63900b308cd57a9fae29141b64c1dd9b00752579) | garrytan |
| 2026-11-22 | [Prompt router stops sending feature requests to your bug-fix skill (#…](https://github.com/garrytan/gstack/commit/596ff8a7cc913d405e7682ac99106cdfa7aab7e9) | garrytan |
| 2026-11-22 | [Review and ship tools: read Codex numbered severities, check Remote C…](https://github.com/garrytan/gstack/commit/b3323f47b8cb6ec074bc755d3b108983a816007a) | garrytan |
| 2026-11-22 | [Test selection finds tests for NodeNext .js imports and Rails specs (…](https://github.com/garrytan/gstack/commit/4bd15f8a3d7e159f61e8fe2d465cb20f4b0629c6) | garrytan |
| 2026-11-22 | [A skipped CI run no longer blocks reusing a passing run on the same c…](https://github.com/garrytan/gstack/commit/7530280407b9a466fc4a546f026f1cc3eff8211a) | garrytan |
| 2026-11-22 | [/ship can finish after a docs audit stopped before saving its snapsho…](https://github.com/garrytan/gstack/commit/25bf93c4e29d80f520e415c65b0ae778867c9ded) | garrytan |
| 2026-11-22 | [Local checks reuse every green CI run at your code, not only the firs…](https://github.com/garrytan/gstack/commit/3d3ce73eb9eb6d1d1f472e0e81f419d8fd9bdc73) | garrytan |
| 2026-11-22 | [Fix eight problems users reported in skill instructions (#4686)](https://github.com/garrytan/gstack/commit/113deeaf9c99847c719cc9d1dd826ea2ef7ce4e5) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
