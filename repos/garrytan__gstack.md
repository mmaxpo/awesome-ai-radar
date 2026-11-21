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
| 🐞 **Open issues + PRs** | [119](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-21 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — 2026-11-20 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 271.1 MB |

## 📦 Recent releases

### [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — gstack v1.102.1.0
<sub>2026-11-20 · today</sub>

> gstack 1.102.1.0 closes a gap where a secret written after a slash could be printed unhidden, locks down gstack's usage reporting and makes it more useful for people who opt in, fixes a set of bugs in how gstack picks the right skill for a prompt, and makes a gstack skill's start step run as Claude Code loads the skill, so it can't be skipped.
> **Usage reporting (telemetry, opt-in)**
> - The usage-reporting backend now accepts data only through its own checked endpoint: the public key in the repo can no longer read or write the tables, and a signed-in Supabase user is denied everything. gstack's own test runs never send usage data, test traffic is left out of `gstack-community-dashboard`, and its weekly active count now counts real installs instead of update checks. gstack versions older than v0.11.16.0 (March 2026) stop sending usage data, because they wrote straight to the tables. (#4537)
> - If you opt in, each skill run now also sends nine new fields, each a pick from a fixed list: which coding agent ran it, the model family, whether you, the model or another skill started it, why it ended, whether its own checks passed, whether gstack's routing section and hooks are set up, a random session id, and for upgrades the version you came from and why an upgrade failed. Runs from CI and gstack's own evals label themselves, and a duration gstack couldn't measure is sent empty instead of 0. The opt-in question lists the new fields, and anonymous mode now says it sends "no device ID; a random id per agent session that is never reused". No field carries code, file paths, prompts or repo names; every field is listed in docs/privacy.md. (#4542)
> **Skills and skill suggestions**
> - In Claude Code, each gstack skill's start step now runs while the skill loads, so the model can no longer skip it (in test runs, models had followed a loaded skill's start step in only 45% to 62% of sessions). If loading fails, the skill says so in one line and the model runs the start step itself, as before. Codex and other agents keep the old instructions. (#4509) gstack's paid test that checks this start step now counts one that ran during loading. (#4543)
> …

### [v1.102.0.0](https://github.com/garrytan/gstack/releases/tag/v1.102.0.0) — gstack v1.102.0.0
<sub>2026-11-19 · yesterday</sub>

> gstack 1.102.0.0 makes Codex a first-class host: it now gets gstack's skill suggestions, the destructive-command check and /review's checklist hold. The destructive-command check was rebuilt to ask far less often while catching far more real damage.
> **Destructive-command check (/careful)**
> - It no longer asks about deleting scratch files (`/tmp`, `mktemp` folders, caches, build output), and it now asks before deletes outside your project, throwing away uncommitted work, history rewrites, remote branch deletes, database resets and cloud deletes. A recursive delete of `/` or your home folder, a force-push to the default branch, and wiping a whole disk are blocked however they're written. On a replay of 254,322 real agent commands, harmless asks fell from 1.40% of commands to 0.33%, and destructive commands caught rose from 443 to 930 of 948. (#4513)
> - It reads commands more carefully: `git push --repo=origin +main`, force-pushes after a `cd` or with `--all`/`--mirror`, quiet `git clean -q`, `find -L … -delete`, and `wipefs -a` in every spelling are caught; `git push -nf` dry runs and greps for SQL text no longer ask. On the same replay this catches no fewer destructive commands, and it adds 141 harmless asks (0.39% of commands in total); a follow-up is working on those. (#4525)
> - Agent SDK programs get a warning instead of an ask, because the SDK refuses an ask nobody answers. Set `GSTACK_SESSION_KIND=interactive` to keep the ask. (#4513)
> **Codex**
> …

### [v1.101.0.0](https://github.com/garrytan/gstack/releases/tag/v1.101.0.0) — gstack v1.101.0.0
<sub>2026-11-18 · 2d ago</sub>

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

### [v1.99.5.0](https://github.com/garrytan/gstack/releases/tag/v1.99.5.0) — gstack v1.99.5.0
<sub>2026-11-16 · 5d ago</sub>

> **gstack v1.99.5.0**
> The standalone /plan-eng-review command is back, plus a clearer error from `gstack-redact` and a plain guide to how outside contributions land.
> **What's new**
> - `/plan-eng-review` is back as its own command on every host that had it, including Claude Code, Codex and OpenClaw, and requests like "review the architecture" route to it again. /autoplan works exactly as before [#4375](https://github.com/garrytan/gstack/pull/4375).
> **Fixes**
> - `gstack-redact` now says up front that input over 16 MiB is always refused: `--help` and both "too large" errors name the limit, say `--max-bytes` can't raise it, and suggest splitting the input. Reported by @exGeni and first fixed by @ElNeMeR70 [#4373](https://github.com/garrytan/gstack/pull/4373).
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-21 | [Codex skills no longer stop on temp-file cleanup, which Codex refuses…](https://github.com/garrytan/gstack/commit/bd77c8ccaa373e3a072ef3d9f4839edae16b46f0) | garrytan |
| 2026-11-21 | [The spawnSync overflow test no longer fails about once an hour on CI …](https://github.com/garrytan/gstack/commit/43c9c201e34b6d6a4b75418ec4d20e147557dd80) | garrytan |
| 2026-11-21 | [/office-hours checks for a real user first and ends startup sessions …](https://github.com/garrytan/gstack/commit/27e5db990208898cba69eba87c7fc6b43e51b224) | garrytan |
| 2026-11-21 | [Give the /ship conductor trial's judge one more attempt on fresh labe…](https://github.com/garrytan/gstack/commit/4363c51257325a52cf50158e6f4e371f5a1c8f01) | garrytan |
| 2026-11-21 | [Make /ship's preflight honor the repo's CI rerun time limit and name …](https://github.com/garrytan/gstack/commit/df4d0bd0b159f245a084d4dfbe2703838455a0b6) | garrytan |
| 2026-11-21 | [Tell /ship review readers never to kill processes they didn't start (…](https://github.com/garrytan/gstack/commit/cbe37f2c0a638d295627767f2c400c22328e5574) | garrytan |
| 2026-11-21 | [Make the /ship conductor trial stop only at the final remote-gate ref…](https://github.com/garrytan/gstack/commit/aea71f414e9130435c386bdf4fba1a55789344d3) | garrytan |
| 2026-11-21 | [/ship's review no longer stops when Capy's drive sync database grows …](https://github.com/garrytan/gstack/commit/cc0896560abbaeed0b1df4157900fd2f50f76d66) | garrytan |
| 2026-11-21 | [Let the /ship conductor trial end at the remote gate when a case's ba…](https://github.com/garrytan/gstack/commit/baef51fe0ec9b0f4e7103c874d94eb2c304d7100) | garrytan |
| 2026-11-21 | [Fix ready notes, landing decisions, release PR descriptions and squas…](https://github.com/garrytan/gstack/commit/7fe1900f8b9e4143f15dc9e6becafdcb6375680b) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
