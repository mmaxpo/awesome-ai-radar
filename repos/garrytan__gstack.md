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
| ⭐ **Stars** | 142.5k |
| 🍴 **Forks** | 21.0k |
| 🐞 **Open issues + PRs** | [55](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-24 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.103.1.0](https://github.com/garrytan/gstack/releases/tag/v1.103.1.0) — 2026-11-24 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 275.4 MB |

## 📦 Recent releases

### [v1.103.1.0](https://github.com/garrytan/gstack/releases/tag/v1.103.1.0) — gstack v1.103.1.0
<sub>2026-11-24 · today</sub>

> **gstack v1.103.1.0**
> **What's new**
> - `/ship` now tells you what to change when GitHub refuses a push for email privacy. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - `gstack-approvals rule` and `round-grant` now say which `--owner-ref` check failed. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - The merge queue's bisect now accepts a red judge case whose name holds a space. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - /cso reports every security finding the code supports instead of dropping most of them. ([#4739](https://github.com/garrytan/gstack/pull/4739))
> …

### [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — gstack v1.103.0.0
<sub>2026-11-23 · yesterday</sub>

> **gstack v1.103.0.0**
> This release closes gaps in two of gstack's safety checks and its merge tool, fixes the /ship failures that were stopping pull requests from finishing, and renames `/verify` to `/build-check` so Claude Code's own `/verify` works again. Upgrade with `/gstack-upgrade`.
> **Action needed: `/verify` is now `/build-check`**
> - `/verify` is now `/build-check`, so typing `/verify` opens Claude Code's built-in `/verify` again. Use `/build-check` for gstack's build-and-check loop and `/build-check quick` for the check-only pass. (#4714)
> - If you turned the skill off with `disabled_skills: verify`, change that entry to `build-check`. Until you do, gstack reads `verify` as `build-check`, so the skill stays off after you upgrade. (#4719)
> - gstack no longer runs the check pass before every commit on its own, so the `verify_before_commit` setting is retired. Setting it prints a note and changes nothing, and a config file that still has it keeps working. (#4714)
> …

### [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — gstack v1.102.2.0
<sub>2026-11-21 · 2d ago</sub>

> gstack 1.102.2.0 fixes two things that broke skills on Codex, stops /plan-tune sending your typed answers to the model without a record, lets large repositories use /ship, makes /office-hours start from ground truth, and moves skill routing out of your CLAUDE.md into the hook that now does that job.
> **Codex**
> - Skills no longer stop on Codex 0.170 when they clean up temporary files: gstack's Codex skills stopped using the `rm -f` form that Codex refuses (67 refusals before, 0 after). (#4612)
> - /review on Codex with OpenAI models no longer fails a review that really ran its security pass. Codex encrypts the message sent to that reviewer, so gstack now recognises the pass from the reviewer it started instead of from the message text. (#4622)
> **Privacy and telemetry**
> - /plan-tune's answer summariser now writes the off-machine send record the README promises before it sends your typed answers to the model, and sends nothing if that record can't be written. A new test fails on any model call that writes no record. Thanks to @robbiesierra for the report. (#4621)
> …

### [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — gstack v1.102.1.0
<sub>2026-11-20 · 3d ago</sub>

> gstack 1.102.1.0 closes a gap where a secret written after a slash could be printed unhidden, locks down gstack's usage reporting and makes it more useful for people who opt in, fixes a set of bugs in how gstack picks the right skill for a prompt, and makes a gstack skill's start step run as Claude Code loads the skill, so it can't be skipped.
> **Usage reporting (telemetry, opt-in)**
> - The usage-reporting backend now accepts data only through its own checked endpoint: the public key in the repo can no longer read or write the tables, and a signed-in Supabase user is denied everything. gstack's own test runs never send usage data, test traffic is left out of `gstack-community-dashboard`, and its weekly active count now counts real installs instead of update checks. gstack versions older than v0.11.16.0 (March 2026) stop sending usage data, because they wrote straight to the tables. (#4537)
> - If you opt in, each skill run now also sends nine new fields, each a pick from a fixed list: which coding agent ran it, the model family, whether you, the model or another skill started it, why it ended, whether its own checks passed, whether gstack's routing section and hooks are set up, a random session id, and for upgrades the version you came from and why an upgrade failed. Runs from CI and gstack's own evals label themselves, and a duration gstack couldn't measure is sent empty instead of 0. The opt-in question lists the new fields, and anonymous mode now says it sends "no device ID; a random id per agent session that is never reused". No field carries code, file paths, prompts or repo names; every field is listed in docs/privacy.md. (#4542)
> **Skills and skill suggestions**
> - In Claude Code, each gstack skill's start step now runs while the skill loads, so the model can no longer skip it (in test runs, models had followed a loaded skill's start step in only 45% to 62% of sessions). If loading fails, the skill says so in one line and the model runs the start step itself, as before. Codex and other agents keep the old instructions. (#4509) gstack's paid test that checks this start step now counts one that ran during loading. (#4543)
> …

### [v1.102.0.0](https://github.com/garrytan/gstack/releases/tag/v1.102.0.0) — gstack v1.102.0.0
<sub>2026-11-19 · 4d ago</sub>

> gstack 1.102.0.0 makes Codex a first-class host: it now gets gstack's skill suggestions, the destructive-command check and /review's checklist hold. The destructive-command check was rebuilt to ask far less often while catching far more real damage.
> **Destructive-command check (/careful)**
> - It no longer asks about deleting scratch files (`/tmp`, `mktemp` folders, caches, build output), and it now asks before deletes outside your project, throwing away uncommitted work, history rewrites, remote branch deletes, database resets and cloud deletes. A recursive delete of `/` or your home folder, a force-push to the default branch, and wiping a whole disk are blocked however they're written. On a replay of 254,322 real agent commands, harmless asks fell from 1.40% of commands to 0.33%, and destructive commands caught rose from 443 to 930 of 948. (#4513)
> - It reads commands more carefully: `git push --repo=origin +main`, force-pushes after a `cd` or with `--all`/`--mirror`, quiet `git clean -q`, `find -L … -delete`, and `wipefs -a` in every spelling are caught; `git push -nf` dry runs and greps for SQL text no longer ask. On the same replay this catches no fewer destructive commands, and it adds 141 harmless asks (0.39% of commands in total); a follow-up is working on those. (#4525)
> - Agent SDK programs get a warning instead of an ask, because the SDK refuses an ask nobody answers. Set `GSTACK_SESSION_KIND=interactive` to keep the ask. (#4513)
> **Codex**
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-24 | [v1.103.2.0 release (#4785)](https://github.com/garrytan/gstack/commit/d74ee528b6df9ddb945be2103a24544babe76e65) | garrytan |
| 2026-11-24 | [make-pdf: a NUL character can no longer hide script from the sanitize…](https://github.com/garrytan/gstack/commit/f7402213a04d720eed5c50557c0ba528a69af4bd) | garrytan |
| 2026-11-24 | [After a fix, the second review round is always a full review (#4783)](https://github.com/garrytan/gstack/commit/7deee4292c3d96d97640960c95ef3857ae1d47e1) | garrytan |
| 2026-11-24 | [Weekly benchmark records can't slip text into the release log or lose…](https://github.com/garrytan/gstack/commit/c34b967346f1e0514c2f1eed3836e91a62ac08e3) | garrytan |
| 2026-11-24 | [A small second review round checks the fix again (#4781)](https://github.com/garrytan/gstack/commit/c2e61872197ea2e4968b990dd7d485ccc4f46f76) | garrytan |
| 2026-11-24 | [Show the weekly benchmark in every stable release plan, ready to hold…](https://github.com/garrytan/gstack/commit/a9c746fa0c5cb19524bfc45bf75806b99fc1d2b5) | garrytan |
| 2026-11-24 | [/ship instructions match the new review rules (GST-3562) (#4779)](https://github.com/garrytan/gstack/commit/0603c2738980587466fc3fcc7182329f9945de7e) | garrytan |
| 2026-11-24 | [v1.103.1.0 release (#4780)](https://github.com/garrytan/gstack/commit/8b68498500a15c9aa149deda478fde0ffee98646) | garrytan |
| 2026-11-24 | [A first version's public copy catches a short owner quote whose paddi…](https://github.com/garrytan/gstack/commit/bb6d13ea30a7e2407157d473fc08f50ec5feb396) | garrytan |
| 2026-11-24 | [A first version's public copy keeps out a short owner quote padded wi…](https://github.com/garrytan/gstack/commit/f3a89d2105a8f18852e8b15a016ad7153e6c19dc) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
