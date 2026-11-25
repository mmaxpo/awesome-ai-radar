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
| ⭐ **Stars** | 142.6k |
| 🍴 **Forks** | 21.0k |
| 🐞 **Open issues + PRs** | [52](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-25 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.103.3.0](https://github.com/garrytan/gstack/releases/tag/v1.103.3.0) — 2026-11-25 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 282.4 MB |

## 📦 Recent releases

### [v1.103.3.0](https://github.com/garrytan/gstack/releases/tag/v1.103.3.0) — gstack v1.103.3.0
<sub>2026-11-25 · today</sub>

> **gstack v1.103.3.0**
> **What's new**
> - A first version's ruled-out line now counts only against the one reply it cites. ([#4800](https://github.com/garrytan/gstack/pull/4800))
> - A first version's plan can say the owner ruled something out, and that line now counts only when he actually said it. ([#4789](https://github.com/garrytan/gstack/pull/4789))
> - /ship's instructions now match how it reviews code. ([#4779](https://github.com/garrytan/gstack/pull/4779))
> **Fixes**
> …

### [v1.103.1.0](https://github.com/garrytan/gstack/releases/tag/v1.103.1.0) — gstack v1.103.1.0
<sub>2026-11-24 · yesterday</sub>

> **gstack v1.103.1.0**
> **What's new**
> - `/ship` now tells you what to change when GitHub refuses a push for email privacy. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - `gstack-approvals rule` and `round-grant` now say which `--owner-ref` check failed. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - The merge queue's bisect now accepts a red judge case whose name holds a space. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - /cso reports every security finding the code supports instead of dropping most of them. ([#4739](https://github.com/garrytan/gstack/pull/4739))
> …

### [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — gstack v1.103.0.0
<sub>2026-11-23 · 2d ago</sub>

> **gstack v1.103.0.0**
> This release closes gaps in two of gstack's safety checks and its merge tool, fixes the /ship failures that were stopping pull requests from finishing, and renames `/verify` to `/build-check` so Claude Code's own `/verify` works again. Upgrade with `/gstack-upgrade`.
> **Action needed: `/verify` is now `/build-check`**
> - `/verify` is now `/build-check`, so typing `/verify` opens Claude Code's built-in `/verify` again. Use `/build-check` for gstack's build-and-check loop and `/build-check quick` for the check-only pass. (#4714)
> - If you turned the skill off with `disabled_skills: verify`, change that entry to `build-check`. Until you do, gstack reads `verify` as `build-check`, so the skill stays off after you upgrade. (#4719)
> - gstack no longer runs the check pass before every commit on its own, so the `verify_before_commit` setting is retired. Setting it prints a note and changes nothing, and a config file that still has it keeps working. (#4714)
> …

### [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — gstack v1.102.2.0
<sub>2026-11-21 · 3d ago</sub>

> gstack 1.102.2.0 fixes two things that broke skills on Codex, stops /plan-tune sending your typed answers to the model without a record, lets large repositories use /ship, makes /office-hours start from ground truth, and moves skill routing out of your CLAUDE.md into the hook that now does that job.
> **Codex**
> - Skills no longer stop on Codex 0.170 when they clean up temporary files: gstack's Codex skills stopped using the `rm -f` form that Codex refuses (67 refusals before, 0 after). (#4612)
> - /review on Codex with OpenAI models no longer fails a review that really ran its security pass. Codex encrypts the message sent to that reviewer, so gstack now recognises the pass from the reviewer it started instead of from the message text. (#4622)
> **Privacy and telemetry**
> - /plan-tune's answer summariser now writes the off-machine send record the README promises before it sends your typed answers to the model, and sends nothing if that record can't be written. A new test fails on any model call that writes no record. Thanks to @robbiesierra for the report. (#4621)
> …

### [v1.102.1.0](https://github.com/garrytan/gstack/releases/tag/v1.102.1.0) — gstack v1.102.1.0
<sub>2026-11-20 · 4d ago</sub>

> gstack 1.102.1.0 closes a gap where a secret written after a slash could be printed unhidden, locks down gstack's usage reporting and makes it more useful for people who opt in, fixes a set of bugs in how gstack picks the right skill for a prompt, and makes a gstack skill's start step run as Claude Code loads the skill, so it can't be skipped.
> **Usage reporting (telemetry, opt-in)**
> - The usage-reporting backend now accepts data only through its own checked endpoint: the public key in the repo can no longer read or write the tables, and a signed-in Supabase user is denied everything. gstack's own test runs never send usage data, test traffic is left out of `gstack-community-dashboard`, and its weekly active count now counts real installs instead of update checks. gstack versions older than v0.11.16.0 (March 2026) stop sending usage data, because they wrote straight to the tables. (#4537)
> - If you opt in, each skill run now also sends nine new fields, each a pick from a fixed list: which coding agent ran it, the model family, whether you, the model or another skill started it, why it ended, whether its own checks passed, whether gstack's routing section and hooks are set up, a random session id, and for upgrades the version you came from and why an upgrade failed. Runs from CI and gstack's own evals label themselves, and a duration gstack couldn't measure is sent empty instead of 0. The opt-in question lists the new fields, and anonymous mode now says it sends "no device ID; a random id per agent session that is never reused". No field carries code, file paths, prompts or repo names; every field is listed in docs/privacy.md. (#4542)
> **Skills and skill suggestions**
> - In Claude Code, each gstack skill's start step now runs while the skill loads, so the model can no longer skip it (in test runs, models had followed a loaded skill's start step in only 45% to 62% of sessions). If loading fails, the skill says so in one line and the model runs the start step itself, as before. Codex and other agents keep the old instructions. (#4509) gstack's paid test that checks this start step now counts one that ran during loading. (#4543)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-25 | [/gstack-ship drops bought extra review rounds and the second-model tr…](https://github.com/garrytan/gstack/commit/ec5d7e6fbd456ffddbc6921ec87d9d1b4ee4cd04) | garrytan |
| 2026-11-25 | [make-pdf: diagrams after a sub-heading keep the full width, and HTML …](https://github.com/garrytan/gstack/commit/e11a5833bc1074fe160bb66670921a77de1d5ab2) | garrytan |
| 2026-11-25 | [make-pdf: bold Swiss-style layout by default, --style plain keeps the…](https://github.com/garrytan/gstack/commit/80fd754fd18ca1cd004c803b6c968875dfde4d0d) | garrytan |
| 2026-11-25 | [/cso refuses npm apps whose installed packages don't match the lockfi…](https://github.com/garrytan/gstack/commit/64fe9e5231047aedbca2d2112535894e16118413) | garrytan |
| 2026-11-25 | [Run newer Claude Code and Codex in CI, and read the Astra model from …](https://github.com/garrytan/gstack/commit/a5acd49d9e45a7a4d866920e91113d122ac66b57) | garrytan |
| 2026-11-25 | [Eval plans can check a code judge against a third model's labels, wit…](https://github.com/garrytan/gstack/commit/2eb3e5ad12a743ed83e0863d670b2e027f6c63a5) | garrytan |
| 2026-11-25 | [Release notes keep quoted versions, count only real changes and print…](https://github.com/garrytan/gstack/commit/47b464a0d4a9f361b7e74f050fd569a49b20078a) | garrytan |
| 2026-11-25 | [Stop the QA-only cleanup test from failing at random on a fast termin…](https://github.com/garrytan/gstack/commit/47189a18e2ce4569a46844d483446b2cc1992b2f) | garrytan |
| 2026-11-25 | [Stop three gstack tests from failing at random in CI (GST-3655) (#4821)](https://github.com/garrytan/gstack/commit/789e9badaa754c666fba0ad18032e7c5dad474d7) | garrytan |
| 2026-11-25 | [Install gstack's shipping skill as /gstack-ship so Claude Code's own …](https://github.com/garrytan/gstack/commit/719b1f59f03e8490abc2c7f727128c96c3ed4fe6) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
