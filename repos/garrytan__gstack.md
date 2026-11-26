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
| ⭐ **Stars** | 142.7k |
| 🍴 **Forks** | 21.1k |
| 🐞 **Open issues + PRs** | [48](https://github.com/garrytan/gstack/issues) |
| 💻 **Languages** | TypeScript 91% · Shell 4% · Go Template 3% · JavaScript 1% |
| 📜 **License** | MIT |
| 🏷 **Topics** | — |
| 🕒 **Last activity** | 2026-11-26 (today) |
| 📅 **Created** | 2026-03-11 |
| 📦 **Latest release** | [v1.104.0.0](https://github.com/garrytan/gstack/releases/tag/v1.104.0.0) — 2026-11-26 |
| 🌿 **Default branch** | `main` |
| 💾 **Size** | 280.9 MB |

## 📦 Recent releases

### [v1.104.0.0](https://github.com/garrytan/gstack/releases/tag/v1.104.0.0) — gstack v1.104.0.0
<sub>2026-11-26 · today</sub>

> **gstack v1.104.0.0**
> **What's new**
> - gstack now picks the newest Opus, Fable, Sol and Astra everywhere it chooses a model. ([#4811](https://github.com/garrytan/gstack/pull/4811))
> - New guide section: you don't need to cut back on MCP servers for accuracy, up to about 300 tools, as long as Claude Code's tool search stays on. ([#4814](https://github.com/garrytan/gstack/pull/4814))
> - /gstack-ship honours a ruled edit after the final review, and a stop on a second-model blocker records. ([#4829](https://github.com/garrytan/gstack/pull/4829))
> - make-pdf's new layout handles three more cases. ([#4828](https://github.com/garrytan/gstack/pull/4828))
> …

### [v1.103.3.0](https://github.com/garrytan/gstack/releases/tag/v1.103.3.0) — gstack v1.103.3.0
<sub>2026-11-25 · yesterday</sub>

> **gstack v1.103.3.0**
> **What's new**
> - A first version's ruled-out line now counts only against the one reply it cites. ([#4800](https://github.com/garrytan/gstack/pull/4800))
> - A first version's plan can say the owner ruled something out, and that line now counts only when he actually said it. ([#4789](https://github.com/garrytan/gstack/pull/4789))
> - /ship's instructions now match how it reviews code. ([#4779](https://github.com/garrytan/gstack/pull/4779))
> **Fixes**
> …

### [v1.103.1.0](https://github.com/garrytan/gstack/releases/tag/v1.103.1.0) — gstack v1.103.1.0
<sub>2026-11-24 · 2d ago</sub>

> **gstack v1.103.1.0**
> **What's new**
> - `/ship` now tells you what to change when GitHub refuses a push for email privacy. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - `gstack-approvals rule` and `round-grant` now say which `--owner-ref` check failed. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - The merge queue's bisect now accepts a red judge case whose name holds a space. ([#4748](https://github.com/garrytan/gstack/pull/4748))
> - /cso reports every security finding the code supports instead of dropping most of them. ([#4739](https://github.com/garrytan/gstack/pull/4739))
> …

### [v1.103.0.0](https://github.com/garrytan/gstack/releases/tag/v1.103.0.0) — gstack v1.103.0.0
<sub>2026-11-23 · 3d ago</sub>

> **gstack v1.103.0.0**
> This release closes gaps in two of gstack's safety checks and its merge tool, fixes the /ship failures that were stopping pull requests from finishing, and renames `/verify` to `/build-check` so Claude Code's own `/verify` works again. Upgrade with `/gstack-upgrade`.
> **Action needed: `/verify` is now `/build-check`**
> - `/verify` is now `/build-check`, so typing `/verify` opens Claude Code's built-in `/verify` again. Use `/build-check` for gstack's build-and-check loop and `/build-check quick` for the check-only pass. (#4714)
> - If you turned the skill off with `disabled_skills: verify`, change that entry to `build-check`. Until you do, gstack reads `verify` as `build-check`, so the skill stays off after you upgrade. (#4719)
> - gstack no longer runs the check pass before every commit on its own, so the `verify_before_commit` setting is retired. Setting it prints a note and changes nothing, and a config file that still has it keeps working. (#4714)
> …

### [v1.102.2.0](https://github.com/garrytan/gstack/releases/tag/v1.102.2.0) — gstack v1.102.2.0
<sub>2026-11-21 · 4d ago</sub>

> gstack 1.102.2.0 fixes two things that broke skills on Codex, stops /plan-tune sending your typed answers to the model without a record, lets large repositories use /ship, makes /office-hours start from ground truth, and moves skill routing out of your CLAUDE.md into the hook that now does that job.
> **Codex**
> - Skills no longer stop on Codex 0.170 when they clean up temporary files: gstack's Codex skills stopped using the `rm -f` form that Codex refuses (67 refusals before, 0 after). (#4612)
> - /review on Codex with OpenAI models no longer fails a review that really ran its security pass. Codex encrypts the message sent to that reviewer, so gstack now recognises the pass from the reviewer it started instead of from the message text. (#4622)
> **Privacy and telemetry**
> - /plan-tune's answer summariser now writes the off-machine send record the README promises before it sends your typed answers to the model, and sends nothing if that record can't be written. A new test fails on any model call that writes no record. Thanks to @robbiesierra for the report. (#4621)
> …

## 🔨 Latest commits

| Date | Change | By |
|---|---|---|
| 2026-11-26 | [Upgrading removes the leftover ship and cso skill folders (GST-3999) …](https://github.com/garrytan/gstack/commit/fd81a04ba7a85d20c8d2134893f45765df5ee578) | garrytan |
| 2026-11-25 | [v1.104.0.0 release (#4840)](https://github.com/garrytan/gstack/commit/e6dd567349e85506127c2f4cf69a0392923c032c) | garrytan |
| 2026-11-25 | [Drop release notes that later changes in this release made outdated (…](https://github.com/garrytan/gstack/commit/fe5aee946fdd6626e09e933dd09bf386853b953e) | garrytan |
| 2026-11-25 | [Remove the /cso security audit skill, since a plain audit request fin…](https://github.com/garrytan/gstack/commit/2fae1d78d60fee5faa6e4503b2a3f5bdba3b4f11) | garrytan |
| 2026-11-25 | [Remove the /cso test files, CI workflows and docs ahead of removing /…](https://github.com/garrytan/gstack/commit/fd7e8c7b3640aeb7caad11aa9d72d2ca22a05971) | garrytan |
| 2026-11-25 | [Let CI results count for /ship without the three /cso jobs being remo…](https://github.com/garrytan/gstack/commit/1145e80a4793cbdd8bd44b635478de81a3e61b71) | garrytan |
| 2026-11-25 | [/careful no longer asks before deleting a file inside another worktre…](https://github.com/garrytan/gstack/commit/a48df18f516c69e0e142d286e60082a55d568230) | garrytan |
| 2026-11-25 | [gstack-pr-wait ignores cancelled checks a newer pass replaced, and th…](https://github.com/garrytan/gstack/commit/8aafd408e21f309f6be6079d047ec7a7934256bd) | garrytan |
| 2026-11-25 | [Stop six gstack tests from failing at random in CI (GST-3852) (#4830)](https://github.com/garrytan/gstack/commit/959df8ccc4b7a5879469743c7076d66e6d0918dd) | garrytan |
| 2026-11-25 | [Skill routing no longer fires on subagent hand-backs or passing menti…](https://github.com/garrytan/gstack/commit/76dd597ff149380f5cdfaa49179211822f64244c) | garrytan |

[See all commits ↗](https://github.com/garrytan/gstack/commits)

## ⬇️ Get it

```bash
git clone https://github.com/garrytan/gstack.git
```
