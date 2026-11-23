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
| 🐞 **Open issues + PRs** | [52](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-23 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — 2026-11-23 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 274.5 MB |

## 📦 Recent releases

### [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — gstack v1.103.0.0
<sub>2026-11-23 · today</sub>

> **gstack v1.103.0.0**
> This release closes gaps in two of gstack's safety checks and its merge tool, fixes the /ship failures that were stopping pull requests from finishing, and renames `/verify` to `/build-check` so Claude Code's own `/verify` works again. Upgrade with `/gstack-upgrade`.
> **Action needed: `/verify` is now `/build-check`**
> - `/verify` is now `/build-check`, so typing `/verify` opens Claude Code's built-in `/verify` again. Use `/build-check` for gstack's build-and-check loop and `/build-check quick` for the check-only pass. (#4714)
> - If you turned the skill off with `disabled_skills: verify`, change that entry to `build-check`. Until you do, gstack reads `verify` as `build-check`, so the skill stays off after you upgrade. (#4719)
> - gstack no longer runs the check pass before every commit on its own, so the `verify_before_commit` setting is retired. Setting it prints a note and changes nothing, and a config file that still has it keeps working. (#4714)
> …

### [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — gstack v1.102.2.0
<sub>2026-11-21 · yesterday</sub>

> gstack 1.102.2.0 fixes two things that broke skills on Codex, stops /plan-tune sending your typed answers to the model without a record, lets large repositories use /ship, makes /office-hours start from ground truth, and moves skill routing out of your CLAUDE.md into the hook that now does that job.
> **Codex**
> - Skills no longer stop on Codex 0.170 when they clean up temporary files: gstack's Codex skills stopped using the `rm -f` form that Codex refuses (67 refusals before, 0 after). (#4612)
> - /review on Codex with OpenAI models no longer fails a review that really ran its security pass. Codex encrypts the message sent to that reviewer, so gstack now recognises the pass from the reviewer it started instead of from the message text. (#4622)
> **Privacy and telemetry**
> - /plan-tune's answer summariser now writes the off-machine send record the README promises before it sends your typed answers to the model, and sends nothing if that record can't be written. A new test fails on any model call that writes no record. Thanks to @robbiesierra for the report. (#4621)
> …

### [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — gstack v1.102.1.0
<sub>2026-11-20 · 2d ago</sub>

> gstack 1.102.1.0 closes a gap where a secret written after a slash could be printed unhidden, locks down gstack's usage reporting and makes it more useful for people who opt in, fixes a set of bugs in how gstack picks the right skill for a prompt, and makes a gstack skill's start step run as Claude Code loads the skill, so it can't be skipped.
> **Usage reporting (telemetry, opt-in)**
> - The usage-reporting backend now accepts data only through its own checked endpoint: the public key in the repo can no longer read or write the tables, and a signed-in Supabase user is denied everything. gstack's own test runs never send usage data, test traffic is left out of `gstack-community-dashboard`, and its weekly active count now counts real installs instead of update checks. gstack versions older than v0.11.16.0 (March 2026) stop sending usage data, because they wrote straight to the tables. (#4537)
> - If you opt in, each skill run now also sends nine new fields, each a pick from a fixed list: which coding agent ran it, the model family, whether you, the model or another skill started it, why it ended, whether its own checks passed, whether gstack's routing section and hooks are set up, a random session id, and for upgrades the version you came from and why an upgrade failed. Runs from CI and gstack's own evals label themselves, and a duration gstack couldn't measure is sent empty instead of 0. The opt-in question lists the new fields, and anonymous mode now says it sends "no device ID; a random id per agent session that is never reused". No field carries code, file paths, prompts or repo names; every field is listed in docs/privacy.md. (#4542)
> **Skills and skill suggestions**
> - In Claude Code, each gstack skill's start step now runs while the skill loads, so the model can no longer skip it (in test runs, models had followed a loaded skill's start step in only 45% to 62% of sessions). If loading fails, the skill says so in one line and the model runs the start step itself, as before. Codex and other agents keep the old instructions. (#4509) gstack's paid test that checks this start step now counts one that ran during loading. (#4543)
> …

### [v1.102.0.0](https://github.com/garrytan/gstack/releases/tag/v1.102.0.0) — gstack v1.102.0.0
<sub>2026-11-19 · 3d ago</sub>

> gstack 1.102.0.0 makes Codex a first-class host: it now gets gstack's skill suggestions, the destructive-command check and /review's checklist hold. The destructive-command check was rebuilt to ask far less often while catching far more real damage.
> **Destructive-command check (/careful)**
> - It no longer asks about deleting scratch files (`/tmp`, `mktemp` folders, caches, build output), and it now asks before deletes outside your project, throwing away uncommitted work, history rewrites, remote branch deletes, database resets and cloud deletes. A recursive delete of `/` or your home folder, a force-push to the default branch, and wiping a whole disk are blocked however they're written. On a replay of 254,322 real agent commands, harmless asks fell from 1.40% of commands to 0.33%, and destructive commands caught rose from 443 to 930 of 948. (#4513)
> - It reads commands more carefully: `git push --repo=origin +main`, force-pushes after a `cd` or with `--all`/`--mirror`, quiet `git clean -q`, `find -L … -delete`, and `wipefs -a` in every spelling are caught; `git push -nf` dry runs and greps for SQL text no longer ask. On the same replay this catches no fewer destructive commands, and it adds 141 harmless asks (0.39% of commands in total); a follow-up is working on those. (#4525)
> - Agent SDK programs get a warning instead of an ask, because the SDK refuses an ask nobody answers. Set `GSTACK_SESSION_KIND=interactive` to keep the ask. (#4513)
> **Codex**
> …

### [v1.101.0.0](https://github.com/garrytan/gstack/releases/tag/v1.101.0.0) — gstack v1.101.0.0
<sub>2026-11-18 · 4d ago</sub>

> **gstack v1.101.0.0**
> **What's new**
> - Before you're asked to try an app build, the new `gstack-first-use` command has an agent from another model family play that build on the same kind of device and check the first five things you'll do with it. ([#4465](https://github.com/garrytan/gstack/pull/4465))
> - Before an agent asks its owner a question, `gstack-owner-answers` can check the draft against the owner's earlier answers and suggest dropping only the lines an existing standing yes already covers. ([#4467](https://github.com/garrytan/gstack/pull/4467))
> - GitHub release notes now list every change in plain words, with a link to its pull request. ([#4390](https://github.com/garrytan/gstack/pull/4390))
> - When another agent drives /ship step by step, each phase now runs as one command, the calls are counted, and the run stops itself after 100 minutes. ([#4451](https://github.com/garrytan/gstack/pull/4451))
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-23 | [gstack-upgrade works again after you disable skills (#4704) (#4743)](https://github.com/garrytan/gstack/commit/c4cfe6d1c94e2fd6fe2afd735dd1a5cc914cfe0c) | garrytan |
| 2026-11-23 | [/cso searches the whole repository in one call with a hard time limit…](https://github.com/garrytan/gstack/commit/a3ecfd530df3c78c2d60e92b6488586a75e0ff91) | garrytan |
| 2026-11-23 | [Add a test that stops /ship from gaining refusals without a stated re…](https://github.com/garrytan/gstack/commit/45b48f17d9282442bc1321bc2ba9ffbf037195f3) | garrytan |
| 2026-11-23 | [/cso reports every security finding the code supports instead of drop…](https://github.com/garrytan/gstack/commit/af6deb996eca01f21c6747697af911d95c132de0) | garrytan |
| 2026-11-23 | [Write up a failed or shelved attempt before closing it (GST-3576) (#4…](https://github.com/garrytan/gstack/commit/8143a91809b2305da6ffa7486923008b72d337e6) | garrytan |
| 2026-11-23 | [v1.103.0.0 Release v1.103.0.0: /verify becomes /build-check, plus sec…](https://github.com/garrytan/gstack/commit/71c5e34d706831154dae2fb144a7c50e0e46beda) | garrytan |
| 2026-11-23 | [A green CI run now counts for your branch when only main moved under …](https://github.com/garrytan/gstack/commit/261f380002d19f67bca028dd48364729803c8bc5) | garrytan |
| 2026-11-23 | [Publish the test of /ship's review panel against two plain reads (GST…](https://github.com/garrytan/gstack/commit/8751b382dd5d3953c26e4e9e3f1532ec053031b0) | garrytan |
| 2026-11-23 | [Release check's docs-audit tests accept /ship's step for a stopped do…](https://github.com/garrytan/gstack/commit/50204fd64f80ab4bd3b4095704dc908e989ceda2) | garrytan |
| 2026-11-23 | [/plan-ceo-review explains its mode recommendation by what that mode d…](https://github.com/garrytan/gstack/commit/0408128f2fa5a11ffb5862e1fa05802a3708754c) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
